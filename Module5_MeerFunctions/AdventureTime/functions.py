import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount/10

def silver2gold(amount:int) -> float:
    return amount/5

def copper2gold(amount:int) -> float:
    #return amount/50
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return amount*25

def getPersonCashInGold(personCash:dict) -> float:
    p2g = personCash["platinum"]
    s2g = personCash["silver"]
    c2g = personCash["copper"]
    gold = personCash["gold"]
    platG = platinum2gold(p2g)
    silvG = silver2gold(s2g)
    coppG = copper2gold(c2g)
    totalGold = gold + platG + silvG + coppG

    return totalGold

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    journeyCost = ((COST_FOOD_HUMAN_COPPER_PER_DAY * people) + (COST_FOOD_HORSE_COPPER_PER_DAY * horses)) * JOURNEY_IN_DAYS
    return round(copper2gold(journeyCost),2)
##################### M04.D02.O5 #####################
# key 'round' value True
# if element[key] == True
def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    newList = []
    for element in list:
        if element[key] == value:
            newList.append(element)
    return newList
 
def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    list = getShareWithFriends(friends)
    list = getAdventuringPeople(list)
    return list

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    horses = (math.ceil(people /2))
    return horses

def getNumberOfTentsNeeded(people:int) -> int:
    tents = (math.ceil(people /3))
    return tents

def getTotalRentalCost(horses:int, tents:int) -> float:
    horseCostS = (COST_HORSE_SILVER_PER_DAY * horses) * JOURNEY_IN_DAYS
    tentCost = (COST_TENT_GOLD_PER_WEEK * tents) * math.ceil(JOURNEY_IN_DAYS/7)
    return tentCost + silver2gold(horseCostS)

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    newList = []
    for item in items:
        itemtxt = f"{item['amount']}{item['unit']} {item['name']}"
        newList.append(itemtxt)
    return ', '.join(newList)

def getItemsValueInGold(items:list) -> float:
    totalGold = 0
    for item in items:
        if item["price"]["type"] == "copper":
            totalGold += copper2gold(item["price"]["amount"] * item["amount"])
        elif item["price"]["type"] == "silver":
            totalGold += silver2gold(item["price"]["amount"] * item["amount"])
        elif item["price"]["type"] == "gold":
            totalGold += item["price"]["amount"] * item["amount"]
        elif item["price"]["type"] == "platinum":
            totalGold += platinum2gold(item["price"]["amount"] * item["amount"])
    return totalGold

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    totalGold = 0
    for element in people:
        totalGold += copper2gold(element["cash"]["copper"])
        totalGold += silver2gold(element["cash"]["silver"])
        totalGold += (element["cash"]["gold"])
        totalGold += platinum2gold(element["cash"]["platinum"])
    return round(totalGold,2)

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()