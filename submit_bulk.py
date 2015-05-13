from elasticsearch import Elasticsearch
import timeit

NUM_BULKS = 30 
bulk_data = [[] for x in xrange(NUM_BULKS)]
ES_HOST = {"host" : "localhost", "port" : 9200}
INDEX_NAME = "expertsearch_index_uiuc"
curr = 0
print "Creating bulks..."
with open('expertsearch_bulk_uiuc.txt', 'r') as f:
	while True:
		line1 = f.readline().rstrip()
		line2 = f.readline().rstrip()
		line1 = ''.join(i for i in line1 if ord(i)<128)
		line2 = ''.join(i for i in line2 if ord(i)<128)
		bulk_data[curr % NUM_BULKS].append(line1)
		bulk_data[curr % NUM_BULKS].append(line2)
		curr += 1
		if not line2:
			break
print str(len(bulk_data[0]))
es = Elasticsearch(hosts = [ES_HOST])

# since we are running locally, use one shard and no replicas
request_body = {
	"settings" : {
		"number_of_shards": 1,
		"number_of_replicas": 0
	}
}

curr = 0
total = 0
for curr_bulk in bulk_data:
	print("bulk indexing... " + str(curr) + " of size " + str(len(curr_bulk)))
	start = timeit.default_timer()
	res = es.bulk(index = INDEX_NAME, body = curr_bulk, refresh = True)
	bulk = open('bulk.log', 'w')
	bulk.write("response: " + str(res))
	elapsed = timeit.default_timer() - start
	total += elapsed
	curr += 1
print "Using " + str(NUM_BULKS) + " bulks of size " + str(len(bulk_data[0] )) + " took " + str(total)
