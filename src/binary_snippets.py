from itertools import izip

def pairwise(iterable):
    '''Returns an iterator that yields elements from the iterable in pairs

    >>> list(pairwise('abcdefgh'))
    [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h')]
    >>> list(pairwise('abcdefghi'))
    [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h')]
    '''
    #courtesy of http://stackoverflow.com/a/5389547/1451794
    a = iter(iterable)
    return izip(a, a)

def beautify_hex(iterable):
    '''Turns a hex without spaces into one with spaces.

    >>> beautify_hex('010203')
    '01 02 03'
    '''
    stuff = pairwise(iterable)
    return ' '.join((i + j for i, j in stuff))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
