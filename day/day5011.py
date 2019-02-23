num=int(input("请输入一个数:"))
f=1
if num<0:
    print("负数没有阶乘")
elif num==0:
    print("0的阶乘为1")
else:
    for i in range(1,num+1):
        f=f*i
    print("%d的阶乘为%d" %(num,f))