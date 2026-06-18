import re

html_file = r'd:\OFFICE\LIVE\JUNE[16-06-26]\Gymnastics & Acrobatics Training Center\index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to insert the new sections before the <footer tag.
new_sections = """

    <!-- 1. Facility Bento Grid -->
    <section class="section container">
        <div class="section-title">
            <span class="subheading">World-Class Equipment</span>
            <h2>Interactive Facility Tour</h2>
        </div>
        <div class="bento-grid">
            <div class="bento-item bento-large">
                <img src="assets/images/facility_spring_floor.png" alt="Spring Floor" class="bento-img">
                <div class="bento-content">
                    <h3>Olympic Spring Floor</h3>
                    <p>Train safely on our premium resilient surfaces.</p>
                </div>
            </div>
            <div class="bento-item bento-tall">
                <img src="assets/images/gymnastics_chalk_hands.png" alt="Chalk Hands" class="bento-img">
                <div class="bento-content">
                    <h3>Professional Grip</h3>
                    <p>High-grade chalk stations everywhere.</p>
                </div>
            </div>
            <div class="bento-item bento-small">
                <div class="bento-content-center">
                    <h3 style="font-size: 32px; color: var(--primary-accent); margin-bottom: 8px;">15,000</h3>
                    <p>Sq Ft. Facility</p>
                </div>
            </div>
            <div class="bento-item bento-small" style="background: var(--secondary-accent); color: white;">
                <div class="bento-content-center">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-bottom: 12px;"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                    <p style="color: white; margin: 0; font-weight: 600;">Safety First</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. Infinite Marquee -->
    <section class="section" style="background-color: var(--secondary-bg); overflow: hidden;">
        <div class="section-title">
            <span class="subheading">Success Stories</span>
            <h2>Hear From Our Community</h2>
        </div>
        <div class="marquee-container">
            <div class="marquee-track">
                <!-- Testimonial 1 -->
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <p>"The coaching staff is incredible. My daughter has progressed from cartwheels to back handsprings in just six months!"</p>
                    <div class="testimonial-author">
                        <img src="assets/images/gymnast_gold_medal.png" alt="Avatar">
                        <div>
                            <h4>Sarah Jenkins</h4>
                            <span>Parent of Level 3 Gymnast</span>
                        </div>
                    </div>
                </div>
                <!-- Testimonial 2 -->
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <p>"A safe, nurturing environment that pushes athletes to reach their true Olympic potential."</p>
                    <div class="testimonial-author">
                        <div class="author-avatar-placeholder">M</div>
                        <div>
                            <h4>Marcus T.</h4>
                            <span>Former Athlete</span>
                        </div>
                    </div>
                </div>
                <!-- Testimonial 3 -->
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <p>"We love the state-of-the-art facility. The foam pits make learning new release moves completely fearless."</p>
                    <div class="testimonial-author">
                        <div class="author-avatar-placeholder">L</div>
                        <div>
                            <h4>Laura B.</h4>
                            <span>Elite Parent</span>
                        </div>
                    </div>
                </div>
                <!-- Duplicate for Infinite Loop -->
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <p>"The coaching staff is incredible. My daughter has progressed from cartwheels to back handsprings in just six months!"</p>
                    <div class="testimonial-author">
                        <img src="assets/images/gymnast_gold_medal.png" alt="Avatar">
                        <div>
                            <h4>Sarah Jenkins</h4>
                            <span>Parent of Level 3 Gymnast</span>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <p>"A safe, nurturing environment that pushes athletes to reach their true Olympic potential."</p>
                    <div class="testimonial-author">
                        <div class="author-avatar-placeholder">M</div>
                        <div>
                            <h4>Marcus T.</h4>
                            <span>Former Athlete</span>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <p>"We love the state-of-the-art facility. The foam pits make learning new release moves completely fearless."</p>
                    <div class="testimonial-author">
                        <div class="author-avatar-placeholder">L</div>
                        <div>
                            <h4>Laura B.</h4>
                            <span>Elite Parent</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Head Coaches -->
    <section class="section glass-section" style="background-image: url('assets/images/facility_spring_floor.png');">
        <div class="glass-overlay"></div>
        <div class="container" style="position: relative; z-index: 2;">
            <div class="section-title" style="color: white;">
                <span class="subheading" style="color: var(--primary-accent);">Elite Leadership</span>
                <h2 style="color: white;">Meet Our Head Coaches</h2>
            </div>
            
            <div class="glass-cards-container">
                <div class="glass-card float-up">
                    <img src="assets/images/coach_portrait_elite.png" alt="Coach Michael" class="glass-card-img">
                    <div class="glass-card-info">
                        <h3>Coach Michael</h3>
                        <span class="glass-badge">Olympic Finalist</span>
                        <p>Specializing in advanced tumbling and trampoline.</p>
                    </div>
                </div>
                <div class="glass-card float-down">
                    <img src="assets/images/coach_portrait_elite.png" alt="Coach Elena" class="glass-card-img" style="object-position: top;">
                    <div class="glass-card-info">
                        <h3>Coach Elena</h3>
                        <span class="glass-badge">National Champion</span>
                        <p>Focuses on balance beam and elegant floor routines.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Why Choose Us Sticky Scroll -->
    <section class="section container">
        <div class="sticky-layout">
            <div class="sticky-sidebar">
                <span class="subheading">Core Values</span>
                <h2>Why Choose GymnasticsAcademy?</h2>
                <p>We believe in a holistic approach to athletic development, ensuring each child receives the attention they need to safely grow their skills.</p>
                <a href="about.html" class="btn btn-outline" style="margin-top: 24px;">Learn More About Us</a>
            </div>
            <div class="sticky-content">
                <div class="sticky-card">
                    <div class="sticky-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
                    <h3>Uncompromising Safety</h3>
                    <p>Safety is our foundation. From USAG-certified coaches to foam block pits, every element is designed to minimize risk.</p>
                </div>
                <div class="sticky-card">
                    <div class="sticky-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 12l-4-4-4 4M12 8v8"/></svg></div>
                    <h3>Proven Methodology</h3>
                    <p>Our structured curriculum ensures consistent, measurable progress from the first forward roll to advanced aerials.</p>
                </div>
                <div class="sticky-card">
                    <div class="sticky-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg></div>
                    <h3>Fun & Engagement</h3>
                    <p>We maintain a positive, energetic atmosphere. A gymnast who loves the sport will naturally excel.</p>
                </div>
            </div>
        </div>
    </section>

"""

content = content.replace('<footer', new_sections + '<footer')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully!")
