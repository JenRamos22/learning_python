
purchases = [15.0, 45.0, 8.0, 60.0]

def calculate_total_spent(purchase_list):
    total_spent = 0
    
    for amount in purchase_list:
        total_spent = total_spent + amount
        
    return total_spent

# Probar la función
final_total = calculate_total_spent(purchases)

print("Total amount spent:")
print(final_total)