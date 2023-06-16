import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import messagebox
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="contabilidad"
)

if conexion.is_connected():
  print("Conexión exitosa a la base de datos")

cursor = conexion.cursor()
consulta = "SELECT * FROM promedios"
cursor.execute(consulta)

for fila in cursor.fetchall():
  print(fila)

conexion.close()


def validar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    if usuario == "1234" and contraseña == "conta":
       messagebox.showinfo("Inicio de sesión exitoso", "¡Bienvenido de nuevo!")
       ventana.destroy()
       
    else:
        messagebox.showerror("Datos incorrectos", "Usuario o contraseña incorrectos")


def mostrar_desarrolladores():
    desarrolladores = [
        "Jonathan Raul Cruz Magaña",
        "Juan Josmar Bacelis de la Rosa",
        "Patricia Beatriz Perez Berdejo"
    ]
    messagebox.showinfo("Desarrolladores", "\n".join([f"{i + 1}. {nombre}" for i, nombre in enumerate(desarrolladores)]))

def mostrar_instrucciones():
    instrucciones = "Este programa está hecho para sacar los promedios contables.\n" \
                    "Por favor, al ingresar, rellena los datos solicitados y disfruta del programa."
    messagebox.showinfo("Instrucciones de usuario", instrucciones)

ventana = Tk()
ventana.title("Inicio de sesión")
ventana.geometry("800x600")
ventana.configure(bg="#f5f5f5")

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

x = int((ancho_pantalla - 800) / 2)
y = int((alto_pantalla - 600) / 2)

ventana.geometry(f"800x600+{x}+{y}")

label_titulo = Label(ventana, text="BIENVENIDO A LA MATERIA DE CONTABILIDAD FINANCIERA", font=("Courier", 18), bg="#f5f5f5")
label_titulo.pack(pady=30)

label_descripcion = Label(ventana, text="Software para sacar promedios contables", font=("Courier", 12), bg="#f5f5f5")
label_descripcion.pack(pady=20)

label_usuario = Label(ventana, text="Usuario:", font=("Courier", 10), bg="#f5f5f5")
label_usuario.pack()

entry_usuario = Entry(ventana, font=("Courier", 10))
entry_usuario.pack(pady=5)

label_contraseña = Label(ventana, text="Contraseña:", font=("Courier", 10), bg="#f5f5f5")
label_contraseña.pack()

entry_contraseña = Entry(ventana, show="*", font=("Courier", 10))
entry_contraseña.pack(pady=5)

btn_ingresar = Button(ventana, text="Ingresar", command=validar_login, font=("Courier", 12), bg="#0078D7", fg="white")
btn_ingresar.pack(pady=10)

btn_desarrolladores = Button(ventana, text="Desarrolladores", command=mostrar_desarrolladores, font=("Courier", 10), bg="#0078D7", fg="white")
btn_desarrolladores.pack(pady=5)

btn_instrucciones = Button(ventana, text="Instrucciones de usuario", command=mostrar_instrucciones, font=("Courier", 10), bg="#0078D7", fg="white")
btn_instrucciones.pack(pady=5)

ventana.mainloop()

