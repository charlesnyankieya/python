# performs certain conditions as long as a certain condition is true

number = 0
while number <= 10:
    print(number)
    number += 1

# Using breaks

colors = ["Black", "White", "Brown", "Green", "Yellow", "Orange"]
color_i_want = "Green"

length = len(colors)
count = 0

while count < length:
    print(colors[count])

    if colors[count] == color_i_want:
        print("I love it")
        break
    count += 1
