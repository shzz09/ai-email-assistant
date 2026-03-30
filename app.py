from flask import Flask, render_template, request

app = Flask(__name__)

def process_email(email):
    text = email.lower()

    # 🎯 Tone detection
    if any(word in text for word in ["hey", "hi", "bro"]):
        tone = "Informal"
    else:
        tone = "Formal"

    # 📌 Subject generation
    if "meeting" in text:
        subject = "Meeting Update"
    elif "leave" in text:
        subject = "Leave Request"
    elif "project" in text:
        subject = "Project Discussion"
    elif "complaint" in text or "damaged" in text:
        subject = "Complaint Regarding Product"
    else:
        subject = "General Email"

    # 📝 Summary
    words = email.split()
    summary = " ".join(words[:10]) + "..."

    # ✍️ Rewrite
    if tone == "Formal":
        rewritten = "I would like to inform you that " + email
    else:
        rewritten = "Just letting you know that " + email

    return f"""
Subject: {subject}
Tone: {tone}
Summary: {summary}
Rewritten Email: {rewritten}
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    result = process_email(email)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)