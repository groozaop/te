import os,pip
import requests
import platform
import random, time, datetime
import subprocess
import json, sys, re
import pathlib
import threading
try:
    import flag
except:
    pip.main(['install', 'emoji'])
    import emoji
from random import uniform


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

def check_os():
    return './' if platform.system() == "Windows" else "/sdcard/"

if check_os() == "./":
    my_os = "Wɪɴᴅᴏᴡs"
else:
    my_os = "Aɴᴅʀᴏɪᴅ"

my_cpu = platform.machine()
my_py = platform.python_version()

print(f"\33[1;32m OS in my system : {'Wɪɴᴅᴏᴡs' if platform.system() == 'Windows' else 'Aɴᴅʀᴏɪᴅ'}\33[0m")

def check_folders(folder_list):
    for folder in folder_list:
        os.makedirs(check_os() + folder, exist_ok = True)

check_folders(['Hits/', 'Hits/👺𝕎𝕋𝔽√ᵐ3ᵘCheck/'])

hits_folder = check_os() + 'Hits/👺𝕎𝕋𝔽√ᵐ3ᵘCheck/'

def save(hit):
    dosya=open(hits_folder + "👺𝙵𝙰𝚆𝙺𝙴𝚂" + host + "_" + str(time.strftime('%d-%m-%Y')) + '👺WTF√ᵐ3ᵘSingleCheck.txt','a+', encoding = 'utf-8')
    dosya.write(hit)
    dosya.close()    

def save1(hit):
    dosya=open(hits_folder + "👺𝙵𝙰𝚆𝙺𝙴𝚂" + host + "_" + str(time.strftime('%d-%m-%Y')) + '👺WTF√ᵐ3ᵘFileCheck.txt','a+', encoding = 'utf-8')
    dosya.write(hit)
    dosya.close()    

import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)
        

ses= requests.Session()

Pusheka = ("""\33[0m


╔════      ✮ WTF √ᵐ3ᵘ Check ✮       ════╗
                 ʙʏ ᴘᴜsʜᴇᴋᴀ  \33[0m\33[91m
      ╔═══╦═══╦╗╔╗╔╦╗╔═╦═══╦═══╗     
      ║╔══╣╔═╗║║║║║║║║╔╣╔══╣╔═╗║     
      ║╚══╣║─║║║║║║║╚╝╝║╚══╣╚══╗     
      ║╔══╣╚═╝║╚╝╚╝║╔╗║║╔══╩══╗║     
      ║║──║╔═╗╠╗╔╗╔╣║║╚╣╚══╣╚═╝║     
      ╚╝──╚╝─╚╝╚╝╚╝╚╝╚═╩═══╩═══╝      \33[0m
\33[90m            ᴘʏ ᴍᴏᴅᴅᴇᴅ ʙʏ ꜰᴀᴡᴋᴇꜱ      \n
\33[90m               ╔══╗   
\33[90m               ╚╗╔╝   
\33[90m               ╔╝\33[38;5;160m(¯`v´¯)    
\33[90m               ╚══\33[38;5;160m`.¸.\33[91m👺𝙵𝙰𝚆𝙺𝙴𝚂 \33[0m
""")

lines = ["""\33[0m

╔════      ✮ WTF √ᵐ3ᵘ Check ✮       ════╗
                 ʙʏ ᴘᴜsʜᴇᴋᴀ  \33[0m\33[91m
      ╔═══╦═══╦╗╔╗╔╦╗╔═╦═══╦═══╗     
      ║╔══╣╔═╗║║║║║║║║╔╣╔══╣╔═╗║     
      ║╚══╣║─║║║║║║║╚╝╝║╚══╣╚══╗     
      ║╔══╣╚═╝║╚╝╚╝║╔╗║║╔══╩══╗║     
      ║║──║╔═╗╠╗╔╗╔╣║║╚╣╚══╣╚═╝║     
      ╚╝──╚╝─╚╝╚╝╚╝╚╝╚═╩═══╩═══╝      \33[0m
\33[90m            ᴘʏ ᴍᴏᴅᴅᴇᴅ ʙʏ ꜰᴀᴡᴋᴇꜱ      \n
\33[90m               ╔══╗   
\33[90m               ╚╗╔╝   
\33[90m               ╔╝\33[38;5;160m(¯`v´¯)    
\33[90m               ╚══\33[38;5;160m`.¸.\33[91m👺𝙵𝙰𝚆𝙺𝙴𝚂 \33[0m


\33[93m To test a file with m3u in it, place it in the folder ➢ /Hits/👺𝕎𝕋𝔽√ᵐ3ᵘCheck/  

\33[92m          Always use with a VPN !!!
\33[0m"""]
for line in lines:
    for c in line:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(uniform(0, 0.01))
    print('')


HEADERd={
"Cookie": "stb_lang=en; timezone=Europe%2FIstanbul;",
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip, deflate",
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"User-Agent": "VLC",
            }
veri=""
panel=""
Active=0
global yaz
yaz=""
def data_server(scountry):
    bandera=''
    pais=''
    origen=''
    try:        
        codpais=scountry
        bandera=flag.flag(codpais)
        origen=bandera
    except:pass
    return origen

def kategori(katelink):
    try:
        res = ses.get(katelink,headers=HEADERd, timeout=1, verify=False)
        veri=""
        kate=""
        veri=str(res.text)
        for i in veri.split('category_name":"'):
            kate=kate+" «❖» "+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
    except:pass
    #print(kate)
    return kate


