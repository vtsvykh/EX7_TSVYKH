num = int(input())
word_dict = {}
for _ in range(num):
    string = input().split()
    word_dict[string[0]] = string[1:]

target = input()

for key in word_dict:
    if target in word_dict[key]:
        print(key)
