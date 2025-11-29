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

# with open("file.txt") as file:
#     lines = file.readlines()
# for line in sorted(lines):
#     print("hello" , line.rstrip())


"""example 5"""

# names= []
# with open("file.txt" ) as file:
#     for line in file:
#         names.append(line.strip())
# for name in sorted(names , reverse=True):
#     print(f"hello {name}")


"""example 6 csv files"""
# student = []
# with open("file.csv") as file:
#     for line in file:
#         name , house , years = line.strip().split(',')
#         student.append(f"{name} is in {house} , and {years}")
#
# for _ in sorted(student):
#     print(_)


"""example 7"""
# import csv
# student = []
# with open('file.csv', newline='') as file:
#     reader = csv.reader(file, delimiter='\t')
#     for row in reader:
#         if len(row) != 3:
#             continue
#         student.append({'name': name, 'house': home , 'years': age})
# for student in sorted(student , key=lambda student: student['name']):
#     print(f"{student['name']} is {student['years']} years old.")



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



