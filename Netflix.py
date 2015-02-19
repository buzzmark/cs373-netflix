#!/usr/bin/env python3

from math import sqrt
import json

probe_location = '/u/downing/cs/netflix/probe.txt'
answers_location = '/u/mck782/netflix-tests/pma459-answersCache.json'
answer_cache = json.load(open(answers_location, 'r'))


approx_list = []
answer_list = []
current_movie_id = 0

# ------------
# netflix_read
# ------------

def netflix_read (s) :
    """
    read next line of probe data
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    global current_movie_id
    if s.endswith(':\n') :
       current_movie_id = int(s[:-2])
       return -1
    return int(s)

# ------------
# netflix_eval
# ------------

def netflix_eval (customer_id) :
    """
    customer_id the custom to make a prediction for
    return the customer's predicted rating for the current movie
    """
    global approx_list
    global answer_list
    
    #compute aprroximate rating
    rating = 3.0
    
    approx_list.append(rating)
    answer_list.append(int(answer_cache[str(current_movie_id)][str(customer_id)]))
    return rating

# -------------
# netflix_print
# -------------

def netflix_print (w, s) :
    """
    print the given string
    w a writer
    s the string to print
    """
    w.write(str(s) + "\n")
    
# -------------
# netflix_rmse
# -------------
 
def netflix_rmse (it1, it2) :
    """
    it1 an iterable
    it2 an iterable
    return a string containing the root mean square error between it1 and it2
    """
    z = zip(it1, it2)
    v = sum((x - y) ** 2 for x, y in z)
    return '%.2f' % sqrt(v / len(it1))
    

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        customer_id = netflix_read(s)
        if customer_id < 0 :
           w.write(s)
           continue
        rating = netflix_eval(customer_id)
        netflix_print(w, rating)
    netflix_print(w, "RMSE: " + netflix_rmse(approx_list, answer_list) )
        
        
        
        