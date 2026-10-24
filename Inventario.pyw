from tkinter import *

tallas = []
conttalla = {}

ventana = Tk()
ventana.title("INVENTARIO")
ventana.geometry("500x400")
ventana.iconbitmap("Inventario.ico")
ventana.resizable(0, 0)

texto = Label(ventana, text="INVENTARIO DE BOTAS", bg="gray", width=40, font=("Comic Sans MS", 16, "bold"))
texto.place(x=-6, y=0)

principal = Frame(ventana, bg="brown", width=500, height=372)
principal.place(x=0, y=29)

bota = Spinbox(principal, from_=1, to=70)
bota.place(x=180, y=52)

cuenta = Label(principal, text="Talla del par de botas:", bg="brown", font=("Arial", 12, "bold"))
cuenta.place(x=0, y=50)


def subir():
	try:
		talla = int(bota.get())
		print(f"La talla {talla} aparece {tallas.count(talla) + 1} vez/veces")
		tallas.append(talla)

		if talla in conttalla:
			conttalla[talla] += 1
		else:
			conttalla[talla] = 1	

	except ValueError:
		print("No se permite texto")

def salir():
	print(tallas)
	ventana = Toplevel()
	ventana.title("Datos")
	ventana.geometry("500x400")
	ventana.iconbitmap("Inventario.ico")
	ventana.resizable(0, 0)

	cabeza1 = Label(ventana, text="TALLA DEL PAR", width=20)
	cabeza1.grid(row=0, column=0)

	cabeza2 = Label(ventana, text="CANTIDAD", width=15)
	cabeza2.grid(row=0, column=1)

	for fila, (talla, cantidad) in enumerate(conttalla.items(), start=1):
		Label(ventana, text=talla, width=20).grid(row=fila, column=0)
		Label(ventana, text=cantidad, width=15).grid(row=fila, column=1)


continuar = Button(principal, text="Aceptar", bg="yellow", activebackground="brown", width=60, command=subir)
continuar.place(x=40, y=120)

terminar = Button(principal, text="Terminar", bg="yellow", activebackground="brown", width=60, command=salir)
terminar.place(x=40, y=160)



ventana.mainloop()