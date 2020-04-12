import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
caps = {
      "platformName": "Android",
      "platformVersion": "5.1.1",
      "deviceName": "127.0.0.1:62025",
      "appPackage": "com.ss.android.ugc.aweme",
      "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
      "noReset": True,
      "unicodekeyboard":True,
      "resetkeyboard":True
}
#appium 操作手机
drive = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=caps)

def get_size():
    x = drive.get_window_size()['width']
    y = drive.get_window_size()['height']

    return (x,y)
try:
    if WebDriverWait(drive,10).until(lambda x:x.find_element_by_id('com.ss.android.ugc.aweme:id/akc')):
        drive.tap([(845,94)],500)
except:
    pass
# time.sleep(20)
# drive.tap([(845,94)], 500)

#点击搜索框并输入要搜索的用户
try:
    if WebDriverWait(drive,10).until(lambda x:x.find_element_by_id('com.ss.android.ugc.aweme:id/ai2')):
        drive.find_element_by_id('com.ss.android.ugc.aweme:id/ai2').click()
        drive.find_element_by_id('com.ss.android.ugc.aweme:id/ai2').send_keys('迪丽热巴')
        if WebDriverWait(drive,10).until(lambda x:x.find_element_by_id('com.ss.android.ugc.aweme:id/fzm')):
            drive.find_element_by_id('com.ss.android.ugc.aweme:id/fzm').click()
except:
    time.sleep(20)
    drive.find_element_by_id('com.ss.android.ugc.aweme:id/ai2').click()
    drive.find_element_by_id('com.ss.android.ugc.aweme:id/ai2').send_keys('迪丽热巴')
    if WebDriverWait(drive, 10).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/fzm')):
        drive.find_element_by_id('com.ss.android.ugc.aweme:id/fzm').click()

try:
    if WebDriverWait(drive,10).until(lambda x:x.find_element_by_id('com.ss.android.ugc.aweme:id/w_')):
        drive.tap([(430,195)],500)
        if WebDriverWait(drive,10).until(lambda x:x.find_element_by_id('com.ss.android.ugc.aweme:id/w_')):
            drive.tap([(90,320)],500)

except:
   pass
#点击控件获取粉丝列表界面
try:
    if WebDriverWait(drive,10).until(lambda x:x.find_element_by_id('com.ss.android.ugc.aweme:id/b5k')):
        drive.find_element_by_id('com.ss.android.ugc.aweme:id/b5k').click()

except:
    pass

#往上滑动不断获取
position = get_size()
x1 = int(position[0]*0.5)
y1 = int(position[1]*0.9)
y2 = int(position[1]*0.25)

while True:
    if '没有更多了' in drive.page_source:
        break
    else:
        drive.swipe(x1,y1,x1,y2)



