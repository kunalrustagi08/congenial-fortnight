from typing import ChainMap


def check_missing_alpha(my_str, alphas):

    for alpha in alphas:
        if not my_str.get(alpha):
            return alpha
    return -1



alphas = ''
for a in range(97,123):
    alphas += chr(a)

my_str = "the quick brown box jumps over a lazy dog"
my_str = {i:1 for i in my_str}
print(check_missing_alpha(my_str, alphas))