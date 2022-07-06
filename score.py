# main 화면 출력
def main_screen():
    print('**********************************************************************')
    print(' 1. Retrieve')
    print(' 2. Input')
    print(' 3. Update')
    print(' 4. Delete')
    print(' 5. Quit')
    print('**********************************************************************')

# retrieve & update에서 재사용.
def show_list():
    print('Index\tID\tName\tKorean\tEnglish\tMath')
    print('---------- ---------- ---------- ---------- ---------- ----------')
    for i in range(len(kor_li)):
        print('{}\t{}\t{}\t{}\t{}\t{}'.format(i + 1, id_li[i], name_li[i], kor_li[i], eng_li[i], math_li[i]))

# input & update에서 재사용.
def input_kor():
    kor = int(input('Korean > '))
    while kor < 0 or kor > 100:
        print('Please enter a number between 0 to 100!!')
        kor = int(input('Korean > '))
    return kor

def input_eng():
    eng = int(input('English > '))
    while eng < 0 or eng > 100:
        print('Please enter a number between 0 to 100!!')
        eng = int(input('English > '))
    return eng

def input_math():
    math = int(input('Math > '))
    while math < 0 or math > 100:
        print('Please enter a number between 0 to 100!!')
        math = int(input('Math > '))
    return math

# 변수 선언 및 저장 코드
id = ''
name = ''
kor = eng = math = -1
id_li = []
name_li = []
kor_li = []
eng_li = []
math_li = []

# 프로그램 실행 관련 코드
while True:
    main_screen()

    n = input('> ')

    # Retrieve
    if int(n) == 1:
        show_list()

    # Input
    elif int(n) == 2:
        id = input('ID > ')
        id_li.append(id)

        name = input('Name > ')
        name_li.append(name)

        kor_li.append(input_kor())
    
        eng_li.append(input_eng())

        math_li.append(input_math())


    # Update
    elif int(n) == 3:
        show_list()
        num = int(input('index > '))

        while num <= 0 or num > len(id_li):
            print('Please enter 1 to',len(id_li))
            num = int(input('index > '))
        
        n = num - 1 # 화면상의 index와 배열의 index가 다른 것을 조정함.

        id_li[n] = input('ID > ')
        name_li[n] = input('Name > ')
                
        kor_li[n] = input_kor()
        
        eng_li[n] = input_eng()

        math_li[n] = input_kor()
        
        print('\nUpdated.\n')
        
        show_list()

    # Delete
    elif int(n) == 4:
        if len(id_li) == 0:
            print('There is no data.')
        
        else:
            show_list()
            num = int(input('Index> '))
        
            while num > len(id_li) or num <= 0:
                print('Please enter a number between 1 to', len(id_li))
                num = int(input('index> '))
        
            n = num - 1

            id_li.remove(id_li[n])
            name_li.remove(name_li[n])
            kor_li.remove(kor_li[n])
            eng_li.remove(eng_li[n])
            math_li.remove(math_li[n])

            print('Deleted.')
            if len(id_li) > 0:
                show_list()
            else:
                print('There is no data\n')
    
    # Quit
    elif int(n) == 5:
        print('Bye!!')
        break