from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
# for voice
engine=pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()


bot = ChatBot("MyBOT")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(bot)

trainer.train(conversation)

# response = bot.get_response("How are you doing?")
# print(response)

main =Tk()
main.geometry("500x650")
main.title("My Chat Bot")

# img=PhotoImage(file="bot.png")
# PhotoL=Label(main,image=img)
# PhotoL.pack(pady=5)


# take query: it takes audio and convert to string
def take_query():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("our bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,"you : " +query)
    msgs.insert(END,"bot : " +str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)




frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)

sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH, pady=10)
frame.pack()

# creating text field

textF=Entry(main,font=("Verdana", 20))
textF.pack(fill=X,pady=10)

btn=Button(main,text="Ask from Bot",font=("Verdana", 20),command=ask_from_bot)
btn.pack()

# Enter function
def enter_function(event):
    btn.invoke()

# foing to bind main window with enter key
main.bind('<Return>', enter_function)

def repeat_listen():
    while True:
        take_query()

t=threading.Thread(target=repeat_listen)
t.start()
main.mainloop()
