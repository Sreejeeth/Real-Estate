
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
        return
    txt_fil.close()
    idx_fil.close()


    print("Do you wish to modify??\n Press Y or N Please...")
    ch=input()
    if ch=='Y' or ch=='y':
        with open(txt_filename) as f:
            with open("estatedetailsdup.txt", "w") as f1:
                for line in f:
                    f1.write(line)
        f.close()
        f1.close()
        f1 = open("estatedetailsdup.txt", "r")

        txt_fil=open(txt_filename,"w").close();
        # f1=open(txt_filename,"r+")
        txt_fil=open(txt_filename,"w")
               #probs
        for lin in f1:
            words = lin.split('|')
                # for line in f1:
                #     words_again = line.split('|')
            if estateName!=words[0]:
                txt_fil.write(lin)
            # else:
            #     for line in f1:
            #         words_again = line.split('|')
            #         if words_again!=words:
            #             txt_fil.write(line)
            #
        word_list=list()
        print("enter the following details\nestateName\nestateAreaName\nestateAddress\nestateSize\nestatePrice\nestateOwner\nestateCondition\n")
        text_file= open("estatedetails.txt","a")
        for i in range (1, 8):
            print("Please enter data: ")
            line = input("\n")
            word_list.append(line + "|")

        word_list.append("\n")
        txt_fil.writelines(word_list)
if __name__ == "__main__":
    main()

# EOF
#form dictionary of dictionaries - 12th april 2018

#give the index(key) file a unique value . match the value with the first data of the main text file .
