'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = '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'

@app.route('/')
def home():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Demo</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
        <h2>About Page</h2>
        <a href="{url_for('about')}">About Recipe Generator</a>
        <h2>Team</h2>
        <a href="{url_for('index')}">Group Members</a>
        <h2>Get Cooking</h2>
        <a href="{url_for('time_temp')}">Find the appropriate baking time/temperature</a>
     '''

@app.route('/about')
def about():
    ''' display the about page '''
    print('processing / about')
    return f'''
        <h1>About Group 20</h1>
        <p>Group 20 is on a mission to provide the best recipes possible. Users of 
        Group 20's application will be able to request for any type of desert recipe.</p>
    '''

@app.route('/index')
def index():
    ''' display the about page '''
    print('processing / index')
    return f'''
       <h1>Group 20 (The Team)</h1>
       <p>Group 20 members is comprised of three computer science ladies aimed at providing 
       user scentric web applications for the whole of spring semester 2023. These 
       amazing developers include:</p>
       <ul>
       <i><a href="{url_for('ariasmith')}">Aria Smith</a></i>
       <i><a href="{url_for('abbiemurphy')}">AbbieMurphy</a></i>
       </ul>
    '''

@app.route('/ariasmith')
def ariasmith():
    ''' display the team members '''
    print('processing / ariasmith')
    return f'''
        
        <h2>Aria Smith (Full Stack and All That)</h2>
        <p>Aria Smith is currently a senior at Brandeis University who has a passion for baked 
        goods. She loves anything that has to do with pies and that is her main focus for each 
        recipe. She is responsible for the pie generator section for this recipe app as well as
        general structure and setup.</p>
    '''
@app.route('/abbiemurphy')
def abbiemurphy():
    ''' team member '''
    print('processing / abbiemurphy')
    return f'''
        <h2>Abbie Murphy</h2>
        <p>Abbie Murphy is a junior at Brandeis University who gained her footing baking with her 
        mother and long-time family friend. Her go-to baking projects were always different types
        of cookies but has been known to ocassionally burn her recipies, inspiring her to help others 
        with this problem. Abbie created the repository and added each teammate to the group.</p>
    '''
@app.route('/time_temp', methods =['GET', 'POST'])
def time_temp():
    ''' takes in a baked good and temperature or time request
        and sends to GPT for response
    '''
    if request.method == 'GET':
        return '''
        <h1>There is no burn in baking!</h1>
        <form method="POST" action="/time_temp">
          Enter the baked good you would like to know about, followed by "time" or "temperature": <input type="text" name="num"><br>
          <input type="submit" value="get response">
        </form>
        '''
    elif request.method == 'POST':
        question=int(request.form['question'])
        answer = gptAPI.getCookingTimeTemp(question)
        return factors
    else:
        return 'unknown HTTP method: ' +str(request.method)
    
@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
