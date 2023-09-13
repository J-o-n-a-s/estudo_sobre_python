'''
Crie um programa que abra e reproduza o áudio de um arquivo MP3.
'''

from pygame import event, init, mixex
init()
mixex.music.load('ex021.mp3')
event.wait()
