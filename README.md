# WHAT SHOULD I COOK TODAY?
This recipe food recommender system (RS) uses Sentiment, SVD, and LightFM modeling.
User type name recipe food, choose method, and slide number of K. Then, RS will recommend to users the top K recipe food with the best score.

# 🍽️ Recipe Recommend System

> **Note:** This project is an early-stage implementation of a food-recipe recommendation system.  
> I plan to refine, optimize, and expand it over time.

---

## 🧐 Project Overview

This system allows users to type in a recipe name or food item, choose a recommendation method, and select the number **K** of top results.  
It then returns the top **K** recommended recipes using one of the following approaches:

- 🧠 **Sentiment-Based Modelling**  
- 🔢 **Matrix Factorization (SVD)**  
- ⚙️ **Hybrid / Embedding Model using LightFM**

From a user’s perspective:  
> *“What should I cook today?”* — Enter your input, pick a method, set K, and discover new recipes.

---

## 📁 Project Structure

| Folder / File | Description |
|----------------|-------------|
| `demo.py` | Quick demo script showing how to run and interact with the recommender system. |
| `requirements.txt` | List of required Python dependencies. |
| `setup.sh` | Shell script to set up the virtual environment and install dependencies. |
| `Recommendations_LightFM.csv` | Pre-computed recommendations from the LightFM model. |
| `Recommendations_SVD.csv` | Pre-computed recommendations from the SVD model. |
| `Recommendations_Sentiment.csv` | Pre-computed recommendations from the sentiment-based model. |
| `data_for_print.csv` | Sample dataset used for testing and printing demonstration results. |
| (optional) `images/` | Directory containing visuals (logos, demo screenshots, etc.). |

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/meanlifevn/recipe_recommend_system.git
cd recipe_recommend_system
```
### 2. Set up your environment
```bash
bash setup.sh
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the demo
```bash
python demo.py
```
### 5. Interact

- Enter a recipe or food name (e.g., "`spaghetti`").

- Choose a recommendation method:

-- `sentiment`

-- `svd`

-- `lightfm`

- Set the number of top recommendations (K).

- View the results.

## 🎯 Recommendation Methods
### 🧠 Sentiment-Based

Uses text analysis of user reviews to determine the sentiment of each recipe, recommending ones with similar emotional tone or taste profile.

### 🔢 SVD (Singular Value Decomposition)

A matrix factorization technique used for **collaborative filtering**, finding hidden relationships between users and recipes.

### ⚙️ LightFM (Hybrid Model)

Combines **content-based** and **collaborative filtering** approaches, using embeddings to provide more personalized recommendations.

## 📌 Why This Project?

- Most recipe apps only show trending or popular dishes.

- This project aims to generate **intelligent, personalized** recommendations based on user behavior and recipe similarity.

- Having multiple algorithms enables testing and comparing the most effective approach.

## 🛠️ Future Improvements

- 🔍 Expand the dataset with more recipes and user interactions.

- 🖥️ Build a simple web UI (e.g., Streamlit or Flask).

- 🧾 Add explainability — show why a recipe was recommended.

- ⚡ Enable real-time updates for new user feedback.

- ✅ Add automated testing and continuous integration.

## 📄 License
This project is distributed under the MIT License.
You are free to use, modify, and share it — contributions are welcome!


✨ Thanks for checking out this project! I’d love your feedback and suggestions.
