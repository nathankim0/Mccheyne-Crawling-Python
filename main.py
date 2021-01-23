from selenium import webdriver
import json

url = "http://bible4u.pe.kr/zbxe/?mid=open_read&now_day="
loc = '&b_num='

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)

dayOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


file_path = "./mcc.json"
data = {}

for i in range(1, 12 + 1):

    for j in range(1, dayOfMonth[i-1] + 1):
        date = str(i) + '-' + str(j)
        data[date] = []

        for k in range(1, 4 + 1):
            # http://bible4u.pe.kr/zbxe/?mid=open_read&now_day=1-1&b_num=1
            completeUrl = url + date + loc + str(k)
            driver.get(completeUrl)

            trs = driver.find_elements_by_class_name("li_f_size")
            for tr in trs:
                tds = tr.find_elements_by_tag_name("td")

                print('id: ' + str(k))
                print('book: ' + tds[0].text)
                print('verse :' + tds[1].text)
                print('content: ' + tds[2].text)

                data[date].append({
                    "id": k,
                    "book": tds[0].text,
                    "verse": tds[1].text,
                    "content": tds[2].text
                })

with open(file_path, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)
