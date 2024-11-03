file = open('the_essay.txt', 'r')
print("Reading First Line....")
print(file.readLine())
file.close()

file = open('the_essay.txt' , 'r')
print("Reading Multiple Lines....")
print(file.readLine())
print(file.readLine())
print(file.readLine())
file.close()

file = open('the_essay.txt' , 'r')
print("Looping through lines....")
for line in file:
    print(line)
file.close()

