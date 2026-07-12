import urllib.request
import base64

def get_base64_from_url(url):
    print(f"Downloading & Embedding: {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            img_data = response.read()
            b64_data = base64.b64encode(img_data).decode('utf-8')
            return f"data:image/jpeg;base64,{b64_data}"
    except Exception as e:
        print(f"Failed to embed {url}: {e}")
        # Return a generic transparent pixel
        return "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"

def build_demo():
    print("Generating ultra-rich embedded base64 HTML for Ayna Clinic...")
    
    imgs = {
        "hero": get_base64_from_url("https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?w=1200&q=70"),
        "about": get_base64_from_url("https://images.pexels.com/photos/5327656/pexels-photo-5327656.jpeg?auto=compress&cs=tinysrgb&w=800"), # Male doctor
        "cat1": get_base64_from_url("https://images.unsplash.com/photo-1515377905703-c4788e51af15?w=600&q=70"), 
        "cat2": get_base64_from_url("https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?w=600&q=70"), 
        "cat3": get_base64_from_url("https://images.unsplash.com/photo-1522337660859-02fbefca4702?w=600&q=70"), 
        "cat4": get_base64_from_url("https://images.unsplash.com/photo-1580618672591-eb180b1a973f?w=600&q=70"),
        "whyus": get_base64_from_url("https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=800&q=70") # Clinic interior
    }

    html_content = f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ayna Clinic | Dr. Bilal Keşkek - Medikal Estetik & Cilt Sağlığı</title>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <!-- Phosphor Icons -->
    <script src="https://unpkg.com/@phosphor-icons/web"></script>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        base: "#FCFCFC",
                        surface: "#FFFFFF",
                        accent: "#D4AF37", /* Pure Gold */
                        accentdark: "#B5952F",
                        darktext: "#1A1A1A", 
                        graytext: "#666666"
                    }},
                    fontFamily: {{
                        sans: ['Outfit', 'sans-serif'],
                        serif: ['Playfair Display', 'serif'],
                    }},
                    boxShadow: {{
                        'premium': '0 20px 40px -15px rgba(212, 175, 55, 0.15)',
                    }}
                }}
            }}
        }}
    </script>

    <style>
        body {{
            background-color: #FCFCFC;
            color: #1A1A1A;
            overflow-x: hidden;
        }}

        .hero-overlay {{
            background: linear-gradient(to right, rgba(26, 26, 26, 0.85), rgba(26, 26, 26, 0.3));
        }}
        
        .float-anim {{
            animation: float 6s ease-in-out infinite;
        }}
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-15px); }}
            100% {{ transform: translateY(0px); }}
        }}

        .faq-answer {{
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease-out;
        }}
        .faq-item.active .faq-answer {{
            max-height: 400px;
        }}
        .faq-item.active .faq-icon {{
            transform: rotate(45deg);
        }}
    </style>
