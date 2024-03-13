#####
from time import sleep
from tkinter import BOTH, END, X, BooleanVar, Button, Checkbutton, Entry, Frame, Label, Menu, Tk, ttk, messagebox, scrolledtext 
from pathlib import Path
from TEK_Pack.tek_pack_v2 import  güncellemeler , dersler

# Ana dizin ve dosya yolu tanımları daha kısa hale getirildi.
local_path = Path.home() / 'AppData' / 'Local' / 'TK-BİLGİ'
local_path.mkdir(parents=True, exist_ok=True)
kayit_klasoru = local_path / 'kullanici_bilgileri.txt'

# Renk ve font tanımları bir kez yapıldı.
giris_kutusu_rengi = "lavender"
etiket_rengi = "white"
arka_plan_rengi = "steelblue"
font_stil = ("Helvetica", 12, "bold")
font_family, font_size, font_weight = font_stil
yeni_boyut = int(font_size * 0.8)

# Kullanıcı bilgilerini almak için fonksiyon tanımlaması kısaltıldı.
def kullanici_bilgileri():
    return str(Path("~").expanduser())[9:].capitalize()

######
def sifre_kontrol(giris_yap_fonskiyonu):
    def dogrulama():
        nonlocal denemehakki
        if parola.get() == "1234":
            messagebox.showinfo("GİRİŞ!", "GİRİŞ YAPILIYOR....")
            sleep(0.1)
            sifre.destroy()
            sleep(1)
            giris_yap_fonskiyonu()
        else:
            denemehakki -= 1
            messagebox.showerror("HATA!", f"PAROLAYI HATALI GİRDİNİZ.\nDENEME HAKKI: {denemehakki} KALDI.")
            sleep(0.5)
            if denemehakki == 0:
                messagebox.showerror(f"HATA!", "PROGRAM KAPATILIYOR...")
                sleep(0.5)
                sifre.destroy()
    sifre = Tk()
    sifre.title("Kilit Ekranı")
    sifre.geometry("400x180+200+100")
    sifre.config(bg=arka_plan_rengi)
    sifre.resizable(False, False)
    parola = Entry(sifre, show='****************************')
    parola.pack(pady=5, fill=X, padx=5)
    Label(sifre, text="Parolanızı giriniz").pack(pady=5, padx=5)
    denemehakki = 3
    Button(sifre, text="Giriş Yap", command=dogrulama).pack(expand=True, fill="both", pady=5, padx=5)
    sifre.mainloop()

#######Önceki kayıtları okuyan textbox ve penceresi #################################
def kayitlari_oku():
    kayitlari_oku = Tk()
    kayitlari_oku.title("Kullanıcı Bilgi")
    kayitlari_oku.geometry("500x500")
    text_widget = scrolledtext.ScrolledText(kayitlari_oku, width=80, height=30)
    text_widget.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    try:
        with open(kayit_klasoru, 'r', encoding='utf-8') as dosya:
            dosya_icerigi = dosya.read()
            text_widget.delete(1.0, END)
            text_widget.insert(END, dosya_icerigi)
    except FileNotFoundError:
        text_widget.delete(1.0, END)
        text_widget.insert(END, "Dosya bulunamadı.")

####### Ana programın olduğu bölüm #################################
def AnaProgram():
    kullanıcı_adı = kullanici_bilgileri()
    kullanıcı_adı = f'Bilgisayar kullanıcı adı: {kullanıcı_adı}'
    pencere = Tk()
    pencere.title("Kişi Bilgi Kaydı")
    menü_cubuğu =Menu(pencere, bg=arka_plan_rengi )
    pencere_menü = Menu(menü_cubuğu , tearoff=0 ,bg="grey")
    menü_cubuğu.add_cascade(label="Bilgi", menu=pencere_menü )
    pencere_menü.add_command(label="Güncellemeler", command=güncellemeler)
    pencere_menü.add_command(label="kayitlari_oku", command=kayitlari_oku)
    pencere.config( menu=menü_cubuğu ,bg=arka_plan_rengi)
    pencere.resizable(False,False)
    pencere.geometry("400x450+200+100")
