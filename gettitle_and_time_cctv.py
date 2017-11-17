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
def find():#查找文章title以及时间，记录more选项的url链接
    for link in driver.find_elements_by_xpath("//*[@class='new_title']")
        time=link.text[0:10]
        Time.append(time)
        title=link.text[11:len(link.text)]
        Title.append(title)
    for con in driver.find_elements_by_xpath("//*[@class='new_content']"):
        SampleContent.append(con.text)
    for linkurl in driver.find_elements_by_xpath("//*[@class='new_more']/a"):
        Urls.append(linkurl.get_attribute('href'))
def more():#爬之前记录的more链接打开网页的详细文章内容
    for url in Urls:
        driver.get(url)
        DeatilContent.append(driver.find_element_by_xpath("//*[@id='myContent']").text)
def show():#显示简单/详细内容合时间
    for i in range(len(Title)):
        print("title:",Title[i],"        time:",Time[i])
        print("SampleContent:\n",SampleContent[i])
        print("DeaitlContent:\n",DeatilContent[i])

if __name__ == '__main__':
    while(1):
        find()
        try:
            driver.find_element_by_link_text("下一页").click()
        except BaseException as e:
            break  #final page
    more()
    driver.quit()
    show()
    print('end')
