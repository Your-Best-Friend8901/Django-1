#Функция для проверки пароля отправителя
def check_password(nick,password):
    if len(password) < 8 or len(password) > 16:
        return 'Пароль должен быть от 8 до 16 символов'
    
    if len(nick) < 8 or len(nick) > 16:
        return 'Никнейм должен быть от 8 до 16 символов'
    
    if not password.isalnum():
        return "Пароль может содержать только буквы и цифры"
    
    if not any(number.isdigit() for number in password):
        return "Пароль должен содержать хотя бы одну цифру"
    
    if not any(abc.isalpha() for abc in password):
        return "Пароль должен содержать хотя бы одну букву"
    
    else:
        return "Пароль подходит!"
    

    