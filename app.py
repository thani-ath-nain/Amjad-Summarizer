from flask import Flask, render_template, request
from Summarizer import AmjadSummarizer
import json, sys
app = Flask(__name__)


@app.route('/summ', methods = ['GET', 'POST'])
def summ():
    if request.method == 'POST':
        print('Incoming...', file=sys.stdout)
        print(request.get_json(), file=sys.stdout)
        summarizer = AmjadSummarizer(str(request.get_json()))
        print(len(str(request.get_json())), file=sys.stdout)
        summ = summarizer.summarize()
        print(len(summarizer.summarize()), file=sys.stdout)
        return json.dumps(summ)
    elif request.method == 'GET':
        pass


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
