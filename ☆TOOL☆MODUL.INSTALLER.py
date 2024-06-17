import os,pip
pip.main(['install','colorama'])
pip.main(['install','pystyle'])
pip.main(['install','termcolor'])
pip.main(['install','requests'])
pip.main(['install','playsound'])
pip.main(['install','user_agent'])
pip.main(['install','fake_useragent'])
pip.main(['install','cloudscraper'])
pip.main(['install','print'])
pip.main(['install','names'])
pip.main(['install','socks'])
pip.main(['install','useragents'])
pip.main(['install','bs4'])
pip.main(['install','pyshorteners'])
pip.main(['install', 'requests[socks]'] )
pip.main(['install', 'sock'] )
pip.main(['install', 'socks'] )
pip.main(['install', 'PySocks'] )
pip.main(['install', 'tkinter'] )
try:
    import colorama    
except:
    pip.main(['install', 'colorama'] )
import colorama	
try:
	import pyshorteners	
except:	
	pip.main(['install', 'pyshorteners'] )
	import pyshorteners
	
	pip.main(['install', 'termcolor'] )

try:
     import threading   
except:
     pip.main(['install', 'threading'] ) 
     import threading