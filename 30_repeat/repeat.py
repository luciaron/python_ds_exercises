def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    res = ''
    count = num
    if isinstance(phrase, str) and isinstance(num, int):
        while count > 0:
            res = res + phrase
            count -= 1
            print(res, count)
        return res
    else:
        return None

    #solution reminded that strings can be multiplied

    # if not isinstance(phrase, str) or not isinstance(num, int):
    #     return None
    # elif num < 0:
    #     return None
    # else:
    #     return phrase * num