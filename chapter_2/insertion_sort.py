"""
Insertion sort implementation in python
"""

def insertion_sort(numbers):
    """
    Sorting numbers in descending order
    """
    for i in range(1, len(numbers)):
        r_index = i

        for j in range(i - 1, -1, -1):

            if numbers[r_index] <= numbers[j]:
                break

            else:
                numbers[r_index], numbers[j] = numbers[j], numbers[r_index]
                r_index = j


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]
    insertion_sort(numbers)
    assert numbers == [5, 4, 3, 2, 1], "simple sort"

    numbers = [1, 1, 1, 1, 1]
    insertion_sort(numbers)
    assert numbers == [1, 1, 1, 1, 1]

    numbers = [3, 2, 1, 4, 5]
    insertion_sort(numbers)
    assert numbers == [5, 4, 3, 2, 1]

    numbers = [5, 4, 3, 2, 1]
    insertion_sort(numbers)
    assert numbers == [5, 4, 3, 2, 1]
