num=int(input("请输入一个数"))#输入一个数求它的阶乘
f=1#赋值一个数为1 最后求出阶乘结果
if num<0:
    print("负数没有阶乘")#输出的数小于0，则提示没有结果
elif num==0:
    print("0的阶乘为1")#输出的数等于0，则提示结果为1
else :
    for i in range(1,num+1):#从1开始到num+1的前一项
        f=f*i#从
