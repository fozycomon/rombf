#!usr/bin/python2.7
# coding=utf-8
import os, time
from app import config
from app import login
from app import rom
from romi import friends_list
from romi import friends
from romi import search_name
from romi import likes
from bs4 import BeautifulSoup as parser

class Brute(object):

    def __init__(self, url):
        self.url = url
        self.config = config.Config()
        self.cookie = self.config.loadCookie()
        self.menu = ''
        self.menu += '\x1b[1;97m [1] Dump Id Teman\n'
        self.menu += '\x1b[1;97m [2] Dump Id Daftar Teman\n'
        self.menu += '\x1b[1;97m [3] Dump Id Pencarian Nama\n'
        self.menu += '\x1b[1;97m [4] Dump Id Dari Like Status\n'
        self.menu += '\x1b[1;97m [5] Start Crack\n'
        self.menu += '\x1b[1;97m [\x1b[1;91m6\x1b[1;97m]\x1b[1;91m Hapus Cookies\n'
        self.menu += '\x1b[1;97m [\x1b[1;92m7\x1b[1;97m] \x1b[1;92mUpdate Tools\n'
        self.menu += '\x1b[1;97m [\x1b[1;91m0\x1b[1;97m] \x1b[1;91mExit\n'
        self.menu += '\x1b[1;97m════════════════════════════════════════════════'
        if self.cookie == False:
            login.loginFb(self, self.url, self.config)
            self.cookie = self.config.loadCookie()

    def start(self):
        response = self.config.httpRequest(self.url + '/profile.php', self.cookie).encode('utf-8')
        if 'mbasic_logout_button' in str(response):
            self.main(response)
        else:
            os.remove('log/cookies.log')
            print '\n\x1b[1;91m [!] Cookie Invalid !'
            raw_input('\n [Back]')
            login.loginFb(self, self.url, self.config)
            self.cookie = self.config.loadCookie()
            self.start()
            exit()

    def main(self, response):
        os.system('clear')
        print self.config.banner()
        html = parser(response, 'html.parser')
        print '\x1b[1;97m════════════════════════════════════════════════'
        print ('\x1b[1;97m Selamat Datang \x1b[1;92m').decode('utf-8') + html.title.text.upper()
        print '\x1b[1;97m════════════════════════════════════════════════'
        print self.menu
        try:
            choose = int(raw_input(' \x1b[1;97m[?] >\x1b[1;97m '))
        except ValueError:
            print '\x1b[1;91m [!] Isi yang benar'
            os.system('python2 rom.py')

        if choose == 1 or choose == 1:
            exit(friends_list.main(self, self.cookie, self.url, self.config))
        elif choose == 2 or choose == 2:
            exit(friends.main(self, self.cookie, self.url, self.config))
        elif choose == 3 or choose == 3:
            exit(search_name.main(self, self.cookie, self.url, self.config))
        elif choose == 4 or choose == 4:
            exit(likes.main(self, self.cookie, self.url, self.config))
        elif choose == 5 or choose == 5:
            ngentod = raw_input('\n\x1b[1;97m Note : Sebelum Mulai Crack Anda Diwajibkan\n Dump ID Terlebih Dahulu!\n \x1b[1;97m[?] Apakah Anda Yakin [\x1b[1;92my\x1b[1;97m/\x1b[1;91mn\x1b[1;97m]\x1b[1;91m :\x1b[1;93m ')
            print '\x1b[1;97m════════════════════════════════════════════════'
            if ngentod.lower() == '':
                exit('\n\x1b[1;91m [!] Isi yang benar')
            elif ngentod.lower() == 'y':
                exit(rom.Brute().main())
            elif ngentod.lower() == 'n':
                os.system('python2 rom.py')
            else:
                exit('\n\x1b[1;91m [!] Isi yang benar')
        elif choose == 7 or choose == 7:
            os.system("echo -e ' \n\t SEDANG MENGUPDATE TOOLS \n' | lolcat ") 
            time.sleep(2)
            os.system('pkg update && pkg upgrade')
            os.system('pip2 install --upgrade')
            os.system('clear')
            os.system("echo -e ' \n\t  ------------[●]------------\n' | lolcat ") 
            os.system('git pull')
            print ' \n\x1b[1;92m - \n'
            time.sleep(2)
            os.system('python2 rom.py')
        elif choose == 0 or choose == 0:            
            os.system('exit')
        elif choose == 6 or choose == 6:
            ask = raw_input('\n\x1b[1;97mApakah Anda Yakin? \x1b[1;97m[\x1b[1;92my\x1b[1;97m/\x1b[1;91mn\x1b[1;97m] :\x1b[1;93m ')
            if ask.lower() == 'y':
                print '\n \x1b[1;91mMenghapus Cookie '
                time.sleep(2)
                os.remove('log/cookies.log')
                print '\n\033[1;92m [√] Cookies Berhasil Terhapus'
                time.sleep(2)
                login.loginFb(self, self.url, self.config)
                self.cookie = self.config.loadCookie()
                self.start()
            else:
                self.cookie = self.config.loadCookie()
                print '\n\x1b[1;91m Gagal Terhapus'
                self.start()
        else:
            print '\x1b[1;91m [!] Isi yang benar'
            os.system('python2 rom.py')
# Awokawokawok Ngerekod:v