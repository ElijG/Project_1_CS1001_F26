"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(hw1.vowel_count("Apple"), 2)
        self.assertEqual(hw1.vowel_count("AEIOUaeiou"), 10)

    def test_vowel_count_empty_string(self):
        self.assertEqual(hw1.vowel_count(""), 0)
        self.assertEqual(hw1.vowel_count("rhythm"), 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        self.assertEqual(hw1.short_lists([[1], [2, 3], [], [4, 5, 6], [7, 8]]),[[2, 3], [7, 8]])
                         
    def test_short_lists_no_matching_lengths(self):
        self.assertEqual(hw1.short_lists([[1], [], [4, 5, 6]]), [])
    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual(hw1.ascending_pairs([[1, 2], [9, 2], [5, 5]]), [[1, 2], [2, 9], [5, 5]])

    def test_ascending_pairs_other_lengths_unchanged(self):
       self.assertEqual(hw1.ascending_pairs([[9, 2], [3, 1, 2], [], [4]]), [[2, 9], [3, 1, 2], [], [4]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
       self.assertEqual(hw1.add_prices(data.Price(3, 25), data.Price(2, 50)),data.Price(5, 75))

    def test_add_prices_with_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(3, 75), data.Price(2, 50)),data.Price(6, 25))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        rectangle = data.Rectangle(data.Point(0, 4), data.Point(3, 0))
        result = hw1.rectangle_area(rectangle)
        self.assertEqual(result, 12)

    def test_rectangle_area_negative_coordinates(self):
        rectangle = data.Rectangle(data.Point(-4, -1), data.Point(-1, -3))
        result = hw1.rectangle_area(rectangle)
        self.assertEqual(result, 6)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        author = 'Ann'
        book1 = data.Book(['Ann'], 'First')
        book2 = data.Book(['Bob'], 'Second')
        book3 = data.Book(['Ann', 'Cy'], 'Third')
        books = [book1, book2, book3]
        result = hw1.books_by_author(author, books)
        self.assertEqual(result, [book1, book3])

    def test_books_by_author_no_matches(self):
        author = 'Zed'
        books = [data.Book(['Ann'], 'First')]
        result = hw1.books_by_author(author, books)
        self.assertEqual(result, [])
        result = hw1.books_by_author(author, [])
        self.assertEqual(result, [])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        rectangle = data.Rectangle(data.Point(0, 2), data.Point(2, 0))
        result = hw1.circle_bound(rectangle)
        self.assertEqual(result, data.Circle(data.Point(1, 1), 2 ** 0.5))

    def test_circle_bound_non_square_rectangle(self):
        rectangle = data.Rectangle(data.Point(0, 6), data.Point(8, 0))
        result = hw1.circle_bound(rectangle)
        self.assertEqual(result, data.Circle(data.Point(4, 3), 5))

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        employees = [data.Employee('Low', 10), data.Employee('Mid', 20), data.Employee('High', 30)]
        result = hw1.below_pay_average(employees)
        self.assertEqual(result, ['Low'])

    def test_below_pay_average_empty_list(self):
        employees = []
        result = hw1.below_pay_average(employees)
        self.assertEqual(result, [])
        employees = [data.Employee('A', 15), data.Employee('B', 15)]
        result = hw1.below_pay_average(employees)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
