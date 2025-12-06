# app.py
import gradio as gr
from rag_query import get_answer

# 模式選擇：定義不同模式提示詞（可自訂）
MODE_HINTS = {
    "查詢實習資訊": "根據實習職缺資料與大學部實習說明回答問題。",
    "詢問申請與繳交文件": "根據注意事項、繳交文件與大學部實習說明回答問題。",
    "全部": "根據所有資料回答問題，包括職缺、注意事項、繳交文件與實習說明。"
}

# 儲存對話紀錄
chat_history = []

# 回答函式（包含來源）
def answer_question(user_input, mode, history):
    system_hint = MODE_HINTS.get(mode, "") # 若沒有對應的提示，則給空字串。
    query = f"[{mode}] {user_input}\n\n{system_hint}"
    answer, sources = get_answer(query, return_sources=True)
    history.append((user_input, answer))
    sources_display = "\n".join([f"📂 來源：{src}" for src in sources]) if sources else "(未提供來源)"
    return history, sources_display

# 左欄說明文字
with open("注意事項.txt", encoding="utf-8") as f:
    notice_text = f.read()

# Gradio Blocks UI
with gr.Blocks(title="RAG 問答系統 v2") as demo:
    gr.Markdown("""
    # 📚 Internship RAG 問答系統 v2
    ### 整合校外實習職缺、申請規定、繳交表件、課程說明之問答系統。
    """)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("""## 📌 實習公告與說明文件
            
            """)
            gr.Textbox(value=notice_text, lines=20, label="公告內容", interactive=False)

        with gr.Column(scale=2):
            mode_selector = gr.Dropdown(
                choices=["全部", "查詢實習資訊", "詢問申請與繳交文件"],
                value="全部",
                label="選擇問題模式"
            )
            chatbot = gr.Chatbot(label="問答對話區")
            sources_box = gr.Textbox(label="來源檔案資訊", interactive=False)

            user_input = gr.Textbox(placeholder="請輸入你的問題，例如：2學分與5學分有何差別？", label="輸入問題", lines=2)
            send_btn = gr.Button("🔍 送出問題")
            

            send_btn.click(
                fn=answer_question,
                inputs=[user_input, mode_selector, chatbot],
                outputs=[chatbot, sources_box]
            )

            user_input.submit(
                fn=answer_question,
                inputs=[user_input, mode_selector, chatbot],
                outputs=[chatbot, sources_box]
            )

demo.launch()