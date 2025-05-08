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