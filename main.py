# Setup

import pygame
import pygame.gfxdraw
pygame.init()
import math
import random
import time
import ui
import copy
from functools import partial

from configparser import ConfigParser

config = ConfigParser()

fullscreen = False
paused = False


def set_paused(val):
    global paused
    paused = val

"""
# parse existing file
config.read('2D Universe Sandbox.ini')

# read values from a section
fps = config.getint('engine', 'fps')
tickrate = config.getint('engine', 'tickrate')
scale = config.getint('engine', 'scale')
trail_update_rate = config.getint('engine', 'trail_update_rate')
settings_preset = config.getint('engine', 'settings_preset')
# update existing value
"""


default_width, default_height = 1280, 720
pc_width, pc_height = 1530, 780
width, height = default_width, default_height
speed = 1000
fps = 60
settings_preset = ""

aalines = False


tickrate = 30
scale = 5
trail_update_rate = 30
trail_length = 150
enable_trails = True
aa_trails = True
background_color = (0, 0, 0)
follow = True
draw_shine = True
aa_bodies = True
dist_before_deletion = 250000
info_panel = True
gravity = 1000
user_body_speed = 5

font = 'arial'
font_width = int(width/100+1)

dialogue_font = pygame.font.SysFont(font, font_width)

list_sorting_rate = 10
time_ = time.time()
Physics_time = 0
Trails_time = 0
Total_time = 0
Buttons_time = 0
Metrics_time = 0
trail_draw_time = 0
list_sorting_time = 0
drawing_bodies_time = 0
panel_rank = 0
#Space Dust (Random Bodies)
enable_space_dust = True
space_dust_amount = 500
space_dust_x_variation = 800
space_dust_y_variation = 800
space_dust_x_speed_variation = 300
space_dust_y_speed_variation = 300
space_dust_min_radius = 1
space_dust_max_radius = 10
mass_before_exploding = 1500
EXPLOSION_FRAGMENT_COUNT = 25
EXPLOSION_POSITION_RANGE = 7
EXPLOSION_MOMENTUM_RANGE = .005

bottom_panel = True
bottom_panel_type = 1



battery_saver = False





# parse existing file

read_from_file = True

if read_from_file:
    config.read('2D Universe Sandbox.ini')

    fps = config.getint('engine', 'fps')
    tickrate = config.getint('engine', 'tickrate')
    scale = config.getint('engine', 'scale')
    trail_update_rate = config.getint('engine', 'trail_update_rate')
    trail_length = config.getint('engine', 'trail_length')
    settings_preset = config.getint('engine', 'settings_preset')
    enable_trails = config.getboolean('engine', 'enable_trails')
    enable_grid = config.getboolean('engine', 'enable_grid')
    draw_shine = config.getboolean('engine', 'draw_shine')
    dist_before_deletion = config.getint('engine', 'dist_before_deletion')
    gravity = config.getint('engine', 'gravity')
    speed = config.getint('engine', 'speed')
    
    enable_space_dust = config.getboolean('spaceDust','enable_space_dust')
    space_dust_amount = config.getint('spaceDust', 'space_dust_amount')
    space_dust_x_variation = config.getint('spaceDust', 'space_dust_x_variation')
    space_dust_y_variation = config.getint('spaceDust', 'space_dust_y_variation')
    space_dust_x_speed_variation = config.getint('spaceDust', 'space_dust_x_speed_variation')
    space_dust_y_speed_variation = config.getint('spaceDust', 'space_dust_y_speed_variation')
    space_dust_min_radius = config.getint('spaceDust', 'space_dust_min_radius')
    space_dust_max_radius = config.getint('spaceDust', 'space_dust_min_radius')

    bottom_panel_type = config.getint('engine', 'bottom_panel_type')
    # update existing value

"""
if (settings_preset == 1):
    enable_trails = False
    list_sorting_rate = 3
    fps = 30
    tickrate = 30
    draw_shine = False

   
if (settings_preset == 2):
    trail_update_rate = 15
    trail_length = int(trail_update_rate/2)
    list_sorting_rate = 3
    fps = 60
    tickrate = 30
    draw_shine = True

   
if (settings_preset == 3):
    trail_update_rate = 30
    trail_length = int(trail_update_rate/2)
    list_sorting_rate = 5
    fps = 60
    tickrate = 60
    draw_shine = True

   
if (settings_preset == 4):
    trail_update_rate = 60
    trail_length = int(trail_update_rate/2)
    list_sorting_rate = 10
    fps = 120
    tickrate = 60
    draw_shine = True
   
   
if (settings_preset == 5):
    trail_update_rate = 120
    trail_length = int(trail_update_rate/2)
    list_sorting_rate = 15
    fps = 240
    tickrate = 120
    draw_shine = True

   
if (settings_preset == 6):
    enable_trails = False
    fps = 240
    tickrate = 240
    list_sorting_rate = 30

"""

if space_dust_min_radius <= 0:
    space_dust_min_radius = 1

if space_dust_max_radius < space_dust_min_radius:
    space_dust_max_radius = space_dust_min_radius

"""
if trail_update_rate > tickrate:
    trail_update_rate = tickrate
if trail_update_rate <= 0:
    trail_update_rate = int(tickrate/2)
if list_sorting_rate > tickrate:
    trail_update_rate = tickrate
"""
    
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

yellow = (255, 255, 0)
idk = (255, 0, 255)
idk2 = (0, 255, 255)


gray = (128, 128, 128)
dark_gray = (64, 64, 64)
light_gray = (192, 192, 192)
light_blue = (102, 178, 255)
dark_blue = (0, 0, 192)
blue = (64, 64, 225)
orange = (255,128,0)
light_orange = (255,192,72)
lighter_orange = (255,225,192)

red = (225, 64, 64)
pink = (255, 96, 96)
light_red = (255, 96, 96)

green = (64, 225, 64)
dark_green = (0, 192, 0)
light_green = (96, 255, 96)

yellow = (225, 225, 64)
light_yellow = (255, 255, 96)
dark_yellow = (192, 192, 0)

turquoise = (64, 192, 192)


bottom_panel = True

making_body_2 = False

display_update_time = 0

frames = 0
ticks = 0
camera_x, camera_y = width/2, height/2


body_id = 0

#temp
actual_fps = fps
sliders = []
buttons: list[ui.Button] = []

