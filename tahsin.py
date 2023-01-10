from tkinter import *
from tkinter import ttk

root = Tk()
root.title(" Tahs-In app")#حسَّن - يحسِّن - تحسيناً ")
root.iconbitmap("E:/python_file/kelik/kaf.ico")
root.geometry("1000x670")


# creating list1
tempat = [
    "tempat_keluar_huruf",
    "sifat_huruf",
    "sifat_&_makhraj_perhuruf"
    ]

# create list 2
tempat_keluar_huruf = [
    "الْجَوْفُ : Rongga mulut",
    "الْحَلْقُ : tenggorokan",
    "اللِّسَانُ : lidah",
    "الشَّفَتَانِ : bibir",
    "الْخَيْشُوْمُ : rongga_hidung"
]
sifat_huruf = [
    "memiliki lawan kata segi nafas",
    "memiliki lawan kata segi suara",
    "memiliki lawan kata segi pangkal lidah",
    "memiliki lawan kata segi lidah & rongga mulut",
    "memiliki lawan kata segi mudah-sulit mengeluarkan huruf",
    "TIDAK memiliki lawan الصَّفِـيْرُ (Shofir)",
    "TIDAK memiliki lawan االْقَـلْقَـلَةُ (Qolqolah)",
    "TIDAK memiliki lawan اللِّيْنُ (Lin)",
    "TIDAK memiliki lawan الْإِنْحِرَافُ(Inhirof)",
    "TIDAK memiliki lawan التَّكْرِيْرُ (Takrir)",
    "TIDAK memiliki lawan التَّفَشِّي (Tafasyi)",
    "TIDAK memiliki lawan الْاِسْتِـطَالَةُ (Isthitholah)",
]
per_huruf = [
    "أ",
    "ب",
    "ت",
    "ث",
    "ج",
    "ح",
    "خ",
    "د",
    "ذ",
    "ر",
    "ز",
    "س",
    "ش",
    "ص",
    "ض",
    "ط",
    "ظ",
    "ع",
    "غ",
    "ف",
    "ق",
    "ك",
    "ل",
    "م",
    "ن",
    "و",
    "ه",
    "لا",
    "ي"
    
]

# create list3A
tempat_keluar_huruf_rongga = [
    " huruf : ا",
    "",
    " huruf : ي",
    "",
    " huruf : و"
]
tempat_keluar_huruf_tengg = [
    "الْحَلْقِ (Pangkal tenggorokan) : ه - ء ",
    "",
    "وَسْطُ الْحَلْقِ (tengah tenggorokan) : ح - ع ",
    "",
    "أَدْنَى الْحَلْقِ (ujung/atas tenggorokan) : خ - غ " 
]

tempat_keluar_huruf_lidah = [
    " اللَّحْمِيِّ Pangkal lidah (paling belakang) : ق ",
    "",
    "Pangkal lidah (sedikit kedepan) : ك ",
    "",
    "Tengah lidah dengan langit-langit : ش - ي - ج ",
    "",
    "Sisi lidah bertemu geraham atas : ض ",
    "",
    "Ujung sisi lidah  : ل ",
    "",
    "Ujung lidah setelah lam : ن ",
    "",
    "Ujung lidah setelah nun : ر ",
    "",
    "Ujung lidah bertemu gusi atas : ت , د dan ط ",
    "",
    "Ujung lidah diantara gigi atas dan gigi bawah : س, ز dan ص ",
    "",
    "Ujung lidah bertemu Ujung gigi depan atas : ث, ذ dan ظ "
 ]

tempat_keluar_huruf_bibir = [
    "Bibir bawah bagian dalam bertemu ujung gigi atas : ف ",
    "",
    "Dua bibir Tertutup : ب dan م ",
    "",
    "Dua bibir Membentuk bulatan : و "
]

tempat_keluar_huruf_rong_hid = [
    "لَا تَخْلُو نُوْنٌ وَمِيْمٌ مِنْ غُنَّةٍ  keluar dari rongga hidung ن  dan م ",
    "",
    "kedua huruf ini selalu disertai dengan ghunnah"
    "( suara yang keluar dari hidung )"
]

