# uncompyle6 version 3.9.1
# Python bytecode version base 3.6 (3379)
# Decompiled from: Python 3.7.17 (default, Sep  8 2023, 11:57:51) 
# [Clang 14.0.7 (https://android.googlesource.com/toolchain/llvm-project 4c603efb
# Embedded file name: ToxicNoob
import requests, os

def download_m3u(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("playlist.m3u", "wb") as f:
            f.write(response.content)
        return True
    else:
        print("Falha ao baixar a lista m3u.")
        return False


def extract_channels(m3u_content):
    channels = []
    for line in m3u_content.splitlines():
        if line.startswith("#EXTINF"):
            info = line.strip()
            channels.append(info)

    return channels


def extract_movies(m3u_content):
    movies = []
    for line in m3u_content.splitlines():
        if line.startswith("#EXTINF") and "movie" in line.lower():
            info = line.strip()
            movies.append(info)

    return movies


def extract_series(m3u_content):
    series = []
    for line in m3u_content.splitlines():
        if line.startswith("#EXTINF") and "series" in line.lower():
            info = line.strip()
            series.append(info)

    return series


def extract_all(m3u_content):
    channels = extract_channels(m3u_content)
    movies = extract_movies(m3u_content)
    series = extract_series(m3u_content)
    return (channels, movies, series)


def save_to_file(data, filename):
    with open(filename, "w") as f:
        for item in data:
            f.write("%s\n" % item)


if __name__ == "__main__":
    m3u_url = input("Digite o link da lista m3u: ")
    if download_m3u(m3u_url):
        with open("playlist.m3u", "r") as f:
            m3u_content = f.read()
        option = input("Escolha uma opção:\n1 - Extrair canais de TV\n2 - Extrair lista de filmes\n3 - Extrair lista de séries\n4 - Extrair todas as opções separadamente\n")
        if option == "1":
            channels = extract_channels(m3u_content)
            output_file = input("Digite o nome do arquivo para salvar os canais de TV: ")
            save_to_file(channels, output_file)
            print("Canais de TV extraídos com sucesso!")
        elif option == "2":
            movies = extract_movies(m3u_content)
            output_file = input("Digite o nome do arquivo para salvar a lista de filmes: ")
            save_to_file(movies, output_file)
            print("Lista de filmes extraída com sucesso!")
        elif option == "3":
            series = extract_series(m3u_content)
            output_file = input("Digite o nome do arquivo para salvar a lista de séries: ")
            save_to_file(series, output_file)
            print("Lista de séries extraída com sucesso!")
        elif option == "4":
            channels, movies, series = extract_all(m3u_content)
            channels_file = input("Digite o nome do arquivo para salvar os canais de TV: ")
            save_to_file(channels, channels_file)
            movies_file = input("Digite o nome do arquivo para salvar a lista de filmes: ")
            save_to_file(movies, movies_file)
            series_file = input("Digite o nome do arquivo para salvar a lista de séries: ")
            save_to_file(series, series_file)
            print("Todas as opções extraídas com sucesso!")
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("Falha ao baixar a lista m3u. Certifique-se de que o link está correto e tente novamente.")

# okay decompiling Separados_De_ListaV1.0@Doisderj_enc_decoded.pyc
