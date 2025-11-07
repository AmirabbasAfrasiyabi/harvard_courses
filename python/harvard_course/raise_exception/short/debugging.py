"""debugging mario"""
# def main():
#     height = int(input("Height : "))
#     pyramid(height)

# def pyramid(n):
#     for i in range(n):
#         print((i + 1),end="  ")
#         print("#" * (i + 1))

# if __name__ == "__main__":
#     main()


"""Handle exception"""
# distance = {
#     "tehran" : "134 Au",
#     "karaj" : "134",  # type: ignore
# }

# def main():
#     spacecraft = input("Enter a spacecraft: ")
    
#     try:
#         au = float(distance[spacecraft])

#     except KeyError:
#         print(f"{spacecraft} is not in dictionary")
#         return
    
#     except ValueError:
#         print(f"Cant convert{distance[spacecraft]}to a float")
#         return
    
#     m= convert(au)
#     print(f"{m} is away")

# def convert(au):
#     return au * 12345

# main()


"""Raise Exception"""
def main():
    pace = get_pace(miles = 26.2 , minute = 0)
    print(f"You need to run each mile in {round(pace,2)} minute")

def get_pace(miles,minute):
    if not minute >0:
        raise ValueError("value is not good , invalid value")
    return minute /miles

main()