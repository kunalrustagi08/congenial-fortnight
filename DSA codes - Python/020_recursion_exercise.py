def count_char(str):

    if str == '':
        return 0
    else:
        sum = 1
        return sum + count_char(str[1:])


def is_even(x):
    if x%2 == 0:
        return True
    return False

def get_even(arr):

    if arr == []:
        return []

    even_list = []
    temp = get_even(arr[1:])
    print(1, temp)

    if is_even(arr[0]):
        even_list.append(arr[0])
        print(2, even_list)
    
    return even_list + temp




'''
[1,2,3] g_e(2,3)
[2,3] g_E(3) [2] temp 
[3] g_e([]) [] 
[] return
'''


def triangular_num(N):

    if N == 0:
        return 0
    else:
        return N + triangular_num(N-1)


def get_index(word):

    if word[0] == 'x':
        return 0
    else:
        return 1 + get_index(word[1:])




# Exercise 1:  Use recursion to write a function that accepts an array of strings and
# returns the total number of characters across all the strings

a = ["ab", "c", "def", "ghij"]
sum = 0
for str in a:
    sum += count_char(str)
print(sum)

# Exercise 2: Use recursion to write a function that accepts an array of numbers and
# returns a new array containing just the even numbers.

arr = [1,2,3,4,5,6,7,8,9,0,10,11,23]
print(get_even(arr))

# Exercise 3:

print(triangular_num(7))

# Exercise 4:
word = "abcdefghijklmnopqrstuvwxyz"
print(get_index(word)) 