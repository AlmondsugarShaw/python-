n1=int(input("第一列的宽度"))
n2=int(input("第二列的宽度"))
n3=int(input("第三列的宽度"))
def createH(n1,n2,n3):
    str="┌"+"─"*n1+"┬"+"─"*n2+"┬"+"─"*n3+"┐"
    return str
def createM(n1,n2,n3):
    str="├"+"─"*n1+"┼"+"─"*n2+"┼"+"─"*n3+"┤"
    return str
def createB(n1,n2,n3):
    str="└"+"─"*n1+"┴"+"─"*n2+"┴"+"─"*n3+"┘"
    return str
print(createH(n1,n2,n3))
print(createM(n1,n2,n3))
print(createB(n1,n2,n3))
