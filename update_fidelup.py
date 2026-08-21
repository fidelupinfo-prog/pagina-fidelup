import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update CSS
css_additions = """
        /* MOBILE MENU & ACCESSIBILITY */
        .mobile-menu-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100vh; height: 100dvh;
            background: rgba(250, 250, 250, 0.98); backdrop-filter: blur(10px);
            z-index: 2000; display: flex; flex-direction: column;
            padding: 24px; transform: translateX(100%); transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            visibility: hidden;
        }
        .mobile-menu-overlay.open { transform: translateX(0); visibility: visible; }
        .mobile-menu-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; }
        .mobile-menu-close { font-size: 2rem; background: none; border: none; cursor: pointer; color: var(--text-dark); padding: 8px; }
        .mobile-menu-links { display: flex; flex-direction: column; gap: 32px; font-size: 1.5rem; font-weight: 700; }
        .mobile-menu-links a { text-decoration: none; color: var(--text-dark); transition: color 0.2s; }
        .mobile-menu-links a:hover { color: var(--primary); }
        body.menu-open { overflow: hidden; }

        /* SCROLL MARGIN FOR FIXED HEADER */
        section { scroll-margin-top: 90px; }

        /* RESPONSIVE FORM GRID */
        .form-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }

        /* REDUCED MOTION */
        @media (prefers-reduced-motion: reduce) {
            *, ::before, ::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; }
        }

        /* SAFE AREA PADDING */
        .container { padding-left: max(24px, env(safe-area-inset-left)); padding-right: max(24px, env(safe-area-inset-right)); }
"""
content = content.replace("/* Typography */", css_additions + "\n        /* Typography */")

# 2. Update Media Queries
media_query_replacements = """
        @media (max-width: 992px) {
            .nav-links { display: none; }
            .mobile-menu-btn { display: block; padding: 8px; }
            .hero-mascot { width: 140px; }
            .interaction-stage { flex-direction: column; gap: 30px; }
            .stage-arrow { transform: rotate(90deg); }
            .vantaggio-showcase { flex-direction: column; align-items: center; }
            .ricevi-grid, .split-actions, .vs-container, .esempi-wrapper, .cta-grid { grid-template-columns: 1fr; gap: 40px; }
            .pricing-cards { grid-template-columns: 1fr; gap: 20px; }
            .split-actions { flex-direction: column; }
            .vs-container { flex-direction: column; }
            .esempi-wrapper { flex-direction: column-reverse; }
            .tab-btn { padding: 16px; font-size: 1.2rem; }
            .tab-btn.active { transform: translateX(8px); }
            .esempi-content { padding: 32px 24px; }
            .free-month-banner { flex-direction: column; text-align: center; padding: 40px 24px; gap: 20px; }
            .price-strike { font-size: 3rem; }
            .price-free { font-size: 4rem; }
            h1 { font-size: clamp(2.2rem, 8vw, 3rem); }
            h2 { font-size: clamp(1.8rem, 7vw, 2.5rem); }
            .story-section { padding: 60px 0; }
            .form-grid-2 { grid-template-columns: 1fr; gap: 0; }
            .mech-card { padding: 32px 24px; }
            .client-nodes { gap: 16px; }
            .c-node { width: 80px; height: 80px; font-size: 1.8rem; }
            .c-node::after { font-size: 0.8rem; bottom: -24px; }
            .p-card { padding: 32px 24px; }
            .footer-links { flex-direction: column; gap: 16px; }
            .cta-grid { text-align: center; }
            .form-box { padding: 32px 24px; }
        }
"""
content = re.sub(r'@media \(max-width: 992px\) \{.*?\}(?=\s*</style>)', media_query_replacements, content, flags=re.DOTALL)

# 3. Update Mech Grid minmax and sizes
content = content.replace("grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));", "grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr));")

