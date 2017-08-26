""" example on using the zipfile module, first section opens an existing archive and shows a few functions
second section shows how to create an archive and add files to it"""
import zipfile,os

os.chdir('C:\\')
exampleZip=zipfile.ZipFile('example.zip')
print exampleZip.namelist()
spamInfo=exampleZip.getinfo('spam.txt')
print spamInfo.file_size
print spamInfo.compress_size
print 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
exampleZip.extractall()#extracts the archive to the current working dir
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')#extracts file to the path
exampleZip.close()

newZip=zipfile.ZipFile('new.zip','w') #create/open the file in write mode to allow adding of new files to archive. pass 'a' to open in append mode if only going to add files
newZip.write('spam.txt',compress_type=zipfile.ZIP_DEFLATED)#use compression algprithim DEFLATE because it works on all file types(research more algorithims for better use in the future)
newZip.close()

