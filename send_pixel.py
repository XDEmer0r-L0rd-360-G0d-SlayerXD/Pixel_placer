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
    # if cookie is None:
    #     cookie = {"__cfduid": "d20cf0dfd3544064b38fe17dfcc052f7b1554679407", "pixelplanet.session": "s:aqATkVdgw8M1ARwUOLYQon1lvbDskaBU.Jels0pZiwOtNP4S6odF1E9BrTmOVmv4wK7kwLODDhn4"}

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
    with open('help.txt', 'w') as f:
        f.write('''
If you see this, then you at most, you have downloaded requests and lxml for python, and these files from github with my updater.
This program will draw all pixel in a rectangle as a single color.
due to a lack of checking, it will draw a pixel the same color successfully and get the time use for it
Currently the only way to control it is via command line arguments
-cords "(trx, try)" "(blx, bly)" where tr is top right and bl is bottom left
-id color_id
-cookie "{'__cfduid': 'random', 'pixelplanet.session': 'random'}" it needs this format, just replace the randoms with the cookie data found in the header of the post request. Each word needs to be in quotes, and the whole object wraped in double quotes.
all needed data can be found in a post request that sends a pixel.
idk for chrome, but in firefox > f12 > network I can click on a pixel post request, and in parameters is color_id as cr(?). It also has cordinates, but they can be seen on screen where you hover.

Examples:
python Start_me.py -cords "(-15322, -13138)" "(-15317, -13134)" -id 7
will try to draw the black rectangle with no login
        ''')
    os.system('notepad.exe help.txt')
    pass


def main():
    execute_requests(cookie)


if __name__ == '__main__':
    # ensure get_requests for loop ends right
    tr_cord, bl_cord = (1764, -10534), (1768, -10531)
    color_id = 12
    url = 'https://pixelplanet.fun/api/pixel'
    args = sys.argv
    cookie = None
    # can now take arguments from command line
    for num_a, a in enumerate(args):
        if a == '-h' or a == 'help' or a == '-help':
            print("""use -cords "(trx, try)" "(blx, bly)" -id color_id -cookie "{'__cfduid': 'random', 'pixelplanet.session': 'random'}" """)
            print('Help not added yet, ask It#4001')
            show_help()
            exit()
        elif a == '-version':
            # todo update this
            print('v1.01')
            exit()
        elif a == '-cords':
            tr_cord = eval(args[num_a + 1])
            bl_cord = eval(args[num_a + 2])
        elif a == '-id':
            color_id = int(args[num_a + 1])
        elif a == '-url':
            url = args[num_a + 1]
        elif a == '-cookies' or a == '-c':
            cookie = args[num_a + 1]
    main()
    print('done with cords.')
