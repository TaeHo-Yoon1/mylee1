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
selected_eyes = None
selected_nose = None
selected_mouth = None

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

    eye_text = font.render('Select Eyes', True, BLACK)
    nose_text = font.render('Select Nose', True, BLACK)
    mouth_text = font.render('Select Mouth', True, BLACK)

    screen.blit(eye_text, (eye_button_rect.x + 20, eye_button_rect.y + 10))
    screen.blit(nose_text, (nose_button_rect.x + 20, nose_button_rect.y + 10))
    screen.blit(mouth_text, (mouth_button_rect.x + 20, mouth_button_rect.y + 10))

def select_image(images):
    selecting = True
    image_rects = []
    image_width = SCREEN_WIDTH // len(images)  # 화면에 나란히 표시하기 위해 각 이미지의 너비를 설정

    for i, img in enumerate(images):
        rect = pygame.Rect(i * image_width, SCREEN_HEIGHT // 2 - img.get_height() // 2, img.get_width(),
                           img.get_height())
        image_rects.append(rect)

    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(image_rects):
                    if rect.collidepoint(event.pos):
                        selecting = False
                        return i  # 선택된 이미지의 인덱스를 반환

        # Display selection screen
        screen.fill(WHITE)
        for i, img in enumerate(images):
            screen.blit(img, image_rects[i].topleft)
        pygame.display.flip()

    return None

def draw_face(eye_pos=(SCREEN_WIDTH // 2, 50), nose_pos=(SCREEN_WIDTH // 2, 250), mouth_pos=(SCREEN_WIDTH // 2, 400)):
    if selected_eyes is not None and selected_nose is not None and selected_mouth is not None:
        # Draw eyes
        screen.blit(eyes_images[selected_eyes], (eye_pos[0] - eyes_images[selected_eyes].get_width() // 2, eye_pos[1]))
        # Draw nose
        screen.blit(nose_images[selected_nose], (nose_pos[0] - nose_images[selected_nose].get_width() // 2, nose_pos[1]))
        # Draw mouth
        screen.blit(mouth_images[selected_mouth], (mouth_pos[0] - mouth_images[selected_mouth].get_width() // 2, mouth_pos[1]))


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if selected_eyes is None and eye_button_rect.collidepoint(event.pos):
                selected_eyes = select_image(eyes_images)
            elif selected_nose is None and nose_button_rect.collidepoint(event.pos):
                selected_nose = select_image(nose_images)
            elif selected_mouth is None and mouth_button_rect.collidepoint(event.pos):
                selected_mouth = select_image(mouth_images)

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw buttons only if the respective image has not been selected
    if selected_eyes is None or selected_nose is None or selected_mouth is None:
        draw_buttons()

    # Draw the selected face if all parts are selected
    draw_face()

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
