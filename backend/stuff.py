from decimal import Decimal 
#from __future__ import division

# SAMPLE INFORMATION FOR TESTING: obtain actual values from GCP:
sample_easy1 = {'BJS FRITOS NACHOS':7.50, 'BH DBL DELUXE BURGER':10.95}
tax = 1.71
total_no_tip = 20.16
tip_percent = 15

#convert tip_percent to decimal:
tip = tip_percent/100.0

#calculate total with tip
total = 20.16 * (tip + 1.00)
print total

for k,v in sample_easy1.items():
    print k, v
