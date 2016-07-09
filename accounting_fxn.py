#for i in range(len(tokenized_nmc)):
    #tokenized_nmc[i] = int(tokenized_nmc[i])
    #print tokenized_nmc

def expected_v_paid(order_sheet_file):
	melon_cost = 1.00
	order_sheet = open(order_sheet_file)

	for line in order_sheet:
        	order = line.split('|')

                customer_name = order[1]	
 		customer_first = customer_name.split(" ")[0]
		num_melon = float(order[2])
		customer_paid = float(order[3])

 		customer_expected = num_melon * melon_cost
		customer_expected = float(customer_expected)
		
		if customer_expected > customer_paid:
			print customer_first, "paid {:.2f}, expected {:.2f}".format(customer_paid, customer_expected)
	  	else: 
			print "{} got what s/he paid for!".format(customer_first)	

expected_v_paid("customer-orders.txt")
