import os,sys
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

files = [f for f in os.listdir('docs_uiuc/')]
with open('faculty.txt', 'r') as f:
	faculty = f.readlines()
fac_list = [fac.split('|')[0] for fac in faculty]
for fac in fac_list:
	for f in os.listdir('docs_uiuc'):
		if f.startswith(fac):
			with open('docs_uiuc_merged/' + fac + '.txt', 'a') as out:
				contents = open('docs_uiuc/' + f).read()
				out.write(contents + '\n')
