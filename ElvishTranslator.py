#Specify only the needed components from each library as importing all of it will bloat the executable size when using
#pyinstaller later
from pandas import read_excel
from tkinter import Tk
from tkinter import Text
from tkinter import Button
from tkinter import Entry
from tkinter import END
from tkinter import StringVar
from tkinter import Label

#Read in data from both columns
lang = read_excel('ElvishDict.xlsx', names=['English', 'Elvish'])

#Split the languages into two lists with matching indicies
engLex = lang['English'].values.tolist()
elvLex = lang['Elvish'].values.tolist()

#Create some gui
window = Tk() #create a window
window.title('Elvish Translator')

#Create a textbox to display the translated information
textbox = Text(window, width=100, height=20)

#Creates a case where an key event will run process, used later to create a natural enter key progression
def enterpressed(event):
    process()
    return

#translate input phrase and print it to a text box
def process():
    request = entry.get()
    original = request #keep an original copy of request for potential later use
    request = str(request).lower() #create an all lowercase version of the request to not confuse the dictionary
    words = request.split(' ') #create a list of words and punctuation characters
    translated = list() #create a 2d list which tells which language the word comes from

    for i in words:
        if i in engLex: (translated.append(elvLex[engLex.index(i)])) #word is english, translate to elvish
        elif i in elvLex: (translated.append(engLex[elvLex.index(i)])) #word is elvish, translate to english
        else: (translated.append(i)) #if the word is not found in either dictionary then do not translate it

    #Clear the textbox object so that we don't append a new request to an old one
    textbox.delete('1.0', 'end')

    #Add spacing for phrases, and ignore spacing if it's a singular word
    if len(words) > 1: (textbox.insert(END, ' '.join(translated)))
    else: (textbox.insert(END, translated))

    return translated

#Create an input box for text
entryText = StringVar()
textLabel = Label(window, text='Enter Phrase:')
entry = Entry(window, textvariable=entryText, width=100)
entry.bind('<Return>', process)

#Create a button which will run the translation functions
transButton = Button(window, text='Translate!', width=10, height=2, command=process)

#create a case where pressing enter will run the process function
window.bind('<Return>', enterpressed) 

#Set up a grid with out elements
textLabel.grid(column=0, row=0)
entry.grid(column=1, row=0)
transButton.grid(column=2, row=0)
textbox.grid(columnspan=3)

window.mainloop() #run tkinter event loop
