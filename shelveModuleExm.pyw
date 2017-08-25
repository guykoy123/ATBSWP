""" mcb.pyw - Saves and loads pieces of text to the clipboard.
 Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
 py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
 py.exe mcb.pyw list - Loads all keywords to clipboard. """

import shelve, pyperclip, sys

mcbShelf=shelve.open('mcb')

if len(sys.argv)==3 and sys.argv[1].lower()=='save': 
    mcbShelf[sys.argv[2]]=pyperclip.paste()     #if has argument save then save the content of the clipboard
                                                # with key which is the second argument passed to the program
elif len(sys.argv)==2:
    if sys.argv[1].lower()=='list':             #if argument passed is list put all keys in the clipoard
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:               #if the argument passed is in saved keys, put its value in clipboard
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
