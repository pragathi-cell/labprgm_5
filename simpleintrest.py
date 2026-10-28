# Program to calculate Simple Interest

def calculate_simple_interest():
    try:
        # Taking inputs from the user
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual rate of interest (in %): "))
        time = float(input("Enter the time period (in years): "))
        
        # Simple Interest formula: (P * R * T) / 100
        interest = (principal * rate * time) / 100
        
        # Displaying the output
        print(f"\n--- Expected Output ---")
        print(f"Principal Amount: {principal}")
        print(f"Interest Rate   : {rate}%")
        print(f"Time Period     : {time} years")
        print(f"Simple Interest : {interest:.2f}")
        
    except ValueError:
        print("Invalid input! Please enter numerical values.")

if __name__ == "__main__":
    calculate_simple_interest()