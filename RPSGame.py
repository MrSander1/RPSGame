import pygame
import sys
import random
import time

from pygame.locals import *

run = True
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("RPS")

# Time
clock = pygame.time.Clock()
current_time = 0 
clicked_pressed_time = 0

# a dictinary to store the images with names
RPS_images_names = ['rock','paper','scissors']
RPS_images = {}
for name in RPS_images_names:
    filename = 'C:\\RPS Game\\assets\\' + name + '.png'
    RPS_images[name] = pygame.image.load(filename).convert_alpha()

# BIG ICONS
big_rock = RPS_images['rock'] 
big_rock = pygame.transform.scale(big_rock, (600,400))

big_paper = RPS_images['paper']
big_paper = pygame.transform.scale(big_paper, (600,400))

big_scissors = RPS_images['scissors']
big_scissors = pygame.transform.scale(big_scissors, (600,400))

# small icons
small_rock = RPS_images['rock'] 
small_rock = pygame.transform.scale(small_rock, (150,108))
small_rock_rect = small_rock.get_rect()
small_rock_rect.x = 735
small_rock_rect.y = 537

small_paper = RPS_images['paper']
small_paper = pygame.transform.scale(small_paper, (191,72))
small_paper_rect = small_paper.get_rect()
small_paper_rect.x = 909
small_paper_rect.y = 562

small_scissors = RPS_images['scissors']
small_scissors = pygame.transform.scale(small_scissors, (100,100))
small_scissors_rect = small_scissors.get_rect()
small_scissors_rect.x = 1119
small_scissors_rect.y = 554

# Text font
text_font = pygame.font.SysFont("Arial", 90)

# The only sound effect
sfx = pygame.mixer.Sound('C:\\RPS Game\\assets\\sfx.mp3')

# Function that draws text
def draw_text(text, font, text_col, x_pos, y_pos,):
    img = font.render(text, True, text_col)
    SCREEN.blit(img, (x_pos, y_pos))



