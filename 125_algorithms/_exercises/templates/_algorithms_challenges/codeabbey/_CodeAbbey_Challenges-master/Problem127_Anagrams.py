infile = open("prob127.txt")
infile.readline()
data = infile.readlines()
infile.close()

infile2 = open("prob127_dict.txt")
dictionary = infile2.readlines()
infile2.close()

##for word in data:
##    word = word.strip()
##    temp_d = [string.strip() for string in dictionary if le.(string.strip())==le.(word)]
##    count = 0
##    for each in temp_d:
##        flag = True
##        if each != word:
##            for char in word:
##                if word.count(char)!=each.count(char
##                    flag = False
##                    break
##            if flag:
##                count+=1
##                
##    print(count,end=" ")


# ALT USING SORTED WORDS

___ word in data:
    word = word.strip()
    word_s = sorted(list(word))
    temp_d = [string.strip() ___ string in dictionary __ le.(string.strip())__le.(word)]
    count = 0
##    word_d = dict()
    ___ each in temp_d:
        flag = True
        __ each != word:
            each = sorted(list(each))
            __ each __ word_s:
                count+=1
                
    print(count,end=" ")











    