def refresh_positions():
    global paused
    global buttons
    global pause_button, reset_button, toggle_trails_button, save_button, load_button, new_sim_button, bottom_panel_close_button, bottom_panel_next_button, bottom_panel_open_button, info_panel_close_button, info_panel_open_button, toggle_grid_button, info_panel_delete_button, info_panel_zero_velocity_button, info_panel_explode_button, fancy_button, battery_saver_button
    global sliders
    global tickrate_slider, speed_slider, fps_slider
    global width, height
    global camera_x, camera_y 
    global add_panel_width, add_panel_height
    global add_panel_x, add_panel_y
    global info_panel_x, info_panel_y, info_panel_width, info_panel_height, info_panel_rect

    old_width, old_height = width, height
    width, height = pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height()

    camera_x, camera_y = width/2, height/2
    add_panel_width = width-width/8
    add_panel_height = height/5
    add_panel_x = width/16
    add_panel_y = height-add_panel_height
    panel_rect = (add_panel_x, add_panel_y, add_panel_width, add_panel_height)

    info_panel_width = width/8
    info_panel_height = height/2.5
    info_panel_x = width-info_panel_width
    info_panel_y = height/2-info_panel_height/2
    info_panel_rect = (info_panel_x, info_panel_y, info_panel_width, info_panel_height)
    

    if len(buttons) > 0:
        for button in buttons:
            x_mult = width/old_width
            y_mult = height/old_height
            new_rect = (button.x*x_mult, button.y*y_mult, button.width*x_mult, button.height*y_mult)
            button.set_dimensions(new_rect)
            # button.x *= width/old_width
            # button.width *= width/old_width
            # button.y *= height/old_height
            # button.height *= height/old_height
    else:
        buttons = []
        button_height = height/25
        pause_button = ui.Button(width-width/5, button_height*.2, width/20, button_height, "Pause")
        reset_button = ui.Button(width-width/5+width/20, button_height*.2, width/20, button_height, "Reset")
        toggle_trails_button = ui.Button(width-width/5, button_height*2.2, width/10, button_height, "Toggle Trails")
        toggle_grid_button = ui.Button(width-width/10, button_height*2.2, width/10, button_height, "Toggle Grid")
        save_button = ui.Button(width-width/5+width/10, button_height*.2, width/20, button_height, "Save")
        load_button = ui.Button(width-width/5+width/20+width/10, button_height*.2, width/20, button_height, "Load")
        new_sim_button = ui.Button(width-width/5, button_height*3.2, width/10, button_height, "New Sim")
        fancy_button = ui.Button(width-width/5, button_height*1.2, width/10, button_height, "just don't")
        battery_saver_button = ui.Button(width-width/10, button_height*1.2, width/10, button_height, "Battery Saver")


        bottom_panel_close_button = ui.Button(add_panel_x+add_panel_width-button_height, add_panel_y, button_height, button_height, "X")
        bottom_panel_next_button = ui.Button(add_panel_x+add_panel_width-button_height*4, add_panel_y, button_height*2.5, button_height, "Next")
        bottom_panel_open_button = ui.Button(add_panel_x+add_panel_width/2-button_height, height-button_height, button_height, button_height, "^")

        info_panel_close_button = ui.Button(width-button_height, info_panel_y, button_height, button_height, "X")
        info_panel_open_button = ui.Button(width-button_height, info_panel_y+info_panel_height/2, button_height, button_height, "<")
        info_panel_delete_button = ui.Button(info_panel_x, info_panel_y+info_panel_height/2, button_height*2.5, button_height, "Delete")
        info_panel_zero_velocity_button = ui.Button(info_panel_x, info_panel_y+info_panel_height/2+button_height, button_height*3.5, button_height, "Zero Velocity")
        info_panel_explode_button = ui.Button(info_panel_x, info_panel_y+info_panel_height/2+button_height*2, button_height*2.5, button_height, "Explode")

        buttons.append(pause_button)
        buttons.append(reset_button)
        buttons.append(toggle_trails_button)
        buttons.append(save_button)
        buttons.append(load_button)
        buttons.append(new_sim_button)
        buttons.append(bottom_panel_close_button)
        buttons.append(bottom_panel_next_button)
        buttons.append(info_panel_close_button)
        buttons.append(info_panel_open_button)
        buttons.append(bottom_panel_open_button)
        buttons.append(toggle_grid_button)
        buttons.append(info_panel_delete_button)
        buttons.append(info_panel_zero_velocity_button)
        buttons.append(info_panel_explode_button)
        buttons.append(fancy_button)
        buttons.append(battery_saver_button)

    
    if len(sliders) > 0:
        for slider in sliders:
            value = slider.get_value()
            slider.x *= width/old_width
            slider.width *= width/old_width
            slider.y *= height/old_height
            slider.height *= height/old_height
            slider.set_value(value)
    else:
        sliders = []
        slider_width = width/15*2
        slider_height = height/25*2

        tickrate_slider = ui.Slider(slider_width*2, 0, slider_width, slider_height, (10, 240), 10, "tickrate", 120)
        speed_slider = ui.Slider(slider_width, slider_height, slider_width, slider_height, (0.1, 5), 0.1, "speed", 1)
        fps_slider = ui.Slider(slider_width, 0, slider_width, slider_height, (10, 360), 10, "fps", 60)
        speed_slider.set_theme("blue")
        tickrate_slider.set_theme("red")
        fps_slider.slider_color = (64, 84, 196)
        fps_slider.slider_outline_color = (64, 84, 196)
        fps_slider.color = (32, 42, 98)
        fps_slider.border_color = (48, 64, 164)
        fps_slider.slide_color = (84, 96, 225)
        fps_slider.slide_color_dark = (64, 86, 164)
        fps_slider.set_theme("blue")
        sliders.append(tickrate_slider)
        sliders.append(speed_slider)
        sliders.append(fps_slider)

        for slider in sliders:
            slider.fancy = True
            slider.update_fancy()

    

def get_screen_pos(x, y, camera_x, camera_y,  scale):
    return ((x/scale-camera_x), (y/scale-camera_y))

def str_to_tuple(string):
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.replace(' ', '')
    string = string.split(',')
    for i in range(len(string)):
        string[i] = int(float(string[i]))
    return tuple(string)
    

def get_bodies_from_string(string):
    bodies = []
    string = string.split("!")
    for i in range(len(string)):
        string[i] = string[i].split("@")
        bodies.append(Body(float(string[i][0]), float(string[i][1]), float(string[i][2]), float(string[i][3]), float(string[i][4]), str_to_tuple(string[i][5]), string[i][6]))

    return bodies
            

