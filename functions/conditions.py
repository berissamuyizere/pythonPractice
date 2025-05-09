def check_if_even(number):
    if number%2 == 0:
        print(f"{number} is even")




def check_even_or_odd(number):
    if number%2 == 0:
        print(f"{number} is even")

    else:
        print(f"{number} is odd")

def check_divisibility(n):
    for x in range(1, n+1):
        if x%2==0:
            print(f"{x} is divisible by 2")
        elif x%3==0:
            print(f"{x} is divisible by 3")
        elif x%5==0:
            print(f"{x} is divisible by 5")   
        else:
            print(f"{x} is not divisible by 2,3,5")     
               
