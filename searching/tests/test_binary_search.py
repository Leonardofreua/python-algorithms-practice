from unittest import TestCase, main

from searching.binary_search import binary_search


class TestBinarySearch(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print(f"Running tests of {cls.__name__}")

    def test_fail_empty_list(self) -> None:
        self.assertIsNone(binary_search([], 1))

    def test_success_one_item(self) -> None:
        self.assertEqual(binary_search([30], 30), 0)

    def test_success_search_strings(self) -> None:
        say_hello_list = ["hi", "olá", "salut"]
        self.assertEqual(binary_search(say_hello_list, "hi"), 0)
        self.assertEqual(binary_search(say_hello_list, "salut"), 2)

    def test_fail_search_strings(self) -> None:
        say_hello_list = ["hi", "olá", "salut"]
        for target in ["adiós", "你好"]:
            self.assertIsNone(binary_search(say_hello_list, target))

    def test_success_search_integers(self) -> None:
        integers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        for index, element in enumerate(integers):
            self.assertEqual(binary_search(integers, element), index)

    def test_fail_search_integers(self) -> None:
        integers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        for target in [100, 444, 326]:
            self.assertIsNone(binary_search(integers, target))

    def test_fail_search_unsorted_strings_list(self) -> None:
        unsorted_strings = ["salut", "olá", "hi"]
        for target in ["hi", "salut"]:
            self.assertIsNone(binary_search(unsorted_strings, target))

    def test_fail_search_unsorted_integers_list(self) -> None:
        unsorted_integers = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        for target in [0, 80, 90]:
            self.assertIsNone(binary_search(unsorted_integers, target))

    def test_success_search_string_in_middle_of_unsorted_list(self) -> None:
        unsorted_strings = ["salut", "olá", "hi"]
        self.assertEqual(binary_search(unsorted_strings, "olá"), 1)

    def test_success_search_integer_in_middle_of_unsorted_list(self) -> None:
        unsorted_strings = [90, 80, 70]
        self.assertEqual(binary_search(unsorted_strings, 80), 1)

if __name__ == "__main__":
    main()