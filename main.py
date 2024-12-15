def main(path_to_file):
    print(f"--- Starting report on {path_to_file} ---")
    file_contents = open_file(path_to_file)

    words = count_words(file_contents)
    print(f"Number of words: {words}")
    
    total_count = count_characters(file_contents)
    for item in  total_count:
        print(f"the {item} occurs {total_count[item]} times")

    print("--- End report ---")

def open_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(data):
    split_data = data.split()
    words = len(split_data)
    return words

def count_characters(file_contents):
    total_count = {}
    for char in file_contents:
        letter = char.lower()
        if letter in total_count:
            total_count[letter] += 1
        else:
            total_count[letter] = 1
    return total_count

main('books/frankenstein.txt')