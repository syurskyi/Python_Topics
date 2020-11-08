import glob

text_files = glob.glob("file*.txt")
print(text_files)
with open('together.txt', 'w') as outfile:
    for text_file in text_files:
        with open(text_file) as infile:
            for line in infile:
                outfile.write(line + "\n")