def check(veri,user,pas,full_url,host):
        global yaz
        global yaz1
        yaz=""
        yaz1=""
        status=veri.split('status":')[1]
        status=status.split(',')[0]
        status=status.replace('"',"")
        status=status.replace("Active","💚ACTIVE")
        katelink=f"{full_url}/player_api.php?username={user}&password={pas}&action=get_live_categories"

        acon=""
        acon=veri.split('active_cons":')[1]
        acon=acon.split(',')[0]
        acon=acon.replace('"',"")
        mcon=veri.split('max_connections":')[1]
        mcon=mcon.split(',')[0]
        mcon=mcon.replace('"',"")
        trial=veri.split('is_trial":')[1]
        trial=trial.split(',')[0]
        trial=trial.replace('"', '')
        trial=trial.replace("0","NO")
        trial=trial.replace("1","YES")
        timezone=veri.split('timezone":"')[1]
        timezone=timezone.split('",')[0]
        timezone=timezone.replace("\/","/")
        timezone=veri.split('timezone":"')[1]
        timezone=timezone.split('",')[0]
        timezone=timezone.replace("\/","/")
        timezone=timezone.replace("UTC","UTC 🏳️‍🌈")
        timezone=timezone.replace("Europe/Andorra","Europe/Andorra 🇦🇩")
        timezone=timezone.replace("Asia/Dubai","Asia/Dubai 🇦🇪 United Arab Emirates")
        timezone=timezone.replace("Asia/Kabul","Asia/Kabul 🇦🇫 Afghanistan")
        timezone=timezone.replace("America/Antigua","America/Antigua and Barbuda 🇦🇬")
        timezone=timezone.replace("America/Anguilla","America/Anguilla 🇦🇮")
        timezone=timezone.replace("Europe/Tirane","Europe/Tirane 🇦🇱 Albania")
        timezone=timezone.replace("Asia/Yerevan","Asia/Yerevan 🇦🇲 Armenia")
        timezone=timezone.replace("Africa/Luanda","Africa/Luanda 🇦🇴 Angola")
        timezone=timezone.replace("Antarctica/McMurdo","Antarctica/McMurdo 🇦🇶")
        timezone=timezone.replace("Antarctica/South_Pole","Antarctica/South Pole 🇦🇶")
        timezone=timezone.replace("Antarctica/Rothera","Antarctica/Rothera 🇦🇶")
        timezone=timezone.replace("Antarctica/Palmer","Antarctica/Palmer 🇦🇶")
        timezone=timezone.replace("Antarctica/Mawson","Antarctica/Mawson 🇦🇶")
        timezone=timezone.replace("Antarctica/Davis","Antarctica/Davis 🇦🇶")
        timezone=timezone.replace("Antarctica/Casey","Antarctica/Casey 🇦🇶")
        timezone=timezone.replace("Antarctica/Vostok","Antarctica/Vostok 🇦🇶")
        timezone=timezone.replace("Antarctica/DumontDUrville","Antarctica/DumontDUrville 🇦🇶")
        timezone=timezone.replace("Antarctica/Syowa","Antarctica/Syowa 🇦🇶")
        timezone=timezone.replace("Antarctica/Macquarie","Antarctica/Macquarie 🇦🇶")
        timezone=timezone.replace("America/Argentina/Buenos_Aires","America/Buenos Aires 🇦🇷 Argentina")
        timezone=timezone.replace("America/Argentina/Cordoba","America/Cordoba 🇦🇷 Argentina")
        timezone=timezone.replace("America/Argentina/Salta","America/Salta 🇦🇷 Argentina")
        timezone=timezone.replace("America/Argentina/Jujuy","America/Jujuy 🇦🇷 Argentina")
        timezone=timezone.replace("America/Argentina/Tucuman","America/Tucuman 🇦🇷 Argentina")
        timezone=timezone.replace("America/Argentina/Catamarca","America/Catamarca 🇦🇷 Argentina")
        timezone=timezone.replace("America/Argentina/La_Rioja","America/La Rioja 🇦🇷 Argentina")
        timezone=timezone.replace("America/Argentina/San_Juan","America/San Juan 🇦🇷 Argentina")
        timezone=timezone.replace("America/Argentina/Mendoza","America/Mendoza 🇦🇷 Argentina")
        timezone=timezone.replace("America/Argentina/San_Luis","America/San Luis 🇦🇷 Argentina")
        timezone=timezone.replace("America/Argentina/Rio_Gallegos","America/Rio Gallegos 🇦🇷 Argentina")
        timezone=timezone.replace("America/Argentina/Ushuaia","America/Ushuaia 🇦🇷 Argentina")
        timezone=timezone.replace("Pacific/Pago_Pago","Pacific/Pago Pago 🇦🇸 American Samoa")
        timezone=timezone.replace("Europe/Vienna","Europe/Vienna 🇦🇹 Austria")
        timezone=timezone.replace("Australia/Lord_Howe","Australia/Lord Howe 🇦🇺 Australia")
        timezone=timezone.replace("Australia/Hobart","Australia/Hobart 🇦🇺 Australia")
        timezone=timezone.replace("Australia/Currie","Australia/Currie 🇦🇺 Australia")
        timezone=timezone.replace("Australia/Melbourne","Australia/Melbourne 🇦🇺 Australia")
        timezone=timezone.replace("Australia/Sydney","Australia/Sydney 🇦🇺 Australia")
        timezone=timezone.replace("Australia/Broken_Hill","Australia/Broken Hill 🇦🇺 Australia")
        timezone=timezone.replace("Australia/Brisbane","Australia/Brisbane 🇦🇺 Australia")
        timezone=timezone.replace("Australia/Lindeman","Australia/Lindeman 🇦🇺 Australia")
        timezone=timezone.replace("Australia/Adelaide","Australia/Adelaide 🇦🇺 Australia")
        timezone=timezone.replace("Australia/Darwin","Australia/Darwin 🇦🇺 Australia")
        timezone=timezone.replace("Australia/Perth","Australia/Perth 🇦🇺 Australia")
        timezone=timezone.replace("Australia/Eucla","Australia/Eucla 🇦🇺 Australia")
        timezone=timezone.replace("America/Aruba","America/Aruba 🇦🇼")
        timezone=timezone.replace("Europe/Mariehamn","Europe/Mariehamn 🇦🇽 Åland Islands")
        timezone=timezone.replace("Asia/Baku","Asia/Baku 🇦🇿 Azerbaijan")
        timezone=timezone.replace("Europe/Sarajevo","Europe/Sarajevo 🇧🇦 Bosnia and Herzegovina")
        timezone=timezone.replace("America/Barbados","America/Barbados 🇧🇧")
        timezone=timezone.replace("Asia/Dhaka","Asia/Dhaka 🇧🇩 Bangladesh")
        timezone=timezone.replace("Europe/Brussels","Europe/Brussels 🇧🇪 Belgium")
        timezone=timezone.replace("Africa/Ouagadougou","Africa/Ouagadougou 🇧🇫 Burkina Faso")
        timezone=timezone.replace("Europe/Sofia","Europe/Sofia 🇧🇬 Bulgaria")
        timezone=timezone.replace("Asia/Bahrain","Asia/Bahrain 🇧🇾")
        timezone=timezone.replace("Africa/Bujumbura","Africa/Bujumbura 🇧🇮 Burundi")
        timezone=timezone.replace("Africa/Porto","Africa/Porto-Novo 🇧🇯 Benin")
        timezone=timezone.replace("America/St_Barthelemy","America/Saint Barthélemy 🇧🇱")
        timezone=timezone.replace("Atlantic/Bermuda","Atlantic/Bermuda 🇧🇲")
        timezone=timezone.replace("Asia/Brunei","Asia/Brunei 🇧🇳")
        timezone=timezone.replace("America/La_Paz","America/La Paz 🇧🇴 Bolivia")
        timezone=timezone.replace("America/Kralendijk","America/Kralendijk 🇧🇶 Bonaire")
        timezone=timezone.replace("America/Noronha","America/Noronha 🇧🇷 Brazil")
        timezone=timezone.replace("America/Belem","America/Belém 🇧🇷 Brazil")
        timezone=timezone.replace("America/Fortaleza","America/Fortaleza 🇧🇷 Brazil")
        timezone=timezone.replace("America/Recife","America/Recife 🇧🇷 Brazil")
        timezone=timezone.replace("America/Araguaina","America/Araguaína 🇧🇷 Brazil")
        timezone=timezone.replace("America/Maceio","America/Maceió 🇧🇷 Brazil")
        timezone=timezone.replace("America/Bahia","America/Bahia 🇧🇷 Brazil")
        timezone=timezone.replace("America/Sao_Paulo","America/São Paulo 🇧🇷 Brazil")
        timezone=timezone.replace("America/Campo_Grande","America/Campo Grande 🇧🇷 Brazil")
        timezone=timezone.replace("America/Cuiaba","America/Cuiabá 🇧🇷 Brazil")
        timezone=timezone.replace("America/Santarem","America/Santarém 🇧🇷 Brazil")
        timezone=timezone.replace("America/Porto_Velho","America/Porto Velho 🇧🇷 Brazil")
        timezone=timezone.replace("America/Boa_Vista","America/Boa Vista 🇧🇷 Brazil")
        timezone=timezone.replace("America/Manaus","America/Manaus 🇧🇷 Brazil")
        timezone=timezone.replace("America/Eirunepe","America/Eirunepé 🇧🇷 Brazil")
        timezone=timezone.replace("America/Rio_Branco","America/Rio Branco 🇧🇷 Brazil")
        timezone=timezone.replace("America/Nassau","America/Nassau 🇧🇸 Bahamas")
        timezone=timezone.replace("Asia/Thimphu","Asia/Thimphu 🇧🇹 Bhutan")
        timezone=timezone.replace("Africa/Gaborone","Africa/Gaborone 🇧🇼 Botswana")
        timezone=timezone.replace("Europe/Minsk","Europe/Minsk 🇧🇾 Belarus")
        timezone=timezone.replace("America/Belize","America/Belize 🇧🇿")
        timezone=timezone.replace("America/St_Johns","America/Saint Johns 🇦🇬 Antigua and Barbuda")
        timezone=timezone.replace("America/Halifax","America/Halifax 🇨🇦 Canada")
        timezone=timezone.replace("America/Glace_Bay","America/Glace Bay 🇨🇦 Canada")
        timezone=timezone.replace("America/Moncton","America/Moncton 🇨🇦 Canada")
        timezone=timezone.replace("America/Goose_Bay","America/Goose Bay 🇨🇦 Canada")
        timezone=timezone.replace("America/Blanc","America/Blanc 🇨🇦 Canada")
        timezone=timezone.replace("America/Montreal","America/Montreal 🇨🇦 Canada")
        timezone=timezone.replace("America/Toronto","America/Toronto 🇨🇦 Canada")
        timezone=timezone.replace("America/Nipigon","America/Nipigon 🇨🇦 Canada")
        timezone=timezone.replace("America/Thunder_Bay","America/Thunder Bay 🇨🇦 Canada")
        timezone=timezone.replace("America/Iqaluit","America/Iqaluit 🇨🇦 Canada")
        timezone=timezone.replace("America/Pangnirtung","America/Pangnirtung 🇨🇦 Canada")
        timezone=timezone.replace("America/Resolute","America/Resolute 🇨🇦 Canada")
        timezone=timezone.replace("America/Atikokan","America/Atikokan 🇨🇦 Canada")
        timezone=timezone.replace("America/Rankin_Inlet","America/Rankin Inlet 🇨🇦 Canada")
        timezone=timezone.replace("America/Winnipeg","America/Winnipeg 🇨🇦 Canada")
        timezone=timezone.replace("America/Rainy_River","America/Rainy River 🇨🇦 Canada")
        timezone=timezone.replace("America/Regina","America/Regina 🇨🇦 Canada")
        timezone=timezone.replace("America/Swift_Current","America/Swift Current 🇨🇦 Canada")
        timezone=timezone.replace("America/Edmonton","America/Edmonton 🇨🇦 Canada")
        timezone=timezone.replace("America/Cambridge_Bay","America/Cambridge Bay 🇨🇦 Canada")
        timezone=timezone.replace("America/Yellowknife","America/Yellowknife 🇨🇦 Canada")
        timezone=timezone.replace("America/Inuvik","America/Inuvik 🇨🇦 Canada")
        timezone=timezone.replace("America/Creston","America/Creston 🇨🇦 Canada")
        timezone=timezone.replace("America/Dawson_Creek","America/Dawson Creek 🇨🇦 Canada")
        timezone=timezone.replace("America/Vancouver","America/Vancouver 🇨🇦 Canada")
        timezone=timezone.replace("America/Whitehorse","America/Whitehorse 🇨🇦 Canada")
        timezone=timezone.replace("America/Dawson","America/Dawson 🇨🇦 Canada")
        timezone=timezone.replace("Indian/Cocos","Indian/Cocos Islands 🇨🇨")
        timezone=timezone.replace("Africa/Kinshasa","Africa/Kinshasa 🇨🇩 Democratic Republic of the Congo")
        timezone=timezone.replace("Africa/Lubumbashi","Africa/Lubumbashi 🇨🇩 Democratic Republic of the Congo")
        timezone=timezone.replace("Africa/Brazzaville","Africa/Brazzaville 🇨🇩 Democratic Republic of the Congo")
        timezone=timezone.replace("Africa/Bangui","Africa/Bangui 🇨🇫 Central African Republic")
        timezone=timezone.replace("Europe/Zurich","Europe/Zurich 🇨🇭 Switzerland")
        timezone=timezone.replace("Africa/Abidjan","Africa/Abidjan 🇨🇮 Côte d'Ivoire")
        timezone=timezone.replace("Pacific/Rarotonga","Pacific/Rarotonga 🇨🇰 Cook Islands")
        timezone=timezone.replace("America/Santiago","America/Santiago 🇨🇱 Chile")
        timezone=timezone.replace("Pacific/Easter","Pacific/Easter Island 🇨🇱 Chile")
        timezone=timezone.replace("Africa/Douala","Africa/Douala 🇨🇲 Cameroon")
        timezone=timezone.replace("Asia/Shanghai","Asia/Shanghai 🇨🇳 China")
        timezone=timezone.replace("Asia/Harbin","Asia/Harbin 🇨🇳 China")
        timezone=timezone.replace("Asia/Chongqing","Asia/Chongqing 🇨🇳 China")
        timezone=timezone.replace("Asia/Urumqi","Asia/Urumqi 🇨🇳 China")
        timezone=timezone.replace("Asia/Kashgar","Asia/Kashgar 🇨🇳 China")
        timezone=timezone.replace("America/Bogota","America/Bogota 🇨🇴 Colombia")
        timezone=timezone.replace("America/Costa_Rica","America/Costa Rica 🇨🇷")
        timezone=timezone.replace("America/Havana","America/Havana 🇨🇺 Cuba")
        timezone=timezone.replace("Atlantic/Cape_Verde","Atlantic/Cape Verde 🇨🇻")
        timezone=timezone.replace("America/Curacao","America/Curacao 🇨🇼")
        timezone=timezone.replace("Indian/Christmas","Indian/Christmas Island 🇨🇽")
        timezone=timezone.replace("Asia/Nicosia","Asia/Nicosia 🇨🇾 Cyprus")
        timezone=timezone.replace("Europe/Prague","Europe/Prague 🇨🇿 Czech Republic")
        timezone=timezone.replace("Europe/Berlin","Europe/Berlin 🇩🇪 Germany")
        timezone=timezone.replace("Africa/Djibouti","Africa/Djibouti 🇩🇯")
        timezone=timezone.replace("Europe/Copenhagen","Europe/Copenhagen 🇩🇰 Denmark")
        timezone=timezone.replace("America/Dominica","America/Dominica 🇩🇲") 
        timezone=timezone.replace("America/Santo_Domingo","America/Santo Domingo 🇩🇴 Dominican Republic")
        timezone=timezone.replace("Africa/Algiers","Africa/Algiers 🇩🇿 Algeria")
        timezone=timezone.replace("America/Guayaquil","America/Guayaquil 🇪🇨 Ecuador")
        timezone=timezone.replace("Pacific/Galapagos","Pacific/Galápagos Islands 🇪🇨 Ecuador")
        timezone=timezone.replace("Europe/Tallinn","Europe/Tallinn 🇪🇪 Estonia")
        timezone=timezone.replace("Africa/Cairo","Africa/Cairo 🇪🇬 Egypt")
        timezone=timezone.replace("Africa/El_Aaiun","Africa/El Aaiun 🇪🇭 Western Sahara")
        timezone=timezone.replace("Africa/Asmara","Africa/Asmara 🇪🇷 Eritrea")
        timezone=timezone.replace("Europe/Madrid","Europe/Madrid 🇪🇸 Spain")
        timezone=timezone.replace("Africa/Ceuta","Africa/Ceuta 🇪🇸 Spain")
        timezone=timezone.replace("Atlantic/Canary","Atlantic/Canary Islands 🇪🇸 Spain")
        timezone=timezone.replace("Africa/Addis_Ababa","Africa/Addis Ababa 🇪🇹 Ethiopia")
        timezone=timezone.replace("Europe/Helsinki","Europe/Helsinki 🇫🇮 Finland")
        timezone=timezone.replace("Pacific/Fiji","Pacific/Fiji 🇫🇯")
        timezone=timezone.replace("Atlantic/Stanley","Atlantic/Stanley 🇫🇰 Falkland Islands")
        timezone=timezone.replace("Pacific/Chuuk","Pacific/Chuuk 🇫🇲 Micronesia")
        timezone=timezone.replace("Pacific/Pohnpei","Pacific/Pohnpei 🇫🇲 Micronesia")
        timezone=timezone.replace("Pacific/Kosrae","Pacific/Kosrae 🇫🇲 Micronesia")
        timezone=timezone.replace("Atlantic/Faroe","Atlantic/Faroe Islands 🇫🇴")
        timezone=timezone.replace("Europe/Paris","Europe/Paris 🇫🇷 France")
        timezone=timezone.replace("Africa/Libreville","Africa/Libreville 🇬🇦 Gabon")
        timezone=timezone.replace("Europe/London","Europe/London 🇬🇧 Great Britain")
        timezone=timezone.replace("America/Grenada","America/Grenada 🇬🇩")
        timezone=timezone.replace("Asia/Tbilisi","Asia/Tbilisi 🇬🇪 Georgia")
        timezone=timezone.replace("America/Cayenne","America/Cayenne 🇬🇫 French Guiana")
        timezone=timezone.replace("Europe/Guernsey","Europe/Guernsey 🇬🇬")
        timezone=timezone.replace("Africa/Accra","Africa/Accra 🇬🇭 Ghana")
        timezone=timezone.replace("Europe/Gibraltar","Europe/Gibraltar 🇬🇮")
        timezone=timezone.replace("America/Godthab","America/Godthab 🇬🇱 Greenland")
        timezone=timezone.replace("America/Danmarkshavn","America/Danmarkshavn 🇬🇱 Greenland")
        timezone=timezone.replace("America/Scoresbysund","America/Scoresbysund 🇬🇱 Greenland")
        timezone=timezone.replace("America/Thule","America/Thule 🇬🇱 Greenland")
        timezone=timezone.replace("Africa/Banjul","Africa/Banjul 🇬🇲 Gambia")
        timezone=timezone.replace("Africa/Conakry","Africa/Conakry 🇬🇳 Guinea")
        timezone=timezone.replace("America/Guadeloupe","America/Guadeloupe 🇬🇵")
        timezone=timezone.replace("Africa/Malabo","Africa/Malabo 🇬🇶 Equatorial Guinea")
        timezone=timezone.replace("Europe/Athens","Europe/Athens 🇬🇷 Greece")
        timezone=timezone.replace("Atlantic/South_Georgia","Atlantic/South Georgia and the South Sandwich Islands 🇬🇸")
        timezone=timezone.replace("America/Guatemala","America/Guatemala 🇬🇹")
        timezone=timezone.replace("Pacific/Guam","Pacific/Guam 🇬🇺")
        timezone=timezone.replace("Africa/Bissau","Africa/Bissau 🇬🇼 Guinea-Bissau")
        timezone=timezone.replace("America/Guyana","America/Guyana 🇬🇾")
        timezone=timezone.replace("Asia/Hong_Kong","Asia/Hong Kong 🇭🇰")
        timezone=timezone.replace("America/Tegucigalpa","America/Tegucigalpa 🇭🇳 Honduras")
        timezone=timezone.replace("Europe/Zagreb","Europe/Zagreb 🇭🇷 Croatia")
        timezone=timezone.replace("America/Port","America/Port-au-Prince 🇭🇹 Haiti")
        timezone=timezone.replace("Europe/Budapest","Europe/Budapest 🇭🇺 Hungary")
        timezone=timezone.replace("Asia/Jakarta","Asia/Jakarta 🇮🇩 Indonesia")
        timezone=timezone.replace("Asia/Pontianak","Asia/Pontianak 🇮🇩 Indonesia")
        timezone=timezone.replace("Asia/Makassar","Asia/Makassar 🇮🇩 Indonesia")
        timezone=timezone.replace("Asia/Jayapura","Asia/Jayapura 🇮🇩 Indonesia")
        timezone=timezone.replace("Europe/Dublin","Europe/Dublin 🇮🇪 Ireland")
        timezone=timezone.replace("Asia/Jerusalem","Asia/Jerusalem 🇮🇱 Israel")
        timezone=timezone.replace("Europe/Isle_of_Man","Europe/Isle of Man 🇮🇲")
        timezone=timezone.replace("Asia/Kolkata","Asia/Kolkata 🇮🇳 India")
        timezone=timezone.replace("Indian/Chagos","Indian/Chagos 🇮🇴 British Indian Ocean Territory")
        timezone=timezone.replace("Asia/Baghdad","Asia/Baghdad 🇮🇶 Iraq")
        timezone=timezone.replace("Asia/Tehran","Asia/Tehran 🇮🇷 Iran")
        timezone=timezone.replace("Atlantic/Reykjavik","Atlantic/Reykjavik 🇮🇸 Iceland")
        timezone=timezone.replace("Europe/Rome","Europe/Rome 🇮🇹 Italy")
        timezone=timezone.replace("Europe/Jersey","Europe/Jersey 🇯🇪")
        timezone=timezone.replace("America/Jamaica","America/Jamaica 🇯🇲")
        timezone=timezone.replace("Asia/Amman","Asia/Amman 🇯🇴 Jordan") 
        timezone=timezone.replace("Asia/Tokyo","Asia/Tokyo 🇯🇵 Japan")
        timezone=timezone.replace("Africa/Nairobi","Africa/Nairobi 🇰🇪 Kenya")
        timezone=timezone.replace("Asia/Bishkek","Asia/Bishkek 🇰🇬 Kyrgyzstan")
        timezone=timezone.replace("Asia/Phnom_Penh","Asia/Phnom Penh 🇰🇭 Cambodia")
        timezone=timezone.replace("Pacific/Tarawa","Pacific/Tarawa 🇰🇮 Kiribati")
        timezone=timezone.replace("Pacific/Enderbury","Pacific/Enderbury 🇰🇮 Kiribati")
        timezone=timezone.replace("Pacific/Kiritimati","Pacific/Kiritimati 🇰🇮 Kiribati")
        timezone=timezone.replace("Indian/Comoro","Indian/Comoro Islands 🇰🇲")
        timezone=timezone.replace("America/St_Kitts","America/Saint Kitts and Nevis 🇰🇳")
        timezone=timezone.replace("Asia/Pyongyang","Asia/Pyongyang 🇰🇵 North Korea")
        timezone=timezone.replace("Asia/Seoul","Asia/Seoul 🇰🇷 South Korea")
        timezone=timezone.replace("Asia/Kuwait","Asia/Kuwait 🇰🇼")
        timezone=timezone.replace("America/Cayman","America/Cayman Islands 🇰🇾")
        timezone=timezone.replace("Asia/Almaty","Asia/Almaty 🇰🇿 Kazakhstan")
        timezone=timezone.replace("Asia/Qyzylorda","Asia/Qyzylorda 🇰🇿 Kazakhstan")
        timezone=timezone.replace("Asia/Aqtobe","Asia/Aqtobe 🇰🇿 Kazakhstan")
        timezone=timezone.replace("Asia/Aqtau","Asia/Aqtau 🇰🇿 Kazakhstan")
        timezone=timezone.replace("Asia/Oral","Asia/Oral 🇰🇿 Kazakhstan")
        timezone=timezone.replace("Asia/Vientiane","Asia/Vientiane 🇱🇦 Laos")
        timezone=timezone.replace("Asia/Beirut","Asia/Beirut 🇱🇧 Lebanon")
        timezone=timezone.replace("America/St_Lucia","America/Saint Lucia 🇱🇨")
        timezone=timezone.replace("Europe/Vaduz","Europe/Vaduz 🇱🇮 Liechtenstein")
        timezone=timezone.replace("Asia/Colombo","Asia/Colombo 🇱🇰 Sri Lanka")
        timezone=timezone.replace("Africa/Monrovia","Africa/Monrovia 🇱🇷 Liberia")
        timezone=timezone.replace("Africa/Maseru","Africa/Maseru 🇱🇸 Lesotho")
        timezone=timezone.replace("Europe/Vilnius","Europe/Vilnius 🇱🇹 Lithuania")
        timezone=timezone.replace("Europe/Luxembourg","Europe/Luxembourg 🇱🇺")
        timezone=timezone.replace("Europe/Riga","Europe/Riga 🇱🇻 Latvia")
        timezone=timezone.replace("Africa/Tripoli","Africa/Tripoli 🇱🇾 Libya")
        timezone=timezone.replace("Africa/Casablanca","Africa/Casablanca 🇲🇦 Morocco")
        timezone=timezone.replace("Europe/Monaco","Europe/Monaco 🇲🇨")
        timezone=timezone.replace("Europe/Chisinau","Europe/Chisinau 🇲🇩 Moldova")
        timezone=timezone.replace("Europe/Podgorica","Europe/Podgorica 🇲🇪 Montenegro")
        timezone=timezone.replace("America/Marigot","America/Marigot 🇲🇫 Saint Martin")
        timezone=timezone.replace("Indian/Antananarivo","Indian/Antananarivo 🇲🇬 Madagascar")
        timezone=timezone.replace("Pacific/Majuro","Pacific/Majuro 🇲🇭 Marshall Islands")
        timezone=timezone.replace("Pacific/Kwajalein","Pacific/Kwajalein 🇲🇭 Marshall Islands")
        timezone=timezone.replace("Europe/Skopje","Europe/Skopje ??🇰 North Macedonia")
        timezone=timezone.replace("Africa/Bamako","Africa/Bamako 🇲🇱 Mali")
        timezone=timezone.replace("Asia/Rangoon","Asia/Rangoon 🇲🇲 Myanmar")
        timezone=timezone.replace("Asia/Ulaanbaatar","Asia/Ulaanbaatar 🇲🇳 Mongolia")
        timezone=timezone.replace("Asia/Hovd","Asia/Hovd 🇲🇳 Mongolia")
        timezone=timezone.replace("Asia/Choibalsan","Asia/Choibalsan 🇲🇳 Mongolia")
        timezone=timezone.replace("Asia/Macau","Asia/Macau 🇲🇴")
        timezone=timezone.replace("Pacific/Saipan","Pacific/Saipan 🇲🇵 Northern Mariana Islands")
        timezone=timezone.replace("America/Martinique","America/Martinique 🇲🇶")
        timezone=timezone.replace("Africa/Nouakchott","Africa/Nouakchott 🇲🇷 Mauritania")
        timezone=timezone.replace("America/Montserrat","America/Montserrat 🇲🇸")
        timezone=timezone.replace("Europe/Malta","Europe/Malta 🇲🇹")
        timezone=timezone.replace("Indian/Mauritius","Indian/Mauritius 🇲🇺")
        timezone=timezone.replace("Indian/Maldives","Indian/Maldives 🇲🇻")
        timezone=timezone.replace("Africa/Blantyre","Africa/Blantyre 🇲🇼 Malawi")
        timezone=timezone.replace("America/Mexico_City","America/Mexico City 🇲🇽 Mexico")
        timezone=timezone.replace("America/Cancun","America/Cancun 🇲🇽 Mexico")
        timezone=timezone.replace("America/Merida","America/Merida 🇲🇽 Mexico")
        timezone=timezone.replace("America/Monterrey","America/Monterrey 🇲🇽 Mexico")
        timezone=timezone.replace("America/Matamoros","America/Matamoros 🇲🇽 Mexico")
        timezone=timezone.replace("America/Mazatlan","America/Mazatlan 🇲🇽 Mexico")
        timezone=timezone.replace("America/Chihuahua","America/Chihuahua 🇲🇽 Mexico")
        timezone=timezone.replace("America/Ojinaga","America/Ojinaga 🇲🇽 Mexico")
        timezone=timezone.replace("America/Hermosillo","America/Hermosillo 🇲🇽 Mexico")
        timezone=timezone.replace("America/Tijuana","America/Tijuana 🇲🇽 Mexico")
        timezone=timezone.replace("America/Santa_Isabel","America/Santa Isabel 🇲🇽 Mexico")
        timezone=timezone.replace("America/Bahia_Banderas","America/Bahia Banderas 🇲🇽 Mexico")
        timezone=timezone.replace("Asia/Kuala_Lumpur","Asia/Kuala Lumpur 🇲🇾 Malaysia")
        timezone=timezone.replace("Asia/Kuching","Asia/Kuching 🇲🇾 Malaysia")
        timezone=timezone.replace("Africa/Maputo","Africa/Maputo 🇲🇿 Mozambique")
        timezone=timezone.replace("Africa/Windhoek","Africa/Windhoek 🇳🇦 Namibia")
        timezone=timezone.replace("Pacific/Noumea","Pacific/Noumea 🇳🇨 New Caledonia")
        timezone=timezone.replace("Africa/Niamey","Africa/Niamey 🇳🇪 Niger")
        timezone=timezone.replace("Pacific/Norfolk","Pacific/Norfolk Island 🇳🇫")
        timezone=timezone.replace("Africa/Lagos","Africa/Lagos 🇳🇬 Nigeria")
        timezone=timezone.replace("America/Managua","America/Managua 🇳🇮 Nicaragua")
        timezone=timezone.replace("Europe/Amsterdam","Europe/Amsterdam 🇳🇱 Netherlands")
        timezone=timezone.replace("Europe/Oslo","Europe/Oslo 🇳🇴 Norway")
        timezone=timezone.replace("Asia/Kathmandu","Asia/Kathmandu 🇳🇵 Nepal")
        timezone=timezone.replace("Pacific/Nauru","Pacific/Nauru 🇳🇷")
        timezone=timezone.replace("Pacific/Niue","Pacific/Niue 🇳🇺")
        timezone=timezone.replace("Pacific/Auckland","Pacific/Auckland 🇳🇿 New Zealand")
        timezone=timezone.replace("Pacific/Chatham","Pacific/Chatham 🇳🇿 New Zealand")
        timezone=timezone.replace("Asia/Muscat","Asia/Muscat 🇴🇲 Oman")
        timezone=timezone.replace("America/Panama","America/Panama 🇵🇦")
        timezone=timezone.replace("America/Lima","America/Lima 🇵🇪 Peru")
        timezone=timezone.replace("Pacific/Tahiti","Pacific/Tahiti 🇵🇫 French Polynesia")
        timezone=timezone.replace("Pacific/Marquesas","Pacific/Marquesas 🇵🇫 French Polynesia")
        timezone=timezone.replace("Pacific/Gambier","Pacific/Gambier 🇵🇫 French Polynesia")
        timezone=timezone.replace("Pacific/Port_Moresby","Pacific/Port_Moresby 🇵🇬 Papua New Guinea")
        timezone=timezone.replace("Asia/Manila","Asia/Manila 🇵🇭 Philippines")
        timezone=timezone.replace("Asia/Karachi","Asia/Karachi 🇵🇰 Pakistan")
        timezone=timezone.replace("Europe/Warsaw","Europe/Warsaw 🇵🇱 Poland")
        timezone=timezone.replace("America/Miquelon","America/Saint Pierre and Miquelon 🇵🇲")
        timezone=timezone.replace("Pacific/Pitcairn","Pacific/Pitcairn Islands 🇵🇳")
        timezone=timezone.replace("America/Puerto_Rico","America/Puerto Rico 🇵🇷")
        timezone=timezone.replace("Asia/Gaza","Asia/Gaza 🇵🇸 Palastinian Territories")
        timezone=timezone.replace("Asia/Hebron","Asia/Hebron 🇵🇸 Palastinian Territories")
        timezone=timezone.replace("Europe/Lisbon","Europe/Lisbon 🇵🇹 Portugal")
        timezone=timezone.replace("Atlantic/Madeira","Atlantic/Madeira 🇵🇹 Portugal")
        timezone=timezone.replace("Atlantic/Azores","Atlantic/Azores 🇵🇹 Portugal")
        timezone=timezone.replace("Pacific/Palau","Pacific/Palau 🇵🇼")
        timezone=timezone.replace("America/Asuncion","America/Asuncion 🇵🇾 Paraguay")
        timezone=timezone.replace("Asia/Qatar","Asia/Qatar 🇶🇦")
        timezone=timezone.replace("Indian/Reunion","Indian/Réunion 🇷🇪")
        timezone=timezone.replace("Europe/Bucharest","Europe/Bucharest 🇷🇴 Romania")
        timezone=timezone.replace("Europe/Belgrade","Europe/Belgrade 🇷🇸 Serbia")
        timezone=timezone.replace("Europe/Kaliningrad","Europe/Kaliningrad 🇷🇺 Russia")
        timezone=timezone.replace("Europe/Moscow","Europe/Moscow 🇷🇺 Russia")
        timezone=timezone.replace("Europe/Volgograd","Europe/Volgograd 🇷🇺 Russia")
        timezone=timezone.replace("Europe/Samara","Europe/Samara 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Yekaterinburg","Asia/Yekaterinburg 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Omsk","Asia/Omsk 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Novosibirsk","Asia/Novosibirsk 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Novokuznetsk","Asia/Novokuznetsk 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Krasnoyarsk","Asia/Krasnoyarsk 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Irkutsk","Asia/Irkutsk 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Yakutsk","Asia/Yakutsk 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Vladivostok","Asia/Vladivostok 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Sakhalin","Asia/Sakhalin 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Magadan","Asia/Magadan 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Kamchatka","Asia/Kamchatka 🇷🇺 Russia")
        timezone=timezone.replace("Asia/Anadyr","Asia/Anadyr 🇷🇺 Russia")
        timezone=timezone.replace("Africa/Kigali","Africa/Kigali 🇷🇼 Rwanda")
        timezone=timezone.replace("Asia/Riyadh","Asia/Riyadh 🇸🇦 Saudi Arabia")
        timezone=timezone.replace("Pacific/Guadalcanal","Pacific/Guadalcanal 🇸🇧 Solomon Islands")
        timezone=timezone.replace("Indian/Mahe","Indian/Mahe 🇸🇨 Seychelles")
        timezone=timezone.replace("Africa/Khartoum","Africa/Khartoum 🇸🇩 Sudan")
        timezone=timezone.replace("Europe/Stockholm","Europe/Stockholm 🇸🇪 Sweden")
        timezone=timezone.replace("Asia/Singapore","Asia/Singapore 🇸🇬")
        timezone=timezone.replace("Atlantic/St_Helena","Atlantic/Saint Helena 🇸🇭")
        timezone=timezone.replace("Europe/Ljubljana","Europe/Ljubljana 🇸🇮 Slovenia")
        timezone=timezone.replace("Arctic/Longyearbyen","Arctic/Longyearbyen 🇸🇯 Svalbard and Jan Mayen")
        timezone=timezone.replace("Europe/Bratislava","Europe/Bratislava 🇸🇰 Slovakia")
        timezone=timezone.replace("Africa/Freetown","Africa/Freetown 🇸🇱 Sierra Leone")
        timezone=timezone.replace("Europe/San_Marino","Europe/San Marino 🇸🇲")
        timezone=timezone.replace("Africa/Dakar","Africa/Dakar 🇸🇳 Senegal")
        timezone=timezone.replace("Africa/Mogadishu","Africa/Mogadishu 🇸🇴 Somalia")
        timezone=timezone.replace("America/Paramaribo","America/Paramaribo 🇸🇷 Suriname")
        timezone=timezone.replace("Africa/Juba","Africa/Juba 🇸🇸 South Sudan")
        timezone=timezone.replace("Africa/Sao_Tome","Africa/São Tomé and Príncipe 🇸🇹")
        timezone=timezone.replace("America/El_Salvador","America/El Salvador 🇸🇻")
        timezone=timezone.replace("America/Lower_Princes","America/Lower Princes 🇸🇽 Sint Maarten")
        timezone=timezone.replace("Asia/Damascus","Asia/Damascus 🇸🇾 Syria")
        timezone=timezone.replace("Africa/Mbabane","Africa/Mbabane 🇸🇿 Swaziland")
        timezone=timezone.replace("America/Grand_Turk","America/Grand Turk Turks and Caicos Islands 🇹🇨")
        timezone=timezone.replace("Africa/Ndjamena","Africa/Ndjamena 🇹🇩 Chad")
        timezone=timezone.replace("Indian/Kerguelen","Indian/Kerguelen 🇹🇫 French Southern Territories")
        timezone=timezone.replace("Africa/Lome","Africa/Lome 🇹🇬 Togo")
        timezone=timezone.replace("Asia/Bangkok","Asia/Bangkok 🇹🇭 Thailand")
        timezone=timezone.replace("Asia/Dushanbe","Asia/Dushanbe 🇹🇯 Tajikistan")
        timezone=timezone.replace("Pacific/Fakaofo","Pacific/Fakaofo 🇹🇰 Tokelau")
        timezone=timezone.replace("Asia/Dili","Asia/Dili 🇹🇱 Timor-Leste")
        timezone=timezone.replace("Asia/Ashgabat","Asia/Ashgabat 🇹🇲 Turkmenistan")
        timezone=timezone.replace("Africa/Tunis","Africa/Tunis 🇹🇳 Tunisia")
        timezone=timezone.replace("Pacific/Tongatapu","Pacific/Tongatapu 🇹🇴 Tonga")
        timezone=timezone.replace("Europe/Istanbul","Europe/Istanbul 🇹🇷 Turkey")
        timezone=timezone.replace("America/Port_of_Spain","America/Port of Spain 🇹🇹 Trinidad and Tobago")
        timezone=timezone.replace("Pacific/Funafuti","Pacific/Funafuti 🇹🇻 Tuvalu")
        timezone=timezone.replace("Asia/Taipei","Asia/Taipei 🇹🇼 Taiwan")
        timezone=timezone.replace("Africa/Dar_es_Salaam","Africa/Dar es Salaam 🇹🇿 Tanzania")
        timezone=timezone.replace("Europe/Kiev","Europe/Kiev 🇺🇦 Ukraine")
        timezone=timezone.replace("Europe/Uzhgorod","Europe/Uzhgorod 🇺🇦 Ukraine")
        timezone=timezone.replace("Europe/Zaporozhye","Europe/Zaporozhye 🇺🇦 Ukraine")
        timezone=timezone.replace("Europe/Simferopol","Europe/Simferopol 🇺🇦 Ukraine")
        timezone=timezone.replace("Africa/Kampala","Africa/Kampala 🇺🇬 Uganda")
        timezone=timezone.replace("Pacific/Johnston","Pacific/Johnston 🇺🇸 USA")
        timezone=timezone.replace("Pacific/Midway","Pacific/Midway 🇺🇸 USA")
        timezone=timezone.replace("Pacific/Wake","Pacific/Wake")
        timezone=timezone.replace("America/New_York","America/New York 🇺🇸 USA")
        timezone=timezone.replace("America/Detroit","America/Detroit 🇺🇸 USA")
        timezone=timezone.replace("America/Kentucky/Louisville","America/Kentucky/Louisville 🇺🇸 USA")
        timezone=timezone.replace("America/Kentucky/Monticello","America/Kentucky/Monticello 🇺🇸 USA")
        timezone=timezone.replace("America/Indiana/Indianapolis","America/Indiana/Indianapolis 🇺🇸 USA")
        timezone=timezone.replace("America/Indiana/Vincennes","America/Indiana/Vincennes 🇺🇸 USA")
        timezone=timezone.replace("America/Indiana/Winamac","America/Indiana/Winamac 🇺🇸 USA")
        timezone=timezone.replace("America/Indiana/Marengo","America/Indiana/Marengo 🇺🇸 USA")
        timezone=timezone.replace("America/Indiana/Petersburg","America/Indiana/Petersburg 🇺🇸 USA")
        timezone=timezone.replace("America/Indiana/Vevay","America/Indiana/Vevay 🇺🇸 USA")
        timezone=timezone.replace("America/Chicago","America/Chicago 🇺🇸 USA")
        timezone=timezone.replace("America/Indiana/Tell_City","America/Indiana/Tell City 🇺🇸 USA")
        timezone=timezone.replace("America/Indiana/Knox","America/Indiana/Knox 🇺🇸 USA")
        timezone=timezone.replace("America/Menominee","America/Menominee 🇺🇸 USA")
        timezone=timezone.replace("America/North_Dakota/Center","America/North Dakota/Center 🇺🇸 USA")
        timezone=timezone.replace("America/North_Dakota/New_Salem","America/North Dakota/New Salem 🇺🇸 USA")
        timezone=timezone.replace("America/North_Dakota/Beulah","America/North Dakota/Beulah 🇺🇸 USA")
        timezone=timezone.replace("America/Denver","America/Denver 🇺🇸 USA")
        timezone=timezone.replace("America/Boise","America/Boise 🇺🇸 USA")
        timezone=timezone.replace("America/Shiprock","America/Shiprock 🇺🇸 USA")
        timezone=timezone.replace("America/Phoenix","America/Phoenix 🇺🇸 USA")
        timezone=timezone.replace("America/Los_Angeles","America/Los Angeles 🇺🇸 USA")
        timezone=timezone.replace("America/Anchorage","America/Anchorage 🇺🇸 USA")
        timezone=timezone.replace("America/Juneau","America/Juneau 🇺🇸 USA")
        timezone=timezone.replace("America/Sitka","America/Sitka 🇺🇸 USA")
        timezone=timezone.replace("America/Yakutat","America/Yakutat 🇺🇸 USA")
        timezone=timezone.replace("America/Nome","America/Nome 🇺🇸 USA")
        timezone=timezone.replace("America/Adak","America/Adak 🇺🇸 USA")
        timezone=timezone.replace("America/Metlakatla","America/Metlakatla 🇺🇸 USA")
        timezone=timezone.replace("Pacific/Honolulu","Pacific/Honolulu 🇺🇸 USA")
        timezone=timezone.replace("America/Montevideo","America/Montevideo 🇺🇾 Uruguay")
        timezone=timezone.replace("Asia/Samarkand","Asia/Samarkand 🇺🇿 Uzbekistan")
        timezone=timezone.replace("Asia/Tashkent","Asia/Tashkent 🇺🇿 Uzbekistan")
        timezone=timezone.replace("Europe/Vatican","Europe/Vatican City State 🇻🇦") 
        timezone=timezone.replace("America/St_Vincent","America/Saint Vincent and the Grenadines 🇻🇨")
        timezone=timezone.replace("America/Caracas","America/Caracas 🇻🇪 Venezuela")
        timezone=timezone.replace("America/Tortola","America/Tortola 🇻🇬 British Virgin Islands")
        timezone=timezone.replace("America/St_Thomas","America/Saint Thomas 🇻🇮 US Virgin Islands")
        timezone=timezone.replace("Asia/Ho_Chi_Minh","Asia/Ho Chi Minh 🇻🇳 Vietnam")
        timezone=timezone.replace("Pacific/Efate","Pacific/Efate 🇻🇺 Vanuatu")
        timezone=timezone.replace("Pacific/Wallis","Pacific/Wallis and Futuna 🇼🇫")
        timezone=timezone.replace("Pacific/Apia","Pacific/Apia 🇼🇸 Samoa")
        timezone=timezone.replace("Asia/Aden","Asia/Aden 🇾🇪 Yemen")
        timezone=timezone.replace("Indian/Mayotte","Indian/Mayotte 🇾🇹")
        timezone=timezone.replace("Africa/Johannesburg","Africa/Johannesburg 🇿🇦 South Africa")
        timezone=timezone.replace("Africa/Lusaka","Africa/Lusaka 🇿🇲 Zambia")
        timezone=timezone.replace("Africa/Harare","Africa/Harare 🇿🇼 Zimbabwe")
        timezone=timezone.replace("_"," ")
        timezone=timezone.replace('"}}',"")
        form=veri.split('output_formats":')[1]
        form=form.split(']}')[0]
        form=form.replace("[","")
        form=form.replace('"',"")
        form=form.replace(",","⋆")
        realm=veri.split('url":')[1]
        realm=realm.split(',')[0]
        realm=realm.replace('"',"")
        port=veri.split('port":')[1]
        port=port.split(',')[0]
        port=port.replace('"',"")
        user=veri.split('username":')[1]
        user=user.split(',')[0]
        user=user.replace('"',"")
        passw=veri.split('password":')[1]
        passw=passw.split(',')[0]
        passw=passw.replace('"',"")
        message=veri.split('message":"')[1].split(',')[0].replace('"','')
        message=str(message.encode('utf-8').decode("unicode-escape")).replace('\/','/')
        if message=="":
            message="『 Iᴘᴛᴠ Fᴏʀ Fʀᴇᴇ! 』"
        created=veri.split('created_at":')[1]
        created=created.split(',')[0]
        created=created.replace('"',"")
        bitis=veri.split('exp_date":')[1]
        bitis=bitis.split(',')[0]
        bitis=bitis.replace('"',"")
        if bitis=="null":
               bitis="『 🤴ᴜɴʟɪᴍɪᴛᴇᴅ🤴 』"
        else:
               bitis=(datetime.datetime.fromtimestamp(int(bitis)).strftime('%d %B %Y %H:%M'))
        bitis=bitis
        if created=="null":
               created="『 🤴ᴜɴʟɪᴍɪᴛᴇᴅ🤴 』"
        else:
               created=(datetime.datetime.fromtimestamp(int(created)).strftime('%d %B %Y %H:%M'))
        created=created
        url5=""
        url5=f"https://ipleak.net/json/{host}"
        while True:
            try:
                ses= requests.Session()
                res = ses.get(url5, timeout=15, verify=False)
                break
            except:
                bag1= 0
                bag1=bag1+1
                time.sleep(1)
                if bag1==4:
                    break
        try:
            bag1=0
            servreg=""
            sname=""
            sip=""
            veri=str(res.text)
            if not 'title' in veri:
                sip=veri.split('ip": "')[1]
                sip=sip.split('"')[0]
                sname=veri.split('"isp_name": "')[1]
                sname=sname.split('"')[0]
                country_name=veri.split('country_name": "')[1]
                country_name=str((country_name.split('"')[0]).encode('utf-8').decode("unicode-escape"))
                scountry=veri.split('country_code": "')[1]
                scountry=scountry.split('"')[0]    
        except:
            pass

        try:
            kategori="«⋆👺⋆» NO INFO «⋆👺⋆»"
            res = ses.get(katelink,headers=HEADERd, timeout=1, verify=False)
            veri=""
            kate=""
            veri=str(res.text)
            for i in veri.split('category_name":"'):
                kate=kate+" «⋆👺⋆» "+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
                kate=kate.replace("||  «⋆👺⋆»","|| «⋆👺⋆»")
                kate=kate.upper()
            kategori=kate
            kategori=kategori.replace("[{","")
            kategori=kategori.replace("«⭐️»«⭐️»","")
            kategori=kategori.replace("★●•","")
            kategori=kategori.replace("●•★","")
        except:
            pass

        kanalsayisi=""
        filmsayisi=""
        dizisayisi=""
        url5=f"{full_url}/player_api.php?username={user}&password={pas}&action=get_live_streams"
        try:
            kanalsayisi=""
            res = ses.get(url5,timeout=3, verify=False)
            veri=str(res.text)
            kanalsayisi=str(veri.count("stream_id"))
            
            url5=f"{full_url}/player_api.php?username={user}&password={pas}&action=get_vod_streams"
            filmsayisi=""
            res = ses.get(url5,timeout=3, verify=False)
            veri=str(res.text)
            filmsayisi=str(veri.count("stream_id"))
            
            url5=f"{full_url}/player_api.php?username={user}&password={pas}&action=get_series"
            dizisayisi=""
            res = ses.get(url5,timeout=3, verify=False)
            veri=str(res.text)
            dizisayisi=str(veri.count("series_id"))
             
        except:pass

        m3ulink=full_url + "/get.php?username=" + user + "&password=" + pas + "&type=m3u_plus"
        epglink=full_url + "/xmltv.php?username=" + user + "&password=" + pas + "&type=xml_plus"
        realm3ulink="http://" + realm + port + "/get.php?username=" + user + "&password=" + pas + "&type=m3u_plus"

        mt=("""

┏╾╼✬🤴 𝕎𝕋𝔽√ᵐ3ᵘCʜᴇᴄᴋ 🤴✬╾╼㋡
┣╾╌╼『✬𝒮𝒸𝓇𝒾𝓅𝓉 𝒷𝔂 𝒫𝓊𝓈𝒽ℯ𝓀𝒶✬』╾╌╼
┣╾╌╼『✬𝙼𝙾𝙳 👺 𝙵𝙰𝚆𝙺𝙴𝚂✬』╾╌╼
┣┳≻✮SᴄᴀɴWɪᴛʜ➢『 """+my_os+""" 』
╿┣━━╾╌ ╌╼━━➢『 """+str(my_cpu)+""" 』
╎┗━━╾╌ ╌╼━━➢『 """+my_py+""" 』
┣━━━━━━━━━━━━━━━━━━━━━━━╾️
┣≻✮Hᴏsᴛ➢ """+full_url+"""
┣≻✮Rᴇᴀʟ➢ http://"""+realm+""":"""+port+"""
┣≻✮Pᴏʀᴛ➢ """+port+"""
┣≻✮Cʀᴇᴀᴛᴇᴅ➢ """+created+"""
┣≻✮Exᴘɪʀᴇs➢ """+bitis+"""
┣━━━━━━━━━━━━━━━━━━━━━━━╾️
┣━╾╌╼» 𝑿𝑻𝑹𝑬𝑨𝑴 🍀 𝑰𝑵𝑭𝑶 «╾╌╼━
┣≻✮Usᴇʀ➢ """+user+"""
┣≻✮Pᴀss➢ """+pas+"""
┣≻✮Tʀɪᴀʟ➢ """+trial+"""
┣≻✮Sᴛᴀᴛᴜs ➢ """+status+"""
┣≻✮Cᴏɴɴ➢ ᴍᴀx‣ """+mcon+""" / ᴀᴄᴛ‣ """+acon+"""
┣≻✮TɪᴍᴇZᴏɴᴇ➢ """+timezone+"""
┣≻✮Mᴇssᴀɢᴇ➢ """+message+""" 
┣━━━━━━━━━━━━━━━━━━━━━━━╾️
┣━╾╌╼» 𝑺𝑬𝑹𝑽𝑬𝑹 👀 𝑰𝑵𝑭𝑶 «╾╌╼━
┣≻✮Cᴏᴜɴᴛʀʏ➢ """+ str(country_name) + ' ✮ ' + data_server(str(scountry)) +"""
┣≻✮Sᴇʀᴠᴇʀ Iᴘ➢ » """+ str(sip) +""" «
┣≻✮Sᴇʀᴠᴇʀ Nᴀᴍᴇ➢ """+ str(sname) +"""
┣━━━━━━━━━━━━━━━━━━━━━━━╾️""")
            
        sayi=("""
┣━╾╌╼️» 𝑴𝑬𝑫𝑰𝑨 🍀 𝑪𝑶𝑼𝑵𝑻 «╾╌╼━
┣≻✮📺➢『 """+kanalsayisi+""" 』Cʜᴀɴɴᴇʟs
┣≻✮🎞️➢『 """+filmsayisi+""" 』Vᴏᴅ
┣≻✮🍿➢『 """+dizisayisi+""" 』Sᴇʀɪᴇs
┣━━━━━━━━━━━━━━━━━━━━━━━╾️""")


        imzak=("""
┏━╾╌╌╼️» 𝑴𝑬𝑫𝑰𝑨 🍀 𝑳𝑰𝑺𝑻 «╾╌╌╼━
┣≻✮📺➢『 ☟ ℂℍ𝔸ℕℕ𝔼𝕃𝕊 ☟ 』
┣➢ || """+str(kategori)+""" «⋆👺⋆» || """)


        mtl=("""
┣━╾╌╼️» 𝒎3𝒖 🍀 𝑳𝑰𝑵𝑲 «╾╌╼━
┣≻✮Fᴏʀᴍᴀᴛs➢『 """+form+""" 』
┣≻✮Hᴏsᴛ M𝟹ᴜ➢ """+m3ulink+"""
┣≻✮Rᴇᴀʟ M𝟹ᴜ➢ """+realm3ulink+"""
┣≻✮Eᴘɢ Lɪɴᴋ➢ """+epglink+"""
┣━━━━━━━━━━━━━━━━━━━━━━━╾️""")
        mtl1=("""
┣━━━━━━━━━━━━━━━━━━━━━━━╾️
┣━╾╌╌╼━ Sƈαɳ 🕒 Tιɱҽ ━╾╌╌╼━㋡
┣≻✮📆Dᴀᴛᴇ➢ """+str(time.strftime('%A %d %B %Y'))+"""    
┣≻✮⏰Tɪᴍᴇ➢ """+str(time.strftime('%H:%M'))+"""  
╿
┣━╾╼━﹝﹝ "𝕎𝕋𝔽 √ᵐ3ᵘ Check" ﹞﹞
┣━╾╌╼ ﹝﹝⇙⇕⇘Cʜᴇᴄᴋ Bʏ⇙⇕⇘﹞﹞
┣━╾╌╌╼━ ﹝﹝ 👺𝙵𝙰𝚆𝙺𝙴𝚂 ﹞﹞
┣╾╼﹝﹝ t.me/+aj2gqqMbXrtlZTdk ﹞﹞
┣━╾╼🏴‍☠️✬ ᴘʏᴛʜᴏɴ ᴘʏ ᴄᴏɴꜰɪɢ ✬🏴‍☠️╾╼
┗╾╼✬[𝒎3𝒖𝑪𝒉𝒆𝒄𝒌 𝑷𝒚 𝑺𝒄𝒓𝒊𝒑𝒕]✬╾╼㋡
""")            
        yaz=str(mt+sayi+mtl+imzak+mtl1+'\n\n')
        yaz1=str(mt+sayi+mtl+mtl1+'\n\n')

