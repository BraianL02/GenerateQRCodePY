from QRcodeV2_functions import *
import tkinter as tk
from tkinter import ttk,messagebox
current_dir = get_dir()

main_window = tk.Tk()
main_window.title("Generar código QR")
main_window.geometry("400x300")
main_window.minsize(350, 250) 
main_window.maxsize(500, 400)
main_window.configure(bg="#3F48CC")


# Titulo
tittle = tk.Label(main_window, text="Conversor a código QR", font=("Arial", 18),background="#3F48CC",fg="white")
tittle.place(relx=0.5, rely=0.10, anchor="center")

# Link or wifi
def hide_entry():
    entry_url.place_forget()
    entry_name.place(relx=0.28, rely=0.31, anchor="center",relwidth=0.35)
    entry_password.place(relx=0.28, rely=0.40, anchor="center",relwidth=0.35)
    combobox_security.place(relx=0.71, rely=0.31, anchor="center",relwidth=0.35)
    combobox_hidden.place(relx=0.71, rely=0.40, anchor="center",relwidth=0.35)

def appear_entry():
    entry_name.place_forget()
    entry_password.place_forget()
    combobox_security.place_forget()
    combobox_hidden.place_forget()
    entry_url.place(relx=0.5, rely=0.35,relwidth=0.6, relheight=0.15, anchor="center")

btn_link = tk.Button(main_window,text="Link",font=("Arial", 10),background="#3F48CC",fg="white", command=appear_entry)
btn_link.place(relx=0.35, rely=0.21, anchor="center")

btn_wifi = tk.Button(main_window,text="Wi-fi",font=("Arial", 10),background="#3F48CC",fg="white",command=hide_entry)
btn_wifi.place(relx=0.65, rely=0.21, anchor="center")



#######################################################################
#                            Entry URL                                #
#######################################################################


def on_focus_in(event):
    if entry_url.get() == "Ingrese la URL aqui":
        entry_url.delete(0, tk.END)
        entry_url.configure(font=("Arial", 14),foreground="black")  # Cambiar color del texto al escribir
def on_focus_out(event):
    if entry_url.get() == "":
        entry_url.insert(0, "Ingrese la URL aqui")
        entry_url.configure(font=("Arial", 10),foreground="gray")  # Regresar el color de placeholder
style = ttk.Style()
style.configure("Custom.TEntry", padding=(15, 0, 0, 0))  # Márgenes (izq, arriba, der, abajo)
# Ingreso url
entry_url = ttk.Entry(main_window, font=("Arial", 10),style="Custom.TEntry",foreground="gray")
entry_url.insert(0, "Ingrese la URL aqui")  # Texto inicial como placeholder
entry_url.bind("<FocusIn>", on_focus_in)  # Evento al enfocar
entry_url.bind("<FocusOut>", on_focus_out)  # Evento al desenfocar
entry_url.place(relx=0.5, rely=0.35,relwidth=0.6, relheight=0.15, anchor="center")


#######################################################################
#                            Entry Data wifi                          #
#######################################################################
'''Entry name & password'''
def focus_in(event):
    event.widget.delete(0, tk.END)  # Borra el contenido del Entry
    event.widget.config(fg="black")  # Cambia el color del texto a negro

def focus_out(event):
    if not event.widget.get():  # Verifica si el Entry está vacío
        event.widget.insert(0, event.widget.default_text)  # Restaura el texto predeterminado
        event.widget.config(fg="gray")  # Cambia el color del texto a gris

def create_entry(parent, default_text):
    entry = tk.Entry(parent, font=("Arial", 10), foreground="gray")
    entry.default_text = default_text
    entry.insert(0, default_text)  # Texto inicial como placeholder
    entry.bind("<FocusIn>", focus_in)  # Evento al enfocar
    entry.bind("<FocusOut>", focus_out)  # Evento al desenfocar     
    
    return entry
