# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese"
# weight = float(input("Enter weight in kg: "))


def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / height
    
    # Determine BMI category
    if bmi < 18.5:
        return bmi, "Underweight"
    elif bmi < 25:
        return bmi, "Normal weight"
    elif bmi < 30:
        return bmi, "Overweight"
    else:
        return bmi, "Obese"
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))

bmi,category = calculate_bmi(weight, height)
print(f"Your BMI is : {bmi:.2f}, Category: {category}")
calculate_bmi(weight, height)






# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)

radius = float(input("\nEnter the radius of a cylinder:  "))
height = float(input("Enter the height of a cylinder:  "))
def volume_of_a_cylinder(radius,height):
    import math
    volume = (math.pi*(radius**2)*height)
    print(f"The volume of the sphere with radius {radius} and height {height} is {volume}\n\n")
volume_of_a_cylinder(radius,height)