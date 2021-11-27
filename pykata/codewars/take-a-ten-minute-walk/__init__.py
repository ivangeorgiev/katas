"""
You live in the city of Cartesia where all roads are laid out in a 
perfect grid. You arrived ten minutes too early to an appointment, 
so you decided to take the opportunity to go for a short walk. 
The city provides its citizens with a Walk Generating App on their 
phones -- everytime you press the button it sends you an array of 
one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
You always walk only a single block for each letter (direction) 
and you know it takes you one minute to traverse one city block, 
so create a function that will return true if the walk the app gives 
you will take you exactly ten minutes (you don't want to be early or late!) 
and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of 
direction letters ('n', 's', 'e', or 'w' only). It will never give you an 
empty array (that's not a walk, that's standing still!).

https://www.codewars.com/kata/54da539698b8a2ad76000228/python
"""

from functools import reduce

# Decode walk steps into horizontal and vertical distances.
STEPS_MAP = {
    'e': ( 1, 0),    # We move one step right
    'w': (-1, 0),    # We move one step left
    'n': ( 0, 1),    # We move one step up
    's': ( 0,-1),    # We move one step down
}

def is_valid_walk(walk):
    """
    >>> is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
    True

    >>> is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])
    False
    
    >>> is_valid_walk(['w'])
    False

    >>> is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])
    False
    
    """
    # Each walk should last exactly 10 minutes, which translated to Python means
    # that our walk array has exactly 10 elements.
    if len(walk) != 10:
        return False
    # Next step is to make sure that the number of steps north is equal to the number
    # of steps south and that number of steps east equals number of steps west.
    #
    # We could do this using something like: walk.count('n') == walk.count('s'),
    # but we will apply more interesting approach for the sake of challenge and
    # to exercise some functional programming.
    #
    # Lets transform our walk from character directions into steps. Each step
    # is a two element tuple (horizontal_distance, vertical_distance).
    steps = [STEPS_MAP[step] for step in walk]
    # We can sum/reduce the steps to find how far are we from the starting point.
    # We do not need to pass initial value as our walk is always exactly 10 steps
    final_delta = reduce(lambda d1, d2: (d1[0] + d2[0], d1[1] + d2[1]), steps)
    # We should be exactly 0 steps away horizontally and 0 steps away vertically.
    return final_delta == (0, 0)

if __name__ == "__main__": # pragma: no cover
    import doctest
    doctest.testmod()
