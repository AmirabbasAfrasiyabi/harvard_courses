# def main():
#     spacecraft = {
#         "name":"Amirabbas",
#         "distance":"163",}
    
#     #update
#     spacecraft["distance"] = "150"
#     spacecraft["name"] = "Atiye"
#     print(create_report(spacecraft))


# def create_report(spacecraft):
#     return f"""
# ==============REPORT=====================

# Name: {spacecraft["name"]}
# Distance: {spacecraft["distance"]}

# =========================================
# """
# main()


"""Example 2"""
# distance = {
#     "value1":163 , 
#     "value2":136,
#     "value3":150,
#     "value4":123,
#     "value5":180,
# }

# def main():
#     for name in distance.keys():
#         print(f"{name} is {distance[name]} AY from EARTH" )
# main()




"""dictionary method"""

word = {
    "PAIR":4,
    "HAIR":3,
    "CHAIR":5 , 
    "GRAPHICS":7
}
def main():
    print('welcome to Spelling Bee !')
    print("Your letter are : A I P C R H G")

    while len(word) > 0:
        print(f"{len(word)} words left !")
        guess = input("Guess a word:")
        if guess == "GRAPHICS":
            word.clear()
            print("You are Won")
        if guess in word.keys():
            points = word.pop(guess)
            print(f"Good job! Your scored {points} points")
    print("That is the game")

main()