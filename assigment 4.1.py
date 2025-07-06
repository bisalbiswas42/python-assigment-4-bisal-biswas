with open('sample.txt','r')as sample:
    file2=sample.read()
    print(file2)

#used for line spacing
print(  )

#incae of not found 'error' will not be displayed
a='sample.txt'
try:
    with open('a,r')as readfile:
        file1= readfile.read()
    print(file1)

except FileNotFoundError:
    print('the file',(a),'not found')
