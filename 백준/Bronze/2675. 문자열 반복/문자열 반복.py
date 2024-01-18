count = int(input())

num_list = []
word_list = []
for i in range(count):
    word = input()
    num_list.append(int(word[0]))
    word_list.append(word[2:])

for i in range(count):
    word = word_list[i]
    for j in range(len(word)):
        for k in range(num_list[i]):
            print(word[j], end="")
    print()