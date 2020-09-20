# Get the wallpaper from the internet
# Save it to temp directory
# Set the wallpaper
# Automate the calls to this script

import os
import requests
import wget
import subprocess, sys
import time

def get_wallpaper():
    access_key = os.environ.get('UNSPLASH_ACCESS_KEY')
    tmp = os.environ.get('TEMP')
    url = 'https://api.unsplash.com/photos/random/?client_id='+access_key
    params = {
        "query": "HD Wallpapers",
        "orientation": "landscape",
    }
    response = requests.get(url,params).json()
    image_url = response['urls']['full']
    wallpaper = wget.download(image_url, tmp)

    return wallpaper

def main():
    wallpaper = get_wallpaper()
    time.sleep(2)
    p = subprocess.Popen(["powershell.exe","Set-ItemProperty -path 'HKCU:\Control Panel\Desktop\' -name wallpaper -value " + wallpaper + '\n'
    "rundll32.exe user32.dll, UpdatePerUserSystemParameters"], stdout=sys.stdout)
    p.communicate()

if __name__ == '__main__':
    main()