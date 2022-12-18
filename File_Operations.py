
# r for read, r+ for read and write
# w for write, w+ for write and read
# a for append, a+

fp = open("sample1.txt","r") # python script and file present in the same directory

content = fp.read() # read from start to end and return a string
print(content) # in read mode, file pointer is at the start and goes to the end of file

print("-------")


# read a specific number of characters from a file
fp = open("sample1.txt","r")

content = fp.read(25)
print(content)


# readlines or readline
content = fp.readlines() # returns a list with each line as an element
print(content)

print("-------")

# can do slicing
fp = open("sample1.txt","r")
content = fp.readlines()

print(content[:2]) # first two lines


print("-------")

# read one line at a time
fp = open("sample1.txt","r") 
content = fp.readline() # based on \n
print(content)

print("-------")

###
# fp = open("sample1.txt","r") 
# for x in fp:
# 	print(x)









### WRITE operation: flushes the entire file content, use only when creating a new file
fp = open("sample2.txt","w")

fp.write("Testing a line.") # if file does not exist it will create a new file and write into it

fp.write("Testing #2") # overrides the entire file with the new text


fp = open("sample2.txt","w+")


# Tell: current file pointer fp positon, 

# Seek: change the fp position
# seek(offset, postion), offset: number of characters, position: 0=start of file; 1=current position, 2=end of file

# seek(15,0) : change the fp by 15 characters from the start of the file
# seek(0,2) : change the fp by 0 char from the end of file
# when position value is 1 or 2: the offset value must be 0

print(fp.tell())
fp.write("Testing a line.") # when writing fp goes to the end, so we need to move the file pointer again
print(fp.tell())

fp.seek(0,0) # move pointer to the start of the file
print(fp.tell())

print(fp.read())
print(fp.tell())


# r+ will maintain the original content unline w+
fp = open("sample2.txt","r+")

print(fp.read())

fp.write("\n New line added.")


# append: add content to existing file
# in a and a+: the file pointer is at the end
# read and write modes: the fp is at the start

# in a+ we can write and read



## MODES

# r : fp at start; file should already exist; read
# r+ : fp at start; file should already exist; read and write

# w : fp at start; create a new file; write
# w+ : fp at start; create a new file; write and read

# a : fp at end; create a new file; write at end
# a+ : fp at end; create a new file; write and read
