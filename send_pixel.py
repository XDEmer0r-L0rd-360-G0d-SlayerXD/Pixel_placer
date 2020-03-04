import requests
import json
import time


def get_requests():
    global tr_cord, bl_cord, color_id
    all_data = []
    for a in range(tr_cord[0], bl_cord[0] + 1):
        for b in range(tr_cord[1], bl_cord[1] + 1):
            changed = {"cn": 0, "x": a, "y": b, "clr": color_id, "token": None}
            all_data.append(changed)
    return all_data


def main():
    print(get_requests())
    # ses = requests.session()
    header = {'Host': 'pixelplanet.fun',
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
              "Accept": "*/*",
              "Accept-Language": "en-US,en;q=0.5",
              "Accept-Encoding": "gzip, deflate, br",
              "Referer": "https://pixelplanet.fun/",
              "Content-Type": "application/json",
              "Origin": "https://pixelplanet.fun",
              "Content-Length": "50",
              "Connection": "keep-alive",
              'Cookie': "__cfduid=d20cf0dfd3544064b38fe17dfcc052f7b1554679407; pixelplanet.session=s%3AaqATkVdgw8M1ARwUOLYQon1lvbDskaBU.Jels0pZiwOtNP4S6odF1E9BrTmOVmv4wK7kwLODDhn4"}
    # ses.get(url=url, cookies=cookies)
    for a in get_requests():
        r = requests.post(url=url, json=a, headers=header)
        j = json.loads(r.content)
        print(j)
        if j["waitSeconds"] < 45 and j['success'] is True:
            print('again')
            time.sleep(1)
            continue
        print(a)
        time.sleep(9)


if __name__ == '__main__':
    # ensure get_requests for loop ends right
    tr_cord, bl_cord = (1744, -10535), (1758, -10528)
    color_id = 7
    url = 'https://pixelplanet.fun/api/pixel'
    main()
