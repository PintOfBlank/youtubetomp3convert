#!/usr/bin/env python3
import os
import platform
import subprocess

if platform.system() == "Darwin":
    m = subprocess.run("pip3", capture_output=True)
    m_use = bytes("Usage:", 'utf-8')

    if m_use in m.stdout:
        print("pip version valid.")
    else:
        z = subprocess.run("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
        b = subprocess.run("python3 get-pip.py")
        cnf = bytes("command not found")
        if cnf in b.stdout:
            f = subprocess.run("python get-pip.py")
    try:
        x = subprocess.run("pytube", capture_output=True)
    except ModuleNotFoundError:
        d = subprocess.run("pip3 install pytube", capture_output=True)
    endswith = ".mp4"
    url = input("ur youtube link: ")
    os.system("pytube {} -a".format(url))
    for i in os.listdir():
        if i.endswith(endswith):
            d = i
    q = d.split(".")
    my_mp3 = q[0] + ".mp3"
    os.rename(d, my_mp3)
else:
    print("Oops This Service Is Not Available For You OS Right Now.")
