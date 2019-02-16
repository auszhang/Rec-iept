from decimal import Decimal 

# SAMPLE INFORMATION FOR TESTING: obtain actual values from GCP:
sample_easy1 = {'BJS FRITOS NACHOS':7.50, 'BH DBL DELUXE BURGER':10.95}
subtotal = 18.45 #could calculate this later?
tax = 1.71
total_no_tip = 20.16
tip_percent = 15

# convert tip_percent to decimal:
tip_decimal = tip_percent/100.0

# caulculate tip amount
tip_amount = tip_decimal*total_no_tip
tip_amount = float("%.2f" % round(tip_amount,2))
print "Tip amount: $" + str(tip_amount)

# variable for tax+tip (for later)
tax_tip = tip_amount + tax
print "Tax + tip: $" + str(tax_tip)

# add tip amount to total
total = total_no_tip + tip_amount
print "Total after tip: $" +  str(total)

print " "

# find percentage split for each item
for k,v in sample_easy1.items():
    # print k,v
    percent = v/subtotal
    percent = float("%.2f" % round(percent,2))
    print "Percentage of the bill for " + k + ": " + str(percent) + "%"
    k_tax_tip = tax_tip * percent
    k_tax_tip = float("%.2f" % round(k_tax_tip,2))
    print "Person who bought " + k + " pays $" + str(k_tax_tip) + " for tax and tip"
    k_total = v + k_tax_tip
    result_string = "Person who bought " + k + " pays $" + str(k_total) + " in total"
    print result_string
    print " "

