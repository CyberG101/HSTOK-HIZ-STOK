from tkinter import Tk, Label, Entry, Button, Toplevel, messagebox

# Global liste stokları saklamak için
stoklar = []

# Dosya yolu
dosya_yolu = "stoklar.txt"

def stok_koy():
    # Entry widget'ından veri alma
    stok = entry.get()
    if stok:
        stoklar.append(stok)  # Listeye ekleme
        entry.delete(0, 'end')  # Entry widget'ını temizleme
        print(f"'{stok}' stoklara eklendi.")
        verileri_sakla()  # Stokları dosyaya kaydet
    else:
        print("Lütfen bir stok girin.")

def stok_kaldir():
    # Entry widget'ından veri alma
    stok = entry.get()
    if stok in stoklar:
        stoklar.remove(stok)  # Listeden stok kaldırma
        print(f"'{stok}' stoklardan kaldırıldı.")
        verileri_sakla()  # Stokları dosyaya kaydet
        entry.delete(0, 'end')  # Entry widget'ını temizleme
    else:
        # Stok bulunamazsa uyarı mesajı
        messagebox.showwarning("Uyarı", "Stok bulunamadı!")

def stok_goster():
    # Stokları göstermek için yeni pencere oluşturma
    stoklar_penceresi = Toplevel(root)
    stoklar_penceresi.title("Stoklar")
    
    # Stokları liste olarak gösterme
    stok_metni = "\n".join(stoklar)
    stok_label = Label(stoklar_penceresi, text=stok_metni)
    stok_label.pack(pady=10)

def cikis_yap():
    root.destroy()  # Programdan çıkış yapar

def verileri_yukle():
    """Dosyadan stokları yükler."""
    global stoklar
    try:
        with open(dosya_yolu, "r") as dosya:
            stoklar = dosya.read().splitlines()
    except FileNotFoundError:
        stoklar = []  # Dosya yoksa boş liste

def verileri_sakla():
    """Stokları dosyaya kaydeder."""
    with open(dosya_yolu, "w") as dosya:
        for stok in stoklar:
            dosya.write(stok + "\n")

# Ana pencereyi oluşturma
root = Tk()
root.title("Stok Yönetimi")
root.geometry("400x300")
root.configure(bg="red")

# Yapımcı yazısını oluşturma
yapimci_label = Label(root, text="By GNova Team", fg="blue", bg="red")
yapimci_label.pack()

# Entry widget'ı
entry = Entry(root, width=20)
entry.place(relx=0.5, rely=0.3, anchor='center')
entry.insert(0, "Buraya tıklayın ve yazın")  # Yer tutucu metni ekleme

# Butonları oluşturma ve işlev ekleme
stok_koy_button = Button(root, text="Stok Koy", command=stok_koy)
stok_koy_button.place(relx=0.5, rely=0.5, anchor='center')

stok_kaldir_button = Button(root, text="Stok Kaldır", command=stok_kaldir)
stok_kaldir_button.place(relx=0.5, rely=0.6, anchor='center')

stok_goster_button = Button(root, text="Stokları Göster", command=stok_goster)
stok_goster_button.place(relx=0.5, rely=0.7, anchor='center')

# Çıkış butonunu oluşturma ve işlev ekleme
cikis_button = Button(root, text="Çıkış", command=cikis_yap)
cikis_button.place(relx=0.5, rely=0.8, anchor='center')

# Versiyon bilgisini gösteren label
versiyon_label = Label(root, text="Versiyon 1.0", bg="red", fg="white")
versiyon_label.place(relx=1.0, rely=1.0, anchor='se')

# Uygulama başladığında verileri yükle
verileri_yukle()

# Pencereyi çalıştırma
root.mainloop()
