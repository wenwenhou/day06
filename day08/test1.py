import re
a=re.compile('\w+@+\w+\.+com')
b=input('请输入您的邮箱')
pl=re.search(a,b)
if pl:
    print('邮箱验证通过')
else:
    print('邮箱验证不通过')


import  re
a=re.compile("\w+@+\w+.+com")
b=input("请输入邮箱:")
pl=re.search(a,b)
if pl:
    print("通过")
else:
    print("不通过")

import re
a=re.compile("\w+@+\w+\.+com")
b=input("请输入你的邮箱")
pl=re.search(a,b)
if pl:
    print("邮箱验证通过")
else:
    print("不通过")