# 4. Mobile Menu HTML injection
mobile_menu_html = """
    <button class="mobile-menu-btn" id="open-menu-btn" aria-expanded="false" aria-controls="mobile-menu" aria-label="Apri menu">☰</button>
        </div>
    </header>

    <!-- MOBILE MENU OVERLAY -->
    <div class="mobile-menu-overlay" id="mobile-menu" aria-hidden="true">
        <div class="mobile-menu-header">
            <a href="#" class="logo" style="color: var(--primary-dark);">
                <img src="assets/nino.png" alt="" style="width: 32px;">
                FidelUp
            </a>
            <button class="mobile-menu-close" id="close-menu-btn" aria-label="Chiudi menu">✕</button>
        </div>
        <nav class="mobile-menu-links">
            <a href="#storia" class="mobile-link">Come funziona</a>
            <a href="#meccanismi" class="mobile-link">Programmi</a>
            <a href="#ricevi" class="mobile-link">Cosa ricevi</a>
            <a href="#pricing" class="mobile-link">Prezzi</a>
            <a href="#faq" class="mobile-link">FAQ</a>
            <a href="#prenota" class="btn btn-primary mobile-link" style="text-align: center; margin-top: 24px;">Prenota visita</a>
        </nav>
    </div>
"""
content = content.replace('<button class="mobile-menu-btn">☰</button>\n        </div>\n    </header>', mobile_menu_html)

# 5. Form HTML updates (Autocomplete, Grids, Checkbox)
form_html_old = """                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                            <div class="form-group">
                                <label>Città</label>
                                <input type="text" id="citta" required placeholder="Es. Roma">
                            </div>
                            <div class="form-group">
                                <label>Tipo di attività</label>
                                <input type="text" id="tipo" required placeholder="Es. Barbiere">
                            </div>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                            <div class="form-group">
                                <label>Telefono</label>
                                <input type="tel" id="telefono" required placeholder="333 123 4567">
                            </div>
                            <div class="form-group">
                                <label>Email</label>
                                <input type="email" id="email" required placeholder="mario@email.com">
                            </div>
                        </div>"""
form_html_new = """                        <div class="form-grid-2">
                            <div class="form-group">
                                <label for="citta">Città</label>
                                <input type="text" id="citta" required placeholder="Es. Roma" autocomplete="address-level2">
                            </div>
                            <div class="form-group">
                                <label for="tipo">Tipo di attività</label>
                                <input type="text" id="tipo" required placeholder="Es. Barbiere" autocomplete="organization-title">
                            </div>
                        </div>
                        <div class="form-grid-2">
                            <div class="form-group">
                                <label for="telefono">Telefono</label>
                                <input type="tel" id="telefono" required placeholder="333 123 4567" autocomplete="tel">
                            </div>
                            <div class="form-group">
                                <label for="email">Email</label>
                                <input type="email" id="email" required placeholder="mario@email.com" autocomplete="email">
                            </div>
                        </div>"""
content = content.replace(form_html_old, form_html_new)
content = content.replace('<label>Nome e Cognome</label>\n                            <input type="text" id="nome" required placeholder="Es. Mario Rossi">', '<label for="nome">Nome e Cognome</label>\n                            <input type="text" id="nome" required placeholder="Es. Mario Rossi" autocomplete="name">')
content = content.replace('<label>Nome Attività</label>\n                            <input type="text" id="attivita" required placeholder="Es. Barberia Il Taglio">', '<label for="attivita">Nome Attività</label>\n                            <input type="text" id="attivita" required placeholder="Es. Barberia Il Taglio" autocomplete="organization">')

gdpr_checkbox = """
                        <div class="form-group" style="margin-top: 16px;">
                            <label style="display:flex; gap:12px; font-weight:normal; font-size:0.95rem; align-items:flex-start; text-align: left; cursor: pointer;">
                                <input type="checkbox" id="privacy" required style="width:24px; height:24px; flex-shrink:0; cursor: pointer; accent-color: var(--primary);">
                                <span style="line-height: 1.4; color: var(--text-muted);">Acconsento al trattamento dei dati personali ai fini del contatto, nel rispetto della <a href="#privacy-policy" style="color:var(--primary); text-decoration:underline;">Privacy Policy</a>.</span>
                            </label>
                        </div>
"""
content = content.replace('<button type="submit" id="submitBtn"', gdpr_checkbox + '\n                        <button type="submit" id="submitBtn"')

