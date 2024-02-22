num = int(input())
eng_dict = {}
for value in range(num):
    pair = input().split()
    eng_dict[pair[0]] = pair[1]

string_list = input().split()

for word in range(len(string_list)):
    if string_list[word] in eng_dict:
        string_list[word] = eng_dict[string_list[word]]

print(*string_list)

'''
string = input().split()
for index, word in enumerate(string):
    if word in word_dict:
        string[index] = word_dict[word]
print(' '.join(string))
'''
