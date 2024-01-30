# v1 sürümü daha basit bir kod mantığı ile çalışıyor
# v2 bu güncellemeden seçim kutusu(combobox) getirdim ; il ve işletim sistemini listeden alıyoruz
# v3 sonuç ekranını kaldırdım onun yerine mesaj kutusu koydum çünkü sonuç ekranı çirkin gözüküyor
# v4 renk ve boyutlar üzerinde düzeltmeler yapıldı , combobox rengi değiştirme şuanlık çalışmıyor 
        # birden fazla pack yerine tek pack atıyoruz
        # frame ile düzeni geliştiriyoruz
# TKBK_NewGen v4.01 de arayüze şifre uygulaması eklenmiş hatalı şifre giriminde pencereleri kapatması sağlanmıştır

import random
import time
import tkinter as tk
from tkinter import ttk, messagebox


def giris_yap():
    pencere = tk.Tk()
    pencere.title("Kişi Bilgi Kaydı")
    pencere.config(bg="white")
    pencere.geometry("400x450+200+100")

    kelimeler = ["Harika", "Muhteşem", "Harikulade", "Şahane", "Göz alıcı", "Büyüleyici", "Eşsiz", "Parlak", "Mükemmel"]
    rasgele_kelime = random.choice(kelimeler)

    etiket_bg_rengi = "#dedcdc" # açık gri
    entry_bg_rengi = "#d4c5c5"  # crimson renginin açık hali 
    #combobox_bg_rengi = "#f2224c" hatalı
    bg_rengi = "white"
    font_stil = ("Helvetica",12, "bold") #ortak font

    def dosyaya_yaz(isim, soyisim, işsis, sehir):
        with open("kullanici_bilgileri_v4.txt", "a") as dosya:
            dosya.write("\n")
            dosya.write(f"**************************\n")
            dosya.write(f"İsim: {isim}\n")
            dosya.write(f"Soyisim: {soyisim}\n")
            dosya.write(f"İşletim Sistemi: {işsis}\n")
            dosya.write(f"Şehir: {sehir}\n")
            dosya.write(f"**************************\n")
            dosya.write("\n")

    def kayıt_oluştur():
        isim = isim_giris.get()
        soyisim = soyisim_giris.get()
        işsis = işsiz_combobox.get()
        sehir = il_combobox.get()
        
        if not isim or not soyisim or işsis == "Seçiniz..." or sehir == "Seçiniz...":
            messagebox.showerror("Hata", "Lütfen tüm bilgileri eksiksiz girin.")
            return

        rasgele_kelime = random.choice(kelimeler)
        isim = isim.capitalize()
        soyisim = soyisim.capitalize()

        sonuç_text = f"{rasgele_kelime} Biri gibisin {isim} {soyisim}\n{işsis} kullanıyorsun demek, güzel\n{sehir} güzel şehirdir"
        messagebox.showinfo("Sonuç", sonuç_text)

        dosyaya_yaz(isim, soyisim, işsis, sehir)

    multi_pack = tk.Frame(pencere, bg=bg_rengi)

    # Etiket ve giriş alanlarını büyüt
    isim_etiket = tk.Label(multi_pack, text="İsim:",  font=font_stil ,bg=etiket_bg_rengi)
    isim_etiket.pack(pady=10)
    isim_giris = tk.Entry(multi_pack, font=font_stil  ,bg=entry_bg_rengi) 
    isim_giris.pack(pady=5)

    soyisim_etiket = tk.Label(multi_pack, text="Soyisim:", font=font_stil , bg=etiket_bg_rengi)
    soyisim_etiket.pack(pady=5)
    soyisim_giris = tk.Entry(multi_pack, font=font_stil ,bg=entry_bg_rengi)
    soyisim_giris.pack(pady=5)

    işsis_etiket = tk.Label(multi_pack, text="İşletim Sistemi:", font=font_stil ,bg=etiket_bg_rengi)
    işsis_etiket.pack(pady=5)        # Combobox listesi aşğıda
    sistemler = ["Windows", "macOS", "Linux", "Chrome OS", "Android", "iOS"]

    işsiz_combobox = ttk.Combobox(multi_pack, values=sistemler, state="readonly", font=font_stil  )
    işsiz_combobox.set("Seçiniz..." )
    işsiz_combobox.current(0)   #seçim yapılmadan önce 0. seçenek seçili gelir
    işsiz_combobox.pack(pady=5)

    il_etiket = tk.Label(multi_pack, text="İl Seçiniz:", font=font_stil ,bg=etiket_bg_rengi)
    il_etiket.pack(padx=10, pady=5)           # Combobox listesi aşğıda
    şehirler = ["Kastamonu", "İstanbul", "Ankara", "İzmir", "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Antalya", "Artvin", "Aydın", "Balıkesir",
                "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır",
                "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari",
                "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars",
                "Kayseri", "Kırıkkale", "Kırklareli", "Kırşehir", "Kilis", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa",
                "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun",
                "Şanlıurfa", "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van",
                "Yalova", "Yozgat", "Zonguldak"]

    il_combobox = ttk.Combobox(multi_pack, values=şehirler, state="readonly", font=font_stil  ) 
    il_combobox.set("Seçiniz...")
    il_combobox.current(0)      #seçim yapılmadan önce 0. seçenek seçili gelir
    il_combobox.pack(pady=5)

    kaydet_düğme = tk.Button(multi_pack, text="Kayıt Oluştur", command=kayıt_oluştur, font=font_stil )
    kaydet_düğme.pack(pady=5 ) 

    multi_pack.pack()
    pencere.mainloop()


şifre = tk.Tk()
şifre.title("Kilit Ekranı")
şifre.geometry("400x180+200+100")
şifre.config(bg="white")
şifre.resizable(False,False)

parola=tk.Entry(şifre,show='****************************')
parola.pack(pady=5, fill=tk.X  ,padx=5) 

parolatiket=tk.Label(şifre,text="Parolanızı giriniz" )
parolatiket.pack( pady=5 ,padx=5) 

def doğrulama():
    if parola.get() == "1234" :
        şifre.destroy()
        giris_yap() 
        time.sleep(0.5)
        
    else:
        time.sleep(0.1)
        şifre.destroy()

parolasalama=tk.Button(şifre,text="Giriş Yap",command=lambda:doğrulama())
parolasalama.pack(expand=True,fill=tk.BOTH ,pady=5 ,padx=5) 

şifre.mainloop()   

