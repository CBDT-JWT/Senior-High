from time import sleep
import pygame
from pygame.locals import *
import random
from tkinter import Tk
from tkinter.messagebox import showerror,showinfo
from tkinter.filedialog import askopenfilename
from tkinter import Button,Label,Entry,Frame

# 初始化
pygame.init()
pygame.font.init()
# 帧速率
FPS=300
fps_clock=pygame.time.Clock()
# 颜色
BLACK     = (  0,  0,  0)
WHITE     = (255,255,255)
RED       = (255,  0,  0)
GREEN     = (  0,128,  0)
BLUE      = (  0,  0,255)
GRAY      = (128,128,128)
DARK_GRAY = ( 48, 48, 48)
LIME      = (  0,255,  0)
PURPLE    = (128,  0,128)
TEAL      = (  0,128,128)
YELLOW    = (255,255,  0)
# 字体
FONT = pygame.font.SysFont('SimHei', 40)
LITTLE_FONT = pygame.font.SysFont('SimHei', 30)
VERY_LITTLE_FONT = pygame.font.SysFont('SimHei', 20)