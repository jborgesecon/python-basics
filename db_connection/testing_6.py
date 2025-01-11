import credentials as cr
import sqlalchemy as sa
import pandas as pd


# postgresql connection
psql_str = cr.conn_strings[0]
psql_engine = sa.create_engine(psql_str)

dataframe = cr.execute('query2', psql_engine)
print(dataframe) # all good


# # cockroachdb connection
# cockroach_str = cr.conn_strings[1]
# cockroach_engine = sa.create_engine(cockroach_str)

# dataframe1 = cr.execute('query1', cockroach_engine)
# print(dataframe1) # all good