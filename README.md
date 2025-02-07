# AI-Powered Personalized Shopping Assistant

## Overview
This project leverages Large Language Models (LLMs) to build an AI-powered personalized shopping assistant that understands natural language queries and recommends products tailored to individual preferences.

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

## How to Run
1. Clone this repository.
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt

