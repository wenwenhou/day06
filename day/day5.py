def function(n):
    if n==1:
        return 1
    else:
        Error as e:
        print("error", e)
        return n*function(n-1)
num=input()
try:
    with open("jc.txt","w") as file:
        file.write(str(function(int(input(num)))))
except IO