####### Dosyaya Pc kullanıcı adını yazdıran bölüm #################################
    def ödev_kontrol_etap():
        global ödev_durumu
        if ödev_kontrol.get(): ### checkbuttonun etkin olup olmadığını belirler ve değişkenine atar
            ödev_durumu = "evet"
        else :
            ödev_durumu = "hayır"
    def kullanıcı_adını_yazdır():
        with kayit_klasoru.open( "a" , encoding='utf-8') as dosya:
            dosya.write(f"\n********** {kullanıcı_adı} **********\n")
    kullanıcı_adını_yazdır() # Pc adını tek sefer yazdırmak için dosyaya_yaz foknsiyonunun dışına çıkardım
    def dosyaya_yaz(isim, soyisim, dersadi, dersnotu_vize, dersnotu_final, ortalama, odev_durumu): 
        with kayit_klasoru.open("a", encoding='utf-8') as dosya:
            dosya.write(f"İsim: {isim}\n Soyisim: {soyisim}\n"
                        f"Ders Adı: {dersadi}\n"
                        f"Vize: {dersnotu_vize}\n"
                        f"Final: {dersnotu_final}\n"
                        f"Ortalama: {ortalama}\n"
                        f"Ödev durumu: {ödev_durumu}\n"
                        "********************\n\n")
