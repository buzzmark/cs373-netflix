#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_eval, netflix_print, netflix_rmse, netflix_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s = "2000:\n"
        v = netflix_read(s)
        self.assertEqual(v, -1)
        
    def test_read_2 (self) :
        s = "1\n"
        v = netflix_read(s)
        self.assertEqual(v, 1)
        
    def test_read_3 (self) :
        s = "2649429\n"
        v = netflix_read(s)
        self.assertEqual(v, 2649429)
        
    def test_read_4 (self) :
        s = "9999:\n"
        v = netflix_read(s)
        self.assertEqual(v, -1)
        
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, "1.0")
        self.assertEqual(w.getvalue(), "1.0\n")
        
    def test_print_2 (self) :
        w = StringIO()
        netflix_print(w, "3.5")
        self.assertEqual(w.getvalue(), "3.5\n")
        
    def test_print_3 (self) :
        w = StringIO()
        netflix_print(w, "5.0")
        self.assertEqual(w.getvalue(), "5.0\n")
        
    def test_print_4 (self) :
        w = StringIO()
        netflix_print(w, "4.5")
        self.assertEqual(w.getvalue(), "4.5\n")

    # -----
    # rmse
    # -----

    def test_rmse_1 (self) :
        e = netflix_rmse([1,1,1],[1,1,1])
        self.assertEqual(e, '0.00')
        
    def test_rmse_2 (self) :
        e = netflix_rmse([2,3,4],[3,2,5])
        self.assertEqual(e, '1.00')

    def test_rmse_3 (self) :
        e = netflix_rmse([2,3,4],[4,1,6])
        self.assertEqual(e, '2.00')
        
    def test_rmse_4 (self) :
        e = netflix_rmse([2,3,4],[4,3,2])
        self.assertEqual(e, '1.63')    

    # -----
    # solve
    # -----
    
    def test_netflix_solve1(self) :
        w = StringIO()
        r = StringIO("7227:\n874253\n7229:\n1796878\n1676554\n")
        netflix_solve(r,w)
        self.assertEqual(w.getvalue()[:6], "7227:\n")
        self.assertEqual(w.getvalue()[-11:-5], "RMSE: ")
        
    def test_netflix_solve2(self) :
        w = StringIO()
        r = StringIO("7227:\n874253\n")
        netflix_solve(r,w)
        self.assertEqual(w.getvalue()[:6], "7227:\n")
        self.assertEqual(w.getvalue()[-11:-5], "RMSE: ")
        
    def test_netflix_solve3(self) :
        w = StringIO()
        r = StringIO("7229:\n1796878\n1676554\n")
        netflix_solve(r,w)
        self.assertEqual(w.getvalue()[:6], "7229:\n")
        self.assertEqual(w.getvalue()[-11:-5], "RMSE: ")



# ----
# main
# ----

if __name__ == "__main__" :
    main()