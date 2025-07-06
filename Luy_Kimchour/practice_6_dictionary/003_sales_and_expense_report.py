data = {
    'January': {'sales': 1000, 'expenses': 400},
    'February': {'sales': 1200, 'expenses': 500},
    'March': {'sales': 900, 'expenses': 450}
}

def compute_and_print_total_sales_expense(data):
    # print total salse and total expense
    total_sales = 0
    total_expenses = 0
    for month_data in data.values():
        total_sales += month_data['sales']
        total_expenses += month_data['expenses']
    print(f"Total sales: {total_sales}, Total expense: {total_expenses}")
    return (total_sales, total_expenses)

def calculate_profit_for_each_month(data):
    # calculate profit for each month
    profit_data = {}
    for month, month_data in data.items():
        profit_data[month] = month_data['sales'] - month_data['expenses']
    return profit_data

if __name__ == "__main__":
    compute_and_print_total_sales_expense(data)
    print(calculate_profit_for_each_month(data))
    
