import requests, json, time

def aylık_tüketim(parametre):
        return parametre*24*30/1000

def hesapla(enerji):
    enerji = aylık_tüketim(enerji)

    #Mart 2022 itibariyle güncel %8 kdv
    fatura = round(enerji * 1.884213627, 2)
    
    return round(fatura/30*100)/100


"""
req_data = requests.get("https://api.exchangerate.host/latest?base=USD")
req_data = req_data.text
req_data = json.loads(req_data)

usd_try = req_data["rates"]["TRY"]                   ###### Çalışmazsa alttaki"""
usd_try = 14.65

#-----------------------------BTC-------------------------------------

req_data = requests.get("https://whattomine.com/coins/1.json")
req_data = req_data.text
req_data = json.loads(req_data)
btc_usd = req_data["exchange_rate"]                             ######

#-----------------------------RVN-------------------------------------

req_data = requests.get("https://whattomine.com/coins/234.json")
req_data = req_data.text
req_data = json.loads(req_data)
rvn_usd = req_data["exchange_rate"] * btc_usd
btc_per_rvn_mh = float(req_data["btc_revenue"]) / 39            ######
#print(json.dumps(req_data, indent = 4))

#-----------------------------ETH-------------------------------------

req_data = requests.get("https://whattomine.com/coins/151.json")
req_data = req_data.text
req_data = json.loads(req_data)
eth_usd = req_data["exchange_rate"] * btc_usd
btc_per_eth_mh = float(req_data["btc_revenue"]) / 88.5          ######

#-----------------------------ETC-------------------------------------

req_data = requests.get("https://whattomine.com/coins/162.json")
req_data = req_data.text
req_data = json.loads(req_data)
etc_usd = req_data["exchange_rate"] * btc_usd
btc_per_etc_mh = float(req_data["btc_revenue"]) / 88.5          ######

#-----------------------------ERG-------------------------------------

req_data = requests.get("https://whattomine.com/coins/340.json")
req_data = req_data.text
req_data = json.loads(req_data)
erg_usd = req_data["exchange_rate"] * btc_usd
btc_per_erg_mh = float(req_data["btc_revenue"]) / 177          ######

#---------------------------------------------------------------------

req_data = requests.get("https://whattomine.com/coins/348.json")
req_data = req_data.text
req_data = json.loads(req_data)
ton_usd = req_data["exchange_rate"] * btc_usd
btc_per_ton_mh = float(req_data["btc_revenue"]) / 4600          ######
print(btc_per_etc_mh/btc_per_ton_mh)

#---------------------------------------------------------------------

requested_rates = {                             # Sum of requested values
    "usd" : usd_try,
    "btc" : btc_usd,
    "eth" : eth_usd,
    "rvn" : rvn_usd,
    "etc" : etc_usd,
    "erg" : erg_usd,
    "ton" : ton_usd }
for i in requested_rates:
    print(f"{i}: {round(requested_rates[i], 6)}")

requested_diff = {                              # Sum of requested difficulty
    "eth" : btc_per_eth_mh,
    "rvn" : btc_per_rvn_mh,
    "etc" : btc_per_etc_mh,
    "erg" : btc_per_erg_mh,
    "ton" : btc_per_ton_mh }

class new_algo:
    def __init__(self, name, hashrate, power):
        self.name = name
        self.hashrate = hashrate
        self.power = power

class new_dual_algo:
    def __init__(self, f_name, f_hash, s_name, s_hash, power):
        self.f_name = f_name
        self.f_hash = f_hash
        self.s_name = s_name
        self.s_hash = s_hash
        self.power = power
        
class card:                                     # Only card name is mandatory
    def __init__(self, card_name):
        self.card_name = card_name
        self.algos = []
        self.dual_algos = []

    def num_of_algos(self):
        return int(len(self.algos) + len(self.dual_algos))
    
    def create_algo(self, name, hashrate, power): # Add new algoritm to card for listing
        x = new_algo(name, hashrate, power)
        self.algos.append(x)

    def create_dual_algo(self, f_name, f_hash, s_name, s_hash, power):
        x = new_dual_algo(f_name, f_hash, s_name, s_hash, power)
        self.dual_algos.append(x)

class line:                     # A parameter class for create_line function
    def __init__(self, card, algo_name, amount, gross_profit, expense, net_profit):
        self.card = card
        self.algo_name = algo_name
        self.amount = amount
        self.gross_profit = gross_profit
        self.expense = expense
        self.net_profit = net_profit

