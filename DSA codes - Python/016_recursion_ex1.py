def get_nums(arr):

    for i in arr:
        if isinstance(i, list):
            get_nums(i)
        elif isinstance(i, int):
            print(i)

arr = [
 1,
2,
3,
[4, 5, 6],
7,
[8,
[9, 10, 11,
[12, 13, 14]
]
],
[15, 16, 17, 18, 19,
[20, 21, 22,
[23, 24, 25,
[26, 27, 29]
], 30, 31
], 32
], 33
]


print(get_nums(arr))