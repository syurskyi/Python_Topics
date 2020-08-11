# MAKETREEDIR

OS wrapper python package which checks if a given folder tree path exists and creates them.


### Installation

Once you have cloned the repository, you can easily install by

`pip install MakeTreeDir`

### Usage

Consider a situation where you have to create a folder tree like folder structure. i.e Folder inside a folder inside a folder
If you have to make use of traditional approaches, you have to write a number of loops and checks for doing so using os library.
This wrapper has already done it and you can create any folder tree structure in one line.
eg:
```python
from MakeTreeDir import MAKETREEDIR
md=MAKETREEDIR()
md.makedir('this/is/a/testing/package/creation')

### Corner cases
md.makedir('/media/username/New Volume/folderName')
md.makedir('../../../folderName')
md.makedir('C:\\Users\\userName\\folderName')

```
The folders will be created instantly.
## Authors

* **Sreekiran A R** - *Senior Analytics Consultant, AI Labs, Bridgei2i Analytics Solutions* -
 [Github](https://github.com/Sreekiranar) ,
[Stackoverflow](https://stackoverflow.com/users/9605907/sreekiran)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
