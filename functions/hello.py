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
    print(kwargs.values())  # fixed

welcome_student(name="Berissa", age=24)

def create_sentence(**words):
    sentence = ""
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence

print(create_sentence(word1="Hello", word2="there", word3="Berissa!"))

def exam_result(*args, **kwargs):
    if not args:
        name = kwargs["name"] if "name" in kwargs else "Student"
        course = kwargs["course"] if "course" in kwargs else "the course"
        print(f"Hello {name}, you have no scores recorded for {course}")
        return
    total = sum(args)
    average = total / len(args)
    name = kwargs["name"] if "name" in kwargs else "Student"
    course = kwargs["course"] if "course" in kwargs else "the course"
    print(f"Hello {name}, your average score for {course} is {average}")


exam_result(80, 90, 70, name="Berissa", course="Math")

exam_result(name="Berissa", course="Science")