# Main Function
def play():
    # Our click state 
    clicked = None
    # Our random choice
    Output = random.choice(("rock", "paper", "scissors"))
    # Main Loop
    while run:
        # For some reason this exists, I don't need it but I am too lazy too change it back
        waitingstuff = text_font.render('Waiting...',True, 'Black')
        
        # This is our background
        SCREEN.fill("Light Blue")
        # Texts are Drawn here
        draw_text("Player", text_font, (0,0,0), 900, 0)
        draw_text("Computer", text_font, (0,0,0), 200, 0)
        SCREEN.blit(waitingstuff, (200,300))
        
        # Small Icons are drawn
        SCREEN.blit(small_rock, (small_rock_rect.x,small_rock_rect.y))
        SCREEN.blit(small_paper, (small_paper_rect.x,small_paper_rect.y))
        SCREEN.blit(small_scissors,(small_scissors_rect.x,small_scissors_rect.y))

        
        # Our mouses current x, y
        mx, my = pygame.mouse.get_pos()
        
        current_time = pygame.time.get_ticks() 
        print(current_time)

        # For loop for our wonderful controls but also to tell if we click the icons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if small_rock_rect.collidepoint(event.pos):
                    clicked = "rock"
                    clicked_pressed_time = pygame.time.get_ticks()
                    sfx.play()
                elif small_paper_rect.collidepoint(event.pos):
                    clicked = "paper"
                    clicked_pressed_time = pygame.time.get_ticks()
                    sfx.play()
                elif small_scissors_rect.collidepoint(event.pos):
                    clicked = "scissors"
                    clicked_pressed_time = pygame.time.get_ticks()
                    sfx.play()
                
            if clicked and current_time - clicked_pressed_time > 2000: 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        play()
        # Our hover functionllity which lets us see our choices    
        if clicked is None:
          if small_rock_rect.collidepoint(mx,my):
              SCREEN.blit(big_rock,(695,105))
          elif small_paper_rect.collidepoint(mx,my):
              SCREEN.blit(big_paper,(695,105))
          elif small_scissors_rect.collidepoint(mx,my):
              SCREEN.blit(big_scissors,(695,105))
        # our elif that draws what we clicked onto the screens      
        elif clicked == "rock":
            SCREEN.blit(big_rock,(695,105))
        elif clicked == "paper":
            SCREEN.blit(big_paper,(695,105))
        elif clicked == "scissors":
            SCREEN.blit(big_scissors,(695,105))
        # This Draws our randomly selected choice onto the screen and also wait 500 milliseconds
        if clicked:          
            if Output == "rock" and current_time - clicked_pressed_time > 500:
                    pygame.draw.rect(SCREEN,'Light Blue', (200, 300, 400, 400))       
                    SCREEN.blit(big_rock,(95,105))
                    
            if Output == "paper" and current_time - clicked_pressed_time > 500: 
                   pygame.draw.rect(SCREEN,'Light Blue', (200, 300, 400, 400))      
                   SCREEN.blit(big_paper,(95,105)) 
                   
            if Output == "scissors" and current_time - clicked_pressed_time > 500:  
                   pygame.draw.rect(SCREEN,'Light Blue', (200, 300, 400, 400))      
                   SCREEN.blit(big_scissors,(95,105))
        
        # States of Game: So if we win or not, there is also a delay of 2000 milliseconds for our player to tell if they won or not
        if clicked:
            if clicked == "rock" and Output == "paper" and current_time - clicked_pressed_time > 2000:
                SCREEN.fill("Red")
                draw_text("You Lost!", text_font, (0,0,0), 480, 260)
                draw_text("Press Space to Try Again", text_font, (0,0,0), 140, 360)
                               
            if clicked == "paper" and Output == "scissors" and current_time - clicked_pressed_time > 2000:
                SCREEN.fill("Red")
                draw_text("You Lost!", text_font, (0,0,0), 480, 260)
                draw_text("Press Space to Try Again", text_font, (0,0,0), 140, 360)
                
                
            if clicked == "scissors" and Output == "rock" and current_time - clicked_pressed_time > 2000:
                SCREEN.fill("Red")
                draw_text("You Lost!", text_font, (0,0,0), 480, 260) 
                draw_text("Press Space to Try Again", text_font, (0,0,0), 140, 360)
                
               
            if clicked == "paper" and Output == "rock" and current_time - clicked_pressed_time > 2000:
                SCREEN.fill("Light Green")
                draw_text("You Win!", text_font, (0,0,0), 480, 260)
                draw_text("Press Space to Try Again", text_font, (0,0,0), 140, 360)
                
               
            if clicked == "scissors" and Output == "paper" and current_time - clicked_pressed_time > 2000:
                SCREEN.fill("Light Green")
                draw_text("You Win!", text_font, (0,0,0), 480, 260)
                draw_text("Press Space to Try Again", text_font, (0,0,0), 140, 360)
                
            if clicked == "rock" and Output == "scissors" and current_time - clicked_pressed_time > 2000:
                SCREEN.fill("Light Green")
                draw_text("You Win!", text_font, (0,0,0), 480, 260)
                draw_text("Press Space to Try Again", text_font, (0,0,0), 140, 360)
                
             
            if clicked == "rock" and Output == "rock" and current_time - clicked_pressed_time > 2000:
                SCREEN.fill("Light Grey")
                draw_text("You Tie!", text_font, (0,0,0), 480, 260)
                draw_text("Press Space to Try Again", text_font, (0,0,0), 140, 360)
                
              
            if clicked == "paper" and Output == "paper" and current_time - clicked_pressed_time > 2000:
                SCREEN.fill("Light Grey")
                draw_text("You Tie!", text_font, (0,0,0), 480, 260)
                draw_text("Press Space to Try Again", text_font, (0,0,0), 140, 360)
               
            if clicked == "scissors" and Output == "scissors" and current_time - clicked_pressed_time > 2000:
                SCREEN.fill("Light Grey")
                draw_text("You Tie!", text_font, (0,0,0), 480, 260)
                draw_text("Press Space to Try Again", text_font, (0,0,0), 140, 360)
# The game runs on 60 frames per seconds
        pygame.display.flip()
        clock.tick(60)
          
            
                
play()








