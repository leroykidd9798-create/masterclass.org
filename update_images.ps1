$filePath = "d:\Projects\masterclass.org\index.html"
$content = Get-Content -Path $filePath -Raw -Encoding UTF8

$replacements = @{
    "Парикмахер" = "img/Без_названия.jpg"
    "Маникюр" = "img/Без_названия__2_.jpg"
    "Бровист" = "img/Без_названия__1_.jpg"
    "Ресницы" = "img/Lash_aesthetic_in_2024___Lashes__Eyelash_extensions__False_eyelash_accessories.jpg"
    "Перманент" = "img/Рабочее_место_мастера_перманента.jpg"
    "Визажист" = "img/makeup_collection.jpg"
    "Сам себе визажист" = "img/Кисти_для_макияжа.jpg"
    "Косметолог" = "img/The_Dream_Skin_Clinic.jpg"
    "Шугаринг" = "img/_депиляция__эстетика__шугаринг__гладкость_.jpg"
    "Массаж" = "img/Без_названия__3_.jpg"
}

foreach ($key in $replacements.Keys) {
    $img = $replacements[$key]
    $escaped = [regex]::Escape($key)
    # The SVG contains: src="data:image/svg+xml,...%3E<TEXT>%3C/text%3E%3C/svg%3E"
    # We match "src=...<TEXT>%3C/text%3E%3C/svg%3E"
    $pattern = 'src="data:image/svg\+xml,[^"]+?' + $escaped + '%3C/text%3E%3C/svg%3E"'
    $content = [regex]::Replace($content, $pattern, "src=`"$img`"")
}

Set-Content -Path $filePath -Value $content -Encoding UTF8
