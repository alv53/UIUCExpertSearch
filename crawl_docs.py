#Uses the urls obtained from get_urls.py to crawl the n documents related to the faculty member
import os, urllib2, socket, sys

#For now using top 5 documents
n = 5

f = open('fac_downloaded.txt', 'r')
f_downloaded = f.read()
f.close()
fac_downloaded = open('fac_downloaded.txt', 'a')

for prof_txt in os.listdir(os.getcwd() + '/faculty_urls'):
	prof_name = prof_txt[:prof_txt.index('.txt')]
	if prof_name not in f_downloaded:
		print "Crawling for " + prof_name
		f = open('faculty_urls/' + prof_txt)
		urls = f.readlines()
		successes = 0
		for i in range(0,len(urls)):
			url = urls[i].rstrip('\r\n')
			if url.endswith('pdf'):
				print "Skipped " + str(i) + " because it was a pdf"
			if not url.endswith('pdf'):
				file_name = 'docs/' + prof_name + '-' + str(successes) + '.txt'
				curr = open(file_name, 'w')
				attempts = 0
				while attempts < 3:
					try:
						r = urllib2.urlopen(url, timeout=5)	
						curr.write(r.read())
						print 'Success on: ' + prof_name + ' ' + str(i) + ' | ' + url
						successes += 1
						break
					except urllib2.URLError as e:
						print 'urllib2 FAILURE on: ' + prof_name + ' ' + str(i) + ' | ' + url
						attempts += 1
					except socket.timeout, e:
						print 'socket FAILURE on: ' + prof_name + ' ' + str(i) + ' | ' + url
						attempts += 1
			i += 1
			if successes >= n:
				break
		if successes < n:
			sys.exit()
		fac_downloaded.write(prof_name + '\n')
		f.close()
