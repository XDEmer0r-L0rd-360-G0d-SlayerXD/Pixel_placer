import requests
import json
import time
import sys
import os


def generate_requests_data() -> list:
    """
    Generates usable json instructions based on criteria
    :rtype: list
    :return: list of instructions
    """
    global tr_cord, bl_cord, color_id
    all_data = []
    for a in range(tr_cord[0], bl_cord[0] + 1):
        for b in range(tr_cord[1], bl_cord[1] + 1):
            changed = {"cn": 0, "x": a, "y": b, "clr": color_id, "token": None}
            all_data.append(changed)
    return all_data


def execute_requests(cookie=None):
    """
    Sends requests click requests to pixelplanet
    :param cookie: user data, currently set to me for debugging
    :return: None
    """
    if cookie is None:
        cookie = {"__cfduid": "d20cf0dfd3544064b38fe17dfcc052f7b1554679407", "pixelplanet.session": "s:aqATkVdgw8M1ARwUOLYQon1lvbDskaBU.Jels0pZiwOtNP4S6odF1E9BrTmOVmv4wK7kwLODDhn4"}

    global url

    for a in generate_requests_data():
        # goes through each request and sends it and wait based on response
        r = requests.post(url=url, json=a, cookies=cookie)
        j = json.loads(r.content)
        print(a)
        print(j)
        try:
            if j["waitSeconds"] < 45 and j['success'] is True:
                print('again')
                time.sleep(1)
                continue
        except KeyError:
            print('need to fix captcha issue by manually placing a pixel.')
            input('[enter to resume]>')
        print('delay')
        time.sleep(9)


def show_help():
    pass



def main():
    execute_requests()


if __name__ == '__main__':
    # ensure get_requests for loop ends right
    tr_cord, bl_cord = (1764, -10534), (1768, -10531)
    color_id = 12
    url = 'https://pixelplanet.fun/api/pixel'
    args = sys.argv
    # can now take arguments from command line
    for num_a, a in enumerate(args[1:]):
        if a == '-h' or a == 'help' or a == '-help':
            show_help()
        elif a == '-cords':
            tr_cord = eval(args[num_a + 1])
            bl_cord = eval(args[num_a + 2])
        elif a == '-id':
            color_id = int(args[num_a + 1])
    main()
    print('done with cords.')
