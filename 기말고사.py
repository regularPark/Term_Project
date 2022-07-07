ID = Name = ''
Korean = English = Math = -1

ID_li=[]
name_li=[]
korscore = []
engscore = []
mathscore = []

def screen():
    print("*****************************************************")    
    print("1.Retrieve")
    print("2.Input")
    print("3.Update")
    print("4.Delete")
    print("5.Quit")
    print("*****************************************************")    
    print(">",end=" ")

while True:
    screen()
    menu=input()
    if int(menu)==1:
        print("Index\tID\tName\tKorean\tEnglish  Math")
        print("---------- ---------- ---------- ---------- ---------- ----------")

        for i in range(len(mathscore)):
            print(i,'\t',ID_li[i],'\t',name_li[i],'\t',korscore[i],'\t',engscore[i],'\t',mathscore[i])

    if int(menu)==2:
        ID=input("ID  >")
        ID_li.append(ID)
        
        Name=input("Name  >")
        name_li.append(Name)

        while True:
            Korean=input("Korean  >")
            if(int(Korean)<=100 and int(Korean)>=0):
                break
            else:
                print("Please enter a number between 0 to 100!!")
                continue
        korscore.append(Korean)

        while True:
            English=input("English  >")
            if(int(English)<=100 and int(English)>=0):
                break
            else:
                print("Please enter a number between 0 to 100!!")
                continue
        engscore.append(English)

        while True:
            Math=input("Math  >")
            if int(Math)<=100 and int(Math)>=0:
                break
            else:
                print("Please enter a number between 0 to 100!!")
                continue
        mathscore.append(Math)

    if int(menu)==3:
        i=int(input('index >'))
        while i<0:
            print("Please enter a number between 0 to",len(mathscore))
            print()
    
        print('ID:',ID_li[i])
        print('Name:',name_li[i])
        print('Korean:',korscore[i])
        print('English:',engscore[i])
        print('Math:',mathscore[i])
        print()

        ID_li[i]=input("ID   >")
        name_li[i]=input("Name  >")   
        
        korscore[i]=int(input("Korean >"))
        while korscore[i]>100 or korscore[i]<0:
                print("Please enter a number between to 0 to 100!!")
                korscore[i]=int(input("Korean >"))

        engscore[i]=int(input("English >"))
        while engscore[i]>100 or engscore[i]<0:
            print("Please enter a number between to 0 to 100!!")
            engscore[i]=int(input("English >"))
       
        mathscore[i]=int(input("Math >"))
        while mathscore[i]>100 or mathscore[i]<0:
            print("Please enter a number between to 0 to 100!!")
            mathscore[i]=int(input("math >"))

    if int(menu)==4:
        a=int(input("index:"))
        while a<0:
            print("Please enter a number between 0 to",len(mathscore))
            a=int(input("index:"))
        
        del ID_li[a]
        del name_li[a]
        del korscore[a]
        del engscore[a]
        del mathscore[a]
         
        for i in range(len(mathscore)):
            print(i,'\t',ID_li[i],'\t',name_li[i],'\t',korscore[i],'\t',engscore[i],'\t',mathscore[i])
                
    if int(menu)==5:
        print("bye!!")
        break