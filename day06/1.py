f=open("d://aa.txt","w")
f.write("你好我的世界")
f.close()
d=open("d://aa.txt","r")
b=d.read()
c=open("d://bb.txt","w")
c.write(b)
print(b)

