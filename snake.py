# x = 5
# print(min(6, 9))
# some_list =[6, 7, 8, 43]
# def func(name): 
#     print(name)

# one equals sign in python will always be assigning a "value"
x = 5
y = 'abc'
print(x)
#a intiger is any whole number
#a float is any number with a decimal value
an_int = 5
a_float = 5.0
print(type(an_int))
print(type(a_float))
div = an_int / 1
print(type(div))

#MATH OPPERATORS

# Add +
# Subtract -
# multiply *
# divide / - always converts answer into a float
# floor divide // - gives even division disregarding the remainder (rounds DOWN to the nearest int)
# modulo % - gives the remainder of an oddly divisible number
# exponents **

sum1 = 4+5
sub1 = 5-4
prod = 4*5
div1 = 25/5
floor_div = 7//3
rem = 2%3
exp = 5**6


#whatever number % 2 == 0 - HOW TO TELL ODD OR EVEN

#STRINGS
st1 = 'this is a string'
st2 = "this is also a string"
st3 = 'so\'s this'\

print(st2, '\n', st3)
#STRINGS ARE IMMUTIBLE
#how to combine strings:
st4 = st1 + ' ' + st2
print(st4) 

#interpilation - combinding a value with a string (f)
fname = 'toby'
print(f"hello there, {fname}!") #prints "hello there, toby!"

#help(<data type> ge
#LISTS
#iderable - can go though them 1 by 1
#lists are ordered, anything can go into a list:
a_list = ['123', 'abc', 'cookies', 'ramen']

n_list = [77, 25, 164, 8475, 45, 1]

print(sum(n_list)) #prints the sum of the items in a given list
print(min(n_list)) #prints the smallest number in a given list
pring(max(n_list)) #prints the largest number in a given list

print(len(n_list)) #prints the number of items in list
print(n_list[2]) #prints the value placed at a list index of 2
print(n_list[len(n_list)-1]) #prints the number of items in the list(6) minus 1 (5) {the length of a list -1 will always be the last item on the list}
                          #  } these will print the same value
print(n_list[5]) #prints the value placed at a list index of 5
print(n_list[-1]) #prints the last item of the list
print(n_list[-2]) #prints the second to last item  of the list, etc.

list function syntax:       list method syntax:
   print(example)           list.append(example)
   ^^^^^^^^^^^^^               ^^^^^^^^^^^^^
   #  func(ex)                list.method(x)

#list.append(x) --> adds given value to the end of  list
#list.pop(x) --> removes the element that was last added.
#list.remove(x) --> removes the first occurance of a value in a given list
#list.insert(x) --> adds an element to a specific given position in a list ---> example syntax:  list.insert(position, value)

b_list = [1234, 'abc']

b_list.append(46588)
print(b_list)   #prints list with value above(46588) added to the END ---> [1234. 'abc', 46588]

popped = b_list.pop()
print(popped, b_list) #prints list with last item added removed, and prints removed item seperate. --> 46588 [1234, 'abc']

b_list.append(1234) 
print(b_list) #prints [1234, 'abc', 1234]

b_list.remove(1234) #removes first occurence of 1234 in list
print(b_list) #prints ['abc', 1234]

b_list.insert(0, 1234) #inserts item (1234) at the index position of 0. Any numer over the value of the end index will place the item at the end of the list
print(b_list) #prints [1234, 'abc', 1234]


#LOOPS
#for loop - exicutes code block for each item in the list. when the 'for loop' has gone through a list once it stops.
#index loop -
#while - user defined. runs as long as a condition is true.
    #index --> where an item is placed in a list (56 has an index of 3)
    #range --> starts at a 0 index and goes the value given. if 5 it prints 0. 1, 2, 3, 4

l_list = [12, 45, 56, 67]

 #FOR
for l in l_list: 
    print(l) #prints each item of the list once
    print(l+24) #prints each number + 24 once through.
#RANGE func    
for x in range(4): 
    print(x) # prints the index for a range of 4

l_st = 'JSHFGS' 

#INDEX 
for i in range(len(l_st)): #range is limited to to the length of the list, which generates the index automatically
#(i is for index)
    print(l_st[i]) #prints list according to the index
    print(i) #prints the indexes
    
#WHILE 
WHILE TRUE:
    EXECUTE CODE
    BREAK

l = 0 #POINTER - user-defined index (i made it start at 0)
while l < len(l_st):
    print(l_st[l])
    l = l + 1

l_list = [12, 45, 56, 67]
l_st = 'JSHFGS' 

#conditionals/ control flow
# if/elif/else
#if can only be defined as true or false

while l < len(l_st):
    if l_st[1] == 'S':
        print('found it!')
    elif l_st[1] == 'G':
        print("it's here!")
    else:
        print("it is not S, or G")
    
#EXAMPLE   
# age = 53
# if age < 18:
#     print ('minor')
# elif age > 65:
#     print('senior')
# else:
#     print('adult')
    
    
    
#MAKING A FUNCTION
print("function test: \n")
def age_filter(user_age):
    # user_age = int(input('enter age here'))
    if user_age < 18:
        print ('Minor')
    elif user_age >= 18 and user_age <= 65:
        print('Adult')
    else:
        print('Senior')
 age_filter()
