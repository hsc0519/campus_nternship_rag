# rag_query.py
from langchain_community.vectorstores import Chroma
from langchain_openai import AzureOpenAIEmbeddings
from llm import chat_response

# 載入 Azure OpenAI Embedding
with open("api_key.txt", 'r') as f:
    api_key = f.read().strip()

embedding = AzureOpenAIEmbeddings(
    azure_endpoint="https://20250408-genai-group-1.openai.azure.com/",
    deployment="genai-text-embedding-3-large",  # ✅ 用你 Azure 部署的名稱
    api_version="2024-02-01",
    api_key=api_key
)

# 載入向量資料庫
db = Chroma(persist_directory="./chroma_db", embedding_function=embedding)

# 回答主程式，支援 return_sources
def get_answer(query, return_sources=False): #（是否返回資料來源，預設為 False）
    results = db.similarity_search(query, k=3) # 找三個相似的結果

    # 整理上下文內容
    context = "\n---\n".join([doc.page_content for doc in results])
    prompt = f"以下是資料庫找到的相關資訊：\n{context}\n\n根據上面內容回答：{query}"
    answer = chat_response(prompt)

    if return_sources:
        # 嘗試從 metadata 取得檔名或來源資訊（如果有的話）
        sources = []
        for doc in results:
            meta = doc.metadata
            if 'source' in meta:
                sources.append(meta['source'])
            else:
                sources.append("未知來源")

        return answer, sources
    else:
        return answer
    
    