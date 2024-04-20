import pandas as pd
from pandasql import sqldf

# Load the spreadsheet into a DataFrame
df = pd.read_csv('/Users/dhruvikadhiwala/Desktop/atlanta.csv')

# This is a helper function to make it easier to run SQL queries on our dataframe
pysqldf = lambda q: sqldf(q, globals())

# Example SQL query
# Replace 'your_table' with the name you'd like to refer to your DataFrame as in your SQL query,
# and adjust the SQL query according to your needs.
query = """
SELECT *
FROM df
LIMIT 10;
"""

# Run the SQL query
result = pysqldf(query)

# Display the result
print(result)
