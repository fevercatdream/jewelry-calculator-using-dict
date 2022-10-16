jewlery_types = {
  "earrings": 524.5, 
  "necklace": 900, 
  "ring": 550.75}

gem_types = {
  "ruby": 200, 
  "sapphire": 230, 
  "emerald": 400}


def buy_jewlery(jewelery_type, gems):
  total = 0
  total += jewlery_types[jewelery_type]
  for i in range(len(gems)):
    total += gem_types[gems[i]]
  return total


def list_to_string(my_list):
  output = ''
  for i in range(len(my_list)):
    if i != len(my_list) - 1:
      output += " & "
  return output


def string_to_list(my_string):
  split_string = my_string.split(",")
  for i in range(len(split_string)):
    split_string[i] = split_string[i].strip()
  return split_string


jewlery = input("Select a jewlery type\n")
gems = input("Select gems (comma delimited\n").strip().lower()

value = buy_jewlery(jewlery, string_to_list(gems))

print(value)
