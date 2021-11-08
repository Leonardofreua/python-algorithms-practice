from unittest import TestCase

from data_structures._array import Array


class TestArrays(TestCase):
    def test_new_array(self) -> None:
        new_array = Array(10)
        self.assertEqual(new_array.size(), 0)
        self.assertEqual(new_array.capacity(), 32)

    def test_integer_append(self) -> None:
        new_array = Array()

        for index, value in enumerate(range(0, 20)):
            new_array.append(value)
            self.assertEqual(new_array.data[index], value)
            self.assertEqual(new_array.size(), index + 1)

    def test_string_append(self) -> None:
        new_array = Array()

        for index, value in enumerate(["hi", "olá", "salut", "Guten Tag", "Anyoung"]):
            new_array.append(value)
            self.assertEqual(new_array.data[index], value)
            self.assertEqual(new_array.size(), index + 1)

    def test_insert_integer_at_the_beginning(self) -> None:
        new_array = Array()

        # [0, 1, 2]
        for value in range(3):
            new_array.append(value)

        new_array.insert(0, 3)
        self.assertEqual(new_array.data[0], 3)
        self.assertEqual(new_array.size(), 4)

        new_array.insert(0, 4)
        self.assertEqual(new_array.data[0], 4)
        self.assertEqual(new_array.size(), 5)

    def test_insert_string_at_the_beginning(self) -> None:
        new_array = Array()

        for value in ["hi", "olá", "salut"]:
            new_array.append(value)

        new_array.insert(0, "Guten Tag")
        self.assertEqual(new_array.data[0], "Guten Tag")
        self.assertEqual(new_array.size(), 4)

        new_array.insert(0, "Anyoung")
        self.assertEqual(new_array.data[0], "Anyoung")
        self.assertEqual(new_array.size(), 5)

    def test_insert_integer_at_the_end(self) -> None:
        new_array = Array()

        # [0, 1, 2]
        for value in range(3):
            new_array.append(value)

        # index > size
        new_array.insert(new_array.size() + 1, 4)
        self.assertEqual(new_array.data[-1], 4)

        # index < 0
        new_array.insert(-1, 5)
        self.assertEqual(new_array.data[-1], 5)

        self.assertEqual(new_array.size(), 5)

    def test_insert_string_at_the_end(self) -> None:
        new_array = Array()

        for value in ["hi", "olá", "salut"]:
            new_array.append(value)

        # index > size
        new_array.insert(new_array.size() + 1, "Guten Tag")
        self.assertEqual(new_array.data[-1], "Guten Tag")

        # index < 0
        new_array.insert(-1, "Anyoung")
        self.assertEqual(new_array.data[-1], "Anyoung")

        self.assertEqual(new_array.size(), 5)

    def test_insert_integer_at_specific_position(self) -> None:
        new_array = Array()

        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for value in range(10):
            new_array.append(value)

        # In place of the 5
        new_array.insert(5, 88)
        # [0, 1, 2, 3, 4, 88, 5, 6, 7, 8, 9]
        self.assertEqual(new_array.data[5], 88)

        # In place of the 9
        new_array.insert(10, 10)
        # [0, 1, 2, 3, 4, 88, 5, 6, 7, 8, 10, 9]
        self.assertEqual(new_array.data[10], 10)

        self.assertEqual(new_array.size(), 12)

    def test_insert_string_at_specific_position(self) -> None:
        new_array = Array()

        for value in ["hi", "olá", "salut", "Guten Tag", "Anyoung", "Goddag"]:
            new_array.append(value)

        # In place of the Guten Tag
        new_array.insert(3, "Ahlan")
        # ["hi", "olá", "salut", "Ahlan", "Guten Tag", "Anyoung", "Goddag"]
        self.assertEqual(new_array.data[3], "Ahlan")

        # In place of the Goddag
        new_array.insert(6, "Yassou")
        # ["hi", "olá", "salut", "Ahlan", "Guten Tag", "Anyoung", "Yassou", "Goddag"]
        self.assertEqual(new_array.data[6], "Yassou")

        self.assertEqual(new_array.size(), 8)

    def test_raise_ValueError_when_insert_with_an_invalid_index_type(self) -> None:
        new_array = Array()

        with self.assertRaises(ValueError):
            new_array.insert("i", 1)

    def test_get_value_from_specific_index(self) -> None:
        new_array = Array()

        for value in range(20):
            new_array.append(value)

        self.assertEqual(new_array.at(19), 19)

    def test_raise_IndexError_getting_value_list_out_of_range(self) -> None:
        new_array = Array()

        with self.assertRaises(IndexError):
            new_array.at(0)

    def test_raise_ValueError_getting_value_with_an_invalid_index_type(self) -> None:
        new_array = Array()

        with self.assertRaises(ValueError):
            new_array.at("i")

    def test_pop_integer_value_at_the_end(self) -> None:
        new_array = Array()

        # [0, 1, 2]
        for value in range(3):
            new_array.append(value)

        self.assertEqual(new_array.size(), 3)

        p1 = new_array.pop()
        # [0, 1]
        self.assertEqual(p1, 2)
        self.assertEqual(new_array.size(), 2)
        self.assertEqual(new_array.data[-1], 1)

        p2 = new_array.pop()
        # [0]
        self.assertEqual(p2, 1)
        self.assertEqual(new_array.size(), 1)
        self.assertEqual(new_array.data[-1], 0)

    def test_pop_string_value_at_the_end(self) -> None:
        new_array = Array()

        for value in ["hi", "olá", "salut", "Guten Tag"]:
            new_array.append(value)

        self.assertEqual(new_array.size(), 4)

        p1 = new_array.pop()
        # ["hi", "olá", "salut"]
        self.assertEqual(p1, "Guten Tag")
        self.assertEqual(new_array.size(), 3)

        p2 = new_array.pop()
        # ["hi", "olá"]
        self.assertEqual(p2, "salut")
        self.assertEqual(new_array.size(), 2)

    def test_raise_IndexError_when_try_pop_value_into_an_empty_array(self) -> None:
        new_array = Array()

        with self.assertRaises(IndexError):
            new_array.pop()

    def test_raise_IndexError_when_try_pop_value_with_an_index_greates_array_size(
        self,
    ) -> None:
        new_array = Array()

        new_array.append(1)
        with self.assertRaises(IndexError):
            new_array.pop(33)

    def test_raise_ValueError_when_try_pop_value_with_a_non_integer_index(
        self,
    ) -> None:
        new_array = Array()

        new_array.append(1)
        with self.assertRaises(ValueError):
            new_array.pop("i")

    def test_pop_integer_value_from_specific_index(self) -> None:
        new_array = Array()

        # [0, 1, 2, 3, 4]
        for value in range(5):
            new_array.append(value)

        p1 = new_array.pop(3)
        # [0, 1, 2, 4]
        self.assertEqual(p1, 3)
        self.assertEqual(new_array.size(), 4)
        self.assertEqual(new_array.data[-1], 4)

        p2 = new_array.pop(2)
        # [0, 1, 4]
        self.assertEqual(p2, 2)
        self.assertEqual(new_array.size(), 3)
        self.assertEqual(new_array.data[-1], 4)

        p3 = new_array.pop(1)
        # [0, 4]
        self.assertEqual(p3, 1)
        self.assertEqual(new_array.size(), 2)
        self.assertEqual(new_array.data[-1], 4)

        p4 = new_array.pop(0)
        # [4]
        self.assertEqual(p4, 0)
        self.assertEqual(new_array.size(), 1)
        self.assertEqual(new_array.data[-1], 4)

        p5 = new_array.pop(0)
        # []
        self.assertEqual(p5, 4)
        self.assertEqual(new_array.size(), 0)

        self.assertTrue(new_array.is_empty())

    def test_pop_string_value_from_specific_index(self) -> None:
        new_array = Array()

        for value in ["hi", "olá", "salut", "Guten Tag"]:
            new_array.append(value)

        self.assertEqual(new_array.size(), 4)

        p1 = new_array.pop(2)
        # ["hi", "olá", "Guten Tag"]
        self.assertEqual(p1, "salut")
        self.assertEqual(new_array.size(), 3)

        p2 = new_array.pop(1)
        # ["hi", "Guten Tag"]
        self.assertEqual(p2, "olá")
        self.assertEqual(new_array.size(), 2)

        p4 = new_array.pop(0)
        # ["Guten Tag"]
        self.assertEqual(p4, "hi")
        self.assertEqual(new_array.size(), 1)

        p4 = new_array.pop(0)
        # []
        self.assertEqual(p4, "Guten Tag")
        self.assertEqual(new_array.size(), 0)

        self.assertTrue(new_array.is_empty())

    def test_raise_ValueError_when_try_remove_a_non_existent_value(self) -> None:
        new_array = Array()

        new_array.append(1)
        with self.assertRaises(ValueError):
            new_array.remove(33)

        with self.assertRaises(ValueError):
            new_array.remove("hi")

    def test_remove_integer_value(self) -> None:
        new_array = Array()

        for value in [1, 2, 3, 4, 4, 5, 6, 6]:
            new_array.append(value)

        new_array.remove(4)
        self.assertListEqual(new_array.data, [1, 2, 3, 4, 5, 6, 6])
        self.assertEqual(new_array.size(), 7)

        new_array.remove(6)
        self.assertListEqual(new_array.data, [1, 2, 3, 4, 5, 6])
        self.assertEqual(new_array.size(), 6)

        new_array.remove(3)
        self.assertListEqual(new_array.data, [1, 2, 4, 5, 6])
        self.assertEqual(new_array.size(), 5)

    def test_remove_string_value(self) -> None:
        new_array = Array()

        for value in [
            "hi",
            "olá",
            "salut",
            "Guten Tag",
            "Guten Tag",
            "Anyoung",
            "Goddag",
            "Goddag",
        ]:
            new_array.append(value)

        new_array.remove("olá")
        self.assertListEqual(
            new_array.data,
            ["hi", "salut", "Guten Tag", "Guten Tag", "Anyoung", "Goddag", "Goddag"],
        )
        self.assertEqual(new_array.size(), 7)

        new_array.remove("Goddag")
        self.assertListEqual(
            new_array.data,
            ["hi", "salut", "Guten Tag", "Guten Tag", "Anyoung", "Goddag"],
        )
        self.assertEqual(new_array.size(), 6)

        new_array.remove("Guten Tag")
        self.assertListEqual(
            new_array.data, ["hi", "salut", "Guten Tag", "Anyoung", "Goddag"]
        )
        self.assertEqual(new_array.size(), 5)

    def test_raise_ValueError_when_try_remove_multiple_non_existent_values(
        self,
    ) -> None:
        new_array = Array()

        new_array.append(1)
        with self.assertRaises(ValueError):
            new_array.remove_all([33, "hi"])

    def test_remove_multiple_integer_values(self) -> None:
        new_array = Array()

        for value in [1, 2, 3, 4, 4, 5, 6, 6]:
            new_array.append(value)

        new_array.remove_all([4, 4])
        self.assertListEqual(new_array.data, [1, 2, 3, 5, 6, 6])
        self.assertEqual(new_array.size(), 6)

        new_array.remove_all([6, 6])
        self.assertListEqual(new_array.data, [1, 2, 3, 5])
        self.assertEqual(new_array.size(), 4)

        new_array.remove_all([3, 5])
        self.assertListEqual(new_array.data, [1, 2])
        self.assertEqual(new_array.size(), 2)

    def test_remove_multiple_string_value(self) -> None:
        new_array = Array()

        for value in [
            "hi",
            "olá",
            "salut",
            "Guten Tag",
            "Guten Tag",
            "Anyoung",
            "Goddag",
            "Goddag",
        ]:
            new_array.append(value)

        new_array.remove_all(["olá", "hi"])
        self.assertListEqual(
            new_array.data,
            ["salut", "Guten Tag", "Guten Tag", "Anyoung", "Goddag", "Goddag"],
        )
        self.assertEqual(new_array.size(), 6)

        new_array.remove_all(["Goddag", "Goddag"])
        self.assertListEqual(
            new_array.data,
            ["salut", "Guten Tag", "Guten Tag", "Anyoung"],
        )
        self.assertEqual(new_array.size(), 4)

        new_array.remove_all(["Guten Tag", "Guten Tag"])
        self.assertListEqual(new_array.data, ["salut", "Anyoung"])
        self.assertEqual(new_array.size(), 2)

    def test_raise_ValueError_when_try_find_a_non_existent_value(self) -> None:
        new_array = Array()

        with self.assertRaises(ValueError):
            new_array.find(1)

        with self.assertRaises(ValueError):
            new_array.find("i")

    def test_find_integer_value(self) -> None:
        new_array = Array()

        for value in [100, 44, 78, 22, 37]:
            new_array.append(value)

        for index, value in enumerate(new_array.data):
            self.assertEqual(new_array.find(value), index)

    def test_find_string_value(self) -> None:
        new_array = Array()

        for value in ["a", "b", "c", "z", "Y", "w"]:
            new_array.append(value)

        for index, value in enumerate(new_array.data):
            self.assertEqual(new_array.find(value), index)


if __name__ == "__main__":
    unittest.main()
