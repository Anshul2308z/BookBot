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
    return dict;

def sort_on(items):
    return items["num"] ;


def charSorter(dict):
    toReturn = [] ; 
    for char in dict :
        toReturn.append({"char": char, "num": dict[char]});
    
    toReturn.sort(reverse=True,key =sort_on); 
    #sort_on is a helper function passed to sort() via the key= argument. Python calls it on each list 
    #element, using its return value to determine sorting order.

    return toReturn ; 


