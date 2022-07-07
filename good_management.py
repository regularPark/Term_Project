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
    print('2. Search')
    print('3. Update')
    print('4. Delete')
    print('5. Back to main')
    print('*******************************************')

def office_manage():
    show_submenu()

    n = int(input('Enter the number of the menu >'))
    while True:
        if n == 1:
            pass
        elif n == 2:
            pass
        elif n == 3:
            pass
        else:
            pass

def main_menu():
    while True:
        show_menu()
        n = int(input('Enter the number of the menu >'))
        # 사무실 관리
        if n == 1:
            office_manage()



main_menu()