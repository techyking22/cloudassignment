from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data storage (for demonstration purposes)
posts = [
    {"title": "Welcome", "content": "This is your first post in your nice Flask app!"}
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            posts.append({"title": title, "content": content})
        return redirect(url_for('home'))
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)
