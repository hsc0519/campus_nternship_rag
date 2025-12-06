import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://ifm.ntut.edu.tw"
start_url = f"{base_url}/p/412-1083-17371.php?Lang=zh-tw"
headers = {'User-Agent': 'Mozilla/5.0'}

# 擷取子頁資料的函式
def parse_company_page(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    company_name_tag = soup.select_one('.page-title')
    company_name = company_name_tag.text.strip() if company_name_tag else '未知公司'

    sections = soup.select('.card-section')
    labels = {
        '部門名稱': 'department',
        '職缺名稱': 'title',
        '職缺介紹': 'description',
        '職缺需求能力/條件': 'requirement',
        '待遇': 'salary',
        '聯絡人': 'contact_person',
        '聯絡方式': 'contact_info',
        '實習下架時間': 'expire_date',
    }

    records = []
    record = None
    current_department = ''  # 初始化部門

    for section in sections:
        strong_tag = section.select_one('strong')
        if not strong_tag:
            continue

        label = strong_tag.text.strip().replace('：', '')
        key = labels.get(label)
        value = section.get_text(separator='\n', strip=True)


    # 如果遇到部門名稱或職缺名稱，表示開始一個新的職缺資料
        if key == 'department':
            current_department = value  # 只更新部門，不建立新紀錄

        elif key == 'title':
            if record:
                records.append(record)  # 儲存上一筆職缺
            record = {
                'company': company_name,
                'department': current_department,
                'title': value
            }

        elif key:
            if record is None:
                record = {'company': company_name,'department': current_department}
            record[key] = value

        elif section.select_one('img'):
            img_tag = section.select_one('img')
            if record is None:
                record = {'company': company_name}
            record['poster'] = img_tag['src']

    if record:
        records.append(record)

    return records

# 開始從起始頁抓所有公司連結
response = requests.get(start_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
company_links = soup.select('a[href*="/p/404-1083"]')

# 顯示總共要處理幾個連結
print(f"🔍 共找到 {len(company_links)} 個公司頁面連結")

# 擷取每間公司的職缺資料
all_data = []
for link in company_links:
    href = link['href']
    full_url = href if href.startswith('http') else base_url + href

    try:
        company_data = parse_company_page(full_url)
        all_data.extend(company_data)
    except Exception as e:
        print(f"⚠️ 無法處理 {full_url}：{e}")

# 存入 CSV
keys = ['company', 'department', 'title', 'description', 'requirement', 'salary', 'contact_person', 'contact_info', 'expire_date', 'poster']
with open('internships.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(all_data)

print(f"✅ 完成，共儲存 {len(all_data)} 筆職缺資料到 internships.csv")
