from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def whatsmess(name, message):
    startfile("D:\\WindowsApps\\5319275A.WhatsAppDesktop_2.2433.3.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
    sleep(5)
    click(x=238, y=140)
    sleep(1)
    write(name)
    sleep(1)
    click(x=157, y=207)
    sleep(1)
    click(x=829, y=987)
    sleep(1)
    write(message)
    sleep(1)
    press('enter')

def whatscall(name):
    startfile("D:\\WindowsApps\\5319275A.WhatsAppDesktop_2.2433.3.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
    sleep(5)
    click(x=238, y=140)
    sleep(1)
    write(name)
    sleep(1)
    click(x=1731, y=65)

def whatsvcall(name):
    startfile("D:\\WindowsApps\\5319275A.WhatsAppDesktop_2.2433.3.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
    sleep(5)
    click(x=238, y=140)
    sleep(1)
    write(name)
    sleep(1)
    click(x=1663, y=60)
