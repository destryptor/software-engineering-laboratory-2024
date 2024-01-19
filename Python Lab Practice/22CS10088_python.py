# 1.
name = input("Enter name: ")
print("Hello", name)

# 2.
num1 = int(input("Enter num1: "))  #Read the first number 
num2 = int(input("Enter num2: "))  #Read the second number  
   
num3 = num1 + num2      #Add two numbers 
print("Sum is: ", num3)

# 3.
num1 = int((input("Enter number: ")))
print("Number before", num1 ,"is", num1-1);
print("Number after", num1 ,"is", num1+1);

# 4.
print("The Quick Brown Fox jumps over the Lazy Dog")
str1 = "and"
str2 = "Pack my box with Five Dozen Liquor Jugs"
print(str1.center(43))
print(str2.center(43))

# 5.
# This program should read first name and last name  
# of the user and display the name that user has entered. 
fName = input("Enter your first name: ") 
print("\nThanks") 
lName = input("Enter your last name: ") 
 
print("\n" + fName + " " + lName) 
 
print(fName, lName) # either of them works

# 6.
print('F','U', sep='', end='')    #Here default ’\n’ is suppressed 
print('N') 
 
#\n provides new line after printing the year 
print('25',    '12',    '1997', sep='-',     end='\n')  #Extra space does not have any effect 
  
#The different parts areseparated with comma and a special ‘@’ after the end instead of default '\n' 
print('Red','Green','Blue', sep=',', end='@') 
 
print('Debasis') #print statement is delimited with a default '\n' 
print("Debasis") #print statement is delimited with a default '\n' 

# 7.
# Python program showing how to use string modulo operator(%) 
  
print("Two digit value : %5d, Float value : %5.2f" % (1, 354.1732))  
  
print("Total students : %3d, Boys : %2d" % (240, 120))   # print integer value 
  
print("Octal of %2d is %7.3o" % (25, 25))   # print octal value 
  
print("Gravitational constant, G = %10.3E" % (6.6743e-11))   # print exponential value 

# 8.
print('I love {0} for "{3}!"'.format('Python', 'Programming', 'for', 'Data Analytics')) 
  
# Using format() method and referring a position of the object 
print('{0} and {1}'.format('Debasis', 'Samanta')) 
  
print('{1} and {0}'.format('Debasis', 'Samanta')) 
  
print(f"I love {'Programming'} in \"{'Python'}!\"")   #Note the use of 'f' here 
  
# Using format() method and referring a position of the object 
str1 = 'Python'
str2 = 'Programming'
print(f"{str1} is easy for {str2}") 

# 9
str1 = input("String 1: ")
str2 = input("String 2: ")
print(str1, str2, sep='')

# 10.
str1 = input("string: ")
print(len(str1))

# 11.
list = []
str1 = input("String 1: ")
str2 = input("String 2: ")
str3 = input("String 3: ")

list.append(str1)
list.append(str2)
list.append(str3)
print(list)

list.pop()
print(list)
list.pop(0)
print(list)

# 12.
str1 = "Welcome"
str2 = "to"
str3 = "Python"
str4 = "Programming"

str = str1 + " " + str2 + " " + str3 +  " " + str4

print(str)

# 13.
str = input("Enter string: ")
i = int(input("Enter i: "))

str1 = str[:i-1]
str2 = str[i:]


print(str1+str2)

# 14.
tuple = 1, 2, 3
list=[tuple, ("huh", 'bruh', 'jeff'), ('die', 'shine', 'kaette') ]
print(list)

# 15.
# Python program to demonstrate the use of update() method 
  
list1 = [1, 2, 3] 
list2 = [5, 6, 7] 
list3 = [10, 11, 12] 
  
# Lists converted to sets 
set1 = set(list2) 
set2 = set(list1) 
  
# Update method 
set1.update(set2) 
  
# Print the updated set 
print(set1) 
  
# List is passed as an parameter which gets automatically converted to a set 
set1.update(list3) 
print(set1)

list4 = [1, 3, 5, 7, 9, 11, 13]
set3 = set(list3)
set4 = set(list4)
set3.update(set4)
print(set3)


# 16.
List1 = [1, 2, 3, 4] 
List2 = [1, 4, 2, 3, 5] 
Set3 = {'a', 'b', 'c'}

