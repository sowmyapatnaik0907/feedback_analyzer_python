# 📊 Survey Feedback Analyzer Using Python

## 📌 Project Overview

The **Survey Feedback Analyzer** is a beginner-friendly Python project developed as part of the *Python Fundamentals – Module End Assignment 3*.

This project analyzes survey feedback using core Python programming concepts. It collects user feedback, cleans text data, identifies frequently used words, calculates average ratings, and generates useful insights from customer comments.

## 🎯 Objectives

- Store survey data using a dictionary of lists.
- Collect additional feedback from users.
- Clean textual feedback by removing punctuation and extra spaces.
- Convert feedback text to lowercase.
- Count feedback entries containing specific words.
- Calculate the average rating.
- Identify the longest feedback comment.
- Extract unique words from all feedback entries.
- Sort feedback entries by rating.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **IDE:** Visual Studio Code (VS Code)
- **Concepts:** Dictionaries, Lists, Loops, Conditional Statements, Functions, String Manipulation, Sets, `zip()`, and `sorted()`

## 📂 Project Structure

```text
Survey_Feedback_Analyzer/
│
├── survey_feedback.py
└── README.md
```

## ⚙️ Features

### 1. Preloaded Survey Data
Starts with 10 sample feedback entries containing serial numbers, names, written comments, and ratings.

### 2. Add New Feedback
Allows users to enter additional feedback, including the respondent's name, written comment, and rating from 1 to 5.

### 3. Text Cleaning
- Removes punctuation such as `.`, `,`, `!`, and `?`.
- Removes leading and trailing spaces.
- Replaces multiple spaces with a single space.
- Converts all feedback to lowercase.

### 4. Word Count Analysis
Counts the number of feedback entries containing:
- `good`
- `poor`
- `excellent`

### 5. Rating Analysis
Calculates the average rating across all feedback entries.

### 6. Longest Feedback
Identifies the feedback comment containing the greatest number of words.

### 7. Unique Word Extraction
Extracts unique words used across all feedback comments without duplicates.

### 8. Feedback Sorting
Optionally sorts feedback entries from highest rating to lowest.

## ▶️ How to Run the Project

**Step 1:** Install Python on your computer.

**Step 2:** Clone or download this repository.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the terminal and execute:

```bash
python survey_feedback.py
```

If needed on Windows, use:

```bash
py survey_feedback.py
```

**Step 5:** Follow the on-screen instructions to add feedback and view the analysis results.

## 📈 Expected Output

The program displays:
- Successfully cleaned feedback data.
- Counts for feedback entries containing selected words.
- Average survey rating.
- Longest feedback comment and its word count.
- Alphabetically sorted unique words.
- Feedback entries sorted by rating.

*Note: Results depend on the feedback entered by the user.*

## 📚 Learning Outcomes

Through this project, I practiced:
- Python data structures and data manipulation.
- Text preprocessing and string operations.
- Writing reusable functions.
- Applying loops and conditional logic.
- Extracting insights from textual data.
- Organizing and documenting a Python project.

## 🚀 Future Enhancements

- Import feedback from CSV or Excel files.
- Create visualizations of survey ratings.
- Perform sentiment analysis using NLP techniques.
- Build an interactive dashboard for survey insights.

## 👩‍💻 Author

**Sowmya Patnaik**

Aspiring Data Analyst | Python Learner

## 📄 Project Type

Educational Project — Python Fundamentals

---

⭐ If you find this project useful, feel free to explore the code and suggest improvements.
