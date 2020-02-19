'''
import re,urllib
import urllib.request

data=urllib.request.urlopen("https://www.aptransport.org/html/aboutus-contactdirectory-deputytransportcommissioner.html")
text=data.read()
numbers=re.findall("[0-9-]{7}[0-9-]+",str(text),re.I)
for n in numbers:
        print(n)
'''
'''
import re,urllib
import urllib.request

data=urllib.request.urlopen("https://www.aptransport.org/html/aboutus-contactdirectory-deputytransportcommissioner.html")
text=data.read()

#num=re.findall("[0-9-]{7}[0-9-]+",str(text),re.I)
email=re.findall("[0-9a-zA-Z_]+@aptransport.org",str(text),re.I)
#print(email)
for i in email:
    print(i)
'''
'''
print(num)

for x in num:
    print(x)
'''

'''
import re,urllib
import urllib.request

data=urllib.request.urlopen("https://www.redbus.in/info/contactus")

text=data.read()

num=re.findall("[0-9-]{7}[0-9-]+",str(text),re.I)

for x in num:
    print(x)
''' 
# Global Variables
x=10
def hii():
    print(x)
    y=20
    print(y,'this is local variables')
    
def hello():
    print(x)
    print(Y) #this is not support because of local variables

hii()
hello()