# 6. Form JS Logic Update
js_logic_old = """            try {
                await fetch(WEBHOOK_URL, {
                    method: 'POST',
                    mode: 'no-cors',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                msgDiv.innerHTML = '✅ <strong>Richiesta ricevuta.</strong><br>Ti contatteremo per concordare la visita gratuita.';
                msgDiv.style.backgroundColor = '#E8F5E9';
                msgDiv.style.color = '#1B5E20';
                msgDiv.style.display = 'block';
                
                form.reset();
                btn.textContent = 'Prenota visita gratuita';
                btn.disabled = false;
                btn.style.opacity = '1';
                
            } catch (error) {"""
js_logic_new = """            try {
                // Nota Técnica: Se usa 'no-cors' por las restricciones de Google Apps Script.
                // En este modo, la respuesta HTTP es opaca (status 0), por lo que no podemos leer el body real.
                // Si fetch no lanza un error de red (TypeError), asumimos que la petición fue entregada.
                await fetch(WEBHOOK_URL, {
                    method: 'POST',
                    mode: 'no-cors',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                msgDiv.innerHTML = '✅ <strong>Richiesta inviata.</strong><br>I tuoi dati sono stati ricevuti. Ti contatteremo a breve per concordare la visita gratuita.';
                msgDiv.style.backgroundColor = '#E8F5E9';
                msgDiv.style.color = '#1B5E20';
                msgDiv.style.display = 'block';
                msgDiv.setAttribute("role", "alert");
                
                form.reset();
                btn.textContent = 'Richiesta inviata ✓';
                // Dejamos el botón deshabilitado unos segundos para evitar doble envío
                setTimeout(() => {
                    btn.disabled = false;
                    btn.textContent = 'Prenota nuova visita';
                    btn.style.opacity = '1';
                }, 5000);
                
            } catch (error) {"""
content = content.replace(js_logic_old, js_logic_new)

# 7. Mobile Menu JS Logic
mobile_menu_js = """
        // MOBILE MENU LOGIC
        const mobileMenuBtn = document.getElementById('open-menu-btn');
        const closeMenuBtn = document.getElementById('close-menu-btn');
        const mobileMenuOverlay = document.getElementById('mobile-menu');
        const mobileLinks = document.querySelectorAll('.mobile-link');

        function openMenu() {
            mobileMenuOverlay.classList.add('open');
            mobileMenuOverlay.setAttribute('aria-hidden', 'false');
            mobileMenuBtn.setAttribute('aria-expanded', 'true');
            document.body.classList.add('menu-open');
        }

        function closeMenu() {
            mobileMenuOverlay.classList.remove('open');
            mobileMenuOverlay.setAttribute('aria-hidden', 'true');
            mobileMenuBtn.setAttribute('aria-expanded', 'false');
            document.body.classList.remove('menu-open');
        }

        if(mobileMenuBtn) mobileMenuBtn.addEventListener('click', openMenu);
        if(closeMenuBtn) closeMenuBtn.addEventListener('click', closeMenu);
        mobileLinks.forEach(link => {
            link.addEventListener('click', closeMenu);
        });
        
        // Close on click outside
        mobileMenuOverlay.addEventListener('click', (e) => {
            if (e.target === mobileMenuOverlay) closeMenu();
        });
"""
content = content.replace("// GSAP SCROLL STORYTELLING", mobile_menu_js + "\n\n        // GSAP SCROLL STORYTELLING")

