import os

root_dir = r'd:\OFFICE\LIVE\JUNE[16-06-26]\Gymnastics & Acrobatics Training Center'

dropdown_html = '''<div class="dropdown">
                <a href="#" class="nav-link dropdown-toggle">Home <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                <div class="dropdown-menu">
                    <a href="index.html" class="dropdown-item">Home 1</a>
                    <a href="home-2.html" class="dropdown-item">Home 2</a>
                </div>
            </div>'''

files_updated = 0
for filename in os.listdir(root_dir):
    if not filename.endswith('.html'):
        continue
        
    if filename in ['dashboard.html', 'login.html', 'register.html', '404.html', 'coming-soon.html']:
        continue
        
    filepath = os.path.join(root_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<a href="index.html" class="nav-link">Home</a>' in content:
        # We need to replace both Home and Home 2 links
        content = content.replace('<a href="index.html" class="nav-link">Home</a>\n            <a href="home-2.html" class="nav-link">Home 2</a>', dropdown_html)
        # Fallback if line endings differ
        content = content.replace('<a href="index.html" class="nav-link">Home</a>\n            <a href="home-2.html" class="nav-link">Home 2</a>', dropdown_html)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1

print(f'Updated {files_updated} HTML files for dropdown.')
