
n = int(input())
surnames = [input() for _ in range(n)]


def dutch_sort_key(surname):
    for i, char in enumerate(surname):
        if char.isupper():
            return surname[i:]
    return surname  

sorted_surnames = sorted(surnames, key=dutch_sort_key)

for surname in sorted_surnames:
    print(surname)
