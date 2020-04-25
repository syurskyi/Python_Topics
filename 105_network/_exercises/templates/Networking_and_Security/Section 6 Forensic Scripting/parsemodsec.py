# this requires Python 3 to function properly
______ __, ___, __, a_p_

#   This is a class designed to store the results from the parsed file until we're
#   ready to print them out
c_ modsecRec:
    #  this is the initializer
    ___  - (self
    	#  this is the list where all of the individual items are stored
        self.storageList _   # list

    #  append items to the list
    ___ ap.. newItem
        self.storageList.ap..(newItem)

    #  extract information from the message line and append it
    ___ extractMessage msgLine
        self.storageList.ap..(msgLine)

	#  print the parsed data out to a file from the list
    ___ printListToFile outputFilename
        w__ o..(outputFileName, 'a') __ outHandle:
        	#  create a blank string
            completeLine _ ''
            ___ singleEntry __ self.storageList:
                #  strip newlines out but append a comma for CSV format
                completeLine _ completeLine + singleEntry.rs.. + ","
            #  now we can write the line out, but strip the trailing comma
            outHandle.w..(completeLine.rs..(","))

    #  print out the entries to screen since we don't have an output file
    ___ printList(self
        ___ singleEntry __ self.storageList:
            print(singleEntry.rs.., ",")

	#  start over on the list since we've dumped one out
    ___ clear(self
        self.storageList _   # list


#  parse the command line arguments
argParser _ a_p_.A_P..
argParser.a_a..('-i', type_st., help_'the input file with the ModSecurity audit log', required_T..)
argParser.a_a..('-o', type_st., help_'the output file this should generate')
# argParser.add_argument('-f', type=str, help='the format of the output')

p__sedArgs _ vars(argParser.parse_args)

inputFileName _ p__sedArgs['i']
outputFileName _ p__sedArgs['o']

__ not __.pa__.exists(inputFileName
    print("You must specify an input file that exists")
    e..

__ outputFileName an. __.pa__.exists(outputFileName
    __.remove(outputFileName)

eachRecor. _ modsecRec

w__ o..(inputFileName, _) __ fileHandle:
    ___ dataLine __ fileHandle:
        __ '--' __ dataLine:
            __ '-A--' __ dataLine:
                dateInfo _ fileHandle.readline
                logDate _ dateInfo[dateInfo.find("[")+1:dateInfo.find(":")]
                logTime _ dateInfo[dateInfo.find(":")+1:dateInfo.find(" ")]
                eachRecor..ap..(logDate)
                eachRecor..ap..(logTime)
            __ '-B--' __ dataLine:
                httpReq _ fileHandle.readline
                eachRecor..ap..(httpReq)
            __ '-H--' __ dataLine:
                # loop until we get to the end
                ___ messageLine __ fileHandle:
                    __ 'Message' __ messageLine:
                        eachRecor..extractMessage(messageLine)
                    ____
                        b..
            __ '-Z--' __ dataLine:
                # do something with all the data we have acquired
                __ outputFileName:
                	eachRecor..printListToFile(outputFileName)
                ____
                	eachRecor..printList
                eachRecor..clear


fileHandle.c..
