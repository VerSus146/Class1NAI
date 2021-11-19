from Lab3 import parser
import argparse

import numpy as np
from scoring_algorithms import euclidean_distance
from scoring_algorithms import Neighbours_algorithm_clustering

def build_arg_parser():
    parser = argparse.ArgumentParser(description='Find users who are similar to the input user')
    parser.add_argument('--user', dest='user', required=True,
                        help='Input user')
    return parser

# Finds users in the dataset that are similar to the input user
def find_similar_users(dataset, user, num_users):
    if user not in dataset:
        raise TypeError('Cannot find ' + user + ' in the dataset')

    # Compute Pearson score between input user
    # and all the users in the dataset
    scores = np.array([[x, euclidean_distance(dataset, user, x)] for x in dataset if x != user])

    # Sort the scores in decreasing order
    scores_sorted = np.argsort(scores[:, 1])[::-1]

    # Extract the top 'num_users' scores
    top_users = scores_sorted[:num_users]

    return scores[top_users]

def dict_diff(dict_a, dict_b, show_value_diff=True):
  result = {}
  result['added']   = {k: dict_b[k] for k in set(dict_b) - set(dict_a)}
  result['removed'] = {k: dict_a[k] for k in set(dict_a) - set(dict_b)}
  if show_value_diff:
    common_keys =  set(dict_a) & set(dict_b)
    result['value_diffs'] = {
      k:(dict_a[k], dict_b[k])
      for k in common_keys
      if dict_a[k] != dict_b[k]
    }
  return result



def get_user_movies(data,similar_users, user_search):
    user_search_movies = data[user_search]
    recommendation_level = 8

    recommended_movies = []
    unrecommended_movies = []
    for user in similar_users:
        if user[0] not in data:
            continue
        #get user movies
        user_movies = data[user[0]]

        #calculate diff and select NOT already watched movies
        user_movies = dict_diff(user_movies, user_search_movies)

        #sort in the descending order by rating
        movies_diff = sorted(user_movies['added'].items(), key=lambda x: float(x[1]), reverse=True)

        # let's set unrecommended movies - those with rating with 4 and below
        unrecommended_movies = movies_diff[-5:]
        unrecommended_movies = unrecommended_movies[::-1]

        # appending recommended movies of the matching user
        for movie_diff in movies_diff:
            #if we reach 5 recommendation we can return
            if len(recommended_movies) == 5:
                return [recommended_movies, unrecommended_movies]

            # movies has to have certain rating/recommendation level to be approved
            if float(movie_diff[1]) >= recommendation_level:
                recommended_movies.append(movie_diff)

        #if we didn't find enough recommendation we go to another similiar user
        if len(recommended_movies) < 5:
            continue
        return [recommended_movies, unrecommended_movies]

if __name__ == '__main__':
    data = parser.Parse_CSV()
    print(data)

    Neighbours_algorithm_clustering(data, 'pawel_czapiewski', 'maciej_rybacki')

    # args = build_arg_parser().parse_args()
    # user = args.user
    user = 'tomasz_samol'

    # print('\nUsers similar to ' + user + ':\n')
    similar_users = find_similar_users(data, user, 3)
    recommended_movies = get_user_movies(data,similar_users, user)

    print('similiar_matching',similar_users)
    print('recommended_movies', recommended_movies[0], 'recommended_movies', recommended_movies[1])

