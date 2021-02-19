from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import random

list = os.listdir("/Users/tarkanbatar/Desktop/tarkan")  # dir is your directory path
number_files = len(list)
print(number_files - 1)
print(list)

fileNumber = number_files - 1
fileContent = []
t = 1

def pageScroller(a):
    while(time.time() - a < 180):
        html = driver.find_element_by_tag_name('html')
        time.sleep(2)
        for w in range(45):
            html.send_keys(Keys.ARROW_DOWN)
        html.send_keys(Keys.PAGE_DOWN)
        for q in range(45):
            html.send_keys(Keys.ARROW_UP)

def fileOpener(k):
    textFile = open("/Users/tarkanbatar/Desktop/tarkan/%d.txt" % k, "r")
    lines = textFile.read().splitlines()
    return lines


for i in range(fileNumber):
    fileContent.append(fileOpener(t))
    t += 1

while True:
    for n in range(fileNumber):
        random.shuffle(fileContent[n])
        print(fileContent[n])


    options = webdriver.ChromeOptions()
    options.add_extension('./cknebhggccemgcnbidipinkifmmegdel.crx')
    driver = webdriver.Chrome(options=options)
    driver.get("chrome-extension://cknebhggccemgcnbidipinkifmmegdel/html/welcome.html")
    time.sleep(3)

    extensionAccept = driver.find_element_by_id("accept")
    driver.window_handles[0]
    extensionAccept.click()
    time.sleep(3)

    driver.window_handles[1]
    driver.switch_to_window(driver.window_handles[0])
    driver.get(fileContent[0][0])

    for k in range(fileNumber - 2):
        driver.execute_script("window.open('');")
        driver.window_handles[k + 2]
        driver.switch_to_window(driver.window_handles[k + 2])


    for p in range(fileNumber):
        lineNum = len(fileContent[p])

        for b in range(lineNum):
            for t in range(fileNumber):
                driver.switch_to_window(driver.window_handles[t])
                time.sleep(1)
                driver.get(fileContent[t][b])
                time.sleep(2)

            for s in range(fileNumber):
                driver.switch_to_window(driver.window_handles[s])
                time.sleep(2)
                time_start = time.time()
                pageScroller(time_start)













# BU BİTİNCE BAŞLANGIÇ SAYFASINDA OLACAK

# start_time = time.time()
# for j in range(fileNumber):
#     x = 0
#     driver.switch_to_window(driver.window_handles[j])
#     while x < len(fileContent[j]):
#         driver.get(fileContent[j][x+1])
#         while (time.time() - start_time < 10):
#             html = driver.find_element_by_tag_name('html')
#             html.send_keys(Keys.END)
#             html.send_keys(Keys.PAGE_UP)
#         x+=1

