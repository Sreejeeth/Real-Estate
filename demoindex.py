import os
import pandas
import sys
from text_file_indexer_demo import index_text_file

data=[]
word_list=[]
class estateDetails:
    def __init__(self,estateName,estateAddress,estateSize,estatePrice,estateOwner,estateCondition):
        self.estateName=estateName
        self.estateAddress=estateAddress
        self.estateSize=estateSize
        self.estatePrice=estatePrice
        self.estateOwner=estateOwner
        self.estateCondition=estateCondition

    def display_data(self):
        print("\nESTATE NAME -"+self.estateName+"\nESTATE ADDRESS - "+self.estateAddress+"\nESTATE SIZE -"+self.estateSize+"\nESTATE PRICE - "+self.estatePrice+"\nESTATE OWNER -"+self.estateOwner+"\nESTATE CONDITION -"+self.estateCondition)
        #print(st)

    def pack(self,file):
        buf=self.estateName+"|"+self.estateAddress+"|"+self.estateSize+"|"+self.estatePrice+"|"+self.estateOwner+"|"+self.estateCondition+"|"
        buf+="\n"
        file.write(buf)

class index:
    def __init__(self,name):
        self.name=name

    def pack(self,file):
        buf1=self.name
        buf1+="\n"
        file.write(buf1)



def unpack():
    with open("fulldetails4.txt","r") as fp:
        for line in fp:
            fields=line.strip('\n').split("|")[:-1]#[:-1] is needed to not include last | char
            s.append(estateDetails(fields[0],fields[1],fields[2],fields[3],fields[4],fields[5]))


print("\n**************************WELCOME TO ESTATE PORTAL***************************")
print("\nENTER YOUR CHOICE")
while True:
    choice=input("1.Insert a record\n2.Search and Modify a record\n3.Visualize\n4.Exit\n")
    if choice=='1':
        estateName=input("Enter Estate Name")
        estateAddress=input("Enter Estate Address")
        estateSize=input("Enter Estate Size")
        estatePrice=input("Enter Estate Price")
        estateOwner=input("Enter Estate Owner")
        estateCondition=input("Enter Estate Condition")
        temp=estateDetails(estateName,estateAddress,estateSize,estatePrice,estateOwner,estateCondition)
        with open("fulldetails4.txt","a+") as fp:
            temp.pack(fp)

        txt_fil = open("fulldetails4.txt", "r")

        words2=[]
        word_occurrences = {}
        line_num = 0

        for lin in txt_fil:
            line_num += 1
            words = lin.split('|')
            words2.append(words[0])
        fp=open("index4.txt","w").close()
        for word in sorted(words2):
            temp1=index(word)
            with open("index4.txt","a+") as fp:
                temp1.pack(fp)
        txt_fil.close()

    elif choice=="2":
        print("Searching...")

        s=[]
        unpack()
        name_srch=input("Enter the Name to search and modify")
        flag=0
        with open("index4.txt",'r') as fp2:
            for line in fp2:
                field=line.split("\n")[:-1]
                if name_srch==field[0]:
                    for x in s:
                    # field2=line1.split("|")[:-1]
                        if name_srch==x.estateName:
                            flag=1
                            print("Record found")
                            ch=input("Select the field to modify\n1.Address\n2.Size\n3.Price\n4.Owner\n5.Condition")
                            if ch=='1':
                                newadd=input("Enter the new address")
                                x.estateAddress=newadd
                            elif ch=='2':
                                newsize=input("Enter the new size")
                                x.estateSize=newsize
                            elif ch=='3':
                                newprice=input("Enter the new price")
                                x.estatePrice=newprice
                            elif ch=='4':
                                newowner=input("Enter the new owner")
                                x.estateOwner=newowner
                            elif ch=='5':
                                newcond=input("Enter the new condition")
                                x.estateCondition=newcond
                            else:
                                print("invalid option")

                if flag==0:
                    print("House does not exist")

                with open("fulldetails4.txt","w+") as fp:
        #            fp.seek(0)
        #            fp.truncate()
                    for x in s:
                        x.pack(fp)



    elif choice=="3":
        os.system('python mixvisualize.py')

    elif choice=="4":
        exit()

    else :
        print("Invalid Input")
