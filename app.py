import os
from PIL import Image, ImageDraw, ImageFont

def create_brand_assets():
    # Brand Colors
    GOLD = (212, 175, 55)        # Metallic Gold #D4AF37
    OBSIDIAN = (15, 15, 15)      # Obsidian Black #0F0F0F
    WHITE = (255, 255, 255)      # Pure White
    DARK_CARD = (25, 25, 25)     # Dark Gray Card #191919

    output_dir = "brand_assets"
    os.makedirs(output_dir, exist_ok=True)

    # -------------------------------------------------------------
    # 1. SQUARE LOGO / PROFILE ICON (1000x1000 px)
    # -------------------------------------------------------------
    logo_size = 1000
    logo_img = Image.new("RGB", (logo_size, logo_size), OBSIDIAN)
    draw = ImageDraw.Draw(logo_img)

    # Draw Outer Metallic Gold Circular Ring
    margin = 80
    ring_width = 16
    draw.ellipse(
        [margin, margin, logo_size - margin, logo_size - margin],
        outline=GOLD,
        width=ring_width
    )

    # Draw Central Monogram Box / Accent
    center_box = [300, 300, 700, 700]
    draw.rectangle(center_box, outline=GOLD, width=8)

    # Add Brand Monogram Text "FD" & Agency Name
    try:
        font_large = ImageFont.truetype("arial.ttf", 220)
        font_small = ImageFont.truetype("arial.ttf", 48)
    except IOError:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Draw Monogram
    draw.text((370, 350), "FD", fill=GOLD, font=font_large)
    
    # Draw Brand Title Below Box
    draw.text((320, 750), "FAFI DIGITALS", fill=WHITE, font=font_small)

    logo_path = os.path.join(output_dir, "fafi_digitals_logo.png")
    logo_img.save(logo_path)
    print(f"✅ Logo generated: {logo_path}")

    # -------------------------------------------------------------
    # 2. TELEGRAM / SOCIAL MEDIA HEADER BANNER (1200x630 px)
    # -------------------------------------------------------------
    banner_w, banner_h = 1200, 630
    banner_img = Image.new("RGB", (banner_w, banner_h), OBSIDIAN)
    draw_b = ImageDraw.Draw(banner_img)

    # Left Decorative Gold Border Line
    draw_b.rectangle([0, 0, 20, banner_h], fill=GOLD)

    # Header Card Box
    draw_b.rectangle([60, 60, banner_w - 60, banner_h - 60], fill=DARK_CARD, outline=GOLD, width=3)

    try:
        font_title = ImageFont.truetype("arial.ttf", 72)
        font_sub = ImageFont.truetype("arial.ttf", 36)
        font_contact = ImageFont.truetype("arial.ttf", 32)
    except IOError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_contact = ImageFont.load_default()

    # Banner Content
    draw_b.text((100, 120), "FAFI DIGITALS", fill=GOLD, font=font_title)
    draw_b.text((100, 220), "AfriMarketing AI & Digital Growth Suite", fill=WHITE, font=font_sub)
    draw_b.text((100, 300), "• Visual Branding  • Copywriting  • Social Media Strategy", fill=(200, 200, 200), font=font_contact)

    # Contact Info Bar
    draw_b.line([(100, 420), (1100, 420)], fill=GOLD, width=2)
    draw_b.text((100, 460), "📍 Addis Ababa, Ethiopia   |   📞 0901183481   |   📲 @FAFIdigitals", fill=GOLD, font=font_contact)

    banner_path = os.path.join(output_dir, "fafi_digitals_banner.png")
    banner_img.save(banner_path)
    print(f"✅ Social Banner generated: {banner_path}")

    # -------------------------------------------------------------
    # 3. PROMOTIONAL WATERMARK / BADGE (800x200 px)
    # -------------------------------------------------------------
    badge_w, badge_h = 800, 200
    badge_img = Image.new("RGBA", (badge_w, badge_h), (15, 15, 15, 230))
    draw_bg = ImageDraw.Draw(badge_img)

    # Gold Accent Line
    draw_bg.rectangle([0, 0, badge_w, 8], fill=GOLD)
    draw_bg.rectangle([0, badge_h - 8, badge_w, badge_h], fill=GOLD)

    try:
        font_badge = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font_badge = ImageFont.load_default()

    draw_bg.text((40, 70), "POWERED BY FAFI DIGITALS", fill=GOLD, font=font_badge)

    badge_path = os.path.join(output_dir, "fafi_watermark_badge.png")
    badge_img.save(badge_path)
    print(f"✅ Watermark Badge generated: {badge_path}")

if __name__ == "__main__":
    create_brand_assets()
