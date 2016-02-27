from random import sample

def merge(collection, start, mid, end):

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

    if left:
        for i in range(index, index + len(left)):
            collection[i] = left.pop()

    if right:
        for i in range(index, index + len(right)):
            collection[i] = right.pop()


def merge_sort(collection, start, end):

    if start < end:
        mid = start + (end - start) // 2
        merge_sort(collection, start, mid)
        merge_sort(collection, mid + 1, end)
        merge(collection, start, mid, end)


if __name__ == "__main__":

    collection = [5, 4, 3, 2, 1]
    merge_sort(collection, 0, len(collection) - 1)
    assert collection == [1, 2, 3, 4, 5]
    
    collection = []
    merge_sort(collection, 0, len(collection) - 1)
    assert collection == []
    
    collection = [5]
    merge_sort(collection, 0, len(collection) - 1)
    assert collection == [5]
    
    collection = [1, 2, 3, 4, 5]
    merge_sort(collection, 0, len(collection) - 1)
    assert collection == [1, 2, 3, 4, 5]
    
    collection = [ -1, -2, -3, -4, -5]
    merge_sort(collection, 0, len(collection) - 1)
    assert collection == [-5, -4, -3, -2, -1]
    
    collection = [5.1, 4.2, 3.3, 2.4, 1.5]
    merge_sort(collection, 0, len(collection) - 1)
    assert collection == [1.5, 2.4, 3.3, 4.2, 5.1]

    collection = [1, 2, 3, 4, 5]
    merge(collection, 0, (len(collection) - 1) // 2, len(collection) - 1)
    assert collection == [1, 2, 3, 4, 5], collection

    collection = [5, 4, 3, 2, 1]
    merge(collection, 0, (len(collection) - 1) // 2, len(collection) - 1)
    assert collection == [2, 1, 5, 4, 3], collection

    collection = []
    merge(collection, 0, (len(collection) - 1) // 2, len(collection) - 1)
    assert collection == [], collection

    collection = [1]
    merge(collection, 0, (len(collection) - 1) // 2, len(collection) - 1)
    assert collection == [1], collection

    for i in range(1000):
        l = sample(range(1000), 10)
        l_old = l
        merge_sort(l, 0, len(l) - 1)

        assert l == sorted(l), l_old
