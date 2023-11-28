'''
1 2 3 
4 5 6
7 8 9

board = "row" : [1-9]

verticle check
for i in range(9) -> for board.get(i) -> each is unique

horizontal check
for board.value is -> is unique

3x3 check

board.get("row1")[0-2] -> board.get("row2")[0-2] -> board.get("row3")[0-2] -> is unique
board.get("row1")[3-5] -> board.get("row")[3-5] -> board.get("row")[3-5] -> is unique
board.get("row1")[6-8] -> board.get("row")[6-8] -> board.get("row")[6-8] -> is unique

board.get("row4")[0-2] -> board.get("row")[0-2] -> board.get("row")[0-2] -> is unique
board.get("row5")[3-5] -> board.get("row")[3-5] -> board.get("row")[3-5] -> is unique
board.get("row6")[6-8] -> board.get("row")[6-8] -> board.get("row")[6-8] -> is unique

board.get("row7")[0-2] -> board.get("row")[0-2] -> board.get("row")[0-2] -> is unique
board.get("row8")[3-5] -> board.get("row")[3-5] -> board.get("row")[3-5] -> is unique
board.get("row9")[6-8] -> board.get("row")[6-8] -> board.get("row")[6-8] -> is unique



'''


board = {
		"row1" : [1,2,3,4,5,6,7,8,9],
		"row2" : [1,2,3,4,5,6,7,8,9],
		"row3" : [1,2,3,4,5,6,7,8,9],
		"row4" : [1,2,3,4,5,6,7,8,9],
		"row5" : [1,2,3,4,5,6,7,8,9],
		"row6" : [1,2,3,4,5,6,7,8,9],
		"row7" : [1,2,3,4,5,6,7,8,9],
		"row8" : [1,2,3,4,5,6,7,8,9],
		"row9" : [1,2,3,4,5,6,7,8,9]}

def print_game(board):
	for v in board.values():
		output = str(v[0])
		for i in range(1,len(v)):
			output +='|'+str(v[i])
		print(output)


def is_vert(board):
	r1, r2, r3, r4, r5, r6, r7, r8, r9 = list(), list(), list(), list(), list(), list(), list(), list(), list()
	inverted_board = dict()
	for v in board.values():
		r1.append(v[0])
		r2.append(v[1])
		r3.append(v[2])
		r4.append(v[3])
		r5.append(v[4])
		r6.append(v[5])
		r7.append(v[6])
		r8.append(v[7])
		r9.append(v[8])
	# print(r1, r3)
	inverted_board["row1"] = r1
	inverted_board["row2"] = r2
	inverted_board["row3"] = r3
	inverted_board["row4"] = r4
	inverted_board["row5"] = r5
	inverted_board["row6"] = r6
	inverted_board["row7"] = r7
	inverted_board["row8"] = r8
	inverted_board["row9"] = r9
	# print(inverted_board)

	return(is_horizontal(inverted_board)) 


def is_horizontal(board):
	for v in board.values():
		found = dict()
		l =list()
		l += v
		for i in range(len(v)):

			l.remove(v[i])
			if v[i] in l:
				return False
			else:
				found[i] = v[i]
	return True



def is_mini(board):
	r1, r2, r3, r4, r5, r6, r7, r8, r9 = board.values()
	# print (vals)
	new_board = dict()
	new_board["row1"] = r1[0:3]+r2[0:3]+r3[0:3]
	new_board["row2"] = r1[3:6]+r2[3:6]+r3[3:6]
	new_board["row3"] = r1[6:]+r2[6:]+r3[6:]
	new_board["row4"] = r4[0:3]+r5[0:3]+r6[0:3]
	new_board["row5"] = r4[3:6]+r5[3:6]+r6[3:6]
	new_board["row6"] = r4[6:]+r5[6:]+r6[6:]
	new_board["row7"] = r7[0:3]+r8[0:3]+r9[0:3]
	new_board["row8"] = r7[3:6]+r8[3:6]+r9[3:6]
	new_board["row9"] = r7[6:]+r8[6:]+r9[6:]

	return is_horizontal(new_board)








# print_game(board)
# print(is_horizontal(board))
# print(is_vert(board))
print(is_mini(board))

