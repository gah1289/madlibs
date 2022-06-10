from flask import Flask,request,render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app=Flask(__name__)
app.config['SECRET_KEY'] = "hopperdude123"
debug = DebugToolbarExtension(app)

@app.route('/madlibs')
def get_madlibs_home():
   return render_template("home.html")

@app.route('/story')
def get_story():
    answers={
        'place':request.args['place'],
        'noun':request.args['noun'],
        'verb':request.args['verb'],
        'adjective':request.args['adjective'],
        'plural_noun':request.args['plural_noun']
    }
    title= f"{answers['noun']} in {answers['place']}"
    
    text=story.generate(answers)
    return render_template('story.html',text=text, title=title)