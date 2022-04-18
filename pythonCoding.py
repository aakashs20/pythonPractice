
print("----------------------- 'Input' ---------------------------")
name = input()
print(name)

digit = int(input())
print(digit)

print()
print("----------------------- 'Sort the numbers' ---------------------------")
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
print("----------------------- 'Range' --------------------------------------")
rn = range(6, 15, 2)
for r in rn:
    print(r, end=", \n")

print()
for nm in range(5):
    print("My name")

print()
#--------------------- Reverse Number List ---------------------------#
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
#--------------------- String operations -----------------------------#
strings = 'abcd'


