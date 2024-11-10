# 1. Create a simple .txt file within your project in PyCharm. This is achieved by right-
# clicking on project name, choose New, File and type the file name with the
# extension as follows: simpleText.txt. make use of with open and:
# a. Put some text into the file – a few sentences
# b. Read the entire contents and print it
# c. Read one and print it
# d. Use readlines() to print as a string in a list, use time.sleep(2) to slow it
# down
import csv
from itertools import product
from random import random, randint


def read_text_file():
    the_file = open("simpleText.txt", 'r')
    content = the_file.read()
    print(f'Just reading the content from the file: \n {content}')
    the_file.close()


def read_one_line_text_file():
    the_file = open("simpleText.txt", 'r')
    content = the_file.readline()
    print(f'Just reading one line from the file: \n {content}')
    the_file.close()


def read_text_file_convert_to_list():
    the_file = open("simpleText.txt", 'r')
    content = the_file.readlines()
    print(f'Just reading content from the file and convert to list: \n {content}')


# read_text_file()
# read_one_line_text_file()
# read_text_file_convert_to_list()

# 2. Using the simple.txt file above write a function the reads the file and counts the
# occurrence of each word as well as how many vowels are in each sentence.

def get_word_and_vowel_count():
    with (open('simpleText.txt', 'r') as simple_file):
        word_count = 0

        for each_line in simple_file.readlines():
            vowel_count = 0
            # print(each_line)
            for each_word in each_line.split():
                # print(each_word)
                word_count += 1
                for each_letter in each_word:
                    if 'a' in each_letter or 'e' in each_letter or 'i' in each_letter or 'o' in each_letter or 'u' in each_letter:
                        vowel_count += 1
            print(f"Total vowel words in the sentence {vowel_count}")
        print(f"Total words in the file {word_count}")


# get_word_and_vowel_count()


# Read the sales data from the csv file given to you. Make use of the sales.csv file
# and write a function to calculate total amount to pay given the quantity and the
# price. Include a grand total of all sales.
# Hints: using a for loop split each row of the csv file into parts. Once you have a []
# of each row use a for loop to determine the total for each sale as well as the total
# sales amount for all sales.
# This exercise forms part of a ChatGPT formative assessment. Once you have
# completed this exercise ask ChatGPT to give you feedback on your solution.
# After reading the feedback decide what grade you would give yourself out
# of 10. For example, if the feedback came back as almost correct however ....
# then give yourself 8 or 9 out of 10. You need to then go to the link given to
# you in Canvas – under labs week 5 – and complete the questions.


def calculate_total_from_file():
    total_amount = 0
    with open('sales.csv', 'r') as sales_report:
        for sale in sales_report:
            sales_row = sale.strip().split(';')
            each_sale_amount = float(sales_row[1]) * float(sales_row[2])
            total_amount = total_amount + each_sale_amount
            print(f"On {sales_row[0]} the total sale is {each_sale_amount}")

        print(f"The total sales amount for all sales  {total_amount}")


# calculate_total_from_file()


# You need to write a solution for the following sales analysis for an e-commerce
# company problem. This company would like to analyse its monthly sales data to
# understand performance, customer demographics and product popularity.
# However, the data is stored in 3 different files, given to you.
# Sales data -> order_id, product_id, cust_id, quantity, sale_date
# Product info -> product_id, product_name, price
# Customer info -> cust_id, cust_name, age, location
# You need to create a solution for the company that displays a monthly report.
# The key elements for the report are:
# total sales -> total sales for each product
# customer demographic -> details of a customer (include name and city)
# purchasing a product (you only need to show the prod_id )
# Hint: In order to solve this you need to create a {} for sales.csv, products.csv and
# customer.csv so that you can manipulate data to process reports.

_sales_data = {}
_product_info = {}
_customer_info = {}


def convert_sales_csv_to_dict(file_name, target_dict):
    with open(file_name) as file:
        list_convertor = []
        for row in file:
            row_split = row.strip().split(";")
            local_dict = {
                'order_id': row_split[0],
                'product_id': row_split[1],
                'cust_id': row_split[2],
                'sale_date': row_split[3],
            }
            list_convertor.append(local_dict)

        target_dict[file_name.split('.')[0]] = list_convertor


