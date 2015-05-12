# Uses Bing's search api to get the top 50 results of each faculty member
import time
import urllib2
from py_bing_search import PyBingSearch

f = open('faculty.txt', 'r')
fac_list = f.readlines()[1:]
fac_crawled = open('fac_crawled.txt', 'r')
fac_crawled_str = fac_crawled.read()
fac_crawled.close()
fac_crawled = open('fac_crawled.txt', 'a')

bing = PyBingSearch('4PHFvYjEsakSe/xoDxWVuzBp2ok/+3ZZHT6CQdE1XE0')
for fac in fac_list:
	fac_info_list = fac.rstrip('\r\n').split('|')	
	prof_name = fac_info_list[0]
	if prof_name not in fac_crawled_str:
		fac_file = open('faculty_urls/' + prof_name + '.txt', 'w')
		print "Googling " + prof_name
		result_list, next_uri = bing.search(prof_name, limit=50, format='json')
		for i in range(0, len(result_list)):
			fac_file.write(result_list[i].url.encode('utf8') + '\n')
		print "Completed Googling " + prof_name
		fac_crawled.write(prof_name + '\n')
