from faker import Faker
import pandas as pd
import random
import logging
from ..logger import CustomFormatter
import os
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

fake=Faker()

# Data Models

## Employee
def generate_employee(employee_id):
    return {
        "employee_Id": employee_id,
        "first_name": fake.first_name(),
        "last_name":fake.last_name(),
        "email":fake.email(),
        "salary":random.randint(3000,10000)
    }

def generate_customer(customer_id):
    return {
        "customer_id": customer_id,
        "customer_name": fake.name(),
        "address": fake.street_address(),
        "city": fake.city(),
        "zip_code": fake.zipcode()
    }

def generate_product(product_id):
    return {
        "product_id": product_id,
        "product_name": fake.word().capitalize(),
        "price": round(random.uniform(1.0, 1000.0), 2),
        "description": fake.sentence(),
        "category": fake.random_element(elements=("Electronics", "Clothing", "Home & Garden", "Toys", "Books"))
    }

from datetime import datetime
def generate_orders(order_id):
    # Generate a random date between a specific date range
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = fake.date_time_between_dates(start_date, end_date)

    # Extract year, quarter, and month from the random date
    year = random_date.year
    quarter = (random_date.month - 1) // 3 + 1
    month = random_date.strftime('%B')

    return {
        "order_id": order_id,
        "order_date": random_date,
        "year": year,
        "quarter": quarter,
        "month": month
    }

def generate_sales(transaction_id, order_id, product_id, customer_id, employee_id):
    total_sales = round(random.uniform(10.0, 500.0), 2)
    quantity = random.randint(1, 10)
    discount = round(random.uniform(0.0, 0.5), 2)

    return {
        "transaction_id": transaction_id,
        "order_id": order_id,
        "product_id": product_id,
        "customer_id": customer_id,
        "employee_id": employee_id,
        "total_sales": total_sales,
        "quantity": quantity,
        "discount": discount
    }



