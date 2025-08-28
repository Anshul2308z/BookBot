import string
chars = string.ascii_lowercase + string.digits + string.punctuation + string.whitespace


def totalWords(string):
    words = string.split();
    return len(words);

def charCount(string):
    dict = {} 
    text = string.lower() ; 
    for char in chars :
        for c in text: 
            if char == c :
                if char in dict :
                    dict[char] += 1 ;
                else :
                    dict[char] = 1 ;
    print(dict);
