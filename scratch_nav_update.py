import os

root_dir = r'd:\OFFICE\LIVE\JUNE[16-06-26]\Gymnastics & Acrobatics Training Center'

old_enroll = '<a href="register.html" class="btn btn-primary" style="height: 44px; padding: 0 20px;">Enroll Now</a>'
new_login = '<a href="login.html" class="btn btn-primary" style="height: 44px; padding: 0 20px;">Login</a>'

old_dashboard = '<a href="dashboard.html" class="nav-link" style="display: none;">Dashboard</a>'
new_dashboard = '''<a href="dashboard.html" class="nav-link dashboard-icon-link" aria-label="Dashboard" style="display: none; padding: 8px; border-radius: 8px; display: inline-flex; align-items: center; justify-content: center; height: 36px; width: 36px;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="3" width="7" height="7"></rect>
                    <rect x="14" y="3" width="7" height="7"></rect>
                    <rect x="14" y="14" width="7" height="7"></rect>
                    <rect x="3" y="14" width="7" height="7"></rect>
                </svg>
            </a>'''

files_updated = 0
for filename in os.listdir(root_dir):
    if not filename.endswith('.html'):
        continue
        
    if filename in ['dashboard.html', '404.html', 'coming-soon.html', 'login.html', 'register.html']:
        # We might still want to update the navbar if they have it, but usually dashboard has a different layout.
        pass
        
    filepath = os.path.join(root_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Check variations of the enroll button
    if old_enroll in content:
        content = content.replace(old_enroll, new_login)
        modified = True
        
    if old_dashboard in content:
        content = content.replace(old_dashboard, new_dashboard)
        modified = True
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1

print(f'Updated {files_updated} HTML files.')
