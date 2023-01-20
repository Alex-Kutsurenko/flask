from flask import Flask, render_template, url_for

# https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2&ab_channel=CoreySchafer

# bootstrap starter template
# https://getbootstrap.com/docs/3.3/getting-started/


app = Flask(__name__)

posts=[
    {
        "author": "corey schafer",
        "title": "blog post 1",
        "content": "first post content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "blog post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018",
    }

]





@app.route("/")
@app.route("/home")
def home():

    return render_template("home.html", posts=posts)

@app.route("/about")
def about():

    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
    pass