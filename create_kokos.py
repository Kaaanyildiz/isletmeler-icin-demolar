import os

html_content = """<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KoKoŞ Saç Tasarım | Bir Kuaför Salonundan Daha Fazlası</title>
    <meta name="description" content="Sivas'ın en iddialı saç tasarım ve kuaför salonu. Ombre, sombre, gelin başı ve profesyonel kaş alımı için KoKoŞ'a davetlisiniz.">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
    
    <!-- Phosphor Icons -->
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    
    <!-- Swiper CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />
    
    <!-- AOS CSS -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Montserrat', 'sans-serif'],
                        serif: ['"Playfair Display"', 'serif'],
                    },
                    colors: {
                        brand: {
                            light: '#FFFFFF',
                            surface: '#0A0A0A',
                            accent: '#FF1493', /* Deep Pink for Kokos */
                            accentDark: '#C71585', /* Medium Violet Red */
                            primary: '#141414',
                            dark: '#000000',
                            gray: '#A0A0A0'
                        }
                    },
                    boxShadow: {
                        'glow': '0 0 30px rgba(255, 20, 147, 0.25)',
                        'glow-strong': '0 0 40px rgba(255, 20, 147, 0.5)',
                    }
                }
            }
        }
    </script>

    <style>
        body {
            background-color: theme('colors.brand.surface');
            color: theme('colors.brand.light');
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        ::selection {
            background: theme('colors.brand.accent');
            color: theme('colors.brand.light');
        }

        .glass-nav {
            background: rgba(10, 10, 10, 0.95);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255, 20, 147, 0.15);
        }

        .btn-primary {
            background: linear-gradient(45deg, theme('colors.brand.accent'), theme('colors.brand.accentDark'));
            color: theme('colors.brand.light');
            padding: 1rem 2.5rem;
            border-radius: 50px;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            font-size: 0.85rem;
            transition: all 0.4s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            border: none;
            box-shadow: theme('boxShadow.glow');
        }
        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: theme('boxShadow.glow-strong');
        }

        .btn-outline {
            border: 2px solid theme('colors.brand.accent');
            color: theme('colors.brand.accent');
            padding: 1rem 2.5rem;
            border-radius: 50px;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            font-size: 0.85rem;
            transition: all 0.4s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }
        .btn-outline:hover {
            background-color: theme('colors.brand.accent');
            color: theme('colors.brand.light');
            box-shadow: theme('boxShadow.glow');
        }

        .hero-swiper .swiper-slide .hero-bg {
            transform: scale(1.15);
            transition: transform 10s ease-out;
        }
        .hero-swiper .swiper-slide-active .hero-bg {
            transform: scale(1);
        }
        .hero-text {
            opacity: 0;
            transform: translateY(30px);
            transition: all 1s ease;
            transition-delay: 0.5s;
        }
        .hero-swiper .swiper-slide-active .hero-text {
            opacity: 1;
            transform: translateY(0);
        }

        @keyframes pulse-wa {
            0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.6); }
            70% { box-shadow: 0 0 0 25px rgba(37, 211, 102, 0); }
            100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }

        .pink-gradient-text {
            background: linear-gradient(to right, #FF1493, #FF69B4, #C71585, #FF1493);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-size: 200% auto;
            animation: gradient-shift 3s linear infinite;
        }
        
        @keyframes gradient-shift {
            0% { background-position: 0% center; }
            100% { background-position: 200% center; }
        }

        .service-card {
            border: 1px solid rgba(255, 20, 147, 0.1);
            background: theme('colors.brand.primary');
            border-radius: 20px;
            transition: all 0.5s ease;
            overflow: hidden;
        }
        .service-card:hover {
            border-color: theme('colors.brand.accent');
            transform: translateY(-10px);
            box-shadow: theme('boxShadow.glow');
        }
        
        .img-overlay::after {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(90deg, rgba(10,10,10,0.9) 0%, rgba(10,10,10,0.4) 50%, rgba(10,10,10,0.1) 100%);
        }
    </style>
</head>
<body class="antialiased">

    <!-- 1. TOP BAR -->
    <div class="bg-brand-accent text-white w-full py-2 px-4 z-50 relative hidden lg:block text-xs uppercase tracking-[0.2em] font-bold">
        <div class="max-w-[1400px] mx-auto flex justify-between items-center">
            <div class="flex items-center gap-6">
                <span class="flex items-center gap-2"><i class="ph-bold ph-star"></i> Bir Kuaför Salonundan Daha Fazlası</span>
                <span class="flex items-center gap-2"><i class="ph-bold ph-check-circle"></i> Sivas'ın En İddialı Renklendirme Merkezi</span>
            </div>
            <div class="flex items-center gap-6">
                <a href="tel:+903462218714" class="hover:text-black transition-colors flex items-center gap-2"><i class="ph-bold ph-phone"></i> 0346 221 87 14</a>
                <a href="https://wa.me/903462218714" class="text-black font-black hover:text-white transition-colors bg-white/20 px-3 py-1 rounded-full">Randevu Sistemi Mevcuttur</a>
            </div>
        </div>
    </div>

    <!-- 2. NAVBAR -->
    <nav class="glass-nav fixed w-full z-40 transition-all duration-500" id="navbar">
        <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-24">
                
                <a href="#" class="flex flex-col items-center">
                    <span class="font-serif font-black text-4xl tracking-widest text-white leading-none flex items-center gap-2">
                        <i class="ph-fill ph-scissors text-brand-accent text-3xl"></i> KoKoŞ
                    </span>
                    <span class="text-[10px] tracking-[0.5em] uppercase text-brand-accent mt-2 font-bold">Saç Tasarım</span>
                </a>

                <div class="hidden lg:flex items-center space-x-8">
                    <a href="#hakkimizda" class="text-xs font-bold uppercase tracking-[0.2em] text-white hover:text-brand-accent transition-colors">Hakkımızda</a>
                    <a href="#renklendirme" class="text-xs font-bold uppercase tracking-[0.2em] text-white hover:text-brand-accent transition-colors">Renkler</a>
                    <a href="#gelin" class="text-xs font-bold uppercase tracking-[0.2em] text-brand-accent border-b-2 border-brand-accent pb-1">KoKoŞ Gelinleri</a>
                    <a href="#hizmetler" class="text-xs font-bold uppercase tracking-[0.2em] text-white hover:text-brand-accent transition-colors">Hizmetler</a>
                    <a href="#iletisim" class="text-xs font-bold uppercase tracking-[0.2em] text-white hover:text-brand-accent transition-colors">İletişim</a>
                </div>

                <div class="hidden lg:flex items-center gap-4">
                    <a href="https://wa.me/903462218714" class="btn-primary"><i class="ph-bold ph-whatsapp-logo text-xl"></i> Randevu Al</a>
                </div>

                <div class="lg:hidden flex items-center">
                    <button id="mobile-menu-btn" class="text-brand-accent">
                        <i class="ph-light ph-list text-4xl"></i>
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <!-- 3. MEGA HERO SLIDER -->
    <section class="relative h-screen w-full overflow-hidden">
        <div class="swiper hero-swiper h-full w-full">
            <div class="swiper-wrapper h-full w-full">
                
                <!-- Slide 1: Renkler -->
                <div class="swiper-slide relative h-full w-full flex items-center">
                    <div class="absolute inset-0 w-full h-full hero-bg img-overlay">
                        <!-- High quality blonde hair coloring image -->
                        <img src="https://images.unsplash.com/photo-1595476108010-b4d1f10d5e43?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" alt="Saç Renklendirme" class="w-full h-full object-cover">
                    </div>
                    <div class="relative z-10 max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 w-full pt-20 hero-text">
                        <span class="text-brand-accent text-sm font-bold uppercase tracking-[0.4em] mb-4 block">Kusursuz Renkler</span>
                        <h1 class="text-6xl md:text-8xl font-serif text-white max-w-4xl leading-[1.1] mb-6">
                            Hayalinizdeki Saca <br><span class="pink-gradient-text">Kavuşun.</span>
                        </h1>
                        <p class="text-xl text-brand-gray max-w-2xl mb-10 font-light leading-relaxed">
                            Ombre, sombre, röfle ve pigmentasyon işlemlerinde Sivas'ın en çok tercih edilen markası. Saçlarınızı riske atmayın, profesyonellere bırakın.
                        </p>
                        <div class="flex flex-wrap gap-4">
                            <a href="#renklendirme" class="btn-primary">Uygulamaları Gör</a>
                            <a href="https://wa.me/903462218714" class="btn-outline">Fiyat Bilgisi Al</a>
                        </div>
                    </div>
                </div>

                <!-- Slide 2: Bridal -->
                <div class="swiper-slide relative h-full w-full flex items-center">
                    <div class="absolute inset-0 w-full h-full hero-bg img-overlay">
                        <!-- Bridal hair image -->
                        <img src="https://images.unsplash.com/photo-1511289081-d06dda19034d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" alt="KoKoŞ Gelinleri" class="w-full h-full object-cover">
                    </div>
                    <div class="relative z-10 max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 w-full pt-20 hero-text">
                        <span class="text-brand-accent text-sm font-bold uppercase tracking-[0.4em] mb-4 block">KoKoŞ Gelinleri</span>
                        <h1 class="text-6xl md:text-8xl font-serif text-white max-w-4xl leading-[1.1] mb-6">
                            En Özel Gününüzde <br><span class="pink-gradient-text">Yıldız Olun.</span>
                        </h1>
                        <p class="text-xl text-brand-gray max-w-2xl mb-10 font-light leading-relaxed">
                            Porselen makyaj ve eşsiz gelin saçı tasarımlarıyla düğün gününüzde tüm gözler üzerinizde olsun. Erken rezervasyon fırsatlarını kaçırmayın.
                        </p>
                        <div class="flex flex-wrap gap-4">
                            <a href="#gelin" class="btn-primary">Gelin Paketleri</a>
                        </div>
                    </div>
                </div>

                <!-- Slide 3: Haircut -->
                <div class="swiper-slide relative h-full w-full flex items-center">
                    <div class="absolute inset-0 w-full h-full hero-bg img-overlay">
                        <!-- Haircut / styling image -->
                        <img src="https://images.unsplash.com/photo-1560066984-138dadb4c035?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" alt="Trend Kesimler" class="w-full h-full object-cover">
                    </div>
                    <div class="relative z-10 max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 w-full pt-20 hero-text">
                        <span class="text-brand-accent text-sm font-bold uppercase tracking-[0.4em] mb-4 block">Yüz Tipinize Uygun</span>
                        <h1 class="text-6xl md:text-8xl font-serif text-white max-w-4xl leading-[1.1] mb-6">
                            Trend ve Modern <br><span class="pink-gradient-text">Kesimler.</span>
                        </h1>
                        <p class="text-xl text-brand-gray max-w-2xl mb-10 font-light leading-relaxed">
                            Klasik çizgilerden sıkılanlar için modern, dinamik ve yüz hatlarınızı ön plana çıkaran profesyonel saç kesimi ve şekillendirme.
                        </p>
                        <div class="flex flex-wrap gap-4">
                            <a href="https://wa.me/903462218714" class="btn-primary">Randevu Al</a>
                        </div>
                    </div>
                </div>

            </div>
            
            <!-- Navigation Elements -->
            <div class="absolute bottom-10 right-10 z-20 flex gap-4 hidden md:flex">
                <button class="hero-prev w-14 h-14 rounded-full border border-white/20 flex items-center justify-center text-white hover:bg-brand-accent hover:border-brand-accent transition-all">
                    <i class="ph-bold ph-arrow-left text-xl"></i>
                </button>
                <button class="hero-next w-14 h-14 rounded-full border border-white/20 flex items-center justify-center text-white hover:bg-brand-accent hover:border-brand-accent transition-all">
                    <i class="ph-bold ph-arrow-right text-xl"></i>
                </button>
            </div>
            
            <div class="absolute bottom-10 left-10 z-20 hidden md:block">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-[1px] bg-brand-accent"></div>
                    <span class="text-white text-sm font-bold tracking-widest uppercase">Kaydırın</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. ABOUT SECTION -->
    <section id="hakkimizda" class="py-32 relative overflow-hidden bg-brand-surface">
        <div class="absolute top-0 right-0 w-[800px] h-[800px] bg-brand-accent/5 rounded-full blur-[120px] -translate-y-1/2 translate-x-1/2"></div>
        
        <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-20 items-center">
                
                <!-- Left Image Grid -->
                <div class="relative h-[600px] rounded-3xl overflow-hidden" data-aos="fade-right">
                    <div class="absolute inset-0 bg-gradient-to-t from-brand-surface via-transparent to-transparent z-10"></div>
                    <img src="https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Kuaför Salonu" class="w-full h-full object-cover">
                    
                    <div class="absolute bottom-10 left-10 z-20 bg-brand-primary/90 backdrop-blur-md p-8 rounded-2xl border border-white/10 max-w-sm">
                        <div class="flex items-center gap-4 mb-4">
                            <i class="ph-fill ph-quotes text-4xl text-brand-accent"></i>
                        </div>
                        <p class="text-white font-serif text-xl italic mb-4">"Bir kuaför salonundan daha fazlası; burası sizin parladığınız sahne."</p>
                        <p class="text-brand-accent font-bold tracking-widest uppercase text-xs">- KOKOŞ Ekibi</p>
                    </div>
                </div>

                <!-- Right Content -->
                <div data-aos="fade-left">
                    <span class="text-brand-accent font-bold tracking-[0.3em] uppercase text-sm flex items-center gap-4 mb-6">
                        <div class="w-8 h-[2px] bg-brand-accent"></div>
                        Hakkımızda
                    </span>
                    <h2 class="text-4xl md:text-5xl font-serif text-white mb-8 leading-tight">
                        Güzelliğe Giden Yolda <br>En Doğru Adresiniz.
                    </h2>
                    <p class="text-brand-gray text-lg mb-6 leading-relaxed">
                        KoKoŞ Saç Tasarım olarak Sivas'ta yıllardır kalite, güven ve %100 müşteri memnuniyeti felsefesiyle hizmet veriyoruz. Modern dünyanın saç trendlerini yakından takip ediyor, birinci sınıf kaliteli ürünler kullanarak saç sağlığınızı koruyoruz.
                    </p>
                    <p class="text-brand-gray text-lg mb-10 leading-relaxed">
                        Uzman kadromuz; kusursuz renklendirmeler, yüz hatlarınıza en uygun saç kesimleri, kaş alımı ve en özel günleriniz için profesyonel gelin saçı & porselen makyaj hizmetleriyle sizi bekliyor.
                    </p>
                    
                    <div class="grid grid-cols-2 gap-8 mb-12">
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-full bg-brand-accent/20 flex items-center justify-center flex-shrink-0">
                                <i class="ph-bold ph-star text-brand-accent text-2xl"></i>
                            </div>
                            <div>
                                <h4 class="text-white font-bold mb-2">Uzman Kadro</h4>
                                <p class="text-sm text-brand-gray">Sürekli eğitime önem veren profesyonel ekip.</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-full bg-brand-accent/20 flex items-center justify-center flex-shrink-0">
                                <i class="ph-bold ph-shield-check text-brand-accent text-2xl"></i>
                            </div>
                            <div>
                                <h4 class="text-white font-bold mb-2">Kaliteli Ürünler</h4>
                                <p class="text-sm text-brand-gray">Saçınızı yıpratmayan dünya markaları.</p>
                            </div>
                        </div>
                    </div>
                    
                    <a href="#iletisim" class="btn-primary">Bizi Ziyaret Edin</a>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. SERVICES / HİZMETLER -->
    <section id="hizmetler" class="py-32 bg-brand-primary border-y border-white/5 relative">
        <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-20" data-aos="fade-up">
                <span class="text-brand-accent font-bold tracking-[0.3em] uppercase text-sm mb-4 block">Hizmetlerimiz</span>
                <h2 class="text-4xl md:text-6xl font-serif text-white mb-6">Size Özel Dokunuşlar</h2>
                <p class="text-brand-gray text-lg">Güzelliğinizi ön plana çıkaracak geniş hizmet yelpazemiz.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                
                <!-- Service 1 -->
                <div class="service-card group cursor-pointer" data-aos="fade-up" data-aos-delay="100">
                    <div class="h-64 overflow-hidden relative">
                        <div class="absolute inset-0 bg-brand-surface/40 group-hover:bg-transparent transition-colors z-10"></div>
                        <img src="https://images.unsplash.com/photo-1595476108010-b4d1f10d5e43?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Renklendirme" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="p-8">
                        <div class="w-14 h-14 rounded-full bg-brand-surface flex items-center justify-center mb-6 -mt-14 relative z-20 border border-brand-accent/30">
                            <i class="ph-bold ph-palette text-brand-accent text-2xl"></i>
                        </div>
                        <h3 class="text-2xl font-serif text-white mb-4">Saç Renklendirme</h3>
                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">
                            Ombre, sombre, röfle, balyaj ve dip boya işlemleri. Saçınıza zarar vermeden istediğiniz tona ulaşıyoruz.
                        </p>
                        <span class="text-brand-accent text-sm font-bold uppercase tracking-widest flex items-center gap-2 group-hover:gap-4 transition-all">
                            Detaylı Bilgi <i class="ph-bold ph-arrow-right"></i>
                        </span>
                    </div>
                </div>

                <!-- Service 2 -->
                <div class="service-card group cursor-pointer" data-aos="fade-up" data-aos-delay="200">
                    <div class="h-64 overflow-hidden relative">
                        <div class="absolute inset-0 bg-brand-surface/40 group-hover:bg-transparent transition-colors z-10"></div>
                        <img src="https://images.unsplash.com/photo-1560066984-138dadb4c035?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Kesim" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="p-8">
                        <div class="w-14 h-14 rounded-full bg-brand-surface flex items-center justify-center mb-6 -mt-14 relative z-20 border border-brand-accent/30">
                            <i class="ph-bold ph-scissors text-brand-accent text-2xl"></i>
                        </div>
                        <h3 class="text-2xl font-serif text-white mb-4">Kesim & Şekillendirme</h3>
                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">
                            Modern saç kesimleri, kırık alma, fön, maşa ve kalıcı şekillendirme (perma) hizmetleri.
                        </p>
                        <span class="text-brand-accent text-sm font-bold uppercase tracking-widest flex items-center gap-2 group-hover:gap-4 transition-all">
                            Detaylı Bilgi <i class="ph-bold ph-arrow-right"></i>
                        </span>
                    </div>
                </div>

                <!-- Service 3 -->
                <div class="service-card group cursor-pointer" data-aos="fade-up" data-aos-delay="300">
                    <div class="h-64 overflow-hidden relative">
                        <div class="absolute inset-0 bg-brand-surface/40 group-hover:bg-transparent transition-colors z-10"></div>
                        <img src="https://images.unsplash.com/photo-1511289081-d06dda19034d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Gelin Başı" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="p-8">
                        <div class="w-14 h-14 rounded-full bg-brand-surface flex items-center justify-center mb-6 -mt-14 relative z-20 border border-brand-accent/30">
                            <i class="ph-bold ph-crown text-brand-accent text-2xl"></i>
                        </div>
                        <h3 class="text-2xl font-serif text-white mb-4">Gelin Paketleri</h3>
                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">
                            KoKoŞ Gelinleri için özel saç tasarımı, porselen makyaj ve düğün öncesi cilt / saç bakımı.
                        </p>
                        <span class="text-brand-accent text-sm font-bold uppercase tracking-widest flex items-center gap-2 group-hover:gap-4 transition-all">
                            Detaylı Bilgi <i class="ph-bold ph-arrow-right"></i>
                        </span>
                    </div>
                </div>

                <!-- Service 4 -->
                <div class="service-card group cursor-pointer" data-aos="fade-up" data-aos-delay="400">
                    <div class="h-64 overflow-hidden relative">
                        <div class="absolute inset-0 bg-brand-surface/40 group-hover:bg-transparent transition-colors z-10"></div>
                        <img src="https://images.unsplash.com/photo-1512412046876-f386342eddb3?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Makyaj & Kaş" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="p-8">
                        <div class="w-14 h-14 rounded-full bg-brand-surface flex items-center justify-center mb-6 -mt-14 relative z-20 border border-brand-accent/30">
                            <i class="ph-bold ph-eye text-brand-accent text-2xl"></i>
                        </div>
                        <h3 class="text-2xl font-serif text-white mb-4">Kaş & Makyaj</h3>
                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">
                            Profesyonel kaş alımı, kaş tasarımı, günlük ve gece makyajı uygulamaları.
                        </p>
                        <span class="text-brand-accent text-sm font-bold uppercase tracking-widest flex items-center gap-2 group-hover:gap-4 transition-all">
                            Detaylı Bilgi <i class="ph-bold ph-arrow-right"></i>
                        </span>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- 6. KOKOŞ GELİNLERİ HIGHLIGHT -->
    <section id="gelin" class="py-32 bg-brand-surface relative overflow-hidden">
        <div class="absolute top-1/2 left-0 w-[500px] h-[500px] bg-brand-accent/10 rounded-full blur-[100px] -translate-y-1/2 -translate-x-1/2"></div>
        
        <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="bg-brand-primary rounded-[3rem] border border-brand-accent/20 overflow-hidden flex flex-col lg:flex-row items-stretch">
                
                <div class="w-full lg:w-1/2 p-12 lg:p-20 flex flex-col justify-center">
                    <span class="text-brand-accent font-bold tracking-[0.3em] uppercase text-sm mb-6 flex items-center gap-4">
                        <i class="ph-fill ph-crown text-2xl"></i> Özel Paket
                    </span>
                    <h2 class="text-4xl md:text-5xl font-serif text-white mb-8">
                        <span class="pink-gradient-text">KoKoŞ Gelinleri</span> <br>Fark Yaratır.
                    </h2>
                    <p class="text-brand-gray text-lg mb-8 leading-relaxed">
                        Hayatınızın en anlamlı gününde şansa yer bırakmayın. Profesyonel porselen makyaj, prova seansları ve gün boyu bozulmayan kusursuz gelin saçı tasarımıyla rüya gibi bir görünüme kavuşun.
                    </p>
                    <ul class="space-y-4 mb-12">
                        <li class="flex items-center gap-3 text-white"><i class="ph-bold ph-check text-brand-accent text-xl"></i> Saç & Makyaj Provası</li>
                        <li class="flex items-center gap-3 text-white"><i class="ph-bold ph-check text-brand-accent text-xl"></i> Profesyonel Porselen Makyaj</li>
                        <li class="flex items-center gap-3 text-white"><i class="ph-bold ph-check text-brand-accent text-xl"></i> Kullanılan Premium Markalar (MAC, NARS, vb.)</li>
                        <li class="flex items-center gap-3 text-white"><i class="ph-bold ph-check text-brand-accent text-xl"></i> Nedime Paketleri</li>
                    </ul>
                    <div>
                        <a href="https://wa.me/903462218714" class="btn-primary"><i class="ph-bold ph-calendar-plus text-xl"></i> Rezervasyon Yap</a>
                    </div>
                </div>

                <div class="w-full lg:w-1/2 relative min-h-[400px] lg:min-h-full">
                    <img src="https://images.unsplash.com/photo-1541216970279-affbfdd55aa8?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Gelin Makyajı" class="absolute inset-0 w-full h-full object-cover">
                    <div class="absolute inset-0 bg-gradient-to-r from-brand-primary to-transparent hidden lg:block"></div>
                    <div class="absolute inset-0 bg-gradient-to-t from-brand-primary to-transparent lg:hidden block"></div>
                </div>
                
            </div>
        </div>
    </section>

    <!-- 7. INSTAGRAM GALLERY -->
    <section class="py-24 bg-brand-primary border-t border-white/5 relative">
        <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 mb-16 text-center">
            <i class="ph-fill ph-instagram-logo text-5xl text-brand-accent mb-4"></i>
            <h2 class="text-3xl md:text-5xl font-serif text-white mb-4">@kokossivas</h2>
            <p class="text-brand-gray text-lg">Bizi Instagram'da takip edin, son trendleri kaçırmayın.</p>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-1 md:gap-4 px-1 md:px-4">
            <!-- Grid images -->
            <a href="https://instagram.com/kokossivas" target="_blank" class="group relative aspect-square overflow-hidden rounded-xl">
                <img src="https://images.unsplash.com/photo-1595476108010-b4d1f10d5e43?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Instagram Post" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                    <i class="ph-bold ph-heart text-4xl text-white"></i>
                </div>
            </a>
            <a href="https://instagram.com/kokossivas" target="_blank" class="group relative aspect-square overflow-hidden rounded-xl">
                <img src="https://images.unsplash.com/photo-1522337660859-02fbefca4702?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Instagram Post" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                    <i class="ph-bold ph-heart text-4xl text-white"></i>
                </div>
            </a>
            <a href="https://instagram.com/kokossivas" target="_blank" class="group relative aspect-square overflow-hidden rounded-xl">
                <img src="https://images.unsplash.com/photo-1620916297397-a4a5402a3c6c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Instagram Post" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                    <i class="ph-bold ph-heart text-4xl text-white"></i>
                </div>
            </a>
            <a href="https://instagram.com/kokossivas" target="_blank" class="group relative aspect-square overflow-hidden rounded-xl">
                <img src="https://images.unsplash.com/photo-1519014816548-bf5fe059e98b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Instagram Post" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                    <i class="ph-bold ph-heart text-4xl text-white"></i>
                </div>
            </a>
        </div>
        
        <div class="text-center mt-12">
            <a href="https://instagram.com/kokossivas" target="_blank" class="btn-outline">Instagram'da Gör</a>
        </div>
    </section>

    <!-- 8. FOOTER & CONTACT -->
    <footer id="iletisim" class="bg-brand-surface pt-24 pb-10 border-t border-brand-accent/20 relative">
        <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
                
                <div class="lg:col-span-1">
                    <a href="#" class="inline-block mb-6">
                        <span class="font-serif font-black text-4xl tracking-widest text-white leading-none flex items-center gap-2">
                            <i class="ph-fill ph-scissors text-brand-accent"></i> KoKoŞ
                        </span>
                        <span class="text-[10px] tracking-[0.5em] uppercase text-brand-accent mt-2 font-bold block">Saç Tasarım</span>
                    </a>
                    <p class="text-brand-gray text-sm leading-relaxed mb-6">
                        Sivas'ın en iddialı ve modern kuaför salonu. Renklendirme, kesim ve gelin başı için bir numaralı adresiniz.
                    </p>
                    <div class="flex gap-4">
                        <a href="https://instagram.com/kokossivas" class="w-10 h-10 rounded-full bg-brand-primary flex items-center justify-center text-white hover:bg-brand-accent transition-colors">
                            <i class="ph-fill ph-instagram-logo text-xl"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-full bg-brand-primary flex items-center justify-center text-white hover:bg-brand-accent transition-colors">
                            <i class="ph-fill ph-facebook-logo text-xl"></i>
                        </a>
                    </div>
                </div>

                <div>
                    <h4 class="text-white font-bold uppercase tracking-widest mb-6">Hızlı Menü</h4>
                    <ul class="space-y-4">
                        <li><a href="#hakkimizda" class="text-brand-gray hover:text-brand-accent transition-colors">Hakkımızda</a></li>
                        <li><a href="#hizmetler" class="text-brand-gray hover:text-brand-accent transition-colors">Hizmetlerimiz</a></li>
                        <li><a href="#gelin" class="text-brand-gray hover:text-brand-accent transition-colors">Gelin Paketleri</a></li>
                        <li><a href="#iletisim" class="text-brand-gray hover:text-brand-accent transition-colors">İletişim & Randevu</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-white font-bold uppercase tracking-widest mb-6">İletişim</h4>
                    <ul class="space-y-6">
                        <li class="flex items-start gap-4">
                            <i class="ph-fill ph-map-pin text-brand-accent text-2xl mt-1"></i>
                            <span class="text-brand-gray leading-relaxed">Sivas Merkez,<br>Sivas, Türkiye</span>
                        </li>
                        <li class="flex items-center gap-4">
                            <i class="ph-fill ph-phone-call text-brand-accent text-2xl"></i>
                            <a href="tel:+903462218714" class="text-white hover:text-brand-accent transition-colors text-lg font-bold">0346 221 87 14</a>
                        </li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-white font-bold uppercase tracking-widest mb-6">Çalışma Saatleri</h4>
                    <ul class="space-y-4">
                        <li class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-brand-gray">Pzt - Cmt</span>
                            <span class="text-white font-bold">09:00 - 19:30</span>
                        </li>
                        <li class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-brand-gray">Pazar</span>
                            <span class="text-brand-accent font-bold">Kapalı</span>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="border-t border-white/5 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
                <p class="text-brand-gray text-sm text-center md:text-left">
                    &copy; 2026 KoKoŞ Saç Tasarım. Tüm hakları saklıdır.
                </p>
                <div class="text-brand-gray text-sm">
                    Design by <span class="text-brand-accent font-bold">Advanced AI</span>
                </div>
            </div>
        </div>
    </footer>

    <!-- Fixed WhatsApp Button -->
    <a href="https://wa.me/903462218714" target="_blank" class="fixed bottom-8 left-8 z-50 bg-[#25D366] text-white p-4 rounded-full flex items-center justify-center hover:scale-110 transition-transform duration-300" style="animation: pulse-wa 2s infinite;">
        <i class="ph-fill ph-whatsapp-logo text-4xl"></i>
    </a>

    <!-- Scroll to Top -->
    <button id="scrollToTop" class="fixed bottom-8 right-8 z-50 bg-brand-primary text-brand-accent border border-brand-accent/20 p-4 rounded-full flex items-center justify-center hover:bg-brand-accent hover:text-white transition-all duration-300 opacity-0 invisible translate-y-4">
        <i class="ph-bold ph-caret-up text-2xl"></i>
    </button>

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css"></script>
    <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    
    <script>
        // Initialize AOS
        AOS.init({
            duration: 1000,
            once: true,
            offset: 50,
        });

        // Initialize Swiper
        const heroSwiper = new Swiper('.hero-swiper', {
            loop: true,
            effect: 'fade',
            speed: 1500,
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
            navigation: {
                nextEl: '.hero-next',
                prevEl: '.hero-prev',
            },
        });

        // Navbar & Scroll to Top
        const navbar = document.getElementById('navbar');
        const scrollToTopBtn = document.getElementById('scrollToTop');
        
        window.addEventListener('scroll', () => {
            if (window.scrollY > 40) {
                navbar.style.background = 'rgba(10, 10, 10, 0.98)';
                navbar.classList.add('shadow-2xl', 'top-0');
            } else {
                navbar.style.background = 'rgba(10, 10, 10, 0.95)';
                navbar.classList.remove('shadow-2xl', 'top-0');
            }
            
            if (window.scrollY > 500) {
                scrollToTopBtn.classList.remove('opacity-0', 'invisible', 'translate-y-4');
                scrollToTopBtn.classList.add('opacity-100', 'visible', 'translate-y-0');
            } else {
                scrollToTopBtn.classList.add('opacity-0', 'invisible', 'translate-y-4');
                scrollToTopBtn.classList.remove('opacity-100', 'visible', 'translate-y-0');
            }
        });

        scrollToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    </script>
</body>
</html>
"""

with open("kokos_demo.html", "w", encoding="utf-8") as f:
    f.write(html_content)
