import sys, hashlib, getpass

def get_hashed_text(text:str):
    return hashlib.sha256(text.encode()).hexdigest()

while 1:
   key = getpass.getpass('[+] Enter key: ')
   if get_hashed_text(key) != '477a4494a9b8bd2e6ad0eeeb6ecd6aa7d16a5b5f161c954d76b96a7eb311325c':
      sys.stderr,write(f'your given key "{key}" is incorrect.\n')
   
   else:
       break
	   
# Our main function 
print('Hello there!')
print('Welcome to this SMS BOMBEING TOOL👹👹,')
print('You are seeing this because you passed the key verification')

#---------{ ADMIN INFO }----------
# AUTHOR   :RAFIN KHAN
# TEAM   AUTHOR : RAFIN
#-------------------------------- 

import sys
import time
import os
import requests
import smtplib

os.system("xdg-open https://www.facebook.com/profile.php?id=100080364354863&mibextid=ZbWKwL") 
os.system("clear")
def slw(l):
  for i in l:
    sy
