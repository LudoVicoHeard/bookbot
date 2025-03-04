import sys
from stats import char_counts, word_count, sorted_alpha_chars

def main():

    if sys.argv.count != 2:
        print("Usage: python3 main.py <path_to_book>")
    

    path = sys.argv[1]

    book_text = get_book_text(path)
    wc = word_count(book_text)
    char_list_and_count = char_counts(book_text)
    sorted_alpha_output = sorted_alpha_chars(char_list_and_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for item in sorted_alpha_output:
        print(f"{item[0]}: {item[1]}")
    print("============= END ===============")


    #print(f"{wc} words found in the document")
    #print(sorted_alpha_output)

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

    
main()

