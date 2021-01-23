from selenium import webdriver
import json

url = "http://bible4u.pe.kr/zbxe/?mid=open_read&now_day="

dayofmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

file_path="./mc.json"
data={}


driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)
#
# for i in range(1, 13):
#     for j in range(1, dayofmonth[i-1]+1):
#         loc = '&b_num='
#
#         date = str(i) + '-' + str(j)
#         data[date]=[]
#
#         for k in range(1, 5):
#             data[date] = []
#
#             completeUrl = url + date + loc + str(k)
#             driver.get(completeUrl)
#
#             trs = driver.find_elements_by_class_name("li_f_size")
#             for tr in trs:
#                 tds = tr.find_elements_by_tag_name("td")
#                 data[date].append({
#                     "id": str(k),
#                     "book": tds[0],
#                     "verse": tds[1],
#                     "content": tds[2]
#                 })
loc = '&b_num='

date = str(1) + '-' + str(1)
data[date]=[]

for k in range(1, 5):
    data[date] = []

    completeUrl = url + date + loc + str(k) #http://bible4u.pe.kr/zbxe/?mid=open_read&now_day=1-1&b_num=1
    driver.get(completeUrl)

    trs = driver.find_elements_by_class_name("li_f_size")
    for tr in trs:
        tds = tr.find_elements_by_tag_name("td")

        print('id: ' + str(k))
        print('book: ' + tds[0].text)
        print('verse :' + tds[1].text)
        print('content: ' + tds[2].text)

        data[date].append({
            "id": str(k),
            "book": str(tds[0].text),
            "verse": str(tds[1].text),
            "content": str(tds[2].text)
        })

with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent=4)

