import threading,requests,json
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import random,schedule

def job1(url_Article,cookie,window_1):
    print('继续学习，阅读一篇文章获得1分，上限6分')
    #Button_StatusList[1].click()、
    Number=random.choices(range(0,19))
    
    driver.get(url_Article)
    for c in cookie:
        driver.add_cookie(c)
    driver.refresh()
    contents = driver.find_elements_by_id('C9djoy7fjv7400')
    for item in contents[:1]: 
        item.click()

        
        time.sleep(120)
   # driver.close()
    

def job2(url_ShotVideo,cookie,window_1):
    
    driver.get(url_ShotVideo)
    for c in cookie:
        driver.add_cookie(c)
    driver.refresh()
    driver.find_element_by_id('Ck3ln2wlyg3k00').click()
    time.sleep(60)
    driver.close()
    

def job3(url_Article,cookie,window_1):
    print('继续学习，阅读一篇文章每累计4分钟获得1分，上限8分')
    #Button_StatusList[1].click()、
    driver.get(url_Article)
    for c in cookie:
        driver.add_cookie(c)
    driver.refresh()
    driver.find_elements_by_id('C9djoy7fjv7400').click
    time.sleep(300)
    driver.close()


def job4(url_LongVideo,cookie,window_1):
    
    driver.get(url_LongVideo)
    for c in cookie:
        driver.add_cookie(c)
    driver.refresh()
    driver.find_element_by_id('Ce41u7czkg8o0').click()
    time.sleep(2000)
    driver.close()    

#def job(Button_StatusList,cookie):   
 


    
    #if i == 0:
    #    print("已完成今天的学习任务")


if __name__ == "__main__":
    location = 'C:\\FirefoxPortable\\App\\Firefox64\\firefox.exe'
    driver = webdriver.Firefox(firefox_binary=location)
    driver.maximize_window()

    url_xuexi = 'https://pc.xuexi.cn/points/my-points.html'
    url_Article='https://www.xuexi.cn/d05cad69216e688d304bb91ef3aac4c6/9a3668c13f6e303932b5e0e100fc248b.html'
    url_ShotVideo = 'https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html'
    url_LongVideo='https://www.xuexi.cn/8e35a343fca20ee32c79d67e35dfca90/7f9f27c65e84e71e1b7189b7132b4710.html'
    driver.get(url_xuexi)
    window_1 = driver.current_window_handle
    time.sleep(20)
    cookie = driver.get_cookies()
    f1 = open('cookie.txt','w')
    f1.write(json.dumps(cookie))
    f1.close()

    driver.get(url_xuexi)
    time.sleep(20)

    Button_StatusList = driver.find_elements_by_class_name('big')
    #i=0   # Flag for number of not finished tasks
    if Button_StatusList[3].text !="已完成" :
        #i=i+1 
        driver.switch_to.window(window_1)
        #Button_StatusList[3].click()       
        driver.find_element_by_id('C4ats065rhr800').click()
        time.sleep(120)
    else:
        print('3 已完成长时间阅读文章任务！') 
        
    if Button_StatusList[1].text !="已完成" :
        print('继续学习，阅读一篇文章获得1分，上限6分')
        driver.switch_to.window(window_1)
        Button_StatusList[1].click()    
    #Button_StatusList[1].click()、          
        random.choice(driver.find_elements_by_id('C4ats065rhr800')).click()
        time.sleep(60)

    else:
        print('1 已完成阅读文章任务！')  

    if Button_StatusList[4].text !="已完成" :
        driver.switch_to.window(window_1)  
       # i=i+1
        print('继续学习，观看视频每累计5分钟，获得1分，上限10分')
        i=0
        for item in driver.find_elements_by_class_name('big'):
            if i==4 :
                item.click()           
            driver.find_elements_by_id('C9djoy7fjv7400').click()
            i=i+1
        time.sleep(2000)
        
    else:
        print('4 已完成长时间观看视频任务！') 

    if Button_StatusList[2].text !="已完成" :
        driver.switch_to.window(window_1) 
        print('2. 继续学习，观看一个视频获得1分，上限6分')
        driver.find_element_by_link_text('学习强国').click() 
        time.sleep(10)    
#html body#app div.content div.screen div#Cjnt8afuclko00 div#Cl1pel7oatvk00 div#C2zy9omm9m7800 div#Cdnz3vc593e000.div-background-img-stretching div#C569w84z4l4c00 div#C9z3zznpkm8k00 div#C45g3rqpd9l000 div#Cgfgrgxetdr400 div#Cgul4rdu9kww00.background-img-stretching.largen_image.lazy
#html body#app div.content div.screen div#C9djoy7fjv7400 div#Caepwflu1h6800 div#Ced5lslw30ig00 div#Ce5n9m4qye1s00 div#Chz65a0d3rrc00 div div#C1dctbkougneo0 div#Ck3ln2wlyg3k00.word-item

        driver.find_element_by_id('Cgul4rdu9kww00').click()
        time.sleep(10)
        driver.find_elements_by_id('Ck3ln2wlyg3k00').click()        
        time.sleep(200)
        #i=i+1
        #Button_StatusList[2].click()
        #job2(url_ShotVideo,cookie,window_1)
        
    else:
        print('2 已完成观看短视频任务！') 




    
    
    #schedule.every().day.at("6:10").do(job,cookie)
    #schedule.every().day.at("6:40").do(job,cookie)
    #schedule.every().day.at("12:10").do(job)
    #schedule.every().day.at("20:10").do(job) 

