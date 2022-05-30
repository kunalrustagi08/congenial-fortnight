def get_first_non_duplicate(word):
    
    hash_table = {}

    for ch in word:
        if hash_table.get(ch) == None:
            hash_table[ch] = 1
        else:
            hash_table[ch] += 1

    print(hash_table)
    
    for ch in word:
        if hash_table[ch] == 1:
            return ch
    
    return -1

word = 'minimum'
print(get_first_non_duplicate(word))