#CREATE LIST 3B
nafas = [
    " * Al-Hams (الهمس) - Keluar nafas فَحَثَهُ شَخْصٌ سَكَتَ",
    " ف – ح – ث – هـ – ش – خ – ص – س – ك – ت ",
    "",
    " * Al-Jahr (الجهر) - tidak keluar nafas ",
    "ع – ظ – م – و- ز- ن – ق – ا- ر- ء- ذ- ي- غ – ض – ج – د- ط – ل – ب"
]

tekan = [
    " * Asy Syiddah (الشِّدَّةُ ) - suara tertekan ",
    " أ – ج – د- ق- ط- ب – ك- ت",
    "",
    " * Ar-Rokhowah (الرَّخْوَةُ )- Suara terlepas",
    " خ – ذ – غ – ث – ح – ظ- ف – ض- ش – و – ص – ز- ي – س – هـ",
    "",
    " * Al-Bainiyah/At Tawassuth - pertengahan",
    " ل – ن – ع – م – ر"
]
pang_lidah = [
    "* الإِسْتِعْلاَءُ (Al Isti’la’) - terangkatnya lidah ke rongga atas ",
    "خ – ص- ض- غ- ط- ق- ر- ظ",
    "",
    "* الإِسْتِـفَالُ (Al Istifal) - lidah menurun ",
    " ث – ب – ت – ع – ز – م -ن -ي – ج – و- د- ح-",
    "ر – ف- هـ- إ – ذ – س-ل – ش- ك- ا"
    
]


lidah_rongga_mulut = [
    "* االإِطْبَاقُ (Al Ithbaq) - menempelnya lidah dengan rongga atas ",
    " ص – ض- ط- ظ",
    "",
    "* الإِنفِتَاحُ (Al Infitah)  - terlepasnya lidah dari rongga atas ",
    "  م – ن – أ- خ – ذ – و – ج – د -س – ع – ة – ف -ز – ك – ح -ق -",
    " ل – ه – ش- ر – ب – غ – ي – ث"
    
]

mudah_huruf = [
    "*اللإِذْلاَق ُ (Al Idzlaq) - mudah ",
    " ف – ر- م- ن- ل- ب",
    "",
    "* الإِصْمَاتُ (Al Ishmat)  - susah / tertahan ",
    "  ج – ز -غ – ش -س – خ – ط – ص – د – ث – ق – ",
    " ة – إ – ذ -و -ع-ظ- ه – ي- ح – ض – ك"
    
]

Shofir = [
    "الصَّفِـيْرُ (Shofir) -  suara desis",
    " ص - س  - ز  "
    ]
Qolqolah = [
    "الْقَـلْقَـلَةُ (Qolqolah) -  suara memantul / bergetar",
    " قُطْبُ جَدٍّ"
    ]
Lin = [
    "اللِّيْنُ (Lin) - mengeluarkan suara dengan lembut",
    " و - ي"
    ]
Inhirof = [
    "االْإِنْحِرَافُ(Inhirof) - Suara belok",
    " ل - ر "
    ]
Takrir = [
    "االتَّكْرِيْرُ (Takrir) - Ujung lidah bergetar:",
    " ر "
    ]
Tafasyi = [
    "التَّفَشِّي (Tafasyi) - Angin menyebar di mulut:",
    " ش "
]
Isthitholah = [
    "الْاِسْتِـطَالَةُ (Isthitholah) -  Suara memanjang ",
    " ض "
    
]

# create list 3c

hamzah = [
    "(أ) Sifat hamzah adalah jarh, syiddah, istifal, infitah, ishmat."
    ]
ba = [
    " (ب) Sifat ba’ adalah jahr, syiddah, istifal, infitah, idzlaq dan qalqalah."]
ta = [
    "(ت) Sifat ta’ adalah hams, syiddah, istifal, infitah dan ishmat."]
tsa = [
    "(ث) Sifat tsa’ adalah hams, rakhawah, istifal, infitah dan ishmat."]
jim = [
    "(ج) Sifat jim adalah jahr, syiddah, istifal, infitah, ishmat dan qalqalah."]
ha = [
    "(ح) Sifat ha’ adalah hams, rakhawah, istifal, infitah dan ishmat."]
kha = [
    "(خ) Sifat kha’ adalah hams, rakhawah, isti’la, infitah dan ishmat."]
