import urllib.request
import base64
import re
from io import BytesIO
from PIL import Image

def get_b64(u):
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read()
        img = Image.open(BytesIO(res))
        
        # Resize to reasonable dimensions to save size
        max_size = (1200, 1200)
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Convert to WebP for best compression
        out = BytesIO()
        img.save(out, format="WEBP", quality=70)
        b64 = base64.b64encode(out.getvalue()).decode('utf-8')
        return f"data:image/webp;base64,{b64}"
    except Exception as e:
        print(f"Error downloading {u}: {e}")
        return ""

print("Downloading images...")

images = {
    # Premium restaurant / romantic dinner / event planner vibes
    "hero": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=1600&q=80", # Elegant dining table / wine
    "about": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1000&q=80", # Restaurant interior
    "food_1": "https://images.unsplash.com/photo-1551218808-94e220e084d2?w=800&q=80", # Premium food presentation
    "food_2": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=800&q=80", # Fine dining
    "food_3": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=800&q=80", # Dessert or coffee
    "event_1": "https://images.unsplash.com/photo-1478146896981-b80fe463b330?w=800&q=80", # Event table setup
    "gallery_1": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&q=80",
    "gallery_2": "https://images.unsplash.com/photo-1600565193348-f74bd3c7ccdf?w=800&q=80",
    "gallery_3": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&q=80",
    "gallery_4": "https://images.unsplash.com/photo-1560053608-13721e0d69e8?w=800&q=80",
    "gallery_5": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=800&q=80",
    "gallery_6": "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=800&q=80",
}

b64_images = {}
for k, v in images.items():
    print(f"Downloading {k}...")
    b64_images[k] = get_b64(v)

