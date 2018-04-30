
import sys
import os
import string

#
# txt_fil="estatedetails.txt"
# idx_fil= "index2.txt"

def index_text_file(txt_filename, idx_filename,
    delimiter_chars=",.;:!?/|"):

    txt_fil = open(txt_filename, "r")

    words2=[]
    word_occurrences = {}
    line_num = 0

    for lin in txt_fil:
        line_num += 1
        words = lin.split('|')
        #words.split("|")
        words2.append(words[0])
        # print(words[0])
    # # Create the index file.
    idx_fil = open(idx_filename, "w")
    for word in sorted(words2):
        idx_fil.write(word + " ")
        idx_fil.write("\n")
    txt_fil.close()
    idx_fil.close()


    print("Enter the estate name")
    estateName= input()
    idx_fil = open(idx_filename, "r")
    txt_fil = open(txt_filename, "r")
    print("The details are :")
    count=0
    for word in sorted(words2):
        if word == estateName:
            for lin in txt_fil:
                words = lin.split('|')
                if estateName==words[0]:
                    for details in words:
                        print(details)
                    break;
        else:
            count=count+1

    if count==len(sorted(words2)) :
        print("not found")
    txt_fil.close()
    idx_fil.close()

if __name__ == "__main__":
    main()

# EOF
#form dictionary of dictionaries - 12th april 2018

#give the index(key) file a unique value . match the value with the first data of the main text file .
