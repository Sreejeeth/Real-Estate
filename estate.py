import os
import pandas
import sys
import time
data=[]
i1=[]
cnt=-1
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

    def pack(self,file):
        global cnt,i1
        pos=file.tell()
        buf=self.estateName+"|"+self.estateAddress+"|"+self.estateSize+"|"+self.estatePrice+"|"+self.estateOwner+"|"+self.estateCondition+"|"
        buf+="\n"
        file.write(buf)
        cnt+=1
        i1.append(index(self.estateName,pos))
        i1.sort(key = lambda x:x.estateName)


class index:
    def __init__(self,name,addr):
        self.estateName=name
        self.addr=addr

    def pack(self,file):
        buf1=self.estateName
        buf1+="\n"
        file.write(buf1)

def create_index():
    global cnt, pos, i1
    pos = 0
    try:
        with open("fulldetails.txt","r") as fp:
            line = fp.readline()
            while line:
                if line.startswith('*') or len(line) == 0:#if the record is deleted, dont add to index and read the next record
                    line = fp.readline()
                    pos = fp.tell()
                else:
                    fields=line.strip('\n').split("|")[:-1]
                    i1.append(index(fields[0], pos))
                    pos = fp.tell()
                    cnt += 1
                    line = fp.readline() #needed since when we delete, extra blank line is present at the end of the file
                    # i1.append(index(self.estateName,pos))
                    i1.sort(key = lambda x:x.estateName)#sort index list based on usn
    #        for y in i1:#to check if i1 is correct when prog. closedand opened and if it prints in sorted order
    #            print(y.usn,y.addr)
    except:
        pass

def find_index(name_srch):
    ind = -1
    for i in range(cnt+1):
        # print(i)
        if i1[i].estateName == name_srch:
            ind = i
            print(ind)
    return ind

def search():
    global i1,x
    name_srch = input("Enter the name of the estate to be found")
    ind = find_index(name_srch)
    if ind == -1:
        print('Record not found')
        return
    else:
        print('Record found and Updated\n')
        with open("fulldetails.txt","r") as fp:
            fp.seek(i1[ind].addr)
            line = fp.readline()
            fields=line.split("|")
            print("\nESTATE NAME -"+fields[0]+"\nESTATE ADDRESS - "+fields[1]+"\nESTATE SIZE -"+fields[2]+"\nESTATE PRICE - "+fields[3]+"\nESTATE OWNER -"+fields[4]+"\nESTATE CONDITION -"+fields[5])

            # print(line.strip('\n'))

    ch=input("Do you wish to modify ( y/n)\n")
    if ch=="y":
        for x in s:
            if name_srch==x.estateName:
                ch=input("Select the field to modify\n1.Address\n2.Size\n3.Price\n4.Owner\n5.Condition\n")
                if ch=='1':
                    newadd=input("Enter the new address\n")
                    x.estateAddress=newadd
                elif ch=='2':
                    newsize=input("Enter the new size\n")
                    x.estateSize=newsize
                elif ch=='3':
                    newprice=input("Enter the new price\n")
                    x.estatePrice=newprice
                elif ch=='4':
                    newowner=input("Enter the new owner\n")
                    x.estateOwner=newowner
                elif ch=='5':
                    newcond=input("Enter the new condition\n")
                    x.estateCondition=newcond
                else:
                    print("invalid option")


        with open("fulldetails.txt","w+") as fp:
            for x in s:
                x.pack(fp)

def unpack():
    with open("fulldetails.txt","r") as fp:
        for line in fp:
            fields=line.strip('\n').split("|")[:-1]#[:-1] is needed to not include last | char
            s.append(estateDetails(fields[0],fields[1],fields[2],fields[3],fields[4],fields[5]))
    with open("index.txt","r") as fp:
        for line in fp:
            fields=line.strip('\n')#[:-1] is needed to not include last | char
            p.append(index(fields,0))

create_index()
print("\n**************************WELCOME TO ESTATE PORTAL***************************")
print("\nENTER YOUR CHOICE")
while True:
    print()
    print()
    choice=input("1.Insert a record\n2.Search and Modify a record\n3.Delete record\n4.Visualize\n5.Exit\n")
    if choice=='1':
        estateName=input("Enter Estate Name\n")
        estateAddress=input("Enter Estate Address\n")
        estateSize=input("Enter Estate Size ( in Sqft)\n")
        estatePrice=input("Enter Estate Price (in  Rupees)\n")
        estateOwner=input("Enter Estate Owner\n")
        estateCondition=input("Enter Estate Condition ( Sale,Resale,Rent)\n")
        temp=estateDetails(estateName,estateAddress,estateSize,estatePrice,estateOwner,estateCondition)
        with open("fulldetails.txt","a+") as fp:
            temp.pack(fp)

        txt_fil = open("fulldetails.txt", "r")

        words2=[]
        word_occurrences = {}
        line_num = 0

        for lin in txt_fil:
            line_num += 1
            words = lin.split('|')
            words2.append(words[0])
        fp=open("index.txt","w").close()
        for word in sorted(words2):
            temp1=index(word,0)
            with open("index.txt","a+") as fp:
                temp1.pack(fp)
        txt_fil.close()
    elif choice == "2":
        s=[]
        p=[]
        unpack()
        search()
        # print("Record Updated")

    elif choice=="3":
        s=[]
        p=[]
        unpack()
        name_srch=input("Enter the Name of the house to be Deleted\n")
        flag=0
        with open("index.txt",'r') as fp2:
            for line in fp2:
                field=line.split("\n")[:-1]
                if name_srch==field[0]:
                    for x in s:
                    # field2=line1.split("|")[:-1]
                        if name_srch==x.estateName:
                            flag=1
                            print("Record found and deleted")
                            with open("fulldetailsdup.txt","w+") as fp:
                            #            fp.seek(0)
                            #            fp.truncate()
                                for x in s:
                                    if name_srch!=x.estateName:
                                        x.pack(fp)

                            with open("indexdup.txt","w+") as fp:
                            #            fp.seek(0)
                            #            fp.truncate()
                                for x in p:
                                    if name_srch!=x.estateName:
                                        x.pack(fp)

                            with open("fulldetailsdup.txt","r") as fp, open('fulldetails.txt', 'w') as fp1:
                                for line in fp:
                                    fp1.write(line)

                            with open("indexdup.txt","r") as fp, open('index.txt', 'w') as fp1:
                                for line in fp:
                                    fp1.write(line)

        if flag==0:
            print("House does not exist")

    elif choice=="4":
        os.system("python mixvisualize.py")

    elif choice=="5":
        exit()

    else :
        print("Invalid Input")
