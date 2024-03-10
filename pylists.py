# manipulating python lists

nummer = [21, 32, 34, 45, 56]
print("Before Append:", nummer)

# using append method
nummer.append(60)
nummer.append([45, 54, 69])
print("After Append:", nummer)

# using extend Method
prime_numbers = [2, 3, 5, 7, 11]
print("List1:", prime_numbers)

even_numbers = [4, 6, 8, 10]
print("List2:", even_numbers)

prime_numbers.extend(even_numbers)
print("final:", prime_numbers)

# deleting files python using del()

languages = ["Python", "JavaScript", "Java", "C"]
for language in languages:
    print(language)

print(languages[2])

del languages[2]
print(languages)

# using remove
languages.remove("C")
print(languages)

# python list comprehension

numbers = [number * number for number in range(1, 9)]
print(numbers)

# tuples
var1 = "Hallo"
print(type(var1))

var2 = ("Hallo",)
print(type(var2))

# brackets are not a must sometimes

var3 = "Hallo",
print(type(var3))
word = ('p', 'r', 'o', 'g', 'r', 'a', 'm')

print(word[-1])

print(word.count('o'))
print(word.count('p'))
print(word.index('g'))

