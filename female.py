str1=input("enter the input string")

count1=0
count2=0
l1=list(str1)

for i in range(len(l1)):
    if(l1[i]=='f'):
        count1+=1
    else:
        count2+=1
dict1={}
dict1['f_count']=count1
dict1['m_count']=count2
print(dict1)
l2=[]
for i in range(count1):
    l2.append('f')
for i in range(count2):
    l2.append('m')
str2=''.join(str(i) for i in l2)  
print(str2)
