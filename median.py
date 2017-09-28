def checkio(data):

    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        median = int(len(sorted_data)/2)
        return(sorted_data[median])
    else:
        median_lower = sorted_data[int(len(sorted_data)/2)]
        median_upper = sorted_data[int(len(sorted_data)/2)- 1]
        median = float(median_lower + median_upper)/2
        return median

  

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")
