# C:\...\PP4E\System\Streams> python teststreams.py
import teststreams

# Hello stream world
# Enter a number>12
# 12 squared is 144
# Enter a number>10
# 10 squared is 100
# Enter a number>^Z
# Bye
#
# C:\...\PP4E\System\Streams> type input.txt
# 86
# C:\...\PP4E\System\Streams> python teststreams.py < input.txt
# Hello stream world
# Enter a number>8 squared is 64
# Enter a number>6 squared is 36
# Enter a number>Bye
#
# C:\...\PP4E\System\Streams> python teststreams.py < input.txt > output.txt
# C:\...\PP4E\System\Streams> type output.txt
# Hello stream world
# Enter a number>8 squared is 64
# Enter a number>6 squared is 36
# Enter a number>Bye