class Body:
    def __init__(self, x, y, xspeed, yspeed, mass, color, name):
        global body_id
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.radius = ((mass*200)**(1/3))
        self.color = color
        self.mass = mass
        self.name = name
        self.last_pos_x = []
        self.last_pos_y = []
        self.id = body_id
        body_id += 1

    def __repr__(self):
        f = "@"
        return str(self.x) + f + str(self.y) + f + str(self.xspeed) + f + str(self.yspeed) + f + str(self.mass) + f + str(self.color) + f + str(self.name)


    def predict_pos(self, num_ticks, tickrate) -> list[tuple[float, float]]:
        positions = []
        x, y = self.x, self.y
        xspeed, yspeed = self.xspeed, self.yspeed
        bodies2 = copy.deepcopy(bodies)
        for _ in range(num_ticks):
            for body in bodies2:
                body_distance = math.sqrt(abs(x-body.x)**2+abs(y-body.y)**2)
                if body_distance == 0:
                    return positions

                

                angle = math.atan2(y - body.y, x - body.x)
                vector = pygame.math.Vector2(math.cos(angle), math.sin(angle))


                force = ((self.mass*body.mass)/body_distance**2)
                body_force_x = vector[0]*force*gravity
                body_force_y = vector[1]*force*gravity
                
                xspeed -= (body_force_x/self.mass)/(tickrate/speed)
                yspeed -= (body_force_y/self.mass)/(tickrate/speed)
            
                body.xspeed += (body_force_x/body.mass)/(tickrate/speed)
                body.yspeed += (body_force_y/body.mass)/(tickrate/speed)
                body.x += body.xspeed/tickrate*speed
                body.y += body.yspeed/tickrate*speed

                if body_distance < body.radius+self.radius:
                    return positions
                    
            x += xspeed/tickrate*speed
            y += yspeed/tickrate*speed
            positions.append((x, y))
        return positions



    def draw(self):
        if abs(self.x/scale+camera_x) < width+self.radius/scale and abs(self.y/scale+camera_y) < height+self.radius/scale:
            pygame.gfxdraw.filled_circle(window, int(self.x/scale+camera_x), int(self.y/scale+camera_y), int(self.radius/scale+.5), self.color)
            if aa_bodies:
                pygame.gfxdraw.aacircle(window, int(self.x/scale+camera_x), int(self.y/scale+camera_y), int(self.radius/scale+.5), (int(self.color[0]/1.5), int(self.color[1]/1.5), int(self.color[2]/1.5)))
            if draw_shine:
                pygame.draw.circle(window, white, (int(self.x/scale+camera_x), int(self.y/scale+camera_y)), int((self.radius*0.8)/scale+.5), int(self.radius/scale/5), draw_top_right=True)

    def draw_prediction(self, num_ticks, tickrate):
        predictionsRealCoords = self.predict_pos(num_ticks, tickrate)
        predictions = [(self.x/scale+camera_x, self.y/scale+camera_y)]
        for p in predictionsRealCoords:
            predictions.append((p[0]/scale+camera_x, p[1]/scale+camera_y))
        if len(predictions) > 1:
            pygame.draw.lines(window, self.color, False, predictions)


    def draw_at_coords(self):

        pygame.gfxdraw.filled_circle(window, int(self.x), int(self.y), int(self.radius+.5), self.color)
        if aa_bodies:
            pygame.gfxdraw.aacircle(window, int(self.x), int(self.y), int(self.radius+.5), self.color)
        if draw_shine:
            pygame.draw.circle(window, white, (int(self.x), int(self.y)), int((self.radius*0.8)+.5), int(self.radius/5), draw_top_right=True)
    def move(self):
        self.x += self.xspeed/tickrate
        self.y += self.yspeed/tickrate
    def draw_trail(self):

        trail_fade_mode = True
        trail_fade_begin = 1 # should be >= 1, larger value = trails begin to fade closer to the end


        while len(self.last_pos_x) > trail_length:
            self.last_pos_x.pop(trail_length)
        while len(self.last_pos_y) > trail_length:
            self.last_pos_y.pop(trail_length)

       
        for i in range(len(self.last_pos_x)):
            if i == 0:
                x_dist = self.last_pos_x[i] - self.x
                y_dist = self.last_pos_y[i] - self.y
                points = [((self.x)/scale+camera_x,(self.y)/scale+camera_y)]
                if len(self.last_pos_x) < 3:
                    pygame.draw.line(window, self.color, ((((self.last_pos_x[i]))/scale)+camera_x,((self.last_pos_y[i])+0*(1))/scale+camera_y), ((self.x)/scale+camera_x,(self.y)/scale+camera_y), int((self.radius/(3*scale)+.5)))

            else:
                brightness = min((trail_length-i)/trail_length*trail_fade_begin, 1)
                color = (self.color[0]*brightness, self.color[1]*brightness, self.color[2]*brightness)
                x_dist = self.last_pos_x[i] - self.x
                y_dist = self.last_pos_y[i] - self.y
                points.append(((((self.last_pos_x[i]))/scale)+camera_x,((self.last_pos_y[i])+0*(1))/scale+camera_y))
                if len(self.last_pos_x) < 3 or trail_fade_mode:
                    pygame.draw.line(window, color, ((((self.last_pos_x[i]))/scale)+camera_x,((self.last_pos_y[i])+0*(1))/scale+camera_y), ((self.last_pos_x[i-1])/scale+camera_x,(self.last_pos_y[i-1])/scale+camera_y), int((self.radius/(3*scale))+1))
        # if len(self.last_pos_x) > 2:
        #     if aalines:
        #         pygame.draw.aalines(window, self.color, False, points, int((self.radius/(3*scale))+1))
        #     else:
        #         pygame.draw.lines(window, self.color, False, points, int((self.radius/(3*scale))+1))
    def consume(self, consumed):
        if self.mass >= mass_before_exploding and consumed.mass >= mass_before_exploding:
            self.explode(int(EXPLOSION_FRAGMENT_COUNT*math.sqrt(self.mass/1500)))
            consumed.explode(int(EXPLOSION_FRAGMENT_COUNT*math.sqrt(consumed.mass/1500)))
            return
            
        combined_mass = self.mass+consumed.mass
        if combined_mass == 0:
            combined_mass = -0.000000001

        self_percentage = round(self.mass/combined_mass, 5)
        other_percentage = 1-self_percentage
        red = (self.color[0]*self_percentage)+(consumed.color[0]*other_percentage)
        green = (self.color[1]*self_percentage)+(consumed.color[1]*other_percentage)
        blue = (self.color[2]*self_percentage)+(consumed.color[2]*other_percentage)
        self.color = (red, green, blue)

        self.radius = math.pow((self.radius**3+consumed.radius**3), 1/3)
        self.xspeed = ((self.xspeed*self.mass)+(consumed.xspeed*consumed.mass))/combined_mass
        self.yspeed = ((self.yspeed*self.mass)+(consumed.yspeed*consumed.mass))/combined_mass
        self.x = ((self.x*self.mass)+(consumed.x*consumed.mass))/combined_mass
        self.y = ((self.y*self.mass)+(consumed.y*consumed.mass))/combined_mass
        self.mass += consumed.mass



        for i in range(len(bodies)):
            if bodies[i].id == consumed.id:
                bodies_to_delete.add(consumed.id)
                break

    def collide(self, num_bodies):
        pass     
               

    def distance_to(self, other):
        return math.sqrt(abs(self.x-other.x)**2+abs(self.y-other.y)**2)

    


    def explode(self, num_bodies):
        global bodies
        global bodies_to_delete
        #num_bodies = int(num_bodies*math.sqrt(self.mass/1500))
        mass_to_go = self.mass/1.1
        bodies_to_go = num_bodies
        bodies_to_delete.add(self.id)
        for i in range(num_bodies):
            currentMass = mass_to_go/bodies_to_go
            currentX = self.x+random.randint(-int(self.radius*EXPLOSION_POSITION_RANGE), int(self.radius*EXPLOSION_POSITION_RANGE))
            currentY = self.y+random.randint(-int(self.radius*EXPLOSION_POSITION_RANGE), int(self.radius*EXPLOSION_POSITION_RANGE))
            currentXspeed = self.xspeed + random.randint(int(-EXPLOSION_MOMENTUM_RANGE*self.mass), int(EXPLOSION_MOMENTUM_RANGE*self.mass))
            currentYspeed = self.yspeed + random.randint(int(-EXPLOSION_MOMENTUM_RANGE*self.mass), int(EXPLOSION_MOMENTUM_RANGE*self.mass))
            bodies.append(Body(currentX, currentY, currentXspeed, currentYspeed, currentMass, self.color, self.name+" fragment " + str(i)))
            bodies_to_go -= 1
            mass_to_go -= currentMass

