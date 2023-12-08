import requests

def main():
    def get_ip():
        url = 'https://api.ipify.org'
        resl = requests.get(url)
        ip_add = resl.text
        return ip_add

    ip = get_ip()
    print(f'IP ADDRESS is {ip}')

run = int(input("To Run Press anything || To Exit press 0 or o"))
