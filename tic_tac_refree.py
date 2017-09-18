# CheckIO - Home Challenge 5 : Xs and Os Referee
# http://checkio.org

# Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O)
# who take turns marking the spaces in a 3×3 grid. 
# The player who succeeds in placing three respective marks in a horizontal, vertical, 
# or diagonal rows (NW-SE and NE-SW) wins the game.
# But we will not be playing this game. You will be the referee for this games results. 
# You are given a result of a game and you must determine if the game ends in a win 
# or a draw as well as who will be the winner. 
# Make sure to return "X" if the X-player wins and "O" if the O-player wins. 
# If the game is a draw, return "D".
# A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.
# Input: A game result as a list of strings (unicode).
# Output: "X", "O" or "D" as a string.
# Precondition:
#   There is either one winner or a draw.
#   len(game_result) == 3
#   all(len(row) == 3 for row in game_result)

def checkio(data):
    
    # Checking rows
    i=0
    while i<3:
        line=data[i]
        if (line=="XXX"): return "X"
        if (line=="OOO"): return "O"
        i+=1
        
    # Checking collumns
    j=0
    while j<3:
        column= data[0][j] +  data[1][j] +  data[2][j]
        if (column=="XXX"): return "X"
        if (column=="OOO"): return "O"
        j+=1
    
    # Checking diagonals
    d1=data[0][0] +  data[1][1] +  data[2][2]
    d2=data[2][0] +  data[1][1] +  data[0][2]
    print("D1: " + d1 + " - D2: " + d2)
    diagonals=[d1,d2]
    k=0
    while k<2:
        diagonal=diagonals[k]
        if (diagonal=="XXX"): return "X"
        if (diagonal=="OOO"): return "O"
        k+=1
    
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",