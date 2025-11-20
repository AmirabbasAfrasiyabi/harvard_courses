"""حلقه های تکرار"""

#while loop
# i = 0
# while True:
#     print("Hi")
#     print(i+1)
#     i += 1
#     if i == 100:
#         break
# print("Finished")

#for loop
# for i in range (1,101,1):


"""even and odd digits"""
    # if i % 2 ==0 :
    #     print (f"{i} is even")
    # else:
    #     print (f"{i} is odd")


"""only even digit"""
    # if i % 2 == 0:
    #     print(i)


"""print 5 hi"""
# import time
# for _ in range (5):
#     print("hi")
#     time.sleep(3)
#     print(_)


"""list """

"""solution1"""
# student = ["amir" , "ati" , "rey" , "Hamide" , "mansor"]
#
# for i in range (len(student)):
#     print(i+1 , student[i])
#
# for i in student:
#     print(i)
#
# student.append("Abbas")
# print(student)

"""solution2"""
# std = []
# a = int(input("How many integer?"))
# for i in range(a):
#     std.append(input("Enter number: "))
# print(std)


"""dictionary"""

d = {"Amir" : "09120910309" ,
     "Ati" : "09120034660" ,
     "Reyhan" : "091269931119" ,
     "Mansor" : "09128433591" ,
     "Hamide" : "09120781057"
     }
print(d)
for i in d :
    print(i , d[i] , sep = " : ")

for i in d.items():
    print(i)


