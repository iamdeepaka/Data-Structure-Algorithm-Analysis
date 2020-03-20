# Time complexity : O(1)

# As there is a finite set of roman numerals, the maximum number possible number can be 3999,
# which in roman numerals is MMMCMXCIX. As such the time complexity is O(1)

# If roman numerals had an arbitrary number of symbols, then the time complexity would be proportional
# to the length of the input, i.e. O(n). This is assuming that looking up the value of each symbol is O(1)

# Space complexity : O(1)O(1).

# Because only a constant number of single-value variables are used, the space complexity is O(1)


def romanToInt(s):
    values_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and values_dict[s[i]] < values_dict[s[i + 1]]:
            # If the symbols are out of numeric order.
            # We subtract the value of i+1 and i to get their total value
            total += values_dict[s[i + 1]] - values_dict[s[i]]
            # jump two places as we are considering
            # both i and i+1 here
            i += 2
        else:
            total += values_dict[s[i]]
            i += 1

    return total
