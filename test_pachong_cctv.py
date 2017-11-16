from selenium import webdriver
import re
driver = webdriver.Firefox()
driver.implicitly_wait(6)
baseurl="http://www.cctv-axsq.cn/a/xinwendongtai/"
driver.get(baseurl)
Time=[]
Title=[]
SampleContent=[]
DeatilContent=[]
Urls=[]
def find():
    for link in driver.find_elements_by_xpath("//*[@class='new_title']"):
    #print (link.text)
        time=link.text[0:10]
        Time.append(time)
        title=link.text[11:len(link.text)]
        Title.append(title)
        #print("time:",time)
        #print("title:",title)
    for con in driver.find_elements_by_xpath("//*[@class='new_content']"):
        #print (link.text)
        SampleContent.append(con.text)
    for linkurl in driver.find_elements_by_xpath("//*[@class='new_more']/a"):
        Urls.append(linkurl.get_attribute('href'))
def more():
    for url in Urls:
        driver.get(url)
        DeatilContent.append(driver.find_element_by_xpath("//*[@id='myContent']").text)
def show():
    for i in range(len(Title)):
        print("title:",Title[i],"        time:",Time[i])
        print("SampleContent:\n",SampleContent[i])
        print("DeaitlContent:\n",DeatilContent[i])

if __name__ == '__main__':
    while(1):
        find()
        #if page = driver.find_elements_by_xpath("//*[@class='pages']/[@text='下一页']"):
        try:
            driver.find_element_by_link_text("下一页").click()
        except BaseException as e:
            #print('finnal page is searched')
            break
         
    more()   
    driver.quit()
    show()
    print('end')