# Let's play! You have to return which player won! In case of a draw return Draw!.
SCISSORS='scissors'
PAPER='paper'
ROCK='rock'


def rps(p1: str, p2: str) ->str:
    if (p1 == SCISSORS and p2 == SCISSORS) or (p1 == PAPER and p2 == PAPER) or (p1 == ROCK and p2 == ROCK):
        return 'Draw!'
    elif (p1 == SCISSORS and p2 == PAPER) or (p1 == PAPER and p2 == ROCK) or (p1 == ROCK and p2 == SCISSORS):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
