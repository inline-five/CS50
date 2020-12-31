def main():

    stocks = [19,17,6,9,8,15,6,3,1]
    buysell = []
    print(stockpicker(stocks))
    

############   function below   ############

def stockpicker(listofstocks):
    maxprofit = 0

    for buy in range(0, len(listofstocks)):
        for sell in range(buy+1, len(listofstocks)):
            if listofstocks[sell] - listofstocks[buy] > maxprofit:
                maxprofit = listofstocks[sell] - listofstocks[buy]
                buysell = [buy, sell]

    return buysell


main()