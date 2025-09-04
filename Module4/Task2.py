list = []

user_input = int(input("Enter the numbers (press enter to exit): "))

for i in range((user_input)):

    user_input = int(input("Enter the degits : "))

    if user_input == " ":
        break
    list.append(int(user_input))
    list.sort(reverse=True)
print(list)