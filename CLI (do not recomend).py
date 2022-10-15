
import time 
import random


promptlen = int(input("Enter number of words you want in your prompt \n"))

word = []

#creates list of words
with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    for i in range(promptlen):
      word.append(random.choice(words))
    prompt = ' '.join(map(str,word))
    print(prompt)


#calculates words per minute
def wpm():
    slenth = len(prompt)
    numword = slenth / 4.7
    wordspm = round((numword / (time_lapsed/60)), 2)
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
      tlr = round(time_lapsed, 2)
      print(f"It took you {str(tlr)} seconds to type the prompt")
      wpm()
  else:
      print("you fucked up")
      start()

start()


