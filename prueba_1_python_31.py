Niño = 5500
Joven = 7000
Adulto = 9000
totalNiño = 0
totalJoven =0
totalAdulto = 0
sw=1
total1=0
total2=0
total3=0
decision=0
while sw==1:
    try:
        vOp = int(input("¿Qué tipo de entrada desea?: \n1.- Niño (1 a 13 años)\n2.- Jóven (14 a 21 años)\n3.- Adulto (Mayor a 22)\n4.- Salir\nDigite: "))
        if vOp==1:
            total = Niño
            cantidadEntradas = int(input(f"El precio de su entrada es de ${Niño} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total *= cantidadEntradas
            totalNiño += cantidadEntradas
            print(f"----------BOLETA---------\nCategoría: Niño\nCantidad de entradas: {cantidadEntradas}\nTotal a pagar: ${total} pesos")
            total1 = total
            print("Gracias por su compra, disfrute la función.")

        if vOp==2:
            total = Joven
            cantidadEntradas = int(input(f"El precio de su entrada es de ${Joven} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total *= cantidadEntradas
            totalJoven += cantidadEntradas
            print(f"--------BOLETA----------\nCategoría: Jóven\nCantidad de entradas: {cantidadEntradas}\nTotal a pagar: ${total} pesos")
            total2 = total
            print("Gracias por su compra, disfrute la función.")
            
        if vOp==3:
            total = Adulto
            cantidadEntradas = int(input(f"El precio de su entrada es de ${Adulto} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total *= cantidadEntradas
            totalAdulto += cantidadEntradas
            print(f"--------BOLETA--------\nCategoría: Adulto\nCantidad de entradas: {cantidadEntradas}\nTotal a pagar: ${total} pesos")
            total3 = total
            print("Gracias por su compra, disfrute la función.")

        if vOp==4:
            sw=0
        
            

        
        
        decision = int(input("¿Desea realizar otra compra?\n1.- Si\n2.- No\nDigite: "))
        
        totalEntradas = (totalNiño + totalJoven + totalAdulto)
        totalTodo = total1 + total2 + total3
        print(f"La cantidad de entradas de categoría \"Niño\" vendidas es: {totalNiño} ({((totalNiño*1.00)//totalEntradas)}% de las entradas totales.)")
        print(f"La cantidad de entradas de categoría \"Jóven\" vendidas es: {totalJoven} ({((totalJoven*100)//totalEntradas)}% de las entradas totales.)")
        print(f"La cantidad de entradas de categoría \"Adulto\" vendidas es: {totalAdulto} ({((totalAdulto*100)//totalEntradas)}% de las entradas totales.)")
        print(f"Total de ganancias del día: ${totalTodo} pesos")
    except ValueError:
        print("Acción no valida.")
        
       
        

    
    