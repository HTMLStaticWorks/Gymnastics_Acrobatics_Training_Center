import os

root_dir = r"d:\OFFICE\LIVE\JUNE[16-06-26]\Gymnastics & Acrobatics Training Center"

# Extract Navbar and Footer from index.html
with open(os.path.join(root_dir, "index.html"), "r", encoding="utf-8") as f:
    index_content = f.read()

nav_start = index_content.find('<!-- Navbar -->')
nav_end = index_content.find('<!-- Hero Section -->')
navbar = index_content[nav_start:nav_end]

footer_start = index_content.find('<footer')
footer_end = index_content.find('</body>')
footer = index_content[footer_start:footer_end]

# Common header
def get_header(title):
    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-width=1.0">
    <title>{title} | Gymnastics & Acrobatics Training Center</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/dark-mode.css">
    <link rel="stylesheet" href="assets/css/rtl.css">
    <link rel="stylesheet" href="assets/css/pages.css">
</head>
<body>
{navbar}
"""

def get_footer():
    return f"""{footer}
</body>
</html>
"""

# about.html
about_content = get_header("About Us") + """
<header class="page-hero container" style="text-align: center; padding-top: 160px; padding-bottom: 60px;">
    <span class="subheading">Who We Are</span>
    <h1 style="margin-bottom: 24px;">About The Academy</h1>
    <p style="max-width: 600px; margin: 0 auto;">Discover our journey, our mission, and what makes us the premier gymnastics training center.</p>
</header>

<section class="section container">
    <div class="grid grid-cols-2 gap-8 items-center">
        <div>
            <span class="subheading">Academy Story</span>
            <h2>A Legacy of Excellence</h2>
            <p>Founded with the belief that every child deserves the opportunity to develop their physical and mental strength, our academy has grown from a small community gym to a state-of-the-art training facility.</p>
            <p>We pride ourselves on offering the highest quality instruction in a supportive, challenging, and fun environment.</p>
        </div>
        <div class="image-reveal-wrapper">
            <img src="assets/images/about_facility_1781704800816.png" alt="Academy Facility" class="rounded-image shadow-img" style="width: 100%; border-radius: var(--border-radius-lg);">
        </div>
    </div>
</section>

<section class="section" style="background: var(--secondary-bg);">
    <div class="container grid grid-cols-2 gap-8 items-center flex-md-col-reverse">
        <div class="image-reveal-wrapper" style="animation-delay: 0.2s;">
            <img src="assets/images/about_mission_1781704820711.png" alt="Academy Mission" class="rounded-image shadow-img" style="width: 100%; border-radius: var(--border-radius-lg);">
        </div>
        <div>
            <span class="subheading">Mission & Vision</span>
            <h2>Empowering The Next Generation</h2>
            <p>Our mission is to foster self-esteem, discipline, and physical fitness through the sport of gymnastics. We envision a community where every young athlete has the resources to achieve their dreams, whether that's mastering a handstand or competing on a national stage.</p>
            <ul class="custom-list" style="margin-top: 24px;">
                <li>Build character and confidence</li>
                <li>Ensure a safe, progressive learning environment</li>
                <li>Nurture individual talent and teamwork</li>
            </ul>
        </div>
    </div>
</section>

<section class="section container">
    <div class="section-title text-center">
        <span class="subheading">Safety First</span>
        <h2>Our Safety Standards</h2>
    </div>
    <div class="grid grid-cols-3 gap-6">
        <div class="card premium-card hover-lift">
            <h3 style="color: var(--primary-accent);">Certified Staff</h3>
            <p>All coaches undergo rigorous safety certification and background checks.</p>
        </div>
        <div class="card premium-card hover-lift">
            <h3 style="color: var(--primary-accent);">Premium Equipment</h3>
            <p>We use state-of-the-art, Olympic-grade equipment regularly inspected for safety.</p>
        </div>
        <div class="card premium-card hover-lift">
            <h3 style="color: var(--primary-accent);">Structured Ratios</h3>
            <p>Strict coach-to-student ratios ensure every child receives personalized attention.</p>
        </div>
    </div>
</section>

<section class="section" style="background: var(--primary-bg); border-top: 1px solid var(--border-color);">
    <div class="container grid grid-cols-2 gap-8 items-center">
        <div>
            <span class="subheading">Our Approach</span>
            <h2>Training Philosophy</h2>
            <p>We believe in positive reinforcement and structured progression. Every child develops at their own pace, and our curriculum is designed to celebrate individual milestones while keeping athletes challenged and engaged.</p>
        </div>
        <div class="image-reveal-wrapper">
            <img src="assets/images/coach_female_1781704842189.png" alt="Training Philosophy" class="rounded-image shadow-img" style="width: 100%; border-radius: var(--border-radius-lg);">
        </div>
    </div>
</section>
""" + get_footer()

with open(os.path.join(root_dir, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_content)


# contact.html
contact_content = get_header("Contact Us") + """
<header class="page-hero container" style="text-align: center; padding-top: 160px; padding-bottom: 60px;">
    <span class="subheading">Get In Touch</span>
    <h1 style="margin-bottom: 24px;">Contact Us</h1>
    <p style="max-width: 600px; margin: 0 auto;">Have questions about enrollment, schedules, or our programs? We're here to help.</p>
</header>

