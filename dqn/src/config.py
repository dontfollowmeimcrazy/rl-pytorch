"""
Written by Matteo Dunnhofer - 2018

Configuration class
"""
import math
import torch
from torch.autograd import Variable


class Configuration(object):
    """
    Class defining all the hyper parameters of:
        - net architecture
        - training
        - test
        - dataset path
        ...
    """
    PROJECT_NAME = 'DQN'

    ENV = 'CartPole' #PongDeterministic-v4'
    EXPERIMENTS_PATH = '../experiments'

    # training hyperparameters
    OBSERVATION_SIZE = [80, 80]

    SEED = 123
    LEARNING_RATE = 1e-5
    BATCH_SIZE = 32
    DECAY_LR = False
    DECAY_LR_STEPS = [500]
    OPTIM = 'adam'
    MOMENTUM = 0.95
    MAX_EPISODES = 100000
    GAMMA = 0.999
    
    EPS_START = 0.9 #0.9
    EPS_END = 0.05 #0.1
    EPS_DECAY = 10000 #5e5
    TARGET_UPDATE = 100
    EXPERIENCE_REPLAY_SIZE = 10000
    TRAIN_START = 1000
    ATARI_STATE_STACK_N = 4

    NUM_ACTIONS = 2 #4
    
    USE_GPU = True
    GPU_IDS = [0] #[0, 1, 2]

    RENDER = False
    DISPLAY_STEP = 100
    SAVE_STEP = 100

    def __init__(self):
        super(Configuration, self).__init__()

    def __str__(self):
        cfg2str = "Configuration parameters\n"
        cfg2str += "PROJECT_NAME = " + str(self.PROJECT_NAME) + '\n'
        cfg2str += "ENV = " + str(self.ENV) + '\n'
        cfg2str += "SEED = " + str(self.SEED) + '\n'
        cfg2str += "LEARNING_RATE = " + str(self.LEARNING_RATE) + '\n'
        cfg2str += "BATCH_SIZE = " + str(self.BATCH_SIZE) + '\n'
        cfg2str += "DECAY_LR = " + str(self.DECAY_LR) + '\n'
        cfg2str += "DECAY_LR_STEPS = " + str(self.DECAY_LR_STEPS) + '\n'
        cfg2str += "OPTIM = " + str(self.OPTIM) + '\n'
        cfg2str += "MOMENTUM = " + str(self.MOMENTUM) + '\n'
        cfg2str += "MAX_EPISODES = " + str(self.MAX_EPISODES) + '\n'
        cfg2str += "NUM_ACTIONS = " + str(self.NUM_ACTIONS) + '\n'
        cfg2str += "GAMMA = " + str(self.GAMMA) + '\n'
        cfg2str += "EPS_START = " + str(self.EPS_START) + '\n'
        cfg2str += "EPS_END = " + str(self.EPS_END) + '\n'
        cfg2str += "EPS_DECAY = " + str(self.EPS_DECAY) + '\n'
        cfg2str += "TARGET_UPDATE = " + str(self.TARGET_UPDATE) + '\n'
        cfg2str += "TRAIN_START = " + str(self.TRAIN_START) + '\n'
        cfg2str += "ATARI_STATE_STACK_N = " + str(self.ATARI_STATE_STACK_N) + '\n'
        cfg2str += "OBSERVATION_SIZE = " + str(self.OBSERVATION_SIZE) + '\n'
        cfg2str += "RENDER = " + str(self.RENDER) + '\n'
        cfg2str += "DISPLAY_STEP = " + str(self.DISPLAY_STEP) + '\n'
        cfg2str += "SAVE_STEP = " + str(self.SAVE_STEP) + '\n'
        cfg2str += "EXPERIMENTS_PATH = " + str(self.EXPERIMENTS_PATH) + '\n'
        cfg2str += "USE_GPU = " + str(self.USE_GPU) + '\n'
        cfg2str += "GPU_IDS = " + str(self.GPU_IDS) + '\n'

        return cfg2str
