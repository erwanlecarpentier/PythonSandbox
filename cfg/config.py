MYRL_TEST = {
    'environments': [
        {'class': 'gridworld', 'parameters': {'name': 'TestGrid', 'grid_name': 'test', 'size': None, 'gamma': 0.9,
                                              'slip_probability': 0.05, 'is_goal_terminal': False}}
    ],
    'n_episodes': [10],  # number of episodes for each environment
    'n_steps': [10],  # number of decision epochs for each episode
    'n_instances': [3],  # number of agents instances for each environment to create confidence intervals
    'timeout': None,  # maximum number of steps for each environment
    'agents': [
        {'class': 'rmax', 'grid_search': True,
         'parameters': {'name': 'RMax', 'n_known': [1], 'epsilon_q': [0.1]}},
        {'class': 'qlearning', 'grid_search': True,
         'parameters': {'name': 'Q-Learning', 'learning_rate': [0.05], 'epsilon': [0.1]}},
        {'class': 'random', 'grid_search': False, 'parameters': {'name': 'Random'}}
    ],
    'n_processes': 1,  # maximum number of processes, if None, take as many processes as the number of available CPU
    'save_ma': 1,  # on disk, rewards are saved based on this moving average window size
    'reward_plot_ma': [300],  # graphs: rewards per step are displayed based on these moving average window sizes
    'return_plot_ma': [1, 10],  # graphs: return per episodes are displayed based on these moving average window sizes
    'markers_freq': None,  # Markers frequency in graphs (automatically computed if None)
    'gpu': False
}
