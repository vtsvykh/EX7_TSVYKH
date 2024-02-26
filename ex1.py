string = input().split()
dict_word = {}
reverse_dict_word = {}

for word in string:
    if word not in dict_word:
        dict_word[word] = 1
    else:
        dict_word[word] += 1

for item in dict_word.items():
    reverse_dict_word[item[1]] = item[0]

reverse_dict_word = sorted(reverse_dict_word.items(), reverse=True)

for tpl in reverse_dict_word:
    print(tpl[1])
