from unittest import TestCase, TestSuite, TestLoader, TextTestRunner

from binary_search import binary_search, binary_search_rec

LIST_SIZE_1 = [30]
LIST_SIZE_2 = [34, 55]
LIST_SIZE_3 = [111, 202, 566]
LIST_SIZE_10 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]



class TestBinarySearch(TestCase):
  @classmethod
  def setUpClass(cls) -> None:
      print(f"Running tests of {cls.__name__}")

  # LIST SIZE 1
  def test_success_search_element_list_size_1(self) -> None:
    self.assertEqual(binary_search(list_of_items=LIST_SIZE_1, target=30), 0)

  def test_fail_search_for_non_existent_element_list_size_1(self) -> None:
    for element in [99, -99]:
      self.assertIsNone(binary_search(list_of_items=LIST_SIZE_1, target=element))

  # LIST SIZE 2
  def test_success_search_elements_list_size_2(self) -> None:
    for index, element in enumerate(LIST_SIZE_2):
      self.assertEqual(binary_search(list_of_items=LIST_SIZE_2, target=element), index)

  def test_fail_search_for_non_existent_elements_list_size_2(self) -> None:
     for element in [35, -55]:
      self.assertIsNone(binary_search(list_of_items=LIST_SIZE_2, target=element))

  def test_fail_search_unsorted_list_size_2(self):
    self.assertIsNone(binary_search(list_of_items=LIST_SIZE_2[::-1], target=34))

  # LIST SIZE 3
  def test_success_search_elements_list_size_3(self) -> None:
    for index, element in enumerate(LIST_SIZE_3):
      self.assertEqual(binary_search(list_of_items=LIST_SIZE_3, target=element), index)

  def test_fail_search_for_non_existents_list_size_3(self) -> None:
     for element in [110, -111, 567]:
      self.assertIsNone(binary_search(list_of_items=LIST_SIZE_3, target=element))

  def test_fail_search_unsorted_list_size_3(self) -> None:
      self.assertIsNone(binary_search(list_of_items=LIST_SIZE_3[::-1], target=111))

  # LIST SIZE 10
  def test_success_search_elements_list_size_10(self) -> None:
    for index, element in enumerate(LIST_SIZE_10):
      self.assertEqual(binary_search(list_of_items=LIST_SIZE_10, target=element), index)

  def test_fail_search_for_non_existents_list_size_10(self) -> None:
     for element in [11, -10, 100]:
      self.assertIsNone(binary_search(list_of_items=LIST_SIZE_10, target=element))

  def test_fail_search_unsorted_list_size_10(self) -> None:
      self.assertIsNone(binary_search(list_of_items=LIST_SIZE_10[::-1], target=10))


class TestBinarySearchRecursive(TestCase):
  @classmethod
  def setUpClass(cls) -> None:
      print(f"Running tests of {cls.__name__}")

  # LIST SIZE 1
  def test_success_search_element_list_size_1(self) -> None:
    result = binary_search_rec(
      list_of_items=LIST_SIZE_1,
      target=30,
      left=0,
      right=len(LIST_SIZE_1) - 1)
    self.assertEqual(result, 0)

  def test_fail_search_for_non_existent_element_list_size_1(self) -> None:
    for element in [99, -99]:
      result = binary_search_rec(
        list_of_items=LIST_SIZE_1,
        target=element,
        left=0,
        right=len(LIST_SIZE_1) - 1)
      self.assertIsNone(result)

  # LIST SIZE 2
  def test_success_search_elements_list_size_2(self) -> None:
    for index, element in enumerate(LIST_SIZE_2):
      result = binary_search_rec(
        list_of_items=LIST_SIZE_2,
        target=element,
        left=0,
        right=len(LIST_SIZE_2) - 1)
      self.assertEqual(result, index)

  def test_fail_search_for_non_existent_elements_list_size_2(self) -> None:
     for element in [35, -55]:
      result = binary_search_rec(
        list_of_items=LIST_SIZE_2,
        target=element,
        left=0,
        right=len(LIST_SIZE_2) - 1)
      self.assertIsNone(result)

  def test_fail_search_unsorted_list_size_2(self):
    reverted_list = LIST_SIZE_2[::-1]
    result = binary_search_rec(
      list_of_items=reverted_list,
      target=34,
      left=0,
      right=len(reverted_list) - 1)
    self.assertIsNone(result)

  # LIST SIZE 3
  def test_success_search_elements_list_size_3(self) -> None:
    for index, element in enumerate(LIST_SIZE_3):
      result = binary_search_rec(
        list_of_items=LIST_SIZE_3,
        target=element,
        left=0,
        right=len(LIST_SIZE_3) - 1)
      self.assertEqual(result, index)

  def test_fail_search_for_non_existents_list_size_3(self) -> None:
     for element in [110, -111, 567]:
      result = binary_search_rec(
        list_of_items=LIST_SIZE_3,
        target=element,
        left=0,
        right=len(LIST_SIZE_3) - 1)
      self.assertIsNone(result)

  def test_fail_search_unsorted_list_size_3(self) -> None:
    reverted_list = LIST_SIZE_3[::-1]
    result = binary_search_rec(
      list_of_items=reverted_list,
      target=111,
      left=0,
      right=len(reverted_list) - 1)
    self.assertIsNone(result)

  # LIST SIZE 10
  def test_success_search_elements_list_size_10(self) -> None:
    for index, element in enumerate(LIST_SIZE_10):
      result = binary_search_rec(
        list_of_items=LIST_SIZE_10, 
        target=element, 
        left=0, 
        right=len(LIST_SIZE_10) - 1)
      self.assertEqual(result, index)

  def test_fail_search_for_non_existents_list_size_10(self) -> None:
     for element in [11, -10, 100]:
      result = binary_search_rec(
        list_of_items=LIST_SIZE_10, 
        target=element, 
        left=0, 
        right=len(LIST_SIZE_10) - 1)
      self.assertIsNone(result)

  def test_fail_search_unsorted_list_size_10(self) -> None:
    reverted_list = LIST_SIZE_10[::-1]
    result = binary_search_rec(
      list_of_items=reverted_list, 
      target=10, 
      left=0, 
      right=len(reverted_list) - 1)
    self.assertIsNone(result)


def build_suite():
    suite = TestSuite()
    for test_case in [TestBinarySearch, TestBinarySearchRecursive]:
      tests = TestLoader().loadTestsFromTestCase(test_case)
      suite.addTests(tests)
    return suite


if __name__ == "__main__":
  runner = TextTestRunner()
  runner.run(build_suite())
  