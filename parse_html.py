#Parses the raw html found at http://illinois.edu/ds/facultyListing that has all of the faculty at UIUC in a giant div.

from bs4 import BeautifulSoup

with open('raw.html', 'r') as f:
	raw_data = f.read()
	soup = BeautifulSoup(raw_data)
	main_nav_div = soup.find('div', {'id': 'col-2'})
	ws_a_z_div = main_nav_div.find('div', {'id': 'ws-a-z'})
	dept_details_div = ws_a_z_div.find('div', {'class': 'ws-ds-dept-details ws-a-z-dept-details'})
	depts = dept_details_div.find_all('h4')
	uls = dept_details_div.find_all('ul')
	print "name|email|position|department"
	for x in range(0,40):
		dept = depts[x].find_all('a')[1].get_text()
		lis = uls[x].find_all('li')
		for li in lis:
			prof_name = li.find('a').get_text()
			href = li.find('a')['href']
			prof_email = href[7 + href.index('search='):]
			prof_position = ''
			if li.find('span') is not None:
				prof_position = li.find('span').text
			print prof_name + "|" + prof_email + "|" + str(prof_position) + "|" + dept
