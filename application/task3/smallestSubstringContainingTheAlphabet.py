from string import ascii_lowercase as alphabet


def isStringPangram(input_str):
    if len(input_str) < len(alphabet):
        return False

    return all(i in input_str for i in alphabet)


def smallestSubstringContainingTheAlphabet(input_str):
    if not isinstance(input_str, str):
        print "invalid input: expecting string"
        raise TypeError

    if len(input_str) < len(alphabet):
        return ""

    input_str = input_str.lower()
    for substr_len in range(len(alphabet), len(input_str) + 1):
        for pos in range(0, len(input_str) - substr_len + 1):
            if isStringPangram(input_str[pos:pos+substr_len]):
                return input_str[pos:pos+substr_len]

    return ""
