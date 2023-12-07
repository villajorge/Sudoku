data = {
  "generator": "myv@API: SUDOKU All-Purpose PRO",
  "documentation": "https://myv.at/api/sudoku/",
  "operation": "create",
  "output": {
    "format": "raw",
    "raw_data": "009753180000010706020980300190800030600030000300000520210000409006300000807001060",
    "initial_values": 32
  },
  "status": {
    "notice": "",
    "error": ""
  },
  "created": {
    "on": "Tue, 05 Dec 2023 04:57:27 PM CET",
    "in": "0.0078sec"
  },
  "Thanks": "for using myv@ APIs!"
}

board_string = data["output"]["raw_data"]
board = dict()
for i in range(9):
    temp = board_string[0+i:9+i]
    board["row"+str(i+1)] = temp

print(board)
