# v1 sürümü daha basit bir kod mantığı ile çalışıyor

import random
import tkinter as tk

pencere = tk.Tk()
pencere.title("Kişi Bilgi Kaydı")
pencere.config(bg="white") 
pencere.geometry("300x300")

kelimeler = ["Harika", "Muhteşem", "Harikulade", "Şahane", "Göz alıcı", "Büyüleyici", "Eşsiz", "Parlak", "Mükemmel"]
rasgele_kelime = random.choice(kelimeler)

#dosyaya yazma fonkisyonu
def kayıt_oluştur():
    isim = isim_giris.get()
    soyisim = soyisim_giris.get()
    işsis = işsis_giris.get()
    şehir = şehir_giris.get()

    rasgele_kelime = random.choice(kelimeler)

    sonuc_metni.config(text=f"{rasgele_kelime} Biri gibisin {isim} {soyisim}")
    işsis_metni.config(text=f"{işsis} kullanıyorsun demek, güzel")
    şehir_metni.config(text=f"{şehir} güzel şehirdir")
    with open("kullanici_bilgileri.txt", "a") as dosya:
        dosya.write("\n") 
        dosya.write(f"**************************\n")
        dosya.write(f"İsim: {isim}\n")
        dosya.write(f"Soyisim: {soyisim}\n")
        dosya.write(f"İşletim Sistemi: {işsis}\n")
        dosya.write(f"Şehir: {şehir}\n")
        dosya.write(f"**************************\n")
        dosya.write("\n") 


#tüm tuşlar
isim_etiket = tk.Label(pencere, text="İsim:")
isim_etiket.pack()
isim_giris = tk.Entry(pencere)
isim_giris.pack()
soyisim_etiket = tk.Label(pencere, text="Soyisim:")
soyisim_etiket.pack()
soyisim_giris = tk.Entry(pencere)
soyisim_giris.pack()
işsis_etiket = tk.Label(pencere, text="İşletim Sistemi:")
işsis_etiket.pack()
işsis_giris = tk.Entry(pencere)
işsis_giris.pack()
şehir_etiket = tk.Label(pencere, text="Şehir:")
şehir_etiket.pack()
şehir_giris = tk.Entry(pencere)
şehir_giris.pack()
kaydet_düğme = tk.Button(pencere, text="Kayıt Oluştur", command=kayıt_oluştur)
kaydet_düğme.pack()
sonuc_metni = tk.Label(pencere, text="", font=("Helvetica", 12))
sonuc_metni.pack()
işsis_metni = tk.Label(pencere, text="", font=("Helvetica", 12))
işsis_metni.pack()
şehir_metni = tk.Label(pencere, text="", font=("Helvetica", 12))
şehir_metni.pack()

#pencereyi açık tutma 
pencere.mainloop()




