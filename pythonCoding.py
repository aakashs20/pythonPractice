

################## Sort the numbers #############################
nums = [2, 5, 1, 10, 3]
print(nums)

nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

names = ["Gaurav", "Aakash", "Sonu", "Pooja", "Neha"]

names.sort()
print(names)

############### Range #################################
rn = range(6, 15, 2)
for r in rn:
    print(r, end=", \n")

######################## Reverse Number List ############################
numbs = [1,5,6,9,0]

for i in range(len(numbs)):
  for j in range(i+1, len(numbs)):
    if numbs[i] > numbs[j]:
        # numbs[i], numbs[j] = numbs[j], numbs[i]
        temp = numbs[i]
        temp1 = numbs[j]
        numbs[i] = numbs[j]
        numbs[j] = temp
print(numbs)


strg = 'abcd'



