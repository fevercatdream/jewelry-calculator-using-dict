jewelry_types = {
  "earrings": 524.5, 
  "necklace": 900, 
  "ring": 550.75}

gem_types = {
  "ruby": 200, 
  "sapphire": 230, 
  "emerald": 400}


def buy_jewelry(jewelry_type, gems):
  total = 0
  total += jewelry_types[jewelry_type]
  for i in range(len(gems)):
    total += gem_types[gems[i]]
  return total


def list_to_string(my_list):
  output = ''
  for i in range(len(my_list)):
    if i != len(my_list) - 1:
      output += f"{my_list[i]} & "
    else:
      output += my_list[i]
  return output


def string_to_list(my_string):
  split_string = my_string.split(",")
  for i in range(len(split_string)):
    split_string[i] = split_string[i].strip()
  return split_string

def gems_valid(gems):
  for i in range(len(gems)):
    if gem_types.get(gems[i]) == None:
      return False
  return True

def main():
  jewelry = input("Select a jewelry type\n").strip().lower()
  while jewelry_types.get(jewelry) == None:
    jewelry = input("Select a jewelry type\n").strip().lower()
  gems = string_to_list(input("Select gems (comma delimited)\n").strip().lower())
  while not gems_valid(gems):
    gems = string_to_list(input("Select gems (comma delimited)\n").strip().lower())

  value = buy_jewelry(jewelry, gems)


  print(f"The cost of a {jewelry} with {list_to_string(gems)} is: " + "${:.2f}".format(value))


if __name__ == "__main__":
    main()

