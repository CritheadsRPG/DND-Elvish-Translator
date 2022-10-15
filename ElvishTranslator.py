import pandas as pd
import string

#Read in data from both columns
lang = pd.read_excel('ElvishDict.xlsx', names=['English', 'Elvish'])

#Split the languages into two lists with matching indicies
engLex = lang['English'].values.tolist()
elvLex = lang['Elvish'].values.tolist()

while True:
    inp = str(input('Enter English Word (0 To Quit): ')).lower() #get input from user

    inp = inp.translate(str.maketrans('', '', string.punctuation)) #remove punctuation from user input to not run into issuesi li
    words = inp.split(' ') #split at each word so we can translate each word and form a sentence at the end
    translated = list()

    for i in range(len(words)):
        if words[i] in engLex:
            ind = engLex.index(words[i]) #get the index of the word
            trans = elvLex[ind] #get elvish word
        else:
            trans = words[i] #if there is no elvish word, print the english word
        
        translated.append(trans) #add translated word to list
        translated.append(' ') #append a space characte between each word so it prints out proper

    if inp == '0':
        print('Thanks for using the Elvish Translator!')
        break
    
    print('English:', '\n', inp) #don't need to iterate, just print their typed info
    print('Elvish:') 

    for i in range(len(translated)): #print translated sentence 
        print(translated[i], end='') #print inline
    print() #start newline for new query
