import requests
meta_ip ="192.168.13.131" #Your Metasploitable’s IP can be different
target_website = "http://"+meta_ip+"/mutillidae"
directory=open('dirs.txt','r') #This is an example
# directory="addnews"
for line in directory:
	directory = line.strip()
	url = target_website+"/"+directory
	response = requests.get(url)
	if response:
		print(url)
