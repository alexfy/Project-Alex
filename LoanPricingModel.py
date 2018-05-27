# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:25:00 2018

@author: tidus
"""

#Helper functions

def samesign(a,b):
    return a * b > 0

def f(p,x,cf,r,cs,T):
    ans = 0.0 - p
    for t in range(int(T)):
        ans += cf/((1+r[t]+x+cs[t])**(t+1))
    ans+=1/((1+r[T-1]+x+cs[T-1])**(T))
    return ans


# We assume notional is 1 for now
class Loan:
    def __init__(self, price, coupon, factors, spreads, maturity):
        self.discount_curve = DiscountCurve(factors)
        self.credit_market = CreditMarket(spreads)
        self.coupon = coupon
        self.maturity = maturity
        self.marked_price = price
        self.pricing_model = PricingModel()
        self.pricing_model.funding_rate(price, coupon, factors, spreads, maturity)
    
    def marked_price(self):
        return self.marked_price
    
    def model_price(self, coupon, factors, spreads, maturity):
        return self.pricing_model.model_price(coupon, factors, spreads, maturity)
        
        

class DiscountCurve:
    def __init__(self, factors):
        self.discount_factors=[]
        n = len(factors)
        for i in range (n):
            self.discount_factors.append(factors[i])
        

class CreditMarket:
    def __init__(self, spreads):
        self.credit_spreads=[]
        n = len(spreads)
        for i in range (n):
            self.credit_spreads.append(spreads[i])


class PricingModel:
    def __init__(self):
        self.fund_rate=-1.0
     #   pass
    def funding_rate(self,marked_price, coupon, factors, spreads, maturity):
        if(self.fund_rate==-1.0):
            high = 1.0
            low = 0.0
            i=0
            while ((high-low>0.00001) and i<10000):
                mid = (low + high) / 2.0
                if samesign(f(marked_price,low,coupon,factors,spreads,maturity), f(marked_price,mid,coupon,factors,spreads,maturity)):
                    low = mid
                else:
                    high = mid
                i+=1
            self.fund_rate = mid
        return self.fund_rate
    def model_price(self, coupon, factors, spreads, maturity):
        ans = 0.0
        for t in range(int(maturity)):
            ans += coupon/((1+factors[t]+self.fund_rate+spreads[t])**(t+1))        
        ans+=1/((1+factors[maturity-1]+self.fund_rate+spreads[maturity-1])**(maturity))
        return ans    



''' 
facs = [0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01]
sprds = [0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]
mp = 1
cp = 0.05
mat = 10

dc = DiscountCurve(facs)
cm = CreditMarket(sprds)
pm = PricingModel()
'''
'''
print dc.discount_factors[9];
print cm.credit_spreads[9];

fx = f(mp,0.02,cp,facs,sprds,mat)
print fx
fx = f(mp,0.0205078125,cp,facs,sprds,mat)
print fx

dfx = df(0.02,cp,facs,sprds,mat)
print dfx
'''
'''
fr = pm.funding_rate(mp,cp,facs,sprds,mat)
print fr
modelprice = pm.model_price(cp,facs,sprds,mat)
print modelprice

facs2 = [0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]
facs3 = [0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03]

sprds2 = [0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03,0.03]
sprds3 = [0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04]
'''
'''
modelprice2 = pm.model_price(cp,facs2,sprds,mat)
print modelprice2

modelprice3 = pm.model_price(cp,facs3,sprds,mat)
print modelprice3
'''
'''
modelprice2 = pm.model_price(cp,facs,sprds2,mat)
print modelprice2

modelprice3 = pm.model_price(cp,facs,sprds3,mat)
print modelprice3
'''