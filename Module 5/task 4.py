def sum_number(number):
    total=0
    for i in number:
        total=total+i
    return total
user_input=[1,2,3,4,5,8,9]
value=sum_number(user_input)
print(value)