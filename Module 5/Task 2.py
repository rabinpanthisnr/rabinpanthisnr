

numbers = []

while True:
    user_input = input("Enter a number or (press enter to quit): ")

    if user_input == "":
        break
    numbers.append(int(user_input))
numbers.sort(reverse=True)

top_five = numbers[:5]

print("The five gratest numbers are:", top_five)

