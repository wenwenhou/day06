numbers=[1,5,-12,37,6,93,100]
even=[]
odd=[]

for i in range(len(numbers)):
    if (numbers[i]%2==0):
        odd.append(numbers[i])
    else:
        even.append(numbers[i])
print("奇数",even)
print("偶数",odd)



