from unittest import TestCase, main

from searching.binary_search_recursive import binary_search_recursive


class TestBinarySearchRecursive(TestCase):
    LEFT: int = 0

    @classmethod
    def setUpClass(cls) -> None:
        print(f"Running tests of {cls.__name__}")

    def test_fail_empty_list(self) -> None:
        list_of_items = []
        self.assertIsNone(
            binary_search_recursive(list_of_items, 1, self.LEFT, len(list_of_items))
        )

    def test_success_one_item(self) -> None:
        list_of_items = [30]
        index = binary_search_recursive(list_of_items, 30, self.LEFT, len(list_of_items))
        self.assertEqual(index, 0)

    def test_success_search_strings(self) -> None:
        say_hello_list = ["hi", "olá", "salut"]
        right = len(say_hello_list)
        self.assertEqual(binary_search_recursive(say_hello_list, "hi", self.LEFT, right), 0)
        self.assertEqual(
            binary_search_recursive(say_hello_list, "salut", self.LEFT, right), 2
        )

    def test_fail_search_strings(self) -> None:
        say_hello_list = ["hi", "olá", "salut"]
        for target in ["adiós", "你好"]:
            index = binary_search_recursive(
                say_hello_list, target, self.LEFT, len(say_hello_list)
            )
            self.assertIsNone(index)

    def test_success_search_integers(self) -> None:
        integers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        for index, element in enumerate(integers):
            self.assertEqual(
                binary_search_recursive(integers, element, self.LEFT, len(integers)), index
            )

    def test_fail_search_integers(self) -> None:
        integers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        for target in [100, 444, 336]:
            self.assertIsNone(
                binary_search_recursive(integers, target, self.LEFT, len(integers))
            )

    def test_fail_search_unsorted_strings_list(self) -> None:
        unsorted_strings = ["salut", "olá", "hi"]
        for target in ["hi", "salut"]:
            index = binary_search_recursive(
                unsorted_strings, target, self.LEFT, len(unsorted_strings)
            )
            self.assertIsNone(index)

    def test_fail_search_unsorted_integers_list(self) -> None:
        unsorted_integers = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        for target in [0, 80, 90]:
            index = binary_search_recursive(
                unsorted_integers, target, self.LEFT, len(unsorted_integers)
            )
            self.assertIsNone(index)

    def test_success_search_string_in_middle_of_unsorted_list(self) -> None:
        unsorted_strings = ["salut", "olá", "hi"]
        index = binary_search_recursive(
            unsorted_strings, "olá", self.LEFT, len(unsorted_strings)
        )
        self.assertEqual(index, 1)

    def test_success_search_integer_in_middle_of_unsorted_list(self) -> None:
        unsorted_integers = [90, 80, 70]
        index = binary_search_recursive(
            unsorted_integers, 80, self.LEFT, len(unsorted_integers)
        )
        self.assertEqual(index, 1)

if __name__ == "__main__":
    main()