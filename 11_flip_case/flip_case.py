def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    temp_list = list(phrase)

    swapper = to_swap.lower()

    new_list = []

    for letter in phrase:
        if letter.lower() == swapper:
            new_list.append(letter.swapcase())
        else:
            new_list.append(letter)
    
    res = ''.join(new_list)
    return res