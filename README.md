<img src="https://capsule-render.vercel.app/api?type=waving&color=00D9FF&height=180&section=header&text=Ishaan%20Sandhwar&fontSize=48&fontColor=0D1117&animation=fadeIn&fontAlignY=38&desc=AI%2FML%20Engineering%20%7C%20Retrieval%20Systems%20%7C%20Applied%20Deep%20Learning&descAlignY=58&descSize=16" width="100%" />

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=00D9FF&center=true&vCenter=true&width=520&lines=Fine-tuned+Retrievers+%7C+Agentic+Pipelines;PyTorch+%7C+Sentence+Transformers+%7C+FastAPI;C%2B%2B+Data+Structures+Written+From+Scratch" alt="Typing SVG" />

<br>

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ishaansandhwar@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ishaan-sandhwar)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ishaan-sandhwar)
[![Portfolio](https://img.shields.io/badge/Portfolio-00D9FF?style=for-the-badge&logo=googlechrome&logoColor=0D1117)](https://ishaansandhwar.netlify.app/)

![Focus](https://img.shields.io/badge/%F0%9F%8E%AF_Focus-AI%2FML_Engineering-00D9FF?style=flat-square&labelColor=0D1117)
![Status](https://img.shields.io/badge/%F0%9F%9F%A2_Status-Open_to_Internships-success?style=flat-square&labelColor=0D1117)
![Location](https://img.shields.io/badge/%F0%9F%93%8D-Punjab%2C_India-00D9FF?style=flat-square&labelColor=0D1117)

</div>

---

### 👋 About Me

I'm a Computer Science undergraduate at **Lovely Professional University**, specializing in **AI & Machine Learning**. I build ML systems end to end — data, model, evaluation, and the interface someone actually uses.

Most of my work sits around **retrieval and LLM pipelines**, with a stubborn habit of measuring things properly: held-out splits, real baselines, and ablations that tell me whether a component earned its place. I've shipped a reranker in the *disabled* state because the benchmark said it didn't transfer — I'd rather report that than quietly ship a number that doesn't hold up. ⚡

---

### 🛠️ Tech Stack

**Languages**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=openjdk&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)

**AI / ML**
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Sentence_Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

**Backend / Frontend**
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

**Tools & Platforms**
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Oracle Cloud](https://img.shields.io/badge/Oracle_Cloud-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)

---

### 🚀 Featured Projects

**🎓 Agentic AI for Academic Benefit Nomination — *Sep 2026***
*EDU Revolution, Lovely Professional University*

- Built a five-stage system that reads student achievement documents, checks eligibility against published rules, maps achievements to university courses, and drafts nominations for human approval.
- Fine-tuned a bi-encoder on hard negatives mined from the retriever's own top-20 errors — **+0.454 MRR** over TF-IDF and **+0.133 P@1** over the zero-shot encoder on held-out queries.
- Document-type classifier (MiniLM embeddings + keyword hybrid) reached **macro F1 0.916** against a 0.394 phrase-table baseline on a grouped unseen-template split.
- Benchmarked a cross-encoder reranker, found it memorised training queries and transferred nothing (held-out separation −0.037), and **shipped it disabled** with the negative result documented.
- Extraction cascade (PDF text layer → local OCR → vision LLM), inspectable rule engine, server-side RBAC, **1,071 tests**.

**Stack:** `Python` `PyTorch` `Sentence Transformers` `FastAPI` `scikit-learn` `React` `TypeScript`

🔒 *Private repository — graded academic deliverable. Walkthrough available on request.*

<br>

**🛡️ UPI Risk Desk — UPI Fraud Ring Detection & Merchant Risk Analytics — *Sep 2026***
*TransOrg AgentIQ Datathon, Track 1 — Team of 5 · Best Pipeline Award*

- Team project: a risk platform that turns **20,000 payments from four broken source systems** into one auditable model and a live analyst dashboard. **My part: data engineering and the analytics model.**
- Cleaned and linked the four sources into a **star schema + SQLite model**, with every defect logged in a **70-check data-quality ledger** — 6 date formats, 6 ID spellings, 16 KYC status variants, 41 city spellings, amounts like `Rs. 6362.9` and `27.3k`. This is the cleaning pipeline behind the team's Best Pipeline Award.
- Removed **400 duplicate payments** that would have inflated volume by **₹51.9 L**, and flagged **6,288 customer IDs** reused by different people instead of silently merging them.
- Found that complaint-side IDs disagree with the payment they dispute, so disputes are attributed through `txn_id` — otherwise merchant ratios blame the wrong merchants.

**Stack:** `Python` `pandas` `SQLite`

🔗 [GitHub](https://github.com/ishaan-sandhwar/upi-risk-desk) *(fork of the team leader's repo)* · [Live Demo](https://adityashukla2615.github.io/upi-risk-desk/outputs/upi_risk_desk.html?v=2)

<br>

**🌆 LifeLine — Smart City Disaster Response & Evacuation Simulator — *Jul 2026***
*Data Structures & Algorithms — Team of 5*

- Built a disaster response simulator over a fictional city of **40 locations and 83 roads**, served as a single static binary from a zero-dependency C++17 backend.
- Implemented min-heap, max-heap, djb2 hash map, trie and Union-Find **from scratch** instead of using the STL.
- Shipped 10+ graph algorithms — Dijkstra, A\*, Bellman-Ford, Floyd-Warshall, Edmonds-Karp max-flow/min-cut, Tarjan bridges, Prim/Kruskal MST, 0/1 knapsack DP.
- Verified correctness against networkx over **1,600+ node pairs** across 96 checks in 5 test suites; A\* settles 8 nodes where Dijkstra settles 24 on the same 4.78 km path.

**Stack:** `C++17` `React` `Vite` `Leaflet` `REST`

🔗 [GitHub](https://github.com/ishaan-sandhwar/lifeline) · [Live Demo](https://lifeline-31iq.onrender.com)

<br>

**💳 PSO Feature Selection for Credit Card Fraud Detection — *Jul 2026***
*Nature-Inspired Optimisation — Team of 2*

- Implemented **binary Particle Swarm Optimisation from scratch** — sigmoid transfer function, repair mask, early stopping — for feature selection on a heavily imbalanced dataset (492 fraud cases, 0.98% positive rate).
- Converged at iteration 18 of 50 with 30 particles, cutting **30 features down to 7**.
- PSO + Random Forest reached **ROC-AUC 0.977 / PR-AUC 0.886 / F1 0.888**, against a full-feature logistic regression baseline at ROC-AUC 0.974 / PR-AUC 0.881 — ranking metrics improve while precision trades off.
- Built a four-tab Streamlit dashboard with Parquet caching for **5–10× faster** repeat runs, plus 7 unit tests on the PSO core.

**Stack:** `Python` `scikit-learn` `imbalanced-learn` `Streamlit` `Pandas`

🔗 [GitHub](https://github.com/ishaan-sandhwar/pso-fraud-feature-selection)

<br>

**📦 Product Intelligence Engine — *Aug 2026***
*Team of 4*

- Built a pipeline that turns a part number and a **35-character** distributor description into a validated, delivery-ready product record across a **252-column** template — from a source catalogue of 1,000 rows × 6 columns, half of them placeholder markers.
- Designed deterministic-first extraction so most fields never cost a token: trade-shorthand decoding (`P150` → grit 150, `27k` → 2700 K) runs before any model call, clearing **all 1,000 rows in 7 seconds**.
- Keyword classifier resolves **~71%** of the catalogue on its own against a 26-class canonical schema; only the remainder escalates to the LLM classifier.
- Every value carries source, evidence snippet, method, confidence and rejected alternatives, checked by an adversarial LLM judge. Quality is stored **before and after** on the same yardstick, so uplift is measured rather than asserted.

**Stack:** `Python` `LLMs` `RAG` `SQLite` `Knowledge Graphs`

🔗 [GitHub](https://github.com/ishaan-sandhwar/product-intelligence-engine)

---

### 💼 Experience

**AI Mentorship Intern** — Launched Global × Deevelo X · *May 2025 – Jun 2025*
Completed a structured AI/ML training programme followed by an assigned capstone project.

---

### 🏆 Achievements

|  | Title | Where | When |
| --- | --- | --- | --- |
| 🏆 | **Best Pipeline Award** — TransOrg AgentIQ Datathon, Track 1 (team entry) | TransOrg | 2026 |
| 🥉 | **Top 30 Finalist** — CodeXtreme 4.0 Java Coding Contest | Lovely Professional University × iamneo | 2026 |
| 🎖️ | **Participant** — Algo Arena 2.0, two-day coding competition | WeInnova8, hosted on TheEduCode | 2026 |

---

### 📜 Certifications

| Certification | Issuer | Date |
| --- | --- | --- |
| Oracle Cloud Infrastructure 2025 Certified AI Foundations Associate | Oracle University | Nov 2025 |
| Oracle Data Platform 2025 Certified Foundations Associate | Oracle University | May 2026 |
| DSA Placement Bootcamp — *Grade O* | LPU Centre for Professional Enhancement | Jul 2026 |
| Database Management System (Part I) | Infosys Springboard | Aug 2026 |
| Programming Using C++ | Infosys Springboard | Aug 2025 |

---

### 🎓 Education

| Degree | Institution | Duration |
| --- | --- | --- |
| **B.Tech, Computer Science & Engineering**<br>Specialization: Artificial Intelligence & Machine Learning | Lovely Professional University | 2024 – 2028 |
| 12th Grade (Science) | Narayana E-Techno School, Mumbai | 2024 |

**Focus areas:** Information Retrieval & Dense Embeddings · Agentic LLM Systems · Classical ML & Optimisation · Data Structures & Algorithms

**Currently learning:** GATE Data Science & AI · Advanced DSA in C++ · Retrieval fine-tuning

---

### 📊 GitHub Stats

<div align="center">

<img src="https://streak-stats.demolab.com/?user=ishaan-sandhwar&hide_border=true&theme=tokyonight&fire=00D9FF&currStreakLabel=00D9FF" alt="GitHub Streak" />

<br><br>

![Followers](https://img.shields.io/github/followers/ishaan-sandhwar?style=for-the-badge&color=00D9FF&labelColor=0D1117&logo=github&logoColor=white)
![Public Repos](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2Fishaan-sandhwar&label=Public%20Repos&query=%24.public_repos&color=00D9FF&labelColor=0D1117&style=for-the-badge&logo=github&logoColor=white)
![Stars](https://img.shields.io/github/stars/ishaan-sandhwar?style=for-the-badge&color=00D9FF&labelColor=0D1117&logo=github&logoColor=white)

</div>

---

<div align="center">

Outside of code I run a Discord community and play more games than I should admit.

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=00D9FF&height=100&section=footer" width="100%" />
