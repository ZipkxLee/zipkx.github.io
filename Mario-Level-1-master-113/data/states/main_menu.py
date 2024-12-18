__author__ = 'justinarmstrong'

import pygame as pg
import tkinter as tk
from tkinter import simpledialog
import json
from .. import setup, tools
from .. import constants as c
from ..components import info, mario


class Menu(tools._State):
    def __init__(self):
        """Initializes the state"""
        tools._State.__init__(self)
        persist = {c.COIN_TOTAL: 0,
                   c.SCORE: 0,
                   c.LIVES: 3,
                   c.TOP_SCORE: 0,
                   c.CURRENT_TIME: 0.0,
                   c.LEVEL_STATE: None,
                   c.CAMERA_START_X: 0,
                   c.MARIO_DEAD: False}
        self.startup(0.0, persist)

    def startup(self, current_time, persist):
        """Called every time the game's state becomes this one. Initializes
        certain values"""
        self.next = c.LOAD_SCREEN
        self.persist = persist
        self.game_info = persist
        self.overhead_info = info.OverheadInfo(self.game_info, c.MAIN_MENU)

        self.sprite_sheet = setup.GFX['title_screen']
        self.setup_background()
        self.setup_mario()
        self.setup_cursor()

    def setup_cursor(self):
        """Creates the mushroom cursor to select 1, 2, or new options"""
        self.cursor = pg.sprite.Sprite()
        dest = (300, 358)
        self.cursor.image, self.cursor.rect = self.get_image(
            24, 160, 8, 8, dest, setup.GFX['item_objects'])
        self.cursor.state = c.PLAYER1

    def setup_mario(self):
        """Places Mario at the beginning of the level"""
        self.mario = mario.Mario()
        self.mario.rect.x = 110
        self.mario.rect.bottom = c.GROUND_HEIGHT

    def setup_background(self):
        """Setup the background image to blit"""
        self.background = setup.GFX['level_1']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(
            self.background,
            (int(self.background_rect.width * c.BACKGROUND_MULTIPLER),
             int(self.background_rect.height * c.BACKGROUND_MULTIPLER))
        )
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

        self.image_dict = {}
        self.image_dict['GAME_NAME_BOX'] = self.get_image(
            1, 60, 176, 88, (170, 100), setup.GFX['title_screen'])

    def get_image(self, x, y, width, height, dest, sprite_sheet):
        """Returns images and rects to blit onto the screen"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(sprite_sheet, (0, 0), (x, y, width, height))
        if sprite_sheet == setup.GFX['title_screen']:
            image.set_colorkey((255, 0, 220))
            image = pg.transform.scale(
                image,
                (int(rect.width * c.SIZE_MULTIPLIER),
                 int(rect.height * c.SIZE_MULTIPLIER))
            )
        else:
            image.set_colorkey(c.BLACK)
            image = pg.transform.scale(
                image,
                (int(rect.width * 3),
                 int(rect.height * 3))
            )

        rect = image.get_rect()
        rect.x = dest[0]
        rect.y = dest[1]
        return (image, rect)

    def update(self, surface, keys, current_time):
        """Updates the state every refresh"""
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = self.current_time
        self.update_cursor(keys, surface)
        self.overhead_info.update(self.game_info)

        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(self.image_dict['GAME_NAME_BOX'][0],
                     self.image_dict['GAME_NAME_BOX'][1])
        surface.blit(self.mario.image, self.mario.rect)
        surface.blit(self.cursor.image, self.cursor.rect)
        self.overhead_info.draw(surface)

    def update_cursor(self, keys, surface):
        """Update the position of the cursor"""
        input_list = [pg.K_RETURN, pg.K_a, pg.K_s]

        if self.cursor.state == c.PLAYER1:
            self.cursor.rect.y = 358
            if keys[pg.K_DOWN]:
                self.cursor.state = "INPUT_NAME"
            for input in input_list:
                if keys[input]:
                    self.reset_game_info()
                    self.done = True
        elif self.cursor.state == "INPUT_NAME":
            self.cursor.rect.y = 403
            if keys[pg.K_DOWN]:
                self.cursor.state = "VIEW_RANK"
            if keys[pg.K_UP]:
                self.cursor.state = c.PLAYER1
            if keys[pg.K_RETURN]:
                self.show_input_box()
        elif self.cursor.state == "VIEW_RANK":
            self.cursor.rect.y = 448
            if keys[pg.K_UP]:
                self.cursor.state = "INPUT_NAME"
            if keys[pg.K_RETURN]:
                self.show_rankings(surface)

    def show_input_box(self):
        """Displays a tkinter input box to input the player name"""
        root = tk.Tk()
        root.withdraw()  # 隱藏 tkinter 主視窗
        player_name = simpledialog.askstring("輸入角色名稱", "請輸入您的角色名稱：")
        if not player_name:
            player_name = "未命名角色"  # 預設名稱
        setup.player_name = player_name  # 儲存到全域變數
        root.destroy()
        self.overhead_info = info.OverheadInfo(self.game_info, c.MAIN_MENU)

    def show_rankings(self, surface):
        """Displays the top 3 rankings from a JSON file"""
        try:
            with open("score.json", "r") as file:
                scores = json.load(file)

            # 創建一個半透明的矩形作為背景
            ranking_bg = pg.Surface((400, 300))  # 排行榜背景尺寸
            ranking_bg.fill((0, 0, 0))  # 黑色背景
            ranking_bg.set_alpha(200)  # 半透明效果
            bg_rect = ranking_bg.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))

            # 設置字體
            font = pg.font.Font("Iansui-Regular.ttf", 20)  # 普通字體大小
            title_font = pg.font.Font("Iansui-Regular.ttf", 24)  # 標題字體大小

            # 監控排行榜的狀態
            showing_rankings = True  # 排行榜顯示狀態

            while showing_rankings:
                # 塗黑畫面並繪製排行榜背景
                surface.fill((15, 15, 15))
                surface.blit(ranking_bg, bg_rect)

                # 繪製標題
                title_text = title_font.render("排行榜 - 前三名", True, (255, 255, 255))
                title_rect = title_text.get_rect(center=(surface.get_width() // 2, bg_rect.y + 30))
                surface.blit(title_text, title_rect)

                # 繪製每個排名的玩家名稱和分數
                for i in range(1, 4):
                    rank_text = font.render(
                        f"排名 {i}: {scores[f'player{i}']} - 分數: {scores[f'score{i}']}",
                        True,
                        (255, 255, 255),
                    )
                    rank_rect = rank_text.get_rect(center=(surface.get_width() // 2, bg_rect.y + 70 + (i * 40)))
                    surface.blit(rank_text, rank_rect)

                # 更新畫面
                pg.display.flip()

                # 檢測事件
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        # 如果玩家關閉窗口
                        showing_rankings = False
                        self.done = True
                        self.next = None
                    elif event.type == pg.KEYDOWN:
                        # 如果按下 ESC 鍵，關閉排行榜
                        if event.key == pg.K_RETURN:
                            showing_rankings = False
            self.cursor.state = "INPUT_NAME"
        except FileNotFoundError:
            print("找不到 score.json 檔案！")


    def reset_game_info(self):
        """Resets the game info in case of a Game Over and restart"""
        self.game_info[c.COIN_TOTAL] = 0
        self.game_info[c.SCORE] = 0
        self.game_info[c.LIVES] = 3
        self.game_info[c.CURRENT_TIME] = 0.0
        self.game_info[c.LEVEL_STATE] = None
        self.persist = self.game_info