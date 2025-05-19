def total_inventory(ArrProduct):
    totalPrice = 0
    for product in ArrProduct:
        productPrice=  product["price"]*product["quantity"]
        totalPrice+=productPrice
        
    return totalPrice

ArrProduct = [{"name":"rice", "price": 600, "quantity": 20},{"name":"cake", "price": 800, "quantity": 10},{"name":"maize", "price": 190, "quantity": 20}]
print(total_inventory(ArrProduct))


def balanced_str(str):
    vowels = ["a", "i","o","u", "e"]
    vowelCout =0
    consoCount =0
    for char in str:
        if char in vowels:
            vowelCout+=1
        else:
            consoCount+=1   
    return vowelCout == consoCount

str = "munezero"
print(balanced_str(str))

def print_num(x):
    for i in x:
        # print(i)
        print(i%7)


x= [10,20,30,40]
print_num(x)

def list_traversal(y):
    b = []
    for num in y:
        for i in num:
            print(i)
            b.append(i)
    print(b)


y = [[1,2,3],[4,5,6],[7,8,9,10]]
list_traversal(y) 

def list_complehension(x):
    print([i**3 for i in x])
    print([i%9 for i in x])

x =[1,2,3,4,5]
list_complehension(x)   

def two_lists(z):
    new= len(z)//2
    print([i*3 for i in z[:new]])
    print([i*3 for i in z[new:]])

z = [0,1,2,3,4,5,6,7,8,9]
two_lists(z)

def set_methods(numbers):
    for i in numbers:
        print(i)
numbers = {10,30,20,60,40,20}
set_methods(numbers) 

def perfect_number(number):
    sum = 0
    for i in range(1, number):
        if number%i == 0:
            sum+=i

    return sum == number        

print(perfect_number(28))

def factorial(n):
    if n== 0:
        return 1
    return n * factorial(n-1)
print(factorial(7)) 

def case_string(string):
    lower =0
    upper=0
    for char in string:
        if char.isupper():
            upper+=1
        else:
            lower+=1
    return [lower , upper]
print(case_string("AnaLogE"))


# def student_details(students):
    # sortedstudents = sorted(students["score"])
#     scores = []
#     for student in students:
#         student["score"]
#     sortedscore = sorted(scores)

# students = [{"name": "Queen", "score": 60}, {"name": "Joyline", "score": 70}, {"name": "Keza", "score": 50}, {"name": "Jimmy", "score": 90}]  
# student_details(students)