dal = [
    "(د) Sifat dal adalah jahr, syiddah, istifal, infitah, ishmat dan qalqalah."]
dzal = [
    "(ذ) Sifat dzal adalah jahr, rakhawah, istifal, infitah dan ishmat."]
ra = [
    "(ر) Sifat ra’ adalah jahr, tawasuth, istifal, infitah, idzlaq, inhiraf dan takrir."]
zay = [
    "(ز) Sifat zay adalah jahr, rakhawah, istifal, infitah dan ishmat."]
sin = [
    "(س) Sifat sin adalah hams, rakhawah, istifal, infitah dan ishmat."]
syin = [
    "(ش) Sifat syin adalah hams, rakhawah, istifal, infitah, ishmat dan tafasyi."]
sho = [
    "(ص) Sifat shad adalah hams, rakhawah, isti’la, ithbaq dan ishmat."]
dhad = [
    "(ض) Sifat dhad adalah jahr, rakhawah, isti’la, ithbaq, ishmat dan istithalah."]
tha = [
    "(ط) Sifat tha; adalah jahr, syiddah, isti’la, ithbaq, ishmat dan qalqalah."]
zha = [
    "(ظ) Sifat zha’ adalah jahr, rakhawah, isti’la, ithbaq dan ishmat."]
ai = [
    "(ع) Sifat ‘ain adalah jahr, tawasuth, istifal, infitah dan ishmat."]
ghain = [
    "(غ) Sifat ghain adalah jahr, rakhawah, isti’la, infitah dan ishmat."]
fa = [
    "(ف) Sifat fa’ adalah hams, syiidah, istifal, infitah dan idzlaq."]
qaf = [
    "(ق) Sifat qaf adalah jahr, syiddah, isti’la, infitah, ishmat dan qalqalah."]
kaf = [
    "(ك) Sifat kaf adalah hams, syiddah, istifal, infitah dan ishmat."]
lam = [
    "(ل) Sifat lam adalah jahr, tawasuth, istifal, infitah, idzlaq dan inhiraf."]
mim = [
    "(م) • Makhraj mim adalah dua bibir dengan tanpa tekanan. Satu makhraj dengan ba’ dan wau.",
    "Sifat mim adalah jahr, tawasuth, istifal, infitah, idzlaq dan ghunnah."]
nun = [
    "(ن) Sifat nun adalah jahr, tawasuth, istifal, infitah, idzlaq dan ghunnah."]
wau = [
    "(و) Sifat wau adalah jahr, rakhawah, istifal, infitah, ishmat, lin dan khafa’."]
haa = [
    "(ه) Sifat ha’ adalah hams, rakhawah, istifal, infitah, ishmat dan khafa’."]
lam_alif =[
    "(لا)Sifat lam/alif adalah jahr, rakhawah, isitifal, infitah, ishmat dan khafa"]
ya = [
    "(ي) Sifat ya’ adalah jahr, rakhawah, istifal, infitah, ishmat dan lin dan khafa’."]
##list box
my_frame = Frame(root)
my_frame.pack(pady=10)

# list box
my_list1 = Listbox(my_frame,height=3,font=10)
my_list2 = Listbox(my_frame)
my_list3 = Listbox(my_frame)
my_list1.grid(row=2, column=0, pady=200)
my_list2.grid(row=2, column=1, padx=5)
my_list2.config(width=0,height=0)
my_list3.grid(row=2, column=2, padx=5)
my_list3.config(width=0,height=0)#grid(row=0, column=2, padx=5)

label1=Label(my_frame,text='بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ ',fg='blue',font=('Lucida',10))
label1.grid(row=0,column=1,padx=5,pady=1)
label2=Label(my_frame,text='Rangkuman Kategori dalam TAHSIN ',fg='blue',font=('Lucida',7))
label2.grid(row=1,column=1,padx=5,pady=5)
label3=Label(my_frame,text='saputrokelik2@gmail.com ',fg='black',font=('Lucida',7))
label3.grid(row=3,column=1,padx=5,pady=5)


#function for list 1
def list_color(e):
    my_list2.delete(0, END)
    if my_list1.get(ANCHOR) == "tempat_keluar_huruf":
        for item in tempat_keluar_huruf:
            my_list2.insert(END, item)    
    if my_list1.get(ANCHOR) == "sifat_huruf":
        for item in sifat_huruf:
            my_list2.insert(END, item)    
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        for item in per_huruf:
            my_list2.insert(END, item)    

