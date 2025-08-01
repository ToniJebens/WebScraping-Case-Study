# 🛒 E-Commerce Price Scraper: Digital Camera Market Analysis

A hands-on case study focused on building a scraping and analysis pipeline to compare pricing and inventory across Jessops, Camera World, and Castle Cameras.  
This project was completed as part of a data science interview task.  
[Spoiler: I got the internship]

---

## 🧠 Problem Statement

You're in the market to purchase your first camera. A friend recommends Jessops, a UK-based online camera retailer. To better understand the market and ensure you're getting the best value, you want to:

1. Explore the **range of cameras** sold by Jessops (DSLR, Mirrorless, Compact).
2. Compare Jessops' offerings with **competing retailers** to benchmark prices and availability.

---

## 🎯 Objectives

- ✅ Build a web scraper for **Jessops.com** to collect product listings, categories, and prices.
- ✅ Perform **cross-site price comparison** against other camera retailers (Castle Cameras, Camera World)
- ✅ Summarize findings with actionable insights in a presentation format.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10  
- **Libraries:** `requests`, `BeautifulSoup`, `pandas`, `matplotlib`  
- **Tools:** Jupyter Notebook, Google Slides (for final presentation)

---

## 🗂️ Project Structure

```python
WebScraping-Case-Study/
│
├── Scrapers/
│ ├── Jessops.py # Main scraper for Jessops product pages
│ └── CastleCameras.py
│ └── CameraWorld.py
│
├── Analysis/
│ └── Market_Comparison.py # Analysis of pricing differences
│
├── Data/
│ └── redacted
│
├── Presentation/
│ └── Camera Purchase Case Study AJebens.pdf # Summary of findings (also linked below)
│
└── README.md
```

---

## 📊 Summary of Findings

- **Jessops is generally more expensive**, though price differences depend on the camera segment.  
- **Retailer positioning differs**: Jessops carries more high-end models, while Camera World and Castle Cameras offer broader mid- to low-range options.  
- For **Mirrorless and DSLR**, Jessops is competitive:
  - Competitors did **not consistently beat Jessops on price**
  - Product ranges were **well-aligned** across sites
- For **Compact cameras**, **Camera World had the largest inventory**.
- 📌 **Recommendation**: Pick your desired model first, then compare listing and bundle deals across retailers.

📥 **Presentation Deck**:  
[Camera Price Comparison – Slides (Google Drive)](https://drive.google.com/file/d/1Uz_V7RUZNYn5lq0x1lrRTn2dlCopDwao/view?usp=sharing)

---

## 💡 Key Learnings

- Built a structured scraping pipeline with pagination, product-level extraction, and data consolidation.
- Applied fuzzy matching to remove duplicates and standardize product listings across formats.
- Cleaned and aligned datasets from multiple retailers for fair price and range comparisons.
- Presented actionable insights through a compact slide deck, balancing technical findings with consumer relevance.
---

