# # Please reference the included PDF for complete instructions.
# #
# # You can create your table (from the instructions) using a doc or spreadsheet.
# #
# # Advanced students should attempt to implement
# # Rock, Paper, Scissors, Lizard, Spock using 3 or 4 players instead (This is much harder.)
# # 1. Ask player 1 for their move.
# move1 = input('Rock, paper, or scissors?')
# print(move1)
#
# # 3. Ask player 2 for their move.
# move2 = input('Rock, paper, or scissors?')
# print(move2)
#
# # 5. Print out the winner or 'tie'
# if move1 == move2:
#     print('tie')
# elif move1 == 'Rock':
#     if move2 == 'paper':
#         print('P2 wins!')
#     else:
#         print('P1 wins!')
# elif move1 == 'paper':
#     if move2 == 'scissors':
#         print('P2 wins!')
#     else:
#         print('P1 wins!')
# elif move1 == 'scissors':
#     if move2 == 'Rock':
#         print('P2 wins!')
#     else:
#         print('P1 wins!')
# else:
#     print('bad move')
n=10
i=10
while i>0:
    print(i)
    if i % 2 == 0:
        i = 1/2
    else:
        i = i + 1