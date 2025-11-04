import pygame
import sys
import random
import time

# 初始化pygame
pygame.init()
pygame.font.init()

# 屏幕设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("键盘盲打练习")

# 颜色定义
BACKGROUND = (30, 30, 45)
TEXT_COLOR = (220, 220, 255)
ACCENT_COLOR = (70, 130, 180)
ERROR_COLOR = (220, 80, 60)
SUCCESS_COLOR = (80, 200, 120)
HIGHLIGHT_COLOR = (100, 150, 200)
PROGRESS_BG = (50, 50, 70)
PROGRESS_FG = (70, 130, 180)

# 字体
title_font = pygame.font.SysFont('SimHei', 36, bold=True)  # 使用中文字体
current_char_font = pygame.font.SysFont('Consolas', 72, bold=True)
stats_font = pygame.font.SysFont('SimHei', 24)
key_font = pygame.font.SysFont('Arial', 16)
feedback_font = pygame.font.SysFont('SimHei', 48, bold=True)

class TypingGame:
    def __init__(self):
        self.reset_game()
        
        # 根据截图设置键盘布局
        self.keyboard_rows = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'BACKSPACE'],
            ['TAB', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'ENTER'],
            ['SHIFT', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'SHIFT']
        ]
        
        self.setup_keyboard()
        
    def reset_game(self):
        self.current_char = '0'  # 初始字符
        self.next_chars = self.generate_chars(20)  # 生成后续字符
        self.correct_count = 0
        self.error_count = 0
        self.start_time = time.time()
        self.current_input = ''
        self.feedback_text = ''
        self.feedback_timer = 0
        self.feedback_color = ERROR_COLOR
        self.progress = 0
        self.total_chars = 10  # 总练习字符数
        
    def generate_chars(self, count):
        """生成随机字符序列"""
        chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return [random.choice(chars) for _ in range(count)]
    
    def setup_keyboard(self):
        """设置键盘布局和位置"""
        self.key_rects = {}
        key_width = 50
        key_height = 50
        start_x = 50
        start_y = HEIGHT - 200
        
        for row_idx, row in enumerate(self.keyboard_rows):
            x = start_x
            y = start_y + row_idx * (key_height + 10)
            
            # 第一行特殊处理（数字行）
            if row_idx == 0:
                x += 50  # 数字行向右偏移
                
            for key in row:
                # 特殊键宽度调整
                width = key_width
                if key in ['BACKSPACE', 'TAB', 'CAPS', 'ENTER', 'SHIFT']:
                    if key == 'BACKSPACE':
                        width = key_width * 2
                    elif key == 'TAB':
                        width = key_width * 1.5
                    elif key == 'CAPS':
                        width = key_width * 1.8
                    elif key == 'ENTER':
                        width = key_width * 2.2
                    elif key == 'SHIFT':
                        width = key_width * 2.5
                
                rect = pygame.Rect(x, y, width, key_height)
                self.key_rects[key] = rect
                x += width + 5
    
    def handle_input(self, key_char):
        """处理键盘输入"""
        current_time = time.time()
        
        # 将输入转换为大写进行比较（不区分大小写）
        input_char = key_char.upper()
        target_char = self.current_char.upper()
        
        if input_char == target_char:
            # 输入正确
            self.correct_count += 1
            self.feedback_text = "✓"
            self.feedback_color = SUCCESS_COLOR
            self.advance_char()
        else:
            # 输入错误
            self.error_count += 1
            self.feedback_text = "X"
            self.feedback_color = ERROR_COLOR
        
        self.feedback_timer = current_time
        self.current_input = key_char
    
    def advance_char(self):
        """前进到下一个字符"""
        if self.next_chars:
            self.current_char = self.next_chars.pop(0)
            self.progress = min(100, (self.correct_count / self.total_chars) * 100)
            
            # 如果字符用完，生成新的
            if len(self.next_chars) < 5:
                self.next_chars.extend(self.generate_chars(10))
    
    def update(self):
        """更新游戏状态"""
        current_time = time.time()
        
        # 清除过期的反馈信息
        if self.feedback_text and current_time - self.feedback_timer > 0.5:
            self.feedback_text = ''
    
    def draw(self, screen):
        """绘制游戏界面"""
        screen.fill(BACKGROUND)
        
        # 绘制标题
        title = title_font.render("键盘盲打练习", True, TEXT_COLOR)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))
        
        # 绘制当前练习字符
        char_text = current_char_font.render(self.current_char, True, HIGHLIGHT_COLOR)
        screen.blit(char_text, (WIDTH // 2 - char_text.get_width() // 2, 120))
        
        # 绘制进度条
        self.draw_progress_bar(screen, 100, 200, WIDTH - 200, 20)
        
        # 绘制统计信息
        elapsed_time = time.time() - self.start_time
        hours = int(elapsed_time) // 3600
        minutes = (int(elapsed_time) % 3600) // 60
        seconds = int(elapsed_time) % 60
        
        time_text = f"{hours}:{minutes:02d}:{seconds:02d}"
        stats_text = f"{time_text} / {self.correct_count} / {self.error_count}"
        stats_surface = stats_font.render(stats_text, True, TEXT_COLOR)
        screen.blit(stats_surface, (WIDTH // 2 - stats_surface.get_width() // 2, 240))
        
        # 绘制反馈信息
        if self.feedback_text:
            feedback = feedback_font.render(self.feedback_text, True, self.feedback_color)
            screen.blit(feedback, (WIDTH // 2 - feedback.get_width() // 2, 280))
        
        # 绘制键盘
        self.draw_keyboard(screen)
        
        # 绘制当前输入提示
        if self.current_input:
            input_text = stats_font.render(f"输入: {self.current_input}", True, ACCENT_COLOR)
            screen.blit(input_text, (WIDTH // 2 - input_text.get_width() // 2, 320))
    
    def draw_progress_bar(self, screen, x, y, width, height):
        """绘制进度条"""
        # 背景
        pygame.draw.rect(screen, PROGRESS_BG, (x, y, width, height), border_radius=10)
        # 进度
        progress_width = int(width * (self.progress / 100))
        if progress_width > 0:
            pygame.draw.rect(screen, PROGRESS_FG, (x, y, progress_width, height), border_radius=10)
        # 边框
        pygame.draw.rect(screen, TEXT_COLOR, (x, y, width, height), 2, border_radius=10)
        
        # 进度文本
        progress_text = stats_font.render(f"{int(self.progress)}%", True, TEXT_COLOR)
        screen.blit(progress_text, (x + width + 10, y))
    
    def draw_keyboard(self, screen):
        """绘制键盘"""
        keyboard_bg = pygame.Rect(40, HEIGHT - 250, WIDTH - 80, 220)
        pygame.draw.rect(screen, (40, 40, 60), keyboard_bg, border_radius=10)
        
        # 绘制每个键
        for key, rect in self.key_rects.items():
            # 高亮当前需要按的键
            is_target = (key.upper() == self.current_char.upper())
            color = HIGHLIGHT_COLOR if is_target else (60, 60, 80)
            
            pygame.draw.rect(screen, color, rect, border_radius=5)
            pygame.draw.rect(screen, TEXT_COLOR, rect, 1, border_radius=5)
            
            # 绘制键标签
            key_label = key_font.render(key, True, TEXT_COLOR)
            label_x = rect.x + (rect.width - key_label.get_width()) // 2
            label_y = rect.y + (rect.height - key_label.get_height()) // 2
            screen.blit(key_label, (label_x, label_y))

# 创建游戏实例
game = TypingGame()

# 键盘映射（将pygame键值映射到字符）
KEY_MAPPING = {
    pygame.K_1: '1', pygame.K_2: '2', pygame.K_3: '3', pygame.K_4: '4', pygame.K_5: '5',
    pygame.K_6: '6', pygame.K_7: '7', pygame.K_8: '8', pygame.K_9: '9', pygame.K_0: '0',
    pygame.K_MINUS: '-', pygame.K_EQUALS: '=',
    pygame.K_q: 'Q', pygame.K_w: 'W', pygame.K_e: 'E', pygame.K_r: 'R', pygame.K_t: 'T',
    pygame.K_y: 'Y', pygame.K_u: 'U', pygame.K_i: 'I', pygame.K_o: 'O', pygame.K_p: 'P',
    pygame.K_a: 'A', pygame.K_s: 'S', pygame.K_d: 'D', pygame.K_f: 'F', pygame.K_g: 'G',
    pygame.K_h: 'H', pygame.K_j: 'J', pygame.K_k: 'K', pygame.K_l: 'L', pygame.K_SEMICOLON: ';',
    pygame.K_QUOTE: "'", pygame.K_z: 'Z', pygame.K_x: 'X', pygame.K_c: 'C', pygame.K_v: 'V',
    pygame.K_b: 'B', pygame.K_n: 'N', pygame.K_m: 'M', pygame.K_COMMA: ',', pygame.K_PERIOD: '.',
    pygame.K_SLASH: '/', pygame.K_BACKSLASH: '\\', pygame.K_LEFTBRACKET: '[', pygame.K_RIGHTBRACKET: ']'
}

# 游戏主循环
clock = pygame.time.Clock()
running = True

print("游戏已启动！按对应键位进行练习...")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            # 处理退出键
            if event.key == pygame.K_ESCAPE:
                running = False
            
            # 处理重置键
            elif event.key == pygame.K_r and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                game.reset_game()
                print("游戏已重置！")
            
            # 处理普通按键输入
            elif event.key in KEY_MAPPING:
                key_char = KEY_MAPPING[event.key]
                game.handle_input(key_char)
                print(f"检测到按键: {key_char}")
            
            else:
                print(f"未映射的按键: {event.key}")
    
    # 更新游戏状态
    game.update()
    
    # 绘制游戏
    game.draw(screen)
    
    # 更新屏幕
    pygame.display.flip()
    
    # 控制帧率
    clock.tick(60)

pygame.quit()
sys.exit()