from urllib.parse import urlparse, parse_qs

def check_m3u_file(file_path):
    global host
    Active = 0
    NoActivec = 0
    Error = 0
    Totalc = 0
    urls = []  # Инициализирайте празен списък за урл-овете
    with open(file_path, 'r') as file:
        for line in file:
            urls.append(line.strip())  # Добавете всеки урл към списъка

    Totalc = len(urls)  # Пребройте броя на урл-овете в списъка
    cls()
    print(Pusheka)
    print(f" \33[1;93;30mTotal m3u count:\33[0m {Totalc}")
    
    for index, url in enumerate(urls):  # Промененият цикъл с enumerate
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        full_url = parsed_url.scheme + "://" + parsed_url.netloc
        host = parsed_url.hostname
        user = query_params['username'][0]
        pas = query_params['password'][0]
        link = f"{full_url}/player_api.php?username={user}&password={pas}&type=m3u"
        try:
            res = ses.get(link, headers=HEADERd, timeout=3, verify=False)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    Active += 1
                    check(veri, user, pas, full_url, host)
                    save1(str(yaz1))
                else:
                    NoActivec += 1
                print(f'\r \33[1;32mCHECK processed:\33[0m {Totalc}/{index + 1}', end='', flush=True)
            else:
                Error += 1
                print(f'\r \33[1;32mCHECK processed:\33[0m {Totalc}/{index + 1}', end='', flush=True)
        except Exception as e:
            Error += 1
            print(f'\r \33[1;32mCHECK processed:\33[0m {Totalc}/{index + 1}', end='', flush=True)
    
    print("\r Done processing all URLs")
    print(f" \33[1;32mActive count:\33[0m {Active}")
    print(f" \33[1;33mNoActive count:\33[0m {NoActivec}")
    print(f" \33[1;31mNot working m3u count:\33[0m {Error}")
    print("\n File saved in /Hits/👺𝕎𝕋𝔽√ᵐ3ᵘCheck/")
    print("\n\n Press Enter to exit")
    input()

