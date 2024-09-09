#############################################################################################################################
# Hackerank eeasy question
# library fine 
# The Head Librarian at a library is having a hard time keeping track of all the books that are returned late. To help him, you must create a program that calculates the fine for a book based on the following rules:

# If the book is returned on or before the expected return date, no fine will be charged.

# If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, the fine is 15 units per day.

# If the book is returned after the expected return month but within the same calendar year as the expected return date, the fine is 500 units per month.

# If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10,000 units.

# You are given the actual return date and the expected return date. Write a function libraryFine(d1, m1, y1, d2, m2, y2) that takes the following parameters:

# d1, m1, y1: The actual return date day, month, and year.
# d2, m2, y2: The expected return date day, month, and year.
#############################################################################################################################


def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1 == y2 :
        if m1 == m2:
            if d1 == d2:
                fine = 0
                return fine
            else:
                late_date = d1-d2
                fine = 15 * late_date
                return fine
        else :
            late_month = m1-m2
            fine = 500 * late_month
            return fine
    else:
        fine = 10000
        return fine


d1 = int(input())

m1 = int(input())

y1 = int(input())
d2 = int(input())

m2 = int(input())

y2 = int(input())

result = libraryFine(d1, m1, y1, d2, m2, y2)
print(result)

