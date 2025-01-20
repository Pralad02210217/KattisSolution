def sorted_print(longest,words):
    for word in sorted(words,key= lambda w: w[::-1]):
        numberofSpaces=longest-len(word)
        spaces=" "*numberofSpaces
        print(f"{spaces}{word}")


def main():
    longest, word_list=-1,[]
    
    while True:
        try:
            word=input()
            
            if not word:
                sorted_print(longest,word_list)
                print()
                longest,word_list=-1,[]
            else:
                longest=max(longest,len(word))
                word_list.append(word)
            
        except EOFError:
            sorted_print(longest,word_list)
            break
if __name__=="__main__":
    main()