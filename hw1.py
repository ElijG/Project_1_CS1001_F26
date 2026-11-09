"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # It counts the numbers of vowels within a string and return the int number of vowels that there are
    # Text is inputed 
    #  returns a int/number representing the number of vowels within the string
    
    count = 0
    for i in text.lower():
        if i in 'aeiou':
            count += 1 
    return count

# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # it takes in list within lists and only returns the lists that are two numbers long 
    # list of list of integers
    # list with only the lists inside of it that are two integers long
    result = []
    for i in items:
        if len(i) == 2:
            result.append(i)
    return result



# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # takes in a list within a list and returns a list within a list with all the ones where it is two ints long in ascending order 
    # lists within a list holding ints inside
    # returns the same thing just with all the two number long lists in ascending order
    result = []
    for i in items:
        if len(i) == 2:
            if i[0] > i[1]:
                result.append([i[1], i[0]])
            else:
                result.append(i)
        else:
            result.append(i)
    return result
                
            





# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # adds two prices together 
    # the first and the second prices that are added togehter 
    # new price where the cents value is within 0-99
    total_cents = (first.dollars + second.dollars) * 100 + first.cents + second.cents
    return data.Price(total_cents // 100, total_cents % 100)


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # gives area of a rectangle
    # rectangles data by its top left and bottom left
    # width times height as a float
    width = abs(rectangle.bottom_right.x - rectangle.top_left.x)
    height = abs(rectangle.top_left.y - rectangle.bottom_right.y)
    return width * height


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # find the books made by the author
    # authors name, books given in a list 
    # it returns a new list of the books that are authored or co authered by the inputed author.
    result = []
    for book in books:
        if author in book.authors:
            result.append(book)
    return result
        


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # gives the smallest circle that encloses a rectangle
    # rectangle
    # circle centered at same point as rectangle 
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    center = data.Point(center_x, center_y)
    half_width = rectangle.bottom_right.x - center_x
    half_height = rectangle.top_left.y - center_y
    radius = (half_width ** 2 + half_height ** 2) ** 0.5
    return data.Circle(center, radius)
    


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # finds the people who are being paid less than the average pay rate    
    # list of all employees
    # list of employees who are below the average pay rate in the original order that they are listed
    underpaid_employees = [] 
    if len(employees) == 0:
        return []
    average = sum(e.pay_rate for e in employees) / len(employees)
    for people in employees:
        if people.pay_rate < average:
            underpaid_employees.append(people.name)
    return underpaid_employees

