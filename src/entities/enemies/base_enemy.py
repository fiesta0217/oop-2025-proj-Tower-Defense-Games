import pygame
from src.entities.base_entity import BaseEntity
from src.utils.constants import TILE_SIZE  # 改為引入專案的 TILE_SIZE

class BaseEnemy(BaseEntity):
    name = "BaseEnemy"
    base_speed = 60  # pix/sec
    base_hp = 30
    reward = 10

    def __init__(self, start_tile, game_manager):
        difficulty = getattr(game_manager, "difficulty", "normal")
        if difficulty == "easy":
            self.speed = self.base_speed * 0.8
            self.hp_default = int(self.base_hp * 0.8)
        elif difficulty == "hard":
            self.speed = self.base_speed * 1.2
            self.hp_default = int(self.base_hp * 1.5)
        else:  # normal
            self.speed = self.base_speed
            self.hp_default = self.base_hp
        x = start_tile[1] * TILE_SIZE + TILE_SIZE // 2
        y = start_tile[0] * TILE_SIZE + TILE_SIZE // 2
        image = pygame.Surface((TILE_SIZE - 6, TILE_SIZE - 6), pygame.SRCALPHA)
        pygame.draw.circle(
            image,
            (180, 80, 80),
            ((TILE_SIZE - 6) // 2, (TILE_SIZE - 6) // 2),
            (TILE_SIZE - 6) // 2
        )
        super().__init__(x, y, image, self.hp_default)
        self.game_manager = game_manager
        self.path = list(game_manager.map_manager.path_tiles) if hasattr(game_manager, "map_manager") else []
        self.target_idx = 0
        self.slow_timer = 0
        self.slow_ratio = 1.0  # 初始化


    def update(self, dt):
        '''
        if self.slow_timer > 0:
            move_speed = self.speed * 0.4
            self.slow_timer -= dt
        else:
            move_speed = self.speed
        '''
        print(f"Enemy speed: {self.speed}")
        if self.slow_timer > 0:
            move_speed = self.speed * self.slow_ratio
            self.slow_timer -= dt
            if self.slow_timer <= 0:
                self.slow_ratio = 1.0  # 恢復正常速度
        else:
            move_speed = self.speed
            
        if self.target_idx >= len(self.path):
            return
        target_tile = self.path[self.target_idx]
        target_x = target_tile[1] * TILE_SIZE + TILE_SIZE // 2
        target_y = target_tile[0] * TILE_SIZE + TILE_SIZE // 2
        dx, dy = target_x - self.x, target_y - self.y
        dist = (dx * dx + dy * dy) ** 0.5
        if dist < move_speed * dt:
            self.x, self.y = target_x, target_y
            self.target_idx += 1
        else:
            self.x += dx / dist * move_speed * dt
            self.y += dy / dist * move_speed * dt
        self.rect.center = (self.x, self.y)

    def get_hp_percent(self):
        return self.hp / self.max_hp if self.max_hp > 0 else 0

    def draw(self, surface):
        # 畫敵人本體
        surface.blit(self.image, self.rect.topleft)
        # 血條座標與尺寸
        bar_width = self.rect.width
        bar_height = 7
        bar_x = self.rect.x
        bar_y = self.rect.y - 12

        # 血條底
        pygame.draw.rect(surface, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))
        # 血條現值
        percent = max(0, self.hp / self.max_hp)
        pygame.draw.rect(surface, (220, 30, 30), (bar_x, bar_y, int(bar_width * percent), bar_height))

        # 顯示百分比數字
        font = pygame.font.SysFont("Arial", 12)
        percent_txt = font.render(f"{int(percent * 100)}%", True, (255, 255, 255))
        txt_rect = percent_txt.get_rect(center=(self.rect.centerx, bar_y + bar_height // 2))
        surface.blit(percent_txt, txt_rect)

    def take_damage(self, dmg):
        super().take_damage(dmg)
        if self.hp <= 0 and hasattr(self.game_manager, "earn_money"):
            if hasattr(self.game_manager, "audio_manager"):
                self.game_manager.audio_manager.play("enemy_die")
            self.game_manager.earn_money(self.reward)
            self.game_manager.add_score(self.reward)
    
    # base_enemy.py
    def slow(self, slow_ratio, t):

        self.slow_ratio = min(self.slow_ratio, slow_ratio)
        self.slow_timer = max(self.slow_timer, t)

    def get_map_grid_pos(self):
        return (int(self.y) // TILE_SIZE, int(self.x) // TILE_SIZE)
