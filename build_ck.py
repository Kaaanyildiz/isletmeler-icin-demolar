import urllib.request
import base64
from io import BytesIO
from PIL import Image
import os

def get_b64(u):
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read()
        img = Image.open(BytesIO(res))
        
        # Resize to reasonable dimensions
        max_size = (1200, 1200)
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Convert to WebP
        out = BytesIO()
        img.save(out, format="WEBP", quality=75)
        b64 = base64.b64encode(out.getvalue()).decode('utf-8')
        return f"data:image/webp;base64,{b64}"
    except Exception as e:
        print(f"Error downloading {u}: {e}")
        return ""

print("Downloading images for CK Mimarlik...")

# Architecture, interior design, real estate images
images = {
    "hero": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1600&q=80", # Luxury modern house exterior
    "about_1": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1000&q=80", # Modern interior living room
    "about_2": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=1000&q=80", # Blueprint / architectural drawing / desk
    "proj_1": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&q=80", # Luxury villa
    "proj_2": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800&q=80", # Minimalist interior
    "proj_3": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=800&q=80", # Modern kitchen/dining
    "proj_4": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=800&q=80", # Premium bedroom
    "serv_1": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=800&q=80", # Architecture building
    "serv_2": "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?w=800&q=80", # Interior
    "serv_3": "https://images.unsplash.com/photo-1582407947304-fd86f028f716?w=800&q=80", # Real estate / keys / house
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
    <title>C.K Mimarlık & Gayrimenkul | Mimari Tasarım, Proje ve Uygulama</title>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <!-- Outfit for modern, geometric look; Inter for clean body text -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    
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
                        sans: ['Inter', 'sans-serif'],
                        display: ['Outfit', 'sans-serif'],
                    }},
                    colors: {{
                        brand: {{
                            black: '#050505',
                            dark: '#111111',
                            surface: '#1A1A1A',
                            gray: '#2A2A2A',
                            light: '#F4F4F5',
                            white: '#FFFFFF',
                            gold: '#D4AF37',       /* Premium Gold from their logo */
                            goldDark: '#B8860B',
                        }}
                    }},
                    letterSpacing: {{
                        'widest': '.25em',
                    }}
                }}
            }}
        }}
    </script>
    
    <style>
        body {{
            background-color: #050505;
            color: #F4F4F5;
            overflow-x: hidden;
            selection-background-color: #D4AF37;
            selection-color: #050505;
        }}
        
        ::selection {{
            background: #D4AF37;
            color: #050505;
        }}
        
        .font-display {{
            font-family: 'Outfit', sans-serif;
        }}

        .hero-bg {{
            background-image: url('{b64_images["hero"]}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        .hero-overlay {{
            background: linear-gradient(135deg, rgba(5,5,5,0.95) 0%, rgba(5,5,5,0.6) 100%);
        }}

        .glass-nav {{
            background: rgba(5, 5, 5, 0.85);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }}

        .text-outline {{
            color: transparent;
            -webkit-text-stroke: 1px rgba(255, 255, 255, 0.2);
        }}
        
        .text-outline-gold {{
            color: transparent;
            -webkit-text-stroke: 1px rgba(212, 175, 55, 0.5);
        }}

        /* Architecture style solid lines */
        .arch-line-vertical {{
            width: 1px;
            background-color: rgba(255,255,255,0.1);
            position: absolute;
            top: 0;
            bottom: 0;
        }}
        
        .arch-line-horizontal {{
            height: 1px;
            background-color: rgba(255,255,255,0.1);
            width: 100%;
        }}

        .btn-arch {{
            position: relative;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            padding: 1rem 2rem;
            background: transparent;
            color: #fff;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-size: 0.875rem;
            font-weight: 500;
            border: 1px solid rgba(212, 175, 55, 0.5);
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        
        .btn-arch::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #D4AF37;
            transform: scaleX(0);
            transform-origin: right;
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: -1;
        }}
        
        .btn-arch:hover {{
            color: #050505;
            border-color: #D4AF37;
        }}
        
        .btn-arch:hover::before {{
            transform: scaleX(1);
            transform-origin: left;
        }}

        .project-card {{
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }}
        
        .project-card img {{
            transition: transform 1.2s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        
        .project-card:hover img {{
            transform: scale(1.05);
        }}
        
        .project-overlay {{
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(5,5,5,0.9) 0%, rgba(5,5,5,0) 50%);
            opacity: 0;
            transition: opacity 0.5s ease;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 2rem;
        }}
        
        .project-card:hover .project-overlay {{
            opacity: 1;
        }}
        
        .project-title {{
            transform: translateY(20px);
            opacity: 0;
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.1s;
        }}
        
        .project-card:hover .project-title {{
            transform: translateY(0);
            opacity: 1;
        }}

        .section-padding {{
            padding-top: 8rem;
            padding-bottom: 8rem;
        }}

        .stat-number {{
            background: linear-gradient(to bottom right, #FFFFFF, #888888);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .gold-gradient-text {{
            background: linear-gradient(to right, #D4AF37, #F3E5AB, #D4AF37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
    </style>
</head>
<body class="antialiased">

    <!-- Grid Lines Background -->
    <div class="fixed inset-0 pointer-events-none z-[-1] opacity-20">
        <div class="container mx-auto px-4 h-full relative">
            <div class="arch-line-vertical left-4 md:left-6"></div>
            <div class="arch-line-vertical left-1/4 hidden md:block"></div>
            <div class="arch-line-vertical left-2/4 hidden md:block"></div>
            <div class="arch-line-vertical left-3/4 hidden md:block"></div>
            <div class="arch-line-vertical right-4 md:right-6"></div>
        </div>
    </div>

    <!-- Header -->
    <header class="fixed w-full top-0 z-50 glass-nav transition-all duration-500" id="header">
        <div class="container mx-auto px-4 md:px-6">
            <div class="flex items-center justify-between h-24">
                <!-- Logo -->
                <a href="#" class="flex items-center gap-3 group">
                    <div class="w-12 h-12 flex items-center justify-center border-2 border-brand-gold rounded relative overflow-hidden group-hover:bg-brand-gold transition-colors duration-500">
                        <!-- Abstract CK representation -->
                        <span class="font-display font-bold text-xl text-brand-gold group-hover:text-brand-black transition-colors duration-500">CK</span>
                    </div>
                    <div class="flex flex-col">
                        <span class="font-display font-bold text-lg tracking-widest uppercase text-white leading-tight">Mimarlık</span>
                        <span class="font-display font-light text-xs tracking-[0.3em] text-brand-gold uppercase leading-tight">& Gayrimenkul</span>
                    </div>
                </a>

                <!-- Desktop Nav -->
                <nav class="hidden md:flex items-center gap-10">
                    <a href="#about" class="text-xs font-medium text-brand-light hover:text-brand-gold transition-colors tracking-widest uppercase">Kurumsal</a>
                    <a href="#services" class="text-xs font-medium text-brand-light hover:text-brand-gold transition-colors tracking-widest uppercase">Hizmetler</a>
                    <a href="#projects" class="text-xs font-medium text-brand-light hover:text-brand-gold transition-colors tracking-widest uppercase">Projeler</a>
                    <a href="#contact" class="btn-arch">
                        İletişim
                        <i class="ph-bold ph-arrow-right"></i>
                    </a>
                </nav>

                <!-- Mobile Menu Button -->
                <button class="md:hidden text-white p-2" id="mobile-menu-btn">
                    <i class="ph ph-list text-3xl"></i>
                </button>
            </div>
        </div>
        
        <!-- Mobile Nav -->
        <div class="md:hidden absolute top-full left-0 w-full glass-nav flex-col items-start p-6 gap-6 hidden border-t border-white/10" id="mobile-nav">
            <a href="#about" class="text-sm font-medium text-brand-light hover:text-brand-gold transition-colors tracking-widest uppercase w-full pb-4 border-b border-white/10">Kurumsal</a>
            <a href="#services" class="text-sm font-medium text-brand-light hover:text-brand-gold transition-colors tracking-widest uppercase w-full pb-4 border-b border-white/10">Hizmetler</a>
            <a href="#projects" class="text-sm font-medium text-brand-light hover:text-brand-gold transition-colors tracking-widest uppercase w-full pb-4 border-b border-white/10">Projeler</a>
            <a href="#contact" class="text-sm font-medium text-brand-gold tracking-widest uppercase w-full">İletişim</a>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="relative h-screen flex items-center overflow-hidden">
        <div class="absolute inset-0 hero-bg scale-105 transform origin-center animate-[pulse_20s_ease-in-out_infinite_alternate]"></div>
        <div class="absolute inset-0 hero-overlay"></div>
        
        <div class="container mx-auto px-4 md:px-6 relative z-10 pt-20">
            <div class="max-w-4xl" data-aos="fade-up" data-aos-duration="1200">
                <div class="flex items-center gap-4 mb-8">
                    <div class="h-[1px] w-16 bg-brand-gold"></div>
                    <span class="text-brand-gold tracking-[0.3em] uppercase text-xs font-semibold">Tasarım • Proje • Gayrimenkul</span>
                </div>
                
                <h1 class="text-5xl md:text-7xl lg:text-8xl font-display font-bold text-white mb-8 leading-[1.1] uppercase">
                    Mimarinin <br/>
                    <span class="text-outline-gold">Gayrimenkul İle</span><br/>
                    Buluştuğu Nokta
                </h1>
                
                <p class="text-lg md:text-xl text-brand-light/70 mb-12 font-light max-w-2xl leading-relaxed">
                    İç mimari tasarımdan anahtar teslim projelere, hayalinizdeki yaşam alanlarını tasarlıyor ve hayata geçiriyoruz. Sivas Bağdat Caddesi'nden tüm Türkiye'ye.
                </p>
                
                <div class="flex flex-col sm:flex-row gap-6">
                    <a href="#projects" class="btn-arch justify-center">
                        <span>Projeleri İncele</span>
                    </a>
                    <a href="#contact" class="inline-flex items-center justify-center gap-3 px-8 py-4 text-xs font-medium tracking-widest uppercase text-white hover:text-brand-gold transition-colors border border-transparent hover:border-brand-gold/30">
                        <span>Bize Ulaşın</span>
                        <i class="ph-bold ph-arrow-down-right"></i>
                    </a>
                </div>
            </div>
        </div>
        
        <!-- Social & Scroll -->
        <div class="absolute bottom-10 left-0 w-full z-20">
            <div class="container mx-auto px-4 md:px-6 flex justify-between items-end">
                <div class="flex flex-col gap-4">
                    <a href="https://instagram.com/ckmimarlikgayrimenkul" target="_blank" class="w-10 h-10 border border-white/20 rounded-full flex items-center justify-center text-white hover:border-brand-gold hover:text-brand-gold transition-colors">
                        <i class="ph-fill ph-instagram-logo"></i>
                    </a>
                </div>
                <div class="flex flex-col items-center gap-4">
                    <span class="text-[10px] tracking-widest uppercase text-brand-light/50" style="writing-mode: vertical-rl;">Kaydır</span>
                    <div class="w-[1px] h-12 bg-white/20 relative overflow-hidden">
                        <div class="absolute top-0 left-0 w-full h-1/2 bg-brand-gold animate-[ping_2s_cubic-bezier(0,0,0.2,1)_infinite]"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section-padding relative border-b border-white/5 bg-brand-dark">
        <div class="container mx-auto px-4 md:px-6">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-center">
                
                <!-- Images -->
                <div class="relative h-[600px]" data-aos="fade-right">
                    <img src="{b64_images["about_1"]}" alt="Modern İç Mimari" class="absolute top-0 left-0 w-4/5 h-4/5 object-cover grayscale hover:grayscale-0 transition-all duration-700 z-10 border border-white/10">
                    <img src="{b64_images["about_2"]}" alt="Mimari Çizim" class="absolute bottom-0 right-0 w-3/5 h-3/5 object-cover grayscale hover:grayscale-0 transition-all duration-700 z-20 border-4 border-brand-dark shadow-2xl">
                    <div class="absolute -left-8 -bottom-8 w-48 h-48 border border-brand-gold/30 z-0 hidden md:block"></div>
                </div>

                <!-- Content -->
                <div data-aos="fade-left">
                    <div class="flex items-center gap-4 mb-6">
                        <span class="text-brand-gold tracking-widest uppercase text-xs font-semibold">C.K Mimarlık</span>
                        <div class="h-[1px] w-full bg-white/10"></div>
                    </div>
                    
                    <h2 class="text-4xl md:text-5xl lg:text-6xl font-display font-bold text-white mb-8 leading-tight">
                        Fikirleri <span class="text-brand-gold">Gerçeğe</span> <br>Dönüştürüyoruz.
                    </h2>
                    
                    <p class="text-brand-light/70 mb-6 font-light leading-relaxed text-lg">
                        Mekanın potansiyelini en üst düzeye çıkaran estetik, fonksiyonel ve yenilikçi çözümler sunuyoruz. Kavramsal tasarımdan, şantiye yönetimine ve anahtar teslim uygulamaya kadar sürecin her aşamasında titizlikle çalışıyoruz.
                    </p>
                    <p class="text-brand-light/70 mb-10 font-light leading-relaxed text-lg">
                        Aynı zamanda gayrimenkul sektöründeki uzmanlığımızla, değer katan projeler geliştiriyor, yatırımcılarımıza ve müşterilerimize mimari bakış açısıyla doğru gayrimenkul çözümleri sunuyoruz.
                    </p>
                    
                    <div class="grid grid-cols-2 gap-8 pt-8 border-t border-white/10">
                        <div>
                            <div class="font-display text-4xl font-bold text-white mb-2 stat-number">100+</div>
                            <div class="text-xs text-brand-light/50 uppercase tracking-widest">Tamamlanan Proje</div>
                        </div>
                        <div>
                            <div class="font-display text-4xl font-bold text-white mb-2 stat-number">A'dan Z'ye</div>
                            <div class="text-xs text-brand-light/50 uppercase tracking-widest">Anahtar Teslim</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services -->
    <section id="services" class="section-padding bg-brand-black">
        <div class="container mx-auto px-4 md:px-6">
            <div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-8">
                <div data-aos="fade-up">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="h-[1px] w-12 bg-brand-gold"></div>
                        <span class="text-brand-gold tracking-widest uppercase text-xs font-semibold">Uzmanlık Alanlarımız</span>
                    </div>
                    <h2 class="text-4xl md:text-5xl font-display font-bold text-white uppercase">Hizmetlerimiz</h2>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-1">
                <!-- Service 1 -->
                <div class="group relative bg-brand-dark p-10 h-[400px] flex flex-col justify-end overflow-hidden border border-white/5" data-aos="fade-up" data-aos-delay="100">
                    <div class="absolute inset-0 z-0">
                        <img src="{b64_images["serv_1"]}" class="w-full h-full object-cover opacity-10 group-hover:opacity-40 transition-opacity duration-700 mix-blend-luminosity">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-black via-brand-black/80 to-transparent"></div>
                    </div>
                    <div class="relative z-10 transform translate-y-8 group-hover:translate-y-0 transition-transform duration-500">
                        <div class="w-12 h-12 bg-brand-gold/10 flex items-center justify-center rounded-sm mb-6 text-brand-gold">
                            <i class="ph-light ph-pen-nib text-2xl"></i>
                        </div>
                        <h3 class="text-2xl font-display font-bold text-white mb-4 uppercase">Mimari Tasarım & Proje</h3>
                        <p class="text-brand-light/60 font-light text-sm leading-relaxed opacity-0 group-hover:opacity-100 transition-opacity duration-500 delay-100">
                            İhtiyaçlarınıza uygun, estetik ve fonksiyonel mimari projeler çiziyor, mekanın ruhunu tasarlıyoruz.
                        </p>
                    </div>
                </div>
                
                <!-- Service 2 -->
                <div class="group relative bg-brand-dark p-10 h-[400px] flex flex-col justify-end overflow-hidden border border-white/5" data-aos="fade-up" data-aos-delay="200">
                    <div class="absolute inset-0 z-0">
                        <img src="{b64_images["serv_2"]}" class="w-full h-full object-cover opacity-10 group-hover:opacity-40 transition-opacity duration-700 mix-blend-luminosity">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-black via-brand-black/80 to-transparent"></div>
                    </div>
                    <div class="relative z-10 transform translate-y-8 group-hover:translate-y-0 transition-transform duration-500">
                        <div class="w-12 h-12 bg-brand-gold/10 flex items-center justify-center rounded-sm mb-6 text-brand-gold">
                            <i class="ph-light ph-hammer text-2xl"></i>
                        </div>
                        <h3 class="text-2xl font-display font-bold text-white mb-4 uppercase">Anahtar Teslim Uygulama</h3>
                        <p class="text-brand-light/60 font-light text-sm leading-relaxed opacity-0 group-hover:opacity-100 transition-opacity duration-500 delay-100">
                            Tasarımı onaylanmış projelerin inşaat, dekorasyon ve tüm ince işçiliklerini sıfırdan teslim edene kadar yönetiyoruz.
                        </p>
                    </div>
                </div>

                <!-- Service 3 -->
                <div class="group relative bg-brand-dark p-10 h-[400px] flex flex-col justify-end overflow-hidden border border-white/5" data-aos="fade-up" data-aos-delay="300">
                    <div class="absolute inset-0 z-0">
                        <img src="{b64_images["serv_3"]}" class="w-full h-full object-cover opacity-10 group-hover:opacity-40 transition-opacity duration-700 mix-blend-luminosity">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-black via-brand-black/80 to-transparent"></div>
                    </div>
                    <div class="relative z-10 transform translate-y-8 group-hover:translate-y-0 transition-transform duration-500">
                        <div class="w-12 h-12 bg-brand-gold/10 flex items-center justify-center rounded-sm mb-6 text-brand-gold">
                            <i class="ph-light ph-buildings text-2xl"></i>
                        </div>
                        <h3 class="text-2xl font-display font-bold text-white mb-4 uppercase">Gayrimenkul Danışmanlığı</h3>
                        <p class="text-brand-light/60 font-light text-sm leading-relaxed opacity-0 group-hover:opacity-100 transition-opacity duration-500 delay-100">
                            Mimar gözüyle gayrimenkul yatırımlarınızı yönlendiriyor, alım, satım ve kiralama süreçlerinde profesyonel destek sağlıyoruz.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section-padding bg-brand-dark border-t border-white/5">
        <div class="container mx-auto px-4 md:px-6">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="text-5xl md:text-6xl lg:text-7xl font-display font-bold text-outline uppercase mb-4 opacity-50">Portfolio</h2>
                <h3 class="text-3xl md:text-4xl font-display font-bold text-white uppercase -mt-8 relative z-10">Öne Çıkan Projeler</h3>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                
                <!-- Project 1 -->
                <div class="project-card aspect-[4/3] group" data-aos="fade-up" data-aos-delay="100">
                    <img src="{b64_images["proj_1"]}" alt="A D Villa" class="w-full h-full object-cover">
                    <div class="project-overlay">
                        <div class="project-title">
                            <span class="text-brand-gold text-xs tracking-widest uppercase font-semibold block mb-2">Mimari / İç Mimari</span>
                            <h4 class="text-3xl font-display font-bold text-white uppercase">A D Villa</h4>
                            <div class="h-[1px] w-12 bg-brand-gold mt-4"></div>
                        </div>
                    </div>
                </div>

                <!-- Project 2 -->
                <div class="project-card aspect-[4/3] group" data-aos="fade-up" data-aos-delay="200">
                    <img src="{b64_images["proj_2"]}" alt="Minimalist İç Mekan" class="w-full h-full object-cover">
                    <div class="project-overlay">
                        <div class="project-title">
                            <span class="text-brand-gold text-xs tracking-widest uppercase font-semibold block mb-2">Anahtar Teslim</span>
                            <h4 class="text-3xl font-display font-bold text-white uppercase">Premium Residence</h4>
                            <div class="h-[1px] w-12 bg-brand-gold mt-4"></div>
                        </div>
                    </div>
                </div>

                <!-- Project 3 -->
                <div class="project-card aspect-[4/3] group" data-aos="fade-up" data-aos-delay="100">
                    <img src="{b64_images["proj_3"]}" alt="Modern Mutfak" class="w-full h-full object-cover">
                    <div class="project-overlay">
                        <div class="project-title">
                            <span class="text-brand-gold text-xs tracking-widest uppercase font-semibold block mb-2">Tasarım & Uygulama</span>
                            <h4 class="text-3xl font-display font-bold text-white uppercase">Sivas Loft</h4>
                            <div class="h-[1px] w-12 bg-brand-gold mt-4"></div>
                        </div>
                    </div>
                </div>

                <!-- Project 4 -->
                <div class="project-card aspect-[4/3] group" data-aos="fade-up" data-aos-delay="200">
                    <img src="{b64_images["proj_4"]}" alt="Lüks Yatak Odası" class="w-full h-full object-cover">
                    <div class="project-overlay">
                        <div class="project-title">
                            <span class="text-brand-gold text-xs tracking-widest uppercase font-semibold block mb-2">İç Mimari</span>
                            <h4 class="text-3xl font-display font-bold text-white uppercase">Modern Suite</h4>
                            <div class="h-[1px] w-12 bg-brand-gold mt-4"></div>
                        </div>
                    </div>
                </div>

            </div>
            
            <div class="mt-12 text-center">
                <a href="https://instagram.com/ckmimarlikgayrimenkul" target="_blank" class="btn-arch">
                    Tüm Projeler İçin Instagram'ı Ziyaret Edin
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer id="contact" class="bg-brand-black pt-24 pb-12 border-t border-white/10 relative overflow-hidden">
        <!-- Big background text -->
        <div class="absolute bottom-0 left-0 w-full overflow-hidden leading-none z-0 pointer-events-none opacity-5">
            <h2 class="text-[15vw] font-display font-black whitespace-nowrap">CK MIMARLIK</h2>
        </div>
        
        <div class="container mx-auto px-4 md:px-6 relative z-10">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-20">
                
                <div class="lg:col-span-2">
                    <a href="#" class="flex items-center gap-3 mb-8">
                        <div class="w-12 h-12 flex items-center justify-center border-2 border-brand-gold rounded bg-brand-gold">
                            <span class="font-display font-bold text-xl text-brand-black">CK</span>
                        </div>
                        <div class="flex flex-col">
                            <span class="font-display font-bold text-xl tracking-widest uppercase text-white leading-tight">Mimarlık</span>
                            <span class="font-display font-light text-xs tracking-[0.3em] text-brand-gold uppercase leading-tight">& Gayrimenkul</span>
                        </div>
                    </a>
                    <p class="text-brand-light/60 font-light text-sm leading-relaxed max-w-md">
                        Hayalinizdeki mekanı tasarlamak ve hayata geçirmek için buradayız. Mimari vizyonumuz ve gayrimenkul uzmanlığımızla yanınızdayız.
                    </p>
                </div>
                
                <div>
                    <h4 class="text-white font-display font-bold tracking-widest uppercase mb-6 text-sm">İletişim</h4>
                    <ul class="space-y-4">
                        <li class="flex items-start gap-4 text-brand-light/60 font-light text-sm">
                            <i class="ph-fill ph-map-pin text-brand-gold text-lg shrink-0 mt-0.5"></i>
                            <span>Kardeşler Mahallesi,<br>Bağdat Caddesi No: 0005<br>Sivas, Türkiye</span>
                        </li>
                        <li class="flex items-center gap-4 text-brand-light/60 font-light text-sm hover:text-brand-gold transition-colors">
                            <i class="ph-fill ph-phone text-brand-gold text-lg shrink-0"></i>
                            <a href="tel:+905555555555">+90 555 555 55 55</a>
                        </li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-white font-display font-bold tracking-widest uppercase mb-6 text-sm">Sosyal Medya</h4>
                    <a href="https://instagram.com/ckmimarlikgayrimenkul" target="_blank" class="flex items-center gap-3 text-brand-light/60 font-light text-sm hover:text-brand-gold transition-colors group">
                        <div class="w-8 h-8 rounded bg-white/5 border border-white/10 flex items-center justify-center group-hover:border-brand-gold group-hover:bg-brand-gold/10 transition-colors">
                            <i class="ph-fill ph-instagram-logo text-lg text-brand-gold"></i>
                        </div>
                        @ckmimarlikgayrimenkul
                    </a>
                </div>
                
            </div>
            
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row items-center justify-between gap-4">
                <p class="text-brand-light/40 text-xs font-light">
                    &copy; 2026 C.K Mimarlık Gayrimenkul. Tüm hakları saklıdır.
                </p>
                <div class="flex gap-6">
                    <span class="text-brand-light/40 text-xs font-light tracking-widest uppercase">Tasarım & Proje & Uygulama</span>
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
            duration: 1000,
            easing: 'ease-out-cubic',
        }});

        // Header Scroll Effect
        const header = document.getElementById('header');
        window.addEventListener('scroll', () => {{
            if (window.scrollY > 50) {{
                header.classList.add('shadow-2xl');
                header.style.background = 'rgba(5, 5, 5, 0.95)';
            }} else {{
                header.classList.remove('shadow-2xl');
                header.style.background = 'rgba(5, 5, 5, 0.85)';
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

with open("ck_mimarlik_demo.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("ck_mimarlik_demo.html created successfully.")
