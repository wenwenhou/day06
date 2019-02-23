iphone=input("请输入手机号:")
list=[135,156,157,166,177]
try:
    int(iphone)
    if (len(iphone)==11):
        heard=iphone[0:3]
        bool=False
        for i in list:
            if int(heard)==i:
                bool=True
                break
        if(bool):
            print("有效手机号:")
        else:
            print("无效手机号")
    else:
        print("不是手机号")
except ValueError:
    print("输入的不是有效手机号")
