# List
# A Data type for mutable ordered sequence of elements
arr = ["one", "two", "three"]
print(arr[0])
print(arr[-1])
print(arr[-0])

# Lists are mutable:
arr[1] = 'hello'
print(arr)

# list del
del arr[1]
print(arr)  # return ['one', 'three']

# list del 2
a = ['a', 'b', 'c', 'd']
del a[1:3]  # ==> return ['a', 'd']
print(a)
