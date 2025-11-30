"""example 1"""
# nums = []
# for _ in range(3):
#     nums.append(input("whats your name ->"))
# for name in sorted(nums):
#     print(f'hello {name}')


"""example 2 -> write a file with w method """
# name = input("Enter your name: ")
# file = open("file.txt", "w")
# file.write(name)
# file.close()

"""example 3 -> write any example  -> not good"""
# name = input("Enter your name: ")
# file = open("file.txt", "a")
# file.write(f"{name}\n")
# file.close()


"""example 4 -> solve problem example3 -> 1- write with and delete line 19"""
# name = input("Enter your name: ")
# with open("file.txt", "a") as file:
#     file.write(f"{name}\n")


"""example 4 -> print hello to all file.txt user and line"""
# with open("file.txt") as file:
#     lines = file.readlines()
#     print(lines)
# for line in sorted(lines):
#     print("hello" , line.rstrip())


"""example 5 -> Append name to a list for sorting"""

# names= []
# with open("file.txt" ) as file:
#     for line in file:
#         names.append(line.strip())
# for name in sorted(names , reverse=True):
#     print(f"hello {name}")


"""csvfile"""
# students = []
# with open("file.csv") as file:
#     for line in file:
#         name,house = line.strip().split(',')
#         student= {'name': name, 'house': house}
#         students.append(student)
#
# def get_name(student):
#     return student['name']
#
# for student in sorted(students , key = lambda student: student['house']):
#     print(f'name: {student["name"]}, is in  {student["house"]}')



"""example2"""
import csv
students = []
with open("file.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        student= {'name': row[0], 'house': row[1]}
        students.append(student)

for student in sorted(students , key = lambda student: student['house']):
    print(f'name: {student["name"]}, is in  {student["house"]}')



"""" write a csv file using csv.writer """

# import csv
# name = input("Enter your name: ")
# home = input("Enter your home: ")
# grade = input("Enter your home: ")
#
# with open("file.csv" , "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home,grade])
#



