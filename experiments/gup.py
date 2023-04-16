import os

my_string = "Hello, friends."

print(my_string[:3])

print(my_string)

filepath = "new_file"


with open(filepath, "ab") as out_file:
    print(out_file.mode)
    print(out_file.name)

    out_file.write(bytes("yo\n", "UTF-8"))

os.remove(filepath)

# print(os.urandom(24))
