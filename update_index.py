import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Carousel Arrow Fix
html = html.replace('display:none;">←</button>', 'display:flex; align-items:center; justify-content:center;" id="prevBtn" class="carousel-prev desktop-arrow">←</button>')
html = html.replace('display:none;">→</button>', 'display:flex; align-items:center; justify-content:center;" id="nextBtn" class="carousel-next desktop-arrow">→</button>')

# 2. Carousel Remove Buttons
html = re.sub(r'<a href="https://wa\.me/[^>]+>Получить консультацию →</a>', '', html)

# 3. Format Section (Как проходит обучение)
html = html.replace('<section id="format" class="section" style="background: var(--c-white);">', '<section id="format" class="section format-bg">')
html = html.replace('class="step-card"', 'class="step-card glass-card"')

# 4. Results Section (Ваш результат после курса)
# Replace emojis with SVG
html = html.replace('<div class="icon-wrap">💎</div>', '<div class="icon-wrap"><svg viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 2l8 4-8 4-8-4 8-4zm0 8l8 4-8 4-8-4 8-4zm0 8l8 4-8 4-8-4 8-4z"/></svg></div>')
html = html.replace('<div class="icon-wrap">💰</div>', '<div class="icon-wrap"><svg viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m-3-2.818l.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div>')
html = html.replace('<div class="icon-wrap">🚀</div>', '<div class="icon-wrap"><svg viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg></div>')

# 5. Reviews Section Names
html = html.replace('>Айдана</h4>', '>Айдана Касымова</h4>')
html = html.replace('>Мадина</h4>', '>Мадина Токтобекова</h4>')
html = html.replace('>Зарина</h4>', '>Зарина Осмонова</h4>')

# 6. Global Link Replacements
html = html.replace('https://instagram.com/masster.class', 'https://www.instagram.com/jazira.avaz.beauty?igsh=MXhjeGZxaGo0azlxeQ==')
html = html.replace('https://go.2gis.com/j4q49', 'https://2gis.kg/bishkek/geo/15760360721868352')

old_wa_text = "https://wa.me/996553381039"
wa_text_new = "https://wa.me/996553381039?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5!%20%D0%AF%20%D0%BF%D0%B5%D1%80%D0%B5%D1%88%D1%91%D0%BB%20%D1%81%20%D1%81%D0%B0%D0%B9%D1%82%D0%B0%20MasterClass%20%D0%B8%20%D1%85%D0%BE%D1%87%D1%83%20%D1%83%D0%B7%D0%BD%D0%B0%D1%82%D1%8C%20%D0%BF%D0%BE%D0%B4%D1%80%D0%BE%D0%B1%D0%BD%D0%B5%D0%B5%20%D0%BE%20%D0%BA%D1%83%D1%80%D1%81%D0%B0%D1%85."

html = re.sub(r'href="https://wa.me/[^"]*"', f'href="{wa_text_new}"', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
