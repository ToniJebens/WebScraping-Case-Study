# WebScraping-Case-Study

# 📸 Web Scraping Case Study: Camera Price Comparison

This project was completed as part of a data science interview task. The goal was to explore the product and pricing landscape for digital cameras using real-world data scraped from e-commerce websites.

---

## 🧠 Problem Statement

You're in the market to purchase your first camera. A friend recommends Jessops, a UK-based online camera retailer. To better understand the market and ensure you're getting the best value, you want to:

1. Explore the **range of cameras** sold by Jessops (DSLR, Mirrorless, Compact).
2. Compare Jessops' offerings with **competing retailers** to benchmark prices and availability.

---

## 🎯 Objectives

- ✅ Build a web scraper for **Jessops.com** to collect product listings, categories, and prices.
- ✅ Perform **cross-site price comparison** against other camera retailers (e.g., Currys, Wex).
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
│ ├── jessops_scraper.py # Main scraper for Jessops product pages
│ └── currys_scraper.py # Basic competitor scraper (optional)
│
├── Analysis/
│ └── compare_prices.ipynb # Analysis of pricing differences
│
├── Data/
│ └── raw_data/ # Collected HTML / JSON / CSV outputs
│
├── Presentation/
│ └── camera_comparison.pdf # Summary of findings (also linked below)
│
└── README.md
```

---

## 📊 Summary of Findings

- Jessops carries a broad range of entry- to mid-level Mirrorless and DSLR cameras.
- Prices were on average **4–8% higher** than competitors (depending on product category).
- Some exclusive bundle deals offset price differences — not always comparable 1-to-1.

📥 **Presentation Deck**:  
[Camera Price Comparison – Slides (Google Drive)](https://drive.google.com/file/d/1Uz_V7RUZNYn5lq0x1lrRTn2dlCopDwao/view?usp=sharing)

---

## 💡 Key Learnings

- Designed a targeted, multi-page scraper with pagination and data extraction logic.
- Performed price benchmarking and exploratory data analysis.
- Communicated results with business context and recommendations.

---

## 📄 License

MIT — open for reuse, learning, and feedback.
