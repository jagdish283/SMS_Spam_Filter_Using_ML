import os
import joblib
import gradio as gr
import asyncio
import nest_asyncio
import logging
from datetime import datetime
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(level=logging.INFO)

# Load model and vectorizer
model = joblib.load("models/spam_classifier_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Create folders
os.makedirs("messages/inbox", exist_ok=True)
os.makedirs("messages/spam", exist_ok=True)

# Store latest message
latest_message = {"text": "📭 No Telegram messages yet."}

# Classify and store message
def classify_and_store(message):
    vec = vectorizer.transform([message])
    prediction = model.predict(vec)[0]
    folder = "spam" if prediction == "spam" else "inbox"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}_{timestamp}.txt"
    with open(f"messages/{folder}/{filename}", "w", encoding="utf-8") as f:
        f.write(message)

    latest_message["text"] = f"📨 Message: {message}\n\n✅ Classified as: **{prediction.upper()}**"
    return prediction

# Telegram message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text
        print("📩 Telegram:", text)
        classify_and_store(text)

# Run bot in background
def run_bot():
    token = "ENTER YOUR TOKEN HERE"  # Replace with your actual token
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    asyncio.run(app.run_polling())

Thread(target=run_bot, daemon=True).start()

# Read messages from folder
def read_messages(folder):
    folder_path = f"messages/{folder}"
    files = sorted(os.listdir(folder_path), reverse=True)[-10:]
    messages = []
    for file in files:
        with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
            content = f.read()
            messages.append(f"📄 {file}:\n{content}")
    return "\n\n".join(messages) if messages else "📭 No messages yet."

nest_asyncio.apply()

# Gradio UI
with gr.Blocks(title="Real-Time SMS Spam Filter", theme=gr.themes.Base()) as demo:
    gr.Markdown("## 🤖 Real-Time SMS Spam Filter (via Telegram Bot)")

    # Latest message
    latest_box = gr.Textbox(label="📨 Latest Message from Telegram", lines=4)
    refresh_btn = gr.Button("🔄 Refresh")
    refresh_btn.click(fn=lambda: latest_message["text"], outputs=latest_box)

    # Inbox / Spam View
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 📥 Inbox")
            inbox_view = gr.Textbox(lines=10, interactive=False)
            inbox_btn = gr.Button("🔄 Refresh Inbox")
            inbox_btn.click(lambda: read_messages("inbox"), outputs=inbox_view)
        with gr.Column():
            gr.Markdown("### 🚫 Spam")
            spam_view = gr.Textbox(lines=10, interactive=False)
            spam_btn = gr.Button("🔄 Refresh Spam")
            spam_btn.click(lambda: read_messages("spam"), outputs=spam_view)

    # Manual test
    gr.Markdown("### ✏️ Test a Custom SMS Message")
    custom_input = gr.Textbox(label="📋 Paste your message here", lines=3, placeholder="Enter SMS text to test")
    classify_result = gr.Textbox(label="🔍 Classification Result", interactive=False)

    with gr.Row():
        classify_button = gr.Button("🧠 Classify Message")
        clear_button = gr.Button("🗑️ Clear")

    def classify_input(message):
        if not message.strip():
            return "⚠️ Please enter a message to classify."
        result = classify_and_store(message)
        return f"✅ Result: {result.upper()}"

    classify_button.click(fn=classify_input, inputs=custom_input, outputs=classify_result)
    clear_button.click(fn=lambda: ("", ""), outputs=[custom_input, classify_result])

demo.launch(show_api=False)
