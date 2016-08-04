import gym
import pdb
#env = gym.make('CartPole-v0')
#env = gym.make('MountainCar-v0')
env = gym.make('Hopper-v1')
#env = gym.make('MsPacman-v0')
env.reset()
#pdb.set_trace()
for _ in range(10000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
