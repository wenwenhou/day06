# 通过用户输入数字，计算阶乘。
print('请输入一个数字')
a = int(input())
print('请输入阶乘')
b = int(input())
print('结果是', a ** b)


# 判断101-200之间有多少个素数，并输出所有素数
a = []
b = []
for i in range(100, 201):
    for j in range(2, i):
        if i % j == 0:
            a.append(i)
            break
        else:
            b.append(i)
            break
print('素数有L', a)
print('不是素数的有', b)


# 将一个列表的数据复制到另一个列表中，并反向排序输出。
a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
b = []
# 把a 复制到b
for i in range(len(a)):
    b.append(a[i])
print('结果', b)
b = sorted(b, reverse=False)
print('排序后结果是', b)

a=[1,9,6,3,8,7,2,4,9]
b=[]
for i in range(len(a)):
    b.append(a[i])
print(b)
b=sorted(b)
print(b)
a=16
print(a>>2)