entry_name = create_entry(main_window,"Nombre de la red")
entry_password = create_entry(main_window,"Contraseña")
'''Congif wifi'''
# Tipo de seguridad
combobox_security = ttk.Combobox(main_window,values=["WPA","WEP","nopass"], state="readonly")
combobox_security.set("Network type") # Texto inicial
# Hidden
combobox_hidden = ttk.Combobox(main_window,values=["true","false"], state="readonly")
combobox_hidden.set("Red oculta") # Texto inicial
###########################################################################

# Lista de logos
logos = (os.listdir(f"{get_dir()}/Logos/"))
# Creo un combobox
combobox_logo = ttk.Combobox(main_window,values=logos, state="readonly")
combobox_logo.set("Selecciona un logo") # Texto inicial
combobox_logo.place(relx=0.5, rely=0.5, anchor="center")
#Lista de colores
colors = [
    "black", "white","red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "magenta", 
    "brown", "gray", "gold", "lime", "navy", "teal", "maroon",
    "violet", "indigo", "turquoise", "salmon", "coral", "khaki", "plum"
]
colores = [
    "Negro", "Blanco","Rojo", "Verde", "Azul", "Amarillo", "Naranja", "Morado", "Rosa", "Cian", "Magenta",
    "Marrón", "Gris", "Dorado", "Lima", "Azul marino", "Verde azulado", "Granate",
    "Violeta", "Índigo", "Turquesa", "Salmón", "Coral", "Caqui", "Ciruela"
]

# Combobox color principal
primary_color = ttk.Combobox(main_window,values=colors, state="readonly")
primary_color.set("Color principal") # Texto inicial
primary_color.place(relx=0.5, rely=0.6, anchor="center")
# Combobox color secundario
secondary_color = ttk.Combobox(main_window,values=colors, state="readonly")
secondary_color.set("Color secundario") # Texto inicial
secondary_color.place(relx=0.5, rely=0.7, anchor="center")


# Botón Aceptar
def click_accept():
    try:
        # Obtener datos seleccionados de los Combobox
        logo = combobox_logo.get()
        color1 = primary_color.get()
        color2 = secondary_color.get()

        # Validar selección de colores y logo
        if logo == "Selecciona un logo" or color1 == "Color principal" or color2 == "Color secundario":
            messagebox.showwarning("Advertencia", "Asegúrese de seleccionar todas las opciones (logo y colores).")
            return

        # Validar si estamos generando un QR de enlace o Wi-Fi
        if entry_url.winfo_ismapped():  # Si el Entry para la URL está visible
            data = entry_url.get()
            qr_name, valid = verify_link(data)
            if not valid:
                messagebox.showwarning("Advertencia", "El enlace ingresado no es válido.")
                return
        else:  # Si estamos generando un QR de Wi-Fi
            ssid = entry_name.get()
            password = entry_password.get()
            security = combobox_security.get()
            hidden = combobox_hidden.get()

            # Validar campos de Wi-Fi
            if not ssid or ssid == "Nombre de la red":
                messagebox.showwarning("Advertencia", "Ingrese el nombre de la red (SSID).")
                return
            if not password or password == "Contraseña":
                messagebox.showwarning("Advertencia", "Ingrese la contraseña de la red.")
                return
            if security not in ["WPA", "WEP", "nopass"]:
                messagebox.showwarning("Advertencia", "Seleccione un tipo de seguridad válido.")
                return
            if hidden not in ["true", "false"]:
                messagebox.showwarning("Advertencia", "Seleccione si la red es oculta o no.")
                return

            # Generar datos de Wi-Fi
            data = f"WIFI:T:{security};S:{ssid};P:{password};H:{hidden};;"
            qr_name = ssid  # Usar el nombre de la red como nombre del archivo

        # Generar el QR y mostrarlo
        generate_qr(data, current_dir, color1, color2, logo, qr_name)
        show_img(current_dir, qr_name)
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

bttn_accept = tk.Button(main_window, text="Aceptar", command=click_accept)
bttn_accept.place(relx=0.85, rely=0.85, anchor="center")

# Cerrar
button_close = tk.Button(main_window, text="Cerrar", command=main_window.destroy)
button_close.place(relx=0.15, rely=0.85, anchor="center")

main_window.mainloop()
