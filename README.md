# ETL with Python

This module is going to integrated with the group project repository after customization.

With `__init__.py` files we have managed make our modules accessible. Likewise the `setup.py`

In data preperation directory we have:

- `data_generator.py:` for simulating data by using `faker` package
- `schema.py:` for desinging the schema
- `sql_interactions.py:` building dynamic, reproducible **CRUD** operations


## Steps 1: Schema Design

We will try to create below schema:

![Star Schema](star_schema.png)

In `schema.py`, we have used `sqlalchemy` package, which allows map python objects with SQL objects.

By running `schema_builder.py` you will see `temp.db` file in your folder.

## Step 2: Generating the data

running `data_generator.ipynb` file, you will see all the needed data. 

You can save any table as csv, then  read the table, in order to push to database.

Provide



## Step 3: Interacting with SQL

In `basic_etl.py` you need to initializa an object

`Inst=SqlHandler('temp', 'employees')`

Insert, update etc.

`Inst.insert_many(data)`

Close the connection:

`Inst.close_cnxn()`

