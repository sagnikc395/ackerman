import click
from constants import ASCII 


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


@click.command(context_settings={"show_default": True})
@click.option("--src",default='',help='The source string.')
@click.option("--dest",default='',help='The destination string.')
@click.pass_context
def main(ctx,src,dest):
    '''
    compute the levenshtein distance bw two strings.
    '''
    click.secho(ASCII,fg='green',bold=True)

    #show help if both options are empty
    if not src and not dest:
        click.echo(ctx.get_help())
        return

    distance = lev(src,dest)
    click.secho(f">>> Levenshtein distance bw '{src}' and '{dest}' is {distance}",fg='green')
    

        
if __name__ == "__main__":
    main()
