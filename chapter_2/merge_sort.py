from random import sample

def merge(collection, start, mid, end):
    """
    Core function for Merge Sort algorithm. Merging two collections into one in
    ascending order.
    """

    left = collection[start : mid + 1]
    right = collection[mid + 1 : end + 1]

    left.reverse()
    right.reverse()

    index = start

    while left and right:
        if left[len(left) - 1] <= right[len(right) - 1]:
            collection[index] = left.pop()
        else:
            collection[index] = right.pop()

        index += 1

    while left:
        collection[index] = left.pop()
        index += 1

    while right:
        collection[index] = right.pop()
        index += 1


def merge_sort(collection, start=None, end=None):
    """
    Sorting collection using merge sort algorithm.
    """

    if start is None or end is None:
        start = 0
        end = len(collection) - 1

    if start < end:
        mid = start + (end - start) // 2

        merge_sort(collection, start, mid)
        merge_sort(collection, mid + 1, end)
        merge(collection, start, mid, end)


if __name__ == "__main__":

    unsorted_collection = [5, 4, 3, 2, 1]
    merge_sort(unsorted_collection, 0, len(unsorted_collection) - 1)
    assert unsorted_collection == [1, 2, 3, 4, 5]

    unsorted_collection = []
    merge_sort(unsorted_collection, 0, len(unsorted_collection) - 1)
    assert unsorted_collection == []

    unsorted_collection = [5]
    merge_sort(unsorted_collection, 0, len(unsorted_collection) - 1)
    assert unsorted_collection == [5]

    unsorted_collection = [1, 2, 3, 4, 5]
    merge_sort(unsorted_collection, 0, len(unsorted_collection) - 1)
    assert unsorted_collection == [1, 2, 3, 4, 5]

    unsorted_collection = [ -1, -2, -3, -4, -5]
    merge_sort(unsorted_collection, 0, len(unsorted_collection) - 1)
    assert unsorted_collection == [-5, -4, -3, -2, -1]

    unsorted_collection = [5.1, 4.2, 3.3, 2.4, 1.5]
    merge_sort(unsorted_collection, 0, len(unsorted_collection) - 1)
    assert unsorted_collection == [1.5, 2.4, 3.3, 4.2, 5.1]

    unsorted_collection = [1, 2, 3, 4, 5]
    merge(unsorted_collection, 0, (len(unsorted_collection) - 1) // 2, len(unsorted_collection) - 1)
    assert unsorted_collection == [1, 2, 3, 4, 5], unsorted_collection

    unsorted_collection = [5, 4, 3, 2, 1]
    merge(unsorted_collection, 0, (len(unsorted_collection) - 1) // 2, len(unsorted_collection) - 1)
    assert unsorted_collection == [2, 1, 5, 4, 3], unsorted_collection

    unsorted_collection = []
    merge(unsorted_collection, 0, (len(unsorted_collection) - 1) // 2, len(unsorted_collection) - 1)
    assert unsorted_collection == [], unsorted_collection

    unsorted_collection = [1]
    merge(unsorted_collection, 0, (len(unsorted_collection) - 1) // 2, len(unsorted_collection) - 1)
    assert unsorted_collection == [1], unsorted_collection

    for i in range(1000):
        l = sample(range(1000), 10)
        l_old = l
        merge_sort(l, 0, len(l) - 1)

        assert l == sorted(l), l_old
