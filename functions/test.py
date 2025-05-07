def total_inventory(ArrProduct):
    totalPrice = 0
    for product in ArrProduct:
        productPrice=  product["price"]*product["quantity"]
        totalPrice+=productPrice
        
    return totalPrice 

ArrProduct = [{"name":"rice", "price": 100, "quantity": 20},{"name":"cake", "price": 200, "quantity": 10},{"name":"maize", "price": 190, "quantity": 20}]
print(total_inventory(ArrProduct))