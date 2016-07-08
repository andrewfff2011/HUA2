import re

s = re.search("^A", "A big fat cat ate a rat")

if s:
	print "Yes"
else:
	print "No"
