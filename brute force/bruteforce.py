import zipfile 
 
filename = 'secret.zip' 
dictionary = 'dict.txt' 
 
password = None 
file_to_open = zipfile.ZipFile(filename) 
with open(dictionary, 'r') as f: 
   for line in f.readlines(): 
         password = line.strip('\n')
         #password = b'%s' % password
         try:
               file_to_open.extractall(pwd=password.encode()) 
               password = 'Password found: %s' % password 
               print(password)
               break
         except: 
               pass 
