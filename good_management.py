from datetime import *

office = [['0001', 'Eng. Bld.', '4147', 'Park'],
          ['0002', 'Hehwa Bld.', '1151', 'Kim']]
area = [['001', '0001', 'Shelf', 'Hong'], [
    '002', '0001', 'Box', 'Min'], ['001', '0002', 'Locker', 'Cha']]
product = [['1', '0001', '001', 'PC', 'Mac', '2m', 'park', '20220707',
            '-'], ['2', '0002', '001', 'Printer', 'Cannon', '400k', '-', '-', '-'], ['3', '0001', '002', 'Lamp', 'Edison', '3k', '-', '-', '-']]
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


def show_product_menu():
    print('*******************************************')
    print('1. Retrieve')
    print('2. Input')
    print('3. Lend/Return')
    print('4. Transfer')
    print('5. Delete')
    print('6. Back to main')
    print('*******************************************')


def show_search_menu():
    print('*******************************************')
    print('1. View all product')
    print('2. Search product')
    print('3. Back to main')
    print('*******************************************')


def office_manage():
    print('\n\tOffice Management')
    show_submenu()
    global off_num

    n = int(input('Enter the number of the menu > '))
    while True:

        # retrieve
        if n == 1:
            if len(office) == 0:
                print('\nEmpty list. Enter info first.\n')
                office_manage()
            else:
                print('*******************************************')
                print('Ofc. Code\tBld. name\tOfc. address\tOfc. Manager')
                for i in range(len(office)):
                    print('{}\t\t{}\t\t{}\t\t{}'.format(
                        office[i][0], office[i][1], office[i][2], office[i][3]))
                office_manage()

        # input menu
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
        for i in range(len(area)):
            print('{}\t\t{}\t\t{}\t\t{}'.format(
                area[i][0], area[i][1], area[i][2], area[i][3]))
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

                            area.append(
                                [ar_code, off_code, ar_name, ar_m_name])
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
                            area[i][3] = input(
                                'Enter new area manager Name > ')
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


# 2019113632 박정규
def check_code():
    isOfCode = False
    isArCode = False

    print('Available Office number & Area number')
    print('-------------------------------------')
    print('Ofc. number\tArea number')
    # 사용가능한 코드 출력
    for i in range(len(area)):
        print('{}\t\t{}'.format(area[i][1], area[i][0]))

    while isOfCode == False:
        off_num = input('Enter Office Code > ')
        for j in range(len(area)):
            if off_num == area[j][1]:
                isOfCode = True
                break
        if isOfCode == True:
            break
        print('!!! Please check Office code correctly.')

    while isArCode == False:
        ar_num = input('Enter Area Code > ')
        for k in range(len(area)):
            if ar_num == area[k][0]:
                isArCode = True
                break
        if isArCode == True:
            break
        print('!!! Please check Area code correctly.')

    return off_num, ar_num, True, True


# 2019113632 박정규
def show_product():
    print('-------------------------------------')
    print('Prod.\tOfc.\tArea\tProd.\t\t\t\tLend\t\tReturn')
    print('code\tnumber\tnumber\ttype\tname\tprice\tLender\tdate\t\tdate')
    for i in range(len(product)):
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
            product[i][0], product[i][1], product[i][2], product[i][3], product[i][4], product[i][5], product[i][6], product[i][7], product[i][8]))


