'''
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
'''
def calculate_profit_loss(cost, selling_price):
    # Total cost of a dozen bananas
    total_cost = cost
    # Total selling price for a dozen bananas
    total_selling_price = selling_price * 12
    
    # Calculate profit or loss
    profit_loss = total_selling_price - total_cost
    
    return profit_loss

# Input
cost = float(input())
selling_price = float(input())

# Calculate profit or loss
result = calculate_profit_loss(cost, selling_price)

# Output result
if result > 0:
    print(f"Profit : Rs.{result:.2f}")
elif result < 0:
    print(f"Loss : Rs.{-result:.2f}")
else:
    print("No Profit No Loss")
