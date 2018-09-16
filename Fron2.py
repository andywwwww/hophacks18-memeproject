import praw
from flask import Flask, request, render_template
import json
reddit = praw.Reddit(client_id='2TFDHfTcIFAThg',
                     client_secret='VSI2rZgb-zjGaXYw55eHReFdZpQ',
                     user_agent='my user agent')
print(reddit.read_only)
app = Flask(__name__)
# In the future, we will improve the web-application into google chrome extension.
@app.route('/')
def index():
    #first web-page for user
    #search words for meme will be set as Cat in this stage
    return render_template('search_words.html')
@app.route('/', methods=['POST'])
def index_post():
    if request.method == 'POST':
        input1 = request.form['meme']
        mylist = []
        for submission in reddit.subreddit('meme').search(input1):
            my_list = submission.url
            mylist.append(str(my_list))
            #change this into json file
            json.dumps(mylist)
        #our goal is to input json file into html file and automatically refresh each picture we got from reddit search.
        #This will be the future improvement for our meme generator.
        return render_template('refresh.html')
if __name__ == 'main':
    app.run(debug=True)






