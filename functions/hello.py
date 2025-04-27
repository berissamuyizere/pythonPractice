def hello():
    print("Hello Akirachix")


def sayHello(name):
    print(f"hello {name}")


# sayHello()

def greet(name, age):
    year = 2025 -age
    print(f"hello {name}, born in {year}")
# greet() 

def greetings(names):
    for name in names:
        print(f"hello {name}")