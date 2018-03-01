box_value = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def printer():
  global box_value
  print(f"   |   |   \n {box_value[0]} | {box_value[1]} | {box_value[2]} \n   |   |   ")
  print('---|---|---')
  print(f"   |   |   \n {box_value[3]} | {box_value[4]} | {box_value[5]} \n   |   |   ")
  print('---|---|---')
  print(f"   |   |   \n {box_value[6]} | {box_value[7]} | {box_value[8]} \n   |   |   ")
  
  
def tic_tac_toe():
  global box_value
  if (box_value[0] == box_value[1] == box_value[2] != ' ') or (box_value[0] == box_value[3] == box_value[6] != ' ') or (box_value[0] == box_value[4] == box_value[8] != ' ') or (box_value[1] == box_value[4] == box_value[7] != ' ') or (box_value[2] == box_value[5] == box_value[8] != ' ') or (box_value[2] == box_value[4] == box_value[6] != ' ') or (box_value[3] == box_value[4] == box_value[5] != ' ') or (box_value[6] == box_value[7] == box_value[8] != ' '):
    return True
  else:
    return False
  
  
print("Please enter the box number which you want to fill")
for i in range(9):
  if i % 2 == 0:
    value = input("Player 1 input:")
    box_value[value - 1] = 0
    printer()
    if tic_tac_toe():
      print("Player 1 wins")
      break
  else:
    value = input("Player 2 input:")
    box_value[value - 1] = 'X'
    printer()
    if tic_tac_toe():
      print("Player 2 wins")
      break
