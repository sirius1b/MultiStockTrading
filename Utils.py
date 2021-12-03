import numpy as np
import pandas as pd
from finrl.neo_finrl.env_stock_trading.env_stocktrading import StockTradingEnv
from stable_baselines3 import TD3, SAC, PPO
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.noise import (
    NormalActionNoise,
        OrnsteinUhlenbeckActionNoise,
)
from stable_baselines3.common.vec_env import DummyVecEnv
Alg = {'td3': TD3, 'sac': SAC, 'ppo': PPO}

class Agent:
    def __init__ (self, env):
        self.env = env
        self.agent = None

    def specify_model(self,
            model,
            policy = 'MlpPolicy',
            policy_kwargs = None,
            model_kwargs = None,
            verbose = 1):
        if model.lower() not in Alg.keys():
            print("Choose appropriate algorithm")
            print(Alg.keys())
            raise Exception("Unknown Algorithm")
            
        agent = Alg[model.lower()](policy = policy, 
                env = self.env, 
                verbose = verbose,
                policy_kwargs = policy_kwargs,
                **model_kwargs)
        self.agent = agent

    def train(self, tb_log_name, total_timesteps = int(1e5)):
        self.agent.learn( total_timesteps= total_timesteps, 
                            tb_log_name = tb_log_name)
    def get_agent(self):
        return self.agent

    def prediction_custom_env(self, env):
        test_env, obs = env.get_sb_env()
        account_memory = []
        actions_memory = []
        test_env.reset()
        for i in range(len(environment.df.index.unique())):
            actions, _states = self.agent.predict(obs)
            new_obs, rewards, dones, info = test_env.step(action)
            if i == (len(environment.df.index.unique()) - 2):
                account_memory = test_env.env_method(method_name = 'save_asset_memory') 
                actions_memory = test_env.env_method(method_name = 'save_action_memory')
            if dones[0]:
                print('hit end!')
                break
        return account_memory, actioins_memory
