from unittest import TestCase, TestSuite, TestLoader, TextTestRunner

from searches import binary_search, binary_search_rec


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


class TestBinarySearchRecursive(TestCase):
    LEFT: int = 0

    @classmethod
    def setUpClass(cls) -> None:
        print(f"Running tests of {cls.__name__}")

    def test_fail_empty_list(self) -> None:
        list_of_items = []
        self.assertIsNone(
            binary_search_rec(list_of_items, 1, self.LEFT, len(list_of_items))
        )

    def test_success_one_item(self) -> None:
        list_of_items = [30]
        index = binary_search_rec(list_of_items, 30, self.LEFT, len(list_of_items))
        self.assertEqual(index, 0)

    def test_success_search_strings(self) -> None:
        say_hello_list = ["hi", "olá", "salut"]
        right = len(say_hello_list)
        self.assertEqual(binary_search_rec(say_hello_list, "hi", self.LEFT, right), 0)
        self.assertEqual(
            binary_search_rec(say_hello_list, "salut", self.LEFT, right), 2
        )

    def test_fail_search_strings(self) -> None:
        say_hello_list = ["hi", "olá", "salut"]
        for target in ["adiós", "你好"]:
            index = binary_search_rec(
                say_hello_list, target, self.LEFT, len(say_hello_list)
            )
            self.assertIsNone(index)

    def test_success_search_integers(self) -> None:
        integers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        for index, element in enumerate(integers):
            self.assertEqual(
                binary_search_rec(integers, element, self.LEFT, len(integers)), index
            )

    def test_fail_search_integers(self) -> None:
        integers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        for target in [100, 444, 336]:
            self.assertIsNone(
                binary_search_rec(integers, target, self.LEFT, len(integers))
            )

    def test_fail_search_unsorted_strings_list(self) -> None:
        unsorted_strings = ["salut", "olá", "hi"]
        for target in ["hi", "salut"]:
            index = binary_search_rec(
                unsorted_strings, target, self.LEFT, len(unsorted_strings)
            )
            self.assertIsNone(index)

    def test_fail_search_unsorted_integers_list(self) -> None:
        unsorted_integers = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        for target in [0, 80, 90]:
            index = binary_search_rec(
                unsorted_integers, target, self.LEFT, len(unsorted_integers)
            )
            self.assertIsNone(index)

    def test_success_search_string_in_middle_of_unsorted_list(self) -> None:
        unsorted_strings = ["salut", "olá", "hi"]
        index = binary_search_rec(
            unsorted_strings, "olá", self.LEFT, len(unsorted_strings)
        )
        self.assertEqual(index, 1)

    def test_success_search_integer_in_middle_of_unsorted_list(self) -> None:
        unsorted_integers = [90, 80, 70]
        index = binary_search_rec(
            unsorted_integers, 80, self.LEFT, len(unsorted_integers)
        )
        self.assertEqual(index, 1)


def build_suite():
    suite = TestSuite()
    for test_case in [TestBinarySearch, TestBinarySearchRecursive]:
        tests = TestLoader().loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite


if __name__ == "__main__":
    runner = TextTestRunner()
    runner.run(build_suite())
