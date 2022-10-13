from flask import Flask, request, render_template,jsonify
import random
import time
app = Flask(__name__)

promptlen = 1

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
        global promptlen
        promptlen = int(request.form.get("wordlength"))
        return render_template("speed.html", promptlen = promptlen)
    return render_template('index.html')



word = []

#creates list of words
with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    for i in range(promptlen):
      word.append(random.choice(words))
    prompt = ' '.join(map(str,word))
    print(prompt)

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

def wpm():
    slenth = len(prompt)
    numword = slenth / 4.7
    wordspm = numword / (time_lapsed/60)
    wordspm = str(wordspm)
    print("Your WPM is: ", wordspm)


#Starts the timer and calculate the elapsed time
def start():
  input("Press Enter to start")
  start_time = time.time()
  if input() == prompt:
      end_time = time.time()
      global time_lapsed
      time_lapsed = end_time - start_time
      time_convert(time_lapsed)
      print(time_lapsed)
      wpm()
  else:
      print("you fucked up")
      start()

if __name__=='__main__':
    app.run()
    
start()