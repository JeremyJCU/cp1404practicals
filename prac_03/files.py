"""Do-from-scratch Exercise Files"""
#1
print("Question 1")
name = input("What is your name? ")
out_file = open("names.txt", "w")
print(name, file=out_file)
out_file.close()
print()

#2
print("Question 2")
in_file = open("names.txt", "r")
print(f"Hi {in_file.read()}")
in_file.close()
print()

#3
print("Question 3")
with open("numbers.txt") as in_file:
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())
    print(number_1 + number_2)
print()

#4
print("Question 4")
with open("numbers.txt") as in_file:
    for line in in_file:
        print(line.strip())