import os

root_dir = r'd:\OFFICE\LIVE\JUNE[16-06-26]\Gymnastics & Acrobatics Training Center'

social_html = '''
                    <div class="social-icons" style="display: flex; gap: 16px; margin-top: 24px;">
                        <a href="#" class="social-icon" aria-label="Facebook"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
                        <a href="#" class="social-icon" aria-label="Twitter"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
                        <a href="#" class="social-icon" aria-label="Instagram"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
                    </div>'''

back_to_top_html = '''
    <button id="back-to-top" aria-label="Back to top" class="back-to-top">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"></polyline></svg>
    </button>
'''

files_updated = 0
for filename in os.listdir(root_dir):
    if not filename.endswith('.html'):
        continue
        
    if filename in ['dashboard.html', 'login.html', 'register.html', '404.html', 'coming-soon.html']:
        continue
        
    filepath = os.path.join(root_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update footer padding
    content = content.replace('padding: 80px 0;', 'padding: 80px 0 24px 0;')
    
    # 2. Add social icons
    target_text = '<p>A premium Olympic gymnastics academy mixed with a modern child development platform.</p>'
    if target_text in content and 'social-icons' not in content:
        content = content.replace(target_text, target_text + social_html)
        
    # 3. Add back to top button before </body>
    if 'back-to-top' not in content:
        content = content.replace('</body>', back_to_top_html + '\n</body>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    files_updated += 1

print(f'Updated {files_updated} HTML files.')