list = List1 + List2 + list(Set3)

print(list)

set1 = set(List1)
set2 = set(List2)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))


# 17.
Set1 = {1, 2, 3, 4, 5} 
myDict = {6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}
print(myDict[7])
Set1.update(myDict)
print(Set1)

# 18.
# Creating an empty Dictionary  
Dict = {}  
print("Empty Dictionary: ")  
print(Dict)  
   
# Adding elements one at a time  
Dict[0] = 'Apple' 
Dict[1] = 'Banana' 
Dict[2] = 'Mango' 
print("\nDictionary after adding 3 elements: ")  
print(Dict)  
   
# Adding set of values to a single Key  
Dict[3] = 'Orange', 'Cherry', 'Guava' 
print("\nDictionary after adding 3 elements: ")  
print(Dict)  
   
# Updating existing Key's Value  
Dict[2] = 'Water Mellon' 
print("\nUpdated key value: ")  
print(Dict)  

Dict.update({4: 'Pine apple'})
print(Dict)

for key, value in Dict.items():
    if value == 'Banana':
        Dict.pop(key)
        break

print(Dict)

Dict.pop(3)
print(Dict)

# 19.
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

print(max(n1, n2, n3))

# 20.
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

if(n1 < n2):
    if(n3 < n2):
        print(n2)
    else:
        print(n3)
else:
    if(n1<n3):
        print(n3)
    else:
        print(n1)

# 21.
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

if (n1 < n2):
    if(n2 < n3):
        print(n1, "<", n2, "<", n3)
        print(n3, ">", n2, ">", n1)
    else:
        if(n1 < n3):
            print(n1, "<", n3, "<", n2)
            print(n2, ">", n3, ">", n1)
        else:
            print(n3, "<", n1, "<", n2)
            print(n2, ">", n1, ">", n3)
else:
    if(n2<n3):
        if(n1 < n3):
            print(n2, "<", n1, "<", n3)
            print(n3, ">", n1, ">", n2)
        else:
            print(n2, "<", n3, "<", n1)
            print(n1, ">", n3, ">", n2)
    else:
        print(n3, "<", n2, "<", n1)
        print(n1, ">", n2, ">", n3)

# 22.
a = 33 
b = 200 
if b > a: 
    print("b is greater than a") # you will not get an error 

# 23.
import random;

n = (int)(input("Enter n: "));
list = [];
for i in range(n):
    list.append(random.randint(0, 100));
sum = 0;

for i in list:
    if(i == 1):
        continue;
    elif(i == 2):
        sum += i;
    else:
        flag = 0;
        for j in range(2, int(i**0.5) + 1):
            if(i%j == 0):
                flag = 1;
                break;
        if(flag == 0):
            sum += i;

print(sum);
flag = 0;
for i in range(2, int(sum**0.5) + 1):
    if(sum%i == 0):
        flag = 1;
        break;
if(flag == 0):
    print("Sum of prime numbers is prime");
else:
    print("Sum of prime numbers is not prime");

# 24.
def factorial(n):
    if(n == 0):
        return 1;
    else:
        return n * factorial(n-1)

n = (int)(input("Enter n: "))
print("Factorial: ", factorial(n))

# 25.
def avg(a, b):
    return (a+b)/2;

a = (int)(input("a: "))
b = (int)(input("b: "))

print("Average: ", avg(a, b))

# 26.
def swap(a, b):
    return b, a;
a = (int)(input("a: "))
b = (int)(input("b: "))
a, b = swap(a, b)
print("{0}, {1}".format(a, b))

# 27.
def ascending(a, b, c):
    if(a > b):
        a, b = b, a;
    if(b > c):
        b, c = c, b;
    if(a > b):
        a, b = b, a;
    return a, b, c;

a = (int)(input("a: "))
b = (int)(input("b: "))
c = (int)(input("c: "))
a, b, c = ascending(a, b, c)
print("{0}, {1}, {2}".format(a, b, c))

# 28.
def fact(n):
    if(n == 0):
        return 1;
    else:
        return n * fact(n-1)
    
def gcd(a, b):
    if(b == 0):
        return a;
    if(b > a):
        return gcd(b, a)
    else:
        return gcd(b, a%b)
    
