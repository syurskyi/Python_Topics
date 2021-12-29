import  pandas as pd

PATH = 'C:\\Users\\Swee-Chuan Khoo\\Documents\\covic19_MoH\\covid19-public\\'

EPIDEMIC = PATH+"epidemic"
MYSEJAHTERA = PATH+"mysejahtera"
STATIS = PATH+"static"

df = pd.read_csv(EPIDEMIC+"\\cases_state.csv")

print(df['cases_new'].describe())