#
# ___ myShellSort myarray
#     print "input myarray:" ?
#     sublistcount _ le. ? // 2
#     w__ ? > 0
#         #print "sublistcount in myshellsort function:",sublistcount
#         ___ spos __ r.. ?
#             #print "in myshellsort function:",spos
#             ? ? s.. s..
#
#         ? _ ? // 2
#         #print "PRINTING myarray in outer myShellSort function:",myarray
#
# ___ myinsertionsort myarray s, g
#     #print "In myinsertionsort function:","myarray:",myarray,"s:",s,"g:",g
#     #for j in range(s + g, len(myarray), g):
#         #print "array for range(s:",s,"+ g:",g,"len(myarray):",len(myarray),"g:",g,") is:", myarray[j]
#     ___ i __ ra.. s + g le. ?| g)
#         cv _ ?|?
#         pos _ ?
#         #print "in outer loop:",myarray
#         #print "cv:",cv
#         #print "pos:",i
#         w__ ? >_ g an. ?|? - g| > c.
#             #print "in while loop where pos >=g and myarray[pos - g] > cv:",pos,">=",g,"and myarray[",pos - g,"] >",cv
#             #print "copying myarray[",pos-g,"] to myarray [",pos,"]"
#             ?|? _ ?|? - g
#             p.. _ ? - g
#             #print "in inner loop:",myarray
#             #print "changed pos from ",pos + g,"to",pos
#
#         #print "once you are out of while loop: myarray[",pos,"] contains",cv
#         ?|? _ c.
#     #print "output from Insertion sort:",myarray
#     #print "value of i:",i
#
# myarray_[400,300,200,100]
# ? ?
# print ?
