import itertools

#dictionary = 'websites.txt'
list10 = ['test1','test2','test3','']
list11 = ['test1','test2','test3','']
list12= ['test1','test2','test3','']

list13 = ['tests']

list2= ['st','ts','te','et','','tst','sts']
list3 = ['.online','.com','.net','.xyz']
mid_dom = [list10,list11,list13,list12,list2,list3]

file = open("websitelist.txt", "w")

listtt = []
for combM in dict.fromkeys(list(itertools.product(*mid_dom))):
    MD_list = listtt.append(''.join(list(dict.fromkeys(combM))))
    MD_list

print(list(dict.fromkeys(listtt)))
for i in list(dict.fromkeys(listtt)):
    file.write(''.join(i)+"\n")

file.close()
