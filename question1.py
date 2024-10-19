
# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 
def temperature_classification():
    temperature =float(input("\nEnter the temperature in °C:   "))
    if temperature < 0 :
        print('Freezing')
    elif temperature >=0 and temperature <= 10 :
        print('Cold')
    elif temperature >=11 and temperature <= 20 :
        print('Moderate')
    elif temperature >=21 and temperature <= 30 :
        print('Warm')
    else:
        print('Hot')
temperature_classification()
    
# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place

def volume_of_the_sphere():
    r = float(input("\nEnter the radius of a sphere:  "))
    import math
    volume = ((4/3)*math.pi*r**2)
    print(f"The volume of the sphere with radius {r} is equal to {volume:.1f}",end='\n\n')
volume_of_the_sphere()


