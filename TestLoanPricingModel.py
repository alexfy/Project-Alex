# -*- coding: utf-8 -*-
"""
Created on Sun May 27 14:27:42 2018

@author: tidus
"""

import unittest
import numpy as np
import LoanPricingModel as lpm

class TestLoanPricingModel(unittest.TestCase):  
    
    def test_monotonicity_credit_spread_curves(self):
        #input initializations
        facs = [0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01]
        sprds = [0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]
        mp = 1
        cp = 0.05
        mat = 10
        pm = lpm.PricingModel()
        pm.funding_rate(mp,cp,facs,sprds,mat)   
        
        #randomize discount curves
        n = 1000
        s = np.random.uniform(0,1,n)
        s.sort()
        
        #test monotonicity
        model_prices = []
        for i in range(n):
            credit_spread = []
            for j in range(mat):
                credit_spread.append(s[i])
            model_prices.append(pm.model_price(cp,facs,credit_spread,mat))
            #print model_prices[i]
        result = True
        for i in range (n-1):
            if(model_prices[i]<model_prices[i+1]):
                result = False
                i = n
        expected = True
        self.assertEqual(expected,result)

    def test_monotonicity_discount_curves(self):
        #input initializations
        facs = [0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01]
        sprds = [0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]
        mp = 1
        cp = 0.05
        mat = 10
        pm = lpm.PricingModel()
        pm.funding_rate(mp,cp,facs,sprds,mat)   
        
        #randomize discount curves
        n = 1000
        s = np.random.uniform(0,1,n)
        s.sort()
        
        #test monotonicity
        model_prices = []
        for i in range(n):
            discount_curve = []
            for j in range(mat):
                discount_curve.append(s[i])
            model_prices.append(pm.model_price(cp,discount_curve,sprds,mat))
            #print model_prices[i]
        result = True
        for i in range (n-1):
            if(model_prices[i]<model_prices[i+1]):
                result = False
                i = n
        expected = True
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()
