import requests

def download_proxies(proxy_type):
    headersx = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }

    proxy_urls = {
        1: [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=3000&country=all&ssl=all&anonymity=elite",
            "https://www.proxy-list.download/api/v1/get?type=http&anon=elite",
            "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com//sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt"
        ],
        2: [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=Socks4&timeout=10000&country=all&ssl=all&anonymity=elite",
            "https://www.proxy-list.download/api/v1/get?type=socks4&anon=elite",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
            "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://sunny9577.github.io/proxy-scraper/proxies.txt"
        ],
        3: [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=elite",
            "https://www.proxy-list.download/api/v1/get?type=socks5&anon=elite",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "https://raw.githubusercontent.com//sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
        ],
        4: [
            "https://proxy.webshare.io/api/v2/proxy/list/download/izoqfuwuhsdqpwnfuyaonhuhngfeufevwtigesao/-/any/username/direct/-/",
            "https://proxy.webshare.io/api/v2/proxy/list/download/izoqfuwuhsdqpwnfuyaonhuhngfeufevwtigesao/-/any/username/direct/-/",
            "https://proxy.webshare.io/api/v2/proxy/list/download/dameyfjcczsiznrnhbkkntqzrenufenyqzmkjoyv/-/any/username/direct/-/",
            "https://proxy.webshare.io/api/v2/proxy/list/download/itdrbsnpwmfwcofvmohvvtujreuiyezjgydhjmag/-/any/username/direct/-/",
            "https://proxy.webshare.io/api/v2/proxy/list/download/ypwlqxacnkfwrxjqhjhvpcleljhoilnitozyooot/-/any/username/direct/-/",
            "https://proxy.webshare.io/api/v2/proxy/list/download/sotesyengrreaylusnabcdepbscylpzdeelxhkpm/-/any/username/direct/-/",
            "https://proxy.webshare.io/api/v2/proxy/list/download/mqxneapkiyvjokxiietlgpprjlruyyjxjcdcmhgt/-/any/username/direct/-/",
            "https://proxy.webshare.io/api/v2/proxy/list/download/tcnjdortemliymfmzpsiernipbecovkiwiquaidn/-/any/username/direct/-/",
            "https://proxy.webshare.io/api/v2/proxy/list/download/amvtvqhdxlkvdqbkqtmbvxcbabfudubuancwltxx/-/any/username/direct/-/"
        ]
    }

    if proxy_type not in proxy_urls:
        print("Invalid proxy type. Choose from 1 (HTTP), 2 (SOCKS4), 3 (SOCKS5), 4 (WebShare).")
        return

    file_names = {
        1: "HTTP_proxies.txt",
        2: "SOCKS4_proxies.txt",
        3: "SOCKS5_proxies.txt",
        4: "WebShare_proxies.txt"
    }

    file_name = file_names[proxy_type]
    proxy_list = proxy_urls[proxy_type]
    proxies = ""

    for url in proxy_list:
        try:
            response = requests.get(url, headers=headersx)
            proxies += response.text + "\n"
        except requests.RequestException as e:
            print(f"Failed to download proxies from {url}: {e}")

    # Save proxies to file
    with open(file_name, "w", encoding="utf-8-sig") as file:
        file.write(proxies)
    print(f"Proxies saved to {file_name}.")

if __name__ == "__main__":
    print("Enter the number corresponding to the proxy type:")
    print("1: HTTP")
    print("2: SOCKS4")
    print("3: SOCKS5")
    print("4: WebShare")
    try:
        proxy_type = int(input("Enter your choice: ").strip())
        download_proxies(proxy_type)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
