# 1. function to replace every s with $-----------------------------------------------------------------------

def dollarizer(text):
    return text.replace("s", "$").replace("s", "$").capitalize()

# Ask user for input
user_input = input("Enter any text: ")

# call the function 
modified_text = dollarizer(user_input)
# print output
print(f"Modified text: {modified_text}")

# 2. function that replaces every e with euro sign------------------------------------------------------------

def eurizer(text):
    return text.replace("e", "€").replace("e", "€").capitalize()

# Ash user for input
user_input = input("Enter text: ")

# call function
result = eurizer(user_input)

# print output
print(f"Modified text: {result}")

# 3. Combine dollarizer and eurizer functions into one general function called reolacer---------------------------

def replacer(word:str, old: str, new: str) -> str:
    """Replace every occurances of character 'old' with 'new' in the given word."""
    return word.replace(old, new)

replacer_word = input("Enter replacer word? ")
# Call the function
result1 = replacer(replacer_word, 't', '#')
print(f"Replacer word:{result1}")

# 4. A function that replaces every s with the $ and every e with the euro sign and every i with £-----------------

def wonky_text(text: str) -> str:
    """Replace every s with $, e with €, and i with £ in the given text."""
    test = dollarizer(text)
    test = eurizer(test)
    text = replacer(test, 'i', '£')
    return text

# Ask user for input
user_input2 = input("Enter wonky text: ")

# Call the function
modified_wonky_text = wonky_text(user_input2)

# print output
print(f"Modified wonky text: {modified_wonky_text}")

# 5. Creating a function to return celsius to fahrenheit-----------------

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert celsius to fahrenheit using F = C * 9/5 + 32."""
    return celsius * 9/5 + 32

# Ask user for input
celsius_input = float(input("Enter celsius number: "))

# Call the function
fahrenheit_output = celsius_to_fahrenheit(celsius_input)
print(f"{celsius_input}°C is equal to {fahrenheit_output}°F")

# 6. Creatibg a function that takes age in years -----------------------------------------------------

def age_in_days(years: int) -> int:
    """convert years to days (ignoring leap years)."""
    return years * 365

# Ask user input
years_input = int(input("How old are you? "))

# Call the function
days_output = age_in_days(years_input)
print(f"You are approximately {days_output} days old.")

# 7. Function the calculates simple interest-------------------------------------------------

def simple_interest(principal: float, rate: float, time_years: float) -> float:
    """Calculate simple interest using formula SI = (P * R * T)."""
    return (principal * rate * time_years)

# Ask user input
principal_input = float(input("Enter the principal amount: "))
rate_input = float(input("Enter the rate of interest: "))
time_input = float(input("Enter the time in years: "))

# cal;l the function
interest_output = simple_interest(principal_input, rate_input, time_input)
print(f"The simple interest is: {interest_output:.2f}")

# 8. function that takes principal amount, rate of interest, time in years and desired final amount after simple interest-----------------------------------

def plan_finances(principal: float, rate: float, time_years: float, desired_final: float) -> bool:
    """Check if the final amount (principal + simple interest) meet or exceed the goal."""
    si = simple_interest(principal, rate, time_years)
    final_amount = principal = si
    return final_amount >= desired_final

# Ask user input
principal_input3 = float(input("Ente your desired final amount: "))

# Call the function
rate_input3 = plan_finances(principal_input3, rate_input, time_input, 1500)
print(f"Plan Finances:{rate_input3}")