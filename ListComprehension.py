#List comprehension in Python is a concise way to create lists.
#(It allows you to generate a new list by applying an expression to each item in an iterable
#(like a list, tuple, string, or range), often with optional conditions.


#Squares of numbers
#[expression for item in iterable]
squares = [x**2 for x in range(5)]
print(squares)

#Even Numbers
#[expression for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

#Converting String to upper case
names = ["alice", "bob", "charlie"]
upperCaseNames = [name.upper() for name in names]
print(upperCaseNames)

#If Else
#[expression_if_true if condition else expression_if_false for item in iterable]
label = ["even" if num % 2 == 0 else "odd" for num in range(10)]
print(label)

#Nested List Comprehension
#[expression for outer_item in outer_iterable for inner_item in inner_iterable]
list_of_lists = [[1, 2, 3], [4, 5], [6]]
flattedList = [item for sublist in list_of_lists for item in sublist]
print(flattedList)