import pgzrun
from random import randint
from time import time

WIDTH=600
HEIGHT=500

start_time=0
total_time=0
end_time=0

satellites= []
lines= []

next_satellite=0
number_of_satellites= 10

def create_satellites():
    global start_time
    for count in range(0,number_of_satellites):
        sat=Actor("sat")
        sat.pos= randint(40,WIDTH-40), randint(40,HEIGHT-40)
        satellites.append(sat)
    start_time= time()

def draw():
    screen.blit("bg", (0,0))

pgzrun.go()

