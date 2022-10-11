x = 'hello world storm house apple microphone camel'
import time
print("hello world storm house apple microphone camel")
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
input("Press Enter to start")
start_time = time.time()

def wpm():
    slenth = len(x)
    numword = slenth / 4.7
    wordspm = numword / (time_lapsed/60)
    wordspm = str(wordspm)
    print("Your WPM is: ", wordspm)

def start():
    if input() == x:
        end_time = time.time()
        global time_lapsed
        time_lapsed = end_time - start_time
        time_convert(time_lapsed)
        print(time_lapsed)
        wpm()
    else:
        print("you fucked up")
        start()

start()