html_content = f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lal Concept | Premium Cafe & Event Planner</title>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <!-- Icons -->
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    
    <!-- Animations -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    
    <!-- Tailwind -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Montserrat', 'sans-serif'],
                        serif: ['Playfair Display', 'serif'],
                    }},
                    colors: {{
                        brand: {{
                            dark: '#0a0a0a',
                            surface: '#171717',
                            accent: '#D4AF37', /* Gold */
                            accentDark: '#B8860B', /* Darker Gold */
                            ruby: '#9B111E', /* Ruby Red / Lal */
                            light: '#f5f5f5',
                            muted: '#a3a3a3'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    
    <style>
        body {{
            background-color: #0a0a0a;
            color: #f5f5f5;
            overflow-x: hidden;
        }}
        
        .hero-bg {{
            background-image: url('{b64_images["hero"]}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        .hero-overlay {{
            background: linear-gradient(to right, rgba(10,10,10,0.9) 0%, rgba(10,10,10,0.5) 100%);
        }}

        .glass-nav {{
            background: rgba(10, 10, 10, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(212, 175, 55, 0.1);
        }}

        .glass-card {{
            background: rgba(23, 23, 23, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(212, 175, 55, 0.05);
            transition: all 0.4s ease;
        }}

        .glass-card:hover {{
            border-color: rgba(212, 175, 55, 0.3);
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}

        .text-gold-gradient {{
            background: linear-gradient(to right, #D4AF37, #F3E5AB, #D4AF37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .text-ruby {{
            color: #9B111E;
        }}

        .btn-gold {{
            background: linear-gradient(45deg, #B8860B, #D4AF37);
            color: #0a0a0a;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            z-index: 1;
        }}
        
        .btn-gold::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(45deg, #D4AF37, #B8860B);
            z-index: -1;
            transition: opacity 0.3s ease;
            opacity: 0;
        }}
        
        .btn-gold:hover::before {{
            opacity: 1;
        }}

        .btn-outline-gold {{
            border: 1px solid #D4AF37;
            color: #D4AF37;
            transition: all 0.3s ease;
        }}
        
        .btn-outline-gold:hover {{
            background: rgba(212, 175, 55, 0.1);
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
        }}

        .section-padding {{
            padding-top: 6rem;
            padding-bottom: 6rem;
        }}

        .custom-cursor {{
            cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"><circle cx="10" cy="10" r="5" fill="%23D4AF37"/></svg>') 10 10, auto;
        }}
        
        .img-hover-zoom {{
            overflow: hidden;
        }}
        
        .img-hover-zoom img {{
            transition: transform 0.8s ease;
        }}
        
        .img-hover-zoom:hover img {{
            transform: scale(1.05);
        }}
    </style>
</head>
<body class="custom-cursor antialiased">

    <!-- Header -->
    <header class="fixed w-full top-0 z-50 glass-nav transition-all duration-300" id="header">
        <div class="container mx-auto px-4 md:px-6">
            <div class="flex items-center justify-between h-20 md:h-24">
                <!-- Logo -->
                <a href="#" class="flex flex-col items-center justify-center">
                    <span class="font-serif text-2xl md:text-3xl tracking-widest text-gold-gradient font-bold uppercase">Lal Concept</span>
                    <span class="text-[0.6rem] md:text-xs tracking-[0.3em] text-brand-muted uppercase mt-1">Cafe & Event Planner</span>
                </a>

                <!-- Desktop Nav -->
                <nav class="hidden md:flex items-center gap-8">
                    <a href="#about" class="text-sm font-medium text-brand-light hover:text-brand-accent transition-colors tracking-wide uppercase">Hakkımızda</a>
                    <a href="#services" class="text-sm font-medium text-brand-light hover:text-brand-accent transition-colors tracking-wide uppercase">Hizmetler</a>
                    <a href="#menu" class="text-sm font-medium text-brand-light hover:text-brand-accent transition-colors tracking-wide uppercase">Lezzetler</a>
                    <a href="#gallery" class="text-sm font-medium text-brand-light hover:text-brand-accent transition-colors tracking-wide uppercase">Galeri</a>
                    <a href="#contact" class="btn-gold px-6 py-2.5 rounded text-sm font-semibold tracking-wide uppercase">Rezervasyon</a>
                </nav>

                <!-- Mobile Menu Button -->
                <button class="md:hidden text-brand-accent p-2" id="mobile-menu-btn">
                    <i class="ph ph-list text-3xl"></i>
                </button>
            </div>
        </div>
        
        <!-- Mobile Nav -->
        <div class="md:hidden absolute top-full left-0 w-full glass-nav flex-col items-center py-6 gap-6 hidden border-t border-brand-accent/10" id="mobile-nav">
            <a href="#about" class="text-sm font-medium text-brand-light hover:text-brand-accent transition-colors tracking-wide uppercase">Hakkımızda</a>
            <a href="#services" class="text-sm font-medium text-brand-light hover:text-brand-accent transition-colors tracking-wide uppercase">Hizmetler</a>
            <a href="#menu" class="text-sm font-medium text-brand-light hover:text-brand-accent transition-colors tracking-wide uppercase">Lezzetler</a>
            <a href="#gallery" class="text-sm font-medium text-brand-light hover:text-brand-accent transition-colors tracking-wide uppercase">Galeri</a>
            <a href="#contact" class="btn-gold px-8 py-3 rounded text-sm font-semibold tracking-wide uppercase mt-2">Rezervasyon</a>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="relative h-screen flex items-center justify-center overflow-hidden">
        <div class="absolute inset-0 hero-bg"></div>
        <div class="absolute inset-0 hero-overlay"></div>
        
        <div class="container mx-auto px-4 relative z-10 pt-20">
            <div class="max-w-3xl mx-auto text-center" data-aos="fade-up" data-aos-duration="1000">
                <div class="inline-flex items-center gap-2 mb-6">
                    <div class="h-[1px] w-12 bg-brand-accent"></div>
                    <span class="text-brand-accent tracking-[0.2em] uppercase text-sm font-medium">Sakinlik ve Lezzetin Buluşma Noktası</span>
                    <div class="h-[1px] w-12 bg-brand-accent"></div>
                </div>
                
                <h1 class="text-5xl md:text-7xl lg:text-8xl font-serif text-white mb-6 leading-tight">
                    Unutulmaz <br/>
                    <span class="text-gold-gradient italic">Anlar İçin</span>
                </h1>
                
                <p class="text-lg md:text-xl text-brand-light/80 mb-10 font-light max-w-2xl mx-auto leading-relaxed">
                    Premium cafe deneyimi, kusursuz yemek sunumları ve hayalinizdeki özel gün organizasyonları Lal Concept'in eşsiz atmosferinde hayat buluyor.
                </p>
                
                <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                    <a href="#contact" class="btn-gold px-8 py-4 rounded w-full sm:w-auto text-sm font-bold tracking-widest uppercase flex items-center justify-center gap-2">
                        <span>Hemen Rezervasyon Yap</span>
                        <i class="ph-bold ph-arrow-right"></i>
                    </a>
                    <a href="#menu" class="btn-outline-gold px-8 py-4 rounded w-full sm:w-auto text-sm font-bold tracking-widest uppercase flex items-center justify-center gap-2">
                        <span>Menüyü İncele</span>
                    </a>
                </div>
            </div>
        </div>
        
        <!-- Scroll Indicator -->
        <div class="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center animate-bounce">
            <span class="text-xs text-brand-accent uppercase tracking-widest mb-2">Keşfet</span>
            <i class="ph ph-caret-down text-brand-accent text-xl"></i>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section-padding bg-brand-dark relative">
        <div class="absolute top-0 right-0 w-64 h-64 bg-brand-ruby/5 rounded-full blur-[100px]"></div>
        <div class="container mx-auto px-4 md:px-6">
            <div class="flex flex-col lg:flex-row items-center gap-16">
                
                <div class="w-full lg:w-1/2 relative" data-aos="fade-right">
                    <div class="relative z-10 img-hover-zoom rounded-t-full border border-brand-accent/20 p-2">
                        <img src="{b64_images["about"]}" alt="Lal Concept İç Mekan" class="w-full h-[600px] object-cover rounded-t-full rounded-b-xl">
                    </div>
                    <div class="absolute -bottom-10 -right-10 bg-brand-surface border border-brand-accent/30 p-8 rounded-xl z-20 shadow-2xl hidden md:block">
                        <div class="text-5xl font-serif text-brand-accent mb-2">Premium</div>
                        <div class="text-brand-light font-medium tracking-widest uppercase">Deneyim</div>
                    </div>
                </div>

                <div class="w-full lg:w-1/2" data-aos="fade-left">
                    <h4 class="text-brand-accent tracking-[0.2em] uppercase text-sm font-medium mb-4">Hakkımızda</h4>
                    <h2 class="text-4xl md:text-5xl font-serif text-white mb-6">Detaylarda Saklı <br/><span class="italic text-brand-ruby">Lüks ve Zarafet</span></h2>
                    
                    <p class="text-brand-muted mb-6 leading-relaxed font-light text-lg">
                        Lal Concept, sıradan bir kafenin ötesinde, her anınızı özel kılmak için tasarlanmış premium bir yaşam alanıdır. Özenle seçilmiş kahve çekirdeklerimiz, damakta iz bırakan imza lezzetlerimiz ve kusursuz sunumlarımızla ruhunuzu dinlendiren bir deneyim sunuyoruz.
                    </p>
                    <p class="text-brand-muted mb-10 leading-relaxed font-light text-lg">
                        Sadece günlük kaçamaklarınız için değil, aynı zamanda hayatınızın en önemli kutlamaları, romantik akşam yemekleri ve özel organizasyonlarınız (Event Planner) için de profesyonel ekibimizle kusursuzu yaratıyoruz. Lal'in sıcak ve asil atmosferinde, zamanı durdurun.
                    </p>
                    
                    <div class="grid grid-cols-2 gap-8 mb-10 border-t border-brand-accent/10 pt-8">
                        <div>
                            <div class="text-3xl font-serif text-brand-accent mb-2">100%</div>
                            <div class="text-sm text-brand-light uppercase tracking-wider">Müşteri Memnuniyeti</div>
                        </div>
                        <div>
                            <div class="text-3xl font-serif text-brand-accent mb-2">Özel</div>
                            <div class="text-sm text-brand-light uppercase tracking-wider">Tasarım Konseptler</div>
                        </div>
                    </div>
                    
                    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNTAiIGhlaWdodD0iNTAiIHZpZXdCb3g9IjAgMCAxNTAgNTAiPjx0ZXh0IHk9IjM1IiBmb250LWZhbWlseT0iUGxheWZhaXIgRGlzcGxheSwgc2VyaWYiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNENEFGMzciIHN0eWxlPSJmb250LXN0eWxlOml0YWxpYyI+TGFsIENvbmNlcHQ8L3RleHQ+PC9zdmc+" alt="Lal Concept Signature" class="h-12 opacity-80">
                </div>

            </div>
        </div>
    </section>

    <!-- Services / Event Planner Section -->
    <section id="services" class="section-padding bg-brand-surface relative overflow-hidden">
        <div class="absolute -top-40 -left-40 w-96 h-96 bg-brand-accent/5 rounded-full blur-[120px]"></div>
        
        <div class="container mx-auto px-4 md:px-6 relative z-10">
            <div class="text-center max-w-3xl mx-auto mb-20" data-aos="fade-up">
                <h4 class="text-brand-accent tracking-[0.2em] uppercase text-sm font-medium mb-4">Ayrıcalıklar</h4>
                <h2 class="text-4xl md:text-5xl font-serif text-white mb-6">Lal Concept <span class="italic text-brand-ruby">Deneyimleri</span></h2>
                <p class="text-brand-muted font-light leading-relaxed">İster sakin bir kahve molası, ister hayatınızın en görkemli kutlaması. Her ihtiyacınıza uygun premium alanlarımız ve hizmetlerimizle yanınızdayız.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Service 1 -->
                <div class="glass-card p-10 rounded-2xl text-center group" data-aos="fade-up" data-aos-delay="100">
                    <div class="w-20 h-20 mx-auto bg-brand-dark rounded-full flex items-center justify-center mb-8 border border-brand-accent/20 group-hover:border-brand-accent transition-colors">
                        <i class="ph-light ph-coffee text-4xl text-brand-accent"></i>
                    </div>
                    <h3 class="text-2xl font-serif text-white mb-4">Premium Cafe & Restoran</h3>
                    <p class="text-brand-muted font-light leading-relaxed">
                        Dünya mutfağından seçkin lezzetler, artisan kahveler ve görsel bir şölene dönüşen sunumlar. Sakin ve lüks atmosferimizde günün yorgunluğunu atın.
                    </p>
                </div>
                
                <!-- Service 2 -->
                <div class="glass-card p-10 rounded-2xl text-center group relative overflow-hidden border-brand-accent/30" data-aos="fade-up" data-aos-delay="200">
                    <div class="absolute inset-0 bg-brand-ruby/5"></div>
                    <div class="relative z-10">
                        <div class="w-20 h-20 mx-auto bg-brand-dark rounded-full flex items-center justify-center mb-8 border border-brand-accent/20 group-hover:border-brand-accent transition-colors">
                            <i class="ph-light ph-star text-4xl text-brand-accent"></i>
                        </div>
                        <h3 class="text-2xl font-serif text-white mb-4">Özel Gün Organizasyonları</h3>
                        <p class="text-brand-muted font-light leading-relaxed">
                            Event planner ekibimizle doğum günleri, evlilik teklifleri, butik nişan ve kutlamalarınızı kusursuz bir tasarımla hayata geçiriyoruz.
                        </p>
                    </div>
                </div>

                <!-- Service 3 -->
                <div class="glass-card p-10 rounded-2xl text-center group" data-aos="fade-up" data-aos-delay="300">
                    <div class="w-20 h-20 mx-auto bg-brand-dark rounded-full flex items-center justify-center mb-8 border border-brand-accent/20 group-hover:border-brand-accent transition-colors">
                        <i class="ph-light ph-wine text-4xl text-brand-accent"></i>
                    </div>
                    <h3 class="text-2xl font-serif text-white mb-4">Romantik Akşam Yemekleri</h3>
                    <p class="text-brand-muted font-light leading-relaxed">
                        Mum ışığında, size özel dekore edilmiş masanızda, şefimizin özel tadım menüleri eşliğinde unutulmaz romantik akşamlar.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Highlights / Menu Section -->
    <section id="menu" class="section-padding bg-brand-dark">
        <div class="container mx-auto px-4 md:px-6">
            <div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-6" data-aos="fade-up">
                <div>
                    <h4 class="text-brand-accent tracking-[0.2em] uppercase text-sm font-medium mb-4">Görsel Şölen</h4>
                    <h2 class="text-4xl md:text-5xl font-serif text-white">İmza <span class="italic text-gold-gradient">Lezzetlerimiz</span></h2>
                </div>
                <a href="#contact" class="btn-outline-gold px-6 py-3 rounded text-sm tracking-widest uppercase">Tüm Menüyü Gör</a>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Item 1 -->
                <div class="group cursor-pointer" data-aos="fade-up" data-aos-delay="100">
                    <div class="img-hover-zoom h-80 rounded-2xl overflow-hidden mb-6 relative">
                        <img src="{b64_images["food_1"]}" alt="Lal Özel Sunum" class="w-full h-full object-cover">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-dark via-transparent opacity-80"></div>
                        <div class="absolute bottom-4 left-4 right-4 flex justify-between items-end">
                            <span class="text-brand-accent font-serif text-xl italic">Chef's Special</span>
                            <span class="bg-brand-surface/80 backdrop-blur px-3 py-1 rounded text-sm text-brand-light">Yeni</span>
                        </div>
                    </div>
                    <h3 class="text-2xl font-serif text-white mb-2 group-hover:text-brand-accent transition-colors">Lal Dana Madalyon</h3>
                    <p class="text-brand-muted font-light text-sm">Trüf mantarlı patates püresi, kuşkonmaz ve özel lal şarap sosu ile.</p>
                </div>

                <!-- Item 2 -->
                <div class="group cursor-pointer" data-aos="fade-up" data-aos-delay="200">
                    <div class="img-hover-zoom h-80 rounded-2xl overflow-hidden mb-6 relative">
                        <img src="{b64_images["food_2"]}" alt="Premium Makarna" class="w-full h-full object-cover">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-dark via-transparent opacity-80"></div>
                        <div class="absolute bottom-4 left-4 right-4 flex justify-between items-end">
                            <span class="text-brand-accent font-serif text-xl italic">Premium Pasta</span>
                        </div>
                    </div>
                    <h3 class="text-2xl font-serif text-white mb-2 group-hover:text-brand-accent transition-colors">Deniz Mahsüllü Linguine</h3>
                    <p class="text-brand-muted font-light text-sm">Taze deniz ürünleri, sarımsak, beyaz şarap ve fesleğenli özel İtalyan sos.</p>
                </div>

                <!-- Item 3 -->
                <div class="group cursor-pointer" data-aos="fade-up" data-aos-delay="300">
                    <div class="img-hover-zoom h-80 rounded-2xl overflow-hidden mb-6 relative">
                        <img src="{b64_images["food_3"]}" alt="İmza Tatlı" class="w-full h-full object-cover">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-dark via-transparent opacity-80"></div>
                        <div class="absolute bottom-4 left-4 right-4 flex justify-between items-end">
                            <span class="text-brand-accent font-serif text-xl italic">Signature Dessert</span>
                        </div>
                    </div>
                    <h3 class="text-2xl font-serif text-white mb-2 group-hover:text-brand-accent transition-colors">Kırmızı Kadife Rüyası</h3>
                    <p class="text-brand-muted font-light text-sm">Orman meyveleri, mascarpone peyniri ve altın varak dokunuşları.</p>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Event Banner -->
    <section class="py-24 bg-brand-surface relative overflow-hidden">
        <div class="absolute inset-0 opacity-20" style="background-image: url('{b64_images["event_1"]}'); background-size: cover; background-position: center; background-attachment: fixed;"></div>
        <div class="absolute inset-0 bg-brand-dark/80 backdrop-blur-sm"></div>
        
        <div class="container mx-auto px-4 relative z-10 text-center">
            <i class="ph-light ph-diamond text-5xl text-brand-accent mb-6 inline-block"></i>
            <h2 class="text-4xl md:text-6xl font-serif text-white mb-6">Siz Hayal Edin, <br/><span class="text-gold-gradient italic">Biz Tasarlayalım</span></h2>
            <p class="text-brand-light/80 max-w-2xl mx-auto mb-10 text-lg font-light leading-relaxed">
                Lal Concept Event Planner ayrıcalığıyla, en özel günlerinizi sanata dönüştürüyoruz. Masa düzeninden çiçek seçimine kadar her detayı sizin için düşünüyoruz.
            </p>
            <a href="#contact" class="btn-gold px-10 py-4 rounded text-sm font-bold tracking-widest uppercase inline-block">Organizasyon İçin İletişime Geç</a>
        </div>
    </section>

    <!-- Gallery -->
    <section id="gallery" class="py-1 bg-brand-dark">
        <div class="grid grid-cols-2 md:grid-cols-3 gap-1 px-1">
            <div class="img-hover-zoom aspect-square relative group">
                <img src="{b64_images["gallery_1"]}" class="w-full h-full object-cover" alt="Galeri 1">
                <div class="absolute inset-0 bg-brand-dark/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                    <i class="ph-bold ph-instagram-logo text-3xl text-brand-accent"></i>
                </div>
            </div>
            <div class="img-hover-zoom aspect-square relative group">
                <img src="{b64_images["gallery_2"]}" class="w-full h-full object-cover" alt="Galeri 2">
                <div class="absolute inset-0 bg-brand-dark/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                    <i class="ph-bold ph-instagram-logo text-3xl text-brand-accent"></i>
                </div>
            </div>
            <div class="img-hover-zoom aspect-square relative group">
                <img src="{b64_images["gallery_3"]}" class="w-full h-full object-cover" alt="Galeri 3">
                <div class="absolute inset-0 bg-brand-dark/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                    <i class="ph-bold ph-instagram-logo text-3xl text-brand-accent"></i>
                </div>
            </div>
            <div class="img-hover-zoom aspect-square relative group">
                <img src="{b64_images["gallery_4"]}" class="w-full h-full object-cover" alt="Galeri 4">
                <div class="absolute inset-0 bg-brand-dark/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                    <i class="ph-bold ph-instagram-logo text-3xl text-brand-accent"></i>
                </div>
            </div>
            <div class="img-hover-zoom aspect-square relative group">
                <img src="{b64_images["gallery_5"]}" class="w-full h-full object-cover" alt="Galeri 5">
                <div class="absolute inset-0 bg-brand-dark/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                    <i class="ph-bold ph-instagram-logo text-3xl text-brand-accent"></i>
                </div>
            </div>
            <div class="img-hover-zoom aspect-square relative group">
                <img src="{b64_images["gallery_6"]}" class="w-full h-full object-cover" alt="Galeri 6">
                <div class="absolute inset-0 bg-brand-dark/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                    <i class="ph-bold ph-instagram-logo text-3xl text-brand-accent"></i>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer / Contact -->
    <footer id="contact" class="bg-brand-surface pt-20 pb-10 border-t border-brand-accent/20 relative">
        <div class="container mx-auto px-4 md:px-6">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
                
                <div class="lg:col-span-1">
                    <a href="#" class="inline-block mb-6">
                        <span class="font-serif text-3xl tracking-widest text-gold-gradient font-bold uppercase">Lal Concept</span>
                    </a>
                    <p class="text-brand-muted font-light text-sm leading-relaxed mb-6">
                        Premium cafe, eşsiz lezzetler ve hayalinizdeki özel gün organizasyonları için doğru adres.
                    </p>
                    <div class="flex gap-4">
                        <a href="#" class="w-10 h-10 rounded-full border border-brand-accent/30 flex items-center justify-center text-brand-accent hover:bg-brand-accent hover:text-brand-dark transition-colors">
                            <i class="ph-fill ph-instagram-logo text-lg"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-full border border-brand-accent/30 flex items-center justify-center text-brand-accent hover:bg-brand-accent hover:text-brand-dark transition-colors">
                            <i class="ph-fill ph-facebook-logo text-lg"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-full border border-brand-accent/30 flex items-center justify-center text-brand-accent hover:bg-brand-accent hover:text-brand-dark transition-colors">
                            <i class="ph-fill ph-whatsapp-logo text-lg"></i>
                        </a>
                    </div>
                </div>
                
                <div>
                    <h4 class="text-white font-serif text-xl mb-6">İletişim</h4>
                    <ul class="space-y-4">
                        <li class="flex items-start gap-3 text-brand-muted">
                            <i class="ph-fill ph-map-pin text-brand-accent mt-1"></i>
                            <span class="font-light text-sm">Merkez Mah. Premium Cad. No:1, İstanbul</span>
                        </li>
                        <li class="flex items-center gap-3 text-brand-muted">
                            <i class="ph-fill ph-phone text-brand-accent"></i>
                            <a href="tel:+905555555555" class="font-light text-sm hover:text-brand-accent transition-colors">+90 555 555 55 55</a>
                        </li>
                        <li class="flex items-center gap-3 text-brand-muted">
                            <i class="ph-fill ph-envelope-simple text-brand-accent"></i>
                            <a href="mailto:info@lalconcept.com" class="font-light text-sm hover:text-brand-accent transition-colors">info@lalconcept.com</a>
                        </li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-white font-serif text-xl mb-6">Çalışma Saatleri</h4>
                    <ul class="space-y-3 text-brand-muted font-light text-sm">
                        <li class="flex justify-between border-b border-brand-light/10 pb-2">
                            <span>Pazartesi - Perşembe</span>
                            <span class="text-brand-accent">09:00 - 23:00</span>
                        </li>
                        <li class="flex justify-between border-b border-brand-light/10 pb-2">
                            <span>Cuma - Cumartesi</span>
                            <span class="text-brand-accent">09:00 - 01:00</span>
                        </li>
                        <li class="flex justify-between pb-2">
                            <span>Pazar</span>
                            <span class="text-brand-accent">09:00 - 23:00</span>
                        </li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-white font-serif text-xl mb-6">Rezervasyon</h4>
                    <p class="text-brand-muted font-light text-sm mb-4">Özel gün organizasyonları ve VIP masa rezervasyonları için hemen bize ulaşın.</p>
                    <a href="https://wa.me/905555555555" target="_blank" class="w-full btn-gold py-3 rounded flex items-center justify-center gap-2 text-sm font-bold uppercase tracking-wider">
                        <i class="ph-bold ph-whatsapp-logo text-xl"></i>
                        <span>WhatsApp'tan Yazın</span>
                    </a>
                </div>
                
            </div>
            
            <div class="border-t border-brand-accent/20 pt-8 flex flex-col md:flex-row items-center justify-between gap-4">
                <p class="text-brand-muted text-xs font-light">
                    &copy; 2026 Lal Concept Cafe & Event Planner. Tüm hakları saklıdır.
                </p>
                <div class="flex gap-6">
                    <a href="#" class="text-brand-muted hover:text-brand-accent text-xs font-light transition-colors">Gizlilik Politikası</a>
                    <a href="#" class="text-brand-muted hover:text-brand-accent text-xs font-light transition-colors">Kullanım Koşulları</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        // Init AOS
        AOS.init({{
            once: true,
            offset: 50,
            duration: 800,
            easing: 'ease-out-cubic',
        }});

        // Header Scroll Effect
        const header = document.getElementById('header');
        window.addEventListener('scroll', () => {{
            if (window.scrollY > 50) {{
                header.classList.add('shadow-lg');
                header.classList.replace('py-4', 'py-2');
                header.style.background = 'rgba(10, 10, 10, 0.95)';
            }} else {{
                header.classList.remove('shadow-lg');
                header.classList.replace('py-2', 'py-4');
                header.style.background = 'rgba(10, 10, 10, 0.85)';
            }}
        }});

        // Mobile Menu Toggle
        const mobileBtn = document.getElementById('mobile-menu-btn');
        const mobileNav = document.getElementById('mobile-nav');
        
        mobileBtn.addEventListener('click', () => {{
            mobileNav.classList.toggle('hidden');
            mobileNav.classList.toggle('flex');
        }});
        
        // Close mobile menu on click
        document.querySelectorAll('#mobile-nav a').forEach(link => {{
            link.addEventListener('click', () => {{
                mobileNav.classList.add('hidden');
                mobileNav.classList.remove('flex');
            }});
        }});
    </script>
</body>
</html>
"""

with open("lal_concept_demo.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("lal_concept_demo.html created successfully.")
