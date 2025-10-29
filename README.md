# Calculadora Simple con Interfaz Gráfica

Una calculadora de escritorio simple y elegante desarrollada en Python usando la biblioteca tkinter.

## 📋 Descripción

Este proyecto es una calculadora con interfaz gráfica de usuario (GUI) que permite realizar operaciones matemáticas básicas de forma intuitiva mediante una interfaz visual similar a las calculadoras tradicionales.

## ✨ Características

- **Interfaz gráfica moderna**: Diseño colorido y fácil de usar
- **Operaciones básicas**: Suma (+), Resta (-), Multiplicación (*) y División (/)
- **Botones interactivos**: 
  - Números del 0 al 9 (botones azules)
  - Operadores matemáticos (botones naranjas)
  - Botón de cálculo = (botón verde)
  - Botón de limpiar C (botón rojo)
- **Pantalla de visualización**: Muestra la expresión actual y los resultados
- **Manejo de errores**: 
  - Prevención de división por cero
  - Validación de expresiones inválidas
  - Mensajes de error informativos

## 🚀 Requisitos

- Python 3.x
- tkinter (generalmente incluido con Python)

## 📦 Instalación

1. Asegúrate de tener Python 3 instalado en tu sistema:
```bash
python --version
```

2. Clona o descarga este repositorio

3. No se requieren dependencias adicionales, ya que tkinter viene incluido con Python

## 💻 Uso

### Ejecutar la calculadora

Desde la terminal o línea de comandos, ejecuta:

```bash
python main.py
```

### Cómo usar la calculadora

1. **Ingresar números**: Haz clic en los botones numéricos (0-9) para construir tu número
2. **Seleccionar operación**: Haz clic en uno de los operadores (+, -, *, /)
3. **Ingresar segundo número**: Continúa haciendo clic en los números
4. **Calcular resultado**: Presiona el botón "=" para obtener el resultado
5. **Limpiar**: Presiona el botón "C" para borrar la expresión actual y comenzar de nuevo

### Ejemplo de uso

Para calcular `15 + 27`:
1. Click en "1"
2. Click en "5"
3. Click en "+"
4. Click en "2"
5. Click en "7"
6. Click en "="
7. Resultado: 42

## 🏗️ Estructura del Proyecto

```
.
├── main.py          # Archivo principal con la aplicación de la calculadora
└── README.md        # Este archivo
```

## 🔧 Componentes Técnicos

### Clase Principal: `Calculadora`

- **`__init__(self, root)`**: Inicializa la ventana y sus componentes
- **`crear_interfaz()`**: Construye todos los elementos visuales (pantalla y botones)
- **`agregar_a_expresion(valor)`**: Añade números y operadores a la expresión
- **`calcular()`**: Evalúa la expresión matemática y muestra el resultado
- **`limpiar()`**: Reinicia la calculadora borrando la expresión actual

### Características de Diseño

- **Ventana**: 400x500 píxeles, no redimensionable
- **Colores**:
  - Números: Azul (#2196F3)
  - Operadores: Naranja (#FF9800)
  - Igual: Verde (#4CAF50)
  - Limpiar: Rojo (#f44336)
- **Fuente**: Arial, tamaño 18-24pt

## ⚠️ Notas Importantes

- La calculadora utiliza la función `eval()` de Python para evaluar expresiones matemáticas
- Se recomienda usar solo para cálculos básicos
- Los errores de división por cero y expresiones inválidas se manejan con ventanas emergentes

## 🐛 Solución de Problemas

### La calculadora no se abre

- Verifica que tkinter esté instalado correctamente
- En algunos sistemas Linux, puede ser necesario instalar tkinter:
  ```bash
  sudo apt-get install python3-tk
  ```

### Errores al ejecutar

- Asegúrate de estar usando Python 3.x
- Verifica que el archivo `main.py` esté completo y sin errores de sintaxis

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso libre.

## 👨‍💻 Desarrollo

Desarrollado como un proyecto educativo para demostrar el uso de tkinter en Python para crear interfaces gráficas de usuario.

## 🔮 Mejoras Futuras

Posibles mejoras para futuras versiones:
- Soporte para operaciones más avanzadas (potencias, raíces, etc.)
- Historial de cálculos
- Modo científico
- Teclado numérico como entrada
- Temas personalizables
- Soporte para expresiones complejas con paréntesis
