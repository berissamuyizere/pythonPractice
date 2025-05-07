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



def year_of_birth(name, age):
    year = 2025 - age
    print(f"Hello {name}, born in {year}")

# year_of_birth("Jane", 21)

def my_country(name="Uganda"):
    print(f"I love my country {name}")

# my_country()

def welcome_student(**kwargs):
    print(kwargs.values)

def create_sentence(**words):
    sentence = " "
    for word in words.values():
        sentence+= word
        sentence += " "
    return sentence

def exam_result (*args, **kwargs):
    if not args:
        name = kwargs["name"] if "name" in kwargs else "Student"
        print(f"Hello {name}, you have no scores recorder for backend")
        return
    total=0
    for arg in args:
            total+= arg
    average = total/len(args)
    name = kwargs["name"] if "name" in kwargs else "Student"
    print(f"Hello {name}, your average score for backend is {average}")


