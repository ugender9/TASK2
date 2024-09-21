Step 1: Setting Up Your Environment
Before you start, make sure you have Python installed on your machine. You will also need to install a few packages, primarily gym, an open-source library provided by OpenAI that offers various environments to test and develop RL algorithms.

pip install gym

Step 2: Importing Libraries
After installing gym, you can start by importing it along with other necessary libraries:

import gym

import numpy as np

Step 3: Creating the Environment
One of the basic gym environments is the "CartPole-v1," where the goal is to keep a pole balanced on a cart by moving the cart left or right.

env = gym.make('CartPole-v1')

Step 4: Implementing a Simple Agent
We’ll implement a very basic RL agent that randomly decides to move left or right without any learning involved to demonstrate the interaction with the environment.

for episode in range(5):  # Run 5 episodes

    state = env.reset()  # Reset the environment for a new episode

    done = False

    step_count = 0    

    while not done:

        env.render()  # Render the environment to visualize the cart and pole

        action = env.action_space.sample()  # Randomly pick an action (0 or 1)

        state, reward, done, info = env.step(action)  # Execute the action

        step_count += 1        

        if done:

            print(f"Episode {episode + 1} finished after {step_count} steps.")

            break

env.close()  # Close the environment

Step 5: Adding Learning
To make this reinforcement learning example into a learning agent, you would typically incorporate an RL algorithm like Q-learning, Deep Q-Networks (DQN), or policy gradients. These algorithms help the agent to learn from the outcomes of its actions rather than making random decisions.
