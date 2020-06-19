from peewee import *



db = PostgresqlDatabase('spm', user="postgres",
                        password='password', host='localhost', port=5432)

db.connect()
