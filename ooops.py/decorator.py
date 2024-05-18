def swap_num(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper

@swap_num
def div(n1,n2):
    return n1/n2
@swap_num
def sub(n1,n2):
    return n1-n2

print(div(4,10))



def hello(fn):
    def wrapper(user):
      data = f"hello! {fn(user)}"
      return data
    return wrapper
@hello
def greeting_mrng(user):
    return f"good morning {user}"
@hello
def greeting_aft(user):
    return f"good afternoon {user}"
@hello
def greeting_evng(user):
    return f"good evening {user}"


print(greeting_mrng("hari"))


def symbol(fn):
    def wrapper():
        data =  f"<> {fn()} <>"
        return data
    return wrapper
@symbol
def get_hello():
    return "hello"
@symbol
def get_hai():
    return"hai"

print(get_hai())



