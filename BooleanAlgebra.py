OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def conjunction(a, b):
    return a and b


def disjunction(a, b):
    return a or b


def implication(a, b):
    if a: return b
    return 1


def exclusive(a, b):
    return (a and not b) or (b and not a)


def equivalence(a, b):
    return a == b


def boolean(a, b, argument):
    switcher = {
        'conjunction': conjunction(a, b),
        'disjunction': disjunction(a, b),
        'implication': implication(a, b),
        'exclusive': exclusive(a, b),
        'equivalence': equivalence(a, b),
        '': lambda : False

    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda :False)
    if argument in OPERATION_NAMES:
        # Execute the function
        return func
    else:
        False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
