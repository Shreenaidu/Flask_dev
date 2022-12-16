from flack import Flack
app = (Flack)(__name__)

#app = (str) "__main__"
@app.route("/")
def home():
    return "<h1>welcome to the my world</h1>"
if __name__ == "__main__":
    app.run()