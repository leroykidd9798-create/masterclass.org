import os
import shutil

src = os.path.expanduser("~/Downloads")
dst = "d:/Projects/masterclass.org/img"

os.makedirs(dst, exist_ok=True)

files = [
    ("Без названия.jpg", "Без_названия.jpg"),
    ("Без названия (1).jpg", "Без_названия__1_.jpg"),
    ("Без названия (2).jpg", "Без_названия__2_.jpg"),
    ("Без названия (3).jpg", "Без_названия__3_.jpg"),
    ("#депиляция #эстетика #шугаринг #гладкость_.jpg", "_депиляция__эстетика__шугаринг__гладкость_.jpg"),
    ("The Dream Skin Clinic.jpg", "The_Dream_Skin_Clinic.jpg"),
    ("makeup collection.jpg", "makeup_collection.jpg"),
    ("Кисти для макияжа.jpg", "Кисти_для_макияжа.jpg"),
    ("Рабочее место мастера перманента.jpg", "Рабочее_место_мастера_перманента.jpg"),
    ("Lash aesthetic in 2024 _ Lashes, Eyelash extensions, False eyelash accessories.jpg", "Lash_aesthetic_in_2024___Lashes__Eyelash_extensions__False_eyelash_accessories.jpg")
]

for s, d in files:
    src_path = os.path.join(src, s)
    dst_path = os.path.join(dst, d)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied {s} to {d}")
    else:
        print(f"Not found: {src_path}")
