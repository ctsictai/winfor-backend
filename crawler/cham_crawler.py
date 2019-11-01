from selenium  import webdriver
import time
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'winforgg.settings')
import django
django.setup()
from champions.models import Champions   

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='/home/taesoon/chromedriver/chromedriver', chrome_options=chrome_options)
driver.get('https://gameinfo.leagueoflegends.co.kr/ko/game-info/champions/')
driver.implicitly_wait(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

cham_eles = driver.find_elements_by_tag_name('ul.champion-grid img.img')

browser = webdriver.Chrome(executable_path='/home/taesoon/chromedriver/chromedriver', chrome_options=chrome_options)
browser.get('https://www.leagueofgraphs.com/ko/')

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

cham_elems = browser.find_elements_by_css_selector('#championListBox > div > a > div.championName')

cham_img_urls = []
cham_names = []
for cham_ele in cham_eles:
    img_src = cham_ele.get_attribute('data-original')
    if img_src.endswith('png'):
        cham_img_urls.append(img_src)

for cham_elem in cham_elems:
   cham_names.append(cham_elem.text)

print(cham_img_urls)
print(cham_names)

driver.close()

champions = dict(zip(cham_names, cham_img_urls))
print(champions)

for key, value in champions.items():
    Champions(champion_name = key, champion_img_src = value).save()


