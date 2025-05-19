def count_words(text):
	wordlist = text.split()
	return len(wordlist)

def char_count(text):
	chardict = {}
	textfix = text.lower()
	for char in textfix:
		if char in chardict:
			chardict[char] += 1
		else:
			chardict[char] = 1
	return chardict

def sort_on(dict):
	return dict['num']

def sorted_report(dict):
	newdict = {}
	sorted = []
	for key in dict:
		if key.isalpha():
			newdict = {
				'name': key, 
				'num': dict[key]
			}
			sorted.append(newdict)
	sorted.sort(reverse=True, key=sort_on)	
	return sorted
