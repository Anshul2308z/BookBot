import sys ;    #https://docs.python.org/3/library/sys.html#sys.argv

if len(sys.argv) != 2:  #https://www.boot.dev/lessons/7b6379ff-8a74-45fe-8084-a79f9680a371
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import  totalWords, charCount, charSorter

def get_book_text(filePath):
    with open(filePath) as f :
        return f.read();



def main():

    path = sys.argv[1]

    output = get_book_text(path)

    sortedDict = charSorter(charCount(output));
    char_lines  = "\n".join(f"{item['char']}: {item['num']}" for item in sortedDict);

    print(f"""
        ============ BOOKBOT ============
    Analyzing book found at {path}
    ----------- Word Count ----------
    Found {totalWords(output)} total words
    --------- Character Count -------
    {char_lines}
    ============= END =============== """)

main();

