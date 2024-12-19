
purchase_price = .07857
sales_price  = .08842
amount = 400

def percentage_gain(purchase_price, sales_price, amount):
    gain = (sales_price - purchase_price)/purchase_price 
    profit = gain * amount 
    profit = round(profit, 2)

    percentage = float(gain*100)
    percentage = round(percentage, 2)
    print(f"put in {amount}, there was a {percentage}% change in price, for ${profit} in profit")

percentage_gain(purchase_price, sales_price, amount)

# over a week

# BTC --> 4.9%

# ETH --> 6.23%

# SOL --> 9.0%

# COTI -> 12.54%  

# RBN --> 26.48%






