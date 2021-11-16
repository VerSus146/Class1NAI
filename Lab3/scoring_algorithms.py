import argparse
import json
import numpy as np
import pandas as pd


def euclidean_distance(dataset, user1, user2):
    if user1 not in dataset:
        raise TypeError('Cannot find ' + user1 + ' in the dataset')

    if user2 not in dataset:
        raise TypeError('Cannot find ' + user2 + ' in the dataset')

        # Movies rated by both user1 and user2
    common_movies = {}

    for item in dataset[user1]:
        if item in dataset[user2]:
            common_movies[item] = 1

    # If there are no common movies between the users,
    # then the score is 0
    if len(common_movies) == 0:
        return 0

    squared_diff = []

    for item in dataset[user1]:
        if item in dataset[user2]:
            squared_diff.append(np.square(float(dataset[user1][item]) - float(dataset[user2][item])))

    return 1 / (1 + np.sqrt(np.sum(squared_diff)))


def cosine_distance(dataset, user1, user2):
    return
