def get_word_count(text):
  words = text.split()
  return len(words)
#len counts the length of the list already for you there
#was no need to create a for loop for this function
#the two lines above accomplish this perfectly!
def get_character_frequency(text):
  character_dict = {}
  lowercase_text = text.lower()
  for char in lowercase_text:
    if char in character_dict:
      character_dict[char] += 1
    else:
      character_dict[char] = 1
  return character_dict

def sort_on(char_dict_entry):
  return char_dict_entry["num"]

def get_sorted_char_dict(character_dict):
  sorted_list = []
  for char in character_dict:
    if char.isalpha() == True:
      num = character_dict[char]
      char_dict_entry = {"char": char, "num": num}
      sorted_list.append(char_dict_entry)
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list