def num_list(parametr):
    even=[]
    for i in parametr:
        if i % 2==0:
            even.append(i)
    return even

new=[1,2,3,4,5,6,7,8,9]
final=num_list(new)
print(final)
print(new)