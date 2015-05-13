import os
import sys
from os import path

def remove_unicode(string):
	return ''.join(i for i in string if ord(i)<128)

def sanitize(body):
	body = body.replace('\\', '\\\\')
	body = body.replace('\r','')
	body = body.replace('\n', '\\n')
	body = body.replace('\"', '')
	body = body.replace('\'', '')
	for i in range(0, 32):
		body = body.replace(chr(i), '')
	body = body.replace('/', '\\/')
	body = remove_unicode(body)
	return body


with open('faculty.txt') as f:
	lines = f.readlines();
	lines = [line.rstrip('\r\n') for line in lines]
	mapping = []
	for line in lines:
		line_list = line.split('|')
		mapping.append((line_list[0], line_list[1:]))
	prof_dict = dict(mapping)

with open('expertsearch_bulk_prof_only_uiuc.txt', 'wb') as out:
	for f_name in os.listdir('docs_uiuc_merged/'):
		line1 = '{ "create": { "_index": "expertsearch_index_prof_only_uiuc", "_type": "doc"}}'
		with open('docs_uiuc_merged/' + f_name, 'r') as f:
			doc_id = sanitize(f_name)
			body = ''.join(f.readlines())
			body = sanitize(body)
		prof_name = doc_id[:-4]
		prof_email = prof_dict[f_name[:-4]][0]
		prof_pos = prof_dict[f_name[:-4]][1]
		prof_dept = prof_dict[f_name[:-4]][2]
		prof_email = sanitize(prof_email)
		prof_pos = sanitize(prof_pos)
		if 'professor' in prof_pos.lower():
			prof_dept = sanitize(prof_dept)
			line2 = '{"doc_id": "' + doc_id + '", "professor": "' + prof_name + '", "email": "' + prof_email + '", "position": "' + prof_pos + '", "dept": "' + prof_dept + '", "body": "' + body + '"}'
			out.write(line1)
			out.write("\n")
			out.write(line2)
			out.write("\n")
