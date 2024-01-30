
#####
import time
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from pathlib import Path
from Modüller.metinler import şehirler , güncellemelerbilgi , sistemler
from Modüller.şifreekranı import sifre_kontrol
######
giris_kutusu_rengi = "lavender"# ortak renkler
etiket_rengi = "white"         #
arka_plan_rengi = "steelblue"
menü_rengi = "grey"  #   
font_stil = ("Helvetica",12, "bold") # ortak font
####### güncellemeler hakkında bilgi veren text box VE PENCERESİ #################################
def güncellemeler():
    güncelleme = tk.Tk()
    güncelleme.title("Güncelleme Detayları")
    güncelleme.geometry("1000x500")
    güncelleme.config(bg="white")
    güncelleme.resizable(False,False)

    text_box = tk.Text(güncelleme, height=10, width=30  , state="normal")
    text_box.pack(expand=True , fill=tk.BOTH)
    text_box.insert(tk.END, güncellemelerbilgi)

    güncelleme.mainloop()
def menü_güncelleme_açma():
    güncellemeler()
#################################
def kayitlari_oku():
    kullanıcıbigi=tk.Tk()
    kullanıcıbigi.title("Kullanıcı Bilgi")
    text_widget = scrolledtext.ScrolledText(kullanıcıbigi, width=80, height=20)
    text_widget.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    dosya_adı = "kullanici_bilgileri.txt"
    
    try:
        with open(dosya_adı, 'r', encoding='utf-8') as dosya:
            dosya_icerigi = dosya.read()
            text_widget.delete(1.0, tk.END)  # Varolan içeriği temizle
            text_widget.insert(tk.END, dosya_icerigi)  # Dosya içeriğini ekle
    except FileNotFoundError:
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, "Dosya bulunamadı.")
#################################
def giris_yap():
    pencere = tk.Tk()
    pencere.title("Kişi Bilgi Kaydı")
    
    menü_cubuğu =tk.Menu(pencere, bg=arka_plan_rengi )
    pencere_menü = tk.Menu(menü_cubuğu , tearoff=0 ,bg=menü_rengi)
    menü_cubuğu.add_cascade(label="Bilgi", menu=pencere_menü )
    pencere_menü.add_command(label="Güncellemeler", command=menü_güncelleme_açma)
    pencere_menü.add_command(label="kayitlari_oku", command=kayitlari_oku)
    pencere.config( menu=menü_cubuğu ,bg=arka_plan_rengi)
    pencere.resizable(False,False)
    pencere.geometry("400x450+200+100")
#################################
    def dosyaya_yaz(isim, soyisim, işsis, sehir):
        with open("kullanici_bilgileri.txt", "a" , encoding='utf-8') as dosya:
            dosya.write("\n")
            dosya.write(f"**************************\n")
            dosya.write(f"İsim: {isim}\n")
            dosya.write(f"Soyisim: {soyisim}\n")
            dosya.write(f"İşletim Sistemi: {işsis}\n")
            dosya.write(f"Şehir: {sehir}\n")
            dosya.write(f"**************************\n")
            dosya.write("\n")
#################################
    def kayıt_oluştur():
        isim = isim_giris.get()
        soyisim = soyisim_giris.get()
        işsis = işsiz_combobox.get()
        sehir = il_combobox.get()
        
        if not isim or not soyisim or işsis == "Seçiniz..." or sehir == "Seçiniz...":
            messagebox.showerror("Hata", "Lütfen tüm bilgileri eksiksiz girin.")
            return
        isim = isim.capitalize()
        soyisim = soyisim.capitalize()
        sonuç_text = f"{isim} {soyisim} Adlı kişi kaydedildi"
        messagebox.showinfo("Sonuç", sonuç_text)
        dosyaya_yaz(isim, soyisim, işsis, sehir)
    
    #########
    multi_pack = tk.Frame(pencere, bg=arka_plan_rengi)
    ##########
    isim_etiket = tk.Label(multi_pack, text="İsim:",  font=font_stil ,bg=etiket_rengi).pack(pady=10)
    isim_giris = tk.Entry(multi_pack, font=font_stil  ,bg=giris_kutusu_rengi) 
    isim_giris.pack(pady=5)
    ##########
    soyisim_etiket = tk.Label(multi_pack, text="Soyisim:", font=font_stil , bg=etiket_rengi).pack(pady=5)
    soyisim_giris = tk.Entry(multi_pack, font=font_stil ,bg=giris_kutusu_rengi)
    soyisim_giris.pack(pady=5)
    ##########
    işsis_etiket = tk.Label(multi_pack, text="İşletim Sistemi:", font=font_stil ,bg=etiket_rengi).pack(pady=5)
    işsiz_combobox = ttk.Combobox(multi_pack, values=sistemler, state="readonly", font=font_stil  )
    işsiz_combobox.set("Seçiniz..." )        # values liste kutusunda görüntülenecek listeyi belirtir.
    işsiz_combobox.current(0)   #seçim yapılmadan önce 0. seçenek seçili gelir
    işsiz_combobox.pack(pady=5)
    #########
    il_etiket = tk.Label(multi_pack, text="İl Seçiniz:", font=font_stil ,bg=etiket_rengi).pack(padx=10, pady=5)
    il_combobox = ttk.Combobox(multi_pack, values=şehirler, state="readonly", font=font_stil  )
    il_combobox.set("Seçiniz...")
    il_combobox.current(0)      #seçim yapılmadan önce 0. seçenek seçili gelir
    il_combobox.pack(pady=5)
    #########
    kaydet_düğme = tk.Button(multi_pack, text="Kayıt Oluştur", command=kayıt_oluştur, font=font_stil )
    kaydet_düğme.pack(pady=5 ) 
    #########
    multi_pack.pack()
    pencere.mainloop()
####### ŞİFRELEME FONKSİYONU VE PENCERESİ #################################
if __name__ == "__main__":
    sifre_kontrol(giris_yap)  # Şifre kontrol ekranını çağır 

