import pyperclip, re

#finds phone numbers and email addresses in the clipboard

phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #area code
    (\s|-|\.)?                      #separator
    (\d{3})                         #first 3 digits
    (\s|-|\.)                       #separaptor
    (\d{4})                         #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
    )''',re.VERBOSE)

emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          #domain
    (\.[a-zA-Z]{2,4})       #dot-something
    )''',re.VERBOSE)


text=str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phoneNum += ' x'+groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print "copied to clipboard"
    print '\n'.join(matches)
else:
    print "no phone numbers or email adresses found."

    
    
    
#checks if the password is strong enough

capitalLetters=re.compile(r'([A-Z]+)')
lowerCaseLetters=re.compile(r'([a-z]+)')
digits=re.compile(r'([\d]+)')
while True:
    password=raw_input("please input password: ")
    if len(password)>=8:
        check= capitalLetters.search(password)
        if check!=None:
            check=lowerCaseLetters.search(password)
            if check!=None:
                check=digits.search(password)
                if check!=None:
                    print "your password is strong"
                    break
                else:
                    print "password does not contain digits"
            else:
                print "password does not contain lower case letters"
        else:
            print "password does not contain capital letters"
    else:
        print "password is too short"
