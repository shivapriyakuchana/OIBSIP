# This function prompts the user to input a number and keeps asking until a valid number is provided.
def get_user_input(prompt):
    while True:
        try:
            # Convert the input to a float and ensure it is positive.
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            # Handle the case where the input is not a number.
            print("Invalid input. Please enter a number.")

# This function calculates BMI using the formula: BMI = weight / (height_in_meters^2)
def calculate_bmi(weight, height_m):
    return weight / (height_m ** 2)

# This function classifies the BMI into categories based on standard ranges.
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main function to run the BMI calculator.
def main():
    print("Welcome to the BMI Calculator")

    # Get the user's weight and height with proper input validation.
    weight = get_user_input("Please enter your weight in kilograms: ")
    height_m = get_user_input("Please enter your height in meters: ")

    # Calculate the BMI.
    bmi = calculate_bmi(weight, height_m)
    
    # Classify the BMI into a category.
    category = classify_bmi(bmi)

    # Display the BMI and its category to the user.
    print(f"Your BMI is {bmi:.2f}. You are classified as: {category}")

# Ensuring the script runs only when executed directly.
if __name__ == "__main__":
    main()
