import praw
from flask import Flask, request, render_template
import json
reddit = praw.Reddit(client_id='2TFDHfTcIFAThg',
                     client_secret='VSI2rZgb-zjGaXYw55eHReFdZpQ',
                     user_agent='my user agent')
print(reddit.read_only)
# application to jason file
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('search_words.html')
@app.route('/', methods=['POST'])
def index_post():
    if request.method == 'POST':
        input1 = request.form['SearchPathFirstPersonText']
        mylist = []
        #for submission in reddit.multireddit('meme',input1).hot(limit=10):
        for submission in reddit.subreddit('meme').search(input1):
            my_list = submission.url
            mylist.append(str(my_list))
            #json file
            json.dumps(mylist)
        return (json.dumps(mylist))

        #return "this is the score %s" % mylist
if __name__ == 'main':
    app.run(debug=True)

# Output: 10 submission

# reddit.subreddit("redditdev").hot(limit=5)





