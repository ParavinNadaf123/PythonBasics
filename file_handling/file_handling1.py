# file = open("filename.txt", "mode")

file = open("filename1.txt","r")
print(file.read())
file.close()

# Writes data to a file.If the file exists, all previous data is deleted.
file = open("filename1.txt","w")
(file.write("july is also done"))
file.close()

# 3. Append Mode (a) Adds new data to the end of the file.
file = open("filename1.txt","a")
file.write("\nNever mind")
file.close()

# 4. Create File (x) ,  Creates a new file.

# file = open("Newfile.txt","x")
# file.close()

file = open("Newfile.txt","r")
print(file.readline())   # readline()-----Reads one line.
file.close()

file = open("Newfile.txt","r")
print(file.readlines()) #----- Reads all the lines
file.close()


with open("Newfile.txt","r") as file: #-----The with statement automatically closes the file.
    print(file.read())


#File Handling with Exception Handling

try:
    file = open("koko.txt","r")
    print(file.read())

except FileNotFoundError :
    print("File not found")

finally:
    print("File operation is completed")