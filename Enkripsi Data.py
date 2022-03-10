print("----------------------+ Program Enkripsi Caesar +----------------------")

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def enkripsi(abjad):
    str = input("String : ") #input string yang akan di enkripsi
    key = int(input("Key : ")) #kunci untuk pergeseran abjad (enkripsi)

    str = str.lower() #string dikonversi ke huruf kecil semua
    result = '' #deklarasi variable result dengan nilai awal adalah kosong

    for char in str: #membuat perulangan untuk pergeseran abjad dari string
        if char in abjad: #abjad string dipecah 1 1 dan di cek apakah terdapat dalam value abjad
            n = abjad.index(char) #jika ada maka nilai index dari abjad yang ditemukan disimpan dalam variable n
            encrypt = (n - key) % 26 #rumus enkripsi
            convert = abjad[encrypt] #konversi nilai string ke hasil enkripsi
            result = result + convert #abjad yang sudah di konversi disimpat dalam variable result dalam bentuk string
        else:
            result = result + ' ' #jika abjad dari string tidak ditemukan dalam index abjad, maka akan dirubah ke dalam
                                  # bentuk spasi

    print(f"Result : {result}") #hasil dari perulangan untuk enkripsi string di tampilkan