from pathlib import Path


def kullanici_bilgileri():
    kullanıcı_adı = Path("~").expanduser()
    kullanıcı_adı = str(kullanıcı_adı)
    kullanıcı_adı = kullanıcı_adı[9:]
    
    return kullanıcı_adı.capitalize()
