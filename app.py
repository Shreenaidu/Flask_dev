from flack import Flack
app = Flack(__name__)

def home():
    return "<h1>welcome to the my world</h1>"
@app.route("/")
if __name__ == '__main__':
    app.run()