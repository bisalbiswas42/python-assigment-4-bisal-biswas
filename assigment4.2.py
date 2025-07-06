with open('output.txt','r+')as sample1:
    a=input('Enter text to write to the file: ')
    file1=sample1.write(a+'\n')
    print("Data successfully updated to output.txt.")

#used for line spacing
print()

with open('output.txt','a')as sample2:
    b=input('Enter additional text to append: ')
    file2=sample2.write(b)
    print("Data successfully appended.")

#used for line spacing
print()

with open('output.txt','r')as sample2:
    file3=sample2.read()
    print(file3)