def create_line(new_line , space):  # Printing finished lines
    if(new_line.card == '\0'):                  # Dashed line part
        print("+" + "".ljust(space[0],'-') + 
        "+" + "".ljust(space[1],'-') +
        "+" + "".ljust(space[2],'-') +
        "+" + "".ljust(space[3],'-') +
        "+" + "".ljust(space[4],'-') +
        "+" + "".ljust(space[5],'-') + "+")
    else:                                       # Actual line printing
        return_line  = "|" + f"{new_line.card}".center(space[0], ' ')
        return_line += "|" + f"{new_line.algo_name}".center(space[1], ' ')
        return_line += "|" + f"{new_line.amount}".center(space[2], ' ')
        return_line += "|" + f"{new_line.gross_profit}".center(space[3], ' ')
        return_line += "|" + f"{new_line.expense}".center(space[4], ' ')
        return_line += "|" + f"{new_line.net_profit}".center(space[5], ' ') +"|"
        print(return_line)
    
def get_key(aa):                    # Required by sort function
    return aa.net_profit
  
def dashed_line():         # Dashed line command for create_line function
    x = line('\0','\0', '\0', '\0', '\0', '\0')
    lines.append(x)


day = 30
fiat = requested_rates["usd"] if 0 else 1

#fiat, day = (requested_rates["usd"], 1) if 1 else (1, 30)

cards = []
spaces = [0, 0, 0, 0, 0, 0]
lines = []
dashed_line()
###                          Adding Cards and their algorithms               ###
number = 0
cards.append(card("Sistem"))
cards[number].create_algo("etc", 253.3, 1135)
cards[number].create_dual_algo("etc", 252.5, "ton", 4370, 1420)
cards[number].create_algo("rvn", 111, 1260)
cards[number].create_algo("erg", 509.5, 890)
#cards[number].create_algo("ton", 6300, 1010)
cards[number].create_dual_algo("erg", 411.5, "ton", 1470, 900)
number += 1

cards.append(card("Ogi"))
cards[number].create_algo("eth", 98.1, 480)
number += 1

cards.append(card("Test"))
cards[number].create_algo("eth", 42*3, 540)
cards[number].create_algo("erg", 509.8, 900)
cards[number].create_algo("rvn", 111, 1260)
number += 1

cards.append(card("Polaris"))
cards[number].create_algo("eth", 32.7, 80)
cards[number].create_algo("erg", 63.75, 70)
cards[number].create_algo("etc", 31.5, 85)
cards[number].create_algo("rvn", 13.8, 99)
cards[number].create_algo("ton", 790, 85)
cards[number].create_dual_algo("etc",31.35,"ton",620,110)
number += 1
"""
cards.append(card("RTX 3070"))
cards[number].create_algo("eth", 61.6, 125)
number += 1

cards.append(card("RTX 3070 Ti"))
cards[number].create_algo("eth", 59, 240)
number += 1

cards.append(card("RTX 3080 L"))
cards[number].create_algo("eth", 74, 250)
number += 1

cards.append(card("RTX 3080 Ti"))
cards[number].create_algo("eth", 87, 290)
number += 1

cards.append(card("6800 XT"))
cards[number].create_algo("eth", 62.8, 128)
number += 1

cards.append(card("RTX 3090"))
cards[number].create_algo("eth", 120, 300)
number += 1

cards.append(card("5600 XT"))
cards[number].create_algo("eth", 42, 84)
number += 1

cards.append(card("A2000"))
cards[number].create_algo("eth", 42, 69)
cards[number].create_algo("erg", 107, 60)
cards[number].create_algo("ton", 1400, 80)
"""
number += 1

x = line("KART", "COIN", "MİKTAR", "BRÜT", "GİDER", "KAR")
lines.append(x)
spaces[0] = len(x.card) + 2
spaces[1] = len(x.algo_name) + 2
spaces[2] = len(x.amount) + 2
spaces[3] = len(x.gross_profit) + 3
spaces[4] = len(x.expense) + 2
spaces[5] = len(x.net_profit) + 3
# First space allocations

dashed_line()

