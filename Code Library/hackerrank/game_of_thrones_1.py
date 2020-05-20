string = input()
character_count = {}
for i in string:
    if i not in character_count:
        character_count[i] = string.count(i)
odd_counts = 0
for i in character_count:
    if character_count[i] % 2 == 1:
        odd_counts += 1
if odd_counts > 1:
    print("NO")
else:
    print("YES")
