from selenium  import webdriver
import time
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'winforgg.settings')
import django
django.setup()
from stat_cham.models import Stat_champions  
from champions.models import Champions

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='/home/taesoon/chromedriver/chromedriver', chrome_options=chrome_options)
driver.get("https://www.op.gg/statistics/champion/")
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="recent_today"]/span').click()

ranks = driver.find_elements_by_css_selector("#ChampionStatsTable > table > tbody > tr > td.Cell.Rank")

ranks_list = []
for rank in ranks:    
    ranks_list.append(int(rank.text))

print(ranks_list)
champions = driver.find_elements_by_css_selector("#ChampionStatsTable > table > tbody > tr > td.Cell.ChampionName > a")

champions_list = []

for champion in champions:
    champis = Champions.objects.get(champion_name = champion.text)
    champions_list.append(champis.id)
#print(champions_list)

win_rates = driver.find_elements_by_css_selector("#ChampionStatsTable > table > tbody > tr > td:nth-child(4) > span ")
win_rates_list = []
for win_rate in win_rates:
    wi = win_rate.text.replace('.',"")
    win_rate_text = win_rate.text.replace('%',"")
    win_rates_list.append(float(win_rate_text))

#print(win_rates_list)

player_counts = driver.find_elements_by_css_selector("#ChampionStatsTable > table > tbody > tr > td:nth-child(5)")

player_counts_list = []
for player_count in player_counts:
    if player_count.text.find(','):
       player_count =  player_count.text.replace(',','')
    else:
       player_count.text
    player_counts_list.append(int(player_count))

#print(player_counts_list)
scores = driver.find_elements_by_css_selector("#ChampionStatsTable > table > tbody > tr > td.Cell.KDARatio > span")

scores_list = []
for score in scores:
    scores_list.append(score.text)

#print(scores_list)

css = driver.find_elements_by_css_selector("#ChampionStatsTable > table > tbody > tr > td:nth-child(7) > span")

cs_list = []
for cs in css:
    cs_list.append(float(cs.text))

#print(cs_list)

golds = driver.find_elements_by_css_selector("#ChampionStatsTable > table > tbody > tr > td:nth-child(8) > span")

golds_list = []
for gold in golds:
    if gold.text.find(','):
       goldsc = gold.text.replace(',','')
    else:
       goldsc = gold.text
    golds_list.append(int(goldsc))

print(golds_list)

driver.quit()

for i in range(len(golds_list)-1):
    Stat_champions(
            champions      = Champions.objects.get(id=champions_list[i]),
            win_rates      = win_rates_list[i],
            player_numbers = player_counts_list[i],
            kda            = scores_list[i],
            cs_average     = cs_list[i],
            gold_average   = golds_list[i],
            rank           = ranks_list[i],
        ).save()

    

