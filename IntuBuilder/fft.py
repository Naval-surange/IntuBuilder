from pygame.event import clear
from help import FFT_help
from wiki import FFT_wiki 
import pygame, sys
import numpy as np
from utils import *
from functools import partial
from pygame import gfxdraw

import globals

# size = (globals.width, globals.height) = 640*2, 480



class Fourier_reconstructor:
	def load_curve(self,path):
		self.curve = np.loadtxt(path)
		return self.curve
	def rotate(self):
		x = -self.curve[:,1]
		y = self.curve[:,0]
		self.curve = np.column_stack((x,y))
		return self.curve
	def conv2img(self):
		self.zvals = self.curve[:,0] + 1j*self.curve[:,1]
	def fourier_coeff(self,m):    
		numPoints = self.zvals.shape[0]  
		tvals = np.linspace(0,1,numPoints+1)[1:]    
		c_m = 1.0/numPoints * np.sum(self.zvals * np.exp(-2*np.pi*1j*m*tvals))    
		return c_m
	def compute_Fourier_dict(self):
		self.fourier_dict = {}
		for m in range(-1*self.n_max,self.n_max+1):
			cm = self.fourier_coeff(m)
			self.fourier_dict[m] = cm
		return self.fourier_dict
	def reconstruct_Fourier_dict(self,n_max,num_points=100):
		self.n_max = n_max
		self.conv2img()
		self.compute_Fourier_dict()
		
		z_vals_rec = np.zeros(num_points, dtype = complex)
		tvals= np.linspace(0,1,num_points+1)[1:]
		for key in self.fourier_dict.keys():
			z_vals_rec += self.fourier_dict[key] * np.exp(2*np.pi*1j*key*tvals)
		return z_vals_rec


def drawCircle(screen,x,y):
	pygame.draw.circle(screen,(0,0,255),(x,y),5)

def draw_graph(win,display_board,x_values,y_values):
	globals.width,globals.height
	
	if len(x_values) == 0:
		return

	if len(x_values) != len(y_values):
		raise ValueError("list a and list b must have the same length")
	
	colide_array = []
	for index in range(len(x_values)):
		if display_board.collidepoint(int(x_values[index]),int(y_values[index])):
			colide_array.append(1)
		else:
			colide_array.append(0)
	
	for index in range(len(x_values)):
		if colide_array[index] and colide_array[(index+1)%len(x_values)]:
			pygame.draw.aaline(win,BLACK,(x_values[index],y_values[index]),(x_values[(index+1)%len(x_values)],y_values[(index+1)%len(x_values)]))
		if colide_array[index]:
			gfxdraw.aacircle(win,int(x_values[index]),int(y_values[index]),4,BLACK)
			gfxdraw.filled_circle(win,int(x_values[index]),int(y_values[index]),4,BLACK)



def draw_converted(win,data,numSlider):
	globals.width,globals.height
	if len(data) == 0:
		return
	display_board = pygame.draw.rect(win,GREY,[globals.width//2+30,80,globals.width//2-80,globals.height-150],border_radius=10)
	reconstructed = compress(data,numSlider)						
	draw_graph(win,display_board,abs(reconstructed.real)+globals.width//2,abs(reconstructed.imag))

def compress(data,numSlider):
	if len(data) == 0:
		return	
	np_data = np.array(data)
	re = Fourier_reconstructor()
	
	num_points = int(numSlider.val)
 
	
	re.curve = np_data
	re.rotate()
	re.rotate()
	reconstructed = re.reconstruct_Fourier_dict(20,num_points)
	
	return reconstructed
	

def clear(win,data):
	drawing_board = pygame.draw.rect(win,GREY,[30,80,globals.width//2-80,globals.height-150],border_radius=10)
	display_board = pygame.draw.rect(win,GREY,[globals.width//2+30,80,globals.width//2-80,globals.height-150],border_radius=10)
	data.clear()
 
def fft():
	pygame.init()

	win = pygame.display.set_mode(globals.size,pygame.RESIZABLE)
	pygame.display.set_caption("FFT")

	
	data= []
	isPressed = False
	running_fft = True
	first = True
	
	prev_size = (-1,-1)
	
	while running_fft:
		globals.size = (globals.width, globals.height)= win.get_size()
		
		draw_text(win,"Closed Curve Compression using FFT",pos=(globals.width//2,30,'center'),color=WHITE,font_size=35,bold=True)
		if prev_size != globals.size:
			data.clear()
			win.fill(MAIN_COL)
			numSlider = Slider(win,"Number of Points",100,10,400,pos=(globals.width//2,globals.height-60),box_size=(300,50))
			num_points = numSlider.val
			sliders = [numSlider]	
		
			button_1 = Button(win,"i",location=(50 ,globals.height-50 ),action=FFT_help,size=(40,30))
			button_2 = Button(win,"Convert",location=(globals.width//2-10 ,globals.height//2 ),action=partial(draw_converted,win,data,sliders[0]),size=(70,30))
			button_3 = Button(win,"wiki",location=(120 ,(globals.height-50) ),action=FFT_wiki,size=(80,30))
			button_4 = Button(win,"Clear",location=(globals.width - globals.width//4 ,(globals.height-30) ),action=partial(clear, win,data),size=(80,30))
			
			btns = [button_1,button_2,button_3,button_4]
			drawing_board = pygame.draw.rect(win,GREY,[30,80,globals.width//2-80,globals.height-150],border_radius=10)
			display_board = pygame.draw.rect(win,GREY,[globals.width//2+30,80,globals.width//2-80,globals.height-150],border_radius=10)

			prev_size = globals.size
		
  
		if first:
			drawing_board = pygame.draw.rect(win,GREY,[30,80,globals.width//2-80,globals.height-150],border_radius=10)
			display_board = pygame.draw.rect(win,GREY,[globals.width//2+30,80,globals.width//2-80,globals.height-150],border_radius=10)
			first = False


		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
				running_fft = False
				screen = pygame.display.set_mode(size,0,32)
				
	
			pos = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if drawing_board.collidepoint(pos):
					isPressed = True
				check_btn_collide(btns)
				for s in sliders:
					if s.button_rect.collidepoint(pos):
						s.hit = True
			if event.type == pygame.MOUSEBUTTONUP:
				isPressed = False
				for s in sliders:
					s.hit = False	

	
			if event.type == pygame.MOUSEMOTION and isPressed == True:
				if drawing_board.collidepoint(pos):
					(x,y) = pos
					data.append([x,y])
					drawCircle(win,x,y)


		new_num_points = numSlider.val
		if new_num_points != num_points and len(data):
			draw_converted(win,data,sliders[0])


		if len(data):
			draw_converted(win,data,sliders[0])
			
	
		for btn in btns:
			btn.draw()
		
		for s in sliders:
			s.draw()
  
		for s in sliders:
			if s.hit:
				s.move()

		pygame.display.update()


if __name__=="__main__":
	fft()