</head>
<body class="antialiased selection:bg-accent selection:text-white">

    <!-- 1. Topbar -->
    <div class="bg-darktext text-white py-2 px-6 md:px-10 flex justify-between items-center text-xs md:text-sm font-light">
        <div class="flex items-center gap-6">
            <span class="flex items-center gap-2"><i class="ph ph-map-pin text-accent"></i> Kardeşler Mah. Bağdat Caddesi 47/B, Sivas</span>
            <span class="hidden md:flex items-center gap-2"><i class="ph ph-clock text-accent"></i> Pzt-Cts: 09:00 - 18:30</span>
        </div>
        <div class="flex items-center gap-4">
            <a href="https://www.instagram.com/clinic_ayna/" target="_blank" class="hover:text-accent transition-colors"><i class="ph ph-instagram-logo text-lg"></i></a>
            <a href="#" class="hover:text-accent transition-colors"><i class="ph ph-whatsapp-logo text-lg"></i></a>
        </div>
    </div>

    <!-- 2. Navbar -->
    <nav class="sticky top-0 w-full z-50 bg-surface/95 backdrop-blur-md border-b border-darktext/10 p-6 md:px-10 flex justify-between items-center shadow-sm">
        <a href="#" class="flex flex-col text-darktext items-center md:items-start">
            <span class="text-2xl md:text-3xl font-serif font-bold tracking-widest text-darktext">Ayna Clinic</span>
            <span class="text-[10px] uppercase tracking-[0.2em] font-sans font-medium text-accent">Dr. Bilal Keşkek</span>
        </a>
        <div class="hidden lg:flex items-center gap-8 text-sm uppercase tracking-wide font-medium text-darktext">
            <a href="#anasayfa" class="hover:text-accent transition-colors">Ana Sayfa</a>
            <a href="#hakkimizda" class="hover:text-accent transition-colors">Hakkımızda</a>
            <a href="#tedaviler" class="hover:text-accent transition-colors">Tedaviler</a>
            <a href="#nedenbiz" class="hover:text-accent transition-colors">Neden Biz?</a>
            <a href="#sss" class="hover:text-accent transition-colors">S.S.S</a>
            <a href="#iletisim" class="hover:text-accent transition-colors">İletişim</a>
        </div>
        <a href="#iletisim" class="hidden lg:inline-flex items-center gap-2 bg-darktext text-accent px-6 py-3 rounded-md text-sm uppercase tracking-wide font-medium hover:bg-accent hover:text-white transition-colors">
            <i class="ph-fill ph-calendar-plus"></i> Randevu Al
        </a>
        <button class="lg:hidden text-2xl text-darktext"><i class="ph ph-list"></i></button>
    </nav>

    <!-- 3. Mega Hero Section -->
    <section id="anasayfa" class="relative pt-20 pb-32 lg:pt-32 lg:pb-40 overflow-hidden bg-darktext">
        <div class="absolute inset-0 z-0">
            <img src="{imgs['hero']}" class="w-full h-full object-cover opacity-80" alt="Medical Aesthetics">
            <div class="absolute inset-0 hero-overlay"></div>
        </div>
        
        <div class="max-w-[1400px] mx-auto px-6 md:px-10 relative z-10">
            <div class="flex flex-col lg:flex-row items-center gap-16">
                <!-- Sol Taraf -->
                <div class="w-full lg:w-1/2">
                    <div class="inline-flex items-center gap-2 px-4 py-2 bg-accent/20 border border-accent/30 rounded-full text-accent font-bold text-xs uppercase tracking-widest mb-6">
                        <span class="w-2 h-2 rounded-full bg-accent animate-pulse"></span>
                        Medikal Estetik & Cilt Sağlığı
                    </div>
                    <h1 class="text-5xl md:text-6xl lg:text-7xl font-serif text-white leading-[1.1] mb-6">
                        Güzelliğinize <br>
                        <span class="italic text-accent">Tıbbi Dokunuş.</span>
                    </h1>
                    <p class="text-lg text-white/80 mb-10 leading-relaxed max-w-lg font-light">
                        Dr. Bilal Keşkek uzmanlığında; botoks, dolgu, gençlik aşısı ve gelişmiş saç tedavileri ile doğal görünümünüzü koruyarak en iyi versiyonunuza ulaşın.
                    </p>
                    <div class="flex flex-wrap gap-4">
                        <a href="#iletisim" class="bg-accent text-white px-8 py-4 rounded-md text-sm uppercase tracking-wide font-bold hover:bg-white hover:text-darktext transition-all flex items-center gap-2">
                            Ön Görüşme Ayarla <i class="ph-bold ph-arrow-right"></i>
                        </a>
                        <a href="#tedaviler" class="bg-transparent border border-white/30 text-white px-8 py-4 rounded-md text-sm uppercase tracking-wide font-bold hover:bg-white/10 transition-all">
                            Tedavileri İncele
                        </a>
                    </div>
                    
                    <!-- Social Proof -->
                    <div class="mt-12 flex items-center gap-6">
                        <div class="flex -space-x-4">
                            <div class="w-12 h-12 rounded-full border-2 border-darktext bg-white flex items-center justify-center text-accent font-bold text-xl"><i class="ph-fill ph-check-circle"></i></div>
                            <div class="w-12 h-12 rounded-full border-2 border-darktext bg-white flex items-center justify-center text-accent font-bold text-xl"><i class="ph-fill ph-check-circle"></i></div>
                            <div class="w-12 h-12 rounded-full border-2 border-darktext bg-white flex items-center justify-center text-accent font-bold text-xl"><i class="ph-fill ph-check-circle"></i></div>
                        </div>
                        <div class="text-sm font-bold text-white">
                            Sivas'ta Binlerce <br><span class="text-accent font-medium">Mutlu Danışan</span>
                        </div>
                    </div>
                </div>

                <!-- Sağ Taraf / Görsel & Rozet -->
                <div class="w-full lg:w-1/2 relative hidden md:block">
                    <!-- Rozet -->
                    <div class="absolute top-10 right-10 bg-white/10 backdrop-blur-md border border-white/20 p-6 rounded-2xl shadow-2xl z-20 flex flex-col items-center gap-2 float-anim text-center">
                        <i class="ph-fill ph-shield-check text-4xl text-accent"></i>
                        <p class="font-bold text-white text-xl">100%</p>
                        <p class="text-[10px] text-white/80 font-bold uppercase tracking-widest">FDA Onaylı<br>Ürünler</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Counters (İstatistikler) -->
    <section class="py-12 bg-accent relative z-20">
        <div class="max-w-[1400px] mx-auto px-6 md:px-10">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center text-darktext">
                <div>
                    <i class="ph-light ph-certificate text-4xl mb-4 mx-auto opacity-80"></i>
                    <h3 class="text-4xl font-serif font-bold mb-1">10+</h3>
                    <p class="text-xs font-bold uppercase tracking-widest opacity-80">Yıllık Tecrübe</p>
                </div>
                <div>
                    <i class="ph-light ph-users-three text-4xl mb-4 mx-auto opacity-80"></i>
                    <h3 class="text-4xl font-serif font-bold mb-1">5000+</h3>
                    <p class="text-xs font-bold uppercase tracking-widest opacity-80">Başarılı İşlem</p>
                </div>
                <div>
                    <i class="ph-light ph-first-aid text-4xl mb-4 mx-auto opacity-80"></i>
                    <h3 class="text-4xl font-serif font-bold mb-1">Modern</h3>
                    <p class="text-xs font-bold uppercase tracking-widest opacity-80">Klinik Ortamı</p>
                </div>
                <div>
                    <i class="ph-light ph-heart text-4xl mb-4 mx-auto opacity-80"></i>
                    <h3 class="text-4xl font-serif font-bold mb-1">%100</h3>
                    <p class="text-xs font-bold uppercase tracking-widest opacity-80">Memnuniyet</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Hakkımızda (Doktor Profili) -->
    <section id="hakkimizda" class="py-24 bg-base">
        <div class="max-w-[1400px] mx-auto px-6 md:px-10">
            <div class="flex flex-col lg:flex-row items-center gap-16">
                <!-- Görsel -->
                <div class="w-full lg:w-5/12">
                    <div class="relative rounded-t-full rounded-b-3xl overflow-hidden shadow-premium border-8 border-white">
                        <img src="{imgs['about']}" alt="Dr Bilal Keşkek" class="w-full h-auto object-cover aspect-[3/4]">
                        <div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-darktext/90 to-transparent p-8 pt-20">
                            <h3 class="text-white text-2xl font-serif font-bold">Dr. Bilal Keşkek</h3>
                            <p class="text-accent text-sm tracking-widest uppercase mt-1">Medikal Estetik Hekimi</p>
                        </div>
                    </div>
                </div>
                
                <!-- İçerik -->
                <div class="w-full lg:w-7/12">
                    <span class="text-accent tracking-widest uppercase text-sm font-bold mb-4 block flex items-center gap-2">
                        <i class="ph-fill ph-user-circle text-xl"></i> Hekimimiz Hakkında
                    </span>
                    <h2 class="text-4xl md:text-5xl font-serif mb-8 text-darktext leading-tight">
                        Tıbbın ve Estetiğin <br>
                        <span class="italic text-accent">Kusursuz Uyumu.</span>
                    </h2>
                    
                    <p class="text-graytext mb-6 leading-relaxed text-lg font-light">
                        Ayna Clinic olarak, estetik görünüme daima tıbbi bir perspektiften yaklaşıyoruz. Sivas'taki kliniğimizde, güzelliğinizi ön plana çıkarırken doğal görünümünüzü ve yüz anatomik bütünlüğünüzü korumayı temel ilke ediniyoruz.
                    </p>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                        <div class="flex items-start gap-4 p-4 bg-white rounded-xl shadow-sm border border-darktext/5">
                            <div class="w-10 h-10 bg-accent/10 rounded-full flex items-center justify-center text-accent shrink-0">
                                <i class="ph-fill ph-drop"></i>
                            </div>
                            <div>
                                <h4 class="font-bold text-darktext">Kişiye Özel Protokol</h4>
                                <p class="text-sm text-graytext mt-1">Her cilt tipi ve anatomik yapıya özel milimetrik hesaplamalar.</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4 p-4 bg-white rounded-xl shadow-sm border border-darktext/5">
                            <div class="w-10 h-10 bg-accent/10 rounded-full flex items-center justify-center text-accent shrink-0">
                                <i class="ph-fill ph-shield-check"></i>
                            </div>
                            <div>
                                <h4 class="font-bold text-darktext">Güvenli İşlem</h4>
                                <p class="text-sm text-graytext mt-1">Yalnızca klinik etkinliği kanıtlanmış, dünya standartlarında ürünler.</p>
                            </div>
                        </div>
                    </div>
                    
                    <p class="text-graytext mb-8 leading-relaxed font-light">
                        Botoks, dermal dolgular, cilt yenileme protokolleri (Gençlik Aşısı, Mezoterapi) ve yenilikçi saç dökülme tedavilerinde (Cellbooster Hair) güvenli medikal yöntemler uyguluyoruz. Aynalara her baktığınızda en iyi halinizi görmeniz için buradayız.
                    </p>
                    
                    <div class="flex items-center gap-6">
                        <a href="#tedaviler" class="btn-primary inline-flex items-center gap-2 bg-darktext text-white px-8 py-4 rounded-md font-bold uppercase tracking-wide text-sm hover:bg-accent transition-colors">
                            Tüm Uygulamalar <i class="ph-bold ph-arrow-right"></i>
                        </a>
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Eo_circle_gold_letter-a.svg/512px-Eo_circle_gold_letter-a.svg.png" alt="Ayna Logo" class="h-12 w-12 opacity-30 grayscale mix-blend-multiply">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. Tedaviler / Hizmetler (Genişletilmiş Grid) -->
    <section id="tedaviler" class="py-24 bg-surface border-t border-darktext/5">
        <div class="max-w-[1400px] mx-auto px-6 md:px-10">
            <div class="text-center mb-16">
                <span class="text-accent tracking-widest uppercase text-sm font-bold mb-2 block">Klinik Uygulamalarımız</span>
                <h2 class="text-4xl md:text-5xl font-serif text-darktext">Medikal Estetik <span class="italic text-accent">Protokolleri</span></h2>
                <p class="text-graytext mt-4 max-w-2xl mx-auto font-light">Bilimin ışığında, doğal ve sağlıklı güzellik için uyguladığımız ameliyatsız medikal estetik işlemleri.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <!-- Card 1 -->
                <div class="group cursor-pointer bg-base rounded-2xl overflow-hidden shadow-sm border border-darktext/5 hover:shadow-premium transition-all duration-300">
                    <div class="relative aspect-[4/3] overflow-hidden">
                        <img src="{imgs['cat1']}" alt="Botoks ve Dolgu" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-darktext/10 group-hover:bg-darktext/30 transition-colors duration-300"></div>
                        <div class="absolute top-4 right-4 w-10 h-10 bg-white rounded-full flex items-center justify-center text-accent shadow-lg">
                            <i class="ph-fill ph-syringe"></i>
                        </div>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-serif text-darktext mb-3 group-hover:text-accent transition-colors">Dolgu & Botoks</h3>
                        <p class="text-graytext text-sm mb-4 leading-relaxed">Kırışıklık giderme ve hacim kazandırma amaçlı, altın oran hesaplı minimal dokunuşlar ve enjeksiyonlar.</p>
                        <span class="text-xs font-bold uppercase tracking-widest text-accent flex items-center gap-1">İncele <i class="ph-bold ph-caret-right"></i></span>
                    </div>
                </div>
                <!-- Card 2 -->
                <div class="group cursor-pointer bg-base rounded-2xl overflow-hidden shadow-sm border border-darktext/5 hover:shadow-premium transition-all duration-300">
                    <div class="relative aspect-[4/3] overflow-hidden">
                        <img src="{imgs['cat2']}" alt="PRP ve Mezoterapi" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-darktext/10 group-hover:bg-darktext/30 transition-colors duration-300"></div>
                        <div class="absolute top-4 right-4 w-10 h-10 bg-white rounded-full flex items-center justify-center text-accent shadow-lg">
                            <i class="ph-fill ph-drop"></i>
                        </div>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-serif text-darktext mb-3 group-hover:text-accent transition-colors">PRP & Mezoterapi</h3>
                        <p class="text-graytext text-sm mb-4 leading-relaxed">Cilt altı dokusunun kendi kendini yenilemesini sağlayan özel vitamin, mineral ve plazma kompleksleri.</p>
                        <span class="text-xs font-bold uppercase tracking-widest text-accent flex items-center gap-1">İncele <i class="ph-bold ph-caret-right"></i></span>
                    </div>
                </div>
                <!-- Card 3 -->
                <div class="group cursor-pointer bg-base rounded-2xl overflow-hidden shadow-sm border border-darktext/5 hover:shadow-premium transition-all duration-300">
                    <div class="relative aspect-[4/3] overflow-hidden">
                        <img src="{imgs['cat3']}" alt="Gençlik Aşısı" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-darktext/10 group-hover:bg-darktext/30 transition-colors duration-300"></div>
                        <div class="absolute top-4 right-4 w-10 h-10 bg-white rounded-full flex items-center justify-center text-accent shadow-lg">
                            <i class="ph-fill ph-sparkle"></i>
                        </div>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-serif text-darktext mb-3 group-hover:text-accent transition-colors">Gençlik Aşısı</h3>
                        <p class="text-graytext text-sm mb-4 leading-relaxed">Saf hyalüronik asit ile cilde yoğun nem, parlaklık ve lifting etkisi sağlayan derinlemesine anti-aging bakımı.</p>
                        <span class="text-xs font-bold uppercase tracking-widest text-accent flex items-center gap-1">İncele <i class="ph-bold ph-caret-right"></i></span>
                    </div>
                </div>
                <!-- Card 4 -->
                <div class="group cursor-pointer bg-base rounded-2xl overflow-hidden shadow-sm border border-darktext/5 hover:shadow-premium transition-all duration-300">
                    <div class="relative aspect-[4/3] overflow-hidden">
                        <img src="{imgs['cat4']}" alt="Saç Tedavileri" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-darktext/10 group-hover:bg-darktext/30 transition-colors duration-300"></div>
                        <div class="absolute top-4 right-4 w-10 h-10 bg-white rounded-full flex items-center justify-center text-accent shadow-lg">
                            <i class="ph-fill ph-scissors"></i>
                        </div>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-serif text-darktext mb-3 group-hover:text-accent transition-colors">Saç Tedavileri</h3>
                        <p class="text-graytext text-sm mb-4 leading-relaxed">Dünyaca ünlü Cellbooster Hair kompleksi ve dökülme karşıtı medikal protokoller ile güçlü saç kökleri.</p>
                        <span class="text-xs font-bold uppercase tracking-widest text-accent flex items-center gap-1">İncele <i class="ph-bold ph-caret-right"></i></span>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-12">
                <a href="#iletisim" class="inline-flex items-center gap-2 border-2 border-darktext text-darktext px-8 py-4 rounded-md text-sm uppercase tracking-wide font-bold hover:bg-darktext hover:text-white transition-all">
                    Tüm İşlemleri Görüntüle <i class="ph-bold ph-arrow-right"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- 7. Neden Biz? (Why Us Feature) -->
    <section id="nedenbiz" class="py-24 bg-darktext text-white">
        <div class="max-w-[1400px] mx-auto px-6 md:px-10">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <div>
                    <span class="text-accent tracking-widest uppercase text-sm font-bold mb-4 block">Ayrıcalıklarımız</span>
                    <h2 class="text-4xl md:text-5xl font-serif mb-8 leading-tight">
                        Neden <span class="italic text-accent">Ayna Clinic?</span>
                    </h2>
                    
                    <div class="space-y-8">
                        <div class="flex gap-4">
                            <div class="w-14 h-14 rounded-full bg-accent/20 border border-accent/30 flex items-center justify-center text-accent shrink-0 text-2xl">
                                <i class="ph-fill ph-first-aid-kit"></i>
                            </div>
                            <div>
                                <h4 class="text-xl font-bold mb-2">Tam Donanımlı Klinik Ortamı</h4>
                                <p class="text-white/70 font-light leading-relaxed">Tüm işlemlerimiz, hastane standartlarında sterilizasyon sağlanan, Sağlık Bakanlığı onaylı muayenehanemizde gerçekleştirilmektedir.</p>
                            </div>
                        </div>
                        <div class="flex gap-4">
                            <div class="w-14 h-14 rounded-full bg-accent/20 border border-accent/30 flex items-center justify-center text-accent shrink-0 text-2xl">
                                <i class="ph-fill ph-scan"></i>
                            </div>
                            <div>
                                <h4 class="text-xl font-bold mb-2">Bütüncül Yaklaşım</h4>
                                <p class="text-white/70 font-light leading-relaxed">Sadece şikayet edilen bölgeyi değil, yüzün altın oranını ve cilt kalitesini bir bütün olarak değerlendirip işlem uyguluyoruz.</p>
                            </div>
                        </div>
                        <div class="flex gap-4">
                            <div class="w-14 h-14 rounded-full bg-accent/20 border border-accent/30 flex items-center justify-center text-accent shrink-0 text-2xl">
                                <i class="ph-fill ph-package"></i>
                            </div>
                            <div>
                                <h4 class="text-xl font-bold mb-2">Orijinal Ürün Garantisi</h4>
                                <p class="text-white/70 font-light leading-relaxed">Kliniğimizde barkodlu, soğuk zincir kurallarına uygun taşınmış, sadece dünyaca kabul görmüş premium marka ürünler kullanılır.</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="relative">
                    <div class="absolute inset-0 bg-accent transform translate-x-4 translate-y-4 rounded-3xl opacity-20"></div>
                    <img src="{imgs['whyus']}" alt="Klinik Ortamı" class="relative z-10 w-full h-auto rounded-3xl shadow-2xl border-4 border-white/10">
                </div>
            </div>
        </div>
    </section>

    <!-- 8. FAQ (Sıkça Sorulan Sorular) -->
    <section id="sss" class="py-24 bg-base">
        <div class="max-w-3xl mx-auto px-6 md:px-10">
            <div class="text-center mb-16">
                <span class="text-accent tracking-widest uppercase text-sm font-bold mb-2 block">S.S.S.</span>
                <h2 class="text-4xl font-serif text-darktext">Sıkça Sorulan <span class="italic text-accent">Sorular</span></h2>
            </div>
            
            <div class="space-y-4">
                <!-- FAQ 1 -->
                <div class="faq-item bg-white border border-darktext/10 rounded-xl overflow-hidden cursor-pointer" onclick="this.classList.toggle('active')">
                    <div class="p-6 flex justify-between items-center bg-white hover:bg-base transition-colors">
                        <h4 class="font-bold text-darktext pr-8">İşlemler ağrılı mıdır?</h4>
                        <i class="ph-bold ph-plus text-accent text-xl faq-icon transition-transform duration-300"></i>
                    </div>
                    <div class="faq-answer bg-base px-6">
                        <p class="pb-6 text-graytext font-light text-sm leading-relaxed">
                            İşlemlerimiz öncesinde lokal anestezik kremler kullanılarak bölge uyuşturulur. Ayrıca kullandığımız modern ince iğneler ve kanüller sayesinde ağrı hissi minimum seviyeye indirilmektedir.
                        </p>
                    </div>
                </div>
                <!-- FAQ 2 -->
                <div class="faq-item bg-white border border-darktext/10 rounded-xl overflow-hidden cursor-pointer" onclick="this.classList.toggle('active')">
                    <div class="p-6 flex justify-between items-center bg-white hover:bg-base transition-colors">
                        <h4 class="font-bold text-darktext pr-8">Dolgu ve Botoks'un kalıcılık süresi nedir?</h4>
                        <i class="ph-bold ph-plus text-accent text-xl faq-icon transition-transform duration-300"></i>
                    </div>
                    <div class="faq-answer bg-base px-6">
                        <p class="pb-6 text-graytext font-light text-sm leading-relaxed">
                            Botoks uygulamaları kişiden kişiye değişmekle birlikte ortalama 4-6 ay kalıcılığa sahiptir. Hyalüronik asit bazlı dermal dolgular ise uygulanan bölgeye ve ürünün yapısına göre 9 ila 18 ay arasında kalıcılık gösterir.
                        </p>
                    </div>
                </div>
                <!-- FAQ 3 -->
                <div class="faq-item bg-white border border-darktext/10 rounded-xl overflow-hidden cursor-pointer" onclick="this.classList.toggle('active')">
                    <div class="p-6 flex justify-between items-center bg-white hover:bg-base transition-colors">
                        <h4 class="font-bold text-darktext pr-8">Cellbooster Hair tedavisi kaç seans sürer?</h4>
                        <i class="ph-bold ph-plus text-accent text-xl faq-icon transition-transform duration-300"></i>
                    </div>
                    <div class="faq-answer bg-base px-6">
                        <p class="pb-6 text-graytext font-light text-sm leading-relaxed">
                            Saç dökülmesinin şiddetine ve saç köklerinin yapısına göre tedavi protokolü değişmektedir. Genellikle 2-3 hafta aralıklarla 4 ila 6 seanslık bir kür önerilmektedir.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 9. Call to Action (Banner) -->
    <section class="py-24 bg-accent text-darktext text-center px-6">
        <div class="max-w-4xl mx-auto">
            <h2 class="text-4xl md:text-5xl font-serif mb-6 font-bold">Cildiniz En Değerli Giysinizdir.</h2>
            <p class="text-darktext/80 text-lg mb-10 max-w-2xl mx-auto font-medium">
                Ücretsiz ön muayene ile cildinizin ihtiyaçlarını birlikte belirleyelim. Sağlıklı ve ışıldayan bir görünüm için Ayna Clinic'e davetlisiniz.
            </p>
            <a href="tel:+905555555555" class="inline-flex items-center gap-3 bg-darktext text-white px-10 py-5 rounded-md text-sm uppercase tracking-widest font-bold hover:bg-[#222] transition-all shadow-xl hover:shadow-2xl transform hover:-translate-y-1">
                <i class="ph-fill ph-phone-call text-xl"></i> Randevu İçin Arayın
            </a>
        </div>
    </section>

    <!-- 10. Footer (Massive, Comprehensive, Standard Business Footer) -->
    <footer id="iletisim" class="bg-[#111111] text-white pt-24 pb-10 border-t-4 border-darktext">
        <div class="max-w-[1400px] mx-auto px-6 md:px-10">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
                
                <!-- Col 1: Brand -->
                <div>
                    <a href="#" class="flex flex-col text-white mb-6">
                        <span class="text-3xl font-serif font-bold tracking-widest text-accent">Ayna Clinic</span>
                        <span class="text-[10px] uppercase tracking-[0.2em] font-sans font-medium text-white/50">Dr. Bilal Keşkek</span>
                    </a>
                    <p class="text-white/60 font-light mb-8 leading-relaxed">
                        Medikal estetik ve cilt sağlığında Sivas'ın güvenilir referans noktası. Uzman doktor kontrolünde güvenli işlemler.
                    </p>
                    <div class="flex items-center gap-4">
                        <a href="https://www.instagram.com/clinic_ayna/" target="_blank" class="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center hover:bg-accent hover:border-accent hover:text-darktext transition-all">
                            <i class="ph-fill ph-instagram-logo text-xl"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center hover:bg-accent hover:border-accent hover:text-darktext transition-all">
                            <i class="ph-fill ph-whatsapp-logo text-xl"></i>
                        </a>
                    </div>
                </div>

                <!-- Col 2: Quick Links -->
                <div>
                    <h3 class="text-xl font-serif mb-6 relative inline-block text-white">
                        Kurumsal
                        <span class="absolute -bottom-2 left-0 w-1/2 h-0.5 bg-accent"></span>
                    </h3>
                    <ul class="space-y-4 text-white/70 font-light">
                        <li><a href="#anasayfa" class="hover:text-accent transition-colors flex items-center gap-2"><i class="ph-bold ph-caret-right text-accent text-xs"></i> Ana Sayfa</a></li>
                        <li><a href="#hakkimizda" class="hover:text-accent transition-colors flex items-center gap-2"><i class="ph-bold ph-caret-right text-accent text-xs"></i> Dr. Bilal Keşkek</a></li>
                        <li><a href="#nedenbiz" class="hover:text-accent transition-colors flex items-center gap-2"><i class="ph-bold ph-caret-right text-accent text-xs"></i> Neden Biz?</a></li>
                        <li><a href="#sss" class="hover:text-accent transition-colors flex items-center gap-2"><i class="ph-bold ph-caret-right text-accent text-xs"></i> Sıkça Sorulan Sorular</a></li>
                        <li><a href="#" class="hover:text-accent transition-colors flex items-center gap-2"><i class="ph-bold ph-caret-right text-accent text-xs"></i> Aydınlatma ve KVKK Metni</a></li>
                    </ul>
                </div>

                <!-- Col 3: Categories -->
                <div>
                    <h3 class="text-xl font-serif mb-6 relative inline-block text-white">
                        Uygulamalar
                        <span class="absolute -bottom-2 left-0 w-1/2 h-0.5 bg-accent"></span>
                    </h3>
                    <ul class="space-y-4 text-white/70 font-light">
                        <li><a href="#tedaviler" class="hover:text-accent transition-colors flex items-center gap-2"><i class="ph-bold ph-caret-right text-accent text-xs"></i> Dudak ve Yüz Dolgusu</a></li>
                        <li><a href="#tedaviler" class="hover:text-accent transition-colors flex items-center gap-2"><i class="ph-bold ph-caret-right text-accent text-xs"></i> Kırışıklık Tedavisi (Botoks)</a></li>
                        <li><a href="#tedaviler" class="hover:text-accent transition-colors flex items-center gap-2"><i class="ph-bold ph-caret-right text-accent text-xs"></i> Somon DNA & Gençlik Aşısı</a></li>
                        <li><a href="#tedaviler" class="hover:text-accent transition-colors flex items-center gap-2"><i class="ph-bold ph-caret-right text-accent text-xs"></i> Mezoterapi & PRP</a></li>
                        <li><a href="#tedaviler" class="hover:text-accent transition-colors flex items-center gap-2"><i class="ph-bold ph-caret-right text-accent text-xs"></i> Cellbooster Saç Tedavisi</a></li>
                    </ul>
                </div>

                <!-- Col 4: Contact -->
                <div>
                    <h3 class="text-xl font-serif mb-6 relative inline-block text-white">
                        İletişim
                        <span class="absolute -bottom-2 left-0 w-1/2 h-0.5 bg-accent"></span>
                    </h3>
                    <ul class="space-y-6 text-white/70 font-light">
                        <li class="flex items-start gap-4">
                            <i class="ph-fill ph-map-pin text-2xl text-accent shrink-0"></i>
                            <span>Kardeşler Mahallesi, Bağdat Caddesi No:47/B<br>Sivas / Merkez</span>
                        </li>
                        <li class="flex items-center gap-4">
                            <i class="ph-fill ph-phone-call text-2xl text-accent shrink-0"></i>
                            <a href="tel:+905555555555" class="hover:text-accent transition-colors">+90 (555) 555 55 55</a>
                        </li>
                        <li class="flex items-center gap-4">
                            <i class="ph-fill ph-envelope-simple text-2xl text-accent shrink-0"></i>
                            <a href="mailto:info@aynaclinic.com" class="hover:text-accent transition-colors">info@aynaclinic.com</a>
                        </li>
                    </ul>
                </div>

            </div>

            <!-- Bottom Copyright -->
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center gap-4 text-white/40 text-sm font-light">
                <p>&copy; 2024 Ayna Clinic | Dr. Bilal Keşkek. Tüm hakları saklıdır.</p>
                <div class="flex items-center gap-2">
                    <span class="text-[10px] border border-white/20 px-3 py-1.5 rounded uppercase tracking-widest text-white/50">Sayfa içeriği sadece bilgilendirme amaçlıdır.</span>
                </div>
            </div>
        </div>
    </footer>

</body>
</html>"""

    with open("ayna_clinic_demo.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Ultra-rich demo başarıyla oluşturuldu: ayna_clinic_demo.html")

if __name__ == "__main__":
    build_demo()
