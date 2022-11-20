from unicodedata import name


def greet(name):
    if name == "Claire":
        print("You smell like pickles")
        return
    print("Hey there")
    print("Welcome, " + name)


name = "Caleb"
greet(name)
greet("Swabrina")
greet("Noni")
greet("Claire")