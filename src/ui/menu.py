import pygame
from src.utils.constants import FONT_NAME, FONT_SIZE

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.options = [
            ("簡單 (10x15)", "easy", (10, 15)),
            ("普通 (15x20)", "normal", (15, 20)),
            ("困難 (20x30)", "hard", (20, 30)),
        ]
        self.selected = 0

    def draw(self):
        self.screen.fill((50, 50, 80))
        title = self.font.render("塔防遊戲 - 難度選擇", True, (255, 255, 255))
        self.screen.blit(title, (50, 30))
        for i, (label, _, _) in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected else (200, 200, 200)
            text = self.font.render(label, True, color)
            self.screen.blit(text, (70, 80 + i * 40))
        pygame.display.flip()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        _, difficulty, map_size = self.options[self.selected]
                        return difficulty, map_size
            clock.tick(30)

    def show_game_over(self, score):
        self.screen.fill((30, 10, 10))
        font_big = pygame.font.SysFont(FONT_NAME, FONT_SIZE + 10)
        text1 = font_big.render("遊戲結束", True, (255, 80, 80))
        text2 = self.font.render(f"得分: {score}", True, (255, 255, 255))
        text3 = self.font.render("按任意鍵離開...", True, (180, 180, 180))
        self.screen.blit(text1, (60, 60))
        self.screen.blit(text2, (70, 130))
        self.screen.blit(text3, (50, 180))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False 
                    import pygame
                    from src.utils.constants import FONT_NAME, FONT_SIZE

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.options = [
            ("簡單 (10x15)", "easy", (10, 15)),
            ("普通 (15x20)", "normal", (15, 20)),
            ("困難 (20x30)", "hard", (20, 30)),
        ]
        self.selected = 0

    def draw(self):
        self.screen.fill((50, 50, 80))
        title = self.font.render("塔防遊戲 - 難度選擇", True, (255, 255, 255))
        self.screen.blit(title, (50, 30))
        for i, (label, _, _) in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected else (200, 200, 200)
            text = self.font.render(label, True, color)
            self.screen.blit(text, (70, 80 + i * 40))
        pygame.display.flip()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        _, difficulty, map_size = self.options[self.selected]
                        return difficulty, map_size
            clock.tick(30)

    def show_game_over(self, score):
        self.screen.fill((30, 10, 10))
        font_big = pygame.font.SysFont(FONT_NAME, FONT_SIZE + 10)
        text1 = font_big.render("遊戲結束", True, (255, 80, 80))
        text2 = self.font.render(f"得分: {score}", True, (255, 255, 255))
        text3 = self.font.render("按任意鍵離開...", True, (180, 180, 180))
        self.screen.blit(text1, (60, 60))
        self.screen.blit(text2, (70, 130))
        self.screen.blit(text3, (50, 180))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False