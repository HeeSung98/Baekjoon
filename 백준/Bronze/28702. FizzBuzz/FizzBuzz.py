
for i in range(3, 0, -1):
    data = input()
    if data not in ['Fizz', 'Buzz', 'FizzBuzz']:
        result = int(data) + i

if result % 15 == 0:
    print("FizzBuzz")
elif result % 3 == 0 and result % 5 != 0:
    print("Fizz")
elif result % 3 != 0 and result % 5 == 0:
    print("Buzz")
else:
    print(result)
