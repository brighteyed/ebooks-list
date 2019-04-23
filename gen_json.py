import argparse
import glob
import json

from ebooklib import epub

class Book:
    
    def __init__(self, authors, title, description):
        self.title = title
        self.authors = []
        self.authors.extend(authors),
        self.description = description


def main():
    ap = argparse.ArgumentParser(description="Save epub books information into json file")

    ap.add_argument("--dir", type = str, default = '.', help = "Root folder with epub files")
    ap.add_argument("--output", type = str, default = 'books.json', help = "Output file")
    args = ap.parse_args()

    books_info = []
    for file in glob.iglob(args.dir + '/**/*.epub', recursive=True):
        book = epub.read_epub(file)

        desc = book.get_metadata("DC", "description")

        books_info.append(Book(list(next(zip(*book.get_metadata("DC", "creator")))),
                                book.get_metadata("DC", "title")[0][0],
                                desc[0][0] if len(desc) else ""))

    with open(args.output, 'w', encoding='utf-8') as file:
        json.dump(books_info, file, ensure_ascii=False, default=lambda o: o.__dict__, indent=4)


if __name__ == "__main__":
    main()