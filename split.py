import json
import re 
# SAMPLE INFORMATION FOR TESTING: obtain actual values from GCP:
# sample_easy1 = {'BJS FRITOS NACHOS':7.50, 'BH DBL DELUXE BURGER':10.95}
# sample_names = {'BJS FRITOS NACHOS': 'Austin,Sandy', 'Austin'}
# print json.dumps(sample_easy1)

# subtotal = 0.0
# tax = 0.0
# # tip_percent = 0
# # tip_amount = 0
# tax_tip = 0.0
# total = 0.0
# def basics(dictionary):
#     # get subtotal
#     for k,v in dictionary:
#         global subtotal += float(v)
def outputter(item_price, item_name):
    special_words = ['subtotal', 'sub total', 'total', 'tax', 'gratuity', 'tip']
    subtotal = 0.0
    tax = 0.0
    total = 0.0
    gratuity = 0.0
    tip = 0.0
    only_items = {}
    for k,v in item_price.items():
        lol = re.sub("[^a-zA-Z]", "", k).lower()
        if 'subtotal' in lol or 'total' in lol or 'sub total' in lol:
            continue
        elif 'tax' == lol:
            if tax == 0.0:
                tax = float(v)
        elif 'gratuity' == lol:
            if gratuity == 0.0:
                gratuity = float(v)
        elif 'tip' == lol:
            if tip == 0.0:
                tip = float(v)
        else:
            subtotal += v
            only_items[k] = float(v)

    total = subtotal + tip + tax + gratuity

    item_contributions = {}

    for k, v in only_items.items():
        item_contributions[k] = v/subtotal * total

    person_pays = {}

    for k,v in item_name.items():
        names = v.split(",")
        for name in names:
            lower_name = name.lower()
            if 'total' not in lower_name: 
                new_name = name.strip()
                person_pays[new_name] = 0

    for k, v in item_name.items():
        food_item = k
        food_participants = v.split(",")
        num_eaters = len(food_participants)
        for eater in food_participants:
            new_eater = eater.strip()

            person_pays[new_eater] += item_contributions[food_item] / num_eaters
    return person_pays
    # for k,v in person_pays.items():
    #     print('The person named ' + k + ' pays ' + str(v))


def checker(lst, word):
    return re.sub("[^a-zA-Z]", "", word).lower() in lst
# # get total without tip from tax and subtotal
# tax =  #provided???
# total_no_tip = subtotal + tax
# # convert tip_percent to decimal:
# tip_percent = 15
# tip_decimal = tip_percent/100.0

# # caulculate tip amount
# tip_amount = tip_decimal*total_no_tip
# tip_amount = float("%.2f" % round(tip_amount,2))
# print "Tip amount: $" + str(tip_amount)

# # variable for tax+tip (for later)
# tax_tip = tip_amount + tax
# print "Tax + tip: $" + str(tax_tip)

# # add tip amount to total
# total = total_no_tip + tip_amount
# print "Total after tip: $" +  str(total)

# print " "

# find percentage split for each item
# for k,v in sample_easy1.items():
#     # print k,v
#     percent = v/subtotal
#     percent = float("%.2f" % round(percent,2))
#     print "Percentage of the bill for " + k + ": " + str(percent) + "%"
#     k_tax_tip = tax_tip * percent
#     k_tax_tip = float("%.2f" % round(k_tax_tip,2))
#     print "Person who bought " + k + " pays $" + str(k_tax_tip) + " for tax and tip"
#     k_total = v + k_tax_tip
#     result_string = "Person who bought " + k + " pays $" + str(k_total) + " in total"
#     print result_string
#     print " "