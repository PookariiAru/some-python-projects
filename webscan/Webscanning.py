import requests

dictionary = 'websitelist.txt'
 
url = None 
with open(dictionary, 'r') as f: 
   for line in f.readlines(): 
         url = line.strip('\n')
         try:
               response = requests.get('http://' + url)
               print(url + " exsists")
         except requests.ConnectionError as exception:
             pass 
