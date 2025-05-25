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
               
def fizz_buz(number):
    for i in range(1, number):
        if i%3 ==0 and i%5 ==0:
            print("FizzBuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")


def count_down(start):
    while start >=0:
        print(f"count down at {start}")
        start -=1

# count_down(20)
def count_down_with_break(start, stop):
    while start>=0:
        print(f"count down counting at {start}")
        if start == stop:
            print(f"stopping at {stop}")
            break
        start -=1
                 

def count_down_with_odd_numbers(start):
    while start >=0:
        if start%2 ==0:
            start -=1
            continue
        print(f"count down at {start}")  
        start -=1  


def print_even():
    num = 0
    while num < 100:
        num+=1
        if num%2 !=0:
            continue
        print(f"{num} is even")