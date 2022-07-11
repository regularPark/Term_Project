from re import I

import datetime

today = datetime.date.today()

off_code = 0
office = []

area_code = 0
area=[]

product=[]


def show_menu():
    print('************************')
    print('1.Office Management')
    print('2.Area Management')
    print('3.Product Management')
    print('4.Searching')
    print('5.Quit')
    print('************************')

def show_sub_menu():
    print('************************')
    print('1.Retrieve')
    print('2.Input')
    print('3.Update')
    print('4.Delete')
    print('5 Back to show menu')
    print('************************')

#물품관리  
def show_product_menu():
    print('************************')
    print('1.Retrieve')
    print('2.Input')
    print('3 Lend / Return')
    print('4 Delete')
    print('5 Back to main')

def show_list():
         for i in range(len(office)):
            print('{}\t\t{}\t\t{}\t{}'. format(office[i][0], office[i][1], office[i][2], office[i][3]))


def show_list2():
        for i in range(len(area)):
            print('{}\t\t\t{}\t\t\t{}\t\t{}'. format(office[i][0],area[i][0], area[i][1], area[i][2]))
        

#사무실관리
def office_menu():
    
    show_sub_menu()

    global off_code #off_code 전역변수 가져옴

    num2=int(input('Select the number of sub_menu >'))
    while num2 < 0:

        print('Please re-enter the number')
        print()
        num2=int(input('Select the number of sub_menu >'))

    #retrieve
    if num2 == 1:

        print('Office_code\tBuilding_Name\tRoom\tManager')
        print('---------- ---------- ---------- ---------- ---------- ----------')
        show_list()
        office_menu()

    #input
    elif num2==2:

        while True:
            
            off_code += 1 #off_code가 1씩 증가
            off_num = format(off_code, '04') #총4자리고 나머지를 0으로 채워라
            b_name = input("Building name >")
            off_name = input("Office Room >")
            om_name = input("Manager name >")

            office.append([off_num,b_name,off_name,om_name])
            
            break
        office_menu()
        
    #update
    elif num2==3:

        num=int(input("Office_code >"))
        while num<=0 and num<len(off_code):
            print("Please Enter over 0001 >")
            num=int(input("Office_code >"))
        
        num-=1 #인덱스가 0으로 시작해서 넣음

        office[num][1]=input('Building name > ')
        office[num][2]=input('Office name >')
        office[num][3]=input('Manger name >')

        print()
        print("Updated")

        show_list()

        office_menu()
    
    
    #Deleted
    elif num2==4:
        
        num=int(input('Enter the office code you want to delete >'))
        while num<=0 and num>len(off_code):
            print("Please enter over 0001")
            num=int(input('Enter the office code you want to delete >'))
        
        num-=1 #인덱스가 0부터 시작해서 넣음
        print(num)

        if num>=0 and num<off_code:
            office.remove(office[num])

        print()

        print("Deleted")
    

        office_menu()
        
    elif num2==5:

        main_menu()

    
#영역관리      
def area_menu():

    show_sub_menu()
    
    global area_code

    num3 = int(input('Please enter the number of sub_menu >'))
    while num3 < 0:
        print('Please enter over zero >')
        num3 = int(input('Please enter the number of sub_menu >'))

    if num3 == 1:

        print('Off_code\t\tArea_code\t\tArea_name\tManager')
        print('---------- ---------- ---------- ---------- ---------- ---------- ----------')

        show_list2()

    elif num3 == 2:
       
        print('-------Available office_code------')     
        for i in range(len(office)):
            print(office[i][0])

        
        while True:

            isInput = False

            off_code=input('Please enter office code >')
                        
            for i in range(len(office)):
                if office[i][0] == off_code:                   

                    area_code += 1 
                    area_num = format(area_code, '03') 
                    area_name=input('Area_name >')
                    area_manager=input('Area manager >')  

                    area.append([area_num,area_name,area_manager])

                    isInput = True

            if isInput == True:
                 break
        area_menu()

    elif num3 == 3:
        
        num=int(input('Please enter area_code > '))
        while num<=0 or num>len(area):
            print('Please enter over 001')
            num=int(input('Please enter area_code > '))

        num-=1

        area[num][1]=input('Please enter area_name > ')
        area[num][2]=input('Please enter area_manager >')

        print()
        print('----------------Updated----------------------')
        print('         Please retrieve the data!!')
        print() 

        area_menu()

    elif num3 == 4:
          
        print('Can delete area_code : ',area_code)
        num=int(input('Enter the area_code you want to delete >'))
        while num<=0 and num>len(area_code):
            print("Please enter over 0001")
            num=int(input('Enter the area_code you want to delete >'))
        
        num-=1 #인덱스가 0부터 시작해서 넣음

        if num >= 0 and num < len(area):
            area.remove(area[num])

        print()
        print("---------Deleted---------")
        print()
    
        area_menu()
        

    elif num3 == 5:

        main_menu()

