f = open("file1.txt", "a")
f.write(". now the file has more content")
f.close()

#open and read the file after closing
f = open("file1.txt", "r")
print(f.read())

f = open("file1.txt", "w")
f.write("now the file has been overwritten")
f.close()

#open and read the file after closing
f = open("file1.txt", "r")
print(f.read())