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
        # 高等数学习题课（一）
        'https://www.icourse163.org/learn/HIT-431001?tid=1002581006#/learn/content?type=detail&id=1003559012&cid=1004229031',
        #高等数学典型例题与解法（一）
        'https://www.icourse163.org/learn/NUDT-1001616011?tid=1002309003#/learn/content?type=detail&id=1003090040&cid=1003644145',
        #大数据算法 王宏志
        'https://www.icourse163.org/learn/HIT-10001?tid=253002#/learn/content?type=detail&id=520184&cid=550701',
        # 大数据技术原理与应用
        'https://www.icourse163.org/learn/XMU-1002335004?tid=1002458005#/learn/content?type=detail&id=1003335004',
        #嵌入式系统与实验
        'https://www.icourse163.org/learn/XMU-1001766012?tid=1002316003#/learn/content?type=detail&id=1003145431&cid=1003746451',
        'https://www.icourse163.org/learn/NUDT-438002?tid=1002283003#/learn/content?type=detail&id=1003103175&cid=1003666909',
        
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
        cboxs = browser.find_element_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[2]');
        cboxs.click() # open lesson box
        lessons = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div')
        lessons[i].click()
        time.sleep(2)
        lessons = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div')
        lname = lessons[i].get_attribute('title')
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
        sections = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[3]/ul/li')
        sections[i].click()
        time.sleep(3)
        sections = browser.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div/div[3]/ul/li')
        title = sections[i].get_attribute('title')
        if '视频' not in title:
            continue
        print('section title ',title)
        #browser.get("https://www.icourse163.org/learn/NUDT-438002?tid=1002283003#/learn/content?type=detail&id=1003103232")
        #videosrc = browser.find_element_by_tag_name('source')
        #src = videosrc.get_attribute('src')
        videosrc = None
        try:
            videosrc = browser.find_element_by_tag_name('video')
        except NoSuchElementException:
            print(title,'not found video ,skip  continue!!!!!!')
            continue
        if videosrc is None:
            continue
        p = BeautifulSoup(videosrc.get_attribute('innerHTML'),'lxml')
        if p is None:
            continue
        src = p.source['src']
        foutput = chapterdir +"/"+title+".mp4"
        print("save to directiry ",foutput)
        print("download video ",src)
        os.system('wget --progress=dot --wait=3 --read-timeout=10 -t 5 --user-agent="%s" -c %s -O "%s"'
                  %(user_agent,src,foutput))
        print("download ok!!!!!!!!!!!")
        
        
    


    

def email_login():
    user = input("126 email:")
    print("email:",user)
    pwd = getpass()
    print("pwd","*****")
    browser.get('https://www.icourse163.org/')
    time.sleep(5)
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
        #lastlearn = browser.find_element_by_class_name('tnt')
        lastlearn = browser.find_element_by_xpath('//*[@id="courseLearn-inner-box"]/div/div[1]/div/div[1]/div/a[1]')
        lastlearn.click()
        time.sleep(4)
    except NoSuchElementException:
        print("not found tnt class name")
        pass
    
    lessondir = outdir + "/" + browser.title
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
        chapterbox.click()  # open list box
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
       