def product_menu():
    
    show_product_menu()
    
    num = int(input('Please enter Product menu :'))
    if num < 0 or num > 6:
        print('Please re-enter the Product menu ')
        num = int(input('Please enter Product menu :'))

    #retrieve
    elif num == 1:
        pass
    
    #Input
    elif num == 2:

        while True:

            isInput = False

            print('------------Useful Area_code--------------')
            for i in range(len(area)):
                print(area[i][0])

            area_code = input('Please enter area code >')
                        
            for i in range(len(area)):
                if area[i][0] == area_code:
                    print(area[i][0])

                    product_code = input('product_code  >')
                    product_type = input('product_type  >')  
                    product_name = input('product_name >')
                    product_price = input('product_price >')
                    product.append([product_code,product_type,product_name,product_price]) 
                    
                    #product_code = product[i][0]
                    #product_type = prodct[i][1]
                    #product_name = product[i][2]
                    #product_price = product[i][3]

                    isInput = True

            if isInput == True:
                 break
        
        product_menu()

    #Lend / Return
    elif num == 3:

        print('-----------------------')
        print('1. Lend')
        print('2. Return')
        print('-----------------------')

        lend_return = int(input('Please select lend or return >'))
        
        while lend_return < 1 or lend_return>2:
             print('Please re-enter Lend / Return menu :')
             lend_return = int(input('Please select lend or return'))

        if lend_return == 1:

            print('---------There is rental items----------')
            for i in range(len(office)):
                print(product[i][2])

        #product_name == product[i][2]

            while True:
                
                isInput = False

                lend_product = input('Please enter items to rent : ')  #
                for i in range(len(product)):
                    print(today) #오늘 날짜를 기준

                    if product[i][2] == lend_product :
                        lend_date = input('Please enter date to rent  :')
                        
                        isInput = True

                        product.insert([i][4])

                    else:
                        print('Please re-enter date to rent :')
                
                if isInput == True :
                    break
            
        elif lend_return == 2:
            
            while True:

                isInput = False

                print('--------Lent Product----------')
                print(lend_product)
                print()

                return_product = input('Please return to items :')

                for i in range(len(product)):
                    
                     if product[i][2] == return_product:

                        return_date = input('Please enter date to return : ')

                        isInput = True

                        product.append([return_date])
                    
                     else:
                        print('Please re-enter return to date :')
                
                if isInput == True :
                    break


    #Transfer
    elif num == 4:
        pass

    #Back to the menu
    elif num == 5:
        
        main_menu()
        
    

    
#Main menu
def main_menu():

    show_menu()

    num1=int(input("Select the number of show_menu > "))
    while num1<0:
        print('Please re-enter the number')
        num1=int(input("Select the number of show_menu > "))

    while num1 == 1:
            office_menu()
            
    while num1 == 2:  
            area_menu()

    while num1 == 3:
            product_menu()

    while num1 == 4:
        pass

    while num1 == 5:
        print('bye!!')
        exit() #프로그램 종료함수

main_menu()