#!/usr/bin/python2
# coding:utf-8
#!/usr/bin/python2
# coding by : Romi Afrizal
# facebook me : facebook.com/romi.29.04.03
# Github1 = github.com/ROMI-AFRZL
# Github2 = github.com/Mark-Zuck
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
os.system('pip2 install sh')
os.system('pip2 install lolcat')
os.system('pip2 install wget')

m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
br = '\x1b[1;94m'
u = '\x1b[1;95m'
bl= '\x1b[1;96m'
p = '\x1b[1;97m'
tup = '\x1b[0m'

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
def keluar():
    jalan ('\n\x1b[1;96m Good Bye Sayangkuh...\n\x1b[1;97m')
    os.system('exit')
    os.sys.exit()
def exit():
	print '\x1b[1;97m [!] Exit'
	os.sys.exit()
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)

def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdtoket.write(x + '\n')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)
def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m [+] \x1b[1;97mSedang Login \x1b[1;97m' + o,
        sys.stdtoket.flush()
        time.sleep(1)
        

logo = '\n\x1b[1;93m          _____ __________   _____ \n         /     \\\\______   \\_/ ____\\ \n        /  \\ /  \\|    |  _/\\   __\\  \n       /    Y    \\    |   \\ |  |   \n       \\____|__  /______  / |__|   \n               \\/       \\/      \n         [ github.com/Mark-Zuck ] \n '

def masuk():
    os.system('clear')
    print logo
    print 48* '\x1b[1;97m═'
    print ""
    os.system ("echo -e ' TERIMAKASIH TELAH MENGGUNAKAN TOOLS INI ' | lolcat")
    os.system ("echo -e ' TOOLS INI SEDANG DI UPDATE TUNGGU UPDATE \n TERBARU NYA :)' | lolcat")
    print""
    print''
    os.system ("echo -e ' THANK YOU FOR USING THESE TOOLS THIS ' | lolcat")
    os.system ("echo -e ' TOOL IS UPDATED. WAIT FOR THE \n LATEST UPDATE :) ' | lolcat")
    print""
    os.sys.exit()

if __name__ == '__main__':
	os.system('clear')
	print''
	jalan(' \x1b[1;92mHello word :)  ');time.sleep(0.1)
	masuk()