def fib(n):
    if(n == 0):
        return 0;
    elif(n == 1):
        return 1;
    else:
        return fib(n-1) + fib(n-2)
    
def sumofnharmonicnum(n):
    if(n == 1):
        return 1;
    else:
        return 1/n + sumofnharmonicnum(n-1)

def binsearch(list, low, high, key):
    if(low == high):
        return low;
    else:
        mid = (low + high)//2;
        if(list[mid] == key):
            return mid;
        elif(list[mid] > key):
            return binsearch(list, low, mid-1);
        else:
            return binsearch(list, mid+1, high);

def main():
    n = (int)(input("Enter n: "))
    print("Factorial: ", fact(n))
    a = (int)(input("a: "))
    b = (int)(input("b: "))
    print("GCD: ", gcd(a, b))
    print("Fibonacci: ", fib(n))
    print("Sum of n harmonic numbers: ", sumofnharmonicnum(n))
    list = [];
    for i in range(n):
        list.append((int)(input("Enter element: ")))
    key = (int)(input("Enter key: "))
    list.sort()
    print("Index of element: ", binsearch(list, 0, n-1, key))

main()

# 29.
def numchar(s):
    return len(s)

def main():
    s = input("Enter string: ")
    print("Number of characters: ", numchar(s))

main()

