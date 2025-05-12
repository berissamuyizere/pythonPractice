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

str = "munezer"
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