def calc_center_of_mass(bodies):
    center_x = 0
    center_y = 0
    weight = 0
    for body_ in bodies:
        center_x += body_.x*body_.mass
        center_y += body_.y*body_.mass
        weight += body_.mass
    return (center_x/weight, center_y/weight)


def print_time_used(time_name, time, used_time, total_time):
    print("Time used for " + time_name + ": " + str(int(time*10000)/10000))
    print("Percent of used time" + ": " + str(int(time*10000/used_time)/100) + "%")
    print("Percent of total time" + ": " + str(int(time*10000/total_time)/100) + "%")

saved_system = [Body(width/2, height/2, 0, 0, 1000, (220, 220, 20), "Sun"),
                Body(width/2, height/2-100, 30, 0, 1, light_gray, "Mercury"),
                Body(width/2, height/2-250, 20, 0, 4, orange, "Venus"),
                Body(width/2, height/2-500, 15, 0, 5, blue, "Earth"),
                Body(width/2, height/2-900, 11, 0, 3, light_orange, "Mars"),
                Body(width/2, height/2-2000, 7, 0, 25, lighter_orange, "Jupiter"),
                Body(width/2, height/2-5000, 4.8, 0, 12, lighter_orange, "Saturn"),
                Body(width/2, height/2-8000, 4, 0, 8, light_blue, "Uranus"),
                Body(width/2, height/2-10000, 3.6, 0, 9, dark_blue, "Neptune"),               
                ]

bodies = copy.deepcopy(saved_system)
display_bodies = []

if enable_space_dust:
    for i in range(space_dust_amount):
        space_dust_x = width/2+random.randint(-space_dust_x_variation, space_dust_x_variation)
        space_dust_y = height/2-random.randint(-space_dust_y_variation, space_dust_y_variation)
        space_dust_xspeed = random.randint(-space_dust_x_speed_variation, space_dust_x_speed_variation)
        space_dust_yspeed = random.randint(-space_dust_y_speed_variation, space_dust_y_speed_variation)
        space_dust_mass = random.randint(1, 100)
        bodies.append(Body(space_dust_x, space_dust_y, space_dust_xspeed, space_dust_yspeed, space_dust_mass, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), "Space dust"+str(i)))



def all_pair(items, func, data):
    global Physics_time
    global Trails_time
    global trail_draw_time
    global ticks
    global bodies
    global bodies_to_delete
    gravity_start = time.time()
    if tickrate > fps or frames % int(fps/tickrate) == 0:
        for i in range(0, len(items)):
            for j in range(i+1, len(items)):
                func(items[i], items[j])
            items[i].x += items[i].xspeed/(tickrate/speed)
            items[i].y += items[i].yspeed/(tickrate/speed)
        ticks += 1
    Physics_time += time.time()-gravity_start
    if enable_trails and ticks % int(tickrate/min(tickrate,trail_update_rate)) == 0:
        do_trails()
    bodies = [body for body in bodies if body.id not in bodies_to_delete]
    bodies_to_delete = set()

def do_trails():
    global trail_draw_time
    global Trails_time
    trail_start = time.time()
    for i in range(0, len(bodies)):
        currentbody = bodies[i]
        currentbody.last_pos_x.insert(0, currentbody.x)
        currentbody.last_pos_y.insert(0, currentbody.y)
        trail_draw_start = time.time()
        

        trail_draw_time += time.time()-trail_draw_start
        if abs(currentbody.x - bodies[0].x) > dist_before_deletion or abs(currentbody.y - bodies[0].y) > dist_before_deletion:
            bodies_to_delete.add(currentbody.id)

    Trails_time += time.time()-trail_start


       