def convert_product_csv_to_dict(file_name, target_dict):
    with open(file_name) as file:
        list_convertor = []
        for row in file:
            row_split = row.strip().split(";")
            local_dict = {
                'product_id': row_split[0],
                'product_name': row_split[1],
                'price': row_split[2],
            }
            list_convertor.append(local_dict)

        target_dict[file_name.split('.')[0]] = list_convertor


def convert_customer_csv_to_dict(file_name, target_dict):
    with open(file_name) as file:
        list_convertor = []
        for row in file:
            row_split = row.strip().split(";")
            local_dict = {
                'cust_id': row_split[0],
                'cust_name': row_split[1],
                'age': row_split[2],
                'location': row_split[3]
            }
            list_convertor.append(local_dict)

        target_dict[file_name.split('.')[0]] = list_convertor


convert_sales_csv_to_dict('sales1.csv', _sales_data)
convert_product_csv_to_dict('product.csv', _product_info)
convert_customer_csv_to_dict('customer.csv', _customer_info)


# print(_sales_data)
# print(_product_info)
# print(_customer_info)


# just to print after one line
def title(name_of_title):
    print('\n')
    print(f"{name_of_title}:")


def total_sales():
    title('Total sales report for each product')
    for product_details in _product_info['product']:
        count = 0
        for sale in _sales_data['sales1']:
            if sale['product_id'] == product_details['product_id']:
                count += 1
        print(f"For {product_details['product_name']} the total number of sales are {count}")


def customer_details():
    title('Customer details')
    count = 0
    for customer in _customer_info['customer']:
        count += 1
        print(f" Customer {count} - Name: {customer['cust_name']}, city: {customer['location']} ")


def purchase_product():
    title('Here are the product available')
    product_want_to_buy = view_available_product().lower()
    for product_details in _product_info['product']:
        if product_details['product_name'].lower() == product_want_to_buy:
            _sales_data['sales1'].append({
                'order_id': f's122',
                'product_id': product_details['product_id'],
            })


def view_available_product():
    count = 0
    for product_details in _product_info['product']:
        count += 1
        print(f" Product {count} - Name: {product_details['product_name']}, Price: {product_details['price']}")
    return input("Enter the product name you would like to purchase: ")


# total_sales()
# customer_details()
# purchase_product()


# Given the following student data write a report to a file. The student data is as
# follows:
# student_data = [
# {“student_id” : “12345”, “grade1”: 47, “grade2”: 20, “grade3””65},
# {add the others as below}
# ]
# Make use of f-string to write() the report to the file called student_report.csv.
# This is what the file should look like, it also includes the average of the students
# rounded off to 2 decimals.


student_data = [
    {"student_id": "12345", "grade1": 47, "grade2": 20, "grade3": 65},
    {"student_id": "23456", "grade1": 77, "grade2": 50, "grade3": 45},
    {"student_id": "34567", "grade1": 67, "grade2": 80, "grade3": 99},
    {"student_id": "45678", "grade1": 47, "grade2": 20, "grade3": 65},
]


def export_student_data():
    with open('student_report.csv', 'w') as student_data_file:
        student_data_file.write('Student data report\n')
        student_data_file.write(f"{'=' * 20}\n")
        for student_details in student_data:
            student_data_file.write(f"Student id: {student_details['student_id']}\t")
            student_data_file.write(f"Grade 1: {student_details['grade1']}\t")
            student_data_file.write(f"Grade 2: {student_details['grade2']}\t")
            student_data_file.write(f"Grade 3: {student_details['grade3']}\t")
            student_data_file.write(
                f"Average for a student is 3: {((int(student_details['grade1']) + int(student_details['grade2']) + int(student_details['grade3'])) / 3):0.5f}\n")


export_student_data()


# (a) Using the student_report.csv file read the contents in and print to the screen
# in the following format (use the csv.reader() to do this:
# (b) Using the student_report.csv open the file again and read using csv.reader().
# This time create a dictionary with each row. Challenge: the headers must not be
# read in. Make use of next() to skip the headers.






