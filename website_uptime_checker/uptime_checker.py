import requests

def check_site(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            print(f"{url} is UP")
        else:
            print(f"{url} is DOWN")
    except:
        print(f"{url} is DOWN")

check_site("https://www.google.com")
check_site("https://www.nonexistentwebsite.xyz")
