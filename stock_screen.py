import requests
import getpass
from pprint import pprint
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

c_options = webdriver.ChromeOptions()
c_options.add_experimental_option("detach", True)
file1 = open("US_full_stocklist.txt", "r")
file2 = open("Watchlist_raw_3rd_iter.txt", "a")

# url = "https://www.jitta.com/home"
url = "https://accounts.jitta.com/login?applicationName=jittadotcoms&redirectUrl=/stock/nyse:nke/factsheet"
chromepath = "/Users/adisu/Oracle Content - Accounts/Oracle Content/Documents/chromedriver"

i = 0
list1_400 = []
list2_400 = []
list3_400 = []
list4_400 = []
list5_400 = []
list6_400 = []
list7_400 = []
list8_400 = []
list9_400 = []
list10_400 = []
list11_400 = []
list12_400 = []
list13_400 = []
list14_400 = []
list15_400 = []
list16_400 = []

master_list = []
for item in file1.readlines():
    item = item.strip()
    if i < 401:
        list1_400.append(item)
    elif i < 801:
        list2_400.append(item)
    elif i < 1201:
        list3_400.append(item)
    elif i < 1601:
        list4_400.append(item)
    elif i < 2001:
        list5_400.append(item)
    elif i < 2401:
        list6_400.append(item)
    elif i < 2801:
        list7_400.append(item)
    elif i < 3201:
        list8_400.append(item)
    elif i < 3601:
        list9_400.append(item)
    elif i < 4001:
        list10_400.append(item)
    elif i < 4401:
        list11_400.append(item)
    elif i < 4801:
        list12_400.append(item)
    elif i < 5201:
        list13_400.append(item)
    elif i < 5601:
        list14_400.append(item)
    elif i < 6001:
        list15_400.append(item)
    else:
        list16_400.append(item)
    i+=1

master_list.extend([list1_400,list2_400,list3_400,list4_400,list5_400,list6_400,list7_400,list8_400,list9_400,list10_400,list11_400,list12_400,list13_400,list14_400,list15_400,list16_400])
# pprint(master_list)

def jiracheck():
    for monkey in master_list:
        print(monkey)
        # jiracheck()
        print("#########start_check_jira_py###########")
        '''
        This file logs on to https://jira-sd.uk-gov-london-1.oraclegoviaas.uk/projects/NETINFRA/queues/custom/2607 and scrapes information.
        '''
        s = Service(executable_path=chromepath)
        driver = webdriver.Chrome(options=c_options, service=s)
        driver.get(url)
        time.sleep(4)
        # print(driver.title)
        login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[7]/button[1]")
        time.sleep(3)
        email = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[5]/div/input")
        # email.send_keys("ispfyazaqjrzrmzxnp@bvhrk.com")
        email.send_keys("disu.ayotunde@gmail.com")
        # email.send_keys("disu_ayotunde@yahoo.com")
        passwords = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[6]/div/input")
        passwords .send_keys("Wh@t15J1tt@?")
        # passwords.send_keys("Wh@t15J1tta?")
        login.click()
        time.sleep(3)
        homepage = driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div[1]/div/div/div[1]/div/div/a")
        homepage.click()
        time.sleep(3)
        USA = driver.find_element(By.XPATH,
                                  "/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/div/div[1]/a/div/div/div[1]")
        USA.click()
        time.sleep(4)
        Stock_search = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[3]/div/input")
        time.sleep(4)
        for element in monkey:

            element = element.strip()
            # print(element)
            try:
                Stock_search.send_keys(element)
                time.sleep(3)
                Stock_search.send_keys(Keys.ENTER)
                time.sleep(9)
                factsheet = driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div/div[1]/a[2]")
                factsheet.click()
                time.sleep(7)
            except:
                Stock_search.send_keys(Keys.BACKSPACE)
                Stock_search.send_keys(Keys.BACKSPACE)
                Stock_search.send_keys(Keys.BACKSPACE)
                Stock_search.send_keys(Keys.BACKSPACE)
                Stock_search.send_keys(Keys.BACKSPACE)
                Stock_search.send_keys(Keys.BACKSPACE)
                Stock_search.send_keys(Keys.BACKSPACE)

                print(f"fatal error in {element}")
            try:
                datapoint_9 = driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/div/div[3]/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[1]/button/span")
                datapoint_8 = driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/div/div[3]/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[2]/button/span")
                datapoint_7 = driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/div/div[3]/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[3]/button/span")
                datapoint_6 = driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/div/div[3]/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[4]/button/span")
                datapoint_5 = driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/div/div[3]/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[5]/button/span")
                datapoint_4 = driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/div/div[3]/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[6]/button/span")
                datapoint_3 = driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/div/div[3]/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[7]/button/span")
                datapoint_2 = driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/div/div[3]/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[8]/button/span")
                datapoint_1 = driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/div/div[3]/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[9]/button/span")

                if "-" in datapoint_9.text.strip("%"):
                     print(".....\n")
                elif "-" in datapoint_8.text.strip("%"):
                     print(".....\n")
                elif "-" in datapoint_7.text.strip("%"):
                    print(".....\n")
                elif "-" in datapoint_6.text.strip("%"):
                    print(".....\n")
                elif "-" in datapoint_5.text.strip("%"):
                    print(".....\n")
                elif "-" in datapoint_4.text.strip("%"):
                    print(".....\n")
                elif "-" in datapoint_3.text.strip("%"):
                    print(".....\n")
                elif "-" in datapoint_2.text.strip("%"):
                    print(".....\n")
                elif "-" in datapoint_1.text.strip("%"):
                    print(".....\n")
                else:
                    datapoint_9 = float(datapoint_9.text.strip("%"))
                    datapoint_8 = float(datapoint_8.text.strip("%"))
                    datapoint_7 = float(datapoint_7.text.strip("%"))
                    datapoint_6 = float(datapoint_6.text.strip("%"))
                    datapoint_5 = float(datapoint_5.text.strip("%"))
                    datapoint_4 = float(datapoint_4.text.strip("%"))
                    datapoint_3 = float(datapoint_3.text.strip("%"))
                    datapoint_2 = float(datapoint_2.text.strip("%"))
                    datapoint_1 = float(datapoint_1.text.strip("%"))
                    # print(datapoint_1)
                    # print(type(datapoint_1))
                    # print(datapoint_1,datapoint_2,datapoint_3,datapoint_4,datapoint_5,datapoint_6,datapoint_7,datapoint_8,datapoint_9)
                    if datapoint_1 > 4 and datapoint_2 > 2.9 and datapoint_3 > 4 and datapoint_4 > 4 and datapoint_5 > 4 and datapoint_6 > 4 and datapoint_7 > 4 and datapoint_8 > 2.9 and datapoint_9 > 2.9:
                        print(element)
                        file2.writelines(f"This {element} looks good. 2013 ROIC :{datapoint_9}, 2014 ROIC :{datapoint_8}, 2015 ROIC :{datapoint_7}, 2016 ROIC :{datapoint_6}, 2017 ROIC : {datapoint_5}, 2018 ROIC : {datapoint_4}, 2019 ROIC : {datapoint_3}, 2020 ROIC : {datapoint_2}, 2021 ROIC : {datapoint_1}\n")

                    else:
                        print(".....\n")
            except:
                print(f"Fatal Error on {element}")


            # print(driver.title)

            # usernames = driver.find_element(By.NAME, "username")
            # usernames.send_keys("adisu")
            # password = driver.find_element(By.NAME, "password")
            # password.send_keys(f"{passwords}")
            # password.send_keys(Keys.ENTER)
            # time.sleep(3)


jiracheck()
file1.close()
file2.close()
