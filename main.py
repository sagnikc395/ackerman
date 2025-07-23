def lev(s1: str, s2: str) -> None:
    """
    return the levenshtein distance bw the strings
    s1 -> source
    s2 -> dest ie thing we wanna achieve by manipualting s1
    """

    # case 1 : s1 is empty,
    #  basically add all character of s2 to s1 to turn to s1
    if len(s1) == 0:
        return len(s2)
    # case 2 : s2 is empty
    # the number of actions we have to do is the length
    # of the s1
    if len(s2) == 0:
        return len(s1)

    # case if both the character at the posn match
    if s1[-1] == s2[-1]:
        # ignore compile
        return lev(s1[:-1],s2[:-1])
    
    # recursively call on last element , until the size becomes 0
    # using divide and conquer

    # add a character , cause source is reduced, but target is increased.
    return 1+ min(
        lev(s1[:-1], s2),
        # remove a character, cause destination is reduces, source same size
        lev(s1, s2[:-1]),
        ## remove last character from each of them
        lev(s1[:-1], s2[:-1]),
    )


def main():
    print(lev("apple", "dapple"))
    print(lev("apple", "apple"))
    print(lev("apple","grapple"))
    print(lev("apple","dapled"))
    print(lev("apple","eappla"))

    
if __name__ == "__main__":
    main()
