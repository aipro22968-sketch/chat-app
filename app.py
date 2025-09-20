from flask import Flask, render_template_string, request
import os

app = Flask(__name__)
IMAGE_FOLDER = os.path.join('static', 'images')

html = """<!DOCTYPE html>
<html>
<head>
  <title>Simple Image Search</title>
</head>
<body>
  <h1>Search Images</h1>
  <form method="post">
    <input type="text" name="query" placeholder="Type e.g. cat">
    <button type="submit">Search</button>
  </form>
  {% if images %}
    <h2>Results</h2>
    {% for img in images %}
      <img src="{{ url_for('static', filename='images/' + img) }}" width="200">
    {% endfor %}
  {% endif %}
</body>
</html>"""

@app.route("/", methods=["GET","POST"])
def index():
    results = []
    if request.method == "POST":
        q = request.form.get("query","").lower()
        for f in os.listdir(IMAGE_FOLDER):
            if q in f.lower():
                results.append(f)
    return render_template_string(html, images=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
