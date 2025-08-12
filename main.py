import sys
from stats import(
   get_word_count, 
   get_character_frequency,
   get_sorted_char_dict,
)
if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)
else:
  book_path = sys.argv[1]

def main(book_path):
  text = get_book_text(book_path)
  num_words = get_word_count(text)
  character_frequency = get_character_frequency(text)
  sorted_char_list = get_sorted_char_dict(character_frequency)
  #Boots pointed out I needed to print the result and there
  #is a problem with my file path syntax
  print_report(book_path, num_words, sorted_char_list)


def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

#Make sure your function call isn't within the function
#if it is, it will infinitely call on itself and will
#show nothing on the console at times  
#Other error I ran into, I forgot to include the books
#directory in my main function call this made it so my
#program couldn't find my frankenstein file because
#it was looking relative to where I was running my script
#Any subdirectories need to be included in the path
#Issue I ran into was not using the get_book_text as the
#argument for get_character_frequency so when I passed
#in just the file path the program when thinking this was
#the text and was simply counting the letters/characters
#in the flight path
def print_report(book_path, num_words, sorted_char_list):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for item in sorted_char_list:
    if not item["char"].isalpha():
      continue
    print(f"{item['char']}: {item['num']}")
  print("============= END ===============")


main(book_path)
