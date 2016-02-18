def bin_sum(n, SeriesA, SeriesB):
    SeriesC = []
    add = 0

    for i in range(0, n):
        if sum([add, SeriesA[i], SeriesB[i]]) == 0:
            SeriesC.append(0)

        elif sum([add, SeriesA[i], SeriesB[i]]) == 1:
            SeriesC.append(1)
            add = 0

        elif sum([add, SeriesA[i], SeriesB[i]]) == 2:
            SeriesC.append(0)
            add = 1

        elif sum([add, SeriesA[i], SeriesB[i]]) == 3:
            SeriesC.append(1)
            add = 1

    SeriesC.append(add)

    return SeriesC


if __name__ == "__main__":

    n = 3
    SeriesA = [1, 1, 1]
    SeriesB = [0, 0, 0]
    assert bin_sum(n, SeriesA, SeriesB) == [1, 1, 1, 0]

    n = 3
    SeriesA = [1, 1, 1]
    SeriesB = [1, 1, 1]
    assert bin_sum(n, SeriesA, SeriesB) == [0, 1, 1, 1]

    n = 3
    SeriesA = [0, 0, 0]
    SeriesB = [0, 0, 0]
    assert bin_sum(n, SeriesA, SeriesB) == [0, 0, 0, 0]
