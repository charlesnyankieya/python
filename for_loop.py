# how many times to iterate a loop

names = ["John", "Mary", "Kamukunji", "Nairobi", "Kenya"]

for name in names:
    print(name)
# prints individual names

welcome_message = "Welcome Home"
for i in range(5):
    print(welcome_message)

# prints welcome message 5 times

# Using breaks

colors = ["Black", "White", "Brown", "Green", "Yellow", "Orange"]
color_i_want = "Green"

for color in colors:
    if color == color_i_want:
        print("I love it")
        break
    print(color)


ages = [18, 20, 23, 45, 67, 89]

for age in ages:
    if age < 50:
        print(age)
        break


groups = [["Kante", "Davido"], ["Hello", "Adele"], ["Alone", "Marshmello"]]
for group in groups:
    print(group)
    for name in group:
        print(name)
