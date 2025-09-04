cabin_class= str(input("Enter the cabin class: "))
if cabin_class == "LUX" or "lux":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A" or "a":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B" or "b":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C" or "c":
    print("windowless cabin below the car deck.")