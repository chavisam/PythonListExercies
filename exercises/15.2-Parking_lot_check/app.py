parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]




#Your code go here:
def get_parking_lot():
  total_slots=0
  available_slots=0
  occupied_slots=0
  state = {
    'total_Slots' : total_slots,
    'available_Slots' : available_slots,
    'occupied_Slots' : occupied_slots
  }
  for i in parking_state:
    for y in i:
      if y ==1:
        occupied_slots = occupied_slots + 1
        total_slots = total_slots + 1
      elif y ==2:
        available_slots = available_slots + 1
        total_slots = total_slots + 1
      else:
        total_slots = total_slots + 1
  
  state = {
    'total_Slots' : total_slots,
    'available_Slots' : available_slots,
    'occupied_Slots' : occupied_slots
  }

  return state

print(get_parking_lot())
  




