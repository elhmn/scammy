import requests
import json
import string
import random
import os
import time
import threading
from proxy import getProxyAddress


def gen_names():
    final_names = []
    with open("./names.txt", "r") as f:
        names = f.read().split("\n")
        for n in names:
            name = n.split("\t")
            for n2 in name:
                if not n2.isdigit() and len(n2) > 1:
                    final_names.append(n2)
    return final_names

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}

URL = "https://www.newregister.tk/REGISTER/member-login-control.php?callback=http://stalk.ztney.com/gerigetir.php"

emails = ["@gmail.com", "@hotmail.fr", "@yahoo.com", "@outlook.fr"]

data = {
    "username": "",
    "password": "",
    "csrftoken": "undefined"
}

chars = string.ascii_letters + string.digits
random.seed(os.urandom(1024))
count_requests = 0

def submitForm():
    global count_requests
    while True:
        ip_port = getProxyAddress()
        proxyDict = {"http":ip_port,"https":ip_port}
        username_extra = "".join(random.choice(string.digits) for i in range(random.randint(1, 4)))

        data["username"] = random.choice(gen_names()) + username_extra + random.choice(emails)
        data["password"] = "".join(random.choice(chars) for i in range(7))

        try:
            print(">payload : ", data)

            r = requests.post(URL, data, proxies=proxyDict)
            if r.status_code == 200:
                count_requests += 1
                print(">--------------------------------------------")
                print(">>>requests : ", count_requests)
                print(">--------------------------------------------")
            else:
                print(".", end="")
        except Exception as es:
            print(".", end="")

        time.sleep(0.7)


threads = []

def main():
    for i in range(500):
        t = threading.Thread(target=submitForm)
        t.daemon = True
        threads.append(t)

    for i in range(500):
        threads[i].start()

    for i in range(500):
        threads[i].join()


if __name__ == "__main__":
    main()

