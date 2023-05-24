print("Datos Personales")
print("----------------------\n")
vNombre = input("Ingrese su nombre: "):
while True:
    try:
        vEdad = int(input("Ingrese su edad: "))
        break
    except:
        print("Valor no corresponde")

print("----------------------------------")
print(f"Su nombres es: {vNombre}") 
print(f"Su edad es: {vEdad}") 
print("-------------------------------")      
print("Programa finalizado. ")