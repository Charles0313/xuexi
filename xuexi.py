from selenium import webdriver
import time,json,random,os
#from selenium.webdriver.firefox.options import Options

def job1():

    windows = driver.window_handles
    driver.switch_to.window(windows[0]) # 切换到学习强国主页主页
    time.sleep(10)
    #articleID=getArticleID()
    #print(articleID) 
    #selectedContents = random.sample(driver.find_elements_by_class_name('text'),k=1)  # 
    #selectedContents = random.sample(driver.find_elements_by_tag_name('span'),k=1)
    selectedArticles = random.sample(driver.find_elements_by_xpath("//span[@class='text']"),k=1)
    print(selectedArticles[0].text)
    selectedArticles[0].click()
    startXuexi1()
    time.sleep(110)
   
def job2():
    
    windows = driver.window_handles
    driver.switch_to.window(windows[0])        
    driver.find_element_by_xpath('//a[text()="学习电视台"]').click()   #第一频道
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    selectedContents = random.sample(driver.find_elements_by_class_name('textWrapper')[4:],k=1)
    for item in selectedContents:
        print(item.text)
        item.click()
        startXuexi2()
        time.sleep(200)

    
def getArticleID():
    id_list=['C70ngaew6trg00','Ckhjp4r149s000','C3svnupj0auw00','Cex2abil2z7s00','Ckhjp4r149s000','C4ats065rhr800','C3svnupj0auw00','Cg6gdmyi3p3400']
    selectedID = random.sample(id_list,k=1)
    for id in selectedID:
        return id 

def getVideoID():
    id_list=['重要活动视频专辑','学习专题报告','学习新世界','十九大报告视频','新闻联播']
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
    for a in range(4):
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
        #driver.find_element_by_class_name('login-icon').click()
        time.sleep(35)
        driver.refresh()
        time.sleep(2)   
        cookie = driver.get_cookies()
        f2 = open('cookie.txt','w')
        f2.write(json.dumps(cookie))
        f2.close()
       


    time.sleep(5)
    try:
        job1()
    except Exception as e:
        print(e)
    
    try:
        job2()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    
    location = 'C:\\FirefoxPortable\\App\\Firefox64\\firefox.exe'
    url_home ='https://www.xuexi.cn/'
    i = 0
    for num in range (10):
        driver = webdriver.Firefox(firefox_binary=location)    
        driver.maximize_window()
        job()
        driver.quit()
    #time.sleep(5)

    
