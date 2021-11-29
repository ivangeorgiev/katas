def add(a, b):
    """Add two numbers.
    
    >>> add(2, 3)
    5

    >>> add(1, 0)
    1

    >>> add(5, -3)
    2
    """
    return a + b

if __name__ == "__main__": # pragma: no cover
    import doctest
    doctest.testmod()
