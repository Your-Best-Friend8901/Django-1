from twoapp.models import User

def data_user(nick,password):
    if User.objects.filter(nick=nick).exists():
        return 'Имя уже было занята'
    else:
        user = User(nick=nick,password=password)
        user.save()
        return 'Никнейм подходит!'
    
def login_data(nick,password):
    if User.objects.filter(nick=nick,password=password).exists():
        return 'Вы проходите дальше'
    else:
        return 'Вы не прошли'