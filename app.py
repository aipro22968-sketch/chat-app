from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

# ইমেজ রাখার ফোল্ডার
IMAGE_FOLDER = os.path.join('static', 'images')

@app.route("/", methods=["GET","POST"])
def index():
    print("FILES:", os.listdir(IMAGE_FOLDER))
    results = []
    ...
    if request.method == "POST":
        query = request.form.get("query", "").lower().strip()
        if query:
            # static/images এর সব ফাইল লুপ করে মিল খুঁজে বের করা
            for filename in os.listdir(IMAGE_FOLDER):
                if query in filename.lower():
                    results.append(filename)
    # index.html ফাইলকে রেন্ডার করা এবং ফলাফল পাঠানো
    return render_template("index.html", images=results)

if __name__ == "__main__":
    # লোকালি চালাতে হলে: python app.py
    app.run(host="0.0.0.0", port=5000, debug=True)
