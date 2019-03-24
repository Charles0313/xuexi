from selenium import webdriver
import time,json,random,os
#from selenium.webdriver.firefox.options import Options

def job1():

    windows = driver.window_handles
    driver.switch_to.window(windows[0]) # 切换到学习强国主页主页
    time.sleep(10)
    articleID=getArticleID()
    selectedContents = random.sample(driver.find_elements_by_id(articleID),k=1)  # 
    for item in selectedContents:
        print(item.text)
        item.click()
        startXuexi1()
        time.sleep(200)
   
def job2():
    
    windows = driver.window_handles
    driver.switch_to.window(windows[0])        
    driver.find_element_by_xpath('//label[text()="第一频道" and @class="radio-inline"]').click()   #第一频道
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    Flag = True
    while Flag:
        allTypes = random.sample(driver.find_elements_by_class_name('radio-inline'),k=1)
        if allTypes[0].text !="电影频道":
            Flag = False
        allTypes[0].click()
    selectedContents = random.sample(driver.find_elements_by_id('Ck3ln2wlyg3k00'),k=1)
    for item in selectedContents:
        print(item.text)
        item.click()
        startXuexi2()
        time.sleep(260)


def job3():

    windows = driver.window_handles
    driver.switch_to.window(windows[0])   
    windows = driver.window_handles
    driver.switch_to.window(windows[0]) # 切换到学习强国主页主页
    time.sleep(10)
    articleID=getArticleID()
    selectedContents = random.sample(driver.find_elements_by_id(articleID),k=1)  # 
    for item in selectedContents:
        print(item.text)
        item.click()
        startXuexi1()
        time.sleep(160)


def job4():
    
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    #driver.find_element_by_id('Cbkq18r7b9i800').click() # 新闻联播
    driver.find_element_by_xpath('//label[text()="第一频道" and @class="radio-inline"]').click()   #第一频道
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    Flag = True
    while Flag:
        allTypes = random.sample(driver.find_elements_by_class_name('radio-inline'),k=1)
        if allTypes[0].text !="电影频道":
            Flag = False

    allTypes[0].click()
    selectedContents = random.sample(driver.find_elements_by_id('Ck3ln2wlyg3k00'),k=1)
    for item in selectedContents:
        print(item.text)
        item.click()
        startXuexi2()
        time.sleep(310)
    
def getArticleID():
    id_list=['C70ngaew6trg00','Ckhjp4r149s000','C3svnupj0auw00','Cex2abil2z7s00','Ckhjp4r149s000','C4ats065rhr800','C3svnupj0auw00','Cg6gdmyi3p3400']
    selectedID = random.sample(id_list,k=1)
    for id in selectedID:
        return id 

def startXuexi1():
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    js_org = "var q=document.documentElement.scrollTop="
    for a in range(5):
        js=js_org+str(a*200)
        driver.execute_script(js)
        time.sleep(10)

def startXuexi2():
    windows = driver.window_handles
    driver.switch_to.window(windows[2])
    js_org = "var q=document.documentElement.scrollTop="
    for a in range(5):
        js=js_org+str(a*200)
        driver.execute_script(js)
        time.sleep(10)

def job():
    print(time.strftime('%Y.%m.%d  %H:%M:%S',time.localtime(time.time())))
    driver.get(url_home)

    #登陆主页面    
    if os.path.exists('cookie.txt'):
        f1 = open('cookie.txt')
        cookie = f1.read()
        cookie =json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
    
    else:
        print('请尽快扫描二维码登陆网站')
        time.sleep(15)
        driver.refresh()
        time.sleep(5)   
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
    #C70ngaew6trg00
    list=[]
    Button_StatusList = driver.find_elements_by_class_name('big')
    for item in Button_StatusList:
        print(item.text)
        list.append(item.text)
    
    if os.path.exists('cookie.txt') and len(list)==0  :
        print("请重新运行该程序!")
        #os.remove('cookie.txt')
        driver.quit()
        exit()

    time.sleep(5)
    i = 0
    if list[1] !="已完成" :
        print('1 继续学习，阅读一篇文章获得1分，上限6分')
        try:
            job1()
        except Exception as e:
            print(e)
            print('there is issue with job1, continue to run other jobs')     
    else:
        print('1 已完成阅读文章任务，并获得6分！') 
        i=i+1
         
    if list[2]!="已完成" :
        print('2. 继续学习，观看一个视频获得1分，上限6分')     
        try:
            job2()
        except Exception as e:
            print(e)
            print('there is issue with job2, continue to run other jobs')        
    else:
        print('2 已完成观看短视频任务,并获得6分！')
        i=i+1 

    if list[3] != "已完成" :
        print('3 继续学习，阅读一篇文章每累计4分钟获得1分，上限8分')
        try:
            job3()
        except Exception as e:
            print(e)
            print('there is issue with job3, continue to run other jobs')
        
    else:
        print('3 已完成长时间阅读文章任务,并获得8分！') 
        i=i+1

    if list[4]!="已完成" :
        print('4 继续学习，观看视频每累计5分钟，获得1分，上限10分')
        try:
            job4()
        except Exception as e:
            print(e)
            print('there is issue with job4, continue to run other jobs')

    else:
        print('4 已完成长时间观看视频任务,并获得10分！') 
        i=i+1
        
    if i ==4:
        print("完成今天的学习任务")
        driver.quit()  
        exit()


if __name__ == "__main__":
    
    location = 'C:\\FirefoxPortable\\App\\Firefox64\\firefox.exe'
    url_home ='https://www.xuexi.cn/'
    i = 0
    for num in range (20):
        driver = webdriver.Firefox(firefox_binary=location)    
        driver.maximize_window()
        job()
        driver.quit()
        time.sleep(5)

