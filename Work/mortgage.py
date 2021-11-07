# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0     
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
months = 0

while principal > 0:
    if (principal < payment):
        principal = principal
        total_paid = total_paid + principal
        months += 1
        print(f"{months}\t{round(total_paid, 2)}\t{round(principal, 2)}")
        break
        
    else :
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment   
      
    months += 1
    
    if (months >= extra_payment_start_month) and (months <= extra_payment_end_month) :
        principal -=  extra_payment
        total_paid += extra_payment
        
    print(f"{months}\t{round(total_paid, 2)}\t{round(principal, 2)}")

print(f"Total paid {round(total_paid, 2)} over {months} months")
