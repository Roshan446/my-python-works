def smallest_digit(n1, n2):
    s1 = sorted(str(n1))
    s2 = sorted(str(n2))
    res = "{n1} has smallest 1st digit" if s2[0] >s2[0] else "{n2} has the smallest 1st digit"
    return res
print(smallest_digit(450,1250))
