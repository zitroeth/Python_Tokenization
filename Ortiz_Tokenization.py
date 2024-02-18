import re

def tokenization(paragraph):
    option = int(input("\n\n1. White Space\n2. Bigram\n3. Trigram\n4. Regex\n5. Change Paragraph\nEnter option: "))
    
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
            tokens = re.split("[ ,!?:;/]", paragraph)
        case 5:
            tokens = ''
        case _: 
            tokens = "Error"
    
    return tokens        

#paragraph = "Lorem ipsum dolor sit amet"
tokens = ''
while(1):
    if tokens == '':
        paragraph = input("Input Paragraph: ")
    tokens = tokenization(paragraph)
    print(tokens)
    if(tokens == "Error"):
        break