import tkinter as tk
from tkinter import messagebox, ttk
import time
giris_kutusu_rengi = "lavender"         # ortak renkler
etiket_rengi = "white"                #
arka_plan_rengi = "steelblue"    
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