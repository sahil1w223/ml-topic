import os
print(os.getcwd())  # Get the current working directory
os.chdir("05 File Operation")  # Change the current working directory to "05 File Operation
# os.mkdir("package")  # Create a new directory named "new_directory"

print(os.listdir('.')) # List all files and directories in the current directory

dir_name = "new_directory"
file_name = "test_file.txt"
full_path = os.path.join(dir_name, file_name) # Create a full path by joining the directory and file name
print(full_path) # This will print "new_directory/test_file.txt" on Unix-like systems


if os.path.exists(full_path):
    print(f"The file {full_path} exists.")
else:
    print(f"The file {full_path} does not exist.")


file = "example.txt"
absolute_path = os.path.abspath(file) # Get the absolute path of the file
print(absolute_path) # This will print the absolute path of "example.txt".