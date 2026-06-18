import os
import shutil

root_dir = r"d:\OFFICE\LIVE\JUNE[16-06-26]\Gymnastics & Acrobatics Training Center"

dirs = [
    "assets/css",
    "assets/js",
    "assets/images",
]

for d in dirs:
    os.makedirs(os.path.join(root_dir, d), exist_ok=True)

html_files = [
    "index.html", "home-2.html", "about.html", "programs.html", "program-details.html",
    "coaches.html", "progression-framework.html", "pricing.html", "gallery.html",
    "gallery-details.html", "blog.html", "blog-details.html", "contact.html",
    "login.html", "register.html", "dashboard.html", "404.html", "coming-soon.html"
]

for f in html_files:
    path = os.path.join(root_dir, f)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as file:
            file.write(f"<!-- {f} -->\n")

css_files = ["style.css", "dark-mode.css", "rtl.css"]
for f in css_files:
    path = os.path.join(root_dir, "assets", "css", f)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as file:
            file.write(f"/* {f} */\n")

js_files = ["main.js", "dashboard.js"]
for f in js_files:
    path = os.path.join(root_dir, "assets", "js", f)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as file:
            file.write(f"// {f}\n")

print("Project structure created successfully.")
