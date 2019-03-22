from selenium import webdriver
import time,json,random,os
from selenium.webdriver.firefox.options import Options


def job1():

    windows = driver.window_handles
    driver.switch_to.window(windows[0]) # 切换到学习强国主页主页
    time.sleep(10)
    selectedContents = random.sample(driver.find_elements_by_id('C3svnupj0auw00'),k=1)  # 
    for item in selectedContents:
        item.click()
        time.sleep(20)
    # driver.close()
   
def job2():
    
    windows = driver.window_handles
    driver.switch_to.window(windows[0])        
    driver.find_element_by_xpath('//label[text()="第一频道" and @class="radio-inline"]').click()   #第一频道
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    allTypes = random.sample(driver.find_elements_by_class_name('radio-inline'),k=1) 
    for oneType in allTypes :
        oneType.click()
    selectedContents = random.sample(driver.find_elements_by_id('Ck3ln2wlyg3k00'),k=1)
    for item in selectedContents:
        item.click()
        time.sleep(310)


def job3():

    windows = driver.window_handles
    driver.switch_to.window(windows[0])  
    driver.find_elements_by_id('Ca4gvo4bwg7400') # 综合新闻
    selectedContents = random.sample(driver.find_elements_by_id('Cnr0zbz511qo0'),k=1) 
    for item in selectedContents:
        item.click()
        time.sleep(150)

def job4():
    
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    #driver.find_element_by_id('Cbkq18r7b9i800').click() # 新闻联播
    driver.find_element_by_id('C43fanq5itq800').click() # 实播平台   
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    selectedContents = random.sample(driver.find_elements_by_id('Ck3ln2wlyg3k00'),k=1) # 实播平台/每日一讲 
    for item in selectedContents:
        item.click()
        time.sleep(350)   

 


    
    #if i == 0:
    #    print("已完成今天的学习任务")
def job():
    print(time.strftime('%Y.%m.%d.%H.%M.%S',time.localtime(time.time())))

    driver.get(url_home)
    #登陆主页面
    #cookie =readCookie()
    if os.path.exists('cookie.txt'):

        f1 = open('cookie.txt')
        cookie = f1.read()
        cookie =json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
    time.sleep(20)
    cookie = driver.get_cookies()
    f2 = open('cookie.txt','w')
    f2.write(json.dumps(cookie)) 
    f2.close()
    
    
    #检查积分情况
    driver.find_element_by_xpath('//div[text()="我的积分" and @id="Ck8773vhcvww00"]').click()
    time.sleep(5)
    windows =driver.window_handles
    driver.switch_to.window(windows[-1])
    driver.refresh()
    
    list=[]
    Button_StatusList = driver.find_elements_by_class_name('big')
    for item in Button_StatusList:
        print(item.text)
        list.append(item.text)

    time.sleep(5)
    i = 0
    if list[1] !="已完成" :
        print('1 继续学习，阅读一篇文章获得1分，上限6分')
        try:
            job1()
        except:
            print('there is issue with job1, continue to run other jobs')     
    else:
        print('1 已完成阅读文章任务，并获得6分！') 
        i=i+1
         
 
    if list[2]!="已完成" :
        print('2. 继续学习，观看一个视频获得1分，上限6分')
        
        try:
            job2()
        except:
            print('there is issue with job3, continue to run other jobs')
            
        
    else:
        print('2 已完成观看短视频任务,并获得6分！')
        i=i+1 
        
    if list[3] != "已完成" :
        print('3 继续学习，阅读一篇文章每累计4分钟获得1分，上限8分')
        try:
            job3()
        except:
            print('there is issue with job3, continue to run other jobs')
        
    else:
        print('3 已完成长时间阅读文章任务,并获得8分！') 
        i=i+1


    if list[4]!="已完成" :
        print('4 继续学习，观看视频每累计5分钟，获得1分，上限10分')
        try:
            job4()
        except:
            print('there is issue with job4, continue to run other jobs')

    else:
        print('4 已完成长时间观看视频任务,并获得10分！') 
        i=i+1
        
    if i ==4:
        print("完成今天的学习任务")
        driver.quit()  
        exit()


if __name__ == "__main__":
    
    firefox_options =Options()
    firefox_options.add_argument('--headless') 
    location = 'C:\\FirefoxPortable\\App\\Firefox64\\firefox.exe'
    if os.path.exists('cookie.txt'):
        driver = webdriver.Firefox(firefox_binary=location,options=firefox_options)
    else:
        driver = webdriver.Firefox(firefox_binary=location)    
        driver.maximize_window()

    url_home ='https://www.xuexi.cn/'
    i = 0
    for num in range (20):
        job()

