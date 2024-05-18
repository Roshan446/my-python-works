def addition(*args):
    return sum(args)
print(addition(10,20,30,50,80,40))

def product(*args):
    n1 = 1
    for n in args:
        n1*=n
        print(n1)
product(2,4) 


# def last_digit_sum(*args):
#     r=0
#     for n in args:
#         r += (n%10)
#         print(r)
# last_digit_sum(105,205,705)

def last_digit_sum(*args):
    return sum(n%10 for n in args)
print(last_digit_sum(105,105,705))


def last_digit_max(*args):
    return max(n%10 for n in args)

print(last_digit_max(10.50,98,99))

def add_employe(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("salary"))
    print(kwargs)
add_employe(id = 4582, name = "hari", place = "ekm", job_destination = "tvm", salary= 48000000000000)


def last_digit_sort(*args, **kwargs):
    digits = [n%10 for n in args]
    value = kwargs.get("reversed")
    if value == True:
        digits.sort(reverse=True)
    else:
        digits.sort(reverse=False)
    return digits

print(last_digit_sort(1,9,8,7,12,55,89,94, reversed = True))

