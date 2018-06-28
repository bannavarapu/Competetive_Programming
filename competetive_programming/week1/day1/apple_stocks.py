def get_max_profit(stock_prices):

    # Calculate the max profit
    if len(stock_prices)<2:
        raise Exception
    
    mini=stock_prices[0]
    diff=stock_prices[1]-stock_prices[0]
    for i in range(1,len(stock_prices)):
        x=stock_prices[i]
        if(x-mini>diff):
            diff=x-mini
        if(x<mini):
            mini=x
    return diff
