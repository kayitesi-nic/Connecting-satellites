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
    global total_time 
    screen.blit("bg", (0,0))

    num=1
    for satellite in satellites:
        screen.draw.text(str(num),(satellite.pos[0], satellite.pos[1]+20))
        satellite.draw()
    for line in lines:
        screen.draw.line(line[0], line[1], color=(255,255,255))
    if next_satellite < number_of_satellites:
        total_time= time() - start_time
        screen.draw.text(str(round(total_time,2)),(10,10),fontsize=30,)
    else:
        screen.draw.text(str(round(total_time,2)),(10,10),fontsize=30)

def on_mouse_down(pos):
    global lines, next_satellite
    if next_satellite < number_of_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append(satellites[next_satellite-1].pos,satellites[next_satellite].pos)

pgzrun.go()

