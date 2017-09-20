def long_repeat(line):
    if len(line) > 1:
        count = 1
        l = []
        for w in range(0,len(line)-1):
            if line[w] == line[w + 1]:
                count += 1
                l.append(count)
            else:
                count = 1
        if len(l) > 0:
            return (max(l))
        return 1
    
    else:
        return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')

