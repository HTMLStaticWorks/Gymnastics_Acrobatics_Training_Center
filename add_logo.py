import os

root_dir = r'd:\OFFICE\LIVE\JUNE[16-06-26]\Gymnastics & Acrobatics Training Center'

svg_logo = '''<svg class="brand-icon" width="32" height="32" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 10px;">
    <path d="M10 30C10 30 16 14 20 14C24 14 30 30 30 30" stroke="var(--primary-accent)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="20" cy="6" r="5" fill="var(--secondary-accent)"/>
    <path d="M5 22L15 17M35 22L25 17" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
</svg><span style="display: inline-flex; align-items: center;">Gymnastics<span style="color: var(--primary-accent);">Academy</span></span>'''

files_updated = 0
for filename in os.listdir(root_dir):
    if not filename.endswith('.html'):
        continue
        
    filepath = os.path.join(root_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the text-based brand
    if 'Gymnastics<span>Academy</span>' in content:
        content = content.replace('Gymnastics<span>Academy</span>', svg_logo)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1

print(f'Updated {files_updated} HTML files with logo.')
