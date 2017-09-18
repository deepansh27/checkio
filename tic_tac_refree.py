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
    
    
    # checking for rows
    i = 0
    while i < 3:
        row = data[i]
        if row =='XXX':
            return 'X'
        if row =="OOO":
            return "O"
        i += 1
        
    # checking for columns
    j = 0
    while j < 3:
        col = data[0][j]+ data[1][j]+data[2][j]
        if col =='XXX':
            return 'X'
        if col =="OOO":
            return "O"
        j += 1
    
    
    # check for diagonals
    
    d1 = data[0][0] + data[1][1] + data[2][2]
    d2 = data[0][2] + data[1][1] + data[2][0]
    
    diagonals = [d1,d2]
    
    d= 0
    while d < 2:
        diagonal = diagonals[d]
        if diagonal=="XXX":
            return 'X'
        if diagonal=="OOO":
            return 'O'
        d += 1
    
    return 'D'   

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
        "XOO"]) == "X", "Xs wins again"
    
print("success")