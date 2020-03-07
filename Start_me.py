import subprocess
import sys
import os
import importlib


def dl_from_link(url, file_name):
    import requests
    """
    Does as name implies.
    :param url: file source
    :param file_name: where to put it, and what to name it
    :return: None
    """
    print(f'dl: {file_name}')
    with open(file_name, 'wb') as f:
        f.write(requests.get(url).content)


def ensure_minimum():
    for a in to_import:
        try:
            importlib.import_module(a)
        except ModuleNotFoundError:
            print(f'need {a}')
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', a])
            try:
                importlib.import_module(a)
            except Exception:
                print(f'Cannot install {a}')
    importlib.invalidate_caches()


def main():
    given_args = sys.argv
    # dl updater
    if not os.path.isfile('Updater.py'):
        ensure_minimum()
        dl_from_link('https://github.com/XDEmer0r-L0rd-360-G0d-SlayerXD/Simple-Updater/releases/download/v1.0/Updater.py', 'Updater.py')
    # run updater with correct file & repo
    if '-su' not in given_args:
        # supress update = su
        os.system('python Updater.py -t send_pixel.py -r https://github.com/XDEmer0r-L0rd-360-G0d-SlayerXD/Pixel_placer/releases')
    run_pixel_command = 'python ' + ' '.join(given_args)
    print('executing', run_pixel_command)
    exit()
    os.system(run_pixel_command)
    pass


if __name__ == '__main__':
    to_import = ['requests', 'lxml']
    main()

