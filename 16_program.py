# Open file1.txt in read mode
with open("file1.txt", 'r') as fn1:
    print("Content of First file:")
    content = fn1.read()
    print(content)

# Open file1.txt in read mode and file2.txt in write mode
with open("file1.txt", 'r') as fn1, open("file2.txt", 'w') as fn2:
    # Read the content of the file line by line
    cont = fn1.readlines()
    
    # Write content to file2.txt
    for line in cont:
        fn2.write(line)

print("Successfully copied the content of first file to second file")

# Open file2.txt in read mode to confirm the copy
with open("file2.txt", 'r') as fn2:
    cont1 = fn2.read()
    print("Content of Second file:")
    print(cont1)
