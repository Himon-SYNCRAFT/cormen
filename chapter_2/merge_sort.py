from random import sample

def merge(collection, start, mid, end):
    left = collection[start: mid]
    right = collection[mid: end + 1]
    tmp_collection = []

    left_index = 0
    right_index = 0

    while left_index != len(left) and right_index != len(right):
        if left[left_index] <= right[right_index]:
            tmp_collection.append(left[left_index])
            left_index += 1
        else:
            tmp_collection.append(right[right_index])
            right_index += 1

    if len(left) > left_index:
        tmp_collection.extend(left[left_index:])

    if len(right) > right_index:
        tmp_collection.extend(right[right_index:])

    tmp_collection.reverse()

    for i in range(start, end + 1):
        collection[i] = tmp_collection.pop()


def merge_sort(collection, start, end):
    if start < end:
        mid = start + ((end - start) // 2)
        merge_sort(collection, start, mid)
        merge_sort(collection, mid + 1, end)
        merge(collection, start, mid + 1, end)


if __name__ == "__main__":

    collection = [5, 4, 3, 2, 1]
    merge(collection, 0, len(collection) // 2, len(collection) - 1)
    assert collection == [3, 2, 1, 5, 4]

    collection = [1, 5, 2, 4, 3, 0]
    merge(collection, 0, len(collection) // 2, len(collection)  - 1)
    assert collection == [1, 4, 3, 0, 5, 2]

    collection = [1, 1]
    merge(collection, 0, len(collection) // 2, len(collection)  - 1)
    assert collection == [1, 1]

    collection = [1]
    merge(collection, 0, len(collection) // 2, len(collection)  - 1)
    assert collection == [1]

    collection = [5, 4, 3, 2, 1]
    merge_sort(collection, 0, len(collection) - 1)
    assert collection == [1, 2, 3, 4, 5]

    collection = [5, 4, 3, 2, 1]
    merge_sort(collection, 0, len(collection) - 1)
    assert collection == [1, 2, 3, 4, 5]

    for i in range(1000):
        l = sample(range(1000), 10)
        l_old = l
        merge_sort(l, 0, len(l) - 1)

        assert l == sorted(l), l_old
