import re
with open("C:\\Users\ADMIN\Desktop\Zindua Bootcamp\Python\engdict.py", "r") as f:
    s = f.read()
#words with ing
    #result = re.findall(r'\w(\w+ing)\w',s)
    #for r in result:
        #print(r)
#starts with s
    #result = re.findall(r'[s]\w+', s)
    #for r in result:
     #   print (r)
#starts with t
    result = re.findall(r'[t]\w+', s)
    for r in result:
        print (r)



