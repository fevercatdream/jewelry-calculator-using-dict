jewelry_types = {
  "earrings": 524.5, 
  "necklace": 900, 
  "ring": 550.75,
  "bracelet" : 700
}

gem_types = {
  "ruby": 200, 
  "sapphire": 230, 
  "emerald": 400,
  "diamond" : 1000
}


def buy_jewelry(jewelry_type, gems):
  total = 0
  total += jewelry_types[jewelry_type]
  for i in range(len(gems)):
    total += gem_types[gems[i]]
  # print("The cost is ${:.2f}".format(total))
  return total

def list_to_string(my_list):
  if len(my_list) == 0:
    return ""
  if len(my_list) == 1:
    return my_list[0]
  if len(my_list) == 2:
    return f"{my_list[0]} & {my_list[1]}"
  if len(my_list) > 1:
    output = ''
    for i in range(len(my_list)):
      if i < len(my_list) - 2:
        output += f"{my_list[i]} , "
      elif i == len(my_list) - 2:
        output += f"{my_list[i]},"
      else:
        output += f" & {my_list[i]}"
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

  # value = buy_jewelry(jewelry, gems)

# jewelry = "earrings"
# gems = ["ruby", "emerald"]
# value = buy_jewelry(jewelry, gems)

# print(f"The cost of a {jewelry} with {list_to_string(gems)} is: " + "${:.2f}".format(value))
# buy_jewelry("necklace", [])

  # print(f"The cost is: " + "${:.2f}".format(value))

# __name__ is the name the main module/function
if __name__ == "__main__":
    main()