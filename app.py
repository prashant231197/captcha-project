from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("CaptchaWeb.html")
@app.route("/WebCaptcha")
def service():
  return render_template("captchapk.html")
  

if __name__ == "__main__":
  app.run(debug=True)