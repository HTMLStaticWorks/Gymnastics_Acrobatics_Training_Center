css_to_add = """

/* =========================================
   NEW PREMIUM SECTIONS CSS
   ========================================= */

/* 1. Bento Grid */
.bento-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, 250px);
    gap: 16px;
}
.bento-item {
    position: relative;
    border-radius: var(--border-radius-lg);
    overflow: hidden;
    background: var(--card-bg);
    border: 1px solid var(--border-color);
}
.bento-large {
    grid-column: span 2;
    grid-row: span 2;
}
.bento-tall {
    grid-column: span 1;
    grid-row: span 2;
}
.bento-small {
    grid-column: span 1;
    grid-row: span 1;
}
.bento-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
}
.bento-item:hover .bento-img {
    transform: scale(1.05);
}
.bento-content {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 24px;
    background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
    color: white;
    transform: translateY(20px);
    opacity: 0;
    transition: all 0.4s ease;
}
.bento-item:hover .bento-content {
    transform: translateY(0);
    opacity: 1;
}
.bento-content h3 { margin: 0 0 8px 0; color: white; }
.bento-content p { margin: 0; font-size: 14px; opacity: 0.9; }
.bento-content-center {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    text-align: center;
    padding: 24px;
}

@media (max-width: 1024px) {
    .bento-grid {
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: auto;
    }
    .bento-large { grid-column: span 2; grid-row: span 1; height: 300px; }
    .bento-tall { grid-column: span 1; grid-row: span 1; height: 250px; }
    .bento-small { height: 250px; }
}
@media (max-width: 768px) {
    .bento-grid { grid-template-columns: 1fr; }
    .bento-large, .bento-tall, .bento-small { grid-column: span 1; grid-row: span 1; height: 250px; }
    .bento-content { transform: translateY(0); opacity: 1; }
}

/* 2. Infinite Marquee */
.marquee-container {
    width: 100%;
    display: flex;
    overflow: hidden;
    position: relative;
    padding: 24px 0;
}
.marquee-container::before, .marquee-container::after {
    content: '';
    position: absolute;
    top: 0;
    width: 100px;
    height: 100%;
    z-index: 2;
    pointer-events: none;
}
.marquee-container::before {
    left: 0;
    background: linear-gradient(to right, var(--secondary-bg), transparent);
}
.marquee-container::after {
    right: 0;
    background: linear-gradient(to left, var(--secondary-bg), transparent);
}
.marquee-track {
    display: flex;
    gap: 24px;
    animation: marqueeScroll 20s linear infinite;
    width: max-content;
}
.marquee-track:hover {
    animation-play-state: paused;
}
@keyframes marqueeScroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(calc(-50% - 12px)); }
}
.testimonial-card {
    width: 400px;
    background: var(--card-bg);
    padding: 32px;
    border-radius: var(--border-radius-lg);
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border-color);
    flex-shrink: 0;
}
.quote-icon {
    font-size: 48px;
    color: var(--primary-accent);
    line-height: 1;
    margin-bottom: 16px;
    font-family: serif;
}
.testimonial-author {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-top: 24px;
}
.testimonial-author img, .author-avatar-placeholder {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    object-fit: cover;
}
.author-avatar-placeholder {
    background: var(--secondary-accent);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 20px;
}
.testimonial-author h4 { margin: 0; font-size: 16px; }
.testimonial-author span { font-size: 14px; color: var(--text-secondary); }
@media (max-width: 768px) {
    .testimonial-card { width: 300px; padding: 24px; }
}

/* 3. Glassmorphism Sections */
.glass-section {
    position: relative;
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    padding: 120px 0;
}
.glass-overlay {
    position: absolute;
    inset: 0;
    background: rgba(16, 24, 32, 0.75);
}
.glass-cards-container {
    display: flex;
    gap: 40px;
    justify-content: center;
    margin-top: 64px;
}
.glass-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: var(--border-radius-lg);
    overflow: hidden;
    width: 350px;
    color: white;
    transition: transform 0.4s ease;
}
.glass-card:hover {
    transform: translateY(-10px);
    background: rgba(255, 255, 255, 0.15);
}
.glass-card.float-up { animation: floatVertical 6s ease-in-out infinite; }
.glass-card.float-down { animation: floatVertical 6s ease-in-out infinite reverse; }
@keyframes floatVertical {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-15px); }
}
.glass-card:hover { animation-play-state: paused; }
.glass-card-img {
    width: 100%;
    height: 300px;
    object-fit: cover;
}
.glass-card-info {
    padding: 24px;
}
.glass-card-info h3 { color: white; margin-bottom: 8px; }
.glass-badge {
    display: inline-block;
    background: rgba(231, 111, 81, 0.2);
    color: var(--primary-accent);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 16px;
    border: 1px solid rgba(231, 111, 81, 0.4);
}
@media (max-width: 768px) {
    .glass-cards-container { flex-direction: column; align-items: center; gap: 24px; }
    .glass-section { background-attachment: scroll; }
}

/* 4. Sticky Scroll */
.sticky-layout {
    display: flex;
    gap: 64px;
    align-items: flex-start;
}
.sticky-sidebar {
    flex: 1;
    position: sticky;
    top: 120px;
}
.sticky-content {
    flex: 1.5;
    display: flex;
    flex-direction: column;
    gap: 32px;
}
.sticky-card {
    background: var(--card-bg);
    padding: 48px;
    border-radius: var(--border-radius-lg);
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border-color);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}
.sticky-card:hover {
    transform: translateX(10px);
    box-shadow: var(--shadow-md);
    border-color: var(--primary-accent);
}
.sticky-icon {
    width: 64px;
    height: 64px;
    background: rgba(231, 111, 81, 0.1);
    color: var(--primary-accent);
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    margin-bottom: 24px;
}
[dir="rtl"] .sticky-card:hover { transform: translateX(-10px); }
@media (max-width: 1024px) {
    .sticky-layout { flex-direction: column; }
    .sticky-sidebar { position: static; margin-bottom: 40px; }
}

"""

css_file = r'd:\OFFICE\LIVE\JUNE[16-06-26]\Gymnastics & Acrobatics Training Center\assets\css\home.css'

with open(css_file, 'a', encoding='utf-8') as f:
    f.write(css_to_add)

print("home.css updated successfully!")