# 30.
def type(c):
    if(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        return "vowel"
    else:
        return "consonant"
    
def main():
    c = input("Enter character: ")
    print("Type: ", type(c))

main()

# 31.
def arecoprime(a, b):
    if(gcd(a, b) == 1):
        return True;
    else:
        return False;

def gcd(x, y):
    if(y == 0):
        return x;
    if(y > x):
        return gcd(y, x)
    else:
        return gcd(y, x%y)
    
def main():
    a = (int)(input("a: "))
    b = (int)(input("b: "))
    print("Are coprime: ", arecoprime(a, b))

main()

# 32.
def listops():
    list = []
    n = (int)(input("n: "))
    for i in range(n):
        list.append((int)(input("Enter element: ")))
    
    print("Sum: ", sum(list))
    print("Mean: ", sum(list)/ n)
    print("Range: ", max(list) - min(list))
    mean = sum(list)/n
    sumofsquares = 0
    for i in list:
        sumofsquares += (i - mean)**2
    print("Standard deviation: ", (sumofsquares/n)**0.5)

listops()

# 33.
def function1(x: int) -> int: 
       print("Inside the function: The initial value of x:", x) 
       x +=5 
       print("Inside the function: The value of x after the operation is:", x) 
 
# Driver code 
x = 0 
x = (int)(input("Enter a value for x: ")) 
print("The value of x you have entered", x) 
function1(x)             #Call the function with argument x 
print("The value of x after function is called", x) 

student={'Archana':28,'krishna':25,'Ramesh':32,'vineeth':25} 
def test(student): 
   new={'alok':30,'Nevadan':28} 
   student.update(new) 
   print("Inside the function",student) 
   return 
test(student) 
print("outside the function:",student)

# 34.
def countoccurencesofeachword(s : str) -> int:
    list = s.split()
    dict = {}
    for i in list:
        if(i in dict):
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def main():
    s = input("Enter string: ")
    print(countoccurencesofeachword(s))

main()

# 35.
def sumofdigits(n):
    if(n == 0):
        return 0
    else:
        return (n%10) + sumofdigits(n//10)
    
def main():
    n = (int)(input("Enter n: "))
    print("Sum of digits: ", sumofdigits(n))
main()

# 36.
def findcommonelems(a, b):
    list = []
    for i in a:
        if(i in b):
            list.append(i)
    return list

def main():
    a = []
    b = []
    n = (int)(input("n: "))
    for i in range(n):
        a.append((int)(input("Enter element: ")))
    for i in range(n):
        b.append((int)(input("Enter element: ")))
    print("Common elements: ", findcommonelems(a, b))

main()

# 37.
def revstr(s):
    # if(len(s) == 1):
    #     return s
    # else:
    #     return s[-1] + revstr(s[:-1])
    return s[::-1]

def main():
    s = input("Enter string: ")
    print("Reversed string: ", revstr(s))

main()


# 38.
def isNumPalindrome(n):
    if(n == revnum(n)):
        return True
    else:
        return False
    
def revnum(n):
    if(n == 0):
        return 0
    else:
        return (n%10) * (10**(len(str(n))-1)) + revnum(n//10)

def main():
    n = (int)(input("Enter n: "))
    print("Is palindrome: ", isNumPalindrome(n))

main()

# 39.
def isValidEmail(s):
    if(s.count('@') == 1 and s.count('.') == 1):
        if(s.index('@') < s.index('.')):
            return True
        else:
            return False
    else:
        return False
    
def main():
    s = input("Enter email: ")
    print("Is valid email: ", isValidEmail(s))

main()

# 40.
def printnonmax(list):
    max = list[0]
    for i in list:
        if(i > max):
            max = i
    for i in list:
        if(i != max):
            print(i, end=' ')
    print()
def main():
    list = []
    n = (int)(input("n: "))
    for i in range(n):
        list.append((int)(input("Enter element: ")))
    printnonmax(list)
main()

# 41.
file = open('test.txt', 'w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

with open("test2.txt", "w") as f:
    f.write("Hello World!!!")

# 42.
file1 = open('test.txt')
file2 = open('test.txt', 'r')
file3 = open('test.txt', 'rt')

for each in file1:
    print(each)

file = open("test.txt", 'r')
print(file.read())

with open('test2.txt') as file:
    data = file.read()

print(data)

file = open('test.txt', 'r')
print(file.read(5))

with open("test.txt", "r") as f:
    data = f.readlines()
    for line in data:
        word = line.split()
        print(word)

# 43.
file = open('test.txt', 'a')
file.write("This will add at the end of the file.")
file.close()

with open('test.txt') as f:
    print(f.read())

# 44.
import os 
  
def create_file(filename): 
    try: 
        with open(filename, 'w') as f: 
            f.write('Hello, world!\n') 
        print("File " + filename + " created successfully.") 
    except IOError: 
        print("Error: could not create file " + filename) 
  
def read_file(filename): 
    try: 
        with open(filename, 'r') as f: 
            contents = f.read() 
            print(contents) 
    except IOError: 
        print("Error: could not read file " + filename) 
  
def append_file(filename, text): 
    try: 
        with open(filename, 'a') as f: 
            f.write(text) 
        print("Text appended to file " + filename + " successfully.") 
    except IOError: 
        print("Error: could not append to file " + filename) 
  
def rename_file(filename, new_filename): 
    try: 
        os.rename(filename, new_filename) ###
        print("File " + filename + " renamed to " + new_filename + " successfully.") 
    except IOError: 
        print("Error: could not rename file " + filename) 
  
def delete_file(filename): 
    try: 
        os.remove(filename) ###
        print("File " + filename + " deleted successfully.") 
    except IOError: 
        print("Error: could not delete file " + filename) 
  
  
if __name__ == '__main__': 
    filename = "example.txt" 
    new_filename = "new_example.txt" 
  
    create_file(filename) 
    read_file(filename) 
    append_file(filename, "This is some additional text.\n") 
    read_file(filename) 
    rename_file(filename, new_filename) 
    read_file(new_filename) 
    delete_file(new_filename) 

# 45.
def countvowels(data):
    count = 0
    for i in data:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            count += 1
    print("Number of vowels: ", count)

def main():
    file = open('test2.txt', 'r')
    data = file.read()
    countvowels(data)

main()


# 46.
def removeduplicates(data):
    list = data.split()
    dict = {}
    for i in list:
        if(i in dict):
            dict[i] += 1
        else:
            dict[i] = 1
    list = []
    for i in dict:
        list.append(i)
    return list

def main():
    file = open('test3.txt', 'rw')
    data = file.read()
    list = removeduplicates(data)
    print(list)
    file.close()
    file = open('test3.txt', 'w')
    for i in list:
        file.write(i + ' ')

main()

# 47.
with open("data.txt", "r") as f:
    print(f.read())

# 48.
with open('test.txt', 'r') as f:
    word = f.read().split()
print(len(word))

# 49.
with open('test.txt', 'r') as f:
    word = f.read().split()

key = input("Search for: ")
count = 0
for word in word:
    if word == key:
        count += 1

print(count)

# 50.
with open("test2.txt", "r") as f:
    word = f.read().split()

with open("test2.txt", "w") as f:
    f.write(' '.join(reversed(word)))




