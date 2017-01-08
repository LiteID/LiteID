import sys
import re

if len(sys.argv) != 2:
	print "Usage:\n\tpython \"navigation-menu-gen.py\" <filename>"
	exit(1)

f = open(sys.argv[1], 'r')
file = f.read()
f.close()
f = open(sys.argv[1], 'w')
try:
	f.write(file.split('menu: | ')[0]+'menu: | \n')
	for m in re.finditer(r"\n[#]+[ ]*(.*?)[ ]*\n", file):
		f.write(" <a href=\"#{}\" style=\"margin-bottom:1px\">{}</a><br>\n".format(m.group(1).strip().replace(' ', '-').lower(), m.group(1).strip()))
	f.write('---'+file.split('---', 2)[-1])
except:
	f.close()
	f = open(sys.argv[1], 'w')
	f.write(file)
	f.close()
	raise