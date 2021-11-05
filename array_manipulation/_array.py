from typing import TypeVar

INITIAL_SIZE = 0
MIN_INITIAL_CAPACITY = 1
MIN_REAL_CAPACITY = 16
GROWTH_FACTOR = 2
SHRINK_FACTOR = 4

INDEX_OUT_OF_RANGE_ERROR = "Index out of range."
NOT_MATCH_VALUE_FOUND_ERROR = "No match value found."


T = TypeVar("T", int, str, None)


class Array:
    def __init__(self, capacity: int = MIN_INITIAL_CAPACITY) -> None:
        """
        Creates a new array according to the provided capacity.

        About: An array is a contiguous area of memory consisting of equal-size
        elements indexed by contiguous integers.

        - Complexity:
            * Constant-time access to any element - O(1);
            * Constant-time to add/remove at the end - O(1);
            * Linear time to add/remove at an arbitrary location - O(n).
        """
        self._size: int = INITIAL_SIZE
        self._capacity: int = self._set_capacity(capacity)
        self.data: list[T] = []

    def append(self, value: T) -> None:
        """
        Add an item to the end of the list.

        - Complexity: O(1)

        Args:
            value: The value that will be add.
        """
        self._upsize_capacity()
        if self.is_empty():
            self.data = [value]
        else:
            self.data += [value]
        self._size += 1

    def insert(self, index: int, value: T) -> None:
        """
        Insert an item at a given position.

            * [index = 0]: Insert the item at the beginning - Complexity: O(n);\n
            * [index > current size or index < 0]: Insert the item at the end
                (is equivalent to append(value)) - Complexity: O(1);\n
            * [index < current size or any other numbers]: Insert the item among
                other elements - Complexity: O(n).
        --------

        Args:
            index: The index where you want to insert the value.
            value: The value that will be insert.

        Raises:
            ValueError: If the index is not an Integer
        """
        self._validate_index_type(index)

        self._upsize_capacity()
        if index == INITIAL_SIZE:  # Insert the element at the beginning
            shifted_array = [value]
            for item in self.data:
                shifted_array += [item]
            self.data = shifted_array
            self._size += 1
        elif (
            index > self._size or index < INITIAL_SIZE
        ):  # Insert the element at the end
            self.append(value)
        else:  # Insert the element among other elements
            left_content = self.data[:index]
            right_content = self.data[index:]

            left_content += [value]
            for item in right_content:
                left_content += [item]

            self.data = left_content
            self._size += 1

    def at(self, index: int) -> T:
        """
        Returns item at given index.

        - Complexity: O(1)

        Args:
            index: Index where the item is found.

        Raises:
            - IndexError: If index out of range.
            - ValueError: If the index is not an Integer.

        Return:
            T: The found item
        """
        self._validate_index_type(index)

        if index < INITIAL_SIZE or index > self._size - 1:
            raise IndexError(INDEX_OUT_OF_RANGE_ERROR)

        return self.data[index]

    def pop(self, index: int = None) -> T:
        """
        Remove a value at the end, and return it.

        - Complexity:
            * O(1) if the index is at the end.
            * O(n) from specific index.

        Args:
            index: Index where the item is found.

        Raises:
            - IndexError:
                * If there is nothing in the array;
                * And if index is greater than size.
            - ValueError: If the index is not an integer.

        Return:
            T: The removed value
        """
        if index is not None:
            self._validate_index_type(index)

        if self.is_empty() or index is not None and index > self._size:
            raise IndexError(INDEX_OUT_OF_RANGE_ERROR)

        target_value: T = None
        if index is None or index < INITIAL_SIZE or index == self._size - 1:
            self._downsize_capacity()
            target_value = self.data[-1]
            del self.data[-1]
            self._size -= 1
        else:
            # Searching...
            for value in self.data:
                if value == self.data[index]:
                    target_value = value
                    self._downsize_capacity()
                    self._reorganize(index)

                    del self.data[-1]
                    self._size -= 1
                    break
            else:
                raise IndexError(INDEX_OUT_OF_RANGE_ERROR)

        return target_value

    def remove(self, target_value: T) -> None:
        """
        Remove the first item from the array that is equal to the target value.

        Complexity: O(n)

        Args:
            target_value: value you want to remove.

        Raises:
            ValueError:
                * if no matching value is found.
        """
        index_found = self.find(target_value)
        self._downsize_capacity()
        self._reorganize(index_found)
        del self.data[-1]
        self._size -= 1

    def remove_all(self, target_values: list[T]) -> None:
        """
        Remove values from the array that are equal to the list of target values.

        Complexity: O(n)

        Args:
            target_values: list of values you want to remove.

        Raises:
            ValueError: If no matching value is found.
        """
        self._downsize_capacity()
        for target in target_values:
            index_found = self.find(target)
            self._reorganize(index_found)
            del self.data[-1]
            self._size -= 1

    def find(self, value: T) -> int:
        """
        Search for the given value and returns its index.

        - Complexity: O(n)

        Args:
            value: value you want to find.

        Raises:
            ValueError: If the value is not found.
        """
        for index, item in enumerate(self.data):
            if item == value:
                break
        else:
            raise ValueError(NOT_MATCH_VALUE_FOUND_ERROR)
        return index

    def is_empty(self) -> bool:
        """Check if the array is empty."""
        return self._size == INITIAL_SIZE

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def _reorganize(self, target_index: int) -> None:
        for i in range(target_index, self._size - 1):
            self.data[i] = self.data[i + 1]

    @staticmethod
    def _set_capacity(capacity: int) -> int:
        """
        Arrays will be created with a minimium of 16 bits (2 bytes) and
        a growth factor of 2.

        Examples:
            * capacity = 8 ->  Real capacity: 16 bits (2 bytes);
            * capacity = 9 ->  Real capacity: 32 bits (4 bytes);
            * capacity = 17 -> Real capacity: 64 bits (8 bytes);
            * ....
        """
        if capacity < MIN_INITIAL_CAPACITY:
            raise ValueError(
                f"The minimium initial capacity must be greater than or equal to {MIN_INITIAL_CAPACITY}"
            )

        real_capacity = MIN_REAL_CAPACITY
        while capacity > real_capacity // GROWTH_FACTOR:
            real_capacity *= GROWTH_FACTOR

        return real_capacity

    def _upsize_capacity(self) -> None:
        if self._size == self._capacity:
            old_capacity = self._capacity
            self._capacity = self._set_capacity(old_capacity)

    def _downsize_capacity(self) -> None:
        if self._size < self._capacity // SHRINK_FACTOR:
            old_capacity = self._capacity
            new_capacity = self._capacity // GROWTH_FACTOR

            if new_capacity < MIN_REAL_CAPACITY:
                new_capacity = MIN_REAL_CAPACITY

            if new_capacity != old_capacity:
                self._capacity = new_capacity

    @staticmethod
    def _validate_index_type(index: int) -> None:
        if not isinstance(index, int):
            raise ValueError("Index must be a integer!")
