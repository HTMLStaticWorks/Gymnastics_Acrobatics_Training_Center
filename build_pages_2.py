import os

root_dir = r"d:\OFFICE\LIVE\JUNE[16-06-26]\Gymnastics & Acrobatics Training Center"

with open(os.path.join(root_dir, "index.html"), "r", encoding="utf-8") as f:
    index_content = f.read()

nav_start = index_content.find('<!-- Navbar -->')
nav_end = index_content.find('<!-- Hero Section -->')
navbar = index_content[nav_start:nav_end]

footer_start = index_content.find('<footer')
footer_end = index_content.find('</body>')
footer = index_content[footer_start:footer_end]

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

# programs.html
programs_content = get_header("Programs") + """
<header class="page-hero container" style="text-align: center; padding-top: 160px; padding-bottom: 60px;">
    <span class="subheading">Our Curriculum</span>
    <h1 style="margin-bottom: 24px;">Gymnastics Programs</h1>
    <p style="max-width: 600px; margin: 0 auto;">Comprehensive training options for all ages and skill levels, designed to foster growth and athletic excellence.</p>
</header>

<section class="section container">
    <div class="grid grid-cols-2 gap-8 items-center">
        <div>
            <span class="subheading">Early Development</span>
            <h2>Preschool & Beginner</h2>
            <p>Our early development programs focus on fundamental movement skills, balance, and spatial awareness in a fun, safe environment.</p>
            <ul class="custom-list" style="margin-top: 24px;">
                <li>Ages 3-9 years old</li>
                <li>Focus on fun and basic motor skills</li>
                <li>Introduction to equipment safety</li>
            </ul>
        </div>
        <div class="image-reveal-wrapper">
            <img src="assets/images/preschool_gymnastics_1781703621250.png" alt="Preschool Gymnastics" class="rounded-image shadow-img" style="width: 100%; border-radius: var(--border-radius-lg);">
        </div>
    </div>
</section>

<section class="section" style="background: var(--secondary-bg);">
    <div class="container grid grid-cols-2 gap-8 items-center flex-md-col-reverse">
        <div class="image-reveal-wrapper" style="animation-delay: 0.2s;">
            <img src="assets/images/acrobatics_tumbling_1781703603597.png" alt="Advanced Acrobatics" class="rounded-image shadow-img" style="width: 100%; border-radius: var(--border-radius-lg);">
        </div>
        <div>
            <span class="subheading">Skill Mastery</span>
            <h2>Advanced Acrobatics</h2>
            <p>For athletes ready to take their skills to the next level. This program focuses on complex tumbling sequences, aerial maneuvers, and high-level acrobatic combinations.</p>
            <ul class="custom-list" style="margin-top: 24px;">
                <li>Pre-requisite skill assessment required</li>
                <li>Intensive conditioning and flexibility training</li>
                <li>Mastery of complex skills safely</li>
            </ul>
        </div>
    </div>
</section>

<section class="section container">
    <div class="grid grid-cols-2 gap-8 items-center">
        <div>
            <span class="subheading">Elite Competition</span>
            <h2>Competitive Teams</h2>
            <p>Our competitive team program is designed for athletes who demonstrate exceptional talent, dedication, and a desire to compete at state, regional, and national levels.</p>
            <a href="contact.html" class="btn btn-primary" style="margin-top: 24px;">Request Team Tryout</a>
        </div>
        <div class="image-reveal-wrapper" style="animation-delay: 0.4s;">
            <img src="assets/images/competition_team_1781703638660.png" alt="Competition Team" class="rounded-image shadow-img" style="width: 100%; border-radius: var(--border-radius-lg);">
        </div>
    </div>
</section>
""" + get_footer()

with open(os.path.join(root_dir, "programs.html"), "w", encoding="utf-8") as f:
    f.write(programs_content)