#function for list 2                
def detail_texture(e):
    my_list3.delete(0, END)
    if my_list1.get(ANCHOR) == "tempat_keluar_huruf":
        if my_list2.get(ANCHOR) == "الْجَوْفُ : Rongga mulut":
            for item in tempat_keluar_huruf_rongga:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "tempat_keluar_huruf":
            if my_list2.get(ANCHOR) == "الْحَلْقُ : tenggorokan":
                for item in tempat_keluar_huruf_tengg:
                    my_list3.insert(END, item)  
    if my_list1.get(ANCHOR) == "tempat_keluar_huruf":
            if my_list2.get(ANCHOR) == "اللِّسَانُ : lidah":
                for item in tempat_keluar_huruf_lidah:
                    my_list3.insert(END, item)  
    if my_list1.get(ANCHOR) == "tempat_keluar_huruf":
            if my_list2.get(ANCHOR) == "الشَّفَتَانِ : bibir":
                for item in tempat_keluar_huruf_bibir:
                    my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "tempat_keluar_huruf":
            if my_list2.get(ANCHOR) == "الْخَيْشُوْمُ : rongga_hidung":
                for item in tempat_keluar_huruf_rong_hid:
                    my_list3.insert(END, item)  
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "memiliki lawan kata segi nafas":
            for item in nafas:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "memiliki lawan kata segi suara":
            for item in tekan:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "memiliki lawan kata segi pangkal lidah":
            for item in pang_lidah:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "memiliki lawan kata segi lidah & rongga mulut":
            for item in lidah_rongga_mulut:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "memiliki lawan kata segi mudah-sulit mengeluarkan huruf":
            for item in mudah_huruf:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "TIDAK memiliki lawan الصَّفِـيْرُ (Shofir)":
            for item in Shofir:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "TIDAK memiliki lawan االْقَـلْقَـلَةُ (Qolqolah)":
            for item in Qolqolah:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "TIDAK memiliki lawan اللِّيْنُ (Lin)":
            for item in Lin:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "TIDAK memiliki lawan الْإِنْحِرَافُ(Inhirof)":
            for item in Inhirof:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "TIDAK memiliki lawan التَّكْرِيْرُ (Takrir)":
            for item in Takrir:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "TIDAK memiliki lawan التَّفَشِّي (Tafasyi)":
            for item in Tafasyi:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_huruf":
        if my_list2.get(ANCHOR) == "TIDAK memiliki lawan الْاِسْتِـطَالَةُ (Isthitholah)":
            for item in Isthitholah:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "أ":
            for item in hamzah:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ب":
            for item in ba:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ت":
            for item in ta:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ث":
            for item in tsa:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ج":
            for item in jim:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ح":
            for item in ha:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "خ":
            for item in kha:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "د":
            for item in dal:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ذ":
            for item in dzal:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ر":
            for item in ra:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ز":
            for item in zay:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "س":
            for item in sin:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ش":
            for item in syin:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ص":
            for item in sho:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ض":
            for item in dhad:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ط":
            for item in tha:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ظ":
            for item in zha:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ع":
            for item in ai:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "غ":
            for item in ghain:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ف":
            for item in fa:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ق":
            for item in qaf:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ك":
            for item in kaf:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ل":
            for item in lam:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "م":
            for item in mim:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ن":
            for item in nun:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "و":
            for item in wau:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ه":
            for item in haa:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "ي":
            for item in ya:
               my_list3.insert(END, item)
    if my_list1.get(ANCHOR) == "sifat_&_makhraj_perhuruf":
        if my_list2.get(ANCHOR) == "لا":
            for item in lam_alif :
               my_list3.insert(END, item)


# add item to list 1

for item in tempat:
    my_list1.insert(END, item)

# Bind list box
my_list1.bind("<<ListboxSelect>>", list_color)
my_list2.bind("<<ListboxSelect>>", detail_texture)

# quit button
button_quit = Button(my_frame, text="Exit Program !!", command=root.destroy)
button_quit.grid(row=4,column=1)

root.mainloop()
