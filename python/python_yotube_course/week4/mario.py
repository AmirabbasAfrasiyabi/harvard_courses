# print("#")
# print("#")
# print("#")

"""other solution"""
# for i in range(3):
#     print("#")

"""another solution"""
# def main():
#     draw(3)
#
# def draw(n):
#     for _ in range(n):
#         print("#")
# main()


"""Example 2"""
"""square n * n"""
# def main():
#     while True:
#         n = int(input())
#         if n > 0:
#             break
#     square(n)
#
# def square(n):
#     for i in range(n):
#         print(n * "#")
# main()


"""Example 2"""
"""heram"""
def main():
    while True:
        n = int(input())
        if 0 < n < 10:
            break
    square(n)

def square(n):
    for i in range(1,n+1):
        print(i * "#")
main()