# progression-framework.html
framework_content = get_header("Progression Framework") + """
<header class="page-hero container" style="text-align: center; padding-top: 160px; padding-bottom: 60px;">
    <span class="subheading">The Journey</span>
    <h1 style="margin-bottom: 24px;">Progression Framework</h1>
    <p style="max-width: 600px; margin: 0 auto;">Our structured milestone system ensures every athlete builds a solid foundation before advancing to complex skills.</p>
</header>

<section class="section container text-center">
    <h2>Beginner to Advanced Pathway</h2>
    <p style="max-width: 800px; margin: 0 auto 48px;">We break down complex skills into manageable, achievable steps. This builds confidence and ensures safety at every level.</p>
    
    <div class="grid grid-cols-4 gap-6">
        <div class="card premium-card">
            <h3 style="color: var(--primary-accent);">Level 1</h3>
            <p style="font-weight: 500; margin-bottom: 16px;">Foundation</p>
            <p style="font-size: 14px;">Forward rolls, cartwheel prep, balance basics.</p>
        </div>
        <div class="card premium-card">
            <h3 style="color: var(--primary-accent);">Level 2</h3>
            <p style="font-weight: 500; margin-bottom: 16px;">Core Skills</p>
            <p style="font-size: 14px;">Handstands, bridges, pullover on bars.</p>
        </div>
        <div class="card premium-card">
            <h3 style="color: var(--primary-accent);">Level 3</h3>
            <p style="font-weight: 500; margin-bottom: 16px;">Intermediate</p>
            <p style="font-size: 14px;">Back handspring prep, aerial awareness.</p>
        </div>
        <div class="card premium-card">
            <h3 style="color: var(--primary-accent);">Level 4+</h3>
            <p style="font-weight: 500; margin-bottom: 16px;">Advanced</p>
            <p style="font-size: 14px;">Full twisting layouts, elite tumbling passes.</p>
        </div>
    </div>
</section>

<section class="section" style="background: var(--secondary-bg);">
    <div class="container grid grid-cols-2 gap-8 items-center">
        <div class="image-reveal-wrapper">
            <img src="assets/images/hero_gymnastics_beam_1781703585231.png" alt="Skill Milestones" class="rounded-image shadow-img" style="width: 100%; border-radius: var(--border-radius-lg);">
        </div>
        <div>
            <span class="subheading">Assessment</span>
            <h2>Skill Milestones</h2>
            <p>Every athlete undergoes regular skill assessments. These are positive, encouraging evaluations designed to celebrate what they've mastered and identify what they are ready to learn next.</p>
            <ul class="custom-list" style="margin-top: 24px;">
                <li>Quarterly formal assessments</li>
                <li>Continuous coach feedback via Dashboard</li>
                <li>Positive reinforcement focus</li>
            </ul>
        </div>
    </div>
</section>

<section class="section container text-center">
    <div class="card shadow-lg" style="padding: 64px; background: var(--card-bg);">
        <h2>Certification Roadmap</h2>
        <p style="max-width: 600px; margin: 0 auto 32px;">Athletes earn official academy certificates and badges upon completing each level, which are proudly displayed in their Parent Dashboard.</p>
        <a href="register.html" class="btn btn-primary">Start Your Journey</a>
    </div>
</section>
""" + get_footer()

with open(os.path.join(root_dir, "progression-framework.html"), "w", encoding="utf-8") as f:
    f.write(framework_content)


# pricing.html
pricing_content = get_header("Pricing") + """
<header class="page-hero container" style="text-align: center; padding-top: 160px; padding-bottom: 60px;">
    <span class="subheading">Investment</span>
    <h1 style="margin-bottom: 24px;">Tuition & Pricing</h1>
    <p style="max-width: 600px; margin: 0 auto;">Transparent pricing for premium gymnastics instruction. No hidden fees.</p>
</header>

<section class="section container">
    <div class="section-title text-center">
        <h2>Monthly Training Plans</h2>
        <p>Choose the frequency that fits your child's goals and schedule.</p>
    </div>
    
    <div class="grid grid-cols-3 gap-8">
        <div class="card pricing-card hover-lift">
            <h3>Recreational</h3>
            <p>Perfect for beginners</p>
            <div class="price-display">$120<span>/mo</span></div>
            <ul class="custom-list" style="text-align: left; margin: 24px 0 32px;">
                <li>1 Class per week</li>
                <li>Access to Parent Dashboard</li>
                <li>Quarterly skill assessment</li>
                <li>Academy T-shirt</li>
            </ul>
            <a href="register.html" class="btn btn-outline btn-block">Select Plan</a>
        </div>
        
        <div class="card pricing-card popular hover-lift" style="border-color: var(--primary-accent); box-shadow: var(--shadow-lg);">
            <h3>Development</h3>
            <p>Accelerated learning</p>
            <div class="price-display">$210<span>/mo</span></div>
            <ul class="custom-list" style="text-align: left; margin: 24px 0 32px;">
                <li>2 Classes per week</li>
                <li>Access to Parent Dashboard</li>
                <li>Priority class registration</li>
                <li>Monthly progress updates</li>
            </ul>
            <a href="register.html" class="btn btn-primary btn-block">Select Plan</a>
        </div>
        
        <div class="card pricing-card hover-lift">
            <h3>Intensive</h3>
            <p>For dedicated athletes</p>
            <div class="price-display">$280<span>/mo</span></div>
            <ul class="custom-list" style="text-align: left; margin: 24px 0 32px;">
                <li>3+ Classes per week</li>
                <li>Open gym access</li>
                <li>1-on-1 coach review</li>
                <li>Competition prep</li>
            </ul>
            <a href="register.html" class="btn btn-outline btn-block">Select Plan</a>
        </div>
    </div>
</section>

<section class="section" style="background: var(--secondary-bg);">
    <div class="container text-center">
        <h2>Seasonal & Competitive Packages</h2>
        <p style="max-width: 600px; margin: 0 auto 48px;">We also offer specialized summer camps and competitive team tracking packages. Contact our administrative team for a custom assessment and quote for Elite Competition Teams.</p>
        <a href="contact.html" class="btn btn-primary">Contact Administration</a>
    </div>
</section>
""" + get_footer()

with open(os.path.join(root_dir, "pricing.html"), "w", encoding="utf-8") as f:
    f.write(pricing_content)

print("Remaining pages created")
