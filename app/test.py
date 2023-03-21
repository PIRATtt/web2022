# symbols=['~', '!', '?', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '(', ')', '[', ']', '{', '}', '>', '<', '/', "\", '|', """, ''', '.', ',', ':', ';']

def check_pas(passwd):
    eng=['a', 'c' 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x', 'z']
    alf=['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    numb=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    s="""~!?@#$%^&*_-+()[]{}></\|"'.,:;"""
    symbols=[]
    for o in s:
        symbols.append(o)

    if len(passwd)<8 or len(passwd)>128:
        return 'Пароль должен быть не менее 8 символов и не более 128 символов.'

    for p in passwd:
        if p!=' ':
            check=True
            break
        else:
            check=False
    if check==False:
        return 'Пароль не должен содержать пробелов.'

    for p in passwd:
        if p.isupper():
            check=True
            break
        else:
            check=False
    if check==False:
        return 'В пароле должна быть хотя бы 1 заглавная буква.'

    for p in passwd:
        if p.islower():
            check=True
            break
        else:
            check=False
    if check==False:
        return 'В пароле должна быть хотя бы 1 строчная буква.'

    for p in passwd:
        if p in numb:
            check=True
            break
        else:
            check=False
    if check==False:
        return 'В пароле должна быть хотя бы 1 цифра.'

    for p in passwd.lower():
        if p in eng+alf+numb+symbols:
            check=True
        else:
            check=False
            break
    if check:
        return True
    else:
        return 'Пароль содержит недопустимые символы'



def check_login(login):
    eng=['a', 'c' 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x', 'z']
    numb=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if len(login)<5:
        return 'Логин должен быть длинее 5 символов.'

    for l in login.lower():
        if l in eng+numb:
            check=True
        else:
            check=False
            break
    if check:
        return True
    else:
        return 'Логин должен состоять из латинских символов.'