import json
import os
import pygame as pg
from .. import setup
from .. import constants as c


class Digit(pg.sprite.Sprite):
    """Individual digit for score"""
    def __init__(self, image):
        super(Digit, self).__init__()
        self.image = image
        self.rect = image.get_rect()


import json
import os
import pygame as pg
from .. import setup
from .. import constants as c


class Score:
    """Score display and ranking update class."""
    def __init__(self, x, y, score, flag_pole=False):
        self.x = x
        self.y = y
        self.final_score = int(score)  # Store the final score
        self.flag_pole_score = flag_pole

        # Load custom font
        self.font_path = "Iansui-Regular.ttf"  # Replace with your font file path
        self.font_size = 30  # Adjust font size
        self.font = pg.font.Font(self.font_path, self.font_size)

        # Convert the score to a string for rendering
        self.score_string = str(score)
        self.rendered_score = self.font.render(self.score_string, True, (255, 255, 255))  # White color

        # Vertical speed for floating score
        self.y_vel = -4 if flag_pole else -3

    def update(self, score_list, level_info):
        """Update the score movement (if floating)."""
        if self.flag_pole_score:
            self.y += self.y_vel
            if self.y <= 120:
                self.y_vel = 0

        # Update rendered position
        self.rendered_score = self.font.render(self.score_string, True, (255, 255, 255))

        # Check for score list cleanup (for floating scores)
        if score_list:
            self.check_to_delete_floating_scores(score_list, level_info)

    def draw(self, screen):
        """Draw the score at the specified position."""
        screen.blit(self.rendered_score, (self.x, self.y))

    def check_to_delete_floating_scores(self, score_list, level_info):
        """Check if floating scores need to be deleted."""
        for i, score in enumerate(score_list):
            if int(score.score_string) == 1000:
                if (score.y - score.y_vel) > 130:
                    score_list.pop(i)
            else:
                if (score.y - score.y_vel) > 75:
                    score_list.pop(i)

    def update_rankings(self):
        """Update the rankings in score.json with the current score."""
        score_file = "score.json"
        if not os.path.exists(score_file):
            print("score.json 不存在，無法更新分數。")
            return

        # Read score.json
        with open(score_file, "r") as file:
            scores = json.load(file)

        # Extract current scores
        score1 = int(scores["score1"])
        score2 = int(scores["score2"])
        score3 = int(scores["score3"])

        # Update rankings based on the new score
        if self.final_score > score1:  # Higher than score1
            scores["player3"], scores["score3"] = scores["player2"], scores["score2"]
            scores["player2"], scores["score2"] = scores["player1"], scores["score1"]
            scores["player1"], scores["score1"] = setup.player_name, str(self.final_score)

        elif self.final_score > score2:  # Higher than score2
            scores["player3"], scores["score3"] = scores["player2"], scores["score2"]
            scores["player2"], scores["score2"] = setup.player_name, str(self.final_score)

        elif self.final_score > score3:  # Higher than score3
            scores["player3"], scores["score3"] = setup.player_name, str(self.final_score)

        # Write updated scores back to score.json
        with open(score_file, "w") as file:
            json.dump(scores, file, indent=4)

        print("分數更新完成！")
