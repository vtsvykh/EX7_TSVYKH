num = int(input())
word_dict = {}
for word in range(num):
    pair = input().split()
    word_dict[pair[0]] = pair[1]
    word_dict[pair[1]] = pair[0]

target = input()

if target in word_dict:
    print(word_dict[target])
else:
    print(target)
