# from tkinter import *
# from tkinter.font import Font

# # creando ventana de GUI
# root = Tk()				
# root.title('LED ON-OFF with Python')
# root.geometry("400x350")
# root.configure(background="LightSteelBlue3")		

# flag = 1		# auxiliar para el boton


# ---------------------------------------------------------------------------
# # construccion de la ventana de GUI

# myLabel3 = Label(root,text="Presione el botón para Encender o Apagar el LED:",bg="LightSteelBlue3")
# myLabel3.pack(padx=15,pady=20)

# myButton2 = Button(root, text="LED OFF",width=10,bg='red')
# myButton2.pack(padx=20,pady=20)

# myLabel = Label(root,text="Inserte puerto:", bg="LightSteelBlue3")
# myLabel.pack(padx=10,pady=20)

# portCom = Entry(root,width=12)
# portCom.pack(padx=12,pady=15)

# portC = portCom.get()		# se obtiene el puerto al que se quiere conectar

# myLabel2 = Label(root,text="Desconectado", bg="LightSteelBlue3")
# myLabel2.pack(padx=10,pady=10)

# myButton1 = Button(root, text="Conectar",width=9)
# myButton1.pack(padx=10,pady=10)

# root.mainloop()


#def clicked():

   #messagebox.showinfo('Message title', 'Message content')


from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
import json

# ---------------------------------------------------------------------------
with open('productos.json') as json_file:
	data = json.load(json_file)
# ---------------------------------------------------------------------------

