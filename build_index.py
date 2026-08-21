import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will completely rewrite the file content based on the new requirements
# while preserving the CSS variables, webhook JS logic, and basic layout structures.

html_content = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>FidelUp | Fai tornare i tuoi clienti</title>
    <meta name="description" content="FidelUp è il servizio di fidelizzazione gestito per piccole attività locali. Installiamo e gestiamo il tuo programma fedeltà.">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js" defer></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js" defer></script>
    
    <style>
        :root {
            --primary: #2E7D32;
            --primary-light: #4CAF50;
            --primary-dark: #1B5E20;
            --bg: #FAFAFA;
            --surface: #FFFFFF;
            --surface-green: #E8F5E9;
            --surface-green-alt: #C8E6C9;
            --text-dark: #1A1A1A;
            --text-muted: #666666;
            --font-main: 'Outfit', sans-serif;
            --radius-md: 16px;
            --radius-lg: 24px;
            --shadow-soft: 0 10px 40px rgba(0,0,0,0.05);
            --shadow-float: 0 20px 40px rgba(46,125,50,0.15);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body { font-family: var(--font-main); color: var(--text-dark); background-color: var(--bg); line-height: 1.5; -webkit-font-smoothing: antialiased; }

        @media (prefers-reduced-motion: reduce) {
            *, ::before, ::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; }
        }

        h1, h2, h3, h4, h5 { font-weight: 800; line-height: 1.1; letter-spacing: -0.02em; }
        h1 { font-size: clamp(2.5rem, 6vw, 4.5rem); }
        h2 { font-size: clamp(2rem, 5vw, 3.5rem); }
        h3 { font-size: clamp(1.5rem, 3vw, 2rem); }
        p { font-size: 1.1rem; color: var(--text-muted); line-height: 1.6; }
        
        .text-primary { color: var(--primary); }
        .text-light { color: var(--surface); }

        .container { max-width: 1280px; margin: 0 auto; padding: 0 24px; }

        .btn { display: inline-flex; align-items: center; justify-content: center; padding: 18px 36px; border-radius: 100px; font-weight: 700; font-size: 1.1rem; text-decoration: none; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; border: none; }
        .btn-primary { background: var(--primary); color: white; box-shadow: rgba(46,125,50,0.3) 0 8px 24px; }
        .btn-primary:hover { background: var(--primary-dark); transform: translateY(-2px) scale(1.02); box-shadow: rgba(46,125,50,0.4) 0 12px 32px; }
        .btn-white { background: white; color: var(--primary); box-shadow: 0 8px 24px rgba(0,0,0,0.1); }
        .btn-white:hover { background: #f0f0f0; transform: translateY(-2px); }

        header { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; padding: 16px 0; backdrop-filter: blur(12px); background: rgba(250, 250, 250, 0.8); border-bottom: 1px solid rgba(0,0,0,0.05); transition: all 0.3s ease; }
        header .container { display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 1.8rem; font-weight: 900; color: var(--text-dark); text-decoration: none; display: flex; align-items: center; gap: 8px; }
        .nav-links { display: flex; gap: 32px; align-items: center; }
        .nav-links a { text-decoration: none; color: var(--text-dark); font-weight: 600; transition: color 0.2s; }
        .nav-links a:hover { color: var(--primary); }
        .mobile-menu-btn { display: none; font-size: 1.5rem; background: none; border: none; cursor: pointer; width: 44px; height: 44px; align-items: center; justify-content: center; border-radius: 8px; }

        .mobile-menu-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: rgba(250, 250, 250, 0.98); backdrop-filter: blur(10px); z-index: 2000; display: flex; flex-direction: column; padding: 24px; transform: translateX(100%); transition: transform 0.3s; visibility: hidden; }
        .mobile-menu-overlay.open { transform: translateX(0); visibility: visible; }
        .mobile-menu-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; }
        .mobile-menu-close { font-size: 2rem; background: none; border: none; cursor: pointer; }
        .mobile-menu-links { display: flex; flex-direction: column; gap: 32px; font-size: 1.5rem; font-weight: 700; }
        .mobile-menu-links a { text-decoration: none; color: var(--text-dark); }
        
        /* 01 HERO */
        .hero { background: linear-gradient(180deg, #F1F8E9 0%, #FFFFFF 100%); padding: 160px 0 100px; overflow: hidden; }
        .hero-grid { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 60px; align-items: center; }
        .hero-eyebrow { font-size: 0.9rem; font-weight: 800; color: var(--primary); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 16px; }
        .hero h1 { margin-bottom: 24px; }
        .hero p { font-size: 1.25rem; margin-bottom: 40px; max-width: 600px; color: var(--text-dark); font-weight: 500; }
        .hero-microcopy { font-size: 0.9rem; color: var(--text-muted); margin-top: 16px; font-weight: 500; }
        .nino-bubble { background: white; padding: 16px 24px; border-radius: 20px; box-shadow: var(--shadow-float); position: absolute; max-width: 250px; font-size: 0.95rem; font-weight: 600; color: var(--text-dark); z-index: 10; border: 1px solid rgba(0,0,0,0.05); }
        .nino-bubble::after { content: ''; position: absolute; width: 16px; height: 16px; background: white; transform: rotate(45deg); }
        .nino-hero { position: relative; display: flex; justify-content: center; align-items: center; }
        .nino-hero img { width: 100%; max-width: 320px; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.1)); }
        .nino-hero .nino-bubble { bottom: 20%; left: -10%; }
        .nino-hero .nino-bubble::after { bottom: 20px; right: -8px; }

        /* 02 IL PROBLEMA */
        .problema { background: #1A1A1A; color: white; padding: 120px 0; text-align: center; }
        .problema h2 { color: white; margin-bottom: 24px; }
        .problema p { color: rgba(255,255,255,0.8); max-width: 800px; margin: 0 auto; font-size: 1.2rem; }
        .stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin: 60px 0; }
        .stat-card { background: rgba(255,255,255,0.05); padding: 40px 30px; border-radius: var(--radius-lg); border: 1px solid rgba(255,255,255,0.1); }
        .stat-num { font-size: 4rem; font-weight: 900; color: var(--primary-light); margin-bottom: 16px; line-height: 1; }
        .stat-text { font-size: 1.1rem; color: white; font-weight: 600; margin-bottom: 16px; }
        .stat-source { font-size: 0.8rem; color: rgba(255,255,255,0.5); }
        .problema-nino-wrap { display: flex; align-items: center; justify-content: center; gap: 24px; margin-top: 60px; background: rgba(255,255,255,0.05); padding: 24px 40px; border-radius: 100px; width: fit-content; margin-inline: auto; }
        .problema-nino-wrap img { width: 60px; }
        .problema-nino-wrap span { font-weight: 600; font-size: 1.1rem; text-align: left; }

        /* 03 LA SVOLTA */
        .svolta { padding: 120px 0; background: var(--bg); text-align: center; }
        .svolta h2 { max-width: 800px; margin: 0 auto 24px; }
        .svolta p { max-width: 700px; margin: 0 auto 60px; font-size: 1.2rem; }
        .svolta-visual { display: flex; align-items: center; justify-content: center; gap: 40px; }
        .svolta-nino-bubble { background: var(--surface-green); color: var(--primary-dark); padding: 20px; border-radius: 20px; font-weight: 700; max-width: 300px; position: relative; }
        .svolta-visual img { width: 140px; }
        .cliente-anim { display: flex; align-items: center; gap: 20px; background: white; padding: 20px 40px; border-radius: 100px; box-shadow: var(--shadow-soft); }
        .cliente-icon { font-size: 2rem; }
        .cliente-arrow { font-size: 2rem; color: var(--primary); font-weight: 900; }

        /* 04 TU FAI IL TUO LAVORO */
        .tu-fai { padding: 120px 0; background: var(--surface); }
        .tu-fai h2 { text-align: center; margin-bottom: 60px; }
        .steps-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }
        .step-card { text-align: left; }
        .step-num { font-size: 3rem; font-weight: 900; color: var(--surface-green-alt); margin-bottom: 16px; line-height: 1; }
        .step-card h3 { margin-bottom: 16px; }
        .tu-fai-chiusura { text-align: center; font-size: 1.5rem; font-weight: 800; color: var(--primary); margin-top: 60px; }

        /* 05 PER IL TUO CLIENTE È SEMPLICE */
        .semplice { padding: 120px 0; background: var(--surface-green); text-align: center; }
        .semplice h2 { margin-bottom: 60px; }
        .semplice .steps-grid { margin-bottom: 60px; }
        .semplice-card { background: white; padding: 40px; border-radius: var(--radius-lg); text-align: left; box-shadow: var(--shadow-soft); }
        .semplice-chiusura { font-size: 1.5rem; font-weight: 800; color: var(--primary-dark); }

        /* 06 I MECCANISMI */
        .meccanismi { padding: 120px 0; background: var(--bg); }
        .meccanismi-header { text-align: center; margin-bottom: 60px; }
        .meccanismi-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 30px; }
        .mecc-card { background: white; padding: 40px; border-radius: var(--radius-lg); box-shadow: var(--shadow-soft); }
        .mecc-icon { font-size: 2.5rem; margin-bottom: 20px; }
        .mecc-card h3 { margin-bottom: 16px; }
        .mecc-card p { margin-bottom: 16px; }
        .mecc-ideale { font-size: 0.9rem; font-weight: 700; color: var(--primary); background: var(--surface-green); padding: 8px 16px; border-radius: 8px; display: inline-block; }

        /* 07 QUASI NIENTE */
        .quasi-niente { padding: 120px 0; background: var(--surface); text-align: center; }
        .quasi-niente h2 { margin-bottom: 60px; }
        .qn-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 40px; max-width: 900px; margin: 0 auto; }
        .qn-col { background: var(--bg); padding: 40px; border-radius: var(--radius-lg); text-align: left; }
        .qn-col h3 { text-align: center; margin-bottom: 30px; font-size: 2rem; color: var(--text-dark); }
        .qn-col.fidelup { background: var(--primary); color: white; }
        .qn-col.fidelup h3 { color: white; }
        .qn-item { font-size: 1.1rem; font-weight: 600; margin-bottom: 20px; display: flex; align-items: flex-start; gap: 12px; }
        .qn-item::before { content: '✓'; color: var(--primary); font-weight: 900; }
        .qn-col.fidelup .qn-item::before { color: var(--surface-green-alt); }
        .qn-chiusura { font-size: clamp(2rem, 4vw, 3rem); font-weight: 900; margin-top: 80px; line-height: 1.2; }

        /* 08 PERCHÉ FIDELUP */
        .perche { padding: 120px 0; background: var(--surface-green); text-align: center; }
        .perche h2 { margin-bottom: 60px; }
        .table-wrap { max-width: 900px; margin: 0 auto; background: white; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-soft); }
        .table-row { display: grid; grid-template-columns: 1fr 1fr; border-bottom: 1px solid rgba(0,0,0,0.05); }
        .table-row:last-child { border-bottom: none; }
        .table-head { font-weight: 800; font-size: 1.2rem; padding: 24px; background: var(--bg); }
        .table-cell { padding: 24px; font-size: 1.1rem; font-weight: 500; text-align: left; display: flex; align-items: center; gap: 12px; }
        .cell-bad::before { content: '✕'; color: #EF4444; font-weight: 900; }
        .cell-good { background: rgba(76, 175, 80, 0.05); }
        .cell-good::before { content: '✓'; color: var(--primary); font-weight: 900; }
        .perche-chiusura { margin-top: 40px; font-size: 1.2rem; font-weight: 700; }

        /* 09 IL PRIMO MESE */
        .primo-mese { padding: 120px 0; background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%); color: white; text-align: center; }
        .pm-eyebrow { font-size: 0.9rem; font-weight: 800; color: var(--surface-green-alt); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 16px; }
        .primo-mese h2 { color: white; margin-bottom: 24px; }
        .primo-mese p { color: rgba(255,255,255,0.9); max-width: 700px; margin: 0 auto 40px; }
        .pm-zero { font-size: 8rem; font-weight: 900; color: var(--surface-green-alt); line-height: 1; margin-bottom: 40px; }
        .pm-benefits { display: flex; justify-content: center; gap: 40px; margin-bottom: 60px; flex-wrap: wrap; }
        .pm-benefit { font-size: 1.2rem; font-weight: 600; display: flex; align-items: center; gap: 12px; }
        .pm-nino { margin-top: 60px; display: flex; align-items: center; justify-content: center; gap: 24px; background: rgba(0,0,0,0.2); padding: 24px 40px; border-radius: 100px; width: fit-content; margin-inline: auto; }
        .pm-nino img { width: 60px; }

        /* 10 PREZZI */
        .prezzi { padding: 120px 0; background: var(--bg); text-align: center; }
        .prezzi h2 { margin-bottom: 60px; }
        .pricing-cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; max-width: 1100px; margin: 0 auto; }
        .p-card { background: white; padding: 40px; border-radius: var(--radius-lg); text-align: left; box-shadow: var(--shadow-soft); position: relative; }
        .p-card.premium { border: 3px solid var(--primary); transform: scale(1.05); z-index: 2; }
        .p-badge { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: var(--primary); color: white; padding: 6px 16px; border-radius: 20px; font-weight: 800; font-size: 0.9rem; white-space: nowrap; }
        .p-price { font-size: 3rem; font-weight: 900; margin: 20px 0; color: var(--text-dark); }
        .p-price span { font-size: 1rem; color: var(--text-muted); font-weight: 500; }
        .p-features { list-style: none; margin-bottom: 0; }
        .p-features li { margin-bottom: 16px; font-weight: 500; display: flex; align-items: flex-start; gap: 12px; }
        .p-features li::before { content: '✓'; color: var(--primary); font-weight: 900; }
        .prezzi-chiusura { margin-top: 60px; font-size: 1.1rem; font-weight: 700; color: var(--primary-dark); }

        /* 11 FAQ */
        .faq { padding: 120px 0; background: var(--surface); }
        .faq-wrapper { max-width: 800px; margin: 60px auto 0; }
        .faq-item { border-bottom: 1px solid rgba(0,0,0,0.1); }
        .faq-btn { width: 100%; background: none; border: none; padding: 24px 0; cursor: pointer; font-family: var(--font-main); text-align: left; display: flex; justify-content: space-between; align-items: center; gap: 12px; font-size: 1.2rem; font-weight: 700; color: var(--text-dark); }
        .faq-btn:focus-visible { outline: 3px solid var(--primary); border-radius: 4px; }
        .faq-icon { font-size: 1.5rem; color: var(--primary); transition: transform 0.3s; }
        .faq-item.active .faq-icon { transform: rotate(45deg); }
        .faq-a { padding: 0 0 24px; color: var(--text-muted); font-size: 1.1rem; display: none; line-height: 1.6; }

        /* 12 CTA FINAL */
        .cta-final { padding: 120px 0; background: var(--surface-green); }
        .cta-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
        .cta-text h2 { color: var(--primary-dark); margin-bottom: 24px; }
        .form-box { background: white; padding: 48px; border-radius: var(--radius-lg); box-shadow: var(--shadow-float); }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; font-weight: 700; margin-bottom: 8px; font-size: 0.95rem; }
        .form-group input { width: 100%; padding: 16px; border: 2px solid rgba(0,0,0,0.1); border-radius: 12px; font-family: var(--font-main); font-size: 1rem; transition: border-color 0.3s; }
        .form-group input:focus { outline: none; border-color: var(--primary); }
        .form-message { margin-top: 20px; padding: 20px; border-radius: 12px; display: none; font-weight: 600; }
        .cta-nino { display: flex; align-items: center; gap: 20px; margin-top: 40px; background: white; padding: 16px 24px; border-radius: 100px; width: fit-content; box-shadow: var(--shadow-soft); }
        .cta-nino img { width: 50px; }
        .cta-nino span { font-weight: 600; font-size: 0.95rem; }
        .contacts-info { margin-top: 40px; font-weight: 600; color: var(--primary-dark); line-height: 1.8; }

        /* 13 FOOTER */
        footer { background: var(--text-dark); color: white; padding: 60px 0 30px; text-align: center; }
        .footer-logo { font-size: 2rem; font-weight: 900; margin-bottom: 24px; color: white; }
        .footer-links { display: flex; justify-content: center; gap: 24px; margin-bottom: 40px; flex-wrap: wrap; }
        .footer-links a { color: rgba(255,255,255,0.7); text-decoration: none; font-weight: 500; }
        .footer-links a:hover { color: white; }

        /* WHATSAPP FLOAT */
        .wa-float { position: fixed; bottom: 30px; right: 30px; background: #25D366; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 20px rgba(37,211,102,0.3); z-index: 1000; transition: transform 0.3s; text-decoration: none; }
        .wa-float:hover { transform: scale(1.1); }
        .wa-float svg { width: 32px; height: 32px; fill: currentColor; }

        /* RESPONSIVE */
        @media (max-width: 992px) {
            .nav-links { display: none; }
            .mobile-menu-btn { display: flex; }
            .hero-grid { grid-template-columns: 1fr; text-align: center; }
            .nino-hero { order: -1; margin-bottom: 40px; }
            .nino-hero .nino-bubble { bottom: 0; left: 50%; transform: translateX(-50%); }
            .nino-hero .nino-bubble::after { display: none; }
            .stats-grid { grid-template-columns: 1fr; }
            .svolta-visual { flex-direction: column; }
            .steps-grid { grid-template-columns: 1fr; gap: 40px; }
            .meccanismi-grid { grid-template-columns: 1fr; }
            .qn-grid { grid-template-columns: 1fr; }
            .table-row { grid-template-columns: 1fr; }
            .table-head { display: none; }
            .table-cell:nth-child(1) { background: #FAFAFA; font-weight: 700; color: var(--text-muted); }
            .pricing-cards { grid-template-columns: 1fr; max-width: 400px; }
            .p-card.premium { transform: none; margin: 20px 0; }
            .cta-grid { grid-template-columns: 1fr; }
            .pm-benefits { flex-direction: column; align-items: center; }
            .problema-nino-wrap, .pm-nino { flex-direction: column; text-align: center; border-radius: 24px; }
        }
        @media (max-width: 480px) {
            .wa-float { bottom: 20px; right: 20px; width: 50px; height: 50px; }
            .wa-float svg { width: 26px; height: 26px; }
            .hero, .problema, .svolta, .tu-fai, .semplice, .meccanismi, .quasi-niente, .perche, .primo-mese, .prezzi, .faq, .cta-final { padding: 80px 0; }
            .pm-zero { font-size: 6rem; }
            .form-box { padding: 30px 20px; }
        }
    </style>
</head>
<body>

    <header id="header">
        <div class="container">
            <a href="#" class="logo">
                <img src="assets/nino.png" alt="FidelUp" style="width: 32px;">
                FidelUp
            </a>
            <nav class="nav-links">
                <a href="#funziona">Come funziona</a>
                <a href="#perche">Perché FidelUp</a>
                <a href="#prezzi">Prezzi</a>
                <a href="#faq">FAQ</a>
                <a href="#prenota" class="btn btn-primary" style="padding: 12px 24px; font-size: 1rem;">Prenota visita gratuita</a>
            </nav>
            <button class="mobile-menu-btn" id="open-menu-btn" aria-label="Apri menu">☰</button>
        </div>
    </header>

    <div class="mobile-menu-overlay" id="mobile-menu">
        <div class="mobile-menu-header">
            <a href="#" class="logo">
                <img src="assets/nino.png" alt="" style="width: 32px;">
                FidelUp
            </a>
            <button class="mobile-menu-close" id="close-menu-btn">✕</button>
        </div>
        <nav class="mobile-menu-links">
            <a href="#funziona" class="mobile-link">Come funziona</a>
            <a href="#perche" class="mobile-link">Perché FidelUp</a>
            <a href="#prezzi" class="mobile-link">Prezzi</a>
            <a href="#faq" class="mobile-link">FAQ</a>
            <a href="#prenota" class="btn btn-primary mobile-link" style="text-align: center; margin-top: 24px;">Prenota visita gratuita</a>
        </nav>
    </div>

    <!-- 01 HERO -->
    <section class="hero">
        <div class="container hero-grid">
            <div class="hero-content">
                <div class="hero-eyebrow">PER LE PICCOLE ATTIVITÀ LOCALI</div>
                <h1>Ogni giorno entrano nuovi clienti.<br><span class="text-primary">Ma quanti ritornano?</span></h1>
                <p>FidelUp è il servizio di fidelizzazione che fa tornare i tuoi clienti. Installiamo e gestiamo tutto noi. Tu continui a gestire la tua attività.</p>
                <a href="#prenota" class="btn btn-primary">→ Prenota una visita gratuita</a>
                <div class="hero-microcopy">Veniamo nella tua attività. Ti spieghiamo tutto. Nessun impegno.</div>
            </div>
            <div class="nino-hero">
                <div class="nino-bubble gsap-anim-bubble">Ogni giorno entra qualcuno che non rivedremo mai più. E se potessimo cambiarlo?</div>
                <img src="assets/nino.png" alt="Nino, mascotte FidelUp" class="gsap-anim-nino">
            </div>
        </div>
    </section>

    <!-- 02 IL PROBLEMA -->
    <section class="problema" id="problema">
        <div class="container">
            <h2>Il problema non è trovare clienti.<br>È farli tornare.</h2>
            <p>Puoi avere un ottimo servizio, prezzi competitivi e clienti soddisfatti. Ma quando quel cliente esce dalla porta, non hai nessuna garanzia che tornerà. Passano i giorni. Arriva un concorrente. Il cliente si dimentica di te. E tu ricomincia da capo a cercarne un altro.</p>
            
            <div class="stats-grid">
                <div class="stat-card gsap-stat">
                    <div class="stat-num">7×</div>
                    <div class="stat-text">Acquisire un nuovo cliente costa fino a 7 volte di più che fidelizzarne uno esistente</div>
                    <div class="stat-source">Fonte: Harvard Business Review</div>
                </div>
                <div class="stat-card gsap-stat">
                    <div class="stat-num">+67%</div>
                    <div class="stat-text">I clienti fidelizzati spendono in media il 67% in più rispetto ai clienti occasionali</div>
                    <div class="stat-source">Fonte: Bain & Company</div>
                </div>
                <div class="stat-card gsap-stat">
                    <div class="stat-num">80/20</div>
                    <div class="stat-text">L'80% del fatturato di un'attività proviene dal 20% dei clienti più fedeli</div>
                    <div class="stat-source">Fonte: Principio di Pareto</div>
                </div>
            </div>

            <p style="font-weight: 700; color: white;">Il problema non è che non hai clienti.<br>È che troppo spesso li lasci andare senza un motivo concreto per tornare.</p>

            <div class="problema-nino-wrap gsap-nino-2">
                <img src="assets/nino.png" alt="Nino, mascotte FidelUp">
                <span>"Sai quanti dei tuoi clienti di questo mese non torneranno mai più?"</span>
            </div>
        </div>
    </section>

    <!-- 03 LA SVOLTA -->
    <section class="svolta" id="funziona">
        <div class="container">
            <h2>E se quel cliente che esce oggi ricevesse domani un motivo concreto per tornare?</h2>
            <p>FidelUp crea un sistema semplice per mantenere il rapporto con i tuoi clienti anche dopo che hanno lasciato la tua attività. Il cliente partecipa, riceve un vantaggio e ha un motivo reale per tornare. Tu non devi costruire tutto questo da solo.</p>
            
            <div class="svolta-visual">
                <div class="cliente-anim">
                    <div class="cliente-icon">🚶</div>
                    <div class="cliente-arrow">↻</div>
                    <div class="cliente-icon">💖</div>
                </div>
                <div class="svolta-nino-bubble gsap-nino-3">
                    "Da qui in poi la storia cambia. Perché ogni visita diventa l'inizio di una relazione."
                    <div style="position:absolute; left:-10px; top:50%; width:20px; height:20px; background:var(--surface-green); transform:translateY(-50%) rotate(45deg);"></div>
                </div>
                <img src="assets/nino.png" alt="Nino, mascotte FidelUp">
            </div>
        </div>
    </section>

    <!-- 04 TU FAI IL TUO LAVORO -->
    <section class="tu-fai">
        <div class="container">
            <h2>TU FAI IL TUO LAVORO.<br><span class="text-primary">NOI PENSIAMO ALLA FIDELIZZAZIONE.</span></h2>
            
            <div class="steps-grid">
                <div class="step-card gsap-step">
                    <div class="step-num">01</div>
                    <h3>Veniamo da te</h3>
                    <p>Installiamo il materiale direttamente nella tua attività e prepariamo tutto. Nessun corso, nessun manuale.</p>
                </div>
                <div class="step-card gsap-step">
                    <div class="step-num">02</div>
                    <h3>Prepariamo il sistema</h3>
                    <p>Scegliamo insieme il meccanismo più adatto ai tuoi clienti e lo personalizziamo con il tuo brand.</p>
                </div>
                <div class="step-card gsap-step">
                    <div class="step-num">03</div>
                    <h3>Ti accompagniamo nel tempo</h3>
                    <p>FidelUp non è un software che compri e devi imparare a usare. È un servizio che gestiamo insieme a te, ogni mese.</p>
                </div>
            </div>

            <div class="tu-fai-chiusura">Tu non devi diventare un esperto di marketing.</div>
        </div>
    </section>

    <!-- 05 PER IL TUO CLIENTE È SEMPLICE -->
    <section class="semplice">
        <div class="container">
            <h2>PER IL TUO CLIENTE È SEMPLICE.</h2>
            
            <div class="steps-grid">
                <div class="semplice-card gsap-semplice">
                    <div class="step-num">01</div>
                    <h3>Scansiona</h3>
                    <p>Il cliente vede il materiale FidelUp nella tua attività e partecipa dal proprio smartphone.</p>
                </div>
                <div class="semplice-card gsap-semplice">
                    <div class="step-num">02</div>
                    <h3>Partecipa</h3>
                    <p>Riceve il vantaggio o accede al meccanismo che hai scelto.</p>
                </div>
                <div class="semplice-card gsap-semplice">
                    <div class="step-num">03</div>
                    <h3>Ha un motivo per tornare</h3>
                    <p>La relazione non finisce quando esce dalla porta.</p>
                </div>
            </div>

            <div class="semplice-chiusura">Niente app da scaricare.<br>Niente procedure complicate.</div>
        </div>
    </section>

    <!-- 06 I MECCANISMI -->
    <section class="meccanismi">
        <div class="container">
            <div class="meccanismi-header">
                <h2>Troviamo il modo giusto per far tornare i tuoi clienti.</h2>
                <p style="max-width: 700px; margin: 20px auto 0;">Ogni attività è diversa. Per questo non imponiamo un unico meccanismo: scegliamo quello più adatto alla tua clientela e ai tuoi obiettivi.</p>
            </div>

            <div class="meccanismi-grid">
                <div class="mecc-card gsap-mecc">
                    <div class="mecc-icon">🎡</div>
                    <h3>RUOTA DELLA FORTUNA</h3>
                    <p style="font-weight:700; color:var(--text-dark);">Un motivo per tornare, già dalla prima visita.</p>
                    <p>Il cliente gira la ruota e scopre immediatamente il proprio vantaggio.</p>
                    <div class="mecc-ideale">Ideale per: creare coinvolgimento e incentivare il ritorno immediato.</div>
                </div>
                
                <div class="mecc-card gsap-mecc">
                    <div class="mecc-icon">⭐</div>
                    <h3>RACCOLTA PUNTI</h3>
                    <p style="font-weight:700; color:var(--text-dark);">Ogni acquisto vale. Al traguardo, arriva il premio.</p>
                    <p>I clienti accumulano punti ad ogni visita. Quando raggiungono il traguardo, ricevono il premio che hai scelto tu.</p>
                    <div class="mecc-ideale">Ideale per: aumentare la frequenza di visita nel tempo.</div>
                </div>

                <div class="mecc-card gsap-mecc">
                    <div class="mecc-icon">❤️</div>
                    <h3>CLIENTE DI FIDUCIA</h3>
                    <p style="font-weight:700; color:var(--text-dark);">Trasforma i clienti abituali in una clientela ancora più fedele.</p>
                    <p>Vantaggi e iniziative riservate a chi sceglie più volte la tua attività.</p>
                    <div class="mecc-ideale">Ideale per: aumentare frequenza e senso di appartenenza.</div>
                </div>

                <div class="mecc-card gsap-mecc">
                    <div class="mecc-icon">🎁</div>
                    <h3>OFFERTA DI BENVENUTO</h3>
                    <p style="font-weight:700; color:var(--text-dark);">Dai al nuovo cliente un motivo per lasciarti i suoi dati.</p>
                    <p>Un vantaggio immediato che trasforma la prima visita in una relazione che può continuare.</p>
                    <div class="mecc-ideale">Ideale per: iniziare a costruire una clientela abituale.</div>
                </div>
            </div>
        </div>
    </section>

    <!-- 07 QUASI NIENTE -->
    <section class="quasi-niente">
        <div class="container">
            <h2>Quasi niente.<br>È questo il punto.</h2>
            
            <div class="qn-grid">
                <div class="qn-col gsap-qn">
                    <h3>TU</h3>
                    <div class="qn-item">Accogli i clienti</div>
                    <div class="qn-item">Fai il tuo lavoro</div>
                    <div class="qn-item">Presenti il vantaggio</div>
                    <div class="qn-item">Consegni i premi</div>
                </div>
                <div class="qn-col fidelup gsap-qn">
                    <h3>FIDELUP</h3>
                    <div class="qn-item">Configura il sistema</div>
                    <div class="qn-item">Personalizza l'esperienza</div>
                    <div class="qn-item">Installa il materiale</div>
                    <div class="qn-item">Gestisce ogni mese</div>
                    <div class="qn-item">Ti accompagna sempre</div>
                </div>
            </div>

            <div class="qn-chiusura">
                Tu gestisci la tua attività.<br>
                <span class="text-primary">Noi gestiamo la fidelizzazione.</span>
            </div>
        </div>
    </section>

    <!-- 08 PERCHÉ FIDELUP -->
    <section class="perche" id="perche">
        <div class="container">
            <h2>Non ti vendiamo un software.<br>Veniamo da te.</h2>
            
            <div class="table-wrap gsap-table">
                <div class="table-row table-head">
                    <div>Un software</div>
                    <div>FidelUp</div>
                </div>
                <div class="table-row">
                    <div class="table-cell cell-bad">Ti lascia configurare tutto da solo</div>
                    <div class="table-cell cell-good">Veniamo fisicamente nella tua attività</div>
                </div>
                <div class="table-row">
                    <div class="table-cell cell-bad">Devi imparare la piattaforma</div>
                    <div class="table-cell cell-good">Ti spieghiamo tutto — non tocchi niente</div>
                </div>
                <div class="table-row">
                    <div class="table-cell cell-bad">Devi gestirlo autonomamente</div>
                    <div class="table-cell cell-good">Ti accompagniamo ogni mese</div>
                </div>
                <div class="table-row">
                    <div class="table-cell cell-bad">Assistenza solo a distanza</div>
                    <div class="table-cell cell-good">Referente diretto nel tuo locale</div>
                </div>
                <div class="table-row">
                    <div class="table-cell cell-bad">Acquisti uno strumento</div>
                    <div class="table-cell cell-good">Ottieni un servizio completamente gestito</div>
                </div>
                <div class="table-row">
                    <div class="table-cell cell-bad">Prova di 7 giorni</div>
                    <div class="table-cell cell-good">Primo mese completamente gratuito</div>
                </div>
            </div>

            <div class="perche-chiusura">
                La differenza non è quello che utilizzi.<br>
                È quanto lavoro devi fare tu.
            </div>
        </div>
    </section>

    <!-- 09 IL PRIMO MESE -->
    <section class="primo-mese">
        <div class="container">
            <div class="pm-eyebrow">PROVALO NELLA TUA ATTIVITÀ</div>
            <h2>Il primo mese è €0.</h2>
            <p>Installiamo FidelUp nella tua attività e lo provi direttamente con i tuoi clienti. Puoi vedere come funziona, capire come reagiscono i tuoi clienti e valutare il servizio prima di decidere. Se vuoi continuare, continui. Se non vuoi, ti fermi.</p>
            
            <div class="pm-zero gsap-zero">€0</div>
            
            <div class="pm-benefits">
                <div class="pm-benefit"><span>€0</span> Primo mese gratuito</div>
                <div class="pm-benefit"><span>🔓</span> Nessun vincolo — decidi tu se continuare</div>
                <div class="pm-benefit"><span>✓</span> Tutto gestito da noi — non devi imparare nulla</div>
            </div>

            <a href="#prenota" class="btn btn-white">→ Voglio provare FidelUp</a>

            <div class="pm-nino">
                <img src="assets/nino.png" alt="Nino, mascotte FidelUp">
                <span style="font-weight: 600; font-size: 1.1rem; text-align: left;">"Zero rischi. Zero tecnica. Vieni a vederlo direttamente nella tua attività."</span>
            </div>
        </div>
    </section>

    <!-- 10 PREZZI -->
    <section class="prezzi" id="prezzi">
        <div class="container">
            <h2>Quanto costa continuare dopo il primo mese?</h2>
            
            <div class="pricing-cards">
                <div class="p-card gsap-price">
                    <h3>BASE</h3>
                    <div class="p-price">39,99<span>€/mese</span></div>
                    <ul class="p-features">
                        <li>1 meccanismo a scelta</li>
                        <li>Configurazione inclusa</li>
                        <li>Installazione gratuita</li>
                        <li>Gestione FidelUp</li>
                    </ul>
                </div>
                
                <div class="p-card premium gsap-price">
                    <div class="p-badge">⭐ IL PIÙ SCELTO</div>
                    <h3>PREMIUM</h3>
                    <div class="p-price text-primary">47,99<span>€/mese</span></div>
                    <ul class="p-features">
                        <li>1 meccanismo a scelta</li>
                        <li>Personalizzazione brand</li>
                        <li>Gestione continuativa</li>
                        <li>Report mensile</li>
                        <li>Assistenza diretta</li>
                    </ul>
                </div>

                <div class="p-card gsap-price">
                    <h3>VIP</h3>
                    <div class="p-price">64,99<span>€/mese</span></div>
                    <ul class="p-features">
                        <li>Fino a 3 meccanismi</li>
                        <li>Gestione completa</li>
                        <li>Personalizzazione totale</li>
                        <li>Consulenza dedicata</li>
                    </ul>
                </div>
            </div>

            <div class="prezzi-chiusura">🎁 Il primo mese è sempre gratuito, per tutti i piani.</div>
        </div>
    </section>

    <!-- 11 FAQ -->
    <section class="faq" id="faq">
        <div class="container">
            <h2 class="text-center">Domande Frequenti</h2>
            
            <div class="faq-wrapper">
                <div class="faq-item">
                    <button class="faq-btn" aria-expanded="false" aria-controls="faq-a-1" id="faq-q-1">
                        <span>Devo imparare a usare un software?</span>
                        <span class="faq-icon" aria-hidden="true">+</span>
                    </button>
                    <div class="faq-a" id="faq-a-1" role="region" aria-labelledby="faq-q-1">No. FidelUp è un servizio gestito. Configuriamo noi il sistema e ti accompagniamo nel tempo.</div>
                </div>
                
                <div class="faq-item">
                    <button class="faq-btn" aria-expanded="false" aria-controls="faq-a-2" id="faq-q-2">
                        <span>I miei clienti devono scaricare un'app?</span>
                        <span class="faq-icon" aria-hidden="true">+</span>
                    </button>
                    <div class="faq-a" id="faq-a-2" role="region" aria-labelledby="faq-q-2">No. Partecipano direttamente dal loro smartphone, senza scaricare nulla.</div>
                </div>
                
                <div class="faq-item">
                    <button class="faq-btn" aria-expanded="false" aria-controls="faq-a-3" id="faq-q-3">
                        <span>Devo comprare un tablet?</span>
                        <span class="faq-icon" aria-hidden="true">+</span>
                    </button>
                    <div class="faq-a" id="faq-a-3" role="region" aria-labelledby="faq-q-3">No. Il cliente utilizza il proprio telefono.</div>
                </div>

                <div class="faq-item">
                    <button class="faq-btn" aria-expanded="false" aria-controls="faq-a-4" id="faq-q-4">
                        <span>Quanto lavoro devo fare io?</span>
                        <span class="faq-icon" aria-hidden="true">+</span>
                    </button>
                    <div class="faq-a" id="faq-a-4" role="region" aria-labelledby="faq-q-4">Il minimo indispensabile. Tu continui a gestire la tua attività. Noi ci occupiamo della fidelizzazione.</div>
                </div>

                <div class="faq-item">
                    <button class="faq-btn" aria-expanded="false" aria-controls="faq-a-5" id="faq-q-5">
                        <span>Chi installa tutto?</span>
                        <span class="faq-icon" aria-hidden="true">+</span>
                    </button>
                    <div class="faq-a" id="faq-a-5" role="region" aria-labelledby="faq-q-5">Veniamo direttamente nella tua attività e prepariamo tutto insieme a te.</div>
                </div>

                <div class="faq-item">
                    <button class="faq-btn" aria-expanded="false" aria-controls="faq-a-6" id="faq-q-6">
                        <span>E dopo il primo mese?</span>
                        <span class="faq-icon" aria-hidden="true">+</span>
                    </button>
                    <div class="faq-a" id="faq-a-6" role="region" aria-labelledby="faq-q-6">Decidi liberamente se continuare. Il primo mese serve proprio a permetterti di provare FidelUp nella tua attività senza nessun rischio.</div>
                </div>
            </div>
        </div>
    </section>

    <!-- 12 CTA FINAL -->
    <section class="cta-final" id="prenota">
        <div class="container cta-grid">
            <div class="cta-text">
                <h2>Vieni a vedere come funziona nella tua attività.<br>Il primo mese è nostro.</h2>
                <p style="font-size: 1.2rem; font-weight: 500; color: var(--text-dark);">Veniamo nella tua attività, ti mostriamo come funziona FidelUp e valutiamo quale soluzione può essere più adatta ai tuoi clienti. Nessun impegno. Ti contattiamo per concordare giorno e orario.</p>
                
                <div class="cta-nino">
                    <img src="assets/nino.png" alt="Nino, mascotte FidelUp">
                    <span>"Hai domande? Scrivimi direttamente su WhatsApp — rispondo io di persona."</span>
                </div>

                <div class="contacts-info">
                    Giovanni Montaruli · Co-Founder FidelUp<br>
                    339 842 0279<br>
                    fidelup.info@gmail.com
                </div>
            </div>
            
            <div class="form-box">
                <form id="fidelup-form">
                    <div class="form-group">
                        <label for="nome">Nome e cognome</label>
                        <input type="text" id="nome" name="nome" required placeholder="Es. Mario Rossi">
                    </div>
                    <div class="form-group">
                        <label for="attivita">Nome della tua attività</label>
                        <input type="text" id="attivita" name="attivita" required placeholder="Es. Barberia Il Taglio">
                    </div>
                    <div class="form-group">
                        <label for="telefono">Numero di telefono</label>
                        <input type="tel" id="telefono" name="telefono" required placeholder="333 123 4567">
                    </div>
                    <div class="form-group">
                        <label for="citta">Città</label>
                        <input type="text" id="citta" name="citta" required placeholder="Es. Roma">
                    </div>
                    
                    <div class="form-group" style="margin-top: 24px;">
                        <label for="privacy" style="display:flex; gap:12px; font-weight:normal; font-size:0.95rem; align-items:flex-start; cursor: pointer;">
                            <input type="checkbox" id="privacy" name="privacy" required style="width:24px; height:24px; flex-shrink:0; accent-color: var(--primary);">
                            <span style="color: var(--text-muted); line-height: 1.4;">Acconsento al trattamento dei dati personali ai fini del contatto commerciale.</span>
                        </label>
                    </div>

                    <button type="submit" id="submitBtn" class="btn btn-primary" style="width: 100%; font-size: 1.2rem; padding: 20px; margin-top: 16px;">→ Prenota la visita gratuita</button>
                    <div style="text-align: center; margin-top: 16px; font-size: 0.9rem; color: var(--text-muted);">Ti contattiamo entro 24 ore. Nessuno spam, nessun impegno.</div>
                    
                    <div id="form-msg" class="form-message"></div>
                </form>
            </div>
        </div>
    </section>

    <!-- 13 FOOTER -->
    <footer>
        <div class="container">
            <div class="footer-logo">Fidel<span class="text-primary">Up</span></div>
            <div class="footer-links">
                <a href="#funziona">Come funziona</a>
                <a href="#perche">Perché FidelUp</a>
                <a href="#prezzi">Prezzi</a>
            </div>
            <div style="font-size: 0.9rem; color: rgba(255,255,255,0.4);">
                &copy; 2026 FidelUp. Tutti i diritti riservati.<br>
                Tu gestisci la tua attività. Noi gestiamo la fidelizzazione.
            </div>
        </div>
    </footer>

    <!-- WHATSAPP FLOAT -->
    <a href="https://wa.me/393398420279?text=Ciao%20Giovanni%2C%20ho%20visto%20FidelUp%20e%20vorrei%20saperne%20di%20pi%C3%B9." class="wa-float" target="_blank" rel="noopener noreferrer" aria-label="Contattaci su WhatsApp">
        <svg viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.032c0 2.148.563 4.248 1.633 6.096L.103 24l6.02-1.574A11.968 11.968 0 0012.031 24c6.645 0 12.03-5.386 12.03-12.032S18.676 0 12.031 0zm0 22.012c-1.815 0-3.593-.487-5.148-1.41l-.369-.219-3.82.999 1.018-3.725-.24-.383a9.96 9.96 0 01-1.524-5.242c0-5.553 4.516-10.07 10.083-10.07 5.565 0 10.081 4.517 10.081 10.07s-4.516 10.07-10.081 10.07zm5.534-7.558c-.303-.153-1.794-.886-2.074-.988-.28-.101-.484-.152-.687.153-.203.304-.784.988-.962 1.189-.178.203-.356.228-.66.076-.303-.153-1.28-.472-2.438-1.503-.902-.803-1.51-1.794-1.688-2.098-.178-.304-.019-.468.132-.62.136-.137.303-.355.455-.533.151-.178.202-.305.303-.508.101-.203.05-.381-.026-.533-.076-.152-.687-1.656-.941-2.266-.247-.591-.497-.511-.687-.52-.178-.008-.382-.01-.585-.01-.203 0-.533.076-.812.381-.279.305-1.066 1.042-1.066 2.54 0 1.498 1.091 2.946 1.244 3.149.152.203 2.148 3.278 5.204 4.596.726.313 1.293.5 1.737.641.729.232 1.393.199 1.916.12.585-.088 1.794-.733 2.048-1.442.253-.709.253-1.316.178-1.442-.075-.126-.279-.202-.583-.355z"/></svg>
    </a>

    <script>
        // Header blur
        const header = document.getElementById('header');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.style.background = 'rgba(250, 250, 250, 0.95)';
                header.style.boxShadow = '0 4px 20px rgba(0,0,0,0.05)';
            } else {
                header.style.background = 'rgba(250, 250, 250, 0.8)';
                header.style.boxShadow = 'none';
            }
        }, { passive: true });

        // Mobile menu
        const mobileMenuBtn = document.getElementById('open-menu-btn');
        const closeMenuBtn  = document.getElementById('close-menu-btn');
        const mobileMenuOverlay = document.getElementById('mobile-menu');
        const mobileLinks = document.querySelectorAll('.mobile-link');

        function openMenu() {
            mobileMenuOverlay.classList.add('open');
            document.body.style.overflow = 'hidden';
        }

        function closeMenu() {
            mobileMenuOverlay.classList.remove('open');
            document.body.style.overflow = '';
        }

        if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', openMenu);
        if (closeMenuBtn)  closeMenuBtn.addEventListener('click', closeMenu);
        mobileLinks.forEach(link => link.addEventListener('click', closeMenu));

        // FAQ accordion
        document.querySelectorAll('.faq-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const item = btn.closest('.faq-item');
                const answer = document.getElementById(btn.getAttribute('aria-controls'));
                const isOpen = item.classList.contains('active');

                document.querySelectorAll('.faq-item').forEach(i => {
                    i.classList.remove('active');
                    const a = i.querySelector('.faq-a');
                    const b = i.querySelector('.faq-btn');
                    if (a) a.style.display = 'none';
                    if (b) b.setAttribute('aria-expanded', 'false');
                });

                if (!isOpen) {
                    item.classList.add('active');
                    if (answer) answer.style.display = 'block';
                    btn.setAttribute('aria-expanded', 'true');
                }
            });
        });

        // Form submission
        const form = document.getElementById('fidelup-form');
        const btn  = document.getElementById('submitBtn');
        const msgDiv = document.getElementById('form-msg');
        const WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbypPD56D6_kb0w1H9mOGaV8JubjSDk1xwd_3pw9Jq4VkEACab_3cZ0rFyxgqiIRN49d/exec';
        let isSubmitting = false;

        form.addEventListener('submit', async e => {
            e.preventDefault();
            if (isSubmitting) return;
            isSubmitting = true;

            btn.disabled = true;
            btn.textContent = 'Invio in corso...';
            btn.style.opacity = '0.7';
            msgDiv.style.display = 'none';

            // Inviamo stringhe vuote per i campi rimossi per non rompere il webhook
            const payload = {
                source: 'LandingPage_v6_Riveduta',
                nome:     document.getElementById('nome').value.trim(),
                attivita: document.getElementById('attivita').value.trim(),
                citta:    document.getElementById('citta').value.trim(),
                tipo:     '', 
                telefono: document.getElementById('telefono').value.trim(),
                email:    '', 
                messaggio: '', 
                privacy_consent: document.getElementById('privacy').checked ? 'si' : 'no',
                timestamp: new Date().toISOString()
            };

            try {
                await fetch(WEBHOOK_URL, {
                    method: 'POST',
                    mode: 'no-cors',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                msgDiv.innerHTML = '✅ <strong>Richiesta inviata.</strong><br>Ti contatteremo entro 24 ore per concordare la visita gratuita nel tuo locale.';
                msgDiv.style.backgroundColor = '#E8F5E9';
                msgDiv.style.color = '#1B5E20';
                msgDiv.style.display = 'block';
                form.reset();
                btn.textContent = 'Richiesta inviata ✓';

                setTimeout(() => {
                    btn.disabled = false;
                    btn.textContent = '→ Prenota la visita gratuita';
                    btn.style.opacity = '1';
                    isSubmitting = false;
                }, 6000);

            } catch (error) {
                msgDiv.innerHTML = '❌ <strong>Errore di connessione.</strong><br>Riprova più tardi o contattaci direttamente.';
                msgDiv.style.backgroundColor = '#FFEBEE';
                msgDiv.style.color = '#B71C1C';
                msgDiv.style.display = 'block';
                btn.disabled = false;
                btn.textContent = 'Riprova';
                btn.style.opacity = '1';
                isSubmitting = false;
            }
        });

        // GSAP Animations
        window.addEventListener('load', () => {
            if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;
            gsap.registerPlugin(ScrollTrigger);

            const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
            if (prefersReduced) return;

            // Hero
            gsap.from('.gsap-anim-nino', { opacity: 0, x: 50, duration: 1, ease: 'power2.out' });
            gsap.from('.gsap-anim-bubble', { opacity: 0, y: 20, duration: 0.8, delay: 0.5, ease: 'back.out(1.5)' });

            // Problema stats
            gsap.from('.gsap-stat', {
                scrollTrigger: { trigger: '.problema', start: 'top 70%' },
                y: 40, opacity: 0, duration: 0.8, stagger: 0.2
            });

            // Svolta transition
            gsap.from('.cliente-anim', {
                scrollTrigger: { trigger: '.svolta', start: 'top 70%' },
                x: -50, opacity: 0, duration: 1
            });

            // Tu fai / Semplice steps
            gsap.from('.gsap-step', {
                scrollTrigger: { trigger: '.tu-fai', start: 'top 70%' },
                y: 40, opacity: 0, duration: 0.6, stagger: 0.2
            });
            gsap.from('.gsap-semplice', {
                scrollTrigger: { trigger: '.semplice', start: 'top 70%' },
                y: 40, opacity: 0, duration: 0.6, stagger: 0.2
            });

            // Meccanismi
            gsap.from('.gsap-mecc', {
                scrollTrigger: { trigger: '.meccanismi', start: 'top 70%' },
                y: 50, opacity: 0, duration: 0.6, stagger: 0.15
            });

            // Quasi Niente
            gsap.from('.gsap-qn', {
                scrollTrigger: { trigger: '.quasi-niente', start: 'top 70%' },
                y: 30, opacity: 0, duration: 0.6, stagger: 0.2
            });

            // Perche table
            gsap.from('.gsap-table', {
                scrollTrigger: { trigger: '.perche', start: 'top 70%' },
                y: 30, opacity: 0, duration: 0.8
            });

            // Primo mese
            gsap.from('.gsap-zero', {
                scrollTrigger: { trigger: '.primo-mese', start: 'top 70%' },
                scale: 0.5, opacity: 0, duration: 1, ease: 'back.out(1.5)'
            });

            // Pricing
            gsap.from('.gsap-price', {
                scrollTrigger: { trigger: '.prezzi', start: 'top 70%' },
                y: 40, opacity: 0, duration: 0.8, stagger: 0.2
            });
        });
    </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
