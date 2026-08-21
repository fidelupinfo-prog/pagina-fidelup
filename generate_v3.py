import os

html_content = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FidelUp | Fai tornare i tuoi clienti. Al resto pensiamo noi.</title>
    <meta name="description" content="FidelUp è il servizio di fidelizzazione gestito per parrucchieri, centri estetici e attività locali. Installiamo e gestiamo il tuo programma fedeltà. Primo mese gratuito.">
    <meta name="keywords" content="fidelizzazione clienti, programma fedeltà, fidelizzazione parrucchieri, fidelizzazione centri estetici, fidelizzazione barberie, fidelizzazione negozi">
    <meta property="og:title" content="FidelUp | Fai tornare i tuoi clienti. Al resto pensiamo noi.">
    <meta property="og:description" content="Tu pensa al tuo lavoro. Noi pensiamo alla fidelizzazione. Scopri il servizio gestito FidelUp per la tua attività locale.">
    <meta property="og:type" content="website">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --primary: #2E7D32;
            --primary-light: #4CAF50;
            --primary-dark: #1B5E20;
            --surface: #FFFFFF;
            --surface-alt: #FAFAFA;
            --surface-green: #E8F5E9;
            --surface-green-alt: #C8E6C9;
            --text-main: #1A1A1A;
            --text-muted: #666666;
            --border: #E0E0E0;
            --shadow-sm: 0 2px 4px rgba(0,0,0,0.05);
            --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
            --shadow-lg: 0 10px 24px rgba(0,0,0,0.12);
            --transition: all 0.3s ease;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body { font-family: 'Inter', sans-serif; color: var(--text-main); background-color: var(--surface); line-height: 1.6; -webkit-font-smoothing: antialiased; }

        .container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
        .text-center { text-align: center; }
        .text-primary { color: var(--primary); }
        .bg-alt { background-color: var(--surface-alt); }
        .bg-green { background-color: var(--surface-green); }
        .bg-dark { background-color: var(--text-main); color: var(--surface); }
        .section-padding { padding: 90px 0; }
        
        h1, h2, h3, h4 { line-height: 1.2; letter-spacing: -0.02em; }
        h1 { font-size: clamp(2.5rem, 5vw, 3.8rem); font-weight: 900; }
        h2 { font-size: clamp(2rem, 4vw, 2.8rem); font-weight: 800; margin-bottom: 1.5rem; }
        h3 { font-size: 1.5rem; font-weight: 700; }
        .subtitle { font-size: 1.125rem; color: var(--text-muted); margin-bottom: 2rem; max-width: 800px; margin-inline: auto; line-height: 1.8; }

        .badge {
            display: inline-flex; align-items: center; padding: 6px 12px;
            background: var(--surface-green); color: var(--primary-dark);
            border-radius: 20px; font-size: 0.85rem; font-weight: 800;
            text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1.5rem;
            border: 1px solid var(--surface-green-alt);
        }

        .btn {
            display: inline-flex; align-items: center; justify-content: center;
            padding: 16px 32px; border-radius: 12px; font-weight: 800; font-size: 1rem;
            text-decoration: none; cursor: pointer; transition: var(--transition);
            border: 2px solid transparent;
        }
        .btn-primary { background-color: var(--primary); color: white; box-shadow: 0 4px 14px rgba(46,125,50,0.3); }
        .btn-primary:hover { background-color: var(--primary-dark); transform: translateY(-2px); box-shadow: 0 6px 20px rgba(46,125,50,0.4); }
        .btn-outline { background-color: transparent; color: var(--primary); border-color: var(--primary); }
        .btn-outline:hover { background-color: var(--surface-green); }

        .header { position: fixed; top: 0; left: 0; right: 0; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(8px); z-index: 100; border-bottom: 1px solid var(--border); }
        .header .container { display: flex; align-items: center; justify-content: space-between; height: 72px; }
        .logo { display: flex; align-items: center; gap: 8px; font-size: 1.5rem; font-weight: 900; color: var(--text-main); text-decoration: none; }
        .logo-icon { width: 36px; height: 36px; object-fit: contain; mix-blend-mode: multiply; }
        .nav-links { display: flex; gap: 28px; align-items: center; }
        .nav-links a { color: var(--text-muted); text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: color 0.2s; }
        .nav-links a:hover { color: var(--primary); }

        .hero { padding-top: 140px; padding-bottom: 80px; overflow: hidden; }
        .hero-grid { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 60px; align-items: center; }
        .hero-check { display: flex; align-items: center; gap: 8px; font-size: 0.95rem; font-weight: 600; color: var(--text-muted); margin-bottom: 8px; }
        .hero-check::before { content: '✓'; color: var(--primary); font-weight: 900; }
        
        .hero-visual-comp { position: relative; display: flex; justify-content: center; align-items: center; }
        .mascot-hero { width: 100%; max-width: 320px; z-index: 2; position: relative; mix-blend-mode: multiply; animation: float 4s ease-in-out infinite; filter: drop-shadow(0 20px 30px rgba(46,125,50,0.15)); }
        
        .mockup-card { position: absolute; background: white; border-radius: 16px; padding: 16px; box-shadow: var(--shadow-lg); z-index: 1; border: 1px solid var(--border); display: flex; align-items: center; gap: 12px; animation: float 5s ease-in-out infinite reverse; }
        .mockup-qr { top: 10%; right: -5%; }
        .mockup-phone { bottom: 10%; left: -5%; }
        .mockup-icon { width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; background: var(--surface-green); }

        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }

        .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px; margin-top: 48px; }
        .card { background: var(--surface); padding: 40px; border-radius: 24px; border: 1px solid var(--border); transition: var(--transition); height: 100%; }
        .card:hover { border-color: var(--primary-light); box-shadow: var(--shadow-lg); transform: translateY(-4px); }
        
        .mech-icon { width: 72px; height: 72px; border-radius: 20px; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; margin-bottom: 24px; }
        
        .vs-table { width: 100%; border-collapse: collapse; background: var(--surface); border-radius: 24px; overflow: hidden; box-shadow: var(--shadow-md); margin-top: 40px; }
        .vs-table th, .vs-table td { padding: 24px; text-align: left; border-bottom: 1px solid var(--border); }
        .vs-table th { background: var(--surface-alt); font-weight: 800; font-size: 1.1rem; }
        .vs-table th:last-child { background: var(--primary); color: white; }
        .vs-table td:last-child { background: var(--surface-green); font-weight: 600; color: var(--text-main); }
        
        /* Timeline */
        .timeline { display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; margin-top: 48px; align-items: center; }
        .timeline-step { background: var(--surface); padding: 20px 24px; border-radius: 16px; border: 1px solid var(--border); box-shadow: var(--shadow-sm); text-align: center; font-weight: 600; min-width: 140px; }
        .timeline-number { font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px; }
        .timeline-arrow { color: var(--primary); font-size: 1.5rem; font-weight: bold; }
        .timeline-step.highlight { background: var(--surface-green); border-color: var(--primary-light); color: var(--primary-dark); }

        /* Flow list */
        .flow-list { display: flex; align-items: center; gap: 12px; font-weight: 700; font-size: 0.9rem; background: var(--surface-alt); padding: 12px 16px; border-radius: 12px; display: inline-flex; margin-top: 20px; }
        .flow-list span { color: var(--text-muted); }

        /* Form */
        .form-container { background: var(--surface); border-radius: 24px; padding: 48px; box-shadow: var(--shadow-lg); max-width: 650px; margin: 0 auto; border: 1px solid var(--border); }
        .form-group { margin-bottom: 24px; text-align: left; }
        .form-label { display: block; font-weight: 700; margin-bottom: 8px; font-size: 0.95rem; }
        .form-input { width: 100%; padding: 14px 16px; border: 2px solid var(--border); border-radius: 12px; font-family: inherit; font-size: 1rem; transition: var(--transition); }
        .form-input:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 4px rgba(46,125,50,0.1); }
        
        /* Pricing */
        .pricing-card { background: var(--surface); border: 2px solid var(--border); border-radius: 24px; padding: 40px; text-align: left; transition: var(--transition); }
        .pricing-card.popular { border-color: var(--primary); box-shadow: 0 12px 30px rgba(46,125,50,0.15); position: relative; }
        .pricing-price { font-size: 2.8rem; font-weight: 900; margin: 16px 0; display: flex; align-items: baseline; }
        .pricing-price span { font-size: 1.1rem; color: var(--text-muted); font-weight: 600; margin-left: 6px; }
        .pricing-features { list-style: none; margin: 32px 0; }
        .pricing-features li { display: flex; gap: 12px; margin-bottom: 16px; color: var(--text-muted); font-size: 1rem; align-items: flex-start; }
        .pricing-features li::before { content: '✓'; color: var(--primary); font-weight: 900; font-size: 1.1rem; }

        /* FAQ */
        .faq-item { border-bottom: 1px solid var(--border); padding: 24px 0; text-align: left; }
        .faq-q { font-size: 1.25rem; font-weight: 700; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
        .faq-q span { color: var(--primary); font-size: 1.5rem; transition: transform 0.3s; }
        .faq-a { margin-top: 16px; color: var(--text-muted); display: none; line-height: 1.7; font-size: 1.05rem; }
        .faq-item.active .faq-a { display: block; }
        .faq-item.active .faq-q span { transform: rotate(45deg); }

        .target-pills { display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; margin-top: 40px; }
        .target-pill { background: var(--surface); border: 2px solid var(--border); padding: 14px 28px; border-radius: 40px; font-weight: 700; font-size: 1.1rem; box-shadow: var(--shadow-sm); }

        .floating-cta { position: fixed; bottom: 24px; right: 24px; z-index: 90; display: none; }
        .floating-cta.visible { display: block; }
        
        footer { background: var(--text-main); color: white; padding: 80px 0 40px; text-align: center; }
        .footer-links a { color: rgba(255,255,255,0.7); text-decoration: none; margin: 0 16px; font-size: 0.95rem; font-weight: 500; transition: color 0.2s; }
        .footer-links a:hover { color: white; }

        @media (max-width: 992px) {
            .hero-grid { grid-template-columns: 1fr; text-align: center; }
            .hero-check { justify-content: center; }
            .nav-links { display: none; }
            .mascot-hero { max-width: 280px; }
            .mockup-qr { right: 0; }
            .mockup-phone { left: 0; }
            .timeline { flex-direction: column; align-items: stretch; }
            .timeline-arrow { transform: rotate(90deg); margin: 8px auto; }
            .vs-table, .vs-table tbody, .vs-table tr, .vs-table td, .vs-table th { display: block; }
            .vs-table tr { margin-bottom: 24px; border: 1px solid var(--border); border-radius: 16px; overflow: hidden; }
            .vs-table th { display: none; }
            .vs-table td { padding: 20px; text-align: right; position: relative; }
            .vs-table td::before { content: attr(data-label); position: absolute; left: 20px; font-weight: 800; }
        }
    </style>
</head>
<body>

    <header class="header">
        <div class="container">
            <a href="#" class="logo">
                <img src="assets/nino.png" alt="Mascotte ufficiale FidelUp" class="logo-icon">
                Fidel<span>Up</span>
            </a>
            <nav class="nav-links">
                <a href="#soluzione">La Soluzione</a>
                <a href="#programmi">I Programmi</a>
                <a href="#servizio">Cosa Ricevi</a>
                <a href="#prezzi">Prezzi</a>
                <a href="#prenota" class="btn btn-primary" style="padding: 10px 20px; font-size: 0.95rem;">Prenota visita gratuita</a>
            </nav>
        </div>
    </header>

    <section class="hero bg-green">
        <div class="container hero-grid">
            <div>
                <div class="badge">SERVIZIO DI FIDELIZZAZIONE GESTITO</div>
                <h1>Fai tornare i tuoi clienti.<br><span class="text-primary">Al resto pensiamo noi.</span></h1>
                <p class="subtitle" style="margin-left: 0; text-align: left; max-width: 550px;">Installiamo e gestiamo il tuo programma di fidelizzazione. Tu continui a gestire il tuo lavoro senza dover imparare un nuovo software.</p>
                
                <div style="margin-bottom: 32px;">
                    <div class="hero-check">Primo mese gratuito</div>
                    <div class="hero-check">Installazione e configurazione inclusa</div>
                    <div class="hero-check">Assistenza diretta nel tuo locale</div>
                </div>

                <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                    <a href="#prenota" class="btn btn-primary">Prenota una visita gratuita</a>
                    <a href="#soluzione" class="btn btn-outline">Scopri come funziona</a>
                </div>
            </div>
            <div class="hero-visual-comp">
                <!-- Mockup QR -->
                <div class="mockup-card mockup-qr">
                    <div class="mockup-icon">📱</div>
                    <div>
                        <div style="font-weight: 800; font-size: 0.9rem;">Scansiona il QR</div>
                        <div style="font-size: 0.8rem; color: var(--text-muted);">Il cliente partecipa subito</div>
                    </div>
                </div>
                
                <img src="assets/nino.png" alt="Mascotte ufficiale FidelUp" class="mascot-hero">
                
                <!-- Mockup Phone / App -->
                <div class="mockup-card mockup-phone">
                    <div class="mockup-icon" style="background: #FEF3C7;">🎁</div>
                    <div>
                        <div style="font-weight: 800; font-size: 0.9rem;">Premio sbloccato</div>
                        <div style="font-size: 0.8rem; color: var(--text-muted);">Un motivo per tornare</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- IL PROBLEMA -->
    <section class="section-padding">
        <div class="container text-center">
            <h2 style="margin-bottom: 16px; max-width: 800px; margin-inline: auto;">Il problema non è trovare clienti. È farli tornare.</h2>
            <p class="subtitle">Molte attività riescono ad attrarre nuovi clienti, ma non hanno un sistema semplice per mantenere la relazione dopo la prima visita.</p>
            
            <div class="grid-3" style="margin-top: 60px;">
                <div style="text-align: left;">
                    <div style="font-size: 3rem; margin-bottom: 16px;">🚶</div>
                    <h3 style="margin-bottom: 12px;">Cliente che non torna</h3>
                    <p style="color: var(--text-muted);">La visita termina e la relazione può finire lì. Non hai un modo per ricontattarlo o invitarlo di nuovo.</p>
                </div>
                <div style="text-align: left;">
                    <div style="font-size: 3rem; margin-bottom: 16px;">🤷</div>
                    <h3 style="margin-bottom: 12px;">Nessun incentivo</h3>
                    <p style="color: var(--text-muted);">Il cliente oggi ha infinite scelte. Senza una ragione concreta, non ha un motivo urgente per scegliere te un'altra volta.</p>
                </div>
                <div style="text-align: left;">
                    <div style="font-size: 3rem; margin-bottom: 16px;">⚙️</div>
                    <h3 style="margin-bottom: 12px;">Nessun sistema semplice</h3>
                    <p style="color: var(--text-muted);">Vuoi fidelizzare, ma non hai tempo per studiare software complessi o gestire tessere di carta che si perdono.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- LA SOLUZIONE VISUALE -->
    <section class="section-padding bg-alt" id="soluzione">
        <div class="container text-center">
            <div class="badge">L'Esperienza</div>
            <h2>Una visita può diventare una relazione.</h2>
            <p class="subtitle">Guarda cosa succede quando un cliente incontra FidelUp nel tuo locale.</p>
            
            <div class="timeline">
                <div class="timeline-step">
                    <div class="timeline-number">01</div>
                    🚶 Cliente entra
                </div>
                <div class="timeline-arrow">→</div>
                <div class="timeline-step highlight">
                    <div class="timeline-number">02</div>
                    📱 Scansiona il QR
                </div>
                <div class="timeline-arrow">→</div>
                <div class="timeline-step highlight">
                    <div class="timeline-number">03</div>
                    📝 Lascia i suoi dati
                </div>
                <div class="timeline-arrow">→</div>
                <div class="timeline-step highlight">
                    <div class="timeline-number">04</div>
                    🎁 Riceve un vantaggio
                </div>
                <div class="timeline-arrow">→</div>
                <div class="timeline-step" style="background: var(--primary); color: white; border-color: var(--primary);">
                    <div class="timeline-number" style="color: rgba(255,255,255,0.7);">05</div>
                    ❤️ Ha un motivo per tornare
                </div>
            </div>
        </div>
    </section>

    <!-- I TRE MECCANISMI -->
    <section class="section-padding" id="programmi">
        <div class="container">
            <div class="text-center">
                <div class="badge">I Programmi</div>
                <h2>Tre modi per fidelizzare i tuoi clienti.</h2>
                <p class="subtitle">Scegliamo il meccanismo più adatto alla tua attività e lo configuriamo per te.</p>
            </div>

            <div class="grid-3">
                <div class="card" style="border-top: 6px solid #F59E0B;">
                    <div class="mech-icon" style="background: #FEF3C7; padding: 8px;">
                        <img src="assets/nino_star.png" alt="Ruota della Fortuna" style="width: 100%; height: 100%; object-fit: contain; mix-blend-mode: multiply;">
                    </div>
                    <h3>Ruota della Fortuna</h3>
                    <p style="color: var(--text-muted); margin: 16px 0;">Un'esperienza semplice e coinvolgente: il cliente scansiona il QR, gira la ruota, lascia i suoi dati e riceve il premio.</p>
                    <div style="font-weight: 800; font-size: 0.9rem; color: #D97706; margin-top: auto;">Gamification + Incentivo + Raccolta dati</div>
                    <div class="flow-list" style="background: #FFFBEB;">QR <span>→</span> Ruota <span>→</span> Dati <span>→</span> Premio</div>
                </div>

                <div class="card" style="border-top: 6px solid #3B82F6;">
                    <div class="mech-icon" style="background: #DBEAFE; padding: 8px;">
                        <img src="assets/nino_phone.png" alt="Cliente di Fiducia" style="width: 100%; height: 100%; object-fit: contain; mix-blend-mode: multiply;">
                    </div>
                    <h3>Cliente di Fiducia</h3>
                    <p style="color: var(--text-muted); margin: 16px 0;">Un club dedicato ai clienti che vuoi trasformare in clienti abituali, con vantaggi e comunicazioni riservate.</p>
                    <div style="font-weight: 800; font-size: 0.9rem; color: #2563EB; margin-top: auto;">Relazione + Appartenenza + Fidelizzazione</div>
                    <div class="flow-list" style="background: #EFF6FF;">QR <span>→</span> Iscrizione <span>→</span> Club <span>→</span> Vantaggi</div>
                </div>

                <div class="card" style="border-top: 6px solid #EC4899;">
                    <div class="mech-icon" style="background: #FCE7F3; padding: 8px;">
                        <img src="assets/nino_gift.png" alt="Offerta di Benvenuto" style="width: 100%; height: 100%; object-fit: contain; mix-blend-mode: multiply;">
                    </div>
                    <h3>Offerta di Benvenuto</h3>
                    <p style="color: var(--text-muted); margin: 16px 0;">Un regalo stabilito dal tuo negozio per incentivare il cliente a lasciare i propri dati fin dalla prima visita.</p>
                    <div style="font-weight: 800; font-size: 0.9rem; color: #DB2777; margin-top: auto;">Prima visita + Incentivo + Contatto</div>
                    <div class="flow-list" style="background: #FDF2F8;">QR <span>→</span> Dati <span>→</span> Codice <span>→</span> Premio</div>
                </div>
            </div>
        </div>
    </section>

    <!-- DAL QR AL CLIENTE FIDELIZZATO -->
    <section class="section-padding bg-alt text-center">
        <div class="container">
            <h2>Dal QR al cliente fidelizzato.</h2>
            <p class="subtitle">Il QR è il punto di ingresso. Il cliente partecipa comodamente dal suo telefono. I dati ottenuti vengono organizzati in base al meccanismo che hai scelto, pronti per aiutarti a far crescere la tua attività.</p>
            
            <div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 16px; margin-top: 40px;">
                <div style="font-size: 3rem;">📱</div>
                <div style="font-size: 1.5rem; color: var(--primary);">→</div>
                <div style="font-size: 3rem;">📝</div>
                <div style="font-size: 1.5rem; color: var(--primary);">→</div>
                <div style="font-size: 3rem;">🎁</div>
                <div style="font-size: 1.5rem; color: var(--primary);">→</div>
                <div style="font-size: 3rem;">🤝</div>
            </div>
        </div>
    </section>

    <!-- ESEMPI REALI -->
    <section class="section-padding">
        <div class="container text-center">
            <h2>Come potrebbe usarlo la tua attività?</h2>
            <p class="subtitle">Ogni attività è diversa. Ecco alcuni esempi di come FidelUp si adatta a te.</p>

            <div class="grid-3" style="margin-top: 60px;">
                <div class="card" style="text-align: left; padding: 32px;">
                    <div style="font-size: 2.5rem; margin-bottom: 16px;">💈</div>
                    <h3>Barberia</h3>
                    <p style="color: var(--primary); font-weight: 800; margin-bottom: 16px;">Ruota della Fortuna</p>
                    <p style="color: var(--text-muted); font-style: italic;">"Scansiona il QR, gira la ruota e scopri il tuo vantaggio per il prossimo taglio."</p>
                </div>
                <div class="card" style="text-align: left; padding: 32px;">
                    <div style="font-size: 2.5rem; margin-bottom: 16px;">💇</div>
                    <h3>Parrucchiere</h3>
                    <p style="color: var(--primary); font-weight: 800; margin-bottom: 16px;">Offerta di Benvenuto</p>
                    <p style="color: var(--text-muted); font-style: italic;">"Lascia i tuoi dati alla prima visita e ricevi subito un trattamento in omaggio."</p>
                </div>
                <div class="card" style="text-align: left; padding: 32px;">
                    <div style="font-size: 2.5rem; margin-bottom: 16px;">💅</div>
                    <h3>Centro Estetico</h3>
                    <p style="color: var(--primary); font-weight: 800; margin-bottom: 16px;">Cliente di Fiducia</p>
                    <p style="color: var(--text-muted); font-style: italic;">"Entra nel nostro club esclusivo e scopri i vantaggi e gli appuntamenti riservati."</p>
                </div>
            </div>
            
            <div style="margin-top: 48px; background: var(--surface-alt); padding: 32px; border-radius: 20px; border: 1px solid var(--border);">
                <div style="font-size: 2.5rem; margin-bottom: 16px;">🍕</div>
                <h3>Ristorante</h3>
                <p style="color: var(--primary); font-weight: 800; margin-bottom: 16px;">Offerta di Benvenuto</p>
                <p style="color: var(--text-muted); font-style: italic;">"Scansiona il menù, registrati e ricevi il dolce offerto da noi alla tua prossima cena."</p>
            </div>
        </div>
    </section>

    <!-- SERVIZIO GESTITO / COMPARAZIONE -->
    <section class="section-padding bg-dark text-center" id="servizio">
        <div class="container">
            <h2 style="color: white;">Non ti vendiamo solo un software.<br>Ti aiutiamo a farlo funzionare.</h2>
            
            <table class="vs-table" style="margin-top: 60px;">
                <thead>
                    <tr>
                        <th>Software Tradizionale</th>
                        <th>🦎 FidelUp</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td data-label="Software Tradizionale"><span style="color: #EF4444; margin-right: 12px; font-weight: 900;">✗</span> Ti registri e fai tutto da solo.</td>
                        <td data-label="🦎 FidelUp"><span style="color: var(--primary); margin-right: 12px; font-weight: 900;">✓</span> Veniamo nel tuo locale.</td>
                    </tr>
                    <tr>
                        <td data-label="Software Tradizionale"><span style="color: #EF4444; margin-right: 12px; font-weight: 900;">✗</span> Devi capire come configurarlo.</td>
                        <td data-label="🦎 FidelUp"><span style="color: var(--primary); margin-right: 12px; font-weight: 900;">✓</span> Configuriamo noi il sistema.</td>
                    </tr>
                    <tr>
                        <td data-label="Software Tradizionale"><span style="color: #EF4444; margin-right: 12px; font-weight: 900;">✗</span> Devi occuparti della gestione quotidiana.</td>
                        <td data-label="🦎 FidelUp"><span style="color: var(--primary); margin-right: 12px; font-weight: 900;">✓</span> Personalizziamo l'esperienza e i premi.</td>
                    </tr>
                    <tr>
                        <td data-label="Software Tradizionale"><span style="color: #EF4444; margin-right: 12px; font-weight: 900;">✗</span> Supporto impersonale via email.</td>
                        <td data-label="🦎 FidelUp"><span style="color: var(--primary); margin-right: 12px; font-weight: 900;">✓</span> Hai un referente diretto che ti accompagna.</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- COSA RICEVI -->
    <section class="section-padding">
        <div class="container text-center">
            <h2>Cosa ricevi con FidelUp?</h2>
            <p class="subtitle">Il pacchetto completo per iniziare a fidelizzare senza perdite di tempo.</p>
            
            <div class="grid-3" style="margin-top: 60px; text-align: left;">
                <div style="display: flex; gap: 16px;">
                    <div style="font-size: 2rem;">📱</div>
                    <div>
                        <h4 style="font-size: 1.1rem; margin-bottom: 8px;">QR Personalizzato</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Un QR preparato ed esposto nel tuo locale per far accedere i clienti al programma.</p>
                    </div>
                </div>
                <div style="display: flex; gap: 16px;">
                    <div style="font-size: 2rem;">⚙️</div>
                    <div>
                        <h4 style="font-size: 1.1rem; margin-bottom: 8px;">Configurazione Inclusa</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Prepariamo e configuriamo il meccanismo scelto (Ruota, Offerta o Club) per te.</p>
                    </div>
                </div>
                <div style="display: flex; gap: 16px;">
                    <div style="font-size: 2rem;">🎨</div>
                    <div>
                        <h4 style="font-size: 1.1rem; margin-bottom: 8px;">Personalizzazione</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Adattiamo il sistema con il tuo logo, i tuoi colori e la tua identità di brand.</p>
                    </div>
                </div>
                <div style="display: flex; gap: 16px;">
                    <div style="font-size: 2rem;">🤝</div>
                    <div>
                        <h4 style="font-size: 1.1rem; margin-bottom: 8px;">Assistenza Diretta</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Acompañamiento, soporte y resolución de dudas siempre disponibile.</p>
                    </div>
                </div>
                <div style="display: flex; gap: 16px;">
                    <div style="font-size: 2rem;">📊</div>
                    <div>
                        <h4 style="font-size: 1.1rem; margin-bottom: 8px;">I tuoi Dati Organizzati</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">I dati raccolti dai clienti sono organizzati per poterli consultare e utilizzare per le tue attività.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- PERCHE E DIVERSO -->
    <section class="section-padding bg-green text-center">
        <div class="container">
            <h2>Non è solo quello che fa FidelUp.<br>È come lo facciamo.</h2>
            
            <div class="grid-3" style="margin-top: 60px;">
                <div class="card" style="background: white; border: none; box-shadow: var(--shadow-md);">
                    <h3 style="color: var(--primary); margin-bottom: 16px;">Semplice</h3>
                    <p style="color: var(--text-muted);">Il cliente utilizza il suo telefono. Non deve scaricare app pesanti o portare tessere di carta.</p>
                </div>
                <div class="card" style="background: white; border: none; box-shadow: var(--shadow-md);">
                    <h3 style="color: var(--primary); margin-bottom: 16px;">Personalizzato</h3>
                    <p style="color: var(--text-muted);">Il sistema si adatta all'identità del tuo negozio: i tuoi premi, le tue regole, i tuoi colori.</p>
                </div>
                <div class="card" style="background: white; border: none; box-shadow: var(--shadow-md);">
                    <h3 style="color: var(--primary); margin-bottom: 16px;">Gestito</h3>
                    <p style="color: var(--text-muted);">Il proprietario non viene abbandonato. Ricevi accompagnamento continuo dal nostro team.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- TARGET -->
    <section class="section-padding text-center">
        <div class="container">
            <h2>FidelUp è pensato per attività dove il cliente può tornare.</h2>
            <div class="target-pills">
                <div class="target-pill">💇 Parrucchieri</div>
                <div class="target-pill">💅 Centri Estetici</div>
                <div class="target-pill">💈 Barberie</div>
                <div class="target-pill">🍕 Ristoranti</div>
                <div class="target-pill">🛍️ Boutique</div>
            </div>
            <p style="margin-top: 40px; font-size: 1.25rem; font-weight: 600; color: var(--primary-dark);">Se il tuo cliente può tornare, FidelUp può aiutarti a costruire una relazione.</p>
        </div>
    </section>

    <!-- FREE MONTH -->
    <section class="section-padding bg-alt text-center" style="border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
        <div class="container">
            <h2 style="font-size: clamp(2.5rem, 5vw, 3.5rem); margin-bottom: 24px;">Provalo nel tuo locale.<br><span class="text-primary">Il primo mese è gratuito.</span></h2>
            <p class="subtitle" style="font-size: 1.25rem; max-width: 700px;">Installiamo e configuriamo il sistema. Lo utilizzi nel tuo locale con i tuoi clienti e dopo il primo mese puoi valutare se continuare l'esperienza.</p>
        </div>
    </section>

    <!-- PRICING -->
    <section class="section-padding" id="prezzi">
        <div class="container text-center">
            <div class="badge">Piani</div>
            <h2>Scegli il piano giusto per te.</h2>
            <p class="subtitle">Prezzi indicativi. Il piano più adatto alla tua attività verrà definito durante la consulenza.</p>
            
            <div class="grid-3">
                <div class="pricing-card">
                    <h3>Base</h3>
                    <div class="pricing-price">39,99<span>€/mese*</span></div>
                    <ul class="pricing-features">
                        <li>Installazione Inclusa</li>
                        <li>Configurazione del Sistema</li>
                        <li>1 Meccanismo a scelta</li>
                        <li>Dati Organizzati</li>
                    </ul>
                </div>
                <div class="pricing-card popular">
                    <div style="position: absolute; top: -16px; left: 50%; transform: translateX(-50%); background: var(--primary); color: white; padding: 6px 20px; border-radius: 20px; font-size: 0.85rem; font-weight: 800; text-transform: uppercase;">Consigliato</div>
                    <h3>Premium</h3>
                    <div class="pricing-price">47,99<span>€/mese*</span></div>
                    <ul class="pricing-features">
                        <li>Installazione Inclusa</li>
                        <li>Configurazione Personalizzata</li>
                        <li>Fino a 2 Meccanismi</li>
                        <li>Assistenza Diretta</li>
                    </ul>
                </div>
                <div class="pricing-card">
                    <h3>VIP</h3>
                    <div class="pricing-price">64,99<span>€/mese*</span></div>
                    <ul class="pricing-features">
                        <li>Installazione Inclusa</li>
                        <li>Configurazione Premium</li>
                        <li>Tutti i Meccanismi</li>
                        <li>Consulenza e Supporto VIP</li>
                    </ul>
                </div>
            </div>
            <p style="margin-top: 32px; font-size: 0.9rem; color: var(--text-muted);">* I prezzi sono indicativi e potrebbero variare. Il primo mese è sempre gratuito e senza impegno iniziale.</p>
        </div>
    </section>

    <!-- FAQ -->
    <section class="section-padding bg-alt">
        <div class="container">
            <h2 class="text-center" style="margin-bottom: 60px;">Domande Frequenti</h2>
            
            <div style="max-width: 800px; margin: 0 auto;">
                <div class="faq-item">
                    <div class="faq-q">Devo comprare un tablet o dispositivi extra? <span>+</span></div>
                    <div class="faq-a">No! I tuoi clienti partecipano scansionando un codice QR esposto nel tuo locale, utilizzando i loro smartphone. Non c'è bisogno di hardware extra.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-q">I miei clienti devono scaricare un'app? <span>+</span></div>
                    <div class="faq-a">Assolutamente no. Il sistema funziona direttamente tramite il browser del loro smartphone dopo aver scansionato il QR, rendendo l'esperienza immediata e senza frizioni.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-q">Quanto lavoro devo fare io per gestirlo? <span>+</span></div>
                    <div class="faq-a">Il minimo indispensabile. FidelUp è un servizio gestito: noi lo configuriamo e lo prepariamo. Tu dovrai solo verificare o applicare lo sconto/premio quando il cliente te lo mostra in cassa.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-q">Posso personalizzare i colori e i premi? <span>+</span></div>
                    <div class="faq-a">Sì. Adatteremo l'interfaccia inserendo i colori del tuo brand, il tuo logo e configureremo i premi o gli sconti che hai deciso di offrire ai tuoi clienti.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-q">Quale programma è adatto alla mia attività? <span>+</span></div>
                    <div class="faq-a">Dipende dai tuoi obiettivi. La Ruota della Fortuna è ottima per raccogliere contatti divertendo, l'Offerta di Benvenuto incentiva la prima conversione, mentre il Cliente di Fiducia premia i più fedeli. Ne parleremo durante la visita gratuita.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-q">Cosa succede dopo il primo mese gratuito? <span>+</span></div>
                    <div class="faq-a">Terminato il periodo di prova, faremo il punto della situazione insieme. Se il sistema ti piace e vedi risultati, sceglieremo il piano adatto. Altrimenti, ritireremo il materiale senza alcun costo o vincolo per te.</div>
                </div>
            </div>
            
            <div class="text-center" style="margin-top: 48px;">
                <a href="#prenota" class="btn btn-outline">Hai altre domande? Parliamone.</a>
            </div>
        </div>
    </section>

    <!-- FORM & CTA FINAL -->
    <section class="section-padding bg-green" id="prenota">
        <div class="container text-center">
            
            <div style="display: flex; justify-content: center; align-items: center; gap: 24px; margin-bottom: 24px;">
                <img src="assets/nino.png" alt="Mascotte ufficiale FidelUp" style="width: 80px; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1)); mix-blend-mode: multiply;">
                <h2 style="margin-bottom: 0; text-align: left; line-height: 1.1; font-size: clamp(2rem, 4vw, 3rem); color: var(--primary-dark);">Pronto a far tornare<br>i tuoi clienti?</h2>
            </div>
            
            <p class="subtitle" style="margin-bottom: 48px; font-weight: 600; color: var(--primary-dark);">Vediamo insieme quale programma può funzionare meglio per la tua attività.</p>

            <div class="form-container">
                <form id="fidelup-form">
                    <div class="form-group">
                        <label class="form-label">Nome e cognome</label>
                        <input type="text" id="nome" class="form-input" required placeholder="Mario Rossi">
                    </div>
                    <div class="form-group">
                        <label class="form-label">Nome attività</label>
                        <input type="text" id="attivita" class="form-input" required placeholder="Es. Barberia Il Taglio">
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                        <div class="form-group">
                            <label class="form-label">Tipo di attività</label>
                            <input type="text" id="tipo" class="form-input" required placeholder="Es. Barbiere">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Città</label>
                            <input type="text" id="citta" class="form-input" required placeholder="Es. Roma">
                        </div>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                        <div class="form-group">
                            <label class="form-label">Numero di telefono</label>
                            <input type="tel" id="telefono" class="form-input" required placeholder="333 123 4567">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Email</label>
                            <input type="email" id="email" class="form-input" required placeholder="mario@email.com">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Messaggio (Opzionale)</label>
                        <textarea id="messaggio" class="form-input" rows="3" placeholder="Vorrei informazioni per..."></textarea>
                    </div>
                    <div class="form-group" style="display: flex; gap: 12px; margin-top: 32px; align-items: flex-start;">
                        <input type="checkbox" id="privacy" required style="width: 24px; height: 24px; flex-shrink: 0; margin-top: 2px;">
                        <label for="privacy" style="font-size: 0.9rem; color: var(--text-muted); text-align: left; line-height: 1.5;">Acconsento al trattamento dei dati personali ai fini del contatto, nel rispetto della <a href="#privacy" style="color: var(--primary); text-decoration: underline;">Privacy Policy</a>.</label>
                    </div>
                    
                    <button type="submit" id="submitBtn" class="btn btn-primary" style="width: 100%; font-size: 1.15rem; padding: 20px; margin-top: 16px;">Prenota una visita gratuita</button>
                    
                    <div id="form-msg" style="margin-top: 24px; padding: 20px; border-radius: 12px; display: none; font-weight: 600; text-align: left;"></div>
                </form>
            </div>
            
            <div style="margin-top: 48px;">
                <h3 style="font-size: 1.8rem; font-weight: 900; color: var(--primary-dark);">Fai tornare i tuoi clienti.<br>Al resto pensiamo noi.</h3>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <div style="display: flex; justify-content: center; align-items: center; gap: 12px; margin-bottom: 32px;">
                <img src="assets/nino.png" alt="Mascotte ufficiale FidelUp" style="width: 48px; filter: brightness(0) invert(1); opacity: 0.9;">
                <div style="font-size: 2rem; font-weight: 900; letter-spacing: -0.05em;">Fidel<span style="color: var(--primary-light);">Up</span></div>
            </div>
            
            <p style="max-width: 500px; margin: 0 auto 40px; color: rgba(255,255,255,0.7); font-size: 1.05rem;">Servizio di fidelizzazione gestito per attività locali. Tu pensa al tuo lavoro, noi pensiamo alla fidelizzazione.</p>

            <div class="footer-links" style="margin-bottom: 40px;">
                <a href="#soluzione">Come funziona</a>
                <a href="#programmi">I Programmi</a>
                <a href="#servizio">Il Servizio</a>
                <a href="#prezzi">Prezzi</a>
                <a href="#privacy">Privacy Policy</a>
                <a href="#cookie">Cookie Policy</a>
            </div>
            
            <div style="font-size: 0.9rem; color: rgba(255,255,255,0.4); border-top: 1px solid rgba(255,255,255,0.1); padding-top: 32px;">
                © 2026 FidelUp.<br>
                Email: [IN INSERIMENTO] | Tel: [IN INSERIMENTO]<br>
                Sede: [IN INSERIMENTO] | P.IVA: [IN INSERIMENTO]
            </div>
        </div>
    </footer>

    <a href="#prenota" class="btn btn-primary floating-cta" id="floatBtn" style="box-shadow: 0 10px 25px rgba(46,125,50,0.5); padding: 12px 24px;">
        Prenota una visita
    </a>

    <script>
        // FAQ Toggle
        document.querySelectorAll('.faq-q').forEach(q => {
            q.addEventListener('click', () => {
                const item = q.parentElement;
                item.classList.toggle('active');
            });
        });

        // Floating CTA Logic
        const floatBtn = document.getElementById('floatBtn');
        const prenotaSec = document.getElementById('prenota');
        
        window.addEventListener('scroll', () => {
            if (window.innerWidth > 768) {
                const scrollY = window.scrollY;
                const prenotaTop = prenotaSec.offsetTop - 600;
                
                if (scrollY > 700 && scrollY < prenotaTop) {
                    floatBtn.classList.add('visible');
                } else {
                    floatBtn.classList.remove('visible');
                }
            }
        });

        // Form Submit Logic connected to real webhook
        const WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbypPD56D6_kb0w1H9mOGaV8JubjSDk1xwd_3pw9Jq4VkEACab_3cZ0rFyxgqiIRN49d/exec';
        const form = document.getElementById('fidelup-form');
        const btn = document.getElementById('submitBtn');
        const msgDiv = document.getElementById('form-msg');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            if (!form.checkValidity()) return;

            btn.disabled = true;
            btn.textContent = 'Invio in corso...';
            btn.style.opacity = '0.7';
            msgDiv.style.display = 'none';

            const payload = {
                source: 'LandingPage',
                nome: document.getElementById('nome').value,
                attivita: document.getElementById('attivita').value,
                tipo: document.getElementById('tipo').value,
                citta: document.getElementById('citta').value,
                telefono: document.getElementById('telefono').value,
                email: document.getElementById('email').value,
                messaggio: document.getElementById('messaggio').value
            };

            try {
                // Post to Google Apps Script webhook
                await fetch(WEBHOOK_URL, {
                    method: 'POST',
                    mode: 'no-cors',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                // Mostriamo il success reale
                msgDiv.innerHTML = '<span style="font-size:1.5rem; display:block; margin-bottom:8px;">✅</span> <strong>Richiesta ricevuta.</strong><br>Ti contatteremo per concordare la visita gratuita.';
                msgDiv.style.backgroundColor = '#E8F5E9';
                msgDiv.style.color = '#1B5E20';
                msgDiv.style.border = '2px solid #4CAF50';
                msgDiv.style.display = 'block';
                
                form.reset();
                btn.textContent = 'Prenota una visita gratuita';
                btn.disabled = false;
                btn.style.opacity = '1';
                
            } catch (error) {
                msgDiv.innerHTML = '<span style="font-size:1.5rem; display:block; margin-bottom:8px;">❌</span> <strong>Non è stato possibile inviare la richiesta.</strong><br>Controlla i dati e la connessione, poi riprova.';
                msgDiv.style.backgroundColor = '#FFEBEE';
                msgDiv.style.color = '#B71C1C';
                msgDiv.style.border = '2px solid #F44336';
                msgDiv.style.display = 'block';
                
                btn.disabled = false;
                btn.textContent = 'Riprova a inviare';
                btn.style.opacity = '1';
            }
        });
    </script>
</body>
</html>
"""

with open("/home/yadied/Escritorio/pagina fidelup/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("V3 HTML Successfully generated.")
