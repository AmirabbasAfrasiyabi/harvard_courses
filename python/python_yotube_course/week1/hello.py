"""print"""
# print("Hello, world")


"""add_input"""
def main():
    # inp = input("Hello , what is your names -> ").strip().title()
    num = int(input("How many students do you want to study -> "))
    abas = square(num)
    print(abas)

def square(num):
    number = num * num
    return number
main()


"""rounding"""
# x = int(input("First_Number ->"))
# y = float(input("Second_Number ->"))
# z = round((x+y))
# print(type(z))
# print(f"{z:.2f}")
#
# q = x/y
# print(f"{q:.2f}")

