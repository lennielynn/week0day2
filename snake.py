# x = 5
# print(min(6, 9))
# some_list =[6, 7, 8, 43]
# def func(name): 
#     print(name)

# one equals sign in python will always be assigning a "name" to a "value"
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
#interpilation - combinding a value with a string (f)
fname = 'toby'
print(f"hello there, {fname}!")

#lISTS
#iderable - can go though them 1 by 1
#lists are ordered
a_list = ['123', 'abc', 'cookies', 'ramen']
print(min(a_list))
print(len(a_list))
#func(x)         .method(x)
#list.append(x) --> adds to the end of  list
#list.pop(x) --> pops vslue off the end of the list
#list.remove(x) --> removes the first occurance of a value
#list.insert(x) --> adds an element in specific position ---> ex.  lisy.insert(pos, value)
#LOOPS
l_list = [12, 45, 56, 67, 145]
#for - super common use, exicutes code block for each item in the list
for l in l_list:
    print(1)
#index --> where an item is placed in a list (56 has an index of 3)
#range --> starts at 0 and goes the number given. if 5 it prints 0. 1, 2, 3, 4
for x in range(5):
    print(x)
#while --> user defined. runs as long as a condition is true.
while True:
    print('fulfil code')
    
#conditionals/ control flow
# if/elif/else
if l_list[1] == 45:
    print('found it!')
elif l_list[1] == 67:
    print("it's here!")
else:
    print("it is not 45, or 67")
    
    


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
print(age_filter(12))
