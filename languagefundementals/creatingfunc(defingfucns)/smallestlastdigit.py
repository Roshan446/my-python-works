def smallest_lastdigit(n1,n2):
    if n1%10 > n2%10:
        return n2
    else:
        return n1
print(smallest_lastdigit(4005,289))