# Reading a file in Python can be done using the built-in `open()` function. Here are two common ways to read a file:
with open("05 File Operation/example.txt", "r") as file:
    content = file.read()
    print(content) # This will print the entire content of the file as a single string.



with open("05 File Operation/example.txt", "r") as file:
    for line in file:
        print(line.strip()) # .strip() removes leading and trailing whitespace, including the newline character.

# Writing to a file can be done using the `open()` function with the "w" mode. For example:
with open("05 File Operation/example.txt", "w") as file:
    file.write("Hello, World!")


with open("05 File Operation/example.txt", "r") as file1: # Overwrite the file with new content
    for line in file1:
        print(line.strip()) # This will print "Hello, World!" which we just wrote to the file.  


with open("05 File Operation/example.txt", "a") as file: # Append to the file instead of overwriting
    file.write("\nThis is an additional line.") # This will add a new line to the existing content of the file.

with open("05 File Operation/example.txt", "r") as file2:
    for line in file2:
        print(line.strip()) # This will print both "Hello, World!" and "This is an additional line."


# Writing List of Lines to a File
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("05 File Operation/example.txt", "a") as file:
    # method 1: 
    # for l in lines:
    #     file.write(l+"\n") # This will add multiple lines to the file.

    # methode 2: using writelines() method
    file.writelines(lines) # This will also add multiple lines to the file.

with open("05 File Operation/example.txt", "r") as file2:
    for line in file2:
        print(line.strip())


# Writing a Bineary File
with open("05 File Operation/example.bin", "wb") as file:
    file.write(b"Hello, World!") # The 'b' before the string indicates that it is a byte string.

with open("05 File Operation/example.bin", "rb") as file:
    content = file.read()
    print(content) # This will print the byte string: b'Hello, World!'


with open('05 File Operation/example.txt', 'r') as file:
    content = file.read()
    with open('05 File Operation/destination.txt', 'a') as dest_file:
        dest_file.write(content) # This will copy the content of example.txt to destination.txt, appending it if destination.txt already exists.


# writing and than reading a file using with statement
with open("05 File Operation/newfile.txt", "w+") as file:
    file.write("This is a new file created using the with statement.")
    file.write("\nThis file is used to demonstrate reading and writing in the same block.")

    file.seek(0) # Move the file pointer back to the beginning of the file
    content = file.read()
    print(content) # This will print the content we just wrote to the file.