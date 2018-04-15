from places_name import get_start_url
import places_name
import requests
from pyquery import PyQuery as pq
import math
import sys
import pymysql
url = get_start_url()

def gethtml(url):
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
    }
    data    = {}
    params  = {}

    result = requests.get(url,headers=headers)
    return result.text

def getPage(city)->'获取职位的总页码':
    allPositionPage = list()

    sys.stdout.write('正在获取总页码....\r\n')
    for job in url:
            for location in job[1]:
                if city in location:
                    html = gethtml(location)
                    doc = pq(html)
                    positionPage = {}
                    positionPage['total'] = doc.find(".search_yx_tj").find("em").text()
                    positionPage['num'] = 60
                    positionPage['url'] = location
                    positionPage['page'] = math.ceil(int(positionPage['total'])/positionPage['num'])
                    allPositionPage.append(positionPage)

    sys.stdout.write('页面获取成功\r\n')
    return  allPositionPage

def catchData(location)->'给定要获取的城市职位信息':
        allPosition = list()

        sys.stdout.write('正在爬取数据....\r\n')
        html = gethtml(location)
        doc = pq(html)
        page = doc.find(".search_yx_tj").find("em").text()

        table = doc(".zwmc")
        for line in table.items():
            positionArr = {'position': line.find("a").text()}
            if line.find("a").attr("href"):
                details = gethtml(line.find("a").attr("href"))
                details_doc = pq(details)
                data1 = details_doc.find(".terminal-ul")
                positionArr['salary'] = data1.find("li").eq(0).text()
                positionArr['work_location'] = data1.find("li").eq(1).text()
                positionArr['work_attribute'] = data1.find("li").eq(3).text()
                positionArr['experience_year'] = data1.find("li").eq(4).text()
                positionArr['education'] = data1.find("li").eq(5).text()
                positionArr['job_num'] = data1.find("li").eq(6).text()
                positionArr['job_type'] = data1.find("li").eq(7).text()

                positionArr['job_details'] = details_doc.find(".tab-cont-box").find("div").eq(0).text()
                positionArr['company_details'] = details_doc.find(".tab-cont-box").find("div").eq(1).text()

                company = details_doc.find(".terminal-company")
                positionArr['company_name'] = details_doc.find(".company-name-t").text()
                positionArr['company_scale'] = company.find("li").eq(0).text()
                positionArr['company_attribute'] = company.find("li").eq(1).text()
                positionArr['company_position'] = company.find("li").eq(2).text()
                positionArr['company_address'] = company.find("li").eq(4).text()
                allPosition.append(positionArr)

        print('我爬到数据了老铁...')
        return allPosition



def run():
    dbs = db()
    cursor = dbs.cursor()
    url = getPage('北京')
    for line in url:
        #if '北京' in line['url'] and '数据分析' in line['url']:
            #print(line['page'],line['url'])
            for i in range(line['page']):
                #if [job in line['url'] for job in places_name.job_name]:

                result = catchData(str(line['url'])+str('&p=')+str(i))
                sql_header = "INSERT INTO zl_job VALUES"
                for data in result:
                    print(str(data['position'])+str('职位正在保存'))
                    sql = str("(")+str("null,")+str('"')+str(data['position'])+str('",')+str('"')+str(data['salary'])+str('",')+str('"')+str(data['work_location'])+str('",')+str('"')+str(data['work_attribute'])+str('",')+str('"')+str(data['experience_year'])+str('",')+str('"')+str(data['education'])+str('",')+str('"')+str(data['job_num'])+str('",')+str('"')+str(data['job_type'])+str('",')+str('"')+str(data['job_details'])+str('",')+str('"')+str(data['company_details'])+str('",')+str('"')+str(data['company_name'])+str('",')+str('"')+str(data['company_attribute'])+str('",')+str('"')+str(data['company_scale'])+str('",')+str('"')+str(data['company_position'])+str('",')+str('"')+str(data['company_address'])+str('"')+str(")")
                    sql = str(sql_header)+str(sql)
                    try:
                        #print(sql)
                        cursor.execute(sql)
                        dbs.commit()
                        print(str(data['position']) + str('职位保存成功'))
                    except:
                        print('数据保存失败')

                #dbs.close()




def db():
    host = "localhost"
    dbName = "python"
    user = "root"
    password = ""
    db = pymysql.connect(host, user, password, dbName, charset='utf8')
    return db




run()