# 8. Mascot Optimization JS (Disable heavy animations on small screens)
gsap_matchmedia_js = """
        // GSAP SCROLL STORYTELLING with MatchMedia for Mobile Performance
        gsap.registerPlugin(ScrollTrigger);
        let mm = gsap.matchMedia();

        mm.add("(min-width: 993px)", () => {
            // DESKTOP ANIMATIONS
            gsap.from("#hero-mascot", { y: 50, opacity: 0, duration: 1, ease: "power3.out" });
            gsap.from("#hero-title", { y: 30, opacity: 0, duration: 1, delay: 0.2, ease: "power3.out" });
            gsap.from("#hero-sub", { y: 20, opacity: 0, duration: 1, delay: 0.4, ease: "power3.out" });
            gsap.from("#hero-btn", { scale: 0.9, opacity: 0, duration: 1, delay: 0.6, ease: "back.out(1.5)" });

            gsap.to(".hero-content", { y: 100, opacity: 0, scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } });

            const tlProb = gsap.timeline({ scrollTrigger: { trigger: ".scene-problem", start: "top center", end: "center center", scrub: 1 } });
            tlProb.from(".gsap-prob-text", { opacity: 0, y: 50 })
                  .from(".gsap-c1", { opacity: 0, scale: 0, duration: 0.5 })
                  .from(".gsap-c2", { opacity: 0, scale: 0, duration: 0.5 })
                  .from(".gsap-c3", { opacity: 0, scale: 0, duration: 0.5 })
                  .to(".gsap-c3", { opacity: 0.3, filter: "grayscale(1)", duration: 0.5 })
                  .from(".gsap-prob-sol", { opacity: 0, scale: 0.9, duration: 1 });

            const tlFidel = gsap.timeline({ scrollTrigger: { trigger: ".scene-fidelup", start: "top 70%", end: "center center", scrub: 1 } });
            tlFidel.from(".gsap-fidel-title", { opacity: 0, y: -30 })
                   .from(".gsap-stage-1", { opacity: 0, x: -50 })
                   .from(".gsap-stage-arr1", { opacity: 0, scale: 0 })
                   .from(".gsap-stage-2", { opacity: 0, y: 50 })
                   .from(".gsap-stage-arr2", { opacity: 0, scale: 0 })
                   .from(".gsap-stage-3", { opacity: 0, x: 50 });

            gsap.from(".gsap-vcard", { y: 100, opacity: 0, stagger: 0.2, scrollTrigger: { trigger: ".scene-vantaggio", start: "top 60%", end: "center center", scrub: 1 } });

            const tlRel = gsap.timeline({ scrollTrigger: { trigger: ".scene-relazione", start: "top 80%", end: "center center", scrub: 1 } });
            tlRel.from(".gsap-rel-1", { opacity: 0, x: -50 }).from(".gsap-rel-2", { opacity: 0, scale: 0.8 }).from(".gsap-rel-3", { opacity: 0, x: 50, color: "#2E7D32" });
        });

        mm.add("(max-width: 992px)", () => {
            // MOBILE ANIMATIONS (Simplified for performance and UX)
            gsap.from("#hero-mascot", { opacity: 0, duration: 0.8 });
            gsap.from("#hero-title, #hero-sub, #hero-btn", { opacity: 0, y: 20, duration: 0.8, stagger: 0.1, delay: 0.3 });
            
            // Only simple fade-ins for mobile scrolling
            gsap.utils.toArray('.story-section').forEach(section => {
                gsap.from(section.children, {
                    opacity: 0, y: 30, duration: 0.8, stagger: 0.1,
                    scrollTrigger: { trigger: section, start: "top 85%" }
                });
            });
        });
"""
# Need to replace the old GSAP block with the new matchMedia block
old_gsap_start = "// GSAP SCROLL STORYTELLING"
old_gsap_end = "// FORM SUBMISSION (REAL WEBHOOK)"
import sys
start_idx = content.find(old_gsap_start)
end_idx = content.find(old_gsap_end)
if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + gsap_matchmedia_js + "\n        " + content[end_idx:]

with open("index.html", "w") as f:
    f.write(content)

print("Updated successfully!")
