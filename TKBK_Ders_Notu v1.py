#####
import time
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from pathlib import Path
from Modüller.windowsadı  import kullanici_bilgileri
from Modüller.metinler import  güncellemelerbilgiders ,dersler
from Modüller.şifreekranı import sifre_kontrol
######
local_path  = Path.home() / 'AppData' / 'Local' / 'TK-BİLGİ'
#local_path .mkdir ; local path klasörüne make directory yani klasör oluştur diyerek klasör oluşturuyor
local_path.mkdir(parents=True, exist_ok=True) # exist_ok=True dosya zaten varsa olan dosya ile devam eder
                        #parents=True komutu ise dosya yolu eksik veya yanlış ise eksik olan dosya yolunu düzeltir ve ekler
# Dosya yolunu oluştur
kayit_klasoru = local_path  / 'kullanici_bilgileri.txt'
###
giris_kutusu_rengi = "lavender"# ortak renkler
etiket_rengi = "white"         #
arka_plan_rengi = "steelblue"
menü_rengi = "grey"  #   
font_stil = ("Helvetica",12, "bold") # ortak font
font_stil2 = ("Helvetica",12, "bold") # ortak font
font_family, font_size, font_weight = font_stil2
yeni_boyut = int(font_size * 0.8)
####### güncellemeler hakkında bilgi veren text box VE PENCERESİ #################################
def güncellemeler():
    güncelleme = tk.Tk()
    güncelleme.title("Güncelleme Detayları")
    güncelleme.geometry("1000x500")
    güncelleme.config(bg="white")
    güncelleme.resizable(False,False)

    text_box = tk.Text(güncelleme, height=10, width=30  , state="normal")
    text_box.pack(expand=True , fill=tk.BOTH)
    text_box.insert(tk.END, güncellemelerbilgiders)

    güncelleme.mainloop()
#################################
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
#################################
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
##############
    def dosyaya_yaz(kullanıcı_adı,isim, soyisim, dersadı, dersnotu_vize ,dersnotu_final): 
        with kayit_klasoru.open( "a" , encoding='utf-8') as dosya:
            dosya.write("\n")
            dosya.write(f"********** {kullanıcı_adı} **********\n")
            dosya.write(f"İsim: {isim}\n")
            dosya.write(f"Soyisim: {soyisim}\n")
            dosya.write(f"Ders Adı: {dersadı}\n")
            dosya.write(f"Vize: {dersnotu_vize}\n")
            dosya.write(f"Final: {dersnotu_final}\n")
            dosya.write(f"********************\n")     
            dosya.write("\n")
###############
    def kayıt_oluştur():
        isim = isim_giris.get()
        soyisim = soyisim_giris.get()
        dersnotu_vize = dersnotu_vize_giris.get()
        dersnotu_final = dersnotu_final_giris.get()
        dersadı = dersadı_combobox.get()
        
        if not all([isim, soyisim, dersnotu_vize, dersnotu_final, dersadı]):
            messagebox.showerror("Hata", "Lütfen tüm bilgileri eksiksiz girin.")
            return
        isim = isim.capitalize()
        soyisim = soyisim.capitalize()
        sonuç_text = f"{isim} {soyisim} Adlı kişi kaydedildi"
        messagebox.showinfo("Sonuç", sonuç_text)
        dosyaya_yaz(kullanıcı_adı, isim, soyisim, dersadı, dersnotu_vize , dersnotu_final)
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
