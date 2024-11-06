"""459. Repeated Substring Pattern"""


s = "aaaaa"
if len(s)==1:
    print("false")
else:
    ss = (s+s)[1:-1]
    print(ss.find(s)!=-1)


