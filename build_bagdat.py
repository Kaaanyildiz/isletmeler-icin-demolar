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

print("Downloading images for Bagdat Game Station...")

# Gamer / Neon / Dark Room vibes
images = {
    "hero": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1600&q=80", # Gaming setup / Esports / Neon
    "vip_1": "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?w=1000&q=80", # VR / Neon red / Cyberpunk
    "vip_2": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=800&q=80", # PS5 controller / Dark
    "game_1": "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?w=800&q=80", # Gaming console / lights
    "game_2": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=800&q=80", # Neon gamer room
    "game_3": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&q=80", # Big TV screen
    "game_4": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=800&q=80", # Arcade / Neon
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
    <title>Bağdat Game Station | Şehrin En İyi Oyun Deneyimi</title>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <!-- Rajdhani for tech/gamer feel, Inter for text -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
    
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
                        gamer: ['Rajdhani', 'sans-serif'],
                    }},
                    colors: {{
                        brand: {{
                            black: '#09090b', /* Deep black */
                            surface: '#18181b', /* Zinc 900 */
                            neon: '#ff003c', /* Cyberpunk Red */
                            neonDark: '#cc0030',
                            white: '#ffffff',
                            gray: '#a1a1aa'
                        }}
                    }},
                    boxShadow: {{
                        'neon': '0 0 15px rgba(255, 0, 60, 0.5), 0 0 30px rgba(255, 0, 60, 0.3)',
                        'neon-strong': '0 0 20px rgba(255, 0, 60, 0.8), 0 0 40px rgba(255, 0, 60, 0.5)',
                    }}
                }}
            }}
        }}
    </script>
    
    <style>
        body {{
            background-color: #09090b;
            color: #ffffff;
            overflow-x: hidden;
            selection-background-color: #ff003c;
            selection-color: #ffffff;
        }}
        
        ::selection {{
            background: #ff003c;
            color: #ffffff;
        }}
        
        /* Grid background for cyberpunk feel */
        .cyber-grid {{
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background-image: 
                linear-gradient(to right, rgba(255,0,60,0.03) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(255,0,60,0.03) 1px, transparent 1px);
            background-size: 50px 50px;
            z-index: -1;
            pointer-events: none;
            transform: perspective(500px) rotateX(60deg) scale(2);
            transform-origin: center top;
            opacity: 0.5;
        }}

        .hero-bg {{
            background-image: url('{b64_images["hero"]}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            filter: grayscale(80%) contrast(120%);
        }}
        
        .hero-overlay {{
            background: linear-gradient(to bottom, rgba(9,9,11,0.6) 0%, rgba(9,9,11,1) 100%);
        }}

        .glass-nav {{
            background: rgba(9, 9, 11, 0.8);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255, 0, 60, 0.2);
        }}

        .btn-cyber {{
            position: relative;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 1rem 2rem;
            background: transparent;
            color: #ffffff;
            font-family: 'Rajdhani', sans-serif;
            text-transform: uppercase;
            font-weight: 700;
            font-size: 1.125rem;
            letter-spacing: 0.1em;
            border: 2px solid #ff003c;
            transition: all 0.3s ease;
            box-shadow: 0 0 10px rgba(255, 0, 60, 0.2) inset;
            overflow: hidden;
            z-index: 1;
        }}
        
        .btn-cyber::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: #ff003c;
            z-index: -1;
            transform: scaleX(0);
            transform-origin: right;
            transition: transform 0.3s ease;
        }}
        
        .btn-cyber:hover {{
            box-shadow: 0 0 20px rgba(255, 0, 60, 0.6);
            color: #ffffff;
        }}
        
        .btn-cyber:hover::before {{
            transform: scaleX(1);
            transform-origin: left;
        }}

        /* Glitch text effect */
        .glitch {{
            position: relative;
            color: white;
        }}
        
        .glitch::before, .glitch::after {{
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #09090b;
        }}
        
        .glitch::before {{
            left: 2px;
            text-shadow: -2px 0 #ff003c;
            clip: rect(24px, 550px, 90px, 0);
            animation: glitch-anim-2 3s infinite linear alternate-reverse;
        }}
        
        .glitch::after {{
            left: -2px;
            text-shadow: -2px 0 #00ffff;
            clip: rect(85px, 550px, 140px, 0);
            animation: glitch-anim 2.5s infinite linear alternate-reverse;
        }}
        
        @keyframes glitch-anim {{
            0% {{ clip: rect(13px, 9999px, 86px, 0); }}
            20% {{ clip: rect(66px, 9999px, 12px, 0); }}
            40% {{ clip: rect(104px, 9999px, 98px, 0); }}
            60% {{ clip: rect(11px, 9999px, 73px, 0); }}
            80% {{ clip: rect(79px, 9999px, 129px, 0); }}
            100% {{ clip: rect(4px, 9999px, 54px, 0); }}
        }}
        
        @keyframes glitch-anim-2 {{
            0% {{ clip: rect(49px, 9999px, 20px, 0); }}
            20% {{ clip: rect(22px, 9999px, 114px, 0); }}
            40% {{ clip: rect(98px, 9999px, 43px, 0); }}
            60% {{ clip: rect(122px, 9999px, 11px, 0); }}
            80% {{ clip: rect(83px, 9999px, 95px, 0); }}
            100% {{ clip: rect(31px, 9999px, 67px, 0); }}
        }}

        .game-card {{
            position: relative;
            overflow: hidden;
            border-radius: 0.5rem;
            border: 1px solid rgba(255, 0, 60, 0.1);
            transition: all 0.3s ease;
        }}
        
        .game-card:hover {{
            border-color: rgba(255, 0, 60, 0.8);
            box-shadow: 0 0 20px rgba(255, 0, 60, 0.3);
            transform: translateY(-5px);
        }}
        
        .game-card img {{
            transition: transform 0.5s ease;
        }}
        
        .game-card:hover img {{
            transform: scale(1.1);
        }}

        .text-neon {{
            color: #ff003c;
            text-shadow: 0 0 10px rgba(255,0,60,0.5);
        }}

        .section-padding {{
            padding-top: 6rem;
            padding-bottom: 6rem;
        }}
        
        /* Lion Logo styling */
        .lion-logo {{
            filter: drop-shadow(0 0 8px rgba(255, 0, 60, 0.8));
        }}
    </style>
