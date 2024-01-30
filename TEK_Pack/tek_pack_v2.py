from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk
import time

##########
giris_kutusu_rengi = "lavender"         # ortak renkler
etiket_rengi = "white"                #
arka_plan_rengi = "steelblue"  
##########
dersler = ["Bilgisayar donanımı", "Yazılım uygulamalırı testi", "Veritabanı yönetimi", "Programlama ve Algoritma" , "Devreler ve elektronik", "Temel bilgi teknolojileri"]
######
def kullanici_bilgileri():
    kullanıcı_adı = Path("~").expanduser()
    kullanıcı_adı = str(kullanıcı_adı)
    kullanıcı_adı = kullanıcı_adı[9:]
    
    return kullanıcı_adı.capitalize()
######
def apdata_yazma():
    local_path = Path.home() / 'AppData' / 'Local' / 'YourFolderName'

    # Klasörü oluştur
    local_path.mkdir(parents=True, exist_ok=True)

    # Dosya yolunu oluştur
    file_path = local_path / 'your_file.txt'

    # Dosyaya veri ekle
    with file_path.open('a') as file:
        # Kullanıcıdan alınan metin girdisini dosyaya ekleyin
        user_input = input("Metin girdisi: ")
        file.write(user_input + '\n')  # Yeni veriyi dosyanın sonuna ekleyin
######
güncellemelerbilgiders = (   
"   v1 sürümü daha basit bir kod mantığı ile çalışıyor"
"\n   v2 bu güncellemeden seçim kutusu(combobox) getirdim ; il ve işletim sistemini listeden alıyoruz"
"\n   v3 sonuç ekranını kaldırdım onun yerine mesaj kutusu koydum çünkü sonuç ekranı çirkin gözüküyor"
"\n   v4 renk ve boyutlar üzerinde düzeltmeler yapıldı , combobox rengi değiştirme şuanlık çalışmıyor "
"\n            -birden fazla pack yerine tek pack atıyoruz ,frame ile düzeni geliştiriyoruz"
"\n   TKBK-v4.1 de arayüze şifre uygulaması eklenmiştir"
"\n   TKBK-v4.2 DE şifre girişi sonrasında hata yada bilgi meseajı veriliyor"
"\n            -Deneme hakkı uygulaması geldi , global anahtar kelimesi kullanıldı"
"\n   TKBK-v4.3 de packler üzerinde düzenleme yapıldı ve programın genel satır sayısında azalma sağlandı "
"\n            -pack işlemini direkt label ve combobox gibi işlemlerin yanında kullanılıyormuş."
"\n            -entrylerde hataya neden oluyor , get() çalışmıyor "
"\n   TKBK-v4.4 da güncellemeler hakkında bilgi veren text box eklendi ve süresi 3sn ye ayarlandı "
"\n   TKBK-v4.5 te random kelimer kaldırıldı ve güncelleme detayları menüye eklendi"
"\n   TKBK-v4.6 da temizlik yapıldı ve önceki kayıtları okuma özelliği geldi"
"\n            -Modülerlik getirildi"
"\n   TKBK-v4.7 de modülerlik arttırıldı ve 50 satırdan fazla azaltma yapıldı "
"\n   TKBK-v5 te artık veriler rasgele yerlere değil direk appdata ya kaydoluyor. "
)
######
güncellemelerbilgiders_güncel = (   
"\n   TKBk_Ders_Notu programında ders bilgileri , vize notu ve final notu girişi ayarlandı "
"\n            -Şehir bilgisi kaldırıldı "
"\n   TKBk_Ders_Notu v2 de 'PC adı' tek sefer yazdırılıyor ve program yeniden çalıştırılana kadar tekrar yazılmıyor "
"\n   TKBk_Ders_Notu v3 de Ortalama hesabı özelliği geldi ve ortalama kayıt edilip ekrana geliyor "
"\n   TKBk_Ders_Notu v4 de ödev kontrol ediliyor (checkbutton ile) ve ödev oranına göre ortalama hesaplanıyor  "
"\n            - Tüm modüller tek py altına toplandı (tek_pack) ve daha organize hale getirildi "
"\n            - TKBk_Ders_Notu v4.1 de genel kod temizliği yapıldı"
"\n   TKBk_Ders_Notu v5 te artık güncellemeler ekranına menü eklendi ve menü sayesinde önceki  güncellemeleri görüyoruz."
"\n            - TKBk_Ders_Notu v5.1 de genel kod temizliği yapıldı ve güncellemeler menüsü tek_pack_v2 ye taşındı "
)
######
def sifre_kontrol(giris_yap_fonskiyonu):
    şifre = tk.Tk()
    şifre.title("Kilit Ekranı")
    şifre.geometry("400x180+200+100")
    şifre.config(bg=arka_plan_rengi)
    şifre.resizable(False, False)

    parola = tk.Entry(şifre, show='****************************')
    parola.pack(pady=5, fill=tk.X, padx=5)
    parolatiket = tk.Label(şifre, text="Parolanızı giriniz").pack(pady=5, padx=5)
    denemehakkı = 3
    def doğrulama():
        nonlocal denemehakkı
        if parola.get() == "1234":
            messagebox.showinfo("GİRİŞ!", "GİRİŞ YAPILIYOR....")
            time.sleep(0.1)
            şifre.destroy()
            time.sleep(1)
            giris_yap_fonskiyonu()  # giris_yap_func fonksiyonunu burada çağırabilirsiniz
        else:
            denemehakkı -= 1
            messagebox.showerror("HATA!", f"PAROLAYI HATALI GİRDİNİZ.\nDENEME HAKKI:  {denemehakkı} KALDI.")
            time.sleep(0.5)
            if denemehakkı == 0:
                messagebox.showerror(f"HATA!", "PROGRAM KAPATILIYOR...")
                time.sleep(0.5)
                şifre.destroy()
    parolasalama = tk.Button(şifre, text="Giriş Yap", command=doğrulama)
    parolasalama.pack(expand=True, fill=tk.BOTH, pady=5, padx=5)

    şifre.mainloop()
######
def güncellemeler_eski():
    güncelleme = tk.Tk()
    güncelleme.title("Güncelleme Detayları")
    güncelleme.geometry("1000x500")
    güncelleme.config(bg="white")
    güncelleme.resizable(False,False)

    text_box = tk.Text(güncelleme, height=10, width=30 , state="normal")
    text_box.pack(expand=True , fill=tk.BOTH)
    text_box.insert(tk.END, güncellemelerbilgiders)

    güncelleme.mainloop()
######
def güncellemeler():
    güncelleme = tk.Tk()
    güncelleme.title("TKBK Ders Notu Güncelleme Detayları")
    güncelleme.geometry("1000x500")
    güncelleme.resizable(False,False)

    menü_cubuğu =tk.Menu(güncelleme, bg=arka_plan_rengi )
    güncelleme_menü = tk.Menu(menü_cubuğu , tearoff=0 ,bg="white")
    menü_cubuğu.add_cascade(label="Eski güncellemeler", menu=güncelleme_menü )
    güncelleme_menü.add_command(label="Tüm Güncellemeler", command=güncellemeler_eski)
    güncelleme.config( menu=menü_cubuğu ,bg=arka_plan_rengi)

    text_box = tk.Text(güncelleme, height=10, width=30 , state="normal")
    text_box.pack(expand=True , fill=tk.BOTH)
    text_box.insert(tk.END, güncellemelerbilgiders_güncel)

    güncelleme.mainloop()