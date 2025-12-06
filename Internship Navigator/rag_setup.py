# rag_setup.py
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import AzureOpenAIEmbeddings
from langchain.docstore.document import Document

with open("api_key.txt", 'r') as f:
    api_key = f.read().strip()

# 建立嵌入物件
embedding = AzureOpenAIEmbeddings(
    azure_endpoint="https://20250408-genai-group-1.openai.azure.com/",
    deployment="genai-text-embedding-3-large",
    api_version="2024-02-01",
    api_key=api_key
)

all_documents = []
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50) #500切一個 #50重疊

# 處理 internships.csv
df1 = pd.read_csv("internships.csv")
texts1 = []
for _, row in df1.iterrows(): #我只要 row（那行數據），編號 0、1 我不care，所以用 _ 佔位
    content = (
        f"公司: {row['company']}\n"
        f"部門: {row['department']}\n"
        f"職稱: {row['title']}\n"
        f"描述: {row['description']}\n"
        f"條件: {row['requirement']}\n"
        f"薪水: {row['salary']}\n"
        f"聯絡人: {row['contact_person']}\n"
        f"聯絡方式: {row['contact_info']}\n"
        f"截止日: {row['expire_date']}"
    )
    texts1.append(f"【實習職缺】\n{content}")
for chunk in splitter.create_documents(texts1):
    chunk.metadata = {"source": "internships.csv"} #作為過濾用途
    all_documents.append(chunk)

# 改進：處理 繳交文件.csv，加強「表格」語意標示
df2 = pd.read_csv("繳交文件.csv")
texts2 = []
for _, row in df2.iterrows():

    content = (
        f"文件名稱：{row["繳交資料名稱"]}\n"
        f"繳交時間：{row["繳交時間"]}\n"
        f"負責單位：{row["負責填寫單位"]}\n"
        f"文件說明：{row["文件說明"]}\n"
    )
    texts2.append(f"【繳交文件】\n{content}")
for chunk in splitter.create_documents(texts2):
    chunk.metadata = {"source": "繳交文件.csv"}
    all_documents.append(chunk)

# 處理 大學部校外實習說明.csv
df3 = pd.read_csv("大學部校外實習說明.csv")
texts3 = []
for _, row in df3.iterrows():
    content = (
        f"課程編碼：{row['校外實習-課程編碼']}\n"
        f"課程名稱：{row['校外實習-課程名稱']}\n"
        f"課程類別：{row['課程類別']}\n"
        f"學分：{row['學分']}\n"
        f"時數：{row['時數']}\n"
        f"申請方式：{row['申請方式']}\n"
        f"實習前繳交文件：{row['繳交表件-實習前']}\n"
        f"實習後繳交文件：{row['繳交表件-實習前.1']}\n"
        f"學分及成績認列：{row['學分及成績認列']}\n"
        f"說明：{row['說明']}\n"
        f"其他：{row['其他']}\n"
    )
    texts3.append(f"【大學部校外實習說明】\n{content}")
for chunk in splitter.create_documents(texts3):
    chunk.metadata = {"source": "大學部校外實習說明.csv"}
    all_documents.append(chunk)

# 處理 注意事項.txt
with open("注意事項.txt", "r", encoding="utf-8") as f:
    notice_text = f.read()
texts4 = [f"【注意事項】\n{notice_text}"]
for chunk in splitter.create_documents(texts4):
    chunk.metadata = {"source": "注意事項.txt"}
    all_documents.append(chunk)

# 建立向量資料庫
vectorstore = Chroma.from_documents(all_documents, embedding=embedding, persist_directory="./chroma_db")

print("✅ 已整合四份文件並寫入 Chroma 向量資料庫，並標註來源！")

"""
# 讀取 CSV 並整理文字
df = pd.read_csv("internships.csv")
print(df.columns.tolist())  # 檢查欄位名
texts = []

for _, row in df.iterrows():
    content = f"公司: {row['company']}\n職稱: {row['title']}\n薪資: {row['salary']}\n描述: {row['description']}\n要求: {row['requirement']}\n聯絡資訊: {row['contact_info']}\n"
    texts.append(content)

# 分段
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.create_documents(texts)

# 建立向量資料庫
vectorstore = Chroma.from_documents(docs, embedding=embedding, persist_directory="./chroma_db")
vectorstore.persist()
print("✅ 向量資料庫已建立並儲存！")
"""