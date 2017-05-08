import time
import random
import base64

from selenium import webdriver


def getNowTime():

    hour   = time.strftime('%H', time.localtime(time.time()))
    minute = time.strftime('%M', time.localtime(time.time()))

    return hour, minute


def am_SeleniumHander():
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get("http://kq.neusoft.com/")
    time.sleep(1)
    user   = base64.decodestring("emh1LXhk")
    pwd    = base64.decodestring("YWluaTEzLjE0")
    time.sleep(1)
    driver.find_element_by_xpath("//div[2]/input").clear()
    driver.find_element_by_xpath("//div[2]/input").send_keys(user)
    time.sleep(1)
    driver.find_element_by_xpath("//div[3]/input").clear()
    driver.find_element_by_xpath("//div[3]/input").send_keys(pwd)
    time.sleep(1)
    driver.find_element_by_id("loginButton").click()
    time.sleep(2)
    driver.switch_to_default_content()
    time.sleep(1)
    try:
        driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[4]")
    except:
        driver.find_element_by_xpath("//a/img").click()
        print "click am ..."
        time.sleep(2)
    finally:
        driver.find_element_by_xpath("//td[4]/a/img").click()
        time.sleep(1)
        driver.quit()
        print "AM exit ..."


def pm_seleniumHander():
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get("http://kq.neusoft.com/")
    time.sleep(1)
    user   = base64.decodestring("emh1LXhk")
#   base64.encodestring(pattarm)
    pwd    = base64.decodestring("YWluaTEzLjE0")
    time.sleep(1)
    driver.find_element_by_xpath("//div[2]/input").clear()
    driver.find_element_by_xpath("//div[2]/input").send_keys(user)
    time.sleep(1)
    driver.find_element_by_xpath("//div[3]/input").clear()
    driver.find_element_by_xpath("//div[3]/input").send_keys(pwd)
    time.sleep(1)
    driver.find_element_by_id("loginButton").click()
    time.sleep(2)
    driver.switch_to_default_content()
    time.sleep(1)
    try:
        driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]")
    except:
        driver.find_element_by_xpath("//a/img").click()
        print "click pm ..."
    finally:
        driver.find_element_by_xpath("//td[4]/a/img").click()
        time.sleep(1)
        driver.quit()
        print "PM exit ..."


if __name__ == "__main__":

    global_Flag    = True
    AM_Flag        = True
    PM_Flag        = True

    wantAMHour     = "08"
    wantAM_Min     = 35
    wantAM_Min_End = (wantAM_Min + 10) if ((wantAM_Min + 10) < 60) else 52

    wantPMHour     = "18"
    wantPM_Min     = 10
    wantPM_Min_End = (wantPM_Min + 13) if ((wantPM_Min + 13) < 60) else 52

    print "Hello Baby....."

    while global_Flag:

        hour, minute = getNowTime()

        if hour == wantAMHour:
            step         = random.randint(1, 7)
            wantAMMinute = random.randrange(wantAM_Min, wantAM_Min_End, step)

            print "you want choose time hour:minute is %s:%s " % (wantAMHour, wantAMMinute)

            while AM_Flag:

                hour , minute = getNowTime()

                if (int(minute) >= wantAMMinute):
                    print "__________Good Morning_______________"
                    AM_Flag = False
                    am_SeleniumHander()
                    time.sleep(32714)
                else :
                    sleepTime = random.randrange(50, 80, step)
                    time.sleep(sleepTime)

        elif hour == wantPMHour:
            step = random.randint(1, 7)
            wantPMMinute = random.randrange(wantPM_Min, wantPM_Min_End, step)
 
            print "you want choose time hour:minute is %s:%s " % (wantPMHour, wantPMMinute)
 
            while PM_Flag:
 
                hour, minute = getNowTime()
 
                if (int(minute) >= wantPMMinute):
                    print "_________Good Afternoon_______________"
                    PM_Flag     = False
                    global_Flag = False
                    pm_seleniumHander()
                    time.sleep(18)
                    break
                    time.sleep(600)
                else :
                    sleepTime = random.randrange(50, 129, step)
                    time.sleep(sleepTime)

        else:
            print "Waite Sleep......"
            global_Flag = AM_Flag or PM_Flag
            sleepTime   = random.randrange(600, 1200, 103)
            time.sleep(sleepTime)

    print "_________Bye Bye_______________"
