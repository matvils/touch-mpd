import curses, mpd 

#RASPBERY screen 132x35

client = mpd.MPDClient(use_unicode=True)

screen = curses.initscr() 
#curses.noecho() 
curses.curs_set(0) 
screen.keypad(1) 
curses.mousemask(1)
#curses.nodelay(1)



#  ▖   ▗   ▘   ▙   ▚   ▛   ▜   ▝   ▞   ▟ 


#      ▜  ▛  ▟ ▙  ░  ▒  ▓
def draw_prev_song(y, x, color):
#	▜		      1234567890123
	screen.addstr(y+1,x, "╔═══════════╗ ",curses.color_pair(color))
	screen.addstr(y+2,x, "║  █    ▟█  ║ ",curses.color_pair(color))
	screen.addstr(y+3,x, "║  █  ▗███  ║ ",curses.color_pair(color))
	screen.addstr(y+4,x, "║  █  ████  ║ ",curses.color_pair(color))
	screen.addstr(y+5,x, "║  █  ▝███  ║ ",curses.color_pair(color))
	screen.addstr(y+6,x, "║  █    ▜█  ║ ",curses.color_pair(color))
	screen.addstr(y+7,x, "╚═══════════╝ ",curses.color_pair(color))


def draw_play(y, x, color):
#			      1234567890123
	screen.addstr(y+1,x, "╔═══════════╗ ",curses.color_pair(color))
	screen.addstr(y+2,x, "║   ██▙     ║ ",curses.color_pair(color))
	screen.addstr(y+3,x, "║   ████▙   ║ ",curses.color_pair(color))
	screen.addstr(y+4,x, "║   █████▊  ║ ",curses.color_pair(color))
	screen.addstr(y+5,x, "║   ████▛   ║ ",curses.color_pair(color))
	screen.addstr(y+6,x, "║   ██▛     ║ ",curses.color_pair(color))
	screen.addstr(y+7,x, "╚═══════════╝ ",curses.color_pair(color))


def draw_stop(y, x, color):
#			      1234567890123
	screen.addstr(y+1,x, "╔═══════════╗ ",curses.color_pair(color))
	screen.addstr(y+2,x, "║           ║ ",curses.color_pair(color))
	screen.addstr(y+3,x, "║  ███████  ║ ",curses.color_pair(color))
	screen.addstr(y+4,x, "║  ███████  ║ ",curses.color_pair(color))
	screen.addstr(y+5,x, "║  ███████  ║ ",curses.color_pair(color))
	screen.addstr(y+6,x, "║           ║ ",curses.color_pair(color))
	screen.addstr(y+7,x, "╚═══════════╝ ",curses.color_pair(color))



def draw_pause(y, x, color):
#			      1234567890123
	screen.addstr(y+1,x, "╔═══════════╗ ",curses.color_pair(color))
	screen.addstr(y+2,x, "║           ║ ",curses.color_pair(color))
	screen.addstr(y+3,x, "║    █ █    ║ ",curses.color_pair(color))
	screen.addstr(y+4,x, "║    █ █    ║ ",curses.color_pair(color))
	screen.addstr(y+5,x, "║    █ █    ║ ",curses.color_pair(color))
	screen.addstr(y+6,x, "║           ║ ",curses.color_pair(color))
	screen.addstr(y+7,x, "╚═══════════╝ ",curses.color_pair(color))
   

def draw_next_song(y, x, color):
#			      1234567890123
	screen.addstr(y+1,x, "╔═══════════╗ ",curses.color_pair(color))
	screen.addstr(y+2,x, "║  █▙    █  ║ ",curses.color_pair(color))
	screen.addstr(y+3,x, "║  ██▙▖  █  ║ ",curses.color_pair(color))
	screen.addstr(y+4,x, "║  ████  █  ║ ",curses.color_pair(color))
	screen.addstr(y+5,x, "║  ██▛▘  █  ║ ",curses.color_pair(color))
	screen.addstr(y+6,x, "║  █▛    █  ║ ",curses.color_pair(color))
	screen.addstr(y+7,x, "╚═══════════╝ ",curses.color_pair(color))


