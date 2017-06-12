#!/usr/bin/python
import os,time

print "\n\t\t\tSoftware As A Service Cloud Menu::::\n"

print "\t 1. FireFox Service \n"
print "\t 2. GEdit Service \n"
ch=raw_input()

if ch=='1':
	print "\nEnjoy The FireFox Services...."	
	os.system('firefox')
	os.system('clear')
	execfile('saas.py')
elif ch=='2':
	print "\nEnjoy The GEdit Services...."	
	os.system('gedit')
	os.system('clear')
	execfile('saas.py')
else:
	print "Incorrect Choice. Please re-enter Your Choice...\n\n\n\n"
	time.sleep(5)
	os.system('clear')	
	execfile('saas.py')
