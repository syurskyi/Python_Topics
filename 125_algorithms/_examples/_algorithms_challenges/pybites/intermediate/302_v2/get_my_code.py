import os
from pathlib import Path
from urllib.request import urlretrieve
import json

filename = "my_code.json"
url = "https://bites-data.s3.us-east-2.amazonaws.com/{filename}"
tmp = Path(os.getenv("TMP", "/tmp"))
json_input_file = tmp / filename

if not json_input_file.exists():
    urlretrieve(url.format(filename=filename), json_input_file)


def get_json_data():
    with open(json_input_file) as file_in:
        return json.load(file_in)


json_data = get_json_data()


def get_passing_code(json_data=json_data):
    """Get all passing code and write the code for each bite to individual files.
       Output file names should be the bite name and number with a .py extension,
       but not including the description.  For example, if the bite name is
       'Bite 124. Marvel data analysis' the output file name should be Bite124.py.
       Remove any/all spaces from the file name.
       Write to /tmp (tmp variable).
    """
    for bite in json_data['bites']:
        bite_name = bite['bite']
        bite_name = bite_name[:bite_name.index('.')]
        bite_name = bite_name.replace(' ','')

        passing_code = bite['passing_code']
        
        print(passing_code)
        path = tmp / f"{bite_name}.py"
        with open(path,'w') as f:
            f.write(passing_code)



if __name__ == "__main__":

    get_passing_code()

    




