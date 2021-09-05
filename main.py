import datetime
from tkinter import *
from tkinter import messagebox
from pytube import YouTube


# -------------------------------- Funciones ----------------------------------
def download_mp3():
    link = input_link.get()
    try:

        is_download = YouTube(link).streams.filter(only_audio=True).first().download("Path/descargas")
        if is_download:
            yt = YouTube(link)
            with open("PATH/archivo.txt", mode="a") as f:
                f.write(f"Titulo: {yt.streams[0].title} |  Fecha de descarga: {datetime.datetime.now()}\n")
                messagebox.showinfo("Informacion de descarga", message="Su video se convirtió y descargó exitosamente")
    except:
        print("Se produjo un error")


# ----------------------------- Interface --------------------------------------
if __name__ == '__main__':
    window = Tk()
    window.title("Youtube To Mp3 With Python")
    window.config(padx=50, pady=50)
    window.geometry("750x200")

    # inputs
    input_link = Entry(width=35, highlightbackground="black", font=("Oxygen", 14, "bold"))
    input_link.place(y=100)

    # Buttons
    btn_download = Button(text="Descargar", width=20, bg="green", fg="white", font=("Oxygen", 11, "bold"),
                          command=download_mp3)
    btn_download.place(x=450, y=97)

    # Labels
    lb_title = Label(text="Convierte tu musica favorita a mp3", font=("Oxygen", 30, "bold"))
    lb_title.grid(row=0, column=0, columnspan=2)

    window.mainloop()
