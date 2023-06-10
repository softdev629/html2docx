import json
import os
import os
import aspose.words as aw
#create 5 differnt folders
#Split all files equally into the 5 folders with unqiue documents 
#We need 1 excel sheet with the title of the document and the valid until date (end date)
#The title should be catagory, subject, and date
#Each excel sheet should have a field assignee that is the name of the person who is assigned to that document

mainpath = '/Users/rileyvenable/Documents/Development Projects/Peridot_Bank_Migration/000 copy/test3'


#create a basic function
def createWordDoc(path):
    for filename in os.listdir(path):

        filepath = path + '/' + filename
        # Create the jsonpath
        jsonpath = filepath[:-3] + '.json' 
       
        # Open the file
        with open(filepath, 'r') as f:
            filedata = f.read()
            filedata = filedata[29:]
            filedata = filedata[:-1]
        
        with open(jsonpath, 'w') as k:
            k.write(filedata)
            k.close()
        f.close()

        with open(jsonpath, 'r') as j:
            data = json.load(j)
            p = data['p']
            p = p.replace('\\', '')
            p = '<html>' + p + '</html>'
            #save to a html file
            with open(filepath[:-3] + '.html', 'w') as h:
                h.write(p)
                htmlpath = filepath[:-3] + '.html'
                doc = aw.Document(htmlpath)
                doc.save(filepath[:-3] + '.docx')

                h.close()
            
            j.close()
        
            os.remove(filepath)


createWordDoc(mainpath)