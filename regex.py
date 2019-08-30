import re
#the email regex
email_reg=re.compile('[a-zA-Z0-9]+')
#testing it out
print(email_reg.match("chrisngure2599"))
#the functions to test out everything
#@ A set of characters soc
def soc(word):
	#1st compiling
	soc=re.compile('[0-9a-zA-Z ]+')
	#2nd matching
	print(soc.match(word))
soc("Your text")
