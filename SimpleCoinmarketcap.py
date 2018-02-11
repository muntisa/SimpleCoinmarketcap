# Simple Coinmarketcap portofolio
# by muntisa (2018)

# * get information for your coins from Coinmarketcap APIs (you need Internet connection!)
# * needs a portofolio TXT (tab-separated) file with Coin ID and Quantity (in the same folder with the script)
# Example of myPortofolio.txt:
# ethereum	3.15510024
# bitcoin	1.20405000
# litecoin	5.00217822
# * it is possible to call the main function for different portofolio files
# (you can print different portofolios with one run)

# Use:
# - just change the name of portofolios files when you call the function CoinmarketcapPortofolio()
# - call the function one time for each portofolio file

# import libraries
import urllib, json, datetime

# function that get input a portofolio file name and print the info for all coins
def CoinmarketcapPortofolio(sFile):
    f_money = open(sFile)       # open the file with coins & quantities
    lines = f_money.readlines() # get file content as list of rows
    f_money.close()             # close file

    # total values of coins
    total_value = 0             # initially zero total value for coins ($)

    # print header
    print "--------------------------------------------------------------------------"
    print sFile, datetime.datetime.today(),"\n" # print name of the file with coints and date+time  
    
    # print header for the portofolio for one specific file with coins
    print '%-5s %-12s %-10s %-15s %-10s %-10s %-10s\n' % ("Coin","Quantity","USD/coin","Total value(USD)","Var 1h", "Var 24h","Var 7d")

    # process each coin
    for line in lines: # for each line in coins file
        # get coin ID and quantity from money.txt file
        sID, sQty = line.rstrip().split("\t")
        
        # get data from coinmarketcap for each coin
        # define the Coinmarketcap API URL for one coin as
        # https://api.coinmarketcap.com/v1/ticker/[coin ID in Coinmarketcap]/
        url = "https://api.coinmarketcap.com/v1/ticker/%s/" % sID
        response = urllib.urlopen(url)     # open the link
        data = json.loads(response.read()) # get the API answer as JSON (dictionary)
        
        # get specific data from the API result / dictionary
        name               = data[0]['name']
        symbol             = data[0]['symbol']
        price_usd          = data[0]['price_usd']
        percent_change_1h  = data[0]['percent_change_1h']
        percent_change_24h = data[0]['percent_change_24h']
        percent_change_7d  = data[0]['percent_change_7d']

        # uncomment any information you need below and use it for print later
        #rank               = data[0]['rank']
        #price_btc          = data[0]['price_btc']
        #s24h_volume_usd    = data[0]['24h_volume_usd']
        #market_cap_usd     = data[0]['market_cap_usd']
        #available_supply   = data[0]['available_supply']
        #total_supply       = data[0]['total_supply']
        #max_supply         = data[0]['max_supply']
        #last_updated       = data[0]['last_updated']

        # add each coin value to the total value ($)
        total_value += float(sQty)*float(price_usd) 

        # print information for each coin
        # (you can add any variable from the above lines!)
        print '%-5s %-12s $%-10s $%-15s %-10s %-10s %-10s' %(symbol,sQty,price_usd,str(float(sQty)*float(price_usd)),percent_change_1h,percent_change_24h,percent_change_7d)

    # print total value of your coins ($) in the current portofolio file
    print "\nTOTAL value = $", total_value


###################################################
# MAIN

if __name__ == "__main__":
    # print portofolio for miners.txt file
    CoinmarketcapPortofolio("myPortofolio1.txt") # please change myPortofolio1.txt with your portofolio file!

    # print portofolio for miners.txt file
    CoinmarketcapPortofolio("myPortofolio2.txt") # please change myPortofolio2.txt with your portofolio file!

    # you can add any other portofolio with
    # CoinmarketcapPortofolio("YouNewPortofolio.txt")
    
    # wait to press ENTER to exit
    input("\nPress ENTER to exit ...")

