import pypandoc

input_file = "temp.html"
output_file = "output.docx"
pypandoc.download_pandoc()

output = pypandoc.convert_file(input_file, "docx", outputfile=output_file)

print("Conversion complete.")
