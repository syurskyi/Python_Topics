# C:\...\PP4E\System\Streams> python teststreams.py < input.txt | more
# Hello stream world
# Enter a number>8 squared is 64
# Enter a number>6 squared is 36
# Enter a number>Bye
#
# C:\...\PP4E\System\Streams> type writer.py
print("Help! Help! I'm being repressed!")
print(42)
# C:\...\PP4E\System\Streams> type reader.py
# ######################################################################################################################

print('Got this: "%s"' % input())
import sys
data = sys.stdin.readline()[:-1]
print('The meaning of life is', data, int(data) * 2)

# C:\...\PP4E\System\Streams> python adder.py < data.txt sum file
# 1164
# C:\...\PP4E\System\Streams> type data.txt | python adder.py sum type output
# 1164
# C:\...\PP4E\System\Streams> type writer2.py
for data in (123, 0, 999, 42):
    print('%03d' % data)
# C:\...\PP4E\System\Streams> python writer2.py | python sorter.py sort py output
# 000
# 042
# 123
# 999
# C:\...\PP4E\System\Streams> writer2.py | sorter.py shorter form
# ...same output as prior command on Windows...
# C:\...\PP4E\System\Streams> python writer2.py | python sorter.py | python adder.py
# 1164

