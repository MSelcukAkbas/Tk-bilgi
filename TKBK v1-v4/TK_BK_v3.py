
#sonuç ekranını kaldırdım onun yerine mesaj kutusu koydum çünkü sonuç ekranı çirkin gözüküyor

import random
import tkinter as tk
from tkinter import ttk, messagebox

pencere = tk.Tk()
pencere.title("Kişi Bilgi Kaydı")
pencere.config(bg="grey")
pencere.geometry("300x400")

kelimeler = ["Harika", "Muhteşem", "Harikulade", "Şahane", "Göz alıcı", "Büyüleyici", "Eşsiz", "Parlak", "Mükemmel"]
rasgele_kelime = random.choice(kelimeler)

# dosyaya yazma fonksiyonu
def kayıt_oluştur():
    isim = isim_giris.get()
    soyisim = soyisim_giris.get()
    işsis = işsiz_combobox.get()
    sehir = il_combobox.get()  
    rasgele_kelime = random.choice(kelimeler)
    isim = isim.capitalize()
    soyisim = soyisim.capitalize()

    sonuç_text = f"{rasgele_kelime} Biri gibisin {isim} {soyisim}\n{işsis} kullanıyorsun demek, güzel\n{sehir} güzel şehirdir"

    messagebox.showinfo("Sonuç", sonuç_text)

    # dosyaya yaz
    with open("kullanici_bilgileri_v3.txt", "a") as dosya:
        dosya.write("\n")
        dosya.write(f"**************************\n")
        dosya.write(f"İsim: {isim}\n")
        dosya.write(f"Soyisim: {soyisim}\n")
        dosya.write(f"İşletim Sistemi: {işsis}\n")
        dosya.write(f"Şehir: {sehir}\n")
        dosya.write(f"**************************\n")
        dosya.write("\n")

# Tüm tuşlar
isim_etiket = tk.Label(pencere, text="İsim:",bg="crimson")
isim_etiket.pack(pady=5)
isim_giris = tk.Entry(pencere)
isim_giris.pack(pady=3)

soyisim_etiket = tk.Label(pencere, text="Soyisim:",bg="crimson")
soyisim_etiket.pack(pady=3)
soyisim_giris = tk.Entry(pencere)
soyisim_giris.pack(pady=3)

işsis_etiket = tk.Label(pencere, text="İşletim Sistemi:" ,bg="crimson")
işsis_etiket.pack(pady=3)
sistemler = ["Windows" ,"macOS" , "Linux" , "Chrome OS", "Android" , "iOS"]

işsiz_combobox = ttk.Combobox(pencere, values=sistemler, state="readonly")
işsiz_combobox.set("Seçiniz...")
işsiz_combobox.current(0)
işsiz_combobox.pack( pady=3)

il_etiket = tk.Label(pencere, text="İl Seçiniz:",bg="crimson")
il_etiket.pack(padx=10 ,pady=3)
şehirler = ["Kastamonu", "İstanbul","Ankara", "İzmir" ,"Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya",  "Antalya", "Artvin", "Aydın", "Balıkesir",
            "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır",
            "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari",
            "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars",
            "Kayseri", "Kırıkkale", "Kırklareli", "Kırşehir", "Kilis", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa",
            "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun",
            "Şanlıurfa", "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van",
            "Yalova", "Yozgat", "Zonguldak"]

il_combobox = ttk.Combobox(pencere, values=şehirler, state="readonly")
il_combobox.set("Seçiniz...")
il_combobox.current(0)
il_combobox.pack( pady=3)

kaydet_düğme = tk.Button(pencere, text="Kayıt Oluştur", command=kayıt_oluştur )
kaydet_düğme.pack( pady=1)

# pencereyi açık tutma
pencere.mainloop()
