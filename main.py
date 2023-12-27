from structure.array import Array
# This is a test area

newArray = Array()

newArray.Append('a')
newArray.Append('b')
newArray.Append('c')

# newArray => [a,b,c]

a = newArray.Pop(); # a

# newArray => [b,c]

print(newArray.length); # 2