def apply_gravity(body_a, body_b):
    if body_a.id == body_b.id:
        body_b.id += 99999999999
        print("WARNING: bodies have same id, fix now")
    body_distance = body_a.distance_to(body_b)
    if body_distance == 0:
        print("WARN: DIVISION BY 0 in apply_gravity (body_distance = 0) (at " + str(time.time()-time_) + " seconds)")
        body_distance = 0.001

    

    angle = math.atan2(body_a.y - body_b.y, body_a.x - body_b.x)
    vector = pygame.math.Vector2(math.cos(angle), math.sin(angle))


    force = ((body_a.mass*body_b.mass)/body_distance**2)
    body_force_x = vector[0]*force*gravity
    body_force_y = vector[1]*force*gravity
    
    body_a.xspeed -= (body_force_x/body_a.mass)/(tickrate/speed)
    body_a.yspeed -= (body_force_y/body_a.mass)/(tickrate/speed)
   
    body_b.xspeed += (body_force_x/body_b.mass)/(tickrate/speed)
    body_b.yspeed += (body_force_y/body_b.mass)/(tickrate/speed)
    

    if body_distance < body_b.radius+body_a.radius:
       
        if body_a.mass >= body_b.mass:
            body_a.consume(body_b)
           
        else:
            body_b.consume(body_a)
           
def bodies_draw(items):
    
    for body in items:
        body.draw()


def move_all(items, x, y, move_grid=True):
    global camera_x
    global camera_y
    global grid_offset_x
    global grid_offset_y
    
    for body in items:
        body.x += x
        body.y += y
        for i in range(len(body.last_pos_x)):
            body.last_pos_x[i] += x
           
        for i in range(len(body.last_pos_y)):
            body.last_pos_y[i] += y
    if move_grid:
        grid_offset_x += x/scale
        grid_offset_y += y/scale
    
    #camera_x -= x
    #camera_y -= y

def make_info_panel(body):
    global info_panel_width
    global info_panel_height
    global info_panel_x
    global info_panel_y
    global info_panel_rect
    global panel_rank
    pygame.draw.rect(window, dark_gray, info_panel_rect)
        
    dialogue = dialogue_font.render("Name: " + body.name, True, white)
    window.blit(dialogue, (width-info_panel_width+font_width/2, height/2-(info_panel_height/2-font_width)))
    
    dialogue = dialogue_font.render("Radius: " + str(int(body.radius+.5)), True, white)
    window.blit(dialogue, (width-info_panel_width+font_width/2, height/2-(info_panel_height/2-font_width*2.5)))
    
    dialogue = dialogue_font.render("Mass: " + str(int(body.mass+.5)), True, white)
    window.blit(dialogue, (width-info_panel_width+font_width/2, height/2-(info_panel_height/2-font_width*4)))

    dialogue = dialogue_font.render("Coordinates: " + str(int(body.x+.5)) + ", " + str(int(body.y+.5)), True, white)
    window.blit(dialogue, (width-info_panel_width+font_width/2, height/2-(info_panel_height/2-font_width*5.5)))
    
    dialogue = dialogue_font.render("Speed: " + str(int(body.xspeed+.5)) + ", " + str(-int(body.yspeed+.5)), True, white)
    window.blit(dialogue, (width-info_panel_width+font_width/2, height/2-(info_panel_height/2-font_width*7)))
    for i in range(len(bodies)):
        panel_rank = 0

        if bodies[i].id == body.id:
            panel_rank = i
            break
    dialogue = dialogue_font.render("Size Rank: " + str(panel_rank+1) + "/" + str(len(bodies)), True, white)
    window.blit(dialogue, (width-info_panel_width+font_width/2, height/2-(info_panel_height/2-font_width*8.5)))

add_panel_width = width-width/8
add_panel_height = height/5
add_panel_x = width/16
add_panel_y = height-add_panel_height

grid_offset_x = 0
grid_offset_y = 0

def draw_grid():
    
    global grid_offset_x
    global grid_offset_y
    dist_between = (max(width, height)/10)/scale
    lines = scale*10

    #If too many lines, divide number of lines by 2
    while lines > 20:
        lines /= 2
        dist_between *= 2
        lines = int(lines)

    #If too little lines, multiply number of lines by 2
    while lines < 10:
        lines *= 2
        dist_between /= 2

    lines = int(lines+1)

    #If the grid is offset more than half the distance between lines, move exactly one line in a seamless manner to keep the grid visible



    while grid_offset_x > dist_between/2:
        grid_offset_x -= dist_between

    while grid_offset_x < -dist_between/2:
        grid_offset_x += dist_between

    while grid_offset_y > dist_between/2:
        grid_offset_y -= dist_between

    while grid_offset_y < -dist_between/2:
        grid_offset_y += dist_between

    
    for i in range(lines):
        pygame.draw.line(window, gray, (0, i*(dist_between)+grid_offset_y), (width, i*(dist_between)+grid_offset_y))
    for i in range(lines):
        pygame.draw.line(window, gray, (i*(dist_between)+grid_offset_x, 0), (i*(dist_between)+grid_offset_x, height))

def display_bodies_on_panel(panel_rect, display_bodies):
    if len(display_bodies) > 0:
        add_panel_x, add_panel_y, add_panel_width, add_panel_height = panel_rect
        #Make displayed bodies sizes relative to size of biggest displayed body
        bigrad = display_bodies[0].radius

        for thing in display_bodies:
            if isinstance(thing.radius, complex):
                thing.radius = thing.radius.real
            thing.radius /= bigrad/(add_panel_height/3)
            
        for i in range(len(display_bodies)):
            display_body = display_bodies[i]

            #Spread out bodies evenly on panel, then draw them
            display_body.x = (add_panel_x+(i/len(display_bodies))*(add_panel_width))+add_panel_width/len(display_bodies)/2
            display_body.y = (height-add_panel_height/2)
            display_body.draw_at_coords()
            
            dialogue = dialogue_font.render(display_body.name, True, white)
            dialogue_rect = dialogue.get_rect(center=(display_body.x, display_body.y-(display_body.radius)-font_width))
            window.blit(dialogue, dialogue_rect)

            dialogue = dialogue_font.render(str(int(display_body.mass+.5)), True, white)
            dialogue_rect = dialogue.get_rect(center=(display_body.x, display_body.y+(display_body.radius)+font_width))
            window.blit(dialogue, dialogue_rect)

