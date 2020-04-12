#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
#import logging
#from logging import Formatter, FileHandler
#from forms import *
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('pages/stocks.html')
    elif request.method == 'POST':
        print("------------------Drusti----------------")
        
    # Input Fields
    symbol = request.form['stockSymbol']
    allotment = float(request.form['allotment'])
    final_share_price = float(request.form['finalPrice'])
    sell_comm = float(request.form['sellCommission'])
    init_share_price = float(request.form['initialPrice'])
    buy_comm = float(request.form['buyCommission'])
    cap_gain_tax = float(request.form['taxRate'])

    # # Make Calculations

    proceeds = int(allotment) * float(final_share_price)
    total_tax = (((float(final_share_price) - float(init_share_price))
                  * int(allotment) - float(buy_comm) - float(sell_comm)))
    tax = total_tax * float(cap_gain_tax) / 100
    init_total = int(allotment) * float(init_share_price)
    cost = init_total + float(buy_comm) + float(sell_comm) + tax
    net_profit = proceeds - cost
    return_on_inv = net_profit / cost * 100
    breakeven = (init_total + float(buy_comm) +
                 float(sell_comm)) / int(allotment)

    # reprocess the above calculations with proper UI
    print_proceeds = "$%.2f" % proceeds
    print_cost = "$%.2f" % cost
    print_total = str(allotment) + " x $" + \
        str(init_share_price) + " = %.2f" % init_total
    #print_total = allotment + " x $" + init_share_price + " = %.2f" % init_total
    print_gain = str(cap_gain_tax) + "% of $" + \
        "%.2f" % total_tax + " = %.2f" % tax
    print_net_profit = "$" + "%.2f" % net_profit
    print_ret_on_inv = "%.2f" % return_on_inv + "%"
    print_breakeven = "$" + "%.2f" % breakeven

    tempData = {'symbol': symbol, 'allotment': allotment,
                'final_share_price': final_share_price, 'sell_comm': sell_comm,
                'init_share_price': init_share_price, 'buy_comm': buy_comm,
                'cap_gain_tax': cap_gain_tax, 'proceeds': print_proceeds, 'gain': print_gain,
                'cost': print_cost, 'init_total': print_total, 'net_profit': print_net_profit,
                'ret_on_inv': print_ret_on_inv, 'breakeven': print_breakeven}
    print(tempData)
    return render_template('pages/stocks.html', **tempData)

# Default port:
if __name__ == '__main__':
    app.run()
