def binary_search(sorted_collection, value):
    """
    Return index if find value in sorted_collection. If not return None
    """
    if len(sorted_collection) == 1:
        if value == sorted_collection[0]:
            return 0
        else:
            return None

    mid = (len(sorted_collection) - 1) // 2

    if value <= sorted_collection[mid]:
        return binary_search(sorted_collection[: mid + 1], value)

    else:
        right = binary_search(sorted_collection[mid + 1 :], value)

        if right is not None:
            right += (mid + 1)

        return right

if __name__ == "__main__":

    assert binary_search([1,2,3,4,5], 1) == 0
    assert binary_search([1,2,3,4,5], 2) == 1
    assert binary_search([1,2,3,4,5], 3) == 2
    assert binary_search([1,2,3,4,5], 4) == 3
    assert binary_search([1,2,3,4,5], 5) == 4
    assert binary_search([1,2,3,4,5], 6) == None
    assert binary_search([1,2,3,4,5], -1) == None
