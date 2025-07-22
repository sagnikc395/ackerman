
def lev(s1: str,s2:str) -> None:
    '''
        return the levenshtein distance bw the strings
        s1 -> source
        s2 -> dest ie thing we wanna achieve by manipualting s1 
    '''

    # case 1 : s1 is empty,
    #  basically add all character of s2 to s1 to turn to s1
    if len(s1) == 0:
        return len(s2)
    # case 2 : s2 is empty
    # the number of actions we have to do is the length
    # of the s1  
    if len(s2) == 0: 
        return len(s1)

    # recursively call on last element , until the size becomes 0
    # using divide and conquer

    # add a character , cause source is reduced, but target is increased.
    lev(s1[:-1],s2)
    # remove a character, cause destination is reduces, source same size
    lev(s1,s2[:-1])

    assert False, "not implemented"

def main():
    print(lev("apple","dapple"))
    print(lev("apple","apple"))

if __name__ == "__main__":
    main()
