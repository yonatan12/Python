import tkinter as tk
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os

class PersonalAssistantApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.open_files = {}
        self.text = tk.Text(self, height=20, width=50)
        self.text.pack()
        self.listen_button = tk.Button(self, text="Listen", command=self.listen)
        self.listen_button.pack()

    def listen(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            self.text.insert("end", "Say something!\n")
            audio = recognizer.listen(source)

        try:
            speech = recognizer.recognize_google(audio)
            self.text.insert("end", "You said: " + speech + "\n")
            if "hello" in speech:
                self.text.insert("end", "Hello! How can I help you today?\n")
            elif "goodbye" in speech:
                self.text.insert("end", "Goodbye! Have a great day.\n")
                self.quit()
            elif "what is the time" in speech:
                now = str(datetime.datetime.now().time())
                self.text.insert("end", "The current time is " + now + "\n")
            elif "search" in speech:
                search_term = speech.split("search", 1)[1]
                webbrowser.open("https://www.google.com/search?q=" + search_term)
                self.text.insert("end", "Searching for '" + search_term + "' on Google.\n")
            elif "find" in speech:
                search_term = speech.split("find", 1)[1]
                webbrowser.open("https://www.google.com/search?q=" + search_term)
                self.text.insert("end", "Searching for '" + search_term + "' on Google.\n")
            elif "tell me about" in speech:
                search_term = speech.split("tell me about", 1)[1]
                wikipedia_summary = wikipedia.summary(search_term, sentences=2)
                self.text.insert("end", "According to Wikipedia, " + wikipedia_summary + "\n")
            elif "open file" in speech:
                file_name = speech.split("open file", 1)[1]
                try:
                    self.open_files[file_name] = open(file_name, "r")
                    self.text.insert("end", "File '" + file_name + "' opened successfully.\n")
                except:
                    self.text.insert("end", "Failed to open file '" + file_name + "'.\n")
            elif "close file" in speech:
                file_name = speech.split("close file", 1)[1]
                try:
                    self.open_files[file_name].close()
                    del self.open_files[file_name]
                    self.text.insert("end", "File '" + file_name + "' closed successfully.\n")
                except:
                    self.text.insert("end", "Failed to close file '" + file_name + "'.\n")
            elif "play video" in speech:
                video_name = speech.split("play video", 1)[1]
                webbrowser.open("https://www.youtube.com/results?search_query=" + video_name)
                self.text.insert("end", "Playing video '" + video_name + "' on YouTube.\n")
            else:
                self.text.insert("end", "Sorry, I didn't understand what you said. Can you please repeat?\n")
        except sr.UnknownValueError:
            self.text.insert("end", "I'm sorry, I couldn't understand what you said.\n")
        except sr.RequestError as e:
            self.text.insert("end", "I'm sorry, my speech recognition service is down.\n")

if __name__ == "__main__":
    app = PersonalAssistantApp()
    app.mainloop()

