#!/usr/bin/python

import os,time,getpass

print " Please Enter The Credentials:::\n\n"

u_name=raw_input("Username:\t")
passwd=getpass.getpass("Password:\t")

if u_name=='root' and passwd =='redhat':
	print "Login Accepted. Please Wait."
	time.sleep(5)
	os.system('clear')
	execfile('choice.py')
else:
	print "Not Authorized. Please Check Credentials and Re-enter them....\n\n\n\n"
	time.sleep(5)
	os.system('clear')
	execfile('login.py')


