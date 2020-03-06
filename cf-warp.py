import requests
import json
import datetime
import random
import string
from time import sleep

referrer = "71a51e19-f56d-40a1-b06d-7c29ae1515e4"
timesToLoop = 20
retryTimes = 5


def genString(stringLength):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


url = 'https://api.cloudflareclient.com/v0a745/reg'


def run():
    install_id = genString(11)
    body = {"key": "{}=".format(genString(42)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "locale": "zh-CN"}

    bodyString = json.dumps(body)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Host': 'api.cloudflareclient.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.1'
               }

    r = requests.post(url, data=bodyString, headers=headers)
    return r

s=0
#for i in range(timesToLoop):
while True:
    result = run()
    if result.status_code == 200:
        s+=1
        print(s,"OK")
    else:
        print("Error")
        for r in range(retryTimes):
            retry = run()
            sleep(20)
            if retry.status_code == 200:
                print("Retry #" + str(r + 1), "OK")
                s+=1
                break
            else:
                print("Retry #" + str(r + 1), "Error")
                if r == retryTimes - 1:
                    exit()
