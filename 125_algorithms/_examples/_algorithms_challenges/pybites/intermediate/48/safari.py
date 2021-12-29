import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def create_chart():
    slack_frequency = {}

    with open(SAFARI_LOGS) as file:
        safari_logs = file.readlines()
        for i in range(len(safari_logs)):
            previous = safari_logs[i -1]
            current = safari_logs[i]
            if "sending to slack channel" in current:
                if current[:5] not in slack_frequency:
                    slack_frequency[current[:5]] = [1]
                    if 'Python' in previous:
                        slack_frequency[current[:5]].append(slack_frequency[current[:5]][0]) 
                else:
                    slack_frequency[current[:5]][0] += 1
                    if 'Python' in previous:
                        slack_frequency[current[:5]].append(slack_frequency[current[:5]][0])

    for key, value in slack_frequency.items():

        bar = ""
        if len(value) == 1:
            for i in range(1, value[0] +1):
                bar += "."
            print(key, bar)
        else:
            j = 1
            for i in range(1, value[0] +1):
                snake_num = len(value) -1
                if j <= snake_num:
                    snake_value_at_i = value[j]

                if i == snake_value_at_i:
                    bar += "🐍"
                    j += 1
                else:
                    bar += "."
        
            print(key, bar)


# if __name__ == "__main__":
#     create_chart()