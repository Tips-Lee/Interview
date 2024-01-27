

class Login_System:
    def __init__(self):
        with open('info.csv', 'r+') as info:
            info = info.readlines()
            self.info = [item.strip().split(',') for item in info]

    def login(self):
        cnt = 0
        while cnt < 3:
            user_name = input('please input username :  ')
            pass_word = input('please input password :  ')
            if [user_name, pass_word] in self.info:
                print('Login succeed !')
                break
            else:
                print('Login failed, please try again !')
                cnt += 1

    def register(self):
        user_name = input('please input username :  ')
        pass_word = input('please input password :  ')
        self.info.append([user_name, pass_word])
        with open('info.csv', 'a') as info:
            info.write('%s,%s\n' % (user_name, pass_word))
        print('Register success!')


l = Login_System()
l.register()
l.login()