def write_json(data, filename='productos.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4)
# ---------------------------------------------------------------------------

window = Tk()

window.title("Actualizador de Productos")

window.geometry('1000x600')

file_path= ""

# ---------------------------------------------------------------------------
lbl1 = Label(window, text="ID")
lbl1.grid(column=0, row=0)
txt1 = Entry(window,width=40)
txt1.grid(column=1, row=0)
#txt1.insert(0, int(data[len(data)-1]['ID'])+1)

lbl2 = Label(window, text="Tipo")
lbl2.grid(column=0, row=1)
txt2 = Entry(window,width=40)
txt2.grid(column=1, row=1)
txt2.insert(0, "simple")

lbl3 = Label(window, text="SKU")
lbl3.grid(column=0, row=2)
txt3 = Entry(window,width=40)
txt3.grid(column=1, row=2)

lbl4 = Label(window, text="Nombre")
lbl4.grid(column=0, row=3)
txt4 = Entry(window,width=40)
txt4.grid(column=1, row=3)

lbl5 = Label(window, text="Publicado")
lbl5.grid(column=0, row=4)
txt5 = Entry(window,width=40)
txt5.grid(column=1, row=4)
txt5.insert(0, 1)

lbl50 = Label(window, text="¿Está destacado?")
lbl50.grid(column=0, row=5)
txt50 = Entry(window,width=40)
txt50.grid(column=1, row=5)
txt50.insert(0, 0)

lbl6 = Label(window, text="Visibilidad en el catálogo")
lbl6.grid(column=0, row=6)
txt6 = Entry(window,width=40)
txt6.grid(column=1, row=6)
txt6.insert(0, "visible")

lbl7 = Label(window, text="Descripción corta")
lbl7.grid(column=0, row=7)
txt7 = Entry(window,width=40)
txt7.grid(column=1, row=7)

lbl8 = Label(window, text="Descripción")
lbl8.grid(column=0, row=8)
txt8 = Entry(window,width=40)
txt8.grid(column=1, row=8)

lbl9 = Label(window, text="Día en que empieza el precio rebajado")
lbl9.grid(column=0, row=9)
txt9 = Entry(window,width=40)
txt9.grid(column=1, row=9)

lbl10 = Label(window, text="Día en que termina el precio rebajado")
lbl10.grid(column=0, row=10)
txt10 = Entry(window,width=40)
txt10.grid(column=1, row=10)

lbl11 = Label(window, text="Estado del impuesto")
lbl11.grid(column=0, row=11)
txt11 = Entry(window,width=40)
txt11.grid(column=1, row=11)
txt11.insert(0, "taxable")

lbl12 = Label(window, text="Clase de impuesto")
lbl12.grid(column=0, row=12)
txt12 = Entry(window,width=40)
txt12.grid(column=1, row=12)
txt12.insert(0, "comision")

lbl13 = Label(window, text="¿En inventario?")
lbl13.grid(column=0, row=13)
txt13 = Entry(window,width=40)
txt13.grid(column=1, row=13)
txt13.insert(0, 1)

lbl14 = Label(window, text="Cantidad de bajo inventario")
lbl14.grid(column=0, row=14)
txt14 = Entry(window,width=40)
txt14.grid(column=1, row=14)

lbl15 = Label(window, text="¿Permitir reservas de productos agotados?")
lbl15.grid(column=0, row=15)
txt15 = Entry(window,width=40)
txt15.grid(column=1, row=15)
txt15.insert(0, 1)

lbl16 = Label(window, text="¿Vendido individualmente?")
lbl16.grid(column=0, row=16)
txt16 = Entry(window,width=40)
txt16.grid(column=1, row=16)
txt16.insert(0, 0)

lbl17 = Label(window, text="Peso (lbs)")
lbl17.grid(column=0, row=17)
txt17 = Entry(window,width=40)
txt17.grid(column=1, row=17)

lbl18 = Label(window, text="Longitud (in)")
lbl18.grid(column=0, row=18)
txt18 = Entry(window,width=40)
txt18.grid(column=1, row=18)

lbl19 = Label(window, text="Anchura (in)")
lbl19.grid(column=0, row=19)
txt19 = Entry(window,width=40)
txt19.grid(column=1, row=19)

lbl20 = Label(window, text="Altura (in)")
lbl20.grid(column=0, row=20)
txt20 = Entry(window,width=40)
txt20.grid(column=1, row=20)

lbl21 = Label(window, text="¿Permitir valoraciones de clientes?")
lbl21.grid(column=0, row=21)
txt21 = Entry(window,width=40)
txt21.grid(column=1, row=21)
txt21.insert(0, 1)

lbl22 = Label(window, text="Nota de compra")
lbl22.grid(column=0, row=22)
txt22 = Entry(window,width=40)
txt22.grid(column=1, row=22)

lbl23 = Label(window, text="Precio rebajado")
lbl23.grid(column=0, row=23)
txt23 = Entry(window,width=40)
txt23.grid(column=1, row=23)

lbl24 = Label(window, text="Precio normal")
lbl24.grid(column=0, row=24)
txt24 = Entry(window,width=40)
txt24.grid(column=1, row=24)

lbl25 = Label(window, text="Categorías")
lbl25.grid(column=0, row=25)
txt25 = Entry(window,width=40)
txt25.grid(column=1, row=25)
# ----------------------------------------------------------------------------------------
lbl26 = Label(window, text="Etiquetas")
lbl26.grid(column=3, row=0)
txt26 = Entry(window,width=40)
txt26.grid(column=4, row=0)

lbl27 = Label(window, text="Clase de envío")
lbl27.grid(column=3, row=1)
txt27 = Entry(window,width=40)
txt27.grid(column=4, row=1)

lbl28 = Label(window, text="Imágenes")
lbl28.grid(column=3, row=2)
txt28 = Entry(window,width=40)
txt28.grid(column=4, row=2)

lbl29 = Label(window, text="Límite de descargas")
lbl29.grid(column=3, row=3)
txt29 = Entry(window,width=40)
txt29.grid(column=4, row=3)

lbl30 = Label(window, text="Días de caducidad de la descarga")
lbl30.grid(column=3, row=4)
txt30 = Entry(window,width=40)
txt30.grid(column=4, row=4)

lbl31 = Label(window, text="Superior")
lbl31.grid(column=3, row=5)
txt31 = Entry(window,width=40)
txt31.grid(column=4, row=5)

lbl32 = Label(window, text="Productos agrupados")
lbl32.grid(column=3, row=6)
txt32 = Entry(window,width=40)
txt32.grid(column=4, row=6)

lbl33 = Label(window, text="Ventas dirigidas")
lbl33.grid(column=3, row=7)
txt33 = Entry(window,width=40)
txt33.grid(column=4, row=7)

lbl34 = Label(window, text="Ventas cruzadas")
lbl34.grid(column=3, row=8)
txt34 = Entry(window,width=40)
txt34.grid(column=4, row=8)

lbl35 = Label(window, text="URL externa")
lbl35.grid(column=3, row=9)
txt35 = Entry(window,width=40)
txt35.grid(column=4, row=9)

lbl36 = Label(window, text="Texto del botón")
lbl36.grid(column=3, row=10)
txt36 = Entry(window,width=40)
txt36.grid(column=4, row=10)

lbl37 = Label(window, text="Posición")
lbl37.grid(column=3, row=11)
txt37 = Entry(window,width=40)
txt37.grid(column=4, row=11)
txt37.insert(0, 0)

lbl38 = Label(window, text="Minimum Quantity")
lbl38.grid(column=3, row=12)
txt38 = Entry(window,width=40)
txt38.grid(column=4, row=12)

lbl39 = Label(window, text="Maximum Quantity")
lbl39.grid(column=3, row=13)
txt39 = Entry(window,width=40)
txt39.grid(column=4, row=13)

lbl40 = Label(window, text="Swatches Attributes")
lbl40.grid(column=3, row=14)
txt40 = Entry(window,width=40)
txt40.grid(column=4, row=14)

lbl41 = Label(window, text="Nombre del atributo 1")
lbl41.grid(column=3, row=15)
txt41 = Entry(window,width=40)
txt41.grid(column=4, row=15)

lbl42 = Label(window, text="Valor(es) del atributo 1")
lbl42.grid(column=3, row=16)
txt42 = Entry(window,width=40)
txt42.grid(column=4, row=16)

lbl43 = Label(window, text="Atributo visible 1")
lbl43.grid(column=3, row=17)
txt43 = Entry(window,width=40)
txt43.grid(column=4, row=17)

lbl44 = Label(window, text="Atributo global 1")
lbl44.grid(column=3, row=18)
txt44 = Entry(window,width=40)
txt44.grid(column=4, row=18)

lbl45 = Label(window, text="Meta: min_quantity")
lbl45.grid(column=3, row=19)
txt45 = Entry(window,width=40)
txt45.grid(column=4, row=19)

lbl46 = Label(window, text="Meta: max_quantity")
lbl46.grid(column=3, row=20)
txt46 = Entry(window,width=40)
txt46.grid(column=4, row=20)

lbl47 = Label(window, text="Meta: linked_attribute")
lbl47.grid(column=3, row=20)
txt47 = Entry(window,width=40)
txt47.grid(column=4, row=20)

lbl48 = Label(window, text="Meta: min_quantity_var")
lbl48.grid(column=3, row=21)
txt48 = Entry(window,width=40)
txt48.grid(column=4, row=21)

lbl49 = Label(window, text="Meta: max_quantity_var")
lbl49.grid(column=3, row=22)
txt49 = Entry(window,width=40)
txt49.grid(column=4, row=22)

#----------------------------------------------------------------------------


def null_arg(arg):
	try:
		int(arg)
	except:
		return arg
	return int(arg)

def imagen():
	global file_path
	file_path_aux=filedialog.askopenfilename()
	file_path = file_path+','+file_path_aux.replace('C:/Users/IBAUTISTA/Desktop/MARIEDVA/Encuentralo en U/','https://encuentraloenusa.com/ftp_images/')
	print(file_path)


# ---------------------------------------------------------------------------
def update():
	global file_path
	res1 = txt1.get()												#	1
	txt1.delete(first=0, last=10)
	res2 = txt2.get()												#	2
	res3 = txt3.get()												#	3
	res4 = txt4.get()												#	4
	res5 = txt5.get()												#	5
	res6 = txt6.get()												#	6
	res7 = txt7.get()												#	7
	res8 = txt8.get()												#	8
	res9 = txt9.get()												#	9

	res10 = txt10.get()												#	10
	res11 = txt11.get()												#	11
	res12 = txt12.get()												#	12
	res13 = txt13.get()												#	13
	res14 = txt14.get()												#	14
	res15 = txt15.get()												#	15
	res16 = txt16.get()												#	16
	res17 = txt17.get()												#	17
	res18 = txt18.get()												#	18
	res19 = txt19.get()												#	19

	res20 = txt20.get()												#	20
	res21 = txt21.get()												#	21
	res22 = txt22.get()												#	22
	res23 = txt23.get()												#	23
	res24 = txt24.get()												#	24
	res25 = txt25.get()												#	25
#---------------------------------------------
	res26 = txt26.get()												#	26
	res27 = txt27.get()												#	27
	res28 = file_path#txt28.get() 												#	28
	res29 = txt29.get()												#	29

	res30 = txt30.get()												#	30
	res31 = txt31.get()												#	31
	res32 = txt32.get()												#	32
	res33 = txt33.get()												#	33
	res34 = txt34.get()												#	34
	res35 = txt35.get()												#	35
	res36 = txt36.get()												#	36
	res37 = txt37.get()												#	37
	res38 = txt38.get()												#	38
	res39 = txt39.get()												#	39

	res40 = txt40.get()												#	40
	res41 = txt41.get()												#	41
	res42 = txt42.get()												#	42
	res43 = txt43.get()												#	43
	res44 = txt44.get()												#	44
	res45 = txt45.get()												#	45
	res46 = txt46.get()												#	46
	res47 = txt47.get()												#	47
	res48 = txt48.get()												#	48
	res49 = txt49.get()												#	49
	res50 = txt50.get()												#	50
									#	51


	#prod=data['productos']

	updt= {
			#"ID": null_arg(res1),												#	1																	 
	        "Tipo": res2,													#	2				
	        "SKU": res3,													#	3					
	        "Nombre": res4,												#		4
	        "Publicado": null_arg(int(res5)),												#	5	
	        "Is featured?": null_arg(res50),												#	6	
	        "Visibility in catalog": res6,													#	7
	        "Short description": res7,												#	8
	        "Description": res8,												#	9
	        "Date sale price starts": res9,												#	10
	        "Date sale price ends": res10,												#	11
	        "Estado del impuesto": res11,												#	12
	        "Clase de impuesto": res12,												#	13
	        "In stock?": null_arg(res13),												#	14
	        "Inventario": res14,												#	15
	        "Cantidad de bajo inventario": res14,												#	16
	        "Backorders allowed?": null_arg(res15),												#	17
	        "Sold individually?": null_arg(res16),												#	18
	        "Peso (lbs)": null_arg(res17),												#	19
	        "Longitud (in)": null_arg(res18),												#	20
	        "Anchura (in)": null_arg(res19),												#	21
	        "Altura (in)": null_arg(res20),												#	22
	        "Allow customer reviews?": null_arg(res21),												#	23
	        "Nota de compra": res22,												#	24
	        "Precio rebajado": res23,												#	25
	        "Precio normal": float(res24),												#	26
	        "Categories": res25,												#	27
	        "Etiquetas": res26,												#	28
	        "Shipping class": res27,												#	29
	        "Images": res28,												#	30
	        "Download limit": res29,												#	31
	        "Download expiry days": res30,												#	32
	        "Superior": res31,												#	33
	        "Productos agrupados": res32,												#	34
	        "Ventas dirigidas": res33,												#	35
	        "Ventas cruzadas": res34,												#	36
	        "URL externa": res35,												#	37
	        "Button text": res36,												#	38
	        "Position": null_arg(res37),												#	39
	        "Minimum Quantity": res38,												#	40
	        "Maximum Quantity": res39,												#	41
	        "Swatches Attributes": res40,												#	42
	        "Nombre del atributo 1": res41,												#	43
	        "Valor(es) del atributo 1": res42,												#	44
	        "Atributo visible 1": res43,												#	45
	        "Atributo global 1": res44,												#	46
	        "Meta: min_quantity": res45,												#	47
	        "Meta: max_quantity": res46,												#	48
	        "Meta: linked_attribute": res47,												#	49
	        "Meta: min_quantity_var": res48,												#	50
	        "Meta: max_quantity_var": res49												#	51
			}
	#prod.append(updt)
	data.append(updt)
	write_json(data)

	# txt3.delete(first=0, last=100)
	# txt4.delete(first=0, last=100)
	# txt5.delete(first=0, last=100)
	# txt8.delete(first=0, last=100)
	# txt9.delete(first=0, last=100)
	# txt10.delete(first=0, last=100)
	# txt11.delete(first=0, last=100)
	# txt15.delete(first=0, last=100)
	# txt18.delete(first=0, last=100)
	# txt19.delete(first=0, last=100)
	# txt20.delete(first=0, last=100)
	# txt21.delete(first=0, last=100)
	# txt23.delete(first=0, last=100)
	# txt24.delete(first=0, last=100)
	# txt25.delete(first=0, last=100)
	# txt26.delete(first=0, last=100)
	
	# txt27.delete(first=0, last=100)
	# txt28.delete(first=0, last=100)
	# txt29.delete(first=0, last=100)
	# txt30.delete(first=0, last=100)
	# txt31.delete(first=0, last=100)
	# txt32.delete(first=0, last=100)
	# txt33.delete(first=0, last=100)
	# txt34.delete(first=0, last=100)
	# txt35.delete(first=0, last=100)
	# txt36.delete(first=0, last=100)
	# txt37.delete(first=0, last=100)

	
	# txt39.delete(first=0, last=100)
	# txt40.delete(first=0, last=100)
	# txt41.delete(first=0, last=100)
	# txt42.delete(first=0, last=100)
	# txt43.delete(first=0, last=100)
	# txt44.delete(first=0, last=100)
	# txt45.delete(first=0, last=100)
	# txt46.delete(first=0, last=100)
	# txt47.delete(first=0, last=100)
	# txt48.delete(first=0, last=100)
	# txt49.delete(first=0, last=100)
	file_path = ''
	#txt1.insert(0, int(data[len(data)-1]['ID'])+1)

# # ---------------------------------------------------------------------------
btn = Button(window, text="Actualizar",command = update)
#btn.pack(padx=10,pady=10)
btn2 = Button(window, text="Imagen",command = imagen)

btn2.grid(column=4)

btn.grid(column=1)

window.mainloop()