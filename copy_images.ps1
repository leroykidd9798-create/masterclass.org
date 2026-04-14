$src = "C:\Users\Consul\Downloads"
$dst = "d:\Projects\masterclass.org\img"

if (!(Test-Path $dst)) { New-Item -ItemType Directory -Path $dst | Out-Null }

Copy-Item "$src\Без названия.jpg" "$dst\Без_названия.jpg" -Force
Copy-Item "$src\Без названия (1).jpg" "$dst\Без_названия__1_.jpg" -Force
Copy-Item "$src\Без названия (2).jpg" "$dst\Без_названия__2_.jpg" -Force
Copy-Item "$src\Без названия (3).jpg" "$dst\Без_названия__3_.jpg" -Force
Copy-Item "$src\#депиляция #эстетика #шугаринг #гладкость_.jpg" "$dst\_депиляция__эстетика__шугаринг__гладкость_.jpg" -Force
Copy-Item "$src\The Dream Skin Clinic.jpg" "$dst\The_Dream_Skin_Clinic.jpg" -Force
Copy-Item "$src\makeup collection.jpg" "$dst\makeup_collection.jpg" -Force
Copy-Item "$src\Кисти для макияжа.jpg" "$dst\Кисти_для_макияжа.jpg" -Force
Copy-Item "$src\Рабочее место мастера перманента.jpg" "$dst\Рабочее_место_мастера_перманента.jpg" -Force
Copy-Item "$src\Lash aesthetic in 2024 _ Lashes, Eyelash extensions, False eyelash accessories.jpg" "$dst\Lash_aesthetic_in_2024___Lashes__Eyelash_extensions__False_eyelash_accessories.jpg" -Force
