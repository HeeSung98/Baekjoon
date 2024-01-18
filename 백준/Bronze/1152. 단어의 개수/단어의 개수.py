text = input()

result = 0
for i in range(len(text)):
    if text[i] == " " and i != 0 and i != len(text) - 1:
        result = result + 1
    
if text == " ":
    print(result)
else:
    print(result + 1)