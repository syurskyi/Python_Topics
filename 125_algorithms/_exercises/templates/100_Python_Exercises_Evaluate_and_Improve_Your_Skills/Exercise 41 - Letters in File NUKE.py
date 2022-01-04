#FromScratch - Create a script that generates a file where all letters of English alphabet are listed one in each line
#TO BE USED AS FIRST LECTURE EXAMPLE
#SOLUTION WOULD BE LIKE: Think of the program as a machine that gets some input and produces some output.
#In this case the input would be alphabet letters and the output a file with the alphabet letters. And between we need to use every tool that we can to make that happen.

_______ s__

w__ open("letters.txt", "w") __ file:
    ___ letter __ s__.ascii_lowercase:
        file.write(letter + "\n")
