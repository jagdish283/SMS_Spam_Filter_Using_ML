# 📩 Real-Time SMS Spam Filter

A modern, real-time SMS classification system powered by **Machine Learning**, **Telegram Bot API**, and **Gradio**.

- 🔍 Classifies incoming messages as **Spam** or **Inbox**  
- 📲 Accepts messages from **Telegram**  
- 💾 Automatically stores messages in respective folders  
- 🧠 Trained with Scikit-learn (Multinomial Naive Bayes)  
- 🖥️ Includes a clean, modern **Gradio web app interface**  
- 🔁 Auto-refresh + Manual message input for classification  

---

## 📌 Features

✅ Telegram Bot Integration  
✅ Spam Detection using ML  
✅ Live Dashboard with Gradio  
✅ Auto Message Storage  
✅ Paste Text & Classify Instantly  
✅ Professional UI Styling  

---

## 🚀 Live Demo

👉 Try it now on Hugging Face Spaces:  
🔗 [Click to Launch SMS Spam Filter](https://huggingface.co/spaces/jagdishsutar20/SMS_Sam_Filter_ML)


## 📁 Folder Structure

```
SMS_Spam_Filter_ML/
│
├── app.py                       # Main Python app
├── requirements.txt             # Required dependencies
├── models/
│   ├── spam_classifier_model.pkl    # Trained ML model
│   └── vectorizer.pkl               # CountVectorizer for text input
├── messages/
│   ├── inbox/                   # Inbox messages (not spam)
│   └── spam/                    # Spam messages
├── Project Setup Guide.pdf      # Project setup guide 
└── README.md                    # This file
```

---

## ⚙️ Installation & Running the App or refer the Project Setup Guide.pdf

1. **Unzip the project folder**

2. **Open the folder in VS Code or your IDE**

3. **Open a terminal**

4. **Create the virtual environment**
   ```
   Python -m venv smsenv
   ```

5. **Activate the virtual environment**
   ```
   smsenv\Scripts\activate
   ```

6. **Install all required packages**
   ```
   pip install -r requirements.txt
   ```

7. **Run the application**
   ```
   python app.py
   ```

> The app will run locally at:  
> http://127.0.0.1:7860

---

## 🤖 Setting Up the Telegram Bot

1. Open [@BotFather](https://t.me/BotFather) in Telegram  
2. Type `/newbot` and follow the steps to create a bot  
3. After creation, copy the **bot token**  
4. Paste the token into the `app.py` file:
   ```python
   token = "PASTE_YOUR_BOT_TOKEN_HERE"
   ```
5. Save the file and restart the app  
6. Send messages to your bot on Telegram to classify them in real time

---

## 🧠 ML Model Details

- **Algorithm:** Multinomial Naive Bayes  
- **Text Vectorizer:** CountVectorizer  
- **Dataset Used:** SMS Spam Collection Dataset (UCI)  
- **Frameworks:** scikit-learn, Python  

---

## 🖼️ Web App Preview

> ✨ Sleek, professional interface with dark theme and modern layout  
> Below is the live UI screenshot from Hugging Face:

![SMS Spam Filter Screenshot](https://github.com/jagdish283/sms-spam-filter/blob/main/screenshot.png?raw=true)

---

## 🔐 Auto Classification System

- Messages sent to Telegram Bot are auto-classified  
- Inbox and spam messages are saved in:
  - `messages/inbox/`
  - `messages/spam/`

---

## 🛠️ Tech Stack

- Python 3.11+  
- Gradio  
- Telegram Bot API  
- Scikit-learn  
- Joblib  
- AsyncIO  
- Nest-AsyncIO  
- Threading  

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙋 Author

**Jagadish Sutar**  
*AI Developer | Data Analyst | Data Engineer | Python Enthusiast*  
🔗 [LinkedIn](https://www.linkedin.com/in/jagdish-sutar/)  


---

## 📬 Feedback or Suggestions?

Open an **Issue** or drop a message via the Telegram Bot. Contributions are welcome!
