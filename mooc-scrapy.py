#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:28:36 2018

@author: lcy
"""
from selenium import webdriver
from bs4 import  BeautifulSoup
import os,time
import json
from getpass import getpass
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import subprocess  



  



from selenium.common.exceptions import (ElementClickInterceptedException,
                                        ElementNotInteractableException,
                                        ElementNotSelectableException,
                                        ElementNotVisibleException,
                                        ErrorInResponseException,
                                        InsecureCertificateException,
                                        InvalidCoordinatesException,
                                        InvalidElementStateException,
                                        InvalidSessionIdException,
                                        InvalidSelectorException,
                                        ImeNotAvailableException,
                                        ImeActivationFailedException,
                                        InvalidArgumentException,
                                        InvalidCookieDomainException,
                                        JavascriptException,
                                        MoveTargetOutOfBoundsException,
                                        NoSuchCookieException,
                                        NoSuchElementException,
                                        NoSuchFrameException,
                                        NoSuchWindowException,
                                        NoAlertPresentException,
                                        ScreenshotException,
                                        SessionNotCreatedException,
                                        StaleElementReferenceException,
                                        TimeoutException,
                                        UnableToSetCookieException,
                                        UnexpectedAlertPresentException,
                                        UnknownMethodException,
                                        WebDriverException)


outdir = "output"
cookies_file="cookies.ini"
user_agent = '''User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'''

urls = [
        #'https://www.icourse163.org/learn/UESTC-234010?tid=274005#/learn/content?type=detail&id=780283&cid=1003948427',
        #'https://www.icourse163.org/learn/ZJU-21001?tid=1001774003#/learn/content?type=detail&id=1002295118&cid=1002435215',
        #'https://www.icourse163.org/learn/TONGJI-284001?tid=331001#/learn/content?type=detail&id=851156&cid=949215'
        #'https://www.icourse163.org/learn/BIT-47001?tid=275015#/learn/content?type=detail&id=543258&cid=572757',
        #'https://www.icourse163.org/learn/UESTC-234010?tid=274005#/learn/content?type=detail&id=780283&cid=1003950626',
        #* 高等数学习题课（一）
        #'https://www.icourse163.org/learn/HIT-431001?tid=1002581006#/learn/content?type=detail&id=1003559012&cid=1004229031',
        #*高等数学典型例题与解法（一）
        #'https://www.icourse163.org/learn/NUDT-1001616011?tid=1002309003#/learn/content?type=detail&id=1003090040&cid=1003644145',
        #*大数据算法 王宏志
        #'https://www.icourse163.org/learn/HIT-10001?tid=253002#/learn/content?type=detail&id=520184&cid=550701',
        # 大数据技术原理与应用
        #'https://www.icourse163.org/learn/XMU-1002335004?tid=1002458005#/learn/content?type=detail&id=1003335004',
        #嵌入式系统与实验
        #'https://www.icourse163.org/learn/XMU-1001766012?tid=1002316003#/learn/content?type=detail&id=1003145431&cid=1003746451',
        #'https://www.icourse163.org/learn/NUDT-438002?tid=1002283003#/learn/content?type=detail&id=1003103175&cid=1003666909',
        'https://www.icourse163.org/course/ZJU-232005?tid=1001794018',
        #人工智能系列前沿课程
        'https://www.icourse163.org/learn/MSRA-1002435001?tid=1002591003#/learn/content?type=detail&id=1003562081&cid=1004266113'
        ]

# 大学英语（口语）CAP_中国大学MOOC(慕课)
#browser.get('https://www.icourse163.org/learn/ZJU-1001640007?tid=1001722008#/learn/content?type=detail&id=1002395065&cid=1002580183')
# 离散数学_中国大学MOOC(慕课)
#browser.get('https://www.icourse163.org/learn/UESTC-1002268006?tid=1002384010#/learn/content?type=detail&id=1003468006&cid=1004137006')


#Chrome Driver
browser = webdriver.Chrome(executable_path="./chromedriver")



#Firefox Driver
#binary = FirefoxBinary("/opt/pkg/firefox/firefox")
#profile = webdriver.FirefoxProfile()
#profile.set_preference('network.proxy.type',0)
#browser = webdriver.Firefox(firefox_binary=binary,firefox_profile=profile)




def lesson_list(chapterdir):
    #uls = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[3]/ul/li')
    lessons = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div')
    print("lessons size" , len(lessons))
    for i in range(0,len(lessons)):
        try:
            browser.find_element_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[2]').click()
        except:
            continue
        # open lesson box
        lessons = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div')
        lname = None
        try:
            lessons[i].click()
            time.sleep(3)
            lname = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div')[i].get_attribute('title')
        except IndexError:
            continue
        
        print(lname)
        lessondir = chapterdir + "/" + lname
        if not os.path.exists(lessondir):
            os.mkdir(lessondir)
        section_list(lessondir)

def section_list(chapterdir):
    sections = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[3]/ul/li')
    print("section size",len(sections))
    [x.get_attribute('title') for x in sections]
    
    for i in range(0,len(sections)):
        try:
            browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[3]/ul/li')[i].click()
        except :
            continue
        time.sleep(3)
        title = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[3]/ul/li')[i].get_attribute('title')
        if '视频' not in title:
            continue
        print('section title ',title)
        #browser.get("https://www.icourse163.org/learn/NUDT-438002?tid=1002283003#/learn/content?type=detail&id=1003103232")
        #videosrc = browser.find_element_by_tag_name('source')
        #src = videosrc.get_attribute('src')
        src = None
        try:
            html = BeautifulSoup(browser.find_element_by_tag_name('video').get_attribute('innerHTML'),'lxml')
            src = html.source['src']
        except :
            print(title,'not found video ,skip  continue!!!!!!')
            continue
        
        autoplay = browser.find_element_by_class_name('j-autoNext')
        if autoplay.is_selected():
            autoplay.click()
        #ctlbar = browser.find_element_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]')
# =============================================================================
#         ctlbar = browser.find_element_by_class_name('u-edu-h5player')
#         print(ctlbar.get_attribute('innerHTML'))  
#         print("//div[7]/div[3]/div[2]/div")
#        actions.move_to_element(browser.find_element_by_class_name('u-edu-h5player'))
        player = browser.find_element_by_class_name('u-edu-h5player')
#        ActionChains(browser).move_to_element(player).key_down(Keys.SPACE).perform()
        ActionChains(browser).click(player).perform()
#        browser.find_element_by_class_name('u-edu-h5player').send_keys(Keys.SPACE) # stop player 

        
        foutput = chapterdir +"/"+title+".mp4"
        print("save to directiry ",foutput)
        print("download video ",src)
        cmds = ['wget','--wait=3','--read-timeout=10','-t','5','--user-agent="%s"' % user_agent,
                '-c','%s' % src, '-O','%s' % foutput]
        child = subprocess.Popen(cmds,stdout=subprocess.PIPE)
        
        while "Giving up." in child.communicate():
            child = subprocess.Popen(cmds,stdout=subprocess.PIPE)
            print("download Giving up. retry......")
        print("download ok!!!!!!!!!!!")
        
        
    


    

def email_login():
    user = input("126 email:")
    print("email:",user)
    pwd = getpass()
    print("pwd","*****")
    browser.get('https://www.icourse163.org/')
    time.sleep(5)
    try:
        relogin = browser.find_element_by_id('j-reLogin')
        relogin.click()
    except NoSuchElementException:
        loginbtn = browser.find_element_by_class_name('m-index-person-loginBtn')
        loginbtn.click()
    time.sleep(5)
    urs = browser.find_element_by_id('j-ursContainer')
    iframe1 = urs.find_element_by_xpath('.//iframe')
    browser.switch_to_frame(iframe1)
    email = browser.find_element_by_name('email')
    email.send_keys(user)
    password = browser.find_element_by_name('password')
    password.send_keys(pwd)
    dologin = browser.find_element_by_id('dologin')
    dologin.click()
    time.sleep(3)
    browser.switch_to_default_content()
    cookies = browser.get_cookies()
    print("cookies---> ",cookies)
    json.dump(cookies,open(cookies_file,"w"))
    #pickle.dump( browser.get_cookies() , open("cookies.ini","wb"))

def check_login():
    browser.find_element_by_class_name('j-passportforplug')

def get_course(url):
    browser.get(url)
    time.sleep(5)
    
    try:
        browser.find_element_by_xpath('//*[@id="course-enroll-info"]/div/div[2]/div[2]/div[1]/span').click()
        time.sleep(5)
    except NoSuchElementException:
        print("not found xpath")
        pass
    
    try:
        #lastlearn = browser.find_element_by_class_name('tnt')
        browser.find_element_by_xpath('//*[@id="courseLearn-inner-box"]/div/div[1]/div/div[1]/div/a[1]').click()
        time.sleep(4)
    except NoSuchElementException:
        print("not found tnt class name")
        pass
    
   
    
    # //*[@id="g-body"]/div[3]/div/a
    schoolname = browser.find_element_by_xpath('//*[@id="g-body"]/div[3]/div/a')
    print(schoolname)
    lessondir = outdir + "/" + schoolname.get_attribute('title')  + "_" +  browser.title
    if not os.path.exists(lessondir):
        os.mkdir(lessondir)
        # chapter list box
    chapterbox = None
    try:
        chapterbox = browser.find_element_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[1]')
    except NoSuchElementException:
        icon = browser.find_element_by_class_name('u-icon-video2')
        icon.click()
        time.sleep(2)
        chapterbox = browser.find_element_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[1]')
     
    if chapterbox is None:
        return
        
    print(chapterbox.get_attribute('innerHTML'))
    chapters = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div ') 
    print("chapers size " , len(chapters))                       
    for i in range(0,len(chapters)):
        browser.find_element_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[1]').click()
        # open list box
        chapters = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div') 
        chapters[i].click()
        time.sleep(2)
        chapters = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div') 
        cname = chapters[i].get_attribute('title')
        print("open chapter ",cname)
        chapterdir = lessondir + "/" + cname
        if not os.path.exists(chapterdir):
            os.mkdir(chapterdir)
        lesson_list(chapterdir)

if __name__ == '__main__':
    if not os.path.exists(outdir):
        os.mkdir(outdir)
        
    cookies = []
    try:
        cookies = json.load(open(cookies_file,"r"))
    except:
        print("load cookies error!!!")
        email_login()
        
    print("cookies type",type(cookies))
    browser.get('https://www.icourse163.org/')
    #newlist = browser.get_cookies()
   
    browser.delete_all_cookies()
    for cookie in cookies:
        browser.add_cookie(cookie)

    browser.get('https://www.icourse163.org/')
    time.sleep(5)
    try:
        browser.find_element_by_class_name('j-passportforplug')
    except NoSuchElementException:
        browser.delete_all_cookies()
        for cookie in cookies:
            browser.add_cookie(cookie)
        email_login()

        
    for url in urls:
        print("get from",url)
        get_course(url)
       
