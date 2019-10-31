from selenium import webdriver
browser = webdriver.Chrome()

chromedriver = '/home/kykevin/Downloads/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.op.gg/statistics/tier/")

tier = driver.find_elements_by_xpath(f"""//tbody/tr/td[2]""")
summoner = driver.find_elements_by_xpath(f"""//tbody/tr/td[3]""")
aggregate = driver.find_elements_by_xpath(f"""//tbody/tr/td[4]""")

tiers = []
tiers_roman = []
summoners = []
summoners_percent = []
aggregates = []
aggregates_percent = []

for item in tier:
    a = item.text
    b = a.split(" ", maxsplit=1)
    tiers.append(b[0])
    tiers_roman.append(b[1])

for item in summoner:
    a = item.text
    b = a.split(" ", maxsplit=1)
    c = b[1][1:b[1].find("%")]
    summoners.append(b[0])
    summoners_percent.append(c)

print(summoners)
print(summoners_percent)


