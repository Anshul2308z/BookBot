from stats import  totalWords, charCount

def get_book_text(filePath):
    with open(filePath) as f :
        return f.read();



def main():
    
    output = get_book_text("./books/frankenstein.txt")

    # print(output) ; 

    deezWords = totalWords(output)
    print(f"{deezWords} words found in the document");

    charCount(output)


main();