# 2019113632 박정규
def product_manage():
    if len(area) == 0:
        print('No data. Input office & area data. please.')
    else:
        show_product_menu()
        n = int(input('Enter the number of the menu > '))
        while True:
            # retrieve
            if n == 1:
                if len(product) == 0:
                    print('No data. Input product data first. please')
                else:
                    show_product()
                    print()

                product_manage()

            # Input
            elif n == 2:
                off_num, ar_num, isOfCode, isArCode = check_code()

                if isOfCode == True and isArCode == True:
                    p_code = input('Enter Product Code > ')
                    if len(product) > 0:
                        # 물품 코드 중복 방지
                        for i in range(len(product)):
                            while product[i][0] == p_code:
                                print('Already exists. Input again.')
                                p_code = input('Enter Product Code > ')

                    p_type = input('Enter Product Type > ')
                    p_name = input('Enter Product Name > ')
                    p_price = int(input('Enter Product Price > '))
                    lender = '-'
                    len_date = '-'
                    ret_date = '-'

                product.append([p_code, off_num, ar_num, p_type,
                               p_name, p_price, lender, len_date, ret_date])

                product_manage()

            # Lend/Return
            elif n == 3:
                if len(product) == 0:
                    print('There is no data of product. Input data first.')
                    product_manage()
                else:
                    while True:
                        print('-------------------------------------')
                        print('1. Lend')
                        print('2. Return')
                        print('-------------------------------------')

                        num = int(input('Enter the number of the menu > '))
                        # 대출
                        if num == 1:
                            show_product()
                            print('\n*************Lend process************\n')

                            isLent = False
                            while True:
                                off_num, ar_num, isOfCode, isArCode = check_code()
                                p_code = input('Enter Product Code to lend > ')
                                for i in range(len(product)):
                                    if product[i][0] == p_code and product[i][1] == off_num and product[i][2] and isOfCode == True and isArCode == True:
                                        # 물품이 현재 사용 중인 상태
                                        if product[i][7] != '-' and product[i][8] == '-':
                                            print(
                                                '\n!!! This product has already been lent.')

                                            if len(product) == 1:
                                                print(
                                                    '!!! There no product you can lend.')
                                                product_manage()
                                            break

                                        product[i][6] = input(
                                            'Enter lender\'s name > ')
                                        product[i][7] = input(
                                            'Enter lend date(must be 8 numbers) > ')
                                        while len(product[i][7]) != 8:
                                            product[i][7] = input(
                                                'Enter lend date correctly(must be 8 numbers) > ')
                                        # 이전에 대여했던 물품의 반납일자를 초기화함. 대여한 적이 없을 때도 적용됨.
                                        product[i][8] = '-'
                                        print('Lending completed.\n')
                                        isLent = True
                                        show_product()
                                        break

                                if isLent == True:
                                    break

                                print('\n!!!Check Product Code again. Please.')
                                show_product()
                            product_manage()

                        # 반납
                        elif num == 2:
                            show_product()
                            print('\n************Return process***********\n')
                            isReturned = False
                            while True:
                                # 반납할 물품이 없을 때
                                cnt = 0
                                for i in range(len(product)):
                                    if (product[i][7] != '-' and product[i][8] != '-') or (product[i][7] == '-' and product[i][8] == '-'):
                                        cnt += 1
                                if cnt == len(product):
                                    print(
                                        '!!! There is no product can be returned. Move to previous menu.\n')
                                    break

                                p_code = input(
                                    'Enter Product Code to return > ')
                                for i in range(len(product)):
                                    if product[i][0] == p_code and product[i][7] != '-' and product[i][8] == '-':
                                        product[i][8] = input(
                                            'Enter Return Date(must be 8 numbers). > ')
                                        while len(product[i][8]) != 8:
                                            product[i][8] = input(
                                                'Enter Return date correctly(must be 8 numbers) > ')
                                        isReturned = True
                                if isReturned == True:
                                    break
                                print('\n!!! Check Product Code again. Please.\n')

                            product_manage()

                        else:
                            print('Enter the number between 1 to 2')

            # Change place
            elif n == 4:
                if len(product) == 0:
                    print('There is no data of product. Input data first.')
                    product_manage()
                else:
                    show_product()
                    isMoved = False
                    # 이관할 장소가 있을 때만 실행 가능
                    while len(area) > 1:
                        p_code = input('Enter Product Code to transfer > ')
                        for i in range(len(product)):
                            if p_code == product[i][0]:
                                print('\nSelect to change Office & Area')
                                off_num, ar_num, isOfCode, isArCode = check_code()
                                while product[i][1] == off_num and product[i][2] == ar_num:
                                    print('This is already there.')

                                product[i][1], product[i][2] = off_num, ar_num
                                isMoved = True
                                show_product()
                                print('Transfer completed.\n')
                                break
                        if isMoved == True:
                            break
                        print('\n!!! Please check Product Code correctly.')
                    if len(area) == 1:
                        print(
                            '\n!!! There is just one area. Cannot transfer products.\n')
                    product_manage()

            # Delete
            elif n == 5:
                if len(product) == 0:
                    print('There is no data of product. Input data first.')
                    product_manage()
                else:
                    show_product()
                    isDeleted = False
                    while True:
                        p_code = input('Enter product code to delete > ')
                        for i in range(len(product)):
                            if p_code == product[i][0]:
                                product.remove(product[i])
                                isDeleted = True
                                show_product()
                                print('Deleted successfully.\n')
                                break
                        if isDeleted == True:
                            break

                        print('\n!!! Please check Product Code correctly.')
                    product_manage()

            # Quit
            elif n == 6:
                main_menu()
            else:
                print('\nPlease enter number between 1 to 6.\n')
                product_manage()


# 2019113632 박정규
def show_p_code():
    print('\nSearchable product code.')
    for i in range(len(product)):
        print(product[i][0], end='\t')
    print('\n')


# 2019113632 박정규
def show_all_prod():
    for i in range(len(office)):
        print('\n#{}\t{} {}\t\tManager:{}'.format(
            office[i][0], office[i][1], office[i][2], office[i][3]))
        for j in range(len(area)):
            if area[j][1] == office[i][0]:
                for k in range(len(product)):
                    if (area[j][0] == product[k][2]) and (area[j][1] == product[k][1]):
                        print('\t#{} | {}\t(#{}){} | {} in charge'.format(
                            area[j][0], area[j][2], product[k][0], product[k][3], area[j][3]))
        print()


def find_prod(idx):
    for i in range(len(office)):
        if product[idx][1] == office[i][0]:
            print('\n#{}\t{} {}\t\tManager:{}'.format(
                office[i][0], office[i][1], office[i][2], office[i][3]))
    for j in range(len(area)):
        if (product[idx][2] == area[j][0]) and (area[j][1] == product[idx][1]):
            print('\t#{} | {}\t(#{}){} | {} in charge'.format(
                area[j][0], area[j][2], product[idx][0], product[idx][3], area[j][3]))

    print()


# 2019113632 박정규
def search_prod():
    show_search_menu()
    n = int(input('Enter the number of the menu > '))
    if n == 1:
        show_all_prod()
        search_prod()
    elif n == 2:
        show_p_code()
        isFound = False
        while True:
            p_code = input('Enter product code to delete > ')
            for i in range(len(product)):
                if p_code == product[i][0]:
                    find_prod(i)
                    isFound = True
                    break
            if isFound == True:
                break

            print('\n!!! Please enter product code correctly.')
        search_prod()
    elif n == 3:
        main_menu()
    else:
        print('Enter the number between 1 to 3')
        search_prod()


def main_menu():

    print('\n\t\tMain Menu')
    while True:
        show_menu()
        n = int(input('Enter the number of the menu > '))
        # 사무실 관리
        if n == 1:
            office_manage()
        # 영역 관리
        elif n == 2:
            area_manage()
        # 물품 관리
        elif n == 3:
            product_manage()
        # 물품 검색
        elif n == 4:
            search_prod()
        # 종료
        elif n == 5:
            print('Exit program')
            exit()
        else:
            print('\nPlease enter number between 1 to 5.\n')
            main_menu()


main_menu()
