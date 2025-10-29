def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n=== CALCULADORA SIMPLE ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("========================")

def calculadora():
    """Función principal de la calculadora"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSelecciona una operación (1-5): ")
            
            if opcion == '5':
                print("¡Gracias por usar la calculadora! Hasta luego.")
                break
            
            if opcion not in ['1', '2', '3', '4']:
                print("Opción no válida. Por favor selecciona una opción del 1 al 5.")
                continue
            
            # Solicitar los números
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            # Realizar la operación según la opción seleccionada
            if opcion == '1':
                resultado = sumar(num1, num2)
                operacion = "+"
            elif opcion == '2':
                resultado = restar(num1, num2)
                operacion = "-"
            elif opcion == '3':
                resultado = multiplicar(num1, num2)
                operacion = "*"
            elif opcion == '4':
                resultado = dividir(num1, num2)
                operacion = "/"
            
            # Mostrar el resultado
            if isinstance(resultado, str):
                print(f"\n{resultado}")
            else:
                print(f"\nResultado: {num1} {operacion} {num2} = {resultado}")
        
        except ValueError:
            print("\nError: Por favor ingresa números válidos.")
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido! Hasta luego.")
            break
        except Exception as e:
            print(f"\nOcurrió un error: {e}")

if __name__ == "__main__":
    calculadora()
