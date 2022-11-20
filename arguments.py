def greet_multiple(*number, **students):
    num=1
    for number in numbers:
        num*=number
        print(num)
        print(f"Hello {students}")
    