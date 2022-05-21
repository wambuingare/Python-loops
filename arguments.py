def greet_multiple(*args,**kwargs):
    num=1
    for x in args:
        num*=x
        print(num)
        print(f"hello{kwargs}")
    