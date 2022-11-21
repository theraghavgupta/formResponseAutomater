from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import random
from indian_cities.dj_city import cities

df = pd.read_csv('Data.csv')
driver = webdriver.Chrome()
driver.get("https://forms.gle/MKFVzxcF4zxJ2iqK9")
time.sleep(2)
for i in range(0,232):
    name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    age = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    place = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    next_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    name.send_keys(df.loc[i,"Name"])
    email.send_keys(df.loc[i,"Email Id"])
    age.send_keys(str(df.loc[i,"Age"]))
    place.send_keys(cities[random.randint(0,33)][1][0][0])

    next_button.click()
    
    time.sleep(2)
    
    excite_type = random.choice([1,1,1,2,2,3,3,3,4,4,5])
    if excite_type == 1:
        excite_radio = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]')
    elif excite_type == 2:
        excite_radio = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]')
    elif excite_type == 3:
        excite_radio = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]')
    elif excite_type == 4:
        excite_radio = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]')
    else:
        excite_radio = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]')

        
    visited_type = random.choice([1,1,1,2,2,2,3,3,4,5,5])
    if visited_type == 1:
        visited_radio = driver.find_element(By.XPATH,'//*[@id="i9"]/div[3]')
    elif visited_type == 2:
        visited_radio = driver.find_element(By.XPATH,'//*[@id="i12"]/div[3]')
    elif visited_type == 3:
        visited_radio = driver.find_element(By.XPATH,'//*[@id="i15"]/div[3]')
    elif visited_type == 4:
        visited_radio = driver.find_element(By.XPATH,'//*[@id="i18"]/div[3]')
    else:
        visited_radio = driver.find_element(By.XPATH,'//*[@id="i21"]/div[3]')

    mordern_type = random.choice([1,2,2,4,4,3,4])
    if mordern_type==1:
        mordern_radio = driver.find_element(By.XPATH,'//*[@id="i28"]/div[3]')
    elif mordern_type==2:
        mordern_radio = driver.find_element(By.XPATH,'//*[@id="i31"]/div[3]')
    elif mordern_type==3:
        mordern_radio = driver.find_element(By.XPATH,'//*[@id="i34"]/div[3]')
    else:
        mordern_radio = driver.find_element(By.XPATH,'//*[@id="i37"]/div[3]')
    
    research_type = random.choice([1,1,2,3,3])
    if research_type==1:
        research_radio = driver.find_element(By.XPATH,'//*[@id="i44"]/div[3]')
    elif research_type==2:
        research_radio = driver.find_element(By.XPATH,'//*[@id="i47"]/div[3]')
    else:
        research_radio = driver.find_element(By.XPATH,'//*[@id="i50"]/div[3]')
    
    roman_type = random.choice([1,2,2,3,4,1,4,4])
    if roman_type == 1:
        roman_radio = driver.find_element(By.XPATH,'//*[@id="i57"]/div[3]')
    elif roman_type == 2:
        roman_radio = driver.find_element(By.XPATH,'//*[@id="i60"]/div[3]')
    elif roman_type == 3:
        roman_radio = driver.find_element(By.XPATH,'//*[@id="i63"]/div[3]')
    else:
        roman_radio = driver.find_element(By.XPATH,'//*[@id="i66"]/div[3]')

    chinese_type = random.choice([1,1,2,1,3,4])
    if chinese_type==1:
        chinese_radio = driver.find_element(By.XPATH,'//*[@id="i73"]/div[3]')
    elif chinese_type==2:
        chinese_radio = driver.find_element(By.XPATH,'//*[@id="i76"]/div[3]')
    elif chinese_type==3:
        chinese_radio = driver.find_element(By.XPATH,'//*[@id="i79"]/div[3]')
    else:
        chinese_radio = driver.find_element(By.XPATH,'//*[@id="i82"]/div[3]')
    
    geometry_type = random.choice([1,2,2,1,1,3,4,4])
    if geometry_type==1:
        geometry_radio = driver.find_element(By.XPATH,'//*[@id="i89"]/div[3]')
    elif geometry_type==2:
        geometry_radio = driver.find_element(By.XPATH,'//*[@id="i92"]/div[3]')
    elif geometry_type==3:
        geometry_radio = driver.find_element(By.XPATH,'//*[@id="i95"]/div[3]')
    else:
        geometry_radio = driver.find_element(By.XPATH,'//*[@id="i98"]/div[3]')
    
    nile_type = random.choice([1,2,3,2,2,2,4])
    if nile_type==1:
        nile_radio = driver.find_element(By.XPATH,'//*[@id="i105"]/div[3]')
    if nile_type==2:
        nile_radio = driver.find_element(By.XPATH,'//*[@id="i108"]/div[3]')
    if nile_type==3:
        nile_radio = driver.find_element(By.XPATH,'//*[@id="i111"]/div[3]')
    else:
        nile_radio = driver.find_element(By.XPATH,'//*[@id="i114"]/div[3]')

    mosque_type = random.choice([1,2,3,3,2,3,1,4])
    if mosque_type==1:
        mosque_radio = driver.find_element(By.XPATH,'//*[@id="i121"]/div[3]')
    elif mosque_type==2:
        mosque_radio = driver.find_element(By.XPATH,'//*[@id="i124"]/div[3]')
    elif mosque_type==3:
        mosque_radio = driver.find_element(By.XPATH,'//*[@id="i127"]/div[3]')
    else:
        mosque_radio = driver.find_element(By.XPATH,'//*[@id="i130"]/div[3]')

    vihara_type = random.choice([1,2,3,1,1])
    if vihara_type==1:
        vihara_radio = driver.find_element(By.XPATH,'//*[@id="i137"]/div[3]')
    elif vihara_type==2:
        vihara_radio = driver.find_element(By.XPATH,'//*[@id="i140"]/div[3]')
    elif vihara_type==3:
        vihara_radio = driver.find_element(By.XPATH,'//*[@id="i143"]/div[3]')
    else:
        vihara_radio = driver.find_element(By.XPATH,'//*[@id="i146"]/div[3]')
    
    father_type = random.choice([1,2,1,1,2,4,3,4])
    if father_type==1:
        father_radio = driver.find_element(By.XPATH,'//*[@id="i153"]/div[3]')
    elif father_type==2:
        father_radio = driver.find_element(By.XPATH,'//*[@id="i156"]/div[3]')
    elif father_type==3:
        father_radio = driver.find_element(By.XPATH,'//*[@id="i159"]/div[3]')
    else:
        father_radio = driver.find_element(By.XPATH,'//*[@id="i162"]/div[3]')

    rockcut_type = random.choice([1,2,2,1,4,2,3,4])
    if rockcut_type==1:
        rockcut_radio = driver.find_element(By.XPATH,'//*[@id="i169"]/div[3]')
    elif rockcut_type==2:
        rockcut_radio = driver.find_element(By.XPATH,'//*[@id="i172"]/div[3]')
    elif rockcut_type==3:
        rockcut_radio = driver.find_element(By.XPATH,'//*[@id="i175"]/div[3]')
    else:
        rockcut_radio = driver.find_element(By.XPATH,'//*[@id="i178"]/div[3]')

    priests_type = random.choice([1,4,4,4,1,2,2,3,4])
    if priests_type==1:
        priests_radio = driver.find_element(By.XPATH,'//*[@id="i185"]/div[3]')
    elif priests_type==2:
        priests_radio = driver.find_element(By.XPATH,'//*[@id="i188"]/div[3]')
    elif priests_type==3:
        priests_radio = driver.find_element(By.XPATH,'//*[@id="i191"]/div[3]')
    else:
        priests_radio = driver.find_element(By.XPATH,'//*[@id="i194"]/div[3]')

    kochi_type = random.choice([1,2,4,4,1,1,3,4])
    if kochi_type == 1:
        kochi_radio = driver.find_element(By.XPATH,'//*[@id="i201"]/div[3]')
    elif kochi_type == 2:
        kochi_radio = driver.find_element(By.XPATH,'//*[@id="i204"]/div[3]')
    elif kochi_type == 3:
        kochi_radio = driver.find_element(By.XPATH,'//*[@id="i207"]/div[3]')
    else:
        kochi_radio = driver.find_element(By.XPATH,'//*[@id="i210"]/div[3]')

    rock_type = random.choice([1,2,3,3,3,4])
    if rock_type==1:
        rock_radio = driver.find_element(By.XPATH,'//*[@id="i217"]/div[3]') 
    elif rock_type==2:
        rock_radio = driver.find_element(By.XPATH,'//*[@id="i220"]/div[3]') 
    elif rock_type==3:
        rock_radio = driver.find_element(By.XPATH,'//*[@id="i223"]/div[3]') 
    else:
        rock_radio = driver.find_element(By.XPATH,'//*[@id="i226"]/div[3]')

    india_type = random.choice([1,4,4,2,2,3,4])
    if india_type==1:
        india_radio = driver.find_element(By.XPATH,'//*[@id="i233"]/div[3]')
    elif india_type==2:
        india_radio = driver.find_element(By.XPATH,'//*[@id="i236"]/div[3]')
    elif india_type==3:
        india_radio = driver.find_element(By.XPATH,'//*[@id="i239"]/div[3]')
    else:
        india_radio = driver.find_element(By.XPATH,'//*[@id="i242"]/div[3]')
    
    stupa_type = random.choice([1,2,4,4,3,4])
    if stupa_type==1:
        stupa_radio = driver.find_element(By.XPATH,'//*[@id="i249"]/div[3]')
    elif stupa_type==2:
        stupa_radio = driver.find_element(By.XPATH,'//*[@id="i252"]/div[3]')
    elif stupa_type==3:
        stupa_radio = driver.find_element(By.XPATH,'//*[@id="i255"]/div[3]')
    else:
        stupa_radio = driver.find_element(By.XPATH,'//*[@id="i258"]/div[3]')
    
    
    egypt_type = random.choice([1,2,2,2,1,4,3,4])
    if egypt_type==1:
        egypt_radio = driver.find_element(By.XPATH,'//*[@id="i265"]/div[3]')
    elif egypt_type==2:
        egypt_radio = driver.find_element(By.XPATH,'//*[@id="i268"]/div[3]')
    elif egypt_type==3:
        egypt_radio = driver.find_element(By.XPATH,'//*[@id="i271"]/div[3]')
    else:
        egypt_radio = driver.find_element(By.XPATH,'//*[@id="i274"]/div[3]')

    
    submit_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')

    
    
    excite_radio.click()

    visited_radio.click()

    mordern_radio.click()

    research_radio.click()

    roman_radio.click()

    chinese_radio.click()

    geometry_radio.click()

    nile_radio.click()
    
    mosque_radio.click()
    
    vihara_radio.click()
    
    father_radio.click()
    
    rockcut_radio.click()
    
    priests_radio.click()
    
    kochi_radio.click()
    
    rock_radio.click()

    india_radio.click()

    stupa_radio.click()

    egypt_radio.click()
    
    time.sleep(4)
    submit_button.click()
    
    
    time.sleep(2)
    
    new_response = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    
    new_response.click()
    time.sleep(2)