def draw_menu(stdscr):
	#Inicialisation
	#stdscr.clear()
	k=0	

	timebar = " "
	# Start colors in curses
	curses.start_color()
	curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
	curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)
	statusbar=""
	testam = " "
	color_prev = 1 
	color_play = 1
	color_stop = 1
	color_pause = 1
	color_next = 1
	widthn = 0
	heightn = 0
	songidn = ""
	jumptim=0

	#Main loop
	while (k !=ord('q')):
		screen.nodelay(1)
		#stdscr.clear()
		#stdscr.refresh()
		client.connect("localhost", 6600)
		# Get MAX screen size
		height, width = stdscr.getmaxyx()
		#whstr =str(height) +" " + str(width)
		#stdscr.addstr(0, 0, whstr, curses.color_pair(1))
		
		if heightn != height or widthn != width:
			screen.clear()
			screen.refresh()
		
		heightn = height
		widthn = width
		
		# Draw objects
		drawx = int((width // 2) - 35)
		drawy = int((height // 2) - 6)
				
		spacing = 15 
	
		
		draw_prev_song(drawy, drawx, color_prev)
		draw_play(drawy, drawx + spacing , color_play)
		draw_stop(drawy, drawx + spacing*2, color_stop) 
		draw_pause(drawy, drawx + spacing*3, color_pause)
		draw_next_song(drawy, drawx + spacing*4, color_next)
		#Draw statusbar

		h=" "
		output=" "
		
		status = client.status()
		state = status.get('state')
		if state !="stop":
			laiks = str(status.get('time'))
			timera = status.get('time')
			curtime = timera[0]
			maxtime = timera[1]
			songid = status.get('songid')
			song = client.playlistid(songid)
			dziesma = str(song[0]) 
			words = dziesma.split("'")
			artist = str(words[11]) + " - " + str(words[19])
		
			sadalits = timera.split(":")
			maxtime = int(sadalits[1])	
			curtime = int(sadalits[0])
		
			#Prints artist
			vidusx = int((width // 2) - (len(artist) // 2) - len(artist) % 2)
			vidusy = int((height // 2) + 8)
			stdscr.addstr(vidusy, vidusx, artist, curses.color_pair(5))


			#print(curtime)
			slider = int((curtime*74)/maxtime)
			#print(slider)	
			#if int(curtime)  ==  0:
			#	curses.napms(100)
			#	stdscr.clear()
			#	stdscr.refresh()
			
			if songid != songidn:
				stdscr.clear()
				stdscr.refresh()
			

			stdscr.addstr(vidusy-2, drawx, "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░", curses.color_pair(5))
			z=1
			while z<slider:
				stdscr.addstr(vidusy-2, drawx + z - 1  , "█" , curses.color_pair(5))
				z+=1	
				stdscr.refresh()
			songidn = songid
		#stdscr.addstr(0,0, state + " " + songid+ " " + songidn, curses.color_pair(3))
			

		# Mouse click
		event = screen.getch() 
		if event == ord("q"): break 
		if event == curses.KEY_MOUSE:
			_, mx, my, _, _ = curses.getmouse()
			y, x = screen.getyx()
			if (mx>=drawx) and (mx<=(drawx+13)) and (my>drawy) and (my<drawy+8):
				testam = "PREV"		
				client.previous()	
				stdscr.clear()
				stdscr.refresh()

			if (mx>=drawx + spacing) and (mx<=(drawx + 13 + spacing)) and (my>drawy) and (my<drawy+8):
				client.play()
				testam = "PLAY"		
				stdscr.clear()
				stdscr.refresh()

			if (mx>=drawx + 2 * spacing) and (mx<=drawx+13 + 2 * spacing) and (my>drawy) and (my<drawy+8):
				client.stop()
				stdscr.clear()
				stdscr.refresh()
				testam = "STOP"		

			if (mx>=drawx + 3 *spacing) and  (mx<=drawx+13 + 3 * spacing)  and (my>drawy) and (my<drawy+8):
				testam = "PAUSE"		
				client.pause(1)
				stdscr.clear()
				stdscr.refresh()
		
			if (mx>=drawx + 4 * spacing) and  (mx<=drawx+13 + 4  * spacing)  and (my>drawy) and (my<drawy+8):
				testam = "NEXT"		
				client.next()
				stdscr.clear()
				stdscr.refresh()

			if (mx>=drawx) and (mx<=drawx+73) and (my==vidusy-2):	
				
				stdscr.clear()
				stdscr.refresh()
				jumptime = int((maxtime*(mx-drawx))/74)
				#stdscr.addstr(1, 1, str(mx-drawx) + " : " + str(jumptime), curses.color_pair(3))
				client.seekid(songid, jumptime)


		#stdscr.refresh()
		#k = stdscr.getch()
		#screen.refresh()
		curses.napms(100)
		client.close()
		client.disconnect() 

def main():
	curses.wrapper(draw_menu)

if __name__ == "__main__":
	main()



