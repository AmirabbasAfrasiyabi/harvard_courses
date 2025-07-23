#int

"""x = int(input("whats X ->"))
y = int(input("Whats Y ->"))
print(f"final result {x+y}")
"""
# print("--------------------")

#float

"""x = float(input("whats X ->"))
y = float(input("Whats Y ->"))
z = round(x / y)
print(f"final result {x+y}")
print(f"final random  {z:.2f}")
"""

#function
"""
def main():
    x = int(input())
    print("x square is ->" ,square(x))

def square(n):
    return n*n
main()
"""


#function area example 
def area(length,width):
    return length * width

def main():
    house = area(50,30)
    yard = area(50,50)
    total = house + yard
    print(str(total) + " total square feet")
main()
