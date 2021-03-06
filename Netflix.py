#!/usr/bin/env python3

from math import sqrt
import json

f=open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r')
answer_cache = json.load(f)
f.close()
f=open('/u/mck782/netflix-tests/nrc523-ucache.json', 'r')
user_cache = json.load(f)
f.close()
f=open('/u/mck782/netflix-tests/nrc523-mvcache.json', 'r')
mv_cache = json.load(f)
f.close()

approx_list = []
answer_list = []
current_movie_id = 0

# ------------
# netflix_read
# ------------

def netflix_read (s) :
    """
    read next line of probe data; return a customer ID or update the current movie ID
    s a string
    return the customer ID, or -1 if a movie ID was read and updated
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
    assert(customer_id >= 1)
    assert(customer_id <= 2649429)
    
    global approx_list
    global answer_list
    
    year = mv_cache[str(current_movie_id)]['period']    
    
    #the weights are weird but letting them go negative improved the RMSE by .03 
    rating  = 0.64 * mv_cache[str(current_movie_id)]['average']
    rating += 1.19 * user_cache[str(customer_id)][year]
    rating -= 0.39 * user_cache[str(customer_id)]['avg']
    rating -= 0.48 * 3.23
    
    rating = round(rating, 1)
    if rating > 5.0:
       rating = 5.0
    elif rating < 1.0:
       rating = 1.0
    
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
    assert(len(it1) > 0)
    assert(len(it1) == len(it2))
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
    main loop for reading input, and evaluating and printing the solution
    """
    for s in r :
        customer_id = netflix_read(s)
        if customer_id < 0 :
           w.write(s)
           continue
        rating = netflix_eval(customer_id)
        netflix_print(w, rating)
    netflix_print(w, "RMSE: " + netflix_rmse(approx_list, answer_list) )
        
        
        
        