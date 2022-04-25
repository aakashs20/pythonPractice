"""
print("----------------------- 'Input' ---------------------------")

name = input("Enter the string: ")
print("You have entered: " + name)

digit = int(input("Enter the numeric: "))
print(f'"You have entered: " + {digit}')    # Formatting

print()
print("----------------------- 'Sort the numbers' -----------------")

nums = [2, 5, 1, 10, 3]
print(nums)

nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

names = ["Gaurav", "Aakash", "Sonu", "Pooja", "Neha"]

names.sort()
print(names)

print()
print("----------------------- 'Range' -----------------------------")

rn = range(6, 15, 2)
for r in rn:
    print(r, end=", \n")

print()
for nm in range(5):
    print("My name")

print()
print("--------------------- Reverse Number List --------------------")

numbs = [1, 5, 6, 9, 0]

for i in range(len(numbs)):
    for j in range(i + 1, len(numbs)):
        if numbs[i] > numbs[j]:
            # numbs[i], numbs[j] = numbs[j], numbs[i]
            temp = numbs[i]
            temp1 = numbs[j]
            numbs[i] = numbs[j]
            numbs[j] = temp
print(numbs)

print()
print("---------------------Even or Odd-------------------------------")

print("Enter the number:- ")
num1 = int(input())
if num1 % 2 == 0:
    print("The number is Even.")
    # print("{} is even number".format(num1))  # Formatting
else:
    print("Number is Odd.!")

print()
print("---------------------Prime numbers-------------------------------")

print("Enter any number: ")
pnum = int(input())

p = 0
for pn in range(2, pnum):
    if pnum % pn == 0:
        p = 1
        break
if p == 0:
    print("This is a Prime number")
else:
    print("The number is not Prime")
"""
print()
print("--------------------- String operations -----------------------")

myString = "AAKASH"
print(myString[::-1])

s = "Saxena"
str = ""
for i in s:
    str = i + str
print(str)