####### checkbutton ile ödev kontrolü sağlayan fonksiyon #################################
####### Tüm girdiğilerin alındığı ve kayıt edildiği alan #################################
    def kayıt_oluştur():
        isim = isim_giris.get().capitalize()
        soyisim = soyisim_giris.get().capitalize()
        dersnotu_vize =  dersnotu_vize_giris.get()
        dersnotu_final = dersnotu_final_giris.get()
        dersadı = dersadı_combobox.get()

        try: # Tüm bilgilerin eksiksiz girildiğinin kontrolü
            if not all([isim, soyisim, dersnotu_vize, dersnotu_final, dersadı]):
                raise ValueError("Lütfen tüm bilgileri eksiksiz girin.")
        except ValueError as e:
            messagebox.showerror("Hata", str(e))
        else:
            try: # İsim ve soyisim kontrolü
                if not (isinstance(isim, str) and isinstance(soyisim, str)) or not (isim.strip() and soyisim.strip()):
                    raise ValueError("İsim ve soyisim boş olmamalıdır.")
            except ValueError as e:
                messagebox.showerror("Hata", str(e))
            else:
                try: # Vize notu girişlerini sayı olarak
                    dersnotu_vize = float(dersnotu_vize)
                    dersnotu_final = float(dersnotu_final)
                    if not (0 <= dersnotu_vize <= 100 and 0 <= dersnotu_final <= 100):
                        raise ValueError("Ders notları 0 ile 100 arasında olmalıdır.")
                except ValueError as e:
                    messagebox.showerror("Hata", "Ders notları sadece sayı olmalıdır ve 0 ile 100 arasında olmalıdır.")
                else:  pass

    ####### Ortalama hesabının yapıldığı alan alan #################################
        def ortalama_hesabı():
            global vize_oran, ödev_oran 
            vize_oranlar = {
                "Bilgisayar donanımı": 50,
                "Yazılım uygulamaları testi": 30,
                "Veritabanı yönetimi": 40,
                "Devreler ve elektronik": 50,
                "Temel bilgi teknolojileri": 50,
                "Programlama ve Algoritma": 50  }
            
            ödev_oranlar = {
                "Yazılım uygulamaları testi": 0,
                "Veritabanı yönetimi": 0,
                "Devreler ve elektronik": 0,
                "Temel bilgi teknolojileri": 0,
                "Programlama ve Algoritma": 0  }
            
            if ödev_durumu == "evet":
                ödev_oranlar.update({
                    "Yazılım uygulamaları testi": 20,
                    "Veritabanı yönetimi": 10  })
                
            vize_oran  = vize_oranlar.get(dersadı, 0)
            final_oran = 50  
            ödev_oran = ödev_oranlar.get(dersadı, 0)

            toplam_dersnotu = (dersnotu_vize * vize_oran) + (dersnotu_final * final_oran)
            ortalama = toplam_dersnotu / 100 + (ödev_oran * 1)

            sonuçtext = (f"{isim} Adlı kişi kaydedildi\nOrtalaması = {ortalama}")
            messagebox.showinfo("kayıt",sonuçtext) ####### kullanıcıya geri bildirim verir
            dosyaya_yaz(isim, soyisim, dersadı, dersnotu_vize , dersnotu_final , ortalama ,ödev_durumu)
        ortalama_hesabı()
    #########
    multi_pack = Frame(pencere, bg=arka_plan_rengi)
    #########
    pcname = Label(pencere, text=kullanıcı_adı, font=(font_family, yeni_boyut, font_weight), bg=etiket_rengi).pack(anchor='nw', padx=1, pady=1)
    # Pcnin kullanıcı adını alıp yazdırır
    ##########
    isim_etiket = Label(multi_pack, text="İsim:",  font=font_stil ,bg=etiket_rengi).pack(pady=10)
    isim_giris = Entry(multi_pack, font=font_stil  ,bg=giris_kutusu_rengi) 
    isim_giris.pack(pady=5)
    ##########
    soyisim_etiket = Label(multi_pack, text="Soyisim:", font=font_stil , bg=etiket_rengi).pack(pady=5)
    soyisim_giris = Entry(multi_pack, font=font_stil ,bg=giris_kutusu_rengi)
    soyisim_giris.pack(pady=5)
    ##########
    dersnotu_vize = Label(multi_pack, text="vize notu:", font=font_stil , bg=etiket_rengi).pack(pady=5)
    dersnotu_vize_giris = Entry(multi_pack, font=font_stil ,bg=giris_kutusu_rengi)
    dersnotu_vize_giris.pack(pady=5)
    ##########
    dersnotu_final = Label(multi_pack, text="Final notu:", font=font_stil , bg=etiket_rengi).pack(pady=5)
    dersnotu_final_giris = Entry(multi_pack, font=font_stil ,bg=giris_kutusu_rengi)
    dersnotu_final_giris.pack(pady=5)
    ##########
    ödev_kontrol = BooleanVar()
    ödev_kontrol.set(True) #seçim yapılmadan önce "Etkin" olarak gelir 
    kontrol_kutusu = Checkbutton(multi_pack, text="Ödev Kontrol", font=font_stil, bg=etiket_rengi, variable=ödev_kontrol, command=ödev_kontrol_etap).pack()
    ##########
    dersadı_etiket = Label(multi_pack, text="Ders Adı:", font=font_stil ,bg=etiket_rengi).pack(pady=5)
    dersadı_combobox = ttk.Combobox(multi_pack, values=dersler, state="readonly", font=font_stil  )
    dersadı_combobox.set("Seçiniz..." )        # values liste kutusunda görüntülenecek listeyi belirtir.
    dersadı_combobox.current(0)   #seçim yapılmadan önce 0. seçenek seçili gelir
    dersadı_combobox.pack(pady=5)
    #########
    kaydet_düğme = Button(multi_pack, text="Kayıt Oluştur", command=kayıt_oluştur, font=font_stil ).pack(pady=5 ) 
    #########
    multi_pack.pack()
    pencere.mainloop()
####### ŞİFRELEME FONKSİYONU VE PENCERESİ #################################

if __name__ == "__main__":
    sifre_kontrol(AnaProgram)