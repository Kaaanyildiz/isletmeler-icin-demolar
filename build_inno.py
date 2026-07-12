import urllib.request
import base64
from io import BytesIO
from PIL import Image

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

print("Downloading images for Inno Home...")

# Home decor, accessories, interior design images
images = {
    "hero": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1600&q=80", # Beautiful bright living room
    "about": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=1000&q=80", # Elegant furniture/decor detail
    "prod_1": "https://images.unsplash.com/photo-1519710164239-da123dc03ef4?w=800&q=80", # Coffee table / interior
    "prod_2": "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=800&q=80", # Home accessories / vases
    "prod_3": "https://images.unsplash.com/photo-1540932239986-30128078f3c5?w=800&q=80", # Modern lighting / decor
    "prod_4": "https://images.unsplash.com/photo-1615529182904-14819c35db37?w=800&q=80", # Wallpaper / Texture / Living room
    "serv_1": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=800&q=80", # Interior consulting
    "serv_2": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800&q=80", # Project implementation
    "gallery_1": "https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?w=800&q=80", # Decor detail
    "gallery_2": "https://images.unsplash.com/photo-1616046229478-9901c5536a45?w=800&q=80", # Decor detail
    "gallery_3": "https://images.unsplash.com/photo-1616486029423-aaa4789e8c9a?w=800&q=80", # Decor detail
    "gallery_4": "https://images.unsplash.com/photo-1615873968403-89e068629265?w=800&q=80", # Decor detail
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
    <title>İNNO Home Design | İç Mimarlık & Dekorasyon</title>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <!-- Cinzel for elegant logo/headings, Jost for clean modern text -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
    
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
                        sans: ['Jost', 'sans-serif'],
                        serif: ['Cinzel', 'serif'],
                    }},
                    colors: {{
                        brand: {{
                            bg: '#FDFBF7', /* Warm Cream / Off-white */
                            text: '#1C1C1C', /* Soft Black */
                            accent: '#A68A64', /* Muted Champagne Gold */
                            accentLight: '#E8E1D7',
                            gray: '#8C8C8C',
                            white: '#FFFFFF'
                        }}
                    }},
                    letterSpacing: {{
                        'widest': '.2em',
                        'extrawide': '.3em',
                    }}
                }}
            }}
        }}
    </script>
    
    <style>
        body {{
            background-color: #FDFBF7;
            color: #1C1C1C;
            overflow-x: hidden;
            selection-background-color: #A68A64;
            selection-color: #FFFFFF;
        }}
        
        ::selection {{
            background: #A68A64;
            color: #FFFFFF;
        }}
        
        .hero-bg {{
            background-image: url('{b64_images["hero"]}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        .hero-overlay {{
            background: linear-gradient(to bottom, rgba(253,251,247,0.3) 0%, rgba(253,251,247,0.9) 100%);
        }}

        .glass-nav {{
            background: rgba(253, 251, 247, 0.9);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(166, 138, 100, 0.15);
        }}

        .btn-elegant {{
            display: inline-block;
            padding: 1rem 2.5rem;
            background-color: #1C1C1C;
            color: #FFFFFF;
            font-size: 0.875rem;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            transition: all 0.4s ease;
            border: 1px solid #1C1C1C;
        }}
        
        .btn-elegant:hover {{
            background-color: #A68A64;
            border-color: #A68A64;
            color: #FFFFFF;
        }}
        
        .btn-outline {{
            display: inline-block;
            padding: 1rem 2.5rem;
            background-color: transparent;
            color: #1C1C1C;
            font-size: 0.875rem;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            transition: all 0.4s ease;
            border: 1px solid #1C1C1C;
        }}
        
        .btn-outline:hover {{
            background-color: #1C1C1C;
            color: #FFFFFF;
        }}

        .product-card {{
            group: relative;
            overflow: hidden;
        }}
        
        .product-img-wrapper {{
            overflow: hidden;
            position: relative;
            aspect-ratio: 3/4;
        }}
        
        .product-img-wrapper img {{
            transition: transform 1.5s cubic-bezier(0.16, 1, 0.3, 1);
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        
        .product-card:hover .product-img-wrapper img {{
            transform: scale(1.05);
        }}

        .section-padding {{
            padding-top: 7rem;
            padding-bottom: 7rem;
        }}
        
        .line-accent {{
            height: 1px;
            width: 60px;
            background-color: #A68A64;
            display: inline-block;
            margin-bottom: 1.5rem;
        }}

        /* Subtle noise texture for premium print feel */
        .noise-overlay {{
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 9999;
            opacity: 0.03;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
        }}
        
        /* Thin border box */
        .elegant-box {{
            border: 1px solid rgba(166, 138, 100, 0.3);
            padding: 10px;
            position: relative;
        }}
        
        .elegant-box::after {{
            content: '';
            position: absolute;
            inset: -5px;
            border: 1px solid rgba(166, 138, 100, 0.1);
            pointer-events: none;
        }}
    </style>
</head>
<body class="antialiased relative">
    <div class="noise-overlay"></div>

    <!-- Header -->
    <header class="fixed w-full top-0 z-50 transition-all duration-500 py-6" id="header">
        <div class="container mx-auto px-6 md:px-12">
            <div class="flex items-center justify-between h-14">
                
                <!-- Desktop Nav Left -->
                <nav class="hidden md:flex items-center gap-8 w-1/3">
                    <a href="#about" class="text-xs font-medium text-brand-text hover:text-brand-accent transition-colors tracking-widest uppercase relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[1px] after:bg-brand-accent hover:after:w-full after:transition-all">Hikayemiz</a>
                    <a href="#services" class="text-xs font-medium text-brand-text hover:text-brand-accent transition-colors tracking-widest uppercase relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[1px] after:bg-brand-accent hover:after:w-full after:transition-all">İç Mimari</a>
                </nav>

                <!-- Logo -->
                <a href="#" class="flex flex-col items-center justify-center w-1/3 text-center group">
                    <div class="flex items-center gap-2 mb-1">
                        <div class="w-[1px] h-6 bg-brand-text/50 transform rotate-12"></div>
                        <div class="w-[1px] h-8 bg-brand-text"></div>
                        <div class="w-[1px] h-6 bg-brand-text/50 transform -rotate-12"></div>
                        <span class="font-serif text-3xl md:text-4xl tracking-widest text-brand-text ml-2">İNNO</span>
                    </div>
                    <span class="font-sans text-[0.6rem] tracking-[0.4em] text-brand-gray uppercase">Home Design</span>
                </a>

                <!-- Desktop Nav Right -->
                <nav class="hidden md:flex items-center justify-end gap-8 w-1/3">
                    <a href="#collections" class="text-xs font-medium text-brand-text hover:text-brand-accent transition-colors tracking-widest uppercase relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[1px] after:bg-brand-accent hover:after:w-full after:transition-all">Koleksiyon</a>
                    <a href="#contact" class="text-xs font-medium text-brand-text hover:text-brand-accent transition-colors tracking-widest uppercase relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[1px] after:bg-brand-accent hover:after:w-full after:transition-all">İletişim</a>
                </nav>

                <!-- Mobile Menu Button -->
                <button class="md:hidden text-brand-text p-2" id="mobile-menu-btn">
                    <i class="ph-light ph-list text-2xl"></i>
                </button>
            </div>
        </div>
        
        <!-- Mobile Nav -->
        <div class="md:hidden absolute top-full left-0 w-full glass-nav flex-col items-center py-10 gap-8 hidden" id="mobile-nav">
            <a href="#about" class="text-sm font-medium text-brand-text hover:text-brand-accent transition-colors tracking-widest uppercase">Hikayemiz</a>
            <a href="#services" class="text-sm font-medium text-brand-text hover:text-brand-accent transition-colors tracking-widest uppercase">İç Mimari</a>
            <a href="#collections" class="text-sm font-medium text-brand-text hover:text-brand-accent transition-colors tracking-widest uppercase">Koleksiyon</a>
            <a href="#contact" class="text-sm font-medium text-brand-text hover:text-brand-accent transition-colors tracking-widest uppercase">İletişim</a>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="relative h-screen flex flex-col justify-end pb-32">
        <div class="absolute inset-0 hero-bg"></div>
        <div class="absolute inset-0 hero-overlay"></div>
        
        <div class="container mx-auto px-6 md:px-12 relative z-10 text-center">
            <div data-aos="fade-up" data-aos-duration="1200">
                <span class="text-brand-accent tracking-[0.3em] uppercase text-xs font-medium block mb-6">İç Mimari & Dekorasyon</span>
                
                <h1 class="text-5xl md:text-7xl font-serif text-brand-text mb-8 leading-tight">
                    Eviniz İçin <br>
                    <span class="italic font-light">İlham Verici</span> Dokunuşlar
                </h1>
                
                <p class="text-brand-gray mb-12 font-light max-w-xl mx-auto leading-relaxed">
                    İç mimari uzmanlığıyla seçilmiş aksesuarlar, mobilyalar ve duvar kağıtları. Yaşam alanlarınızı yeniden tanımlıyoruz.
                </p>
                
                <div class="flex flex-col sm:flex-row items-center justify-center gap-6">
                    <a href="#collections" class="btn-elegant w-full sm:w-auto">Koleksiyonu Keşfet</a>
                    <a href="#services" class="btn-outline w-full sm:w-auto">Mimari Danışmanlık</a>
                </div>
            </div>
        </div>
    </section>

    <!-- About Concept -->
    <section id="about" class="section-padding bg-brand-bg relative">
        <div class="container mx-auto px-6 md:px-12">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">
                
                <div class="lg:col-span-5" data-aos="fade-right">
                    <div class="line-accent"></div>
                    <h4 class="text-brand-gray tracking-widest uppercase text-xs font-medium mb-4">İnno Home Design</h4>
                    <h2 class="text-4xl font-serif text-brand-text mb-8 leading-snug">Yaşam Alanlarına <br><span class="italic text-brand-accent">Estetik Bir Ruh</span> Katıyoruz.</h2>
                    
                    <p class="text-brand-text/80 mb-6 font-light leading-relaxed">
                        Sivas Bağdat Caddesi'nde yer alan mağazamızda, sadece bir ev dekorasyonu değil, bir yaşam tarzı sunuyoruz. Seçkin mobilya gruplarımız, zigon ve orta sehpalarımız, ithal duvar kağıtlarımız ve özenle seçilmiş aksesuarlarımızla evinizin her köşesine zarafet taşıyoruz.
                    </p>
                    <p class="text-brand-text/80 mb-10 font-light leading-relaxed">
                        Profesyonel iç mimari ekibimizle proje, tasarım ve uygulama süreçlerinizi baştan sona yönetiyor, hayallerinizdeki mekanları gerçeğe dönüştürüyoruz.
                    </p>
                    
                    <a href="https://instagram.com/innohomedesigns" target="_blank" class="inline-flex items-center gap-3 text-brand-text hover:text-brand-accent transition-colors font-medium tracking-widest uppercase text-xs">
                        <span>Bizi Instagram'da Takip Edin</span>
                        <i class="ph-light ph-arrow-right text-lg"></i>
                    </a>
                </div>
                
                <div class="lg:col-span-7 relative" data-aos="fade-left">
                    <div class="elegant-box p-4 md:p-6 bg-white">
                        <img src="{b64_images["about"]}" alt="İnno Home İç Mekan" class="w-full h-auto object-cover">
                    </div>
                    <!-- Floating Badge -->
                    <div class="absolute -bottom-10 -left-10 bg-brand-text text-white p-8 rounded-full w-40 h-40 flex flex-col items-center justify-center text-center hidden md:flex animate-[spin_30s_linear_infinite]">
                        <svg viewBox="0 0 100 100" class="absolute w-full h-full p-2">
                            <path id="curve" d="M 50,50 m -35,0 a 35,35 0 1,1 70,0 a 35,35 0 1,1 -70,0" fill="transparent"/>
                            <text class="text-[10px] tracking-widest uppercase fill-white">
                                <textPath href="#curve" startOffset="0%">• İÇ MİMARİ • DEKORASYON • TASARIM </textPath>
                            </text>
                        </svg>
                        <i class="ph-light ph-house-line text-3xl"></i>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Collections -->
    <section id="collections" class="section-padding bg-white border-y border-brand-accentLight">
        <div class="container mx-auto px-6 md:px-12">
            <div class="text-center mb-20" data-aos="fade-up">
                <div class="line-accent mx-auto"></div>
                <h2 class="text-4xl font-serif text-brand-text mb-4">Özel Koleksiyonlar</h2>
                <p class="text-brand-gray font-light">Evinizin karakterini yansıtacak seçkin parçalar.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                
                <!-- Category 1 -->
                <a href="#" class="product-card group block" data-aos="fade-up" data-aos-delay="100">
                    <div class="product-img-wrapper mb-6 bg-brand-bg">
                        <img src="{b64_images["prod_1"]}" alt="Orta & Zigon Sehpa">
                    </div>
                    <div class="text-center">
                        <h3 class="text-lg font-serif text-brand-text mb-1 group-hover:text-brand-accent transition-colors">Orta & Zigon Sehpa</h3>
                        <span class="text-xs text-brand-gray tracking-widest uppercase">Mobilya</span>
                    </div>
                </a>

                <!-- Category 2 -->
                <a href="#" class="product-card group block" data-aos="fade-up" data-aos-delay="200">
                    <div class="product-img-wrapper mb-6 bg-brand-bg">
                        <img src="{b64_images["prod_2"]}" alt="Aksesuar & Dekor">
                    </div>
                    <div class="text-center">
                        <h3 class="text-lg font-serif text-brand-text mb-1 group-hover:text-brand-accent transition-colors">Ev Aksesuarları</h3>
                        <span class="text-xs text-brand-gray tracking-widest uppercase">Dekorasyon</span>
                    </div>
                </a>

                <!-- Category 3 -->
                <a href="#" class="product-card group block" data-aos="fade-up" data-aos-delay="300">
                    <div class="product-img-wrapper mb-6 bg-brand-bg">
                        <img src="{b64_images["prod_3"]}" alt="Aydınlatma">
                    </div>
                    <div class="text-center">
                        <h3 class="text-lg font-serif text-brand-text mb-1 group-hover:text-brand-accent transition-colors">Aydınlatma Grubu</h3>
                        <span class="text-xs text-brand-gray tracking-widest uppercase">Ambiyans</span>
                    </div>
                </a>

                <!-- Category 4 -->
                <a href="#" class="product-card group block" data-aos="fade-up" data-aos-delay="400">
                    <div class="product-img-wrapper mb-6 bg-brand-bg">
                        <img src="{b64_images["prod_4"]}" alt="Duvar Kağıdı">
                    </div>
                    <div class="text-center">
                        <h3 class="text-lg font-serif text-brand-text mb-1 group-hover:text-brand-accent transition-colors">İthal Duvar Kağıtları</h3>
                        <span class="text-xs text-brand-gray tracking-widest uppercase">Tasarım</span>
                    </div>
                </a>
                
            </div>
            
            <div class="text-center mt-16">
                <a href="#contact" class="btn-outline">Tüm Ürünleri İncelemek İçin Mağazamıza Bekliyoruz</a>
            </div>
        </div>
    </section>

    <!-- Services Banner -->
    <section id="services" class="py-24 bg-brand-text relative overflow-hidden">
        <div class="absolute inset-0 opacity-10">
            <img src="{b64_images["serv_2"]}" class="w-full h-full object-cover">
        </div>
        <div class="container mx-auto px-6 md:px-12 relative z-10">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-16">
                <div data-aos="fade-up">
                    <h2 class="text-3xl font-serif text-white mb-6">İç Mimari <span class="italic text-brand-accent">Danışmanlık</span></h2>
                    <p class="text-brand-gray font-light leading-relaxed mb-8">
                        Mekanlarınızı sadece eşyalarla doldurmuyor, yaşam alışkanlıklarınıza ve zevklerinize uygun olarak yeniden tasarlıyoruz. Profesyonel ekibimizle mekanın potansiyelini analiz ediyor, size özel 3D tasarımlar hazırlıyoruz.
                    </p>
                    <ul class="space-y-4 text-white/80 font-light">
                        <li class="flex items-center gap-3"><i class="ph-fill ph-check-circle text-brand-accent"></i> Kişiye Özel Mekan Tasarımı</li>
                        <li class="flex items-center gap-3"><i class="ph-fill ph-check-circle text-brand-accent"></i> Mobilya & Aksesuar Seçimi</li>
                        <li class="flex items-center gap-3"><i class="ph-fill ph-check-circle text-brand-accent"></i> Renk ve Doku Danışmanlığı</li>
                    </ul>
                </div>
                <div data-aos="fade-up" data-aos-delay="200">
                    <h2 class="text-3xl font-serif text-white mb-6">Proje & <span class="italic text-brand-accent">Uygulama</span></h2>
                    <p class="text-brand-gray font-light leading-relaxed mb-8">
                        Tasarımı onaylanmış projelerin hayata geçme sürecinde, usta ekiplerimizle anahtar teslim hizmet sunuyoruz. Sürecin her adımında kalite kontrolünü sağlıyor, mekanı kullanıma hazır halde teslim ediyoruz.
                    </p>
                    <a href="#contact" class="inline-flex items-center gap-2 text-white hover:text-brand-accent transition-colors font-medium tracking-widest uppercase text-xs pb-1 border-b border-brand-accent">
                        <span>Projeniz İçin Teklif Alın</span>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Teslimler / Instagram Gallery -->
    <section class="section-padding bg-brand-bg">
        <div class="container mx-auto px-6 md:px-12">
            <div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-6" data-aos="fade-up">
                <div>
                    <h2 class="text-3xl font-serif text-brand-text mb-2">Mutlu Evler</h2>
                    <p class="text-brand-gray font-light">Teslimini gerçekleştirdiğimiz bazı projeler ve ürünler</p>
                </div>
                <a href="https://instagram.com/innohomedesigns" target="_blank" class="flex items-center gap-2 text-brand-text hover:text-brand-accent font-medium tracking-widest uppercase text-xs">
                    <i class="ph-light ph-instagram-logo text-xl"></i>
                    <span>@innohomedesigns</span>
                </a>
            </div>

            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <a href="https://instagram.com/innohomedesigns" target="_blank" class="group relative overflow-hidden aspect-square block" data-aos="zoom-in" data-aos-delay="100">
                    <img src="{b64_images["gallery_1"]}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-brand-text/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ph-fill ph-heart text-white text-3xl"></i>
                    </div>
                </a>
                <a href="https://instagram.com/innohomedesigns" target="_blank" class="group relative overflow-hidden aspect-square block" data-aos="zoom-in" data-aos-delay="200">
                    <img src="{b64_images["gallery_2"]}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-brand-text/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ph-fill ph-heart text-white text-3xl"></i>
                    </div>
                </a>
                <a href="https://instagram.com/innohomedesigns" target="_blank" class="group relative overflow-hidden aspect-square block" data-aos="zoom-in" data-aos-delay="300">
                    <img src="{b64_images["gallery_3"]}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-brand-text/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ph-fill ph-heart text-white text-3xl"></i>
                    </div>
                </a>
                <a href="https://instagram.com/innohomedesigns" target="_blank" class="group relative overflow-hidden aspect-square block" data-aos="zoom-in" data-aos-delay="400">
                    <img src="{b64_images["gallery_4"]}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-brand-text/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ph-fill ph-heart text-white text-3xl"></i>
                    </div>
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer id="contact" class="bg-white pt-24 pb-12 border-t border-brand-accentLight">
        <div class="container mx-auto px-6 md:px-12">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-20">
                
                <div class="lg:col-span-1">
                    <a href="#" class="flex flex-col items-start mb-6">
                        <div class="flex items-center gap-2 mb-1">
                            <div class="w-[1px] h-6 bg-brand-text/50 transform rotate-12"></div>
                            <div class="w-[1px] h-8 bg-brand-text"></div>
                            <div class="w-[1px] h-6 bg-brand-text/50 transform -rotate-12"></div>
                            <span class="font-serif text-2xl tracking-widest text-brand-text ml-2">İNNO</span>
                        </div>
                        <span class="font-sans text-[0.55rem] tracking-[0.4em] text-brand-gray uppercase">Home Design</span>
                    </a>
                    <p class="text-brand-gray font-light text-sm leading-relaxed mb-6">
                        Ev dekorasyonunda zarafeti ve kaliteyi bir araya getiriyoruz. İç mimari dokunuşlarla yaşam alanlarınızı güzelleştiriyoruz.
                    </p>
                </div>
                
                <div>
                    <h4 class="text-brand-text font-serif text-lg mb-6">İletişim</h4>
                    <ul class="space-y-4">
                        <li class="flex items-start gap-3 text-brand-gray font-light text-sm">
                            <i class="ph-light ph-map-pin text-brand-accent text-lg shrink-0"></i>
                            <span>Bağdat Cad. Kardeşler Mah. No:29B<br>Sivas, Türkiye</span>
                        </li>
                        <li class="flex items-center gap-3 text-brand-gray font-light text-sm">
                            <i class="ph-light ph-phone text-brand-accent text-lg shrink-0"></i>
                            <a href="tel:+905555555555" class="hover:text-brand-accent transition-colors">+90 555 555 55 55</a>
                        </li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-brand-text font-serif text-lg mb-6">Çalışma Saatleri</h4>
                    <ul class="space-y-3 text-brand-gray font-light text-sm">
                        <li class="flex justify-between">
                            <span>Pazartesi - Cumartesi</span>
                            <span class="text-brand-text">09:00 - 20:00</span>
                        </li>
                        <li class="flex justify-between">
                            <span>Pazar</span>
                            <span class="text-brand-text">Kapalı</span>
                        </li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-brand-text font-serif text-lg mb-6">Sosyal Medya</h4>
                    <p class="text-brand-gray font-light text-sm mb-4">Yeni koleksiyonlarımızı ve projelerimizi Instagram'dan takip edin.</p>
                    <a href="https://instagram.com/innohomedesigns" target="_blank" class="w-10 h-10 rounded-full border border-brand-accentLight flex items-center justify-center text-brand-text hover:bg-brand-text hover:text-white transition-colors">
                        <i class="ph-fill ph-instagram-logo text-lg"></i>
                    </a>
                </div>
                
            </div>
            
            <div class="border-t border-brand-accentLight pt-8 flex flex-col md:flex-row items-center justify-between gap-4">
                <p class="text-brand-gray text-xs font-light">
                    &copy; 2026 İNNO Home Design İç Mimarlık. Tüm hakları saklıdır.
                </p>
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
            duration: 900,
            easing: 'ease-out-cubic',
        }});

        // Header Scroll Effect
        const header = document.getElementById('header');
        window.addEventListener('scroll', () => {{
            if (window.scrollY > 50) {{
                header.classList.add('shadow-sm');
                header.classList.remove('py-6');
                header.classList.add('py-3');
                header.style.background = 'rgba(253, 251, 247, 0.95)';
            }} else {{
                header.classList.remove('shadow-sm');
                header.classList.add('py-6');
                header.classList.remove('py-3');
                header.style.background = 'rgba(253, 251, 247, 0.9)';
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

with open("inno_home_demo.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("inno_home_demo.html created successfully.")
