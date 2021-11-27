import re

def maskify(cc):
    """Changes all but the last four characters into '#'.
    
    >>> maskify("4556364607935616")
    '############5616'

    >>> maskify("64607935616")
    '#######5616'

    >>> maskify("1")
    '1'

    >>> maskify("")
    ''
    
    >>> maskify("Nananananananananananananananana Batman!")
    '####################################man!'
    """
    result = re.sub('.(?=....)', '#', cc)
    return result

if __name__ == "__main__": # pragma: no cover
    import doctest
    doctest.testmod()

