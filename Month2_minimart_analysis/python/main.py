

# ---SIMULATE INITIAL DATA ---
# Using Python dictionaries and lists to represent the relational data.
# Note: Prices are intentionally stored as strings to demonstrate type conversion later.

customers_data = {
    101: 'Sophia Rodriguez',
    102: 'Ethan Carter',
    103: 'Olivia Murphy',
    104: 'Liam Patel',
    105: 'Ava Dubois',
}

# The price is a string for the type conversion exercise
products_data = [
    {'product_id': 1, 'name': 'Noise Cancelling Headphones', 'category': 'Audio', 'price': '249.99'},
    {'product_id': 2, 'name': 'Portable SSD 1TB', 'category': 'Storage', 'price': '79.50'},
    {'product_id': 3, 'name': 'Smart Watch Series 7', 'category': 'Wearables', 'price': '329.00'},
    {'product_id': 4, 'name': 'Premium Coffee Beans (1kg)', 'category': 'Food & Beverage', 'price': '19.99'},
    {'product_id': 5, 'name': 'Wireless Charging Pad', 'category': 'Accessories', 'price': '34.95'},
    {'product_id': 6, 'name': 'Smart Mug (12oz)', 'category': 'Accessories', 'price': '45.00'},
]

# Original orders provided in the SQL prompt
original_orders = [
    {'customer_id': 101, 'product_id': 1, 'quantity': 1},
    {'customer_id': 103, 'product_id': 4, 'quantity': 3},
    {'customer_id': 101, 'product_id': 5, 'quantity': 2},
    {'customer_id': 104, 'product_id': 2, 'quantity': 1},
    {'customer_id': 102, 'product_id': 4, 'quantity': 1},
    {'customer_id': 105, 'product_id': 1, 'quantity': 1},
]

# Simulate new order data
new_orders = [
    {'customer_id': 102, 'product_id': 3, 'quantity': 1},
    {'customer_id': 104, 'product_id': 4, 'quantity': 10}, # Large quantity order
    {'customer_id': 105, 'product_id': 1, 'quantity': 3}, # Large revenue order
    {'customer_id': 103, 'product_id': 6, 'quantity': 1},
]

all_orders = original_orders + new_orders





# --- PRE-PROCESS DATA: TYPE CONVERSION AND DISCOUNTS ---

# Convert products list to a dictionary for O(1) lookup by product_id
# and perform the required type conversion (string to float).
import collections
processed_products = {}
for product in products_data:
    product_id = product['product_id']
    # 3. Convert product prices from string to float
    original_price = float(product['price'])
    final_price = original_price

    # Apply 10% discount if the original price is greater than 100
    if original_price > 100.00:
        discount = 0.10
        final_price = original_price * (1 - discount)
        print(f"Discount applied to Product ID {product_id} ({product['name']}): Original ${original_price:.2f}, Final ${final_price:.2f}")

    processed_products[product_id] = {
        'name': product['name'],
        'category': product['category'],
        'price': final_price # Store the converted and discounted price
    }


# --- ANALYSIS AND REPORT GENERATION ---

# Initialize variables for the final report
product_sales_count = collections.Counter()
revenue_per_customer = collections.defaultdict(float)
large_order_customers = []

# Define thresholds for a "large order"
LARGE_QUANTITY_THRESHOLD = 5
HIGH_VALUE_THRESHOLD = 500.00

print("\n--- Processing Orders and Identifying Large Orders ---")

for order in all_orders:
    cust_id = order['customer_id']
    prod_id = order['product_id']
    qty = order['quantity']

    # Get product details (already processed and discounted)
    product = processed_products.get(prod_id)
    if not product:
        continue # Skip if product ID is invalid

    # Calculate total order value
    order_value = product['price'] * qty

    # Update metrics for the report
    product_sales_count[product['name']] += qty
    revenue_per_customer[cust_id] += order_value
    
    
    

    # 4. Use if, and, or to identify customers who placed large orders
    # A large order is defined as:
    # 1. Quantity is large (>= 5) OR
    # 2. Total order value is high (>= $500.00)
    # AND the customer ID is not already recorded as a large order customer.
    if (qty >= LARGE_QUANTITY_THRESHOLD or order_value >= HIGH_VALUE_THRESHOLD) and cust_id not in large_order_customers:
        large_order_customers.append(cust_id)
        customer_name = customers_data.get(cust_id, "Unknown Customer")
        print(f"LARGE ORDER identified for {customer_name} (ID: {cust_id}). Quantity: {qty}, Value: ${order_value:.2f}")

# Determine the most popular product
most_popular_product_name = product_sales_count.most_common(1)[0][0] if product_sales_count else "N/A"

# Format revenue per customer for the final report
formatted_customer_revenue = {
    customers_data.get(cid, f"ID {cid}"): f"${rev:.2f}"
    for cid, rev in revenue_per_customer.items()
}

# Create a dictionary report summarizing findings
mini_mart_report = {
    "total_products_sold": sum(product_sales_count.values()),
    "most_popular_product": most_popular_product_name,
    "revenue_per_customer": formatted_customer_revenue,
    "large_order_customers_ids": large_order_customers,
    "large_order_customers_names": [customers_data[cid] for cid in large_order_customers]
}

print("\n" + "="*40)
print("FINAL MINI-MART ANALYSIS REPORT")
print("="*40)

# Display the final report
for key, value in mini_mart_report.items():
    print(f"{key.replace('_', ' ').title()}:")
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            print(f"  - {sub_key}: {sub_value}")
    else:
        print(f"  {value}")

print("="*40)
