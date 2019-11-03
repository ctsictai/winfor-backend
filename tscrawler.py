import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "winforgg.settings")
import django
django.setup()
import json

from tierstats.models import Tierstat
from selenium import webdriver

def tierstat_crawler():
    chromedriver = '/home/kykevin/Downloads/chromedriver'
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.op.gg/statistics/tier/")
    tiers = driver.find_elements_by_xpath(f"""//tbody/tr/td[2]""")
    summoners = driver.find_elements_by_xpath(f"""//tbody/tr/td[3]""")
    aggregates = driver.find_elements_by_xpath(f"""//tbody/tr/td[4]""")

    tier_name = []
    tier_roman = []
    summoner_count = []
    summoner_percentage = []
    aggregate_count = []
    aggregate_percentage = []
  
    for item in tiers:
        a = item.text
        b = a.split(" ", maxsplit=1)
        tier_name.append(b[0])
        tier_roman.append(b[1])

    for item in summoners:
        a = item.text
        b = a.split(" ", maxsplit=1)
        c = b[1][1:b[1].find("%")]
        d = b[0].replace(",","")
        e = int(d)
        f = float(c)
        summoner_count.append(e)
        summoner_percentage.append(f)

    for item in aggregates:
        a = item.text
        b = a.split(" ", maxsplit=1)
        c = b[1][1:b[1].find("%")]
        d = b[0].replace(",","")
        e = int(d)
        f = float(c)
        aggregate_count.append(e)
        aggregate_percentage.append(f)
    
    tierstats_list = []
    for n in range(len(tiers)):
        tierstat_object = Tierstat(
            tier = tier_name[n],
            tier_numbers = tier_roman[n],
            summoner = summoner_count[n],
            summoner_percent = summoner_percentage[n],
            aggregate = aggregate_count[n],
            aggregate_percent = aggregate_percentage[n],
        )
        tierstats_list.append(tierstat_object)                              
    Tierstat.objects.bulk_create(tierstats_list)

if __name__ == '__main__' :
    tierstat_crawler()
