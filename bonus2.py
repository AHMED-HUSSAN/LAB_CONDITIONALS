
#user's wieght
wieght = float(input("WRITE YOUR WIEGHT: \n"))

#user's height
height = float(input("WRITE YOUR HEIGHT: \n"))


#BMI
Bmi = wieght / (height ** 2)
print("YOUR BMI = ", Bmi)

#IF conditional
if 25 <= Bmi < 29.9 :
    print("You are overwieght you need to work out more and watch your diet.")
    
elif 18.5 <= Bmi < 24.9 :
    print("You are fit & healthy.")
    
elif Bmi <= 18.5 : 
    print("You are underweight. Watch your health.")
    

    
