#Write your code below this row 👇

for number in range(1, 101):
  if number % 3 == 0:
    print("fizz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  else:
    print(number)

