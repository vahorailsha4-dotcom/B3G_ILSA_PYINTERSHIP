h_cm="175"
w_kg="68.5"

h_cm=int(h_cm)
w_kg=float(w_kg)

h_m=h_cm/100
bmi=w_kg/(h_m*h_m)
print("BMI:",bmi)