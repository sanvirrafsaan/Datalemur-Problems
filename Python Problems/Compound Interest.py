def compound_interest(principal, rate, contribution, years):
    balance = principal
    for i in range(years):
       balance = balance * ((rate/100) + 1) + contribution
    return round(balance, 2)

