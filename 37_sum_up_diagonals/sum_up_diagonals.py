def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    to_add = []
    length = len(matrix)

    count = 0
    while count < length:
        tup = (count, count)
        to_add.append(tup)
        count += 1

    count_y = length - 1
    count = 0
    while count_y >= 0:
        tup = (count_y, count)
        to_add.append(tup)
        count_y -= 1
        count += 1

    sum = 0
    for tup in to_add:
        sum += matrix[tup[0]][tup[1]]

    return sum