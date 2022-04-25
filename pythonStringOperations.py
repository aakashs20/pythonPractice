print()


string = [0,1,2,3,4,5]
print(string[1:4])
print(string[0:])
print(string[:4])
print(string[:-4])
print(string[::4])
print(string[::-1])
print(string[5:0:-1])

x = 'universe'
print(x[2::2])

print(x[:6:2])

s = 'sunshine'
print(s[1:5:2])

print(s[1:5:1])

she = "All that glitters is not gold"
print(she[:-4:-1])
print(she[::10])

"""
string[::2] reads “default start index, default stop index, step size is two—take every second element”.
string[::3] reads “default start index, default stop index, step size is three—take every third element”.
string[::4] reads “default start index, default stop index, step size is four—take every fourth element“.
string[2::2] reads “start index of two, default stop index, step size is two—take every second element starting from index 2“.
"""