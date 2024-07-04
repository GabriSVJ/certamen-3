import csv

# Lista para almacenar los pedidos
pedidos = []

# Función para registrar un nuevo pedido
def registrar_pedido():
    print("\nRegistro de Nuevo Pedido\n")
    id_pedido = input("ID pedido: ")
    cliente = input("Nombre y apellido del cliente: ")
    direccion = input("Dirección del cliente: ")
    comuna = input("Comuna del cliente: ")
    disp_6lts = int(input("Cantidad de dispensadores de 6 litros: "))
    disp_10lts = int(input("Cantidad de dispensadores de 10 litros: "))
    disp_20lts = int(input("Cantidad de dispensadores de 20 litros: "))
    
    # Validar que la suma de las cantidades sea mayor a cero
    if disp_6lts + disp_10lts + disp_20lts <= 0:
        print("Error: La suma de las cantidades debe ser mayor a cero.")
        return
    
    pedido = {
        "ID pedido": id_pedido,
        "Cliente": cliente,
        "Dirección": direccion,
        "Comuna": comuna,
        "Disp. 6lts": disp_6lts,
        "Disp. 10lts": disp_10lts,
        "Disp. 20lts": disp_20lts
    }
    pedidos.append(pedido)
    print("Pedido registrado correctamente.\n")

# Función para listar todos los pedidos
def listar_pedidos():
    print("\nListado de Pedidos\n")
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
    else:
        print("{:<10} {:<20} {:<20} {:<10} {:<10} {:<10}".format(
            "ID pedido", "Cliente", "Dirección", "Comuna", "Disp. 6lts", "Disp. 10lts", "Disp. 20lts"))
        for pedido in pedidos:
            print("{:<10} {:<20} {:<20} {:<10} {:<10} {:<10} {:<10}".format(
                pedido["ID pedido"], pedido["Cliente"], pedido["Dirección"], pedido["Comuna"],
                pedido["Disp. 6lts"], pedido["Disp. 10lts"], pedido["Disp. 20lts"]))
    print()

# Función para imprimir hoja de ruta
def imprimir_hoja_ruta():
    print("\nImpresión de Hoja de Ruta\n")
    sectores = ["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]
    print("Sectores disponibles: ", ", ".join(sectores))
    seleccion_sector = input("Seleccione el sector para generar la hoja de ruta: ")
    
    # Filtrar pedidos por el sector seleccionado
    pedidos_sector = [pedido for pedido in pedidos if pedido["Comuna"] == seleccion_sector]
    
    if len(pedidos_sector) == 0:
        print(f"No hay pedidos registrados para el sector '{seleccion_sector}'.")
        return
    
    nombre_archivo = f"hoja_ruta_{seleccion_sector}.csv"
    encabezado = ["ID pedido", "Cliente", "Dirección", "Comuna", "Disp. 6lts", "Disp. 10lts", "Disp. 20lts"]
    
    with open(nombre_archivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(encabezado)
        for pedido in pedidos_sector:
            writer.writerow([pedido[clave] for clave in encabezado])
    
    print(f"Se ha generado el archivo '{nombre_archivo}' satisfactoriamente.\n")

# Función para buscar un pedido por ID
def buscar_pedido_por_id():
    print("\nBuscar Pedido por ID\n")
    id_busqueda = input("Ingrese el ID del pedido a buscar: ")
    encontrado = False
    
    for pedido in pedidos:
        if pedido["ID pedido"] == id_busqueda:
            print("Detalle del pedido encontrado:")
            print("{:<10} {:<20} {:<20} {:<10} {:<10} {:<10}".format(
                "ID pedido", "Cliente", "Dirección", "Comuna", "Disp. 6lts", "Disp. 10lts", "Disp. 20lts"))
            print("{:<10} {:<20} {:<20} {:<10} {:<10} {:<10}".format(
                pedido["ID pedido"], pedido["Cliente"], pedido["Dirección"], pedido["Comuna"],
                pedido["Disp. 6lts"], pedido["Disp. 10lts"], pedido["Disp. 20lts"]))
            encontrado = True
            break
    
    if not encontrado:
        print(f"No se encontró ningún pedido con el ID '{id_busqueda}'.")
    print()

# Función principal del programa
def main():
    while True:
        print("Bienvenido a CleanWasser - Sistema de Gestión de Pedidos\n")
        print("1. Registrar pedido")
        print("2. Listar todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Buscar un pedido por ID")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_pedido()
        elif opcion == '2':
            listar_pedidos()
        elif opcion == '3':
            imprimir_hoja_ruta()
        elif opcion == '4':
            buscar_pedido_por_id()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-5).")
    
    print("Gracias por utilizar CleanWasser - Sistema de Gestión de Pedidos.")

if __name__ == "__main__":
    main()
