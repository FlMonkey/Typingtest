from flask import Flask, request, render_template,jsonify, redirect, url_for
import random
import time
app = Flask(__name__)

tstartp = 0
word = []

def wpm():
    slenth = len(prompt)
    numword = slenth / 4.7
    wordspm = round((numword / (time_lapsed/60)), 2)
    wordspm = str(wordspm)
    print("Your WPM is: ", wordspm)


def start():
      #input("Press Enter to start")
    start_time = time.time()
    if input() == prompt:
        end_time = time.time()
        global time_lapsed
        time_lapsed = end_time - start_time
        tlr = round(time_lapsed, 2)
        #print(f"It took you {str(tlr)} seconds to type the prompt")
        wpm()
    else:
        return redirect('/test')


@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
        global promptlen
        promptlen = int(request.form.get("wordlength"))
        with open("words.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            
            for p in range(promptlen):
                word.append(random.choice(words))
                global prompt
                prompt = ' '.join(map(str,word))
        
        return redirect('/test')
    return render_template('index.html')
        
@app.route('/test', methods =["GET", "POST"])
def test():
    if request.method == "POST":
        pass
            
    return render_template('speed.html', promptlen = promptlen, prompt = prompt)
 

        

if __name__=='__main__':
    app.run(debug=True)

#Credit to @WhineyMonkey10 for being helpful but for also eating all my cookies
