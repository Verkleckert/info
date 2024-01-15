import random
import numpy as np
import tensorflow as tf
from tensorflow import keras

class ConnectFour:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)
        self.current_player = 1

    def display_board(self):
        for row in self.board:
            print("|", end="")
            for col in row:
                if col == 0:
                    print(" ", end="|")
                elif col == 1:
                    print("X", end="|")
                elif col == 2:
                    print("O", end="|")
            print("\n" + "-" * (self.cols * 2 + 1))

    def drop_piece(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player
                return True
        return False

    def is_winner(self, player):
        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True

        # Check vertical
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True

        # Check diagonals
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True
                if all(self.board[row + 3 - i][col + i] == player for i in range(4)):
                    return True

        return False

    def is_board_full(self):
        return np.all(self.board != 0)

    def switch_player(self):
        self.current_player = 3 - self.current_player  # Switches between player 1 and 2

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []  # Experience replay memory
        self.gamma = 0.95  # Discount factor
        self.epsilon = 1.0  # Exploration-exploitation trade-off
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01
        self.model = self._build_model()
    
    def save_model(self, filename='./spiele/models/dqn_model.h5'):
        self.model.save(filename)

    def load_model(self, filename='./spiele/models/dqn_model.h5'):
        self.model = keras.models.load_model(filename)

    def _build_model(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(64, input_dim=self.state_size, activation='relu'))
        model.add(keras.layers.Dense(64, activation='relu'))
        model.add(keras.layers.Dense(self.action_size, activation='linear'))
        model.compile(optimizer='adam', loss='mse')
        return model

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return np.random.choice(self.action_size)
        q_values = self.model.predict(np.reshape(state, (1, self.state_size)))
        return np.argmax(q_values[0])

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        if len(self.memory) < batch_size:
            return

        minibatch = random.sample(self.memory, batch_size)
        states, targets = [], []

        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(np.reshape(next_state, (1, self.state_size))))
            target_f = self.model.predict(np.reshape(state, (1, self.state_size)))
            target_f[0][action] = target


            states.append(state)
            targets.append(np.squeeze(target_f))
        
        self.model.fit(np.array(states), np.array(targets), epochs=1, verbose=0)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

            
def state_to_input(state):
    return np.reshape(state, (1, -1))

def play_connect_four_dqn(agent1, agent2):
    game = ConnectFour()

    for episode in range(1000):  # You may adjust the number of episodes
        print("")
        print("")
        print(f"Episode: {episode}")
        print("")
        print("")
        state = game.board.flatten()
        for _ in range(game.rows * game.cols):
            if game.current_player == 1:
                action = agent1.act(state)
            else:
                action = agent2.act(state)

            col = action

            if 0 <= col < game.cols and game.drop_piece(col):
                next_state = game.board.flatten()
                reward = 1 if game.is_winner(game.current_player) else 0
                done = game.is_board_full() or reward == 1

                if game.current_player == 1:
                    agent1.remember(state, action, reward, next_state, done)
                    agent1.replay(batch_size=32)
                else:
                    agent2.remember(state, action, reward, next_state, done)
                    agent2.replay(batch_size=32)

                state = next_state

                if done:
                    if game.current_player == 1:
                        agent1.remember(state, action, reward, next_state, done)
                        agent1.replay(batch_size=32)
                    else:
                        agent2.remember(state, action, reward, next_state, done)
                        agent2.replay(batch_size=32)

                    state = next_state

                    if done:
                        game = ConnectFour()

                        if episode % 10 == 0:
                            # Save models every 10 episodes
                            agent1.save_model(f'agent1_model_episode_{episode}.h5')
                            agent2.save_model(f'agent2_model_episode_{episode}.h5')

                        break
                    else:
                        game.switch_player()

def play_vs_agent(agent, episode_number):
    game = ConnectFour()
    state_size = game.rows * game.cols
    action_size = game.cols

    agent.load_model(f'agent_model_episode_{episode_number}.h5')

    while True:
        game.display_board()

        if game.current_player == 1:
            action = int(input("Enter your move (column 0-6): "))
        else:
            action = agent.act(game.board.flatten())

        col = action

        if 0 <= col < game.cols and game.drop_piece(col):
            next_state = game.board.flatten()
            reward = 1 if game.is_winner(game.current_player) else 0
            done = game.is_board_full() or reward == 1

            if game.current_player == 1:
                agent.remember(state, action, reward, next_state, done)
                agent.replay(batch_size=32)

            state = next_state

            if done:
                game.display_board()
                print("Game Over!")
                break
            else:
                game.switch_player()

if __name__ == "__main__":
    state_size = 42  # Replace with the correct state size
    action_size = 7  # Replace with the correct action size
    
    input_type = str(input("Please select type (T)rain|(P)lay:"))

    if input_type == "T":
        loader = str(input("Please select an episode to load from or N for new:"))
        
        if loader == "N":
            # Training phase
            agent1 = DQNAgent(state_size, action_size)
            agent2 = DQNAgent(state_size, action_size)
        else:
            try:
                episode = int(loader)
                agent1 = keras.models.load_model(f'agent1_model_episode_{episode}.h5')
                agent2 = keras.models.load_model(f'agent2_model_episode_{episode}.h5')
            except:
              raise ValueError('Invalid file id')


        for episode in range(1000):
            # ... (same as before)

            if episode % 10 == 0:
                # Save models every 10 episodes
                agent1.save_model(f'agent1_model_episode_{episode}.h5')
                agent2.save_model(f'agent2_model_episode_{episode}.h5')
                
    if input_type == "P":
        # Play against the trained model (specify the episode number)
        agent_to_play_against = str()
        play_vs_agent(agent_to_play_against, episode_number=100)   # Replace 100 with the desired episode number

