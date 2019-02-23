import  random
list=[]
for i in range(50):
    num=random.choice(range(-10,10))
    list.append(num)

print("list长度:",len(list))

z=[]
f=[]

for i in list:
    if i>0:
        z.append(i)
    elif i<0:
        f.append(i)
print("正数",z)
print("负数",f)
