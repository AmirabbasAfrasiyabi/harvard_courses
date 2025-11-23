"""example 1"""
# nums = []
# for _ in range(3):
#     nums.append(input("whats your name ->"))
# for name in sorted(nums):
#     print(f'hello {name}')

"""example 2"""
# name = input("Enter your name: ")
# file = open("file.txt", "w")
# file.write(name)
# file.close()

"""example 3"""
# name = input("Enter your name: ")
# with open("file.txt", "a") as file:
#     file.write(f"{name}\n")


"""example 4"""

with open("file.txt") as file:
    lines = file.readlines()
for line in lines:
    print("hello" , line.rstrip())