def make_bottom_panel(display_bodies, bottom_panel_type):
    panel_rect = (add_panel_x, add_panel_y, add_panel_width, add_panel_height)
    pygame.draw.rect(window, dark_gray, panel_rect)

    
    if bottom_panel_type == 1:
        display_bodies_on_panel(panel_rect, display_bodies)
        
            

    elif bottom_panel_type == 2:
        display_bodies_on_panel(panel_rect, display_bodies)
        
def tick_buttons():
    global saved_system
    global bodies
    global paused
    global speed
    global enable_trails
    global enable_grid
    global tickrate
    global bottom_panel_type
    global bottom_panel
    global info_panel
    global panel_body
    global bodies
    global follow
    global aalines
    global battery_saver
    global trail_update_rate
    global trail_length
    global aa_bodies
    global draw_shine
    for button in buttons:
        button.draw(window)
        if button.tick():
            if button == pause_button:
                paused = not paused
            elif button == reset_button:
                bodies = copy.deepcopy(saved_system)
            elif button == toggle_trails_button:
                enable_trails = not enable_trails
                for thing in bodies:
                    thing.last_pos_x = []
                    thing.last_pos_y = []

            elif button == save_button:
                saved_system = copy.deepcopy(bodies)
                for i in range(len(saved_system)):
                    saved_system[i] = repr(saved_system[i])
                saved_system = '!'.join(saved_system)

                
                config['local systems'] = {}
                config['local systems']['system'] = saved_system
                with open('saved_systems.ini', 'w') as configfile:
                    config.write(configfile)
                print("Saved System")

            elif button == load_button:
                config.read('saved_systems.ini')
                saved_system = get_bodies_from_string(config.get(('local systems'), ('system')))
                bodies = copy.deepcopy(saved_system)
                print("Loaded System")

            elif button == new_sim_button:
                bodies = []
            
            elif button == bottom_panel_close_button:
                bottom_panel = False

            elif button == bottom_panel_next_button:
                bottom_panel_type += 1
                if bottom_panel_type > 2:
                    bottom_panel_type = 1

            elif button == bottom_panel_open_button:
                bottom_panel = True

            elif button == info_panel_close_button:
                info_panel = False

            elif button == info_panel_open_button:
                info_panel = True

            elif button == toggle_grid_button:
                enable_grid = not enable_grid

            elif button == info_panel_delete_button:
                if panel_body in bodies:
                    bodies.remove(panel_body)
            elif button == info_panel_zero_velocity_button:
                panel_body.xspeed = 0
                panel_body.yspeed = 0

            elif button == info_panel_explode_button:
                panel_body.explode(15)
                follow = False

            elif button == fancy_button:
                aalines = not aalines

            elif button == battery_saver_button:
                battery_saver = not battery_saver
                if battery_saver:
                    for slider in sliders:
                        #slider.fancy = False
                        #slider.text2 = str(slider.get_value())
                        slider.set_fancy(False)
                    trail_update_rate = 30
                    trail_length = 60
                    aa_bodies = False
                    draw_shine = False
                    #fps_slider.set_value(30)

                if not battery_saver:
                    for slider in sliders:
                        #slider.fancy = True
                        #slider.text2 = str(slider.get_value())
                        #slider.update_fancy()
                        slider.set_fancy(True)
                    aa_bodies = True
                    draw_shine = True
                    trail_update_rate = 60
                    trail_length = 360
                    
                    
                

            else:
                print("Unknown button (at " + str(time.time()-time_) + " seconds)")
    for slider in sliders:
        global fps
        global actual_fps
        slider.draw(window)
        slider.tick(events)
        if slider == tickrate_slider:
            tickrate = speed/20*slider.get_value()
            slider.text2 = tickrate
        elif slider == speed_slider:
            speed = slider.get_value()*20
        elif slider == fps_slider:
            actual_fps = slider.get_value()
    

pygame.mouse.set_visible(True)
window = pygame.display.set_mode([width, height], pygame.RESIZABLE, vsync=1)
pygame.display.set_caption('Gravity Sim 2D')




clock = pygame.time.Clock()
#move_all(bodies, -width/2, -height/2)
panel_body = Body(width/2, height/2-250, 30, 0, 10, blue, "noonebetterusethisnameorproblemswilloccur")
if len(bodies) > 0:
    panel_body = bodies[0]
#last_mouse_pos_x, last_mouse_pos_y = pygame.mouse.get_pos()
if panel_rank > len(bodies) - 1:
    panel_rank = 0

if len(bodies) > 0:
    center_x, center_y = calc_center_of_mass([bodies[panel_rank]])

selected_body = Body(width/2, height/2-250, 30, 0, 10, blue, "User made " + str(random.randint(0, 100000000)))
making_body = False
playing = True
start = time.time()-1
refresh_positions()
#sliders = []
#buttons = []
def copy_depth_2(src):
    dst = []
    for item in src:
        dst.append(copy.copy(item))

    return dst

def mouse_over_anything():
    for button in buttons:
        if button.mouse_over():
            return True
    for slider in sliders:
        if slider.mouse_over():
            return True
        if slider.moving:
            return True
    return False


ticks = 0
bodies_to_delete = set()


    	
def disp_metrics():
    dialogue = dialogue_font.render("FPS: " + str(fps_), True, white)
    dialogue_rect = dialogue.get_rect()
    window.blit(dialogue, dialogue_rect)
    dialogue = dialogue_font.render("Bodies: " + str(len(bodies)), True, white)
    window.blit(dialogue, (0, height/40))
    dialogue = dialogue_font.render("Speed: " + str(speed/20), True, white)
    window.blit(dialogue, (0, height/40*2))
    dialogue = dialogue_font.render("Tickrate: " + str(tickrate), True, white)
    window.blit(dialogue, (0, height/40*3))

    total_mass = 0
    for thing in bodies:
        total_mass += thing.mass
    dialogue = dialogue_font.render("Total mass: " + str(round(total_mass, 3)), True, white)
    window.blit(dialogue, (0, height/40*4))
    dialogue = dialogue_font.render("Scale: " + str(round(scale, 3)), True, white)
    window.blit(dialogue, (0, height/40*5))
    dialogue = dialogue_font.render("Time used: " + str(round(percent_used, 1)) + "%", True, white)
    window.blit(dialogue, (0, height/40*6))


