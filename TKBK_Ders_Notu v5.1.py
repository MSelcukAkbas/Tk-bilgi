##### Tek_pack v2 olmadan çalışmaz , lütfen dosya düzenine dikkat ediniz
#### TEK_Pack/tek_pack_v2 şekilde dosya düzeni ayarlayınız
## ana dosya düzeni klasör/TKBK_Ders_Notu v5.1.py , TEK_Pack/tek_pack_v2 şeklindedir
import time
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from pathlib import Path
from TEK_Pack.tek_pack_v2 import kullanici_bilgileri , dersler ,sifre_kontrol , güncellemeler 
######
local_path  = Path.home() / 'AppData' / 'Local' / 'TK-BİLGİ' #local_path .mkdir ; local path klasörüne make directory yani klasör oluştur diyerek klasör oluşturuyor
# KULLANICI BİLGILERİNIN ALINMASI ##################################
local_path.mkdir(parents=True, exist_ok=True) # exist_ok=True dosya zaten varsa olan dosya ile devam eder
#parents=True komutu ise dosya yolu eksik veya yanlış ise eksik olan dosya yolunu düzeltir ve ekler

kayit_klasoru = local_path  / 'kullanici_bilgileri.txt'# Dosya yolunu oluştur
######
giris_kutusu_rengi = "lavender"# ortak renkler
etiket_rengi = "white"         #
arka_plan_rengi = "steelblue"
menü_rengi = "grey"  #   
font_stil = ("Helvetica",12, "bold") # ortak font
font_stil2 = ("Helvetica",12, "bold") # ortak font
font_family, font_size, font_weight = font_stil2
yeni_boyut = int(font_size * 0.8)

#######Önceki kayıtları okuyan textbox ve penceresi #################################
def kayitlari_oku():
    kayitlari_oku=tk.Tk()
    kayitlari_oku.title("Kullanıcı Bilgi")
    kayitlari_oku.geometry("500x500")
    text_widget = scrolledtext.ScrolledText(kayitlari_oku, width=80, height=30)
    text_widget.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    ###
    try:
        with open(kayit_klasoru, 'r', encoding='utf-8') as dosya:
            dosya_icerigi = dosya.read()
            text_widget.delete(1.0, tk.END)  # Varolan içeriği temizle
            text_widget.insert(tk.END, dosya_icerigi)  # Dosya içeriğini ekle
    except FileNotFoundError:
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, "Dosya bulunamadı.")
####### Ana programın olduğu bölüm #################################
def AnaProgram():
    kullanıcı_adı = kullanici_bilgileri()
    kullanıcı_adı = f'Bilgisayar kullanıcı adı: {kullanıcı_adı}'
    pencere = tk.Tk()
    pencere.title("Kişi Bilgi Kaydı")
    menü_cubuğu =tk.Menu(pencere, bg=arka_plan_rengi )
    pencere_menü = tk.Menu(menü_cubuğu , tearoff=0 ,bg=menü_rengi)
    menü_cubuğu.add_cascade(label="Bilgi", menu=pencere_menü )
    pencere_menü.add_command(label="Güncellemeler", command=güncellemeler)
    pencere_menü.add_command(label="kayitlari_oku", command=kayitlari_oku)
    pencere.config( menu=menü_cubuğu ,bg=arka_plan_rengi)
    pencere.resizable(False,False)
    pencere.geometry("400x450+200+100")
####### Dosyaya Pc kullanıcı adını yazdıran bölüm #################################
    def kullanıcı_adını_yazdır():
        with kayit_klasoru.open( "a" , encoding='utf-8') as dosya:
            dosya.write("\n")
            dosya.write(f"********** {kullanıcı_adı} **********\n")
    kullanıcı_adını_yazdır() # Pc adını tek sefer yazdırmak için dosyaya_yaz foknsiyonunun dışına çıkardım
    def dosyaya_yaz(isim, soyisim, dersadı, dersnotu_vize ,dersnotu_final ,ortalama): 
        with kayit_klasoru.open( "a" , encoding='utf-8') as dosya:
            dosya.write(f"İsim: {isim}\n")
            dosya.write(f"Soyisim: {soyisim}\n")
            dosya.write(f"Ders Adı: {dersadı}\n")
            dosya.write(f"Vize: {dersnotu_vize}\n")
            dosya.write(f"Final: {dersnotu_final}\n")
            dosya.write(f"Ortalama: {ortalama}\n")
            dosya.write(f"Ödev durumu: {ödev_durumu}\n")
            dosya.write(f"********************\n")     
            dosya.write("\n")
####### checkbutton ile ödev kontrolü sağlayan fonksiyon #################################
    def ödev_kontrol_etap():
        global ödev_durumu
        if ödev_kontrol.get(): ### checkbuttonun etkin olup olmadığını belirler ve değişkenine atar
            ödev_durumu = "evet"
        else :
            ödev_durumu = "hayır"
