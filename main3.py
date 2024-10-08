import pygame
import random

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
hair_images = [pygame.image.load(f'images/hair_{i}.png') for i in range(1, 6)]
eyes_images = [pygame.image.load(f'images/eyes_{i}.png') for i in range(1, 6)]
nose_images = [pygame.image.load(f'images/nose_{i}.png') for i in range(1, 6)]
mouth_images = [pygame.image.load(f'images/mouth_{i}.png') for i in range(1, 6)]

# Current rolling indices (for the slot machine effect)
rolling_hair = random.randint(0, len(hair_images) - 1)
rolling_eyes = random.randint(0, len(eyes_images) - 1)
rolling_nose = random.randint(0, len(nose_images) - 1)
rolling_mouth = random.randint(0, len(mouth_images) - 1)

# Rolling flags to determine when to stop each slot
rolling_hair_active = False
rolling_eyes_active = False
rolling_nose_active = False
rolling_mouth_active = False

# Game state flag
game_started = False
rolling_sequence = 0  # 0 for hair, 1 for eyes, 2 for nose, 3 for mouth

# Notification state
notification_message = ""
notification_time = 0

# Define button areas
start_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50)
slot_button_rect = pygame.Rect(SCREEN_WIDTH - 220, SCREEN_HEIGHT - 70, 200, 50)  # Place button at the bottom right

font = pygame.font.SysFont(None, 36)

def initialize_slots():
    global rolling_hair, rolling_eyes, rolling_nose, rolling_mouth
    rolling_hair = random.randint(0, len(hair_images) - 1)
    rolling_eyes = random.randint(0, len(eyes_images) - 1)
    rolling_nose = random.randint(0, len(nose_images) - 1)
    rolling_mouth = random.randint(0, len(mouth_images) - 1)

def draw_start_screen():
    screen.fill(WHITE)  # Fill the screen with white before the game starts
    pygame.draw.rect(screen, BLACK, start_button_rect, 2)
    start_text = font.render('Start Game', True, BLACK)
    screen.blit(start_text, (start_button_rect.x + 30, start_button_rect.y + 10))

def draw_slot_button():
    pygame.draw.rect(screen, BLACK, slot_button_rect, 2)
    slot_text = font.render('Spin Slots', True, BLACK)
    screen.blit(slot_text, (slot_button_rect.x + 30, slot_button_rect.y + 10))

def draw_face(hair_pos=(SCREEN_WIDTH // 2, 50), eye_pos=(SCREEN_WIDTH // 2, -200), nose_pos=(SCREEN_WIDTH // 2, 300), mouth_pos=(SCREEN_WIDTH // 2, 400)):
    # Draw hair
    screen.blit(hair_images[rolling_hair], (hair_pos[0] - hair_images[rolling_hair].get_width() // 2, hair_pos[1]))
    # Draw eyes
    screen.blit(eyes_images[rolling_eyes], (eye_pos[0] - eyes_images[rolling_eyes].get_width() // 2, eye_pos[1]))
    # Draw nose
    screen.blit(nose_images[rolling_nose], (nose_pos[0] - nose_images[rolling_nose].get_width() // 2, nose_pos[1]))
    # Draw mouth
    screen.blit(mouth_images[rolling_mouth], (mouth_pos[0] - mouth_images[rolling_mouth].get_width() // 2, mouth_pos[1]))


def roll_slots():
    global rolling_hair, rolling_eyes, rolling_nose, rolling_mouth, rolling_sequence
    if rolling_sequence == 0 and rolling_hair_active:
        rolling_hair = (rolling_hair + 1) % len(hair_images)
        print(f"Rolling hair index: {rolling_hair}")  # Debug print for hair
    elif rolling_sequence == 1 and rolling_eyes_active:
        rolling_eyes = (rolling_eyes + 1) % len(eyes_images)
        print(f"Rolling eyes index: {rolling_eyes}")  # Debug print for eyes
    elif rolling_sequence == 2 and rolling_nose_active:
        rolling_nose = (rolling_nose + 1) % len(nose_images)
        print(f"Rolling nose index: {rolling_nose}")  # Debug print for nose
    elif rolling_sequence == 3 and rolling_mouth_active:
        rolling_mouth = (rolling_mouth + 1) % len(mouth_images)
        print(f"Rolling mouth index: {rolling_mouth}")  # Debug print for mouth

def stop_slot():
    global rolling_sequence, rolling_hair_active, rolling_eyes_active, rolling_nose_active, rolling_mouth_active, notification_message, notification_time
    if rolling_sequence == 0:
        rolling_hair_active = False
        rolling_sequence += 1  # Move to the next slot (eyes)
        notification_message = "Hair selected!"
    elif rolling_sequence == 1:
        rolling_eyes_active = False
        rolling_sequence += 1  # Move to the next slot (nose)
        notification_message = "Eyes selected!"
    elif rolling_sequence == 2:
        rolling_nose_active = False
        rolling_sequence += 1  # Move to the next slot (mouth)
        notification_message = "Nose selected!"
    elif rolling_sequence == 3:
        rolling_mouth_active = False
        rolling_sequence = 0  # Reset sequence after the last slot
        notification_message = "Mouth selected!"

    notification_time = pygame.time.get_ticks()  # Record the time of the notification

def draw_notification():
    if notification_message and pygame.time.get_ticks() - notification_time < 2000:  # Show notification for 2 seconds
        notification_text = font.render(notification_message, True, BLACK)
        screen.blit(notification_text, (SCREEN_WIDTH // 2 - notification_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

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
                initialize_slots()  # Initialize the slots when the game starts
                print("Game started!")  # Debug print for game start
            elif game_started and slot_button_rect.collidepoint(event.pos):
                if rolling_sequence == 0:
                    if not rolling_hair_active:
                        rolling_hair_active = True  # Start spinning hair
                        print("Started spinning hair")
                    else:
                        stop_slot()  # Stop hair and save value
                elif rolling_sequence == 1:
                    if not rolling_eyes_active:
                        rolling_eyes_active = True  # Start spinning eyes
                        print("Started spinning eyes")
                    else:
                        stop_slot()  # Stop eyes and save value
                elif rolling_sequence == 2:
                    if not rolling_nose_active:
                        rolling_nose_active = True  # Start spinning nose
                        print("Started spinning nose")
                    else:
                        stop_slot()  # Stop nose and save value
                elif rolling_sequence == 3:
                    if not rolling_mouth_active:
                        rolling_mouth_active = True  # Start spinning mouth
                        print("Started spinning mouth")
                    else:
                        stop_slot()  # Stop mouth and save value

    # Fill the screen with white
    screen.fill(WHITE)

    if not game_started:
        draw_start_screen()
    else:
        # Roll the slots if any are active
        roll_slots()

        # Draw the slot button
        draw_slot_button()

        # Draw the face with current rolling images
        draw_face()

        # Display the notification if needed
        draw_notification()

    # Update the display
    pygame.display.flip()  # This updates the display

    # Control the speed of the slot machine effect
    clock.tick(30)  # Adjust the speed with a higher or lower number

# Quit pygame
pygame.quit()
