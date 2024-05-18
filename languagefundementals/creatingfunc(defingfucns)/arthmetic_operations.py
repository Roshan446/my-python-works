def add(n1, n2):
    res = n1 + n2
    return res
def sub(n1,n2):
    res = n1-n2
    return res
def multi(n1,n2):
    res = n1*n2
    return res

def div(n1, n2):
    res = n1/n2
    return res
print(div(10,5))
print(add(10,5))
print(sub(10,5))
print(multi(10,5))

def smart_sub(n1,n2):
    res = n1-n2 if n1>n2 else n2-n1
    return res
print(smart_sub(5,10))
print(smart_sub(10,5))