####### Tüm girdiğilerin alındığı ve kayıt edildiği alan #################################
    def kayıt_oluştur():
        isim = isim_giris.get()
        soyisim = soyisim_giris.get()
        dersnotu_vize = dersnotu_vize_giris.get()
        dersnotu_final = dersnotu_final_giris.get()
        dersadı = dersadı_combobox.get()
        
        vize_oran = 0
        final_oran =0  # burda notların varsayılan  degerlerini gösteriyorum ama aşşağıda ders adına ve girilen nota göre değerler değişiyor
        ödev_oran = 0

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
                else:
                    # Tüm kontroller geçildiyse burada işlemler devam eder
                    pass
        isim = isim.capitalize()
        soyisim = soyisim.capitalize()
    ####### Ortalama hesabının yapıldığı alan alan #################################
        def ortalama_hesabı():
            global vize_oran, ödev_oran , ödev_durumu
            if dersadı == "Bilgisayar donanımı" :
                vize_oran = 50
                final_oran =50
                ödev_oran = 0
                ödev_durumu = "yok"
            if dersadı == "Yazılım uygulamalırı testi":
                vize_oran = 30
                final_oran = 50
                ödev_oran = 0
                if ödev_durumu == "evet" :
                    ödev_oran = 20
            if dersadı == "Veritabanı yönetimi":
                vize_oran = 40
                final_oran = 50
                ödev_oran = 0
                if ödev_durumu == "evet" :
                    ödev_oran = 10
            if dersadı == "Devreler ve elektronik":
                vize_oran = 50
                final_oran = 50
                ödev_oran = 0
                ödev_durumu = "yok"
            if dersadı == "Temel bilgi teknolojileri":
                vize_oran = 50
                final_oran =50
                ödev_oran = 0
                ödev_durumu = "yok"
            if dersadı == "Programlama ve Algoritma" :
                vize_oran = 50
                final_oran =50
                ödev_oran = 0
                ödev_durumu = "yok"

            toplam_dersnotu=(dersnotu_vize * vize_oran) +  (dersnotu_final*final_oran)
            ortalama=toplam_dersnotu/100         
            ortalama= ortalama + (ödev_oran*1) 
            sonuçtext = (f"{isim} Adlı kişi kaydedildi\nOrtalaması = {ortalama}")
            messagebox.showinfo("kayıt",sonuçtext) ####### kullanıcıya geri bildirim verir
            dosyaya_yaz(isim, soyisim, dersadı, dersnotu_vize , dersnotu_final , ortalama )
        ortalama_hesabı()
    #########
    multi_pack = tk.Frame(pencere, bg=arka_plan_rengi)
    #########
    pcname = tk.Label(pencere, text=kullanıcı_adı, font=(font_family, yeni_boyut, font_weight), bg=etiket_rengi).pack(anchor='nw', padx=1, pady=1)
    # Pcnin kullanıcı adını alıp yazdırır
    ##########
    isim_etiket = tk.Label(multi_pack, text="İsim:",  font=font_stil ,bg=etiket_rengi).pack(pady=10)
    isim_giris = tk.Entry(multi_pack, font=font_stil  ,bg=giris_kutusu_rengi) 
    isim_giris.pack(pady=5)
    ##########
    soyisim_etiket = tk.Label(multi_pack, text="Soyisim:", font=font_stil , bg=etiket_rengi).pack(pady=5)
    soyisim_giris = tk.Entry(multi_pack, font=font_stil ,bg=giris_kutusu_rengi)
    soyisim_giris.pack(pady=5)
    ##########
    dersnotu_vize = tk.Label(multi_pack, text="vize notu:", font=font_stil , bg=etiket_rengi).pack(pady=5)
    dersnotu_vize_giris = tk.Entry(multi_pack, font=font_stil ,bg=giris_kutusu_rengi)
    dersnotu_vize_giris.pack(pady=5)
    ##########
    dersnotu_final = tk.Label(multi_pack, text="Final notu:", font=font_stil , bg=etiket_rengi).pack(pady=5)
    dersnotu_final_giris = tk.Entry(multi_pack, font=font_stil ,bg=giris_kutusu_rengi)
    dersnotu_final_giris.pack(pady=5)
    ##########
    ödev_kontrol = tk.BooleanVar()
    ödev_kontrol.set(True) #seçim yapılmadan önce "Etkin" olarak gelir 
    kontrol_kutusu = tk.Checkbutton(multi_pack, text="Ödev Kontrol", font=font_stil, bg=etiket_rengi, variable=ödev_kontrol, command=ödev_kontrol_etap).pack()
    ##########
    dersadı_etiket = tk.Label(multi_pack, text="Ders Adı:", font=font_stil ,bg=etiket_rengi).pack(pady=5)
    dersadı_combobox = ttk.Combobox(multi_pack, values=dersler, state="readonly", font=font_stil  )
    dersadı_combobox.set("Seçiniz..." )        # values liste kutusunda görüntülenecek listeyi belirtir.
    dersadı_combobox.current(0)   #seçim yapılmadan önce 0. seçenek seçili gelir
    dersadı_combobox.pack(pady=5)
    #########
    kaydet_düğme = tk.Button(multi_pack, text="Kayıt Oluştur", command=kayıt_oluştur, font=font_stil ).pack(pady=5 ) 
    #########
    multi_pack.pack()
    pencere.mainloop()
####### ŞİFRELEME FONKSİYONU VE PENCERESİ #################################

if __name__ == "__main__":
    sifre_kontrol(AnaProgram)
