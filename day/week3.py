import  random
list=[]
for i in range(20):
   num= random.choice(range(10))
   list.append(num)
list[::2]=sorted(list[::2],reverse=False)
print(list)

