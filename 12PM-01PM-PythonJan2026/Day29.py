"""
run in the bash cell/command prompt/terminal

pip install pandas
pip install openpyxl

"""
import pandas

data = pandas.read_excel("C:/Users/Croma Campus/Downloads/Financial_Sample.xlsx")

print(data)

print( data.head(10) )

print( data.isnull().sum() )


"""

RUN THIS SCRIPT ON YOUR COMMAND PROMPT/TERMINAL

pip install jupyter

"""

