import os

root_dir = r'd:\OFFICE\LIVE\JUNE[16-06-26]\Gymnastics & Acrobatics Training Center'

files_updated = 0
for filename in os.listdir(root_dir):
    if not filename.endswith('.html'):
        continue
        
    if filename in ['dashboard.html', 'login.html', 'register.html', '404.html', 'coming-soon.html']:
        continue
        
    filepath = os.path.join(root_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Wrap contents of navbar in <div class="container navbar-container">
    if '<nav class="navbar">' in content and 'navbar-container' not in content:
        content = content.replace('<nav class="navbar">', '<nav class="navbar">\n        <div class="container navbar-container">')
        content = content.replace('</nav>', '    </div>\n    </nav>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1

print(f'Updated {files_updated} HTML files.')
