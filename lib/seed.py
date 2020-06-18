from peewee import *
import json
import sys
from psycopg2 import connect, Error

db = PostgresqlDatabase('spm', user="postgres",
                        password='password', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class ExploreCard(BaseModel):
    name = CharField()
    sort = CharField()
    char_type = CharField()
    affinity = CharField()
    move = IntegerField()
    ap = IntegerField()
    strength = CharField()
    arm = CharField()
    will = CharField()
    dex = CharField()
    heart = IntegerField()
    sk_pn = IntegerField()
    bit = CharField()
    abilities = []


db.connect()


tables = [ExploreCard]
db.drop_tables(tables)
db.create_tables(tables)

# with open('SDESEEDDATA.json') as json_data:
#     record_list = json.load(json_data)

# if type(record_list) == list:
#     first_record = record_list[0]
#     columns = list(first_record.keys())

# table_name = "ExploreCard"
# sql_string = f'INSERT INTO {table_name} '
# sql_string += "(" + ','.join(columns) + ")\nValues "


# values = [list(x.values()) for x in record_list]
# for i, record in enumerate(values):

#     # declare empty list for values
#     val_list = []

#     # append each value to a new list of values
#     for v, val in enumerate(record):
#         if type(val) == str:
#             val = str(Json(val)).replace('"', '')
#         val_list += [str(val)]

#     # put parenthesis around each record string
#     values_str += "(" + ', '.join(val_list) + "),\n"

# # remove the last comma and end SQL with a semicolon
# values_str = values_str[:-2] + ";"

# print("\nSDE Statement")
# print(sql_string)
# db.execute(sql_string)
