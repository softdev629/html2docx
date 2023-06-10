import json
import os
# import groupdocs_conversion_cloud
from docx import Document
from bs4 import BeautifulSoup
#create 5 differnt folders
#Split all files equally into the 5 folders with unqiue documents 
#We need 1 excel sheet with the title of the document and the valid until date (end date)
#The title should be catagory, subject, and date
#Each excel sheet should have a field assignee that is the name of the person who is assigned to that document

totalfiles = 0

mainpath = '/Users/rileyvenable/Documents/Development Projects/Peridot_Bank_Migration/000'

michael = mainpath + '/Michael'
seth = mainpath + '/Seth'
thanh = mainpath + '/Thanh'
marcelo = mainpath + '/Marcelo'
resty = mainpath + '/Resty'

# Iterate through all files in folderPath and calculate the number of files
for filename in os.listdir(mainpath):
    totalfiles += 1

# Calculate the number of files per folder and round down
filesperfolder = totalfiles / 5

#round down
filesperfolder = int(filesperfolder)

#create a object of names of folders and disperse the total files evenly between them and someone gets the remainder
folders = {
    'Michael': filesperfolder,
    'Seth': filesperfolder,
    'Thanh': filesperfolder,
    'Marcelo': filesperfolder,
    'Resty': filesperfolder
}

#calculate the remainder
remainder = totalfiles % 5

#add the remainder to the first folder
folders['Michael'] += remainder

#print the info for the user
print('Michael: ' + str(folders['Michael']))
print('Seth: ' + str(folders['Seth']))
print('Thanh: ' + str(folders['Thanh']))
print('Marcelo: ' + str(folders['Marcelo']))
print('Resty: ' + str(folders['Resty']))
print('Remainder: ' + str(remainder))
print('Total Files: ' + str(totalfiles))
print('Files Per Folder: ' + str(filesperfolder))

# Iterate through total only js files and move them to the correct folder
for filename in os.listdir(mainpath):
    if filename.endswith('.js'):
        if folders['Michael'] > 0:
            os.rename(mainpath + '/' + filename, michael + '/' + filename)
            folders['Michael'] -= 1
        elif folders['Seth'] > 0:
            os.rename(mainpath + '/' + filename, seth + '/' + filename)
            folders['Seth'] -= 1
        elif folders['Thanh'] > 0:
            os.rename(mainpath + '/' + filename, thanh + '/' + filename)
            folders['Thanh'] -= 1
        elif folders['Marcelo'] > 0:
            os.rename(mainpath + '/' + filename, marcelo + '/' + filename)
            folders['Marcelo'] -= 1
        elif folders['Resty'] > 0:
            os.rename(mainpath + '/' + filename, resty + '/' + filename)
            folders['Resty'] -= 1
        else:
            print('Something went wrong')

