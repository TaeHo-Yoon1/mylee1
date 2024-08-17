import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Character Slot Machine')

# Load images for different facial features
eyes_images = [pygame.image.load(f'images/eyes_{i}.png') for i in range(1, 6)]
nose_images = [pygame.image.load(f'images/nose_{i}.png') for i in range(1, 6)]
mouth_images = [pygame.image.load(f'images/mouth_{i}.png') for i in range(1, 6)]

# Current selection indices
selected_eyes = None
selected_nose = None
selected_mouth = None

# Current rolling indices (for the slot machine effect)
rolling_eyes = 0
rolling_nose = 0
rolling_mouth = 0

# Rolling flags to determine when to stop each slot
rolling_eyes_active = False
rolling_nose_active = False
rolling_mouth_active = False

# Game state flag
game_started = False

# Define button areas
start_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50)
eye_start_button_rect = pygame.Rect(50, 50, 100, 50)
eye_stop_button_rect = pygame.Rect(150, 50, 100, 50)
nose_start_button_rect = pygame.Rect(50, 150, 100, 50)
nose_stop_button_rect = pygame.Rect(150, 150, 100, 50)
mouth_start_button_rect = pygame.Rect(50, 250, 100, 50)
mouth_stop_button_rect = pygame.Rect(150, 250, 100, 50)

font = pygame.font.SysFont(None, 36)

def draw_start_screen():
    screen.fill(WHITE)  # Fill the screen with white before the game starts
    pygame.draw.rect(screen, BLACK, start_button_rect, 2)
    start_text = font.render('Start Game', True, BLACK)
    screen.blit(start_text, (start_button_rect.x + 30, start_button_rect.y + 10))

def draw_buttons():
    # Draw start and stop buttons for eyes
    pygame.draw.rect(screen, BLACK, eye_start_button_rect, 2)
    pygame.draw.rect(screen, BLACK, eye_stop_button_rect, 2)
    eye_start_text = font.render('Start', True, BLACK)
    eye_stop_text = font.render('Stop', True, BLACK)
    screen.blit(eye_start_text, (eye_start_button_rect.x + 10, eye_start_button_rect.y + 10))
    screen.blit(eye_stop_text, (eye_stop_button_rect.x + 10, eye_stop_button_rect.y + 10))

    # Draw start and stop buttons for nose
    pygame.draw.rect(screen, BLACK, nose_start_button_rect, 2)
    pygame.draw.rect(screen, BLACK, nose_stop_button_rect, 2)
    nose_start_text = font.render('Start', True, BLACK)
    nose_stop_text = font.render('Stop', True, BLACK)
    screen.blit(nose_start_text, (nose_start_button_rect.x + 10, nose_start_button_rect.y + 10))
    screen.blit(nose_stop_text, (nose_stop_button_rect.x + 10, nose_stop_button_rect.y + 10))

    # Draw start and stop buttons for mouth
    pygame.draw.rect(screen, BLACK, mouth_start_button_rect, 2)
    pygame.draw.rect(screen, BLACK, mouth_stop_button_rect, 2)
    mouth_start_text = font.render('Start', True, BLACK)
    mouth_stop_text = font.render('Stop', True, BLACK)
    screen.blit(mouth_start_text, (mouth_start_button_rect.x + 10, mouth_start_button_rect.y + 10))
    screen.blit(mouth_stop_text, (mouth_stop_button_rect.x + 10, mouth_stop_button_rect.y + 10))

def draw_face(eye_pos=(SCREEN_WIDTH // 2, 50), nose_pos=(SCREEN_WIDTH // 2, 250), mouth_pos=(SCREEN_WIDTH // 2, 400)):
    # Draw eyes
    screen.blit(eyes_images[rolling_eyes], (eye_pos[0] - eyes_images[rolling_eyes].get_width() // 2, eye_pos[1]))
    # Draw nose
    screen.blit(nose_images[rolling_nose], (nose_pos[0] - nose_images[rolling_nose].get_width() // 2, nose_pos[1]))
    # Draw mouth
    screen.blit(mouth_images[rolling_mouth], (mouth_pos[0] - mouth_images[rolling_mouth].get_width() // 2, mouth_pos[1]))

def roll_slots():
    global rolling_eyes, rolling_nose, rolling_mouth

    if rolling_eyes_active:
        rolling_eyes = (rolling_eyes + 1) % len(eyes_images)
        print(f"Rolling eyes index: {rolling_eyes}")  # Debug print for eyes
    if rolling_nose_active:
        rolling_nose = (rolling_nose + 1) % len(nose_images)
        print(f"Rolling nose index: {rolling_nose}")  # Debug print for nose
    if rolling_mouth_active:
        rolling_mouth = (rolling_mouth + 1) % len(mouth_images)
        print(f"Rolling mouth index: {rolling_mouth}")  # Debug print for mouth

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started and start_button_rect.collidepoint(event.pos):
                game_started = True
                print("Game started!")  # Debug print for game start
            elif game_started:
                if eye_start_button_rect.collidepoint(event.pos):
                    rolling_eyes_active = True
                    print("Started rolling eyes")  # Debug print for eyes start
                elif eye_stop_button_rect.collidepoint(event.pos) and rolling_eyes_active:
                    selected_eyes = rolling_eyes
                    rolling_eyes_active = False
                    print(f"Stopped rolling eyes at index {rolling_eyes}")  # Debug print for eyes stop
                elif nose_start_button_rect.collidepoint(event.pos):
                    rolling_nose_active = True
                    print("Started rolling nose")  # Debug print for nose start
                elif nose_stop_button_rect.collidepoint(event.pos) and rolling_nose_active:
                    selected_nose = rolling_nose
                    rolling_nose_active = False
                    print(f"Stopped rolling nose at index {rolling_nose}")  # Debug print for nose stop
                elif mouth_start_button_rect.collidepoint(event.pos):
                    rolling_mouth_active = True
                    print("Started rolling mouth")  # Debug print for mouth start
                elif mouth_stop_button_rect.collidepoint(event.pos) and rolling_mouth_active:
                    selected_mouth = rolling_mouth
                    rolling_mouth_active = False
                    print(f"Stopped rolling mouth at index {rolling_mouth}")  # Debug print for mouth stop

    # Fill the screen with white
    screen.fill(WHITE)

    if not game_started:
        draw_start_screen()
    else:
        # Roll the slots
        roll_slots()

        # Draw buttons for each slot
        draw_buttons()

        # Draw the face with current rolling images
        draw_face()

    # Update the display
    pygame.display.flip()  # This updates the display

    # Control the speed of the slot machine effect
    clock.tick(10)  # Control the frame rate, adjust the speed with a higher or lower number

# Quit pygame
pygame.quit()
