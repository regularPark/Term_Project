office = []
area = []
off_num = 0
ar_num = 0

def show_menu():
    print('*******************************************')
    print('1. Office Management')
    print('2. Area Management')
    print('3. Product management')
    print('4. Search Product')
    print('5. Quit')
    print('*******************************************')

def show_submenu():
    print('*******************************************')
    print('1. Retrieve')
    print('2. Input')
    print('3. Update')
    print('4. Delete')
    print('5. Back to main')
    print('*******************************************')

def show_search_menu():
    print('*******************************************')
    print('1. Retrieve')
    print('2. Search')
    print('3. Update')
    print('4. Delete')
    print('5. Back to main')
    print('*******************************************')    

def office_manage():
    print('\n\tOffice Management')

    show_submenu()
    global off_num

    n = int(input('Enter the number of the menu > '))
    while True:
        
        #retrieve
        if n == 1:
            if len(office) == 0:
                print('\nEmpty list. Enter info first.\n')
                office_manage()
            else:
                print('*******************************************')    
                print('Ofc. Code\tBld. name\tOfc. address\tOfc. Manager')
                for i in range(len(office)):
                    print('{}\t\t{}\t\t{}\t\t{}'.format(office[i][0], office[i][1], office[i][2], office[i][3]))
                office_manage()
        
        #input menu
        elif n == 2:
            off_num += 1
            off_code = format(off_num, '04')
            b_name = input('Enter building name > ')
            off_name = input('Enter a room > ')
            om_name = input('Enter a office manager name > ')

            office.append([off_code, b_name, off_name, om_name])

            office_manage()
            
        elif n == 3:
            pass
        elif n == 4:
            pass
        elif n == 5:
            main_menu()
        else:
            print('\nPlease enter number between 1 to 5.\n')
            office_manage()

def show_area():
    if len(area) > 0:
        print('*******************************************')    
        print('Area Code\tOfc. Code\tArea Name\tArea Manager')
        for i in range(len(office)):
            print('{}\t\t{}\t\t{}\t\t{}'.format(area[i][0], area[i][1], area[i][2], area[i][3]))
    else:
        print('-------------------------------------------')
        print('There is no data\n')


def area_manage():
    print('\n\tArea Management')    
    show_submenu()

    n = int(input('Enter the number of the menu > '))
    while True:
        show_submenu()
        global ar_num
        
        if n == 1:
            if len(area) == 0:
                print('\nEmpty list. Enter info first.\n')
                area_manage()
            else:
                show_area()
                area_manage()

        elif n == 2:
            if len(office) == 0:
                print('No office data. Input office first')
                area_manage()
            else:
                print('Exist office code')
                for i in range(len(office)):
                    print('{}'.format(office[i][0]))

                while True:
                    off_code = input('Enter office code > ')
                    for i in range(len(office)):
                        if off_code == office[i][0]:
                            ar_num += 1
                            ar_code = format(off_num, '03')
                            ar_name = input('Enter area name > ')
                            ar_m_name = input('Enter area manager Name > ')

                            area.append([ar_code, off_code, ar_name, ar_m_name])
                            show_area()
                            area_manage()
                    print('Enter exist Office code.')

        elif n == 3:
            if len(area) > 0:
                print('\nUpdate Area Info')
                show_area()
                while True:
                    f_ar_code = input('Enter area code to update > ')
                    for i in range(len(area)):
                        if f_ar_code == area[i][0]:
                            area[i][2] = input('Enter new area name > ')
                            area[i][3] = input('Enter new area manager Name > ')
                            print('Updated.\n')
                            show_area()

                            area_manage()
                    print('Enter exist Area code.')
            else:
                print('Enter area info first.')
                area_manage()                  

        elif n == 4:
            print('\nDelete Area Info')
            show_area()
            while True:
                    f_ar_code = input('Enter area code to delete > ')
                    for i in range(len(area)):
                        if f_ar_code == area[i][0]:
                            area.remove(area[i])
                            print('Deleted.\n')
                            show_area()

                            area_manage()
                    print('Enter exist Area code.')
        elif n == 5:
            main_menu()
        else:
            print('\nPlease enter number between 1 to 5.\n')
            area_manage()

def main_menu():

    print('\n\t\tMain Menu')
    while True:
        show_menu()
        n = int(input('Enter the number of the menu > '))
        # 사무실 관리
        if n == 1:
            office_manage()
        elif n == 2:
            area_manage()
        elif n == 3:
            pass
        elif n == 4:
            pass
        elif n == 5:
            print('Exit program')
            exit()
        else:
            print('\nPlease enter number between 1 to 5.\n')
            main_menu()





main_menu()