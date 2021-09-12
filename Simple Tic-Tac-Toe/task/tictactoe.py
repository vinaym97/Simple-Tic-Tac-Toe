def figure(indices):
    print("---------")
    print("| "+indices[0][0]+" "+indices[0][1]+" "+indices[0][2]+" |")
    print("| "+indices[1][0]+" "+indices[1][1]+" "+indices[1][2]+" |")
    print("| "+indices[2][0]+" "+indices[2][1]+" "+indices[2][2]+" |")
    print("---------")


def string_to_list(string_):
    first = list(string_[:3])
    second = list(string_[3:6])
    third = list(string_[6:9])
    list_ = [first, second, third]
    return list_


user = input("Enter cells: ")
user = user.replace("_", " ")
user_input = string_to_list(user)
figure(user_input)
while True:
    coordinates = input("Enter Coordinates").split()
    if coordinates[0].isalpha() or coordinates[1].isalpha():
        print("You should enter numbers!")
        continue
    else:
        coordinates = [int(i) for i in coordinates]
        if isinstance(coordinates[0], int) and isinstance(coordinates[1], int):
            x = coordinates[1]
            y = coordinates[0]
            if y > 3 or x > 3:
                print("Coordinates should be from 1 to 3!")
                continue
            elif user_input[y - 1][x - 1] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            user_input[y - 1][x - 1] = 'X'
            break
figure(user_input)




# for x in user_input:
#     if x == "X":
#         list_.append(x)
#     if x == "O":
#         list
#
# X = []
#
#
# def nest_count(list_, symbol):
#     total = sum(x.count(symbol) for x in list_)
#     return int(total)
#
#
# for i in range(3):
#     if (user_input[0][i] == 'X' and user_input[1][i] == 'X' and user_input[2][i] == 'X') or (
#             user_input[i][0] == 'X' and user_input[i][1] == 'X' and user_input[i][2] == 'X'):
#         X.append('win')
#     if (user_input[0][i] == 'O' and user_input[1][i] == 'O' and user_input[2][i] == 'O') or (
#             user_input[i][0] == 'O' and user_input[i][1] == 'O' and user_input[i][2] == 'O'):
#         X.append('lose')
#
# if (user_input[0][0] == 'X' and user_input[1][1] == 'X' and user_input[2][2] == 'X') or (
#         user_input[0][2] == 'X' and user_input[1][1] == 'X' and user_input[2][0] == 'X'):
#     X.append('win')
# elif (user_input[0][0] == 'O' and user_input[1][1] == 'O' and user_input[2][2] == 'O') or (
#         user_input[0][2] == 'O' and user_input[1][1] == 'O' and user_input[2][0] == 'O'):
#     X.append('lose')
#
# if X.count('win') == 1 and X.count('lose') == 1 or (nest_count(user_input, "X") - nest_count(user_input, "O") >= 2) or (
#         nest_count(user_input, "O") - nest_count(user_input, "X") >= 2):
#     print("Impossible")
# elif X.count('win') == 1:
#     print("X wins")
# elif X.count('lose') == 1:
#     print("O wins")
# elif (X.count('win') != 1 and X.count('lose') != 1) and (nest_count(user_input, "_") > 0):
#     print("Game not finished")
# elif (X.count('win') != 1 and X.count('lose') != 1) and (nest_count(user_input, "_") == 0):
#     print("Draw")
