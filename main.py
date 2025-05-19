from stats import count_words, char_count, sorted_report
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		content = f.read()
	return content

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		Path = sys.argv[1]
		fulltext = get_book_text(Path)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {Path}")
		print("----------- Word Count ----------")
		print(f"Found {count_words(fulltext)} total words")
		print("--------- Character Count -------")
		for dict in sorted_report(char_count(fulltext)):
			print(f"{dict['name']}: {dict['num']}")
		print("============= END ===============")

main()
