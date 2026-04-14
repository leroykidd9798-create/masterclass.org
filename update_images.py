import re

with open('d:/Projects/masterclass.org/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'Парикмахер': 'img/Без_названия.jpg',
    'Маникюр': 'img/Без_названия__2_.jpg',
    'Бровист': 'img/Без_названия__1_.jpg',
    'Ресницы': 'img/Lash_aesthetic_in_2024___Lashes__Eyelash_extensions__False_eyelash_accessories.jpg',
    'Перманент': 'img/Рабочее_место_мастера_перманента.jpg',
    'Визажист': 'img/makeup_collection.jpg',
    'Сам себе визажист': 'img/Кисти_для_макияжа.jpg',
    'Косметолог': 'img/The_Dream_Skin_Clinic.jpg',
    'Шугаринг': 'img/_депиляция__эстетика__шугаринг__гладкость_.jpg',
    'Массаж': 'img/Без_названия__3_.jpg'
}

for text_match, img_path in replacements.items():
    # Find the src attribute that contains the SVG encoded tag for the given text match
    # Example: src="data:image/svg+xml,...%3EПарикмахер%3C/text%3E%3C/svg%3E"
    pattern = r'src="data:image/svg\+xml,[^"]+?' + re.escape(text_match) + r'%3C/text%3E%3C/svg%3E"'
    
    # We will replace it with src="..."
    content = re.sub(pattern, f'src="{img_path}"', content)

with open('d:/Projects/masterclass.org/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML modified successfully.")
