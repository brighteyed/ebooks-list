import argparse
import json


def main():
    ap = argparse.ArgumentParser(description="Generate AsciiDoc file for books list")

    ap.add_argument("--input", type = str, default = 'books.json', help = "Json file with books information")
    ap.add_argument("--output", type = str, default = 'books.adoc', help = "Output file")
    args = ap.parse_args()

    with open(args.input, encoding='utf-8') as json_file:
        data = json.load(json_file)

        with open(args.output, 'w', encoding='utf-8') as adoc_file:
            adoc_file.write("== Book list\n\n")
            adoc_file.write(":nofooter:\n")
            adoc_file.write("\n")

            for book in data:
                adoc_file.write("=== ")
                adoc_file.write(", ".join(book["authors"]))
                adoc_file.write(" – ")
                adoc_file.write(book["title"])
                adoc_file.write("\n\n")
                adoc_file.write(book["description"].replace("\n", "\n\n"))
                adoc_file.write("\n\n")


if __name__ == "__main__":
    main()