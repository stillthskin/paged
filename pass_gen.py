#!/usr/bin/env python3

import string
import random
import smtplib
host = "server.smtp.com"
server = smtplib.SMTP(host)
FROM = "testpython@test.com"
TO = "bla@test.com"



server.quit()
print ("Email Send")

userinput = int(input("Enther password length: "))
sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']
print(dir(string))
def diplayey(lenngth):
	password = ""
	while(len(password)<lenngth):
			char = random.randint(1,4)
			print(char)
			if char == 1:
				password += random.choice(string.ascii_lowercase)
				#password += str(char)
			elif char == 2:
				password += random.choice(string.digits)
				#password += str(char)
			elif char == 3:
				password += random.choice(string.ascii_uppercase)
				#password += str(char)
			elif char == 4:
				password += random.choice(string.hexdigits)
				#password += str(char)
	return password
server.sendmail(FROM, TO, MSG)
MSG = diplayey(userinput)
print(diplayey(userinput))
