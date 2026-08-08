def hi(func):
    def wrapper():
        print("start..")
        func()
        print("..stop")
    return wrapper

@hi
def hello():
    print("hello world")

hello()