def main():
    choice = input("\n\33[1;93;30m Select a scan option! \33[0m\n\n    1 ➢ for single m3u Check\n    2 ➢ for file with m3u Check \n\n\33[1;32m Select ➢ \33[0m ")
    cls()
    print(Pusheka)
    if choice == "1":
        global host
        user=""
        pas=""
        full_url=""
        url = input(" \n\33[1;93;30m Input a working m3u playlist! \n\n\33[1;32m Playlist ➢ \33[0m ")
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        full_url = parsed_url.scheme + "://" + parsed_url.netloc
        host = parsed_url.hostname
        user = query_params['username'][0]
        pas = query_params['password'][0]
        
        link=f"{full_url}/player_api.php?username={user}&password={pas}&type=m3u"
        bag1=0
        veri=""
        while True:
            try:
                res = ses.get(link,headers=HEADERd, timeout=3, verify=False)
                break
            except:
                time.sleep(1)
        
        veri=str(res.text)
        if 'username' in veri:
             
            status=veri.split('status":')[1]
            status=status.split(',')[0]
            status=status.replace('"',"")
            if status=='Active':
                print('\n         \33[1;42m     *** ACTIVE ***     \33[0m')
                check(veri,user,pas,full_url,host)
                print(yaz)
                r = input("\33[92m Wanna save the result in a file? Y/N \33[0m")
                if r == "Y" or r == "y":
                    save(str(yaz))
                    print("\n File saved in ➢ /Hits/👺𝕎𝕋𝔽√ᵐ3ᵘCheck/")
                    print("\n\33[91m Press Enter to exit  \33[0m")
                    input()
                else:
                    print("\n 👺 Bye Bye! ")
                    input()
            else:
                print('    \33[1;43m     *** NOACTIVE ***     \33[0m')
    elif choice == "2":
        folder_path = check_os() + "Hits/👺𝕎𝕋𝔽√ᵐ3ᵘCheck/"
        file_names = os.listdir(folder_path)
        for i, file in enumerate(file_names):
            print(f"{i+1}. {file}")
        file_choice = int(input("\n Select a file!\n\n\33[92m Option ➢ \33[0m "))
        selected_file = os.path.join(folder_path, file_names[file_choice-1])
        check_m3u_file(selected_file)
    else:
        print("\n Invalid selection")

if __name__ == "__main__":
    main()

