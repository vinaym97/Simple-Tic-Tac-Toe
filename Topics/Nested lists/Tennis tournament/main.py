"""Several warm-up matches have been played at the tennis tournament. You have data on the victories and losses of some players. Save the names of the winners to a list and calculate the total number of victories.

The input format:

On the first line, you'll receive the integer n specifying a number of lines.

The next n lines will look like either Name win or Name loss.

The output format:

On the first line, print out the list of all players that have won a match, repeat the names if necessary.

Then output the total number of victories based on your list."""



number = int(input())
count = 0
list_ = []
while count < number:
    input_ = input()
    list_.append(input_.split())
    count = count + 1
win = [tournament[0] for tournament in list_ if tournament[1] == "win"]
print(win)
print(len(win))
