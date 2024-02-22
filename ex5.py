def count_grandchild(name, family):
    if name not in family:
        return 0
    cnt = len(family[name])
    for grandchild in family.get(name, []):
        cnt += count_grandchild(grandchild, family)

    return cnt


num = int(input())
family = {}

for idx in range(num):
    pair = input().split()
    if pair[0] in family:
        family[pair[0]].append(pair[1])
    else:
        family[pair[0]] = [pair[1]]

name = input()
print(count_grandchild(name, family))
