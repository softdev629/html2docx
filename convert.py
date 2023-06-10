import os
import aspose.words as aw

directory = '000'

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".html"):
          doc = aw.Document(os.path.join(root, filename))
          doc.save(os.path.join(root, filename.replace(".html", ".docx")))