class VentanaContable:
    def _init_(self, ventana):
        self.ventana = ventana
        self.ventana.title('Contabilidad')
        self.ventana.geometry('800x600')
        self.ventana.configure(bg='#E0EEE0')

        self.concepto = []
        self.entradas = []
        self.salidas = []
        self.existencias = []
        self.precio_unitario = []
        self.debe = []
        self.haber = []
        self.saldo = []

        self.frame_datos = ttk.Frame(self.ventana, padding=(20, 20))
        self.frame_datos.pack()

        ttk.Label(self.frame_datos, text='Concepto:').grid(row=0, column=0, sticky=tk.E)
        ttk.Label(self.frame_datos, text='Entradas:').grid(row=1, column=0, sticky=tk.E)
        ttk.Label(self.frame_datos, text='Salidas:').grid(row=2, column=0, sticky=tk.E)
        ttk.Label(self.frame_datos, text='Existencias:').grid(row=3, column=0, sticky=tk.E)
        ttk.Label(self.frame_datos, text='Precio Unitario:').grid(row=4, column=0, sticky=tk.E)
        ttk.Label(self.frame_datos, text='Debe:').grid(row=5, column=0, sticky=tk.E)
        ttk.Label(self.frame_datos, text='Haber:').grid(row=6, column=0, sticky=tk.E)

        self.entry_concepto = ttk.Entry(self.frame_datos, width=30)
        self.entry_entradas = ttk.Entry(self.frame_datos, width=30)
        self.entry_salidas = ttk.Entry(self.frame_datos, width=30)
        self.entry_existencias = ttk.Entry(self.frame_datos, width=30)
        self.entry_precio_unitario = ttk.Entry(self.frame_datos, width=30)
        self.entry_debe = ttk.Entry(self.frame_datos, width=30)
        self.entry_haber = ttk.Entry(self.frame_datos, width=30)

        self.entry_concepto.grid(row=0, column=1, padx=10, pady=5)
        self.entry_entradas.grid(row=1, column=1, padx=10, pady=5)
        self.entry_salidas.grid(row=2, column=1, padx=10, pady=5)
        self.entry_existencias.grid(row=3, column=1, padx=10, pady=5)
        self.entry_precio_unitario.grid(row=4, column=1, padx=10, pady=5)
        self.entry_debe.grid(row=5, column=1, padx=10, pady=5)
        self.entry_haber.grid(row=6, column=1, padx=10, pady=5)

        self.boton_agregar = ttk.Button(self.frame_datos, text='Agregar', command=self.agregar_transaccion)
        self.boton_agregar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.frame_tabla = ttk.Frame(self.ventana, padding=(20, 0))
        self.frame_tabla.pack()

        self.treeview = ttk.Treeview(self.frame_tabla, columns=('concepto', 'entradas', 'salidas', 'existencias', 'precio_unitario', 'debe', 'haber', 'saldo'), show='headings', style='Custom.Treeview')
        self.treeview.column('concepto', width=100, anchor=tk.CENTER)
        self.treeview.column('entradas', width=100, anchor=tk.CENTER)
        self.treeview.column('salidas', width=100, anchor=tk.CENTER)
        self.treeview.column('existencias', width=100, anchor=tk.CENTER)
        self.treeview.column('precio_unitario', width=100, anchor=tk.CENTER)
        self.treeview.column('debe', width=100, anchor=tk.CENTER)
        self.treeview.column('haber', width=100, anchor=tk.CENTER)
        self.treeview.column('saldo', width=100, anchor=tk.CENTER)

        self.treeview.heading('concepto', text='Concepto')
        self.treeview.heading('entradas', text='Entradas')
        self.treeview.heading('salidas', text='Salidas')
        self.treeview.heading('existencias', text='Existencias')
        self.treeview.heading('precio_unitario', text='Precio Unitario')
        self.treeview.heading('debe', text='Debe')
        self.treeview.heading('haber', text='Haber')
        self.treeview.heading('saldo', text='Saldo')

        self.treeview.tag_configure('oddrow', background='#F0FFF0')
        self.treeview.tag_configure('evenrow', background='#DCDCDC')

        self.treeview.pack()

        self.boton_eliminar = ttk.Button(self.frame_tabla, text='Eliminar', command=self.eliminar_datos)
        self.boton_eliminar.pack(side=tk.LEFT, padx=10, pady=10)

        self.boton_inventario = ttk.Button(self.frame_tabla, text='Inventario Final', command=self.mostrar_inventario_final)
        self.boton_inventario.pack(side=tk.LEFT, padx=10, pady=10)


    def agregar_transaccion(self):
        concepto = self.entry_concepto.get().strip()
        entradas = self.entry_entradas.get().replace(',', '.').strip()
        salidas = self.entry_salidas.get().replace(',', '.').strip()
        existencias = self.entry_existencias.get().replace(',', '.').strip()
        precio_unitario = self.entry_precio_unitario.get().replace(',', '.').strip()
        debe = self.entry_debe.get().replace(',', '.').strip()
        haber = self.entry_haber.get().replace(',', '.').strip()

        if not concepto or not entradas or not salidas or not existencias or not precio_unitario or not debe or not haber:
            messagebox.showwarning('Campos vacíos', 'Por favor, complete todos los campos.')
            return

        if not self.es_letras(concepto):
            messagebox.showwarning('Formato incorrecto', 'El concepto solo debe contener letras.')
            return

        if not self.es_numero(entradas) or not self.es_numero(salidas) or not self.es_numero(existencias) or not self.es_numero(precio_unitario) or not self.es_numero(debe) or not self.es_numero(haber):
            messagebox.showwarning('Formato incorrecto', 'Los campos numéricos deben contener números válidos.')
            return

        entradas = float(entradas.replace(',', '.'))
        salidas = float(salidas.replace(',', '.'))
        existencias = float(existencias.replace(',', '.'))
        precio_unitario = float(precio_unitario.replace(',', '.'))
        debe = float(debe.replace(',', '.'))
        haber = float(haber.replace(',', '.'))

        saldo_anterior = self.saldo[-1] if self.saldo else 0.0
        saldo_actual = saldo_anterior + debe - haber

        self.concepto.append(concepto)
        self.entradas.append(entradas)
        self.salidas.append(salidas)
        self.existencias.append(existencias)
        self.precio_unitario.append(precio_unitario)
        self.debe.append(debe)
        self.haber.append(haber)
        self.saldo.append(saldo_actual)

        self.entry_concepto.delete(0, tk.END)
        self.entry_entradas.delete(0, tk.END)
        self.entry_salidas.delete(0, tk.END)
        self.entry_existencias.delete(0, tk.END)
        self.entry_precio_unitario.delete(0, tk.END)
        self.entry_debe.delete(0, tk.END)
        self.entry_haber.delete(0, tk.END)

        self.actualizar_tabla()

    def eliminar_datos(self):
        seleccion = self.treeview.selection()
        if not seleccion:
            messagebox.showwarning('Sin selección', 'Seleccione una fila para eliminar.')
            return

        indice = int(self.treeview.item(seleccion)['text']) - 1

        del self.concepto[indice]
        del self.entradas[indice]
        del self.salidas[indice]
        del self.existencias[indice]
        del self.precio_unitario[indice]
        del self.debe[indice]
        del self.haber[indice]
        del self.saldo[indice]

        self.actualizar_tabla()

    def mostrar_inventario_final(self):
        if not self.concepto:
            messagebox.showwarning('Sin datos', 'No hay datos para calcular el inventario final.')
            return

        ventana_inventario = tk.Toplevel(self.ventana)
        ventana_inventario.title('Inventario Final')
        ventana_inventario.geometry('400x200')

        frame_inventario = ttk.Frame(ventana_inventario, padding=(20, 20))
        frame_inventario.pack()

        unidades = self.existencias[-1]
        costo_unitario = self.precio_unitario[-1]
        costo_total = unidades * costo_unitario

        ttk.Label(frame_inventario, text='Unidades:').grid(row=0, column=0, sticky=tk.E)
        ttk.Label(frame_inventario, text='Costo Unitario:').grid(row=1, column=0, sticky=tk.E)
        ttk.Label(frame_inventario, text='Costo Total:').grid(row=2, column=0, sticky=tk.E)

        ttk.Label(frame_inventario, text=unidades).grid(row=0, column=1)
        ttk.Label(frame_inventario, text=costo_unitario).grid(row=1, column=1)
        ttk.Label(frame_inventario, text=costo_total).grid(row=2, column=1)

    def actualizar_tabla(self):
        self.treeview.delete(*self.treeview.get_children())

        for i in range(len(self.concepto)):
            self.treeview.insert('', tk.END, text=i+1, values=(
                self.concepto[i],
                self.entradas[i],
                self.salidas[i],
                self.existencias[i],
                self.precio_unitario[i],
                self.debe[i],
                self.haber[i],
                self.saldo[i]
            ), tags=('oddrow',) if i % 2 != 0 else ('evenrow',))

    def es_letras(texto):
        return texto.isalpha()


    def es_numero(texto):
        try:
            float(texto)
            return True
        except ValueError:
            return False


if _name_ == '_main_':

    ventana_principal = tk.Tk()
    app = VentanaContable(ventana_principal)
    ventana_principal.mainloop()