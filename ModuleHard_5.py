import time
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __hash__(self):  # Шифровка пароля
        return self.password

    def __str__(self):
        return f"{self.nickname}"


class Video:  # создает объекты видео
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:  # хранит: список пользователей, список видеофайлов, параметры текущего пользователя
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def add(self, *videos):  # проверяет наличие добавляемого файла video в список videos, если нет, добавляет
        for video in videos:
            if not self.videos:
                self.videos.append(video)
            else:
                for j in self.videos:
                    if video.title != j.title:
                        self.videos.append(video)
                    else:
                        break

    def get_videos(self, search_video):  # поиск видеофайла в списке videos по строке
        self.search_video = search_video.lower()
        self.my_search_list = []
        for i in self.videos:
            my_str = i.title
            self.my_str = my_str.lower()
            if self.search_video in self.my_str:
                self.my_search_list.append(my_str)
        return self.my_search_list

    def watch_video(self, title):  # воспроизводит видео по названию
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    self.log_out()
                    return
                for sec in range(1, video.duration+1):
                    self.current_time_now = sec
                    print(self.current_time_now, sep='', end='-')
                    time.sleep(1)
                print(' Конец видео')
                return
        print('Видео не найдено')

    def register(self, nickname, password, age):  # метод регистрации пользователя
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)  # обращение к классу User
        self.users.append(new_user)
        self.current_user = new_user

    def log_in(self, login, password):  # ищет пользователя в списке зарегистрированных
        for user in self.users:
            if user.nickname == login and user.password == password:
                self.current_user = user
                print('Вы вошли в систему')
                return

    def log_out(self):            # сбрасывает текущего пользователя если ему нет 18
        self.current_user = None


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print()
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
print()
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)



