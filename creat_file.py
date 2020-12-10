import os
import random
size=float(input("Nhập dung lượng file (MB) :"))
while (size > 1024) or (size < 1):
    size=float(input("Nhập dung lượng file (MB) :"))
print('Loading...')
kb=size*1024
number=int(kb/1000)
list=[]
for i in range(0,number):
    a=str(i)
    name='file' + a + '.txt'
    list.append(name)
for i in range(0,number):
    f = open(list[i],'w+')
    data=str(random.randint(0,10))
    f.write (data)
    f.close
    b=os.path.getsize(list[i])
    while (b < 1024000):
        f = open(list[i],'a+')
        data=str(random.randint(0,10))
        f.write (data)
        f.close
        b=os.path.getsize(list[i])

        
        
    

