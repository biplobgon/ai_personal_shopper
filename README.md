# AI-Powered Personalized Shopping Assistant

## Overview
This project leverages Large Language Models (LLMs) to build an AI-powered personalized shopping assistant that understands natural language queries and recommends products tailored to individual preferences.

## Objectives
- Collect product data via web scraping.
- Build and fine-tune an LLM-based model for product recommendations.
- Develop a user-friendly interface (e.g., with Streamlit) for demoing the project.

## Folder Structure
- `/data`: Raw and processed data.
- `/notebooks`: Jupyter Notebooks for exploration.
- `/scripts`: Python scripts (including web scrapers).
- `/models`: Saved models.
- `/docs`: Documentation and blueprints.

## Business Use Case
- **Goal:** Enhance customer experience on e-commerce platforms with personalized product recommendations.
- **Impact:** Increase user engagement and conversion rates by predicting customer needs in real time.

## Data Collection
- **Sources:**  
  - Web scraping product data from e-commerce websites (e.g., Amazon, eBay) using BeautifulSoup and Scrapy.  
  - Alternatively, utilize public datasets from Kaggle containing product information and reviews.
- **Steps:**  
  1. Write a Python script to scrape product listings and details.  
  2. Clean and structure the scraped data.

## Methodology
1. **Data Preprocessing:**  
   - Clean and normalize product data.
2. **Model Development:**  
   - Fine-tune a pre-trained LLM (e.g., GPT-3 or Llama) with domain-specific data.  
   - Integrate with LangChain for managing conversation flows.
3. **MLOps Pipeline:**  
   - Track experiments using MLflow.  
   - Containerize the solution using Docker and set up CI/CD with GitHub Actions.
4. **Deployment:**  
   - Deploy the model on AWS (using SageMaker or Lambda).  
   - Build a front-end with Streamlit to interact with the assistant.

## Technologies Used
- **Languages:** Python  
- **Libraries/Frameworks:** Hugging Face Transformers, LangChain, BeautifulSoup, Scrapy, MLflow, Docker, Streamlit  
- **Cloud:** AWS (SageMaker, Lambda)  
- **Version Control:** Git & GitHub

## 📌 **Project Scope Document**

| Aspect                        | Definition                                                        |
|-------------------------------|-------------------------------------------------------------------|
| **Problem Statement**         | Users struggle with product choice overload online.               |
| **Target Users**              | Casual and frequent online shoppers.                              |
| **Core Features**             | - Personalized Recommendations (based on user history)<br>- Interactive Product Search & Filters<br>- User Profiles<br>- Visual Explanations |
| **Advanced Features (Future)**| - Conversational UI integration<br>- Real-time personalized notifications/promotions |
| **ML Techniques**             | - Collaborative Filtering (Matrix Factorization, ALS)<br>- Content-Based Filtering (TF-IDF, Cosine Similarity) |
| **Success Metrics**           | Precision@5 (≥75%), Recall, Mean Average Precision (MAP), Normalized Discounted Cumulative Gain (NDCG) |

---

## 🎈 **Usage**
Run the Streamlit demo locally:
```bash
streamlit run streamlit_app/app.py
```

## How to Run
Follow these steps to set up the project locally:
1. Ensure you have **Python 3.10+** installed.
2. Clone this repository and navigate into the project directory.
   ```bash
   git clone <repository-url>
   cd ai_personal_shopper
   ```
3. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```
4. Launch the application.
   ```bash
   streamlit run streamlit_app/app.py
   ```