<section class="section container">
    <div class="grid grid-cols-2 gap-8">
        <div class="card form-card shadow-lg" style="padding: 48px;">
            <h3 style="margin-bottom: 24px;">Send us a Message</h3>
            <form action="#">
                <div class="form-group">
                    <label class="form-label">Full Name</label>
                    <input type="text" class="form-control" placeholder="John Doe">
                </div>
                <div class="form-group">
                    <label class="form-label">Email Address</label>
                    <input type="email" class="form-control" placeholder="john@example.com">
                </div>
                <div class="form-group">
                    <label class="form-label">Subject</label>
                    <input type="text" class="form-control" placeholder="How can we help?">
                </div>
                <div class="form-group">
                    <label class="form-label">Message</label>
                    <textarea class="form-control" rows="5" style="height: auto; padding-top: 16px;" placeholder="Write your message here..."></textarea>
                </div>
                <button type="submit" class="btn btn-primary btn-block">Send Message</button>
            </form>
        </div>
        
        <div>
            <div class="card" style="margin-bottom: 24px;">
                <h3 style="margin-bottom: 16px;">Our Location</h3>
                <p>123 Olympic Training Blvd<br>Sports City, SC 12345</p>
                <div style="margin-top: 24px; height: 300px; background: #e2e8f0; border-radius: var(--border-radius); display: flex; align-items: center; justify-content: center; overflow: hidden;">
                    <!-- Placeholder for actual map iframe -->
                    <div style="text-align: center; color: var(--text-secondary);">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-bottom: 8px;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                        <p>Interactive Map Embed</p>
                    </div>
                </div>
            </div>
            <div class="grid grid-cols-2 gap-4">
                <div class="card">
                    <h4>Phone</h4>
                    <p style="color: var(--primary-accent); font-weight: 500;">(555) 123-4567</p>
                </div>
                <div class="card">
                    <h4>Email</h4>
                    <p style="color: var(--primary-accent); font-weight: 500;">info@gymnastics.com</p>
                </div>
            </div>
        </div>
    </div>
</section>
""" + get_footer()

with open(os.path.join(root_dir, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_content)


# coaches.html
coaches_content = get_header("Our Coaches") + """
<header class="page-hero container" style="text-align: center; padding-top: 160px; padding-bottom: 60px;">
    <span class="subheading">Meet The Team</span>
    <h1 style="margin-bottom: 24px;">Our Coaches</h1>
    <p style="max-width: 600px; margin: 0 auto;">Dedicated professionals committed to bringing out the best in every athlete.</p>
</header>

<section class="section container">
    <div class="grid grid-cols-2 gap-8 items-center">
        <div class="image-reveal-wrapper">
            <img src="assets/images/coach_female_1781704842189.png" alt="Head Coach" class="rounded-image shadow-img" style="width: 100%; border-radius: var(--border-radius-lg);">
        </div>
        <div>
            <span class="subheading">Head Coach</span>
            <h2>Elena Rodriguez</h2>
            <p>With over 15 years of experience in elite gymnastics, Coach Elena brings a wealth of knowledge and a passionate teaching style to the academy. Formerly a national competitor, she specializes in advanced routines and mental conditioning.</p>
            <div style="margin-top: 24px;">
                <span class="badge badge-success" style="margin-right: 8px;">USAG Certified</span>
                <span class="badge badge-success">Safesport Trained</span>
            </div>
        </div>
    </div>
</section>

<section class="section" style="background: var(--secondary-bg);">
    <div class="container text-center">
        <div class="section-title">
            <span class="subheading">Training Staff</span>
            <h2>Expert Instructors</h2>
        </div>
        <div class="grid grid-cols-3 gap-6">
            <div class="card premium-card text-center">
                <div style="width: 120px; height: 120px; border-radius: 50%; overflow: hidden; margin: 0 auto 24px; border: 4px solid var(--primary-accent);">
                    <img src="assets/images/about_mission_1781704820711.png" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <h3>Marcus Johnson</h3>
                <p style="color: var(--primary-accent); margin-bottom: 16px;">Acrobatics Director</p>
                <p>Specializes in high-level tumbling and power acrobatics.</p>
            </div>
            <div class="card premium-card text-center">
                <div style="width: 120px; height: 120px; border-radius: 50%; overflow: hidden; margin: 0 auto 24px; border: 4px solid var(--primary-accent);">
                    <img src="assets/images/competition_team_1781703638660.png" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <h3>Sarah Davis</h3>
                <p style="color: var(--primary-accent); margin-bottom: 16px;">Preschool Coordinator</p>
                <p>Expert in early childhood motor development and beginner gymnastics.</p>
            </div>
            <div class="card premium-card text-center">
                <div style="width: 120px; height: 120px; border-radius: 50%; overflow: hidden; margin: 0 auto 24px; border: 4px solid var(--primary-accent);">
                    <img src="assets/images/hero_gymnastics_beam_1781703585231.png" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <h3>David Lee</h3>
                <p style="color: var(--primary-accent); margin-bottom: 16px;">Competitive Team Coach</p>
                <p>Focuses on precision, form, and competitive routine mastery.</p>
            </div>
        </div>
    </div>
</section>

<section class="section container">
    <div class="grid grid-cols-2 gap-8 items-center flex-md-col-reverse">
        <div>
            <h2>Certifications & Awards</h2>
            <p>Our facility and staff maintain the highest level of accreditations in the sport.</p>
            <ul class="custom-list" style="margin-top: 24px;">
                <li>USA Gymnastics Member Club</li>
                <li>Positive Coaching Alliance Partner</li>
                <li>State Excellence in Coaching Award 2025</li>
            </ul>
        </div>
        <div class="card" style="background: var(--primary-accent); color: white; padding: 48px; text-align: center;">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-bottom: 24px;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            <h3 style="color: white;">Committed to Excellence</h3>
            <p style="color: rgba(255,255,255,0.8);">We continuously invest in coach education to provide the best training methods.</p>
        </div>
    </div>
</section>
""" + get_footer()

with open(os.path.join(root_dir, "coaches.html"), "w", encoding="utf-8") as f:
    f.write(coaches_content)

print("Pages created")
