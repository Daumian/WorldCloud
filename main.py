import tkinter as tk
from PIL import Image, ImageTk
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Crear ventana principal
ventana = tk.Tk()
ventana.geometry("300x250")

#Variables:
#Entrada Texto Base
TextoBase = tk.StringVar()
entrada = tk.Entry(ventana, textvariable=TextoBase)
#Palabras Bloqueadas
PalabrasBloqueadas = tk.StringVar()
entrada2 = tk.Entry(ventana, textvariable=PalabrasBloqueadas)


# Crear una función para mostrar la imagen en una ventana secundaria cuando se presiona el botón
def mostrar_imagen():
    # Crear una ventana secundaria
    ventana_secundaria = tk.Toplevel(ventana)
    ventana_secundaria.title("Imagen")
    ventana_secundaria.geometry()
    
    # Cargar la imagen original usando PIL
    imagen = Image.open("image.png")
    
    # Redimensionar la imagen para ajustarla a la ventana secundaria
    max_width = 900  # Ancho máximo deseado para la imagen
    max_height = 800  # Altura máxima deseada para la imagen
    
    # Redimensionar la imagen manteniendo la proporción de aspecto
    imagen.thumbnail((max_width, max_height))
    
    # Convertir la imagen redimensionada a un objeto de tipo PhotoImage de Tkinter
    imagen_tk = ImageTk.PhotoImage(imagen)
    
    # Crear un Label para mostrar la imagen en la ventana secundaria
    etiqueta_imagen = tk.Label(ventana_secundaria, image=imagen_tk)
    etiqueta_imagen.image = imagen_tk  # Mantener una referencia a la imagen para evitar la recolección de basura
    etiqueta_imagen.pack()

# Crear la función para generar la nube de palabras
def generar_wordcloud():
    # Obtener el texto base ingresado por el usuario
    text = TextoBase.get()    
    # Dimensiones de la imagen
    width = 800
    height = 600
    
    # Generar la nube de palabras
    stop_words = set(STOPWORDS)  # Puedes personalizar las palabras bloqueadas aquí
    wordcloud = WordCloud(stopwords=stop_words, background_color="white", width=width, height=height).generate(text)
    
    # Mostrar la nube de palabras
    plt.figure(figsize=(9, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    
    # Guardar la nube de palabras como una imagen
    plt.savefig("image.png", dpi=600)
    mostrar_imagen()

# Titulo
etiqueta_titulo = tk.Label(ventana, text="WordCloud", font=("Arial", 16, "bold"))
# Textos
etiqueta_texto_1 = tk.Label(ventana, text="Ingrese su Texto")
etiqueta_texto_2 = tk.Label(ventana, text="Ingrese Palabras Bloqueadas")

#Botones
#mostarImagen
botonGenerar = tk.Button(ventana, text="Mostrar imagen", command=generar_wordcloud)

#DISEÑO
etiqueta_titulo.pack(pady=10)
etiqueta_texto_1.pack(pady=5)
entrada.pack(pady=5)
etiqueta_texto_2.pack(pady=5)
entrada2.pack(pady=5)
botonGenerar.pack(pady=20)

# Iniciar el bucle principal de la ventana
ventana.mainloop()

