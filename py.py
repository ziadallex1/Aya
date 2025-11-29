import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Winter Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (135, 206, 235)
FONT = pygame.font.SysFont(None, 35)

player_data = {
    "Name": "Aya Khaled Saad Awad",
    "Class": "2",
    "Roll No": "25",
    "Department": "Arabic Kindergarten",
    "Course": "Electronic Program Production",
    "Professor": "Sahar Salah",
    "Assistant": "Nihal Gamal"
}

winter_words = ["Snow", "Hat", "Coat", "Skates"]
image_paths = [
    r"D:\بحث\snow.png",
    r"D:\بحث\hat.png",
    r"D:\بحث\coat.png",
    r"D:\بحث\skates.png"
]

images = []
for path in image_paths:
    try:
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, (100, 100))
        images.append(img)
    except pygame.error as e:
        print(f"Error loading image {path}: {e}")

image_positions = [(650, 50 + i*130) for i in range(len(images))]
image_rects = [img.get_rect(topleft=pos) for img, pos in zip(images, image_positions)]

def draw_text(text, pos, color=BLACK):
    img = FONT.render(text, True, color)
    screen.blit(img, pos)

def frame_player_data():
    running = True
    while running:
        screen.fill(WHITE)
        y_start = 50
        for key, value in player_data.items():
            draw_text(f"{key}: {value}", (50, y_start))
            y_start += 50

        next_button = pygame.Rect(550, 500, 200, 60)
        pygame.draw.rect(screen, BLUE, next_button)
        draw_text("Next", (600, 515), WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.collidepoint(event.pos):
                    running = False

        pygame.display.update()

def frame_start():
    running = True
    while running:
        screen.fill(BLUE)
        draw_text("Winter Game", (300, 200))
        play_button = pygame.Rect(300, 400, 200, 60)
        pygame.draw.rect(screen, WHITE, play_button)
        draw_text("Play Game", (340, 415), BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    running = False

        pygame.display.update()

def frame_game():
    score = 0
    dragged_word = None
    dragged_word_index = None
    running = True

    word_positions = [(50, 150 + i*80) for i in range(len(winter_words))]

    while running:
        screen.fill(WHITE)
        draw_text(f"Score: {score}", (50, 20))
        draw_text(f"Player: {player_data['Name']}", (50, 60))

        for i, word in enumerate(winter_words):
            draw_text(word, word_positions[i])

        for i, img in enumerate(images):
            screen.blit(img, image_rects[i])
            pygame.draw.rect(screen, BLACK, image_rects[i], 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, pos in enumerate(word_positions):
                    word_rect = pygame.Rect(pos[0], pos[1], 150, 50)
                    if word_rect.collidepoint(event.pos):
                        dragged_word = winter_words[i]
                        dragged_word_index = i
            elif event.type == pygame.MOUSEBUTTONUP:
                if dragged_word is not None:
                    correct = False
                    for i, img_rect in enumerate(image_rects):
                        if img_rect.collidepoint(event.pos):
                            if i == dragged_word_index:
                                score += 1
                                correct = True
                            if correct:
                                screen.fill(GREEN)
                                pygame.display.update()
                                time.sleep(0.5)
                            else:
                                screen.fill(RED)
                                pygame.display.update()
                                time.sleep(0.5)
                            break
                    dragged_word = None
                    dragged_word_index = None

        if dragged_word is not None:
            mx, my = pygame.mouse.get_pos()
            draw_text(dragged_word, (mx, my))

        pygame.display.update()

        if score == len(winter_words):
            running = False

    screen.fill(WHITE)
    if score >= len(winter_words):
        draw_text(f"Well done, Aya! Your score: {score}", (200, 250), BLUE)
    else:
        draw_text(f"Try again! Your score: {score}", (200, 250), RED)
    pygame.display.update()
    time.sleep(3)

frame_player_data()
frame_start()
frame_game()
pygame.quit()
