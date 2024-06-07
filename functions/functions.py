def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total

toms_exp=[1200,4500,2343,2500]
johns_exp=[1300,1400,2500,500]

toms_total=calculate_total(toms_exp)
johns_total=calculate_total(johns_exp)

print("Toms total exp: ", toms_total)
print("Johns total exp: ", johns_total)