</head>
<body class="antialiased">
    <div class="cyber-grid"></div>

    <!-- Header -->
    <header class="fixed w-full top-0 z-50 glass-nav transition-all duration-300" id="header">
        <div class="container mx-auto px-4 md:px-8">
            <div class="flex items-center justify-between h-20 md:h-24">
                
                <!-- Logo -->
                <a href="#" class="flex items-center gap-3">
                    <div class="w-12 h-12 md:w-14 md:h-14 bg-brand-black rounded-full border-2 border-brand-neon flex items-center justify-center lion-logo overflow-hidden">
                        <!-- Abstract Lion representation using SVG since we don't have the exact image -->
                        <svg viewBox="0 0 24 24" fill="none" stroke="#ff003c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-8 h-8"><path d="M12 2C7.58 2 4 5.58 4 10c0 1.57.46 3.03 1.24 4.26L4 22l4-2h8l4 2-1.24-7.74C19.54 13.03 20 11.57 20 10c0-4.42-3.58-8-8-8z"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><path d="M9 9h.01"/><path d="M15 9h.01"/></svg>
                    </div>
                    <div class="flex flex-col">
                        <span class="font-gamer font-bold text-xl md:text-2xl text-white tracking-wide uppercase leading-none">Bağdat</span>
                        <span class="font-gamer font-bold text-sm md:text-md text-brand-neon tracking-widest uppercase leading-none mt-1">Game Station</span>
                    </div>
                </a>

                <!-- Desktop Nav -->
                <nav class="hidden md:flex items-center gap-8">
                    <a href="#about" class="font-gamer text-lg font-bold text-white hover:text-brand-neon transition-colors tracking-wider uppercase">Mekan</a>
                    <a href="#vip" class="font-gamer text-lg font-bold text-white hover:text-brand-neon transition-colors tracking-wider uppercase">VIP Odalar</a>
                    <a href="#games" class="font-gamer text-lg font-bold text-white hover:text-brand-neon transition-colors tracking-wider uppercase">Oyunlar</a>
                    <a href="#contact" class="btn-cyber py-2 px-6 text-sm">
                        Rezervasyon
                        <i class="ph-bold ph-crosshair"></i>
                    </a>
                </nav>

                <!-- Mobile Menu Button -->
                <button class="md:hidden text-brand-neon p-2" id="mobile-menu-btn">
                    <i class="ph-bold ph-list text-3xl"></i>
                </button>
            </div>
        </div>
        
        <!-- Mobile Nav -->
        <div class="md:hidden absolute top-full left-0 w-full glass-nav flex-col items-center py-6 gap-6 hidden border-t border-brand-neon/30" id="mobile-nav">
            <a href="#about" class="font-gamer text-xl font-bold text-white hover:text-brand-neon transition-colors tracking-wider uppercase">Mekan</a>
            <a href="#vip" class="font-gamer text-xl font-bold text-white hover:text-brand-neon transition-colors tracking-wider uppercase">VIP Odalar</a>
            <a href="#games" class="font-gamer text-xl font-bold text-white hover:text-brand-neon transition-colors tracking-wider uppercase">Oyunlar</a>
            <a href="#contact" class="btn-cyber py-3 px-8 text-lg w-[80%] justify-center mt-2">Rezervasyon</a>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="relative h-screen flex items-center justify-center pt-20">
        <div class="absolute inset-0 hero-bg"></div>
        <div class="absolute inset-0 hero-overlay"></div>
        
        <div class="container mx-auto px-4 relative z-10">
            <div class="max-w-4xl mx-auto text-center" data-aos="zoom-in" data-aos-duration="1000">
                <div class="inline-flex items-center justify-center gap-2 mb-6 bg-brand-neon/10 border border-brand-neon/30 px-4 py-1.5 rounded-full backdrop-blur-sm">
                    <span class="w-2 h-2 rounded-full bg-brand-neon animate-pulse"></span>
                    <span class="font-gamer text-brand-neon tracking-widest uppercase text-sm font-bold">Her Gün 12:00 - 04:00 Açık</span>
                </div>
                
                <h1 class="text-6xl md:text-8xl lg:text-9xl font-gamer font-bold text-white mb-4 uppercase leading-none glitch" data-text="GAME ON.">
                    GAME ON.
                </h1>
                
                <h2 class="text-2xl md:text-4xl font-gamer font-bold text-white mb-8 uppercase tracking-widest">
                    Şehrin En İyi <span class="text-neon">Oyun Deneyimi</span>
                </h2>
                
                <p class="text-brand-gray text-lg md:text-xl mb-12 max-w-2xl mx-auto">
                    VIP odalar, en güncel konsol oyunları, kesintisiz internet ve limitsiz eğlence. Sivas'ın kalbinde gerçek oyuncuların buluşma noktası.
                </p>
                
                <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                    <a href="#contact" class="btn-cyber w-full sm:w-auto justify-center">
                        <i class="ph-fill ph-game-controller text-xl"></i>
                        <span>Yerini Ayırt</span>
                    </a>
                </div>
            </div>
        </div>
        
        <div class="absolute bottom-10 left-1/2 -translate-x-1/2 animate-bounce hidden md:block">
            <a href="#about" class="text-brand-neon">
                <i class="ph-bold ph-caret-double-down text-3xl"></i>
            </a>
        </div>
    </section>

    <!-- Features / VIP -->
    <section id="vip" class="section-padding bg-brand-surface relative border-t border-brand-neon/20">
        <!-- Neon Glow -->
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-brand-neon/10 rounded-full blur-[120px] pointer-events-none"></div>
        
        <div class="container mx-auto px-4 md:px-8 relative z-10">
            <div class="flex flex-col lg:flex-row gap-16 items-center">
                
                <div class="w-full lg:w-1/2" data-aos="fade-right">
                    <div class="relative">
                        <div class="absolute inset-0 bg-brand-neon mix-blend-color translate-x-4 translate-y-4 rounded-xl z-0 opacity-50 blur-sm"></div>
                        <img src="{b64_images["vip_1"]}" alt="VIP Oda" class="relative z-10 rounded-xl w-full border border-brand-neon/30 grayscale hover:grayscale-0 transition-all duration-500">
                        
                        <!-- Floating Badge -->
                        <div class="absolute -bottom-8 -right-8 bg-brand-black border border-brand-neon p-6 rounded-xl z-20 shadow-neon">
                            <h4 class="font-gamer font-bold text-3xl text-white uppercase mb-1">VIP</h4>
                            <p class="text-brand-neon font-bold tracking-widest text-sm uppercase">Odalar</p>
                        </div>
                    </div>
                </div>

                <div class="w-full lg:w-1/2" data-aos="fade-left">
                    <h4 class="font-gamer text-brand-neon tracking-widest uppercase text-lg font-bold mb-2">Özel Alanınız</h4>
                    <h2 class="text-4xl md:text-5xl font-gamer font-bold text-white mb-6 uppercase">Sinema ve Oyun <br><span class="text-neon">Bir Arada</span></h2>
                    
                    <p class="text-brand-gray text-lg mb-8 leading-relaxed">
                        Sadece size ve arkadaşlarınıza özel tasarlanmış VIP odalarımızda rahatlığın zirvesine ulaşın. Geniş ekran TV'ler, rahat koltuklar ve muazzam ses sistemi ile oyun oynamak veya film izlemek artık çok daha keyifli.
                    </p>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded bg-brand-neon/10 border border-brand-neon/30 flex items-center justify-center text-brand-neon shrink-0">
                                <i class="ph-fill ph-monitor-play text-2xl"></i>
                            </div>
                            <div>
                                <h4 class="font-gamer font-bold text-xl text-white uppercase mb-1">Netflix & Amazon</h4>
                                <p class="text-brand-gray text-sm">Favori dizilerinizi ve filmlerinizi VIP rahatlığında izleyin.</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded bg-brand-neon/10 border border-brand-neon/30 flex items-center justify-center text-brand-neon shrink-0">
                                <i class="ph-fill ph-game-controller text-2xl"></i>
                            </div>
                            <div>
                                <h4 class="font-gamer font-bold text-xl text-white uppercase mb-1">Konsol & Maç</h4>
                                <p class="text-brand-gray text-sm">Derbi maçlarını dev ekranda izleyin veya PES turnuvası yapın.</p>
                            </div>
                        </div>
                    </div>
                    
                    <a href="#contact" class="btn-cyber">VIP Oda Rezervasyonu</a>
                </div>

            </div>
        </div>
    </section>

    <!-- Games Library -->
    <section id="games" class="section-padding bg-brand-black">
        <div class="container mx-auto px-4 md:px-8">
            <div class="text-center mb-16" data-aos="fade-up">
                <h4 class="font-gamer text-brand-neon tracking-widest uppercase text-lg font-bold mb-2">Kütüphane</h4>
                <h2 class="text-4xl md:text-5xl font-gamer font-bold text-white uppercase">Popüler <span class="text-neon">Oyunlar</span></h2>
                <p class="text-brand-gray mt-4 max-w-2xl mx-auto">En yeni çıkan oyunlar ve efsane klasikler Bağdat Game Station'da seni bekliyor.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Game 1 -->
                <div class="game-card group" data-aos="fade-up" data-aos-delay="100">
                    <div class="aspect-[3/4] relative overflow-hidden bg-brand-surface">
                        <img src="{b64_images["game_1"]}" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 mix-blend-luminosity group-hover:mix-blend-normal">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-black via-transparent to-transparent opacity-90"></div>
                        <div class="absolute bottom-0 left-0 w-full p-6">
                            <h3 class="font-gamer font-bold text-2xl text-white uppercase mb-1">Aksiyon & Macera</h3>
                            <div class="h-1 w-12 bg-brand-neon transition-all duration-300 group-hover:w-full"></div>
                        </div>
                    </div>
                </div>

                <!-- Game 2 -->
                <div class="game-card group" data-aos="fade-up" data-aos-delay="200">
                    <div class="aspect-[3/4] relative overflow-hidden bg-brand-surface">
                        <img src="{b64_images["game_2"]}" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 mix-blend-luminosity group-hover:mix-blend-normal">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-black via-transparent to-transparent opacity-90"></div>
                        <div class="absolute bottom-0 left-0 w-full p-6">
                            <h3 class="font-gamer font-bold text-2xl text-white uppercase mb-1">FPS & Shooter</h3>
                            <div class="h-1 w-12 bg-brand-neon transition-all duration-300 group-hover:w-full"></div>
                        </div>
                    </div>
                </div>

                <!-- Game 3 -->
                <div class="game-card group" data-aos="fade-up" data-aos-delay="300">
                    <div class="aspect-[3/4] relative overflow-hidden bg-brand-surface">
                        <img src="{b64_images["vip_2"]}" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 mix-blend-luminosity group-hover:mix-blend-normal">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-black via-transparent to-transparent opacity-90"></div>
                        <div class="absolute bottom-0 left-0 w-full p-6">
                            <h3 class="font-gamer font-bold text-2xl text-white uppercase mb-1">Spor & Yarış</h3>
                            <div class="h-1 w-12 bg-brand-neon transition-all duration-300 group-hover:w-full"></div>
                        </div>
                    </div>
                </div>

                <!-- Game 4 -->
                <div class="game-card group" data-aos="fade-up" data-aos-delay="400">
                    <div class="aspect-[3/4] relative overflow-hidden bg-brand-surface">
                        <img src="{b64_images["game_4"]}" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 mix-blend-luminosity group-hover:mix-blend-normal">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-black via-transparent to-transparent opacity-90"></div>
                        <div class="absolute bottom-0 left-0 w-full p-6">
                            <h3 class="font-gamer font-bold text-2xl text-white uppercase mb-1">Co-Op & Party</h3>
                            <div class="h-1 w-12 bg-brand-neon transition-all duration-300 group-hover:w-full"></div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="mt-12 text-center">
                <p class="text-brand-gray mb-6">Call Of Duty, Cyberpunk, Spider-Man 2, A Way Out, FC 24, PES 2021 ve daha yüzlercesi...</p>
            </div>
        </div>
    </section>

    <!-- Experience Banner -->
    <section class="py-24 bg-brand-neon relative overflow-hidden">
        <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4IiBoZWlnaHQ9IjgiPgo8cmVjdCB3aWR0aD0iOCIgaGVpZ2h0PSI4IiBmaWxsPSIjZmYwMDNjIj48L3JlY3Q+CjxwYXRoIGQ9Ik0wIDBMOCA4Wk04IDBMMCA4WiIgc3Ryb2tlPSIjY2MwMDMwIiBzdHJva2Utd2lkdGg9IjEiPjwvcGF0aD4KPC9zdmc+')] opacity-20"></div>
        <div class="container mx-auto px-4 relative z-10 text-center">
            <h2 class="text-4xl md:text-6xl font-gamer font-bold text-white uppercase mb-6 drop-shadow-lg">Gecenin Ruhu Senle. <br>12:00'den 04:00'e Kadar.</h2>
            <p class="text-white/90 text-lg md:text-xl font-medium max-w-2xl mx-auto mb-10">
                Gecenin ilerleyen saatlerinde kesintisiz oyun heyecanı Bağdat Game Station'da. Kendi takımını kur, VIP odanı ayırt ve sabaha kadar oyna.
            </p>
            <a href="https://instagram.com/bagdatgamestation" target="_blank" class="inline-flex items-center gap-2 bg-brand-black text-white font-gamer font-bold text-xl uppercase px-8 py-4 hover:bg-white hover:text-brand-black transition-colors border-2 border-brand-black">
                <i class="ph-bold ph-instagram-logo text-2xl"></i>
                Bizi Takip Et
            </a>
        </div>
    </section>

    <!-- Footer / Contact -->
    <footer id="contact" class="bg-brand-surface pt-20 pb-10 border-t border-brand-neon/30 relative">
        <div class="container mx-auto px-4 md:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
                
                <div class="lg:col-span-1">
                    <a href="#" class="flex items-center gap-3 mb-6">
                        <div class="w-12 h-12 bg-brand-black rounded-full border border-brand-neon flex items-center justify-center lion-logo overflow-hidden">
                            <svg viewBox="0 0 24 24" fill="none" stroke="#ff003c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-8 h-8"><path d="M12 2C7.58 2 4 5.58 4 10c0 1.57.46 3.03 1.24 4.26L4 22l4-2h8l4 2-1.24-7.74C19.54 13.03 20 11.57 20 10c0-4.42-3.58-8-8-8z"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><path d="M9 9h.01"/><path d="M15 9h.01"/></svg>
                        </div>
                        <div class="flex flex-col">
                            <span class="font-gamer font-bold text-xl text-white tracking-wide uppercase leading-none">Bağdat</span>
                            <span class="font-gamer font-bold text-sm text-brand-neon tracking-widest uppercase leading-none mt-1">Game Station</span>
                        </div>
                    </a>
                    <p class="text-brand-gray font-medium text-sm leading-relaxed mb-6">
                        Şehrin en popüler oyun kütüphanesi, VIP odaları ve kesintisiz gece eğlencesi.
                    </p>
                </div>
                
                <div>
                    <h4 class="text-white font-gamer font-bold text-2xl tracking-wider uppercase mb-6 border-l-4 border-brand-neon pl-3">İletişim</h4>
                    <ul class="space-y-4">
                        <li class="flex items-start gap-3 text-brand-gray">
                            <i class="ph-fill ph-map-pin text-brand-neon text-xl shrink-0 mt-0.5"></i>
                            <span class="font-medium text-sm">Kardeşler Mahallesi 51-18. Sk.3,<br>Sivas 58000</span>
                        </li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-white font-gamer font-bold text-2xl tracking-wider uppercase mb-6 border-l-4 border-brand-neon pl-3">Çalışma Saatleri</h4>
                    <ul class="space-y-3 text-brand-gray font-medium text-sm">
                        <li class="flex justify-between items-center bg-brand-black/50 p-2 rounded border border-white/5">
                            <span>Pzt - Paz</span>
                            <span class="text-brand-neon font-bold">12:00 - 04:00</span>
                        </li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-white font-gamer font-bold text-2xl tracking-wider uppercase mb-6 border-l-4 border-brand-neon pl-3">Rezervasyon</h4>
                    <p class="text-brand-gray font-medium text-sm mb-4">Masanızı veya VIP odanızı önceden ayırtın, beklemeyin.</p>
                    <a href="#" class="w-full btn-cyber py-3 flex items-center justify-center gap-2">
                        <i class="ph-bold ph-calendar-plus text-xl"></i>
                        <span>DM Gönder</span>
                    </a>
                </div>
                
            </div>
            
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row items-center justify-between gap-4">
                <p class="text-brand-gray text-sm font-medium">
                    &copy; 2026 Bağdat Game Station. Tüm hakları saklıdır.
                </p>
                <div class="flex gap-4">
                    <a href="#" class="w-10 h-10 rounded bg-brand-black border border-white/10 flex items-center justify-center text-white hover:border-brand-neon hover:text-brand-neon transition-colors">
                        <i class="ph-fill ph-instagram-logo text-xl"></i>
                    </a>
                    <a href="#" class="w-10 h-10 rounded bg-brand-black border border-white/10 flex items-center justify-center text-white hover:border-brand-neon hover:text-brand-neon transition-colors">
                        <i class="ph-fill ph-tiktok-logo text-xl"></i>
                    </a>
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
                header.style.background = 'rgba(9, 9, 11, 0.95)';
                header.classList.add('shadow-neon');
            }} else {{
                header.style.background = 'rgba(9, 9, 11, 0.8)';
                header.classList.remove('shadow-neon');
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

with open("bagdat_game_demo.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("bagdat_game_demo.html created successfully.")
