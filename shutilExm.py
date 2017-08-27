#pyhon 2.7
#shutilExm.py - Renames filenames with American date format to European format

import shutil, os, re


#compile regex that matches files with American date format
dataPattern=re.compile(r"""^(.*?) #all text before the date
                        ((0|1)?\d)-#one or two digits for the month
                        ((0|1|2|3)?\d)- #one or two digits for the day
                        ((19|20)\d\d) #four digits for the year
                        (.*?)$          #all text after the date
                        """,re,VERBOSE)
#loop over the files in the CWD
for amerFilename in os.listdir('.'):
    mo=datePattern.search(amerFilename)
    #skip files without a date
    if mo==None:
        continue
    #get the different parts of the file name
    beforePart=mo.group(1)
    monthPart=mo.group(2)
    dayPart=mo.group(4)
    yearPart=mo.group(6)
    afterPart=mo.group(8)

    #form European-style filename
    euroFilename=beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart

    #get the absolute file path
    ansWorkingDir=os.path.abspath('.')
    amerFilename=os.path.join(absWorkingDir, amerFilename)
    euroFilename=os.path.join(absWorkingDir,euroFilename)

    #rename the files
    print('Renaming "%s" to "%s"...' %(amerFilename,euroFilename))
    #shutil.move(amerFilename,euroFilename)  #uncomment after testing
