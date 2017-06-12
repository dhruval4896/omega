#!/usr/bin/python

import os,time

print " Welcome User....\n\n"
print " \t\t\t-:Menu:-\n"

print "\t 1. Software As A Service Cloud ( SAAS )\n"
print "\t 2. Storage As A Service Cloud ( STAAS )\n"

ch=raw_input (" \nPlease Enter Your Choice:::\t")

if ch=='1':
	print "\nEntering Software As A Service CLOUD Menu... Please Wait."
	time.sleep(5)
	os.system('clear')
	execfile('saas.py')
elif ch=='2':
	print "\nEntering Storage As A Service CLOUD Menu... Please Wait."
	time.sleep(5)
	os.system('clear')	
	execfile('staas.py')
else :
	print "\nInvalid Choice Entered .Please re-enter the choice:\n\n\n\n"
	time.sleep(5)
	os.system('clear')
	execfile('choice.py')


