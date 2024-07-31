"""
Grocery Store Sales Tracking
Description:
You are managing the sales tracking for a grocery store. Track the total sales amount globally and the daily sales amount locally within a function.

Task:
Define a global variable total_sales to keep track of the total sales amount.
Define a function record_sales() that uses a local variable to count the daily sales amount.
Use the global keyword to update the total_sales from within record_sales().
Call record_sales() for multiple days and print the total sales at the end.
"""
total_sales = 0


def record_sales():
    global total_sales
    local_sales = 0
    while True:
        sale = input("type sales amount / exit for day: ")
        if sale.lower() == "exit":
            break
        else:
            local_sales += float(sale)
    total_sales += local_sales


days = int(input("enter total number of days to enter: "))
for _ in range(days):
    record_sales()
print(f"the total sales: {total_sales}")
