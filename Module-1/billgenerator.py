print("===== ELECTRICITY BILL GENERATOR =====")

name = input("Enter consumer name: ")
consumer_id = input("Enter consumer ID: ")

previous_reading = float(input("Enter previous meter reading: "))
current_reading = float(input("Enter current meter reading: "))
cost_per_unit = float(input("Enter cost per unit: "))

units_consumed = current_reading - previous_reading
energy_charge = units_consumed * cost_per_unit

fixed_charge = 100
total_bill = energy_charge + fixed_charge

print("\n========== ELECTRICITY BILL ==========")
print("Consumer Name:", name)
print("Consumer ID:", consumer_id)
print("Units Consumed:", units_consumed)
print("Energy Charge: ₹", energy_charge)
print("Fixed Charge: ₹", fixed_charge)
print("--------------------------------------")
print("Total Bill: ₹", total_bill)
print("======================================")