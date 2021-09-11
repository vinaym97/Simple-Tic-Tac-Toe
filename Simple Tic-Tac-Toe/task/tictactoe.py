user = input("Enter cells: ")
first = list(user[:3])
second = list(user[3:6])
third = list(user[6:9])
user_input = [first,second,third]
print("---------")
print("| "+user_input[0][0]+" "+user_input[0][1]+" "+user_input[0][2]+" |")
print("| "+user_input[1][0]+" "+user_input[1][1]+" "+user_input[1][2]+" |")
print("| "+user_input[2][0]+" "+user_input[2][1]+" "+user_input[2][2]+" |")
print("---------")
for x in user_input:
    if x == "X":
        list_.append(x)
    if x == "O":
        list

X = []


def nest_count(list_, symbol):
    total = sum(x.count(symbol) for x in list_)
    return int(total)


for i in range(3):
    if (user_input[0][i] == 'X' and user_input[1][i] == 'X' and user_input[2][i] == 'X') or (
            user_input[i][0] == 'X' and user_input[i][1] == 'X' and user_input[i][2] == 'X'):
        X.append('win')
    if (user_input[0][i] == 'O' and user_input[1][i] == 'O' and user_input[2][i] == 'O') or (
            user_input[i][0] == 'O' and user_input[i][1] == 'O' and user_input[i][2] == 'O'):
        X.append('lose')

if (user_input[0][0] == 'X' and user_input[1][1] == 'X' and user_input[2][2] == 'X') or (
        user_input[0][2] == 'X' and user_input[1][1] == 'X' and user_input[2][0] == 'X'):
    X.append('win')
elif (user_input[0][0] == 'O' and user_input[1][1] == 'O' and user_input[2][2] == 'O') or (
        user_input[0][2] == 'O' and user_input[1][1] == 'O' and user_input[2][0] == 'O'):
    X.append('lose')

if X.count('win') == 1 and X.count('lose') == 1 or (nest_count(user_input, "X") - nest_count(user_input, "O") >= 2) or (
        nest_count(user_input, "O") - nest_count(user_input, "X") >= 2):
    print("Impossible")
elif X.count('win') == 1:
    print("X wins")
elif X.count('lose') == 1:
    print("O wins")
elif (X.count('win') != 1 and X.count('lose') != 1) and (nest_count(user_input, "_") > 0):
    print("Game not finished")
elif (X.count('win') != 1 and X.count('lose') != 1) and (nest_count(user_input, "_") == 0):
    print("Draw")


coordinates = input("Enter Coordinates").split()