__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
from .. import constants as c
from . import flashing_coin


class Character(pg.sprite.Sprite):
    """Parent class for all characters used for the overhead level info"""
    def __init__(self, image):
        super(Character, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()


class OverheadInfo(object):
    """Class for level information like score, coin total,
        and time remaining"""
    def __init__(self, game_info, state):
        self.sprite_sheet = setup.GFX['text_images']
        self.coin_total = game_info[c.COIN_TOTAL]
        self.time = 401
        self.current_time = 0
        self.total_lives = game_info[c.LIVES]
        self.top_score = game_info[c.TOP_SCORE]
        self.state = state
        self.special_state = None
        self.game_info = game_info
        self.player_name = setup.player_name
        
        self.font_path = "Iansui-Regular.ttf"  # 字型檔案路徑
        self.font = pg.font.Font(self.font_path, 24)  # 設定字型大小 30
        self.create_image_dict()
        self.create_score_group()
        self.create_info_labels()
        self.create_load_screen_labels()
        self.create_countdown_clock()
        self.create_coin_counter()
        self.create_flashing_coin()
        self.create_mario_image()
        self.create_game_over_label()
        self.create_time_out_label()
        self.create_main_menu_labels()
        


    def create_image_dict(self):
        """Creates the initial images for the score"""
        self.image_dict = {}
        image_list = []

        image_list.append(self.get_image(3, 230, 7, 7))
        image_list.append(self.get_image(12, 230, 7, 7))
        image_list.append(self.get_image(19, 230, 7, 7))
        image_list.append(self.get_image(27, 230, 7, 7))
        image_list.append(self.get_image(35, 230, 7, 7))
        image_list.append(self.get_image(43, 230, 7, 7))
        image_list.append(self.get_image(51, 230, 7, 7))
        image_list.append(self.get_image(59, 230, 7, 7))
        image_list.append(self.get_image(67, 230, 7, 7))
        image_list.append(self.get_image(75, 230, 7, 7))

        image_list.append(self.get_image(83, 230, 7, 7))
        image_list.append(self.get_image(91, 230, 7, 7))
        image_list.append(self.get_image(99, 230, 7, 7))
        image_list.append(self.get_image(107, 230, 7, 7))
        image_list.append(self.get_image(115, 230, 7, 7))
        image_list.append(self.get_image(123, 230, 7, 7))
        image_list.append(self.get_image(3, 238, 7, 7))
        image_list.append(self.get_image(11, 238, 7, 7))
        image_list.append(self.get_image(20, 238, 7, 7))
        image_list.append(self.get_image(27, 238, 7, 7))
        image_list.append(self.get_image(35, 238, 7, 7))
        image_list.append(self.get_image(44, 238, 7, 7))
        image_list.append(self.get_image(51, 238, 7, 7))
        image_list.append(self.get_image(59, 238, 7, 7))
        image_list.append(self.get_image(67, 238, 7, 7))
        image_list.append(self.get_image(75, 238, 7, 7))
        image_list.append(self.get_image(83, 238, 7, 7))
        image_list.append(self.get_image(91, 238, 7, 7))
        image_list.append(self.get_image(99, 238, 7, 7))
        image_list.append(self.get_image(108, 238, 7, 7))
        image_list.append(self.get_image(115, 238, 7, 7))
        image_list.append(self.get_image(123, 238, 7, 7))
        image_list.append(self.get_image(3, 246, 7, 7))
        image_list.append(self.get_image(11, 246, 7, 7))
        image_list.append(self.get_image(20, 246, 7, 7))
        image_list.append(self.get_image(27, 246, 7, 7))
        image_list.append(self.get_image(48, 248, 7, 7))

        image_list.append(self.get_image(68, 249, 6, 2))
        image_list.append(self.get_image(75, 247, 6, 6))



        character_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*'

        for character, image in zip(character_string, image_list):
            self.image_dict[character] = image


    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((92, 148, 252))
        image = pg.transform.scale(image,
                                   (int(rect.width*2.9),
                                    int(rect.height*2.9)))
        return image


    def create_score_group(self):
        """Creates the initial empty score (000000)"""
        self.score_images = []
        self.create_label(self.score_images, '000000', 75, 55)


    def create_info_labels(self):
        """Creates the labels that describe each info"""
        self.mario_label = []
        self.world_label = []
        self.time_label = []
        self.stage_label = []


        self.create_label(self.mario_label, self.player_name.upper() , 75, 30)
        self.create_label(self.world_label, 'WORLD', 450, 30)
        self.create_label(self.time_label, 'TIME', 625, 30)
        self.create_label(self.stage_label, '1-1', 472, 55)

        self.label_list = [self.mario_label,
                           self.world_label,
                           self.time_label,
                           self.stage_label]


    def create_load_screen_labels(self):
        """Creates labels for the center info of a load screen"""
        world_label = []
        number_label = []

        self.create_label(world_label, 'WORLD', 280, 200)
        self.create_label(number_label, '1-1', 430, 200)

        self.center_labels = [world_label, number_label]


    def create_countdown_clock(self):
        """Creates the count down clock for the level"""
        self.count_down_images = []
        self.create_label(self.count_down_images, str(self.time), 645, 55)


    def create_label(self, label_list, string, x, y):
        """Creates a label (WORLD, TIME, MARIO)"""
        # 渲染整個字串，而非單個字母
        text_surface = self.font.render(string, True, (255, 255, 255))  # 白色文字
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)

        # 將整個文字渲染為單一物件，並存入 label_list
        label_list.clear()
        label_list.append(Character(text_surface))
        label_list[0].rect = text_rect


    def set_label_rects(self, label_list, x, y):
        """Set the location of each individual character"""
        for i, letter in enumerate(label_list):
            letter.rect.x = x + ((letter.rect.width + 3) * i)
            letter.rect.y = y
            if letter.image == self.image_dict['-']:
                letter.rect.y += 7
                letter.rect.x += 2


    def create_coin_counter(self):
        """Creates the info that tracks the number of coins Mario collects"""
        self.coin_count_images = []
        self.create_label(self.coin_count_images, '*00', 300, 55)


    def create_flashing_coin(self):
        """Creates the flashing coin next to the coin total"""
        self.flashing_coin = flashing_coin.Coin(280, 53)


    def create_mario_image(self):
        """Get the mario image"""
        self.life_times_image = self.get_image(75, 247, 6, 6)
        self.life_times_rect = self.life_times_image.get_rect(center=(378, 295))
        self.life_total_label = []
        self.create_label(self.life_total_label, str(self.total_lives),
                          450, 285)

        self.sprite_sheet = setup.GFX['mario_bros']
        self.mario_image = self.get_image(178, 32, 12, 16)
        self.mario_rect = self.mario_image.get_rect(center=(320, 290))


    def create_game_over_label(self):
        """Create the label for the GAME OVER screen"""
        game_label = []
        over_label = []

        self.create_label(game_label, 'GAME', 280, 300)
        self.create_label(over_label, 'OVER', 400, 300)

        self.game_over_label = [game_label, over_label]


    def create_time_out_label(self):
        """Create the label for the time out screen"""
        time_out_label = []

        self.create_label(time_out_label, 'TIME OUT', 290, 310)
        self.time_out_label = [time_out_label]


    def create_main_menu_labels(self):
        """Create labels for the MAIN MENU screen"""
        player_one_game = []
        player_two_game = []
        scoreboard = []

        self.create_label(player_one_game, '開始遊戲', 350, 360)
        self.create_label(player_two_game, '修改名稱', 350, 403)
        self.create_label(scoreboard, '查看排名', 350, 448)

        self.main_menu_labels = [player_one_game, player_two_game, scoreboard ]


    def update(self, level_info, mario=None):
        """Updates all overhead info"""
        self.mario = mario
        self.handle_level_state(level_info)
        self.player_name = setup.player_name


    def handle_level_state(self, level_info):
        """Updates info based on what state the game is in"""
        if self.state == c.MAIN_MENU:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)
            self.flashing_coin.update(level_info[c.CURRENT_TIME])

        elif self.state == c.LOAD_SCREEN:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)

        elif self.state == c.LEVEL:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            if level_info[c.LEVEL_STATE] != c.FROZEN \
                    and self.mario.state != c.WALKING_TO_CASTLE \
                    and self.mario.state != c.END_OF_LEVEL_FALL \
                    and not self.mario.dead:
                self.update_count_down_clock(level_info)
            self.update_coin_total(level_info)
            self.flashing_coin.update(level_info[c.CURRENT_TIME])

        elif self.state == c.TIME_OUT:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)

        elif self.state == c.GAME_OVER:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)

        elif self.state == c.FAST_COUNT_DOWN:
            level_info[c.SCORE] += 50
            self.score = level_info[c.SCORE]
            self.update_count_down_clock(level_info)
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)
            self.flashing_coin.update(level_info[c.CURRENT_TIME])
            if self.time == 0:
                self.state = c.END_OF_LEVEL

        elif self.state == c.END_OF_LEVEL:
            self.flashing_coin.update(level_info[c.CURRENT_TIME])


    def update_score_images(self, images, score, x=75, y=55):
        """Updates the score display using the TTF font."""
        # 確保分數字串為 6 位數，不足補 0
        score_str = str(score).zfill(6)
        
        # 確保 images 長度足夠，如果不足就補充
        while len(images) < len(score_str):
            images.append(Character(self.font.render('0', True, (255, 255, 255))))

        # 渲染並更新每個數字的位置
        for index, digit in enumerate(score_str):
            text_surface = self.font.render(digit, True, (255, 255, 255))  # 渲染單個數字
            text_rect = text_surface.get_rect(topleft=(x + index * 15, y))  # 每個字的 x 間隔 15 像素
            
            images[index].image = text_surface
            images[index].rect = text_rect

        # 移除多餘的元素（如果有）
        if len(images) > len(score_str):
            images[:] = images[:len(score_str)]


    def update_count_down_clock(self, level_info):
        """Updates the countdown clock display using the TTF font."""
        if self.state == c.FAST_COUNT_DOWN:
            self.time -= 1
        elif (level_info[c.CURRENT_TIME] - self.current_time) > 400:
            self.current_time = level_info[c.CURRENT_TIME]
            self.time -= 1

        # 渲染倒數時間為整串字串
        time_str = str(self.time).zfill(3)  # 倒數時間至少 3 位數
        text_surface = self.font.render(time_str, True, (255, 255, 255))  # 白色文字
        text_rect = text_surface.get_rect(topleft=(645, 55))

        # 清空舊的倒數圖像，加入新的渲染結果
        self.count_down_images.clear()
        self.count_down_images.append(Character(text_surface))
        self.count_down_images[0].rect = text_rect



    def update_coin_total(self, level_info):
        """Updates the coin total and adjusts label accordingly"""
        self.coin_total = level_info[c.COIN_TOTAL]

        coin_string = str(self.coin_total)
        if len(coin_string) < 2:
            coin_string = '*0' + coin_string
        elif len(coin_string) > 2:
            coin_string = '*00'
        else:
            coin_string = '*' + coin_string

        x = self.coin_count_images[0].rect.x
        y = self.coin_count_images[0].rect.y

        self.coin_count_images = []

        self.create_label(self.coin_count_images, coin_string, x, y)


    def draw(self, surface):
        """Draws overhead info based on state"""
        if self.state == c.MAIN_MENU:
            self.draw_main_menu_info(surface)
        elif self.state == c.LOAD_SCREEN:
            self.draw_loading_screen_info(surface)
        elif self.state == c.LEVEL:
            self.draw_level_screen_info(surface)
        elif self.state == c.GAME_OVER:
            self.draw_game_over_screen_info(surface)
        elif self.state == c.FAST_COUNT_DOWN:
            self.draw_level_screen_info(surface)
        elif self.state == c.END_OF_LEVEL:
            self.draw_level_screen_info(surface)
        elif self.state == c.TIME_OUT:
            self.draw_time_out_screen_info(surface)
        else:
            pass



    def draw_main_menu_info(self, surface):
        """Draws info for main menu"""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for label in self.main_menu_labels:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)


    def draw_loading_screen_info(self, surface):
        """Draws info for loading screen"""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.center_labels:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for word in self.life_total_label:
            surface.blit(word.image, word.rect)

        surface.blit(self.mario_image, self.mario_rect)
        surface.blit(self.life_times_image, self.life_times_rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)


    def draw_level_screen_info(self, surface):
        """Draws info during regular game play"""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for digit in self.count_down_images:
                surface.blit(digit.image, digit.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)


    def draw_game_over_screen_info(self, surface):
        """Draws info when game over"""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.game_over_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)


    def draw_time_out_screen_info(self, surface):
        """Draws info when on the time out screen"""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.time_out_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)









