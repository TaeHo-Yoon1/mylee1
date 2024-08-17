import pygame

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
current_eyes = 0
current_nose = 0
current_mouth = 0

# Define button areas
eye_button_rect = pygame.Rect(50, 50, 200, 50)
nose_button_rect = pygame.Rect(50, 150, 200, 50)
mouth_button_rect = pygame.Rect(50, 250, 200, 50)

font = pygame.font.SysFont(None, 36)


def draw_buttons():
    # Draw buttons
    pygame.draw.rect(screen, BLACK, eye_button_rect, 2)
    pygame.draw.rect(screen, BLACK, nose_button_rect, 2)
    pygame.draw.rect(screen, BLACK, mouth_button_rect, 2)

    eye_text = font.render('Change Eyes', True, BLACK)
    nose_text = font.render('Change Nose', True, BLACK)
    mouth_text = font.render('Change Mouth', True, BLACK)

    screen.blit(eye_text, (eye_button_rect.x + 20, eye_button_rect.y + 10))
    screen.blit(nose_text, (nose_button_rect.x + 20, nose_button_rect.y + 10))
    screen.blit(mouth_text, (mouth_button_rect.x + 20, mouth_button_rect.y + 10))


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse clicked at: {event.pos}")  # 디버그용으로 클릭 위치 출력
            if eye_button_rect.collidepoint(event.pos):
                current_eyes = (current_eyes + 1) % len(eyes_images)
                print("Eye button clicked!")  # 디버그용 메시지
            elif nose_button_rect.collidepoint(event.pos):
                current_nose = (current_nose + 1) % len(nose_images)
                print("Nose button clicked!")  # 디버그용 메시지
            elif mouth_button_rect.collidepoint(event.pos):
                current_mouth = (current_mouth + 1) % len(mouth_images)
                print("Mouth button clicked!")  # 디버그용 메시지

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw buttons
    draw_buttons()

    # Draw the current selected facial features
    screen.blit(eyes_images[current_eyes], (300, 150))
    screen.blit(nose_images[current_nose], (300, 250))
    screen.blit(mouth_images[current_mouth], (300, 350))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
