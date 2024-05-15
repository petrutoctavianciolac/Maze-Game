import pygame
import button
import sys
from maze import Maze
from player import Player
from game import Game
from clock import Clock

input_tile = 60

class Main():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("impact", 30)
        self.message_color = pygame.Color("black")
        self.running = True
        self.game_over = False
        self.final_sound = False
        self.end_time = False
        self.FPS = pygame.time.Clock()
    
    def _draw(self, maze, tile, player, game, clock):
        # draw maze
        for cell in maze.grid_cells:
            cell.draw(screen, tile)

		# add a goal point to reach
        game.add_goal_point(self.screen)

        menu_mouse_pos = pygame.mouse.get_pos()

        for button in [game_back_button, game_restart_button, new_game_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

		# draw every player movement
        player.draw(self.screen)
        player.update()
            
        
        if self.game_over:
            if self.final_sound == False:
                if self.end_time == False:
                    win_sound.play()
                else:
                    lose_sound.play()
            self.final_sound = True
            clock.stop_timer()
            self.screen.blit(game.message(self.end_time),(700,200))
        else:
            clock.update_timer()
        self.screen.blit(clock.display_timer(), (1100,200))
	
        pygame.display.flip()

    def main(self, frame_size, tile):
        cols, rows = frame_size[0] // tile, frame_size[1] // tile
        maze = Maze(cols // 2, rows)
        game = Game(maze.grid_cells[-1], tile)
        player = Player(tile // 3, tile // 3, tile // 3)
        clock = Clock()
        
        maze.generate_maze()
        clock.start_timer()
        
        while self.running:
            self.screen.fill("#3A10E5")
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if game_back_button.checkForInput(pos):
                        self.running = False

                    if game_restart_button.checkForInput(pos):
                        self.game_over = False
                        self.end_time = False
                        player.x, player.y = tile // 3, tile // 3
                        self.final_sound = False
                        clock.reset_timer()
                        clock.start_timer()

                    if new_game_button.checkForInput(pos):
                        maze = Maze(cols // 2, rows)
                        maze.generate_maze()
                        clock.reset_timer()
                        clock.start_timer()
                        self.final_sound = False
                        player.x, player.y = tile // 3, tile // 3
                        self.end_time = False
                        self.game_over = False
                    
                if event.type == pygame.KEYDOWN:
                    if not self.game_over:
                        if event.key == pygame.K_LEFT:
                            player.left_pressed = True
                        if event.key == pygame.K_RIGHT:
                            player.right_pressed = True
                        if event.key == pygame.K_UP:
                            player.up_pressed = True
                        if event.key == pygame.K_DOWN:
                            player.down_pressed = True
                    
                if event.type == pygame.KEYUP:
                    if not self.game_over:
                        if event.key == pygame.K_LEFT:
                            player.left_pressed = False
                        if event.key == pygame.K_RIGHT:
                            player.right_pressed = False
                        if event.key == pygame.K_UP:
                            player.up_pressed = False
                        if event.key == pygame.K_DOWN:
                            player.down_pressed = False

            if not self.game_over:
                player.check_move(tile, maze.grid_cells, maze.thickness)
                if game.is_win(player):
                    self.game_over = True
                    player.left_pressed = False
                    player.right_pressed = False
                    player.up_pressed = False
                    player.down_pressed = False
                
                if clock.get_elapsed_time() == 0:
                    self.game_over = True
                    self.end_time = True
                    player.left_pressed = False
                    player.right_pressed = False
                    player.up_pressed = False
                    player.down_pressed = False
                    
            self._draw(maze, tile, player, game, clock)
            self.FPS.tick(60)


                        

def play():
    window_size = (1280, 720)
    screen = (window_size[0], window_size[1])
    tile_size = input_tile
    screen = pygame.display.set_mode(screen)
    pygame.display.set_caption("Maze")

    game = Main(screen)
    game.main(window_size, tile_size)

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def options():

    global input_tile
    screen.blit(bg, (0, 0))
    
    options_text = get_font(100).render("OPTIONS", True, "#3A10E5")
    options_rect = options_text.get_rect(center=(640, 100))


    screen.blit(options_text, options_rect)

    opt = True
    music = True

    while opt:

        menu_mouse_pos = pygame.mouse.get_pos()

        for but in [opt_back_button, music_volume_button, difficulty_button]:
            but.changeColor(menu_mouse_pos)
            but.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type== pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if opt_back_button.checkForInput(pos):
                    opt = False
                if music_volume_button.checkForInput(pos):
                    if music == True:
                        pygame.mixer.music.pause()
                        music = False
                        music_volume_button.setText("MUSIC OFF")
                        music_volume_button.centerText()
                    else:
                        pygame.mixer.music.unpause()
                        music = True
                        music_volume_button.setText("MUSIC ON")
                        music_volume_button.centerText()
                
                if  difficulty_button.checkForInput(pos):
                    if input_tile == 60:
                        input_tile = 45
                        difficulty_button.setText("MEDIUM")
                        difficulty_button.centerText()
                    elif input_tile == 45:
                        input_tile = 30
                        difficulty_button.setText("HARD")
                        difficulty_button.centerText()
                    elif input_tile == 30:
                        input_tile = 60
                        difficulty_button.setText("EASY")
                        difficulty_button.centerText()

            

        pygame.display.flip()

pygame.init()

pygame.display.set_caption("Maze")

screen = pygame.display.set_mode((1280, 720))
running = True
bg = pygame.image.load("assets/Background.png")

win_sound = pygame.mixer.Sound("assets/final.mp3")
lose_sound = pygame.mixer.Sound("assets/lose.mp3")

pygame.mixer.init()
pygame.mixer.music.load("assets/soundtrack.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

start_button = button.Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="Black", hovering_color="Green")
options_button = button.Button(image = pygame.image.load("assets/Options Rect.png"), pos = (640, 400),
                               text_input="OPTIONS", font = get_font(75), base_color="Black", hovering_color="Blue")
quit_button = button.Button(image = pygame.image.load("assets/Quit Rect.png"), pos = (640, 550),
                            text_input="QUIT", font=get_font(75), base_color="Black", hovering_color="Red")

opt_back_button = button.Button(image = pygame.image.load("assets/Quit Rect.png"), pos = (640, 550),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Blue")

music_volume_button = button.Button(image = pygame.image.load("assets/Sound Rect.png"), pos = (640, 250),
                            text_input="MUSIC ON", font=get_font(75), base_color="Black", hovering_color="Blue")

difficulty_button = button.Button(image = pygame.image.load("assets/Difficulty Rect.png"), pos = (640, 400),
                            text_input="EASY", font=get_font(75), base_color="Black", hovering_color="Blue")

game_back_button = button.Button(image = pygame.image.load("assets/Quit Rect.png"), pos = (900, 650),
                            text_input="BACK", font=pygame.font.SysFont("impact", 75), base_color="Black", hovering_color="Red")

game_restart_button = button.Button(image = pygame.image.load("assets/Quit Rect.png"), pos = (900, 500),
                            text_input="RESTART", font=pygame.font.SysFont("impact", 75), base_color="Black", hovering_color="Red")

new_game_button = button.Button(image = pygame.image.load("assets/Quit Rect.png"), pos = (900, 350),
                            text_input="NEW GAME", font=pygame.font.SysFont("impact", 75), base_color="Black", hovering_color="Red")

while running:
    screen.blit(bg, (0, 0))

    menu_mouse_pos = pygame.mouse.get_pos()

    menu_text = get_font(100).render("MAZE", True, "#3A10E5")
    menu_rect = menu_text.get_rect(center=(640, 100))


    screen.blit(menu_text, menu_rect)

    for button in [start_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
              pos = pygame.mouse.get_pos()
              if quit_button.checkForInput(menu_mouse_pos):
                    running = False
              if options_button.checkForInput(menu_mouse_pos):
                   options()
              if start_button.checkForInput(pos):
                  play()
                   

    pygame.display.flip()


pygame.quit()