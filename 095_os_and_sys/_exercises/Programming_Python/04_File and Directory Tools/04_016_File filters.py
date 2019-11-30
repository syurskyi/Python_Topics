import sys
def filter_files(name, function):
    with open(name, 'r') as input, open(name + '.out', 'w') as output:
        for line in input:
            output.write(function(line)) # write the modified line

def filter_stream(function):
    for line in sys.stdin: # read by lines automatically
        print(function(line), end='')

# C:\...\PP4E\System\Filetools> filters.py < hillbillies.txt
# *Granny
# +Jethro
# *Elly May
# +"Uncle Jed"
# ######################################################################################################################

from filters import filter_files
filter_files('hillbillies.txt', str.upper)
print(open('hillbillies.txt.out').read())
# *GRANNY
# +JETHRO
# *ELLY MAY
# +"UNCLE JED"
# ######################################################################################################################