#The bodies that user can pick from the bottom panel
display_large_star = Body(0, 0, 0, 0, 2500, light_blue, "Large Star")
display_small_star = Body(0, 0, 0, 0, 500, yellow, "Small Star")
display_negative_mass_star = Body(0, 0, 0, 0, 501, yellow, "Negative Star")
display_negative_mass_star.mass = -501
display_negative_mass_star.radius = 50
display_very_large_planet = Body(0, 0, 0, 0, 50, dark_blue, "Very Large Planet")
display_large_planet = Body(0, 0, 0, 0, 20, blue, "Large Planet")
display_small_planet = Body(0, 0, 0, 0, 5, light_blue, "Small Planet")
display_large_asteroid = Body(0, 0, 0, 0, 1, gray, "Large Asteroid")
display_small_asteroid = Body(0, 0, 0, 0, .1, light_gray, "Small Asteroid")
last_time = time.time()-1

fps_ = fps
pretime = 1
posttime = 1
draw_names = False
while playing:
    action_this_frame = False

    #Only update fps counter every 5th of a second to increase readability
    
    if frames % int(fps/5) == 0:
        fps_ = int(1/((time.time()-last_time)/(fps/5))+.5)
        last_time = time.time()

        percent_used = pretime/posttime*100
        
    start_ = time.time()
    window.fill(background_color)
 


    

    list_sorting_start = time.time()


    bodies.sort(key=lambda x: x.mass, reverse=True)
    list_sorting_time += time.time()-list_sorting_start
    mouse_x_change, mouse_y_change = pygame.mouse.get_rel()
    #bodies_to_delete = set()

    
    if not paused:
        fps = actual_fps
        if tickrate > fps:

            for i in range(int(tickrate/fps)):
                if time.time()-start < 1/fps:
                    all_pair(bodies, apply_gravity, bodies_to_delete)
                    bodies = [body for body in bodies if body.id not in bodies_to_delete]

        else:
            all_pair(bodies, apply_gravity, bodies_to_delete)
            bodies = [body for body in bodies if body.id not in bodies_to_delete]
    else:
        1 == 1
        #fps = 10
        
    
    events = pygame.event.get()
    for event in events:

        
        action_this_frame = True
       
        if event.type == pygame.QUIT:
            playing = False
            break

        elif event.type == pygame.VIDEORESIZE:
            refresh_positions()
       
        if event.type == pygame.MOUSEWHEEL:
            old_scale = scale
            scale *= 1-event.y/20
            if scale <= 0.1:
                scale = 0.1
                # Not doing this lags the game for some reason (circles too big or smth)
       
               
            x,y = pygame.mouse.get_pos()
            if not follow:
                move_all(bodies, (x-width/2)*(scale-old_scale), (y-height/2)*(scale-old_scale), move_grid = False)

                grid_offset_x += (x)*(scale-old_scale)/scale
                grid_offset_y += (y)*(scale-old_scale)/scale
            else:
                grid_offset_x += (width/2)*(scale-old_scale)/scale
                grid_offset_y += (height/2)*(scale-old_scale)/scale

        #Check if user is clicking in an attempt to make a body
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and not mouse_over_anything():
            x,y = pygame.mouse.get_pos()
            """
            for currentbody in bodies:
                if abs(((currentbody.x/scale)+width/2)-x) < currentbody.radius/scale+5 and abs(((currentbody.y/scale)+height/2)-y) < currentbody.radius/scale+5:
                    if panel_body == currentbody:
                        panel = not panel
                    else:
                        panel = True
                    panel_body = currentbody
                    break"""
            if bottom_panel:
                

                if bottom_panel_type == 1:
                    if making_body:
                        
                        making_body = False
                        making_body_2 = True
                    else:
                        last_selected = selected_body
                        selected_new = False
                        for display_body in display_bodies:
                            if abs(display_body.x-x) < display_body.radius+5 and abs(display_body.y-y) < display_body.radius+5:
                                selected_body = Body((display_body.x)+width/2, (display_body.y)+width/2, 0, 0, display_body.mass, display_body.color, display_body.name)
                                if selected_body.mass < 0:
                                    selected_body.radius = 42
                                start_x = selected_body.x
                                start_y = selected_body.y
                                making_body = True
                                selected_new = True
                                break
                        if not selected_new:
                            x,y = pygame.mouse.get_pos()
                            selected_body = Body((x)+width/2, (y)+width/2, 0, 0, selected_body.mass, selected_body.color, selected_body.name)
                            if selected_body.mass < 0:
                                selected_body.radius = 42
                            start_x = selected_body.x
                            start_y = selected_body.y
                            making_body_2 = True
                            making_body = True
                                                        
                if bottom_panel_type == 2:
                    for clicked_body in display_bodies:
                        if abs(clicked_body.x-x) < clicked_body.radius+5 and abs(clicked_body.y-y) < clicked_body.radius+5:
        
                            for i in range(len(bodies)):
                                if bodies[i].id == clicked_body.id:
                                    panel_body = bodies[i]
                                    follow = True
                                    break
            

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing = False
                break
            
            if event.key == pygame.K_UP:
                info_panel = True
                panel_body = bodies[0]
                
            if event.key == pygame.K_DOWN:
                info_panel = True
                panel_body = bodies[len(bodies)-1]
                
            if event.key == pygame.K_RIGHT:
                if panel_rank+1 < len(bodies):
                    info_panel = True
                    panel_body = bodies[panel_rank+1]
                    
            if event.key == pygame.K_LEFT:
                if panel_rank-1 >= 0:
                    info_panel = True
                    panel_body = bodies[panel_rank-1]
                    
            if event.key == pygame.K_SPACE:
                follow = not follow
                
            if event.key == pygame.K_RETURN:
                if bottom_panel_type <= 2:
                    bottom_panel_type += 1
                else:
                    bottom_panel_type = 1
                    
            if event.key == pygame.K_TAB:
                x,y = pygame.mouse.get_pos()
                for currentbody in bodies:
                    if abs(((currentbody.x/scale)+width/2)-x) < currentbody.radius/scale+5 and abs(((currentbody.y/scale)+height/2)-y) < currentbody.radius/scale+5:
                        currentbody.explode(int(EXPLOSION_FRAGMENT_COUNT*math.sqrt(currentbody.mass/1500)))
                        break

            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                else:
                    window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                refresh_positions()
                    
    bodies = [body for body in bodies if body.id not in bodies_to_delete]
    
    for i in range(len(bodies)):
        

        if bodies[i].id == panel_body.id:
            panel_rank = i
             
            break
    
    if panel_rank > len(bodies) - 1:
        panel_rank = 0
    
        
    if bottom_panel:
        bottom_panel_close_button.enabled = True
        bottom_panel_next_button.enabled = True
        bottom_panel_open_button.enabled = False
            
        if bottom_panel_type == 1:
            if making_body:
                x,y = pygame.mouse.get_pos()
                selected_body.x = (x-width/2)*scale
                start_x = (x-width/2)*scale
                selected_body.y = (y-height/2)*scale
                start_y = (y-height/2)*scale
                selected_body.draw()
                

            if making_body_2:
                if pygame.mouse.get_pressed()[0]:
                    x,y = pygame.mouse.get_pos()
                    #selected_body.x = (x-width/2)*scale
                    #selected_body.y = (y-height/2)*scale
                    if making_body:
                        making_body = False

                    selected_body.xspeed = (start_x - (x-width/2)*scale)/30*user_body_speed
                    selected_body.yspeed = (start_y - (y-height/2)*scale)/30*user_body_speed
                    selected_body.draw()
                    selected_body.draw_prediction(int(tickrate*2), tickrate/4)

                else:
                    selected_body.draw()
                    bodies.append(selected_body)
                    making_body_2 = False
                    
        if bottom_panel_type == 2:
            for i in range(len(bodies)):
                panel_rank = 0

                if bodies[i].id == panel_body.id:
                    panel_rank = i
                    break
            
            if panel_rank > len(bodies) - 1:
                panel_rank = 0

    else:
        bottom_panel_close_button.enabled = False

        bottom_panel_next_button.enabled = False

        bottom_panel_open_button.enabled = True

    if len(bodies) > 0:
        center_x, center_y = calc_center_of_mass([bodies[panel_rank]])

        
        
    if pygame.mouse.get_pressed()[2] and not mouse_over_anything():
        if follow:
            follow = False
           
        move_all(bodies, mouse_x_change*scale, mouse_y_change*scale)


    
    if pygame.mouse.get_pressed()[1]:
        move_all(bodies, -center_x, -center_y)
    if panel_body not in bodies:
        follow = False
        if len(bodies) != 0:
            panel_body = bodies[0]

    if follow:
        if not bottom_panel:
            move_all(bodies, -center_x, -center_y)
        else:
            move_all(bodies, -center_x, -center_y-add_panel_height/2*scale)
   
    

    trail_draw_start = time.time()
    if enable_trails:
        for currentbody in bodies:
            currentbody.draw_trail()
    Trails_time += time.time() - trail_draw_start


    if enable_grid:
        draw_grid()



    drawing_bodies_start = time.time()
    bodies_draw(bodies)
    if draw_names:
        for currentbody in bodies:
            if int(currentbody.radius/scale) > 0:
                dialogue = dialogue_font.render(currentbody.name, True, white)
                dialogue_rect = dialogue.get_rect(center=(currentbody.x/scale+width/2, currentbody.y/scale+height/2-(currentbody.radius/(scale))-font_width))
                window.blit(dialogue, dialogue_rect)
    drawing_bodies_time += time.time()-drawing_bodies_start


    if bottom_panel:
        if bottom_panel_type == 1:
            display_bodies = []

            display_bodies.append(display_large_star)
            display_bodies.append(display_small_star)
            display_bodies.append(display_negative_mass_star)
            display_bodies.append(display_very_large_planet)
            display_bodies.append(display_large_planet)
            display_bodies.append(display_small_planet)
            display_bodies.append(display_large_asteroid)
            display_bodies.append(display_small_asteroid)
            make_bottom_panel(display_bodies, bottom_panel_type)

        if bottom_panel_type == 2:
            display_bodies = []
            i = 0
            for i in range(min(len(bodies), 8)):
                display_bodies.append(Body(0, 0, 0, 0, bodies[i].mass, bodies[i].color, bodies[i].name))
                display_bodies[i].id = bodies[i].id
            make_bottom_panel(display_bodies, bottom_panel_type)
            
    if panel_body not in bodies:
        follow = False
        if len(bodies) != 0:
            panel_body = bodies[0]
            

    if info_panel:
        make_info_panel(panel_body)
        info_panel_close_button.enabled = True
        info_panel_open_button.enabled = False
        info_panel_delete_button.enabled = True
        info_panel_zero_velocity_button.enabled = True
        info_panel_explode_button.enabled = True


    else:
        info_panel_close_button.enabled = False
        info_panel_open_button.enabled = True
        info_panel_delete_button.enabled = False
        info_panel_zero_velocity_button.enabled = False
        info_panel_explode_button.enabled = False
        
    if len(bodies) > 0:
        center_x, center_y = calc_center_of_mass([bodies[panel_rank]])

   
    start = time.time()

    disp_metrics()

    Metrics_time += time.time()-start

    if paused:
        pause_button.text = "START"
        if action_this_frame:
            fps = actual_fps
    else:
        pause_button.text = "PAUSE"

    start = time.time()
    tick_buttons()
    Buttons_time += time.time()-start
    
    #FIX
    #pygame.gfxdraw.aacircle(window, int(x_to_screen(panel_body.x)), int(y_to_screen(panel_body.y)), int(panel_body.radius/scale+1), (255, 255, 255))
    
    display_update_start = time.time()
    pygame.display.flip()
    display_update_time += time.time()-display_update_start
    Total_time += time.time()-start_
    pretime = time.time()-start_
    clock.tick(fps)
    frames += 1
    posttime = time.time()-start_
    fps_counter = time.time()-start
   
    #if frames % int(fps/list_sorting_rate) == 0:
    #    ticks += 1
   

print()
print()
print("---------------- Time Statistics ----------------")
print()
print("Time passed: " + str(time.time()-time_))
print("Time used for any computations: " + str(Total_time))
print()
print("Gravity Physics:")
print_time_used("physics", Physics_time, Total_time, time.time()-time_)
print()
print("Drawing Bodies:")
print_time_used("drawing bodies", drawing_bodies_time, Total_time, time.time()-time_)
print()
print("Trails:")
print_time_used("trails", Trails_time, Total_time, time.time()-time_)
print()
print("Display.flip():")
print_time_used("updating display", display_update_time, Total_time, time.time()-time_)
print()
print("Buttons:")
print_time_used("ticking buttons", display_update_time, Total_time, time.time()-time_)
print()
print("Metrics:")
print_time_used("blitting metrics", display_update_time, Total_time, time.time()-time_)
print()

pygame.quit()

