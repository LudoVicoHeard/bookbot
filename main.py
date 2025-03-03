from stats import char_counts, word_count

def main():
    path = "books/frankenstein.txt"

    book_text = get_book_text(path)
    wc = word_count(book_text)
    char_list_and_count = char_counts(book_text)

    print(f"{wc} words found in the document")
    print(f"{char_list_and_count}")

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text
    
main()

