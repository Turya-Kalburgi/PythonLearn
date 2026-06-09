# Import the os module
import os

# Specify the directory path
# "." represents the current directory
path = "."

# Get the list of files and folders in the directory
contents = os.listdir(path)

# Print all items in the directory
print("Contents of the directory are:")

for item in contents:
    print(item)