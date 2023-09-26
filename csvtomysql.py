
#import the libraries
import pandas as pd
import sqlalchemy

#load csv file to dataframe
data=pd.read_csv('data.csv',index_col=False,delimiter=',')


#do some data cleaning .change to datetime and balance to float
data['Completion Time']=pd.to_datetime(data['Completion Time'],dayfirst=True)
data['Initiation Time']=pd.to_datetime(data['Initiation Time'],dayfirst=True)
data['Balance']=data['Balance'].str.replace(',','').astype(float)
data['A/C No.']=data['A/C No.'].astype(object)
print(data.dtypes)
print(data.head())
#create connection to mysql
# Define your MySQL connection string
connection_string = "mysql+mysqlconnector://root:root@127.0.0.1:3306/transactions"

try:
    # Create a SQLAlchemy engine
    engine = sqlalchemy.create_engine(connection_string)
    
    # Assuming you have a DataFrame named 'data'
    data.to_sql(name='data', con=engine, if_exists='replace', index=False)

    print("DataFrame successfully loaded to MySQL with inferred schema.")
except Exception as e:
    print("Error loading DataFrame to MySQL:", e)

