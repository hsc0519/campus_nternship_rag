# Internship Navigator 🎓
### A RAG-powered Assistant for University Internship Rules & Opportunities

* **Project Type:** Group Course Project (Introduction to Generative AI)
* **Team Size:** 4 Members
* **My Role:** Co-Developer (Focus: Backend & RAG Architecture)
* **Status:** Proof of Concept (PoC) Completed

---

### Project Background & Motivation

This repository houses the **final group project** for the *Introduction to Generative AI* course. Our team collaborated to identify campus pain points and developed this Chatbot as a practical solution.

> **Personal Technical Growth**
>
> This project marks my **first implementation of a Retrieval-Augmented Generation (RAG) architecture**. The practical experience I gained here—specifically in handling **hybrid data retrieval**—built the essential technical skills that I later applied to my separate graduation thesis on ESG analysis.

#### The Problem Our Team Solved
We observed a critical disconnect in how internship information is presented on campus:

* **Rigid & Scattered Regulations**
  Official internship policies are stored as static **online PDFs** dispersed across various school portals, making them difficult to search or query efficiently.

* **Unorganized Job Listings**
  Internship opportunities are posted on the **department website** as unstructured text blocks, lacking essential categorization or filtering mechanisms.

* **The Verification Gap**
  Students struggle to manually cross-reference these **unstructured job postings** with **strict academic credit policies**, leading to uncertainty about eligibility and high administrative friction.

#### The Solution
**Internship Navigator** bridges this gap. We aggregated and structured the messy web data into a unified RAG knowledge base, allowing students to **query jobs and regulations simultaneously** via a single intelligent interface.

---

###  System Demo

The following demonstration showcases the system's ability to handle complex queries regarding internship regulations and job matching.

[![Watch the Demo Video](https://img.youtube.com/vi/cf4HzJiJvs8/maxresdefault.jpg)](https://youtu.be/cf4HzJiJvs8?t=4m34s)

> **Note:** The video narration and UI are in **Traditional Chinese** as the system was deployed for a local university context.

---

###  Development Iteration: From V1 to V2

A major focus of this assignment was learning through iteration. Based on user feedback from the initial prototype (V1), I implemented specific technical improvements in the final version (V2):

| Challenge | Solution Implemented in V2 | Technical Impact |
| :--- | :--- | :--- |
| **Hallucinations** | **Explicit Source Citation** | Appends metadata (e.g., `Source: 繳交文件.csv`) to responses, implementing a "Grounding" mechanism for verification. |
| **Ambiguity** | **Intent Pre-classification** | Uses a `Dropdown` to route queries (e.g., "Regulations" vs. "Jobs"), narrowing the vector retrieval scope for higher precision. |
| **No Context** | **Conversational Memory** | Upgraded to `Gradio.Chatbot` with state management, enabling the LLM to handle multi-turn follow-up questions. |
| **UX Gaps** | **Static Bulletin Board** | Added a pinned sidebar for critical deadlines, solving the issue of users missing time-sensitive static information. |

---

###  Technical Architecture

This system demonstrates a standard **RAG pipeline** integrated with enterprise-grade models.



[Image of RAG architecture diagram]


#### Core Features
1.  **Dual-Source Integration:** Simultaneously indexes unstructured PDFs (policies) and structured CSVs (job lists).
2.  **Hybrid Search Strategy:** Combines semantic search with intent-based filtering.
3.  **Interactive UI:** Built with **Gradio Blocks** featuring a split-view dashboard.

#### Tech Stack
* **LLM:** Azure OpenAI Service (**GPT-4o**) for reasoning and generation.
* **Embeddings:** Azure OpenAI (**`text-embedding-3-large`**) for high-dimensional vectorization.
* **Vector DB:** **ChromaDB** for local persistence and similarity search.
* **Framework:** **LangChain** for pipeline orchestration.
* **Frontend:** **Gradio** (Python) for the web interface.

---

### 📂 Project Resources

* **[📄 View Presentation Slides (Canva)](https://www.canva.com/design/DAGpB4Nj0rM/bN9GSQEegzqPM8F8w_fUQw/view)**
    * *Highlights: User Persona analysis and architectural diagrams.*
* **[📄 View Project Report (PDF)](./Project_Report_Chinese.pdf)** *(In Traditional Chinese)*
    * *Highlights: Detailed user research and iteration logs.*

---

### 📝 Note on Localization
While the interface and documentation are in **Traditional Chinese** to serve the target audience (local students), the source code follows standard international software engineering practices, demonstrating the implementation of Vector Search, Prompt Engineering, and Backend API handling.
