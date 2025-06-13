import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gym
from gym import spaces
import numpy as np
from Game import main
import pygame

total_reward = 0

class PacAIEnv(gym.Env):
    def __init__(self,render=True):
        super(PacAIEnv, self).__init__()
        self.rendering = render
        self.action_space = spaces.Discrete(4)  # 0 = right, 1 = up, 2 = left, 3 = down
        self.observation_space = spaces.Box(low=0.0, high=1.0, shape=(6,), dtype=np.float32)

    def reset(self):
        obs = main.reset_game()
        return obs

    def step(self, action):
        global total_reward
        main.step_game(action)
        obs = main.get_observation()
        reward = main.get_reward()
        total_reward += reward
        done = main.is_done()
        info = {}
        return obs, reward, done, info
    
    def render(self):
        if self.rendering:
            main.refresh_screen()

    def close(self):
        # Chiudi Pygame
        pygame.quit()