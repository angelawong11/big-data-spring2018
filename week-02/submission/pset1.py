# A1 Create a list containing any 4 strings.
A1 = ["apple", "banana", "orange", "pear"]
print(A1)

# A2 Print the 3rd item in the list
print(A1[2])

#A3 Print the 1st and 2nd item in the list using [:] index slicing.
print(A1[0:2])

#A4 Add a new string with text “last” to the end of the list and print the list.
A1.append("Last")
print(A1)

#A5 Get the list length and print it.
print(len(A1))

#A6 Replace the last item in the list with the string “new” and print
A1[4] = "new"
print(A1)

#B
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']

#B1 Convert the list into a normal sentence with join(), then print.
print(" ".join(sentence_words))

#B2 Reverse the order of this list using the .reverse() method, then print. Your output should begin with [“them”, ”visualize”, … ].
sentence_words.reverse()
print(sentence_words)

#B3 Now user the .sort() method to sort the list using the default sort order.
sentence_words.sort()
print(sentence_words)

#B4 Perform the same operation using the sorted() function. Provide a brief description of how the sorted() function differs from the .sort() method.
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
B4 = sorted(sentence_words)
print(B4)
print(sentence_words)
#The .sort() method does not require the varaible to be passed. The method sorts and stores the result within the variable sentence_words.
#The sorted() function requires the variable to be passed through. The function sorts but doesn't change the original variable, as shown in line 40.

#B Extra Credit: Modify the sort to do a case case-insensitive alphabetical sort
#Code adopted from Stack Overflow, available at: https://stackoverflow.com/questions/10269701/case-insensitive-list-sorting-without-lowercasing-the-result
sentence_words.sort(key=lambda x: x.lower())
print(sentence_words)

#C Random Function
from random import randint
def numC(high, low=0):
    return randint(low, high)
assert(0 <= numC(100) <= 100)
assert(50 <= numC(100, low = 50) <= 100)
numC(40,5)


#D String Formatting Function
def formatD(title2,y):
    title2 = title2.title()
    formatDinputs = [title2,y]
    print(f"The number {formatDinputs[1]} bestseller today is: {formatDinputs[0]}")
formatD("guide to big data",3)


#E Password Validation Function
def password(inputpw):
    digit = 0
    upper = 0
    special = 0
    if len(inputpw) >=8 and len(inputpw) <=14:
        for i in inputpw:
            if i.isdigit() == True:
                digit += 1
            elif i.isupper() == True:
                upper += 1
            elif i in ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']:
                special += 1
            else:
                special +=0
    else:
        print('Error')
    if digit >= 2 and upper >= 1 and special >= 1:
        print('Success')
    else:
        print('Error')
password('Qwerty45$')


#F Exponentiation Function
def exp(x,y):
    Ex = x
    for i in range(y-1):
        Ex = Ex*x
    return(Ex)
exp(5,4)
