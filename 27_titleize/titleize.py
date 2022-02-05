def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase_list = phrase.rsplit(' ')

    return ' '.join(word.capitalize() for word in phrase_list)

    # solution pointed out the .title() method for strings, which is built-in to do this function