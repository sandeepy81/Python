Indian=["Dal","Roti","Chawal"]
Chinese=["spring roll","fried rice","veg manchurian"]
Italian=["Pasta","Pizza","risotto"]
dish=input("Enter the dish name:")
if dish in Indian:
    print("Indian")
elif dish in Chinese:
    print("Chinese")
elif dish in Italian:
    print("Italian")
else:
    print("I can not recognize")

