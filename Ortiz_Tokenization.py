import re

def tokenization(paragraph):
    option = int(input("\n\n1. White Space\n2. Bigram\n3. Trigram\n4. Regex\nEnter option: "))
    
    match option:
        case 1:
            tokens = paragraph.split()
        case 2:
            word = paragraph.split()
            tokens = []
            for i in range(0, len(word)-1):
                tokens.append((word[i], word[i+1]))

        case 3:
            word = paragraph.split()
            tokens = []
            for i in range(0, len(word)-2):
                tokens.append((word[i], word[i+1], word[i+2]))
        case 4:
            tokens = "Error"
        case _: 
            tokens = "Error"
    
    return tokens
        
        
# paragraph = input("Input Paragraph: ")
paragraph = "Lorem ipsum dolor sit amet"
while(1):
    tokens = tokenization(paragraph)
    print(tokens)
    if(tokens == "Error"):
        break