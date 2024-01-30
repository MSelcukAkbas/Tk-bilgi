from pathlib import Path
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
