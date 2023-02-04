# Program 2
# The goal of this program is to simulate the retrieval of filtered data from a dataset
# The data is stored in p2.txt, one item per line.  

# open the file

data = open("data/p2.txt")

# read each line and convert it to a "float", the result should be a list of floats.  You can do this with a loop or list expression

while True:
    s1 = data.readline();
    if(s1 == ''):   #check EOF
        break
    print(float(s1))

# Using the "input" function, ask the user for two values, low and high

a = int (input ("value 1: "))   # 2 integer input
b = int (input ("value 2: "))


# Print the sum of the values between low (inclusive) and high (exclusive)    
# 
# #--------------> uncleared question: sum from the dataset or only from that range?

print('sum: ',sum(range(a, b)))  # exclusive the max value b


# Challenge: See if you can get the program to repeat this process until the user types "q" instead of a number

while True:
    a = input ("value 1: ")
    if a == 'q':
        break    #quit statement
    b = input ("value 2: ")
    if b=='q':
        break    #quit statement
    print('sum: ',sum(range(int(a), int(b))))