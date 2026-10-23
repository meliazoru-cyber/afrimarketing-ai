import os
from PIL import Image, ImageDraw, ImageFont

def create_full_brand_suite():
    # FAFI Digitals Brand Palette
    GOLD = (212, 175, 55)         # Metallic Gold (#D4AF37)
    OBSIDIAN = (15, 15, 15)       # Obsidian Black (#0F0F0F)
    WHITE = (255, 255, 255)       # Bright White
    DARK_CARD = (25, 25, 25)      # High-Contrast Card Fill (#191919)
    ACCENT_GRAY = (180, 180, 180) # Subtitle Gray

    output_dir = "brand_assets"
    os.makedirs(output_dir, exist_ok=True)

    # Helper function to safely load fonts
    def get_font(size):
        try:
            return ImageFont.truetype("arial.ttf", size)
        except IOError:
            return ImageFont.load_default()

    # -------------------------------------------------------------
    # 1. SQUARE LOGO / AVATAR (1000x1000 px)
    # -------------------------------------------------------------
    logo_size = 1000
    logo_img = Image.new("RGB", (logo_size, logo_size), OBSIDIAN)
    draw = ImageDraw.Draw(logo_img)

    # Outer Metallic Gold Ring & Inner Monogram Box
    draw.ellipse([80, 80, 920, 920], outline=GOLD, width=16)
    draw.rectangle([280, 280, 720, 720], fill=DARK_CARD, outline=GOLD, width=8)

    # Text Elements
    draw.text((370, 340), "FD", fill=GOLD, font=get_font(210))
    draw.text((310, 760), "FAFI DIGITALS", fill=WHITE, font=get_font(48))
    draw.text((365, 825), "ADDIS ABABA", fill=GOLD, font=get_font(30))

    logo_path = os.path.join(output_dir, "01_fafi_digitals_logo.png")
    logo_img.save(logo_path)
    print(f"✅ Logo generated: {logo_path}")

    # -------------------------------------------------------------
    # 2. TELEGRAM & SOCIAL HEADER BANNER (1200x630 px)
    # -------------------------------------------------------------
    banner_w, banner_h = 1200, 630
    banner_img = Image.new("RGB", (banner_w, banner_h), OBSIDIAN)
    draw_b = ImageDraw.Draw(banner_img)

    # Left Gold Edge Accent & Card Frame
    draw_b.rectangle([0, 0, 24, banner_h], fill=GOLD)
    draw_b.rectangle([60, 50, banner_w - 60, banner_h - 50], fill=DARK_CARD, outline=GOLD, width=3)

    # Banner Copy
    draw_b.text((100, 110), "FAFI DIGITALS", fill=GOLD, font=get_font(68))
    draw_b.text((100, 200), "AfriMarketing AI & Digital Growth Suite", fill=WHITE, font=get_font(36))
    draw_b.text((100, 275), "• Visual Branding  • AI Copywriting  • Campaign Strategy", fill=ACCENT_GRAY, font=get_font(30))

    draw_b.line([(100, 390), (1100, 390)], fill=GOLD, width=2)
    draw_b.text((100, 430), "📍 Addis Ababa, Ethiopia   |   📞 0901183481   |   📲 @FAFIdigitals", fill=GOLD, font=get_font(28))

    banner_path = os.path.join(output_dir, "02_fafi_digitals_banner.png")
    banner_img.save(banner_path)
    print(f"✅ Social Banner generated: {banner_path}")

    # -------------------------------------------------------------
    # 3. PROMOTIONAL CAROUSEL POST CARD (1080x1080 px)
    # -------------------------------------------------------------
    post_s = 1080
    post_img = Image.new("RGB", (post_s, post_s), OBSIDIAN)
    draw_p = ImageDraw.Draw(post_img)

    # Header Ribbon
    draw_p.rectangle([80, 80, post_s - 80, 180], fill=GOLD)
    draw_p.text((110, 105), "POWERED BY AFRIMARKETING AI", fill=OBSIDIAN, font=get_font(36))

    # Main Card Box
    draw_p.rectangle([80, 220, post_s - 80, post_s - 120], fill=DARK_CARD, outline=GOLD, width=4)
    draw_p.text((130, 280), "Grow Your Local Brand 🇪🇹", fill=GOLD, font=get_font(52))
    
    bullet_points = [
        "✔ High-Converting Amharic-English Copy",
        "✔ 15-Second Viral TikTok Scripts",
        "✔ Formatted Telegram Channel Posts",
        "✔ telebirr & Local Checkout Integration"
    ]
    
    y_pos = 380
    for point in bullet_points:
        draw_p.text((130, y_pos), point, fill=WHITE, font=get_font(32))
        y_pos += 80

    # Call to Action
    draw_p.rectangle([130, 820, post_s - 130, 900], fill=GOLD)
    draw_p.text((260, 840), "CALL NOW: 0901183481", fill=OBSIDIAN, font=get_font(38))

    post_path = os.path.join(output_dir, "03_promo_carousel_card.png")
    post_img.save(post_path)
    print(f"✅ Promo Carousel Post generated: {post_path}")

    # -------------------------------------------------------------
    # 4. DIGITAL BUSINESS CARD (1050x600 px)
    # -------------------------------------------------------------
    card_w, card_h = 1050, 600
    card_img = Image.new("RGB", (card_w, card_h), OBSIDIAN)
    draw_c = ImageDraw.Draw(card_img)

    # Metallic Gold Framing
    draw_c.rectangle([20, 20, card_w - 20, card_h - 20], outline=GOLD, width=5)
    draw_c.rectangle([50, 50, 220, 220], fill=DARK_CARD, outline=GOLD, width=4)
    draw_c.text((85, 80), "FD", fill=GOLD, font=get_font(90))

    # Name & Title
    draw_c.text((260, 65), "Fasika Demisse (Fafi)", fill=WHITE, font=get_font(44))
    draw_c.text((260, 125), "Founder & Creative Lead • FAFI Digitals", fill=GOLD, font=get_font(28))

    draw_c.line([(260, 180), (card_w - 60, 180)], fill=GOLD, width=2)

    # Contact Details
    draw_c.text((70, 260), "📱 Direct Contact: 0901183481", fill=WHITE, font=get_font(30))
    draw_c.text((70, 330), "📲 Telegram: @FAFIdigitals", fill=WHITE, font=get_font(30))
    draw_c.text((70, 400), "📍 Location: Addis Ababa, Ethiopia", fill=WHITE, font=get_font(30))
    draw_c.text((70, 470), "💳 Accepted: telebirr | CBE Birr | Cash on Delivery", fill=GOLD, font=get_font(26))

    card_path = os.path.join(output_dir, "04_digital_business_card.png")
    card_img.save(card_path)
    print(f"✅ Digital Business Card generated: {card_path}")

    # -------------------------------------------------------------
    # 5. WATERMARK / OVERLAY BADGE (800x180 px)
    # -------------------------------------------------------------
    badge_w, badge_h = 800, 180
    badge_img = Image.new("RGBA", (badge_w, badge_h), (15, 15, 15, 230))
    draw_bg = ImageDraw.Draw(badge_img)

    draw_bg.rectangle([0, 0, badge_w, 6], fill=GOLD)
    draw_bg.rectangle([0, badge_h - 6, badge_w, badge_h], fill=GOLD)
    draw_bg.text((40, 60), "FAFI DIGITALS • OFFICIAL BRAND", fill=GOLD, font=get_font(38))

    badge_path = os.path.join(output_dir, "05_fafi_watermark_badge.png")
    badge_img.save(badge_path)
    print(f"✅ Watermark Badge generated: {badge_path}")

if __name__ == "__main__":
    create_full_brand_suite()
