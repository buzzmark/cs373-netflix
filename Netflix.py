#!/usr/bin/env python3

from math import sqrt
import json

answer_cache = json.load(open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r'))
mv_avg_cache = json.load(open('/u/mck782/netflix-tests/pma459-mvAvgCache.json', 'r'))
user_cache = json.load(open('/u/mck782/netflix-tests/nrc523-ucache.json', 'r'))
date_cache = json.load(open('/u/mck782/netflix-tests/af22574-movieDates.json', 'r'))

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
    rating  = 0.30 * mv_avg_cache[current_movie_id]
    
    year = date_cache[str(current_movie_id)]
    if year == 'NULL':
        rating += 0.70 * user_cache[str(customer_id)]['avg']
    else:
        decade = int(year) // 10 * 10
        #rating += 0.00 * user_cache[str(customer_id)]['avg']
        rating += 0.70 * user_cache[str(customer_id)][str(decade)]
    
    
    rating = round(rating, 1)
    approx_list.append(rating)
    answer_list.append(int(answer_cache[str(current_movie_id)][str(customer_id)]))
    assert rating >= 1.0
    assert rating <= 5.0
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
        
        
        
        