def convert_html2word(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Create a new Word document
    document = Document()

    # Find all the paragraphs in the HTML content and add them to the Word document
    for paragraph in soup.find_all('p'):
        document.add_paragraph(paragraph.text)

    # Save the Word document to a file
    document.save('converted_document.docx')

#create a basic function
def createWordDoc(name, path):
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
            p = '<html>'  + p + '</html>'
            #save to a html file
            with open(filepath[:-3] + '.html', 'w') as h:
                h.write(p)
                h.close()
            j.close()

            #here we need to convert the html file to a word doc
            #https://www.freeconvert.com/
            #convertio.co
            #the images need to remain in the document
        
            #delete the json file
            os.remove(jsonpath)
            #delete the js file
            os.remove(filepath)   

            # #delete the html file
            # os.remove(filepath[:-3] + '.html')

# createWordDoc('Thanh', thanh)
# createWordDoc('Seth', seth)
# createWordDoc('Marcelo', marcelo)
# createWordDoc('Resty', resty)
# createWordDoc('Thanh', thanh)
# createWordDoc('Michael', michael)

convert_html2word("<html><div><span style=\"font-family:Arial;font-size:8pt;\"></span></div><table tse-rt width=\"100%\" style=\"border-collapse:collapse;table-layout:fixed;\"><col style=\"width:100%;\" /><tr><td class=\"tse-rt-td\" style=\"border-width:1px 0px 0px;\"><div style=\"text-align:right;\"><span style=\"font-weight:bold;font-family:Arial;color:navy;\"></span><span style=\"font-weight:bold;font-family:Arial;color:navy;\">IBM Global Financing Europe</span><span style=\"font-weight:bold;font-family:Arial;\"></span></div></td></tr><tr><td class=\"tse-rt-td\" style=\"border-width:0px;\"><div><span style=\"font-family:Arial;font-size:8pt;\"></span></div></td></tr><tr><td class=\"tse-rt-td\" style=\"border-width:0px;\"><div><span style=\"font-weight:bold;font-family:Arial;font-size:14pt;color:navy;\">Dokumentation  Dok 05-004</span><span style=\"font-family:Arial;font-size:8pt;\"></span></div><table tse-rt width=\"100%\" style=\"border-collapse:collapse;table-layout:fixed;\"><col style=\"width:50.0069%;\" /><col style=\"width:49.9931%;\" /><tr><td class=\"tse-rt-td\" style=\"border-width:0px;\"><div><span style=\"font-weight:bold;font-family:Arial;color:navy;\">GF Beschluß: Endkundenfinanzierungen</span></div></td><td class=\"tse-rt-td\" style=\"border-width:0px;\"><div style=\"text-align:right;\"><span style=\"font-weight:bold;font-family:Arial;\"></span><span style=\"font-weight:bold;font-family:Arial;color:navy;\">Dok 05-004 - closed</span></div></td></tr><tr><td class=\"tse-rt-td\" style=\"border-width:0px 0px 1px;\"><div><span style=\"font-weight:bold;font-family:Arial;color:navy;\"></span><span style=\"font-weight:bold;font-family:Arial;color:navy;\">German Creditbank Instructions</span><span style=\"font-weight:bold;font-family:Arial;color:navy;\"></span></div></td><td class=\"tse-rt-td\" style=\"border-width:0px 0px 1px;\"><div style=\"text-align:right;\"><span style=\"font-weight:bold;font-family:Arial;color:navy;\"></span><span style=\"font-weight:bold;font-family:Arial;color:navy;\">12/15/2005 - until revoced</span></div></td></tr></table><div><span style=\"font-family:Arial;font-size:8pt;\"></span></div></td></tr></table><div style=\"text-align:center;\"><span style=\"font-family:Arial;font-size:8pt;\"></span></div><div><span style=\"font-size:9pt;color:navy;\"></span></div><div><span style=\"font-size:1pt;color:navy;\"></span></div><table tse-rt width=\"100%\" style=\"border-collapse:collapse;table-layout:fixed;\"><col style=\"width:1.2403in;\" /><col style=\"width:100%;\" /><tr><td class=\"tse-rt-td\" style=\"border-width:0px;\"><div><span style=\"font-size:9pt;color:navy;\">Organization:</span></div></td><td class=\"tse-rt-td\" style=\"border-width:0px;\"><div><span style=\"font-size:9pt;\"></span><span style=\"font-size:9pt;\">001-Kreditgeschäft / GF Marktfolge</span><span style=\"font-size:9pt;color:navy;\"></span></div></td></tr><tr><td class=\"tse-rt-td\" style=\"border-width:0px;\"><div><span style=\"font-size:9pt;color:navy;\">Group:</span></div></td><td class=\"tse-rt-td\" style=\"border-width:0px;\"><div><span style=\"font-size:9pt;\"></span><span style=\"font-size:9pt;\">03-Risikomanagement / Mgr. Kredit (MF)</span><span style=\"color:navy;\"></span></div></td></tr></table><div><span style=\"color:navy;\"></span></div><div><span style=\"color:navy;\"></span></div><div style=\"text-align:center;\"><span style=\"color:navy;\">If working with this document as a hardcopy, please ensure that you use the latest version!</span></div><div><span style=\"color:navy;\"></span></div><div><span style=\"color:navy;\"></span><div></div><div><span style=\"font-family:monospace;\"></span><a href=\"data/attachments/00/000/00000A86/0000.pdf\"><figure style=\"display:inline-block;text-align:center;\"><img width=\"127px\" height=\"47px\" alt=\"Scanned Document1.pdf\" src=\"data:image/gif;base64,\nR0lGODlhfwAvAOUAAP///0hImODg0MjIyICAgPjYmNj4+AAAAFBQUNjYmAgICHC4+Pj4uLj4+EgA\nAJhIAAAAmHAAcABImJjY+Pj42JiYmAAAgNiYSAAASACAAEgAcHAAAAAAcAAA+HAASNj42Pi4cABw\nuIAAALjYmABISDAwMEhISEgASHBwcJhISJhwAJi4mLhwAPgAAEhIcEiY2HBIAIAAgJjYuNj4uAD4\nAAD4+EiYuHC42JjY2Lj42MiYMPjIMPj4AAAAAAAAAAAAACwAAAAAfwAvAEAI/wABCBxIsKDBgwgT\nFiTAsKHDhw4rKJxIsaLFixgxEhAgEKJHhwoGVECBIKPJkyhTGtzYkWMLHiIA1OjQQWCGDAAEDFAg\ncEBJlUCDCl3JEYCCo0iTKkXa8+fQp1CjSp2qkMKDAxgmWF0AgIGHCQMLBEjggKtYsmYDfEgBVuyH\nB1xBSDAQNgBdABRS4IAL4EKIrV09rLAL4OyJCQUOu2VbeGzZxgkIC2QQoUHYw33/8pUb+S7VlCwx\nStTp9LPpz6E3CljNunXrnU1Py5aammNDALdv6+QJwOfs30NDo/QNHGMBBwcOcP0s1vPx5MqLF6Rs\nmWJzFtERYj/AwTKDDcm5Xv+ALqEzZMLNv2Nti5yE5MLIwwt8Prcr+OjjD7jv3Dw9+KzNNTbDBt1N\nVllXEYxgAnL1Pbffe9JNJJxFFRAX4YUmTVhRBSaYUMKHJWAoIkWp6QDBiSiiaMGKLPJE2ogwIlRb\nRbvFFuONA804QEy9xRADADfhVGNvpeEIY22uJckabL2ZYCSOGmZk4ZMjbjTAlVhmqeWWVxZJ5Zdg\nXhSgbGM2dleZppVJXUVnQZgQZSO851VbY6FXJ11naVCdmXzOJ1mbeN5ZV6D82ZXnngECOtCafhJq\np3lhgolmpEQpaelqFXhJaYRRTlTBi5ti2KlCEuU0Zai/jaqQTiORhGpxqe3/kOKsAFhQa60KsKrp\nq1SlxuWvTJ7KK2pFqUrQkMIOO9WMALQQU00D4WQqb8kqG9WMIjgLAE0DAElDTcjuau1TzE4U7rim\nlbtqsOKiG5SvwG5JbbvuqmQsRdXWC9S9E+WrL2hFDUfvvyYhYPDBCCescMIEN+zwwxPNWZiezL0X\nIGCzXXxVgdYFMMOBCFn1AkHqRbedcmKpEF7K8j2XFXzJ1deogQ08V2DJCyQ6lgswHGDDVSO7jFgA\nKh9ww1UyM1oYz9xZ9px+yHGsEGcQPl3eo4/Gh9VggTonGZxYe+2oAf05Bh0GXJ/nmdKJahDn2An5\nJZBcb3HllQwHUg23W3wVKKBBDnxdIDOfWwHmF2B353012Yaq1bfbYS8K8sSWHR744hCfNilFAQEA\nOw==\n\" /></figure></a></div><div></div><div></div><div></div><span style=\"color:navy;\"></span></div><div><span style=\"color:navy;\"></span></div><div><span style=\"color:navy;\"></span></div><div><svg height='10' width='16'><polygon points='0,2 12,2 6,9' style='fill:navy'/></svg><span style=\"font-weight:bold;color:navy;\">Documentation</span></div><div><span style=\"font-size:9pt;color:navy;\"></span><div></div><span style=\"font-size:8pt;\"></span></div><div><svg height='10' width='16'><polygon points='0,2 12,2 6,9' style='fill:navy'/></svg><span style=\"font-weight:bold;color:navy;\">History</span></div><div><span style=\"font-size:8pt;\"></span></div><table tse-rt width=\"100%\" style=\"border-collapse:collapse;table-layout:fixed;\"><col style=\"width:36.2014%;\" /><col style=\"width:20.9479%;\" /><col style=\"width:42.8542%;\" /><tr><td class=\"tse-rt-td\" style=\"border-width:1px 0px 1px 1px;background-color:#efefef;\"><div><span style=\"font-weight:bold;font-size:8pt;\">saved/changed from</span></div></td><td class=\"tse-rt-td\" style=\"background-color:#efefef;\"><div><span style=\"font-weight:bold;font-size:8pt;\">Date</span></div></td><td class=\"tse-rt-td\" style=\"background-color:#efefef;\"><div><span style=\"font-weight:bold;font-size:8pt;\">Status</span></div></td></tr><tr><td class=\"tse-rt-td\" style=\"border-width:1px 0px 1px 1px;\"><div><span style=\"font-size:8pt;\"></span><span style=\"font-size:8pt;\">Uwe Braeuning<br/>Uwe Braeuning<br/>Manfred Breitling<br/>Uwe Braeuning<br/>Uwe Braeuning<br/>Manfred Breitling</span><span style=\"font-size:8pt;\"></span></div></td><td class=\"tse-rt-td\"><div><span style=\"font-size:8pt;\"></span><span style=\"font-size:8pt;\">29.12.2005 14:09:47<br/>29.12.2005 14:09:52<br/>29.12.2005 14:12:35<br/>29.12.2005 14:13:09<br/>29.12.2005 14:13:09<br/>09.08.2016 10:04:27</span><span style=\"font-size:8pt;\"></span></div></td><td class=\"tse-rt-td\"><div><span style=\"font-size:8pt;\"></span><span style=\"font-size:8pt;\">created<br/>created<br/>routed<br/>verified<br/>published<br/>closed</span><span style=\"font-size:8pt;\"></span></div></td></tr></table><div></div><div style=\"text-align:center;\"><span style=\"font-family:Helvetica;color:navy;\">*** End of Document ***</span></div></html>")