for new_element in cards:       # Works for all cards
    local_lines = []            # Temp variable for card algorithm sorting 

    if(len(new_element.card_name) >= spaces[0]):    # CARD section space calc
        spaces[0] = len(new_element.card_name) + 2

    itera = len(new_element.algos)

    for i in range(itera):      # Works for all algorithms 

        if(len(new_element.algos[i].name) >= spaces[1]): # COIN section space calc
            spaces[1] = len(new_element.algos[i].name) + 2

        gross = new_element.algos[i].hashrate
        gross *= requested_diff[new_element.algos[i].name] 
        gross *= requested_rates["btc"]
        gross = round(gross * day * requested_rates["usd"], 2) # TL
            # gross profit is calculated and rolled to 2 digits

        if(len(str(gross)) >= spaces[3]):       # GROSS section space calc
            spaces[3] = len(str(gross)) + 2

        amount = gross / requested_rates[new_element.algos[i].name] 
        amount /= requested_rates["usd"]
        amount = round(amount, 8)
        
            # Equivalent amount of cryptocurrency is calculated and rolled to 8 digits

        if(len(str(amount)) >= spaces[2]):      # AMOUNT section space calc
            spaces[2] = len(str(amount)) + 2

        expense = hesapla(new_element.algos[i].power) * day
        expense = round(expense, 2)  
        # expense is calculated and rolled to 2 digits

        if(len(str(expense)) >= spaces[4]):     #EXPENSE section space calc
            spaces[4] = len(str(expense)) + 2

        profit = round(gross - expense, 2)     
            # profit is calculated and rolled to 2 digits

        if(len(str(profit)) >= spaces[5]):      # PROFIT section space calc
            spaces[5] = len(str(profit)) + 2

        gross = round(gross / fiat, 2)
        expense = round(expense / fiat, 2)
        profit = round(gross - expense, 2)
            
        x = line("",new_element.algos[i].name, amount, gross, expense, profit)
            # Preparing new line for current card's current algorithm

        local_lines.append(x)   # and adding to temp list

    
    itera = len(new_element.dual_algos)
    for i in range(itera):            # Works for all dual algorithms

        dual_name = new_element.dual_algos[i].f_name + "+" + new_element.dual_algos[i].s_name
        if(len(dual_name) >= spaces[1]):             # COIN section space calc
            spaces[1] = len(dual_name) + 2

        gross1 =  new_element.dual_algos[i].f_hash
        gross1 *= requested_diff[new_element.dual_algos[i].f_name] 
        gross1 *= requested_rates["btc"]
        
        gross2 =  new_element.dual_algos[i].s_hash
        gross2 *= requested_diff[new_element.dual_algos[i].s_name]
        gross2 *= requested_rates["btc"]
        
        gross = round((gross1+ gross2) * day * requested_rates["usd"], 2) # TL
            # gross profit is calculated and rolled to 2 digits

        if(len(str(gross)) >= spaces[3]):       # GROSS section space calc
            spaces[3] = len(str(gross)) + 2

        # Because of calculating two algorithms in one line
        # amount section is bypassed

        expense = hesapla(new_element.dual_algos[i].power) * day
        expense = round(expense, 2)   
        # expense is calculated and rolled to 2 digits

        if(len(str(expense)) >= spaces[4]):     #EXPENSE section space calc
            spaces[4] = len(str(expense)) + 2

        profit = round(gross - expense, 2)     
            # profit is calculated and rolled to 2 digits

        if(len(str(profit)) >= spaces[5]):      # PROFIT section space calc
            spaces[5] = len(str(profit)) + 2

        gross = round(gross / fiat, 2)
        expense = round(expense / fiat, 2)
        profit = round(gross - expense, 2)

        x = line("",dual_name, "-", gross, expense, profit)
            # Preparing new line for current card's current algorithm

        local_lines.append(x)   # and adding to temp list
    
    local_lines.sort(key=get_key,reverse=True)
        # Sorting to see which algorithm is the most profitable one

    num = new_element.num_of_algos()
    if(num == 1 or num == 2):      # Adding card name !Visual!
        local_lines[0].card = new_element.card_name
    elif(int(num / 2) % 2 == 0):    # if number of algos is even
        local_lines[int(num / 2) - 1].card = new_element.card_name
    else:
        local_lines[int(num / 2)].card = new_element.card_name

    for i in local_lines:       # When all sorted and name added, 
        lines.append(i)         # Adding all lines to main list

    dashed_line()    # Dashed line for to specify this is the end of the card

for i in range(0,len(lines)):           # Printing all lines
    create_line(lines[i], [a for a in spaces])