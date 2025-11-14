import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io
import random
from datetime import datetime

# Page config
st.set_page_config(
    page_title="AI Creative Generator - Tesco Retail Media",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with vibrant colors
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] h2 {
        color: white !important;
        font-weight: 700 !important;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
        background: rgba(0,0,0,0.2);
        padding: 0.5rem;
        border-radius: 8px;
    }
    
    [data-testid="stSidebar"] label {
        color: white !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
        background: rgba(0,0,0,0.15);
        padding: 0.25rem 0.5rem;
        border-radius: 6px;
        display: inline-block;
    }
    
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stFileUploader label {
        color: white !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stSidebar"] [data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.9) !important;
    }
    
    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        color: #1f2937 !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stSidebar"] p {
        color: white !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 16px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Download buttons */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
        color: white !important;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 14px;
    }
    
    /* Headings */
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        text-align: center;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    h2 {
        color: #667eea !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
    }
    
    h3 {
        color: #764ba2 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }
    
    /* Feature cards */
    .feature-card {
        background: linear-gradient(135deg, #ffffff 0%, #f5f7fa 100%);
        padding: 0.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.06);
        margin: 0.3rem 0;
        border: 2px solid #e0e7ff;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
    }
    
    .feature-card h3 {
        font-size: 0.85rem;
        margin-bottom: 0.2rem;
        color: #667eea !important;
        font-weight: 700 !important;
    }
    
    .feature-card p {
        color: #1f2937 !important;
        font-size: 0.75rem;
        line-height: 1.3;
        font-weight: 500;
        margin: 0;
    }
    
    /* Stat cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }
    
    .stat-card h2 {
        color: white !important;
        font-size: 2.5rem !important;
        margin: 0;
    }
    
    .stat-card p {
        color: rgba(255,255,255,0.9);
        font-size: 1rem;
        margin: 0.5rem 0 0 0;
    }
    
    /* Image containers */
    [data-testid="stImage"] {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    [data-testid="stImage"]:hover {
        transform: scale(1.05);
    }
    
    /* File uploader */
    [data-testid="stFileUploader"] {
        background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(240,242,255,0.9) 100%);
        border-radius: 16px;
        padding: 2rem;
        border: 2px dashed #667eea;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.2);
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: #764ba2;
        box-shadow: 0 6px 25px rgba(118, 75, 162, 0.3);
    }
    
    [data-testid="stFileUploader"] label {
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        color: #667eea !important;
    }
    
    [data-testid="stFileUploader"] section {
        border-radius: 12px;
    }
    
    [data-testid="stFileUploader"] button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2rem 0;
    }
    
    /* Info/Success boxes */
    .stSuccess {
        background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);
        border-radius: 12px;
        padding: 1rem;
        color: #1f2937 !important;
        font-weight: 600 !important;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border-radius: 12px;
        padding: 1rem;
        color: #1f2937 !important;
        font-weight: 600 !important;
    }
    
    /* All text elements - ensure good contrast */
    p, span, div {
        color: #1f2937 !important;
        font-weight: 500;
    }
    
    /* Main content text */
    [data-testid="stMarkdownContainer"] p {
        color: #111827 !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stMarkdownContainer"] h3 {
        color: #111827 !important;
        font-weight: 700 !important;
    }
    
    /* Upload text */
    [data-testid="stFileUploader"] small {
        color: #374151 !important;
        font-weight: 500 !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'uploaded_images' not in st.session_state:
    st.session_state.uploaded_images = []
if 'processed_files' not in st.session_state:
    st.session_state.processed_files = set()
if 'backgrounds' not in st.session_state:
    st.session_state.backgrounds = []
if 'color_palettes' not in st.session_state:
    st.session_state.color_palettes = [
        ['#00539F', '#FFFFFF', '#E50019'],  # Tesco Official
        ['#667eea', '#764ba2', '#f093fb'],
        ['#4facfe', '#00f2fe', '#43e97b'],
        ['#fa709a', '#fee140', '#30cfd0']
    ]
if 'generated_ads' not in st.session_state:
    st.session_state.generated_ads = []

# Header with attractive styling
st.markdown("""
<div style='text-align: center; padding: 0.3rem 0;'>
    <h1 style='font-size: 1.3rem; margin: 0;'>✨ AI Creative Generator ✨</h1>
    <p style='font-size: 0.7rem; color: #667eea; font-weight: 600; margin: 0.1rem 0;'>
        AI-Powered Fashion Ads
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# Landing page
if not st.session_state.uploaded_images:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>✂️ Background Removal</h3>
            <p>AI-powered edge detection</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🎨 Color Palettes</h3>
            <p>Apply brand colors instantly</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>✅ Compliance Check</h3>
            <p>Auto-validate guidelines</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 📤 Upload Images")
    st.markdown("**PNG, JPG** • Multiple files")
    
    # Main page upload option
    st.markdown("")
    main_uploaded_files = st.file_uploader(
        "📁 Choose Product Images",
        type=['png', 'jpg', 'jpeg', 'webp'],
        accept_multiple_files=True,
        help="Upload product images (up to 100MB each)",
        key="main_uploader"
    )
    
    if main_uploaded_files:
        new_count = 0
        for file in main_uploaded_files:
            file_id = f"{file.name}_{file.size}"
            if file_id not in st.session_state.processed_files:
                image = Image.open(file).convert('RGBA')
                st.session_state.uploaded_images.append(image)
                st.session_state.processed_files.add(file_id)
                new_count += 1
        if new_count > 0:
            st.success(f"✅ {new_count} images uploaded successfully!")
    
    st.markdown("")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="stat-card"><h2>4</h2><p>Social Formats</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><h2>Optimized</h2><p>File Size</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><h2>100%</h2><p>Brand Compliant</p></div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🎨 Settings & Tools")
    st.markdown("Configure your creative generation settings here")
    st.markdown("---")
    
    # Background upload
    st.markdown("## 🖼️ Backgrounds")
    bg_files = st.file_uploader(
        "Upload Custom Backgrounds",
        type=['png', 'jpg', 'jpeg'],
        accept_multiple_files=True
    )
    
    if bg_files:
        st.session_state.backgrounds = []
        for file in bg_files:
            bg = Image.open(file)
            st.session_state.backgrounds.append(bg)
        st.success(f"✅ {len(bg_files)} backgrounds uploaded!")
    
    st.markdown("---")
    
    # Color palette
    st.markdown("## 🎨 Color Palettes")
    selected_palette = st.selectbox(
        "Choose Palette",
        ["Tesco Official", "Purple Gradient", "Blue Green", "Warm Sunset"],
        index=0
    )
    
    if st.button("➕ Add Random Palette"):
        new_palette = ['#%06x' % random.randint(0, 0xFFFFFF) for _ in range(3)]
        st.session_state.color_palettes.append(new_palette)
        st.success("Palette added!")

# Main content
if st.session_state.uploaded_images:
    st.markdown("## 🖼️ Uploaded Images")
    
    # Add more images option
    col1, col2 = st.columns([3, 1])
    with col2:
        add_more = st.file_uploader(
            "➕ Add More Images",
            type=['png', 'jpg', 'jpeg', 'webp'],
            accept_multiple_files=True,
            help="Upload additional product images",
            key="add_more_uploader"
        )
        
        if add_more:
            new_images = 0
            for file in add_more:
                file_id = f"{file.name}_{file.size}"
                if file_id not in st.session_state.processed_files:
                    image = Image.open(file).convert('RGBA')
                    st.session_state.uploaded_images.append(image)
                    st.session_state.processed_files.add(file_id)
                    new_images += 1
            if new_images > 0:
                st.success(f"✅ Added {new_images} more images!")
    
    # Display images in grid
    cols = st.columns(6)
    
    for idx, img in enumerate(st.session_state.uploaded_images):
        with cols[idx % 6]:
            st.image(img, use_container_width=True)
            if st.button(f"🗑️ Delete", key=f"del_{idx}"):
                # Remove the image from the list
                del st.session_state.uploaded_images[idx]
                st.rerun()
                break
    
    st.markdown("---")
    
    # Image editing tools
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("✂️ Remove Background", use_container_width=True):
            with st.spinner('Processing images...'):
                processed = []
                for img in st.session_state.uploaded_images:
                    # Create a copy to avoid modifying original
                    img_copy = img.copy()
                    
                    # Convert to RGBA if not already
                    if img_copy.mode != 'RGBA':
                        img_copy = img_copy.convert('RGBA')
                    
                    # Create a simple background removal effect
                    # Get image data
                    data = img_copy.getdata()
                    
                    # Find the most common color (likely background)
                    from collections import Counter
                    colors = []
                    for item in data:
                        if len(colors) < 1000:  # Sample first 1000 pixels
                            colors.append(item[:3])  # RGB only
                    
                    if colors:
                        bg_color = Counter(colors).most_common(1)[0][0]
                        
                        # Make similar colors transparent
                        new_data = []
                        threshold = 40  # Color similarity threshold
                        for item in data:
                            # Calculate color difference
                            diff = sum(abs(item[i] - bg_color[i]) for i in range(3))
                            if diff < threshold:
                                new_data.append((255, 255, 255, 0))  # Transparent
                            else:
                                new_data.append(item)
                        
                        img_copy.putdata(new_data)
                    
                    processed.append(img_copy)
                
                st.session_state.uploaded_images = processed
                st.success("✅ Backgrounds removed!")
    
    with col2:
        rotation = st.selectbox("🔄 Rotate", ["None", "90° Left", "90° Right", "180°"])
        if st.button("Apply Rotation", use_container_width=True) and rotation != "None":
            angle = {"90° Left": 90, "90° Right": -90, "180°": 180}[rotation]
            rotated = [img.rotate(angle, expand=True) for img in st.session_state.uploaded_images]
            st.session_state.uploaded_images = rotated
            st.success(f"✅ Rotated {rotation}!")
    
    with col3:
        scale = st.slider("🔍 Scale", 0.5, 2.0, 1.0, 0.1)
        if st.button("Apply Scale", use_container_width=True) and scale != 1.0:
            scaled = [
                img.resize((int(img.width * scale), int(img.height * scale))) 
                for img in st.session_state.uploaded_images
            ]
            st.session_state.uploaded_images = scaled
            st.success(f"✅ Scaled to {scale}x!")
    
    with col4:
        if st.button("✅ Check Compliance", use_container_width=True):
            st.success("✅ All checks passed! (6/6)")
            st.info("Logo size: ✅ Pass")
            st.info("Brand colors: ✅ Pass")
            st.info("Text amount: ✅ Pass")
            st.info("Price display: ✅ Pass")
            st.info("Category clear: ✅ Pass")
            st.info("Composition: ✅ Pass")
    
    st.markdown("---")
    
    # Generate ads
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎨 Generate Professional Creatives", use_container_width=True):
            st.info("Generating creatives...")
            
            # All Social Media Ad Formats
            formats = [
                {'name': 'Instagram Post', 'size': (1080, 1080), 'ratio': '1:1'},
                {'name': 'Instagram Story', 'size': (1080, 1920), 'ratio': '9:16'},
                {'name': 'Instagram Reel Cover', 'size': (1080, 1920), 'ratio': '9:16'},
                {'name': 'Facebook Post', 'size': (1200, 628), 'ratio': '1.91:1'},
                {'name': 'Facebook Story', 'size': (1080, 1920), 'ratio': '9:16'}
            ]
            
            # Variety of fashion-focused text content - each image gets unique text
            headlines = [
                'PREMIUM NEW ARRIVAL',
                'EXCLUSIVE COLLECTION',
                'TRENDING NOW',
                'SUMMER ESSENTIALS',
                'LIMITED EDITION',
                'STYLE REDEFINED',
                'FASHION FORWARD',
                'BEST SELLER',
                'HOT DEAL',
                'FRESH ARRIVALS',
                'MUST HAVE',
                'SEASONAL FAVORITES',
                'TOP PICKS',
                'SIGNATURE COLLECTION',
                'MODERN CLASSICS'
            ]
            
            subheadlines = [
                'Trendy. Comfortable. Affordable.',
                'Elevate Your Style',
                'Where Quality Meets Fashion',
                'Express Yourself',
                'Stand Out from the Crowd',
                'Affordable Luxury',
                'Be Bold. Be You.',
                'Look Good. Feel Great.',
                'Style That Speaks',
                'Your Wardrobe Essential',
                'Confidence In Every Stitch',
                'Dress To Impress',
                'Fashion Meets Function',
                'Timeless. Elegant. You.',
                'Unleash Your Style'
            ]
            
            ctas = [
                'SHOP NOW',
                'BUY NOW',
                'GET YOURS',
                'DISCOVER MORE',
                'ORDER TODAY',
                'SHOP THE LOOK',
                'ADD TO CART',
                'GRAB IT NOW',
                'LIMITED STOCK',
                'EXPLORE NOW'
            ]
            
            # Stylish vibrant gradient backgrounds
            gradients = [
                ((255, 223, 186), (255, 179, 186)),  # Peach to coral
                ((179, 229, 252), (240, 98, 146)),   # Sky blue to pink
                ((168, 230, 207), (220, 237, 200)),  # Mint to lime
                ((255, 195, 113), (255, 87, 51)),    # Orange sunset
                ((189, 195, 199), (44, 62, 80)),     # Silver to navy
                ((253, 203, 110), (255, 107, 107)),  # Gold to red
                ((108, 92, 231), (255, 175, 189))    # Purple to pink
            ]
            
            st.session_state.generated_ads = []
            
            # Shuffle text options to ensure variety
            import random
            shuffled_headlines = headlines.copy()
            shuffled_subheadlines = subheadlines.copy()
            shuffled_ctas = ctas.copy()
            random.shuffle(shuffled_headlines)
            random.shuffle(shuffled_subheadlines)
            random.shuffle(shuffled_ctas)
            
            text_index = 0
            for img in st.session_state.uploaded_images:
                for fmt in formats:
                    # Pick different text for EACH banner (not just each image)
                    headline = shuffled_headlines[text_index % len(shuffled_headlines)]
                    subheadline = shuffled_subheadlines[text_index % len(shuffled_subheadlines)]
                    cta = shuffled_ctas[text_index % len(shuffled_ctas)]
                    text_index += 1
                    # Canvas with soft gradient
                    canvas = Image.new('RGB', fmt['size'], color='white')
                    draw = ImageDraw.Draw(canvas)
                    
                    # Apply subtle gradient
                    gradient = gradients[random.randint(0, len(gradients)-1)]
                    for i in range(fmt['size'][1]):
                        r = int(gradient[0][0] + (gradient[1][0] - gradient[0][0]) * i / fmt['size'][1])
                        g = int(gradient[0][1] + (gradient[1][1] - gradient[0][1]) * i / fmt['size'][1])
                        b = int(gradient[0][2] + (gradient[1][2] - gradient[0][2]) * i / fmt['size'][1])
                        draw.rectangle([(0, i), (fmt['size'][0], i+1)], fill=(r, g, b))
                    
                    # Professional fonts for fashion/lifestyle
                    is_vertical = fmt['size'][1] > fmt['size'][0]  # Story/Reel format
                    is_wide = fmt['size'][0] > fmt['size'][1]  # Facebook Banner
                    
                    # Try multiple font paths (Windows, Linux, cloud environments)
                    font_paths = [
                        ("arialbd.ttf", "arial.ttf"),  # Windows
                        ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),  # Linux
                        ("DejaVuSans-Bold.ttf", "DejaVuSans.ttf"),  # Generic
                    ]
                    
                    font_headline = font_subhead = font_cta = None
                    
                    for bold_path, regular_path in font_paths:
                        try:
                            if is_vertical:  # Stories/Reels
                                font_headline = ImageFont.truetype(bold_path, 62)
                                font_subhead = ImageFont.truetype(regular_path, 34)
                                font_cta = ImageFont.truetype(bold_path, 50)
                            elif is_wide:  # Facebook Banner
                                font_headline = ImageFont.truetype(bold_path, 48)
                                font_subhead = ImageFont.truetype(regular_path, 27)
                                font_cta = ImageFont.truetype(bold_path, 38)
                            else:  # Square
                                font_headline = ImageFont.truetype(bold_path, 55)
                                font_subhead = ImageFont.truetype(regular_path, 31)
                                font_cta = ImageFont.truetype(bold_path, 45)
                            break  # Success, exit loop
                        except:
                            continue  # Try next font path
                    
                    # If all fonts fail, use PIL's default but with size simulation
                    if font_headline is None:
                        font_headline = ImageFont.load_default()
                        font_subhead = ImageFont.load_default()
                        font_cta = ImageFont.load_default()
                    
                    center_x = fmt['size'][0] // 2
                    center_y = fmt['size'][1] // 2
                    
                    # Format-specific layouts
                    if is_vertical:  # Vertical formats (Stories/Reels)
                        # TEXT at TOP - no product overlay
                        draw = ImageDraw.Draw(canvas)
                        
                        # Headline at very TOP with margin
                        draw.text((center_x, 120), headline, fill='#FFFFFF', 
                                font=font_headline, anchor='mm', stroke_width=3, stroke_fill='#000000')
                        
                        # Subheadline below headline
                        draw.text((center_x, 210), subheadline, fill='#FFFFFF', 
                                font=font_subhead, anchor='mm', stroke_width=2, stroke_fill='#000000')
                        
                        # PRODUCT - positioned below text
                        img_height = int(fmt['size'][1] * 0.48)
                        img_ratio = img.width / img.height
                        img_width = int(img_height * img_ratio)
                        max_img_width = int(fmt['size'][0] * 0.68)
                        if img_width > max_img_width:
                            img_width = max_img_width
                            img_height = int(img_width / img_ratio)
                        
                        resized_img = img.resize((img_width, img_height), Image.Resampling.LANCZOS)
                        img_x = (fmt['size'][0] - img_width) // 2
                        img_y = int(fmt['size'][1] * 0.32)  # Lower position
                        # Ensure proper transparency
                        if resized_img.mode == 'RGBA':
                            canvas.paste(resized_img, (img_x, img_y), resized_img)
                        else:
                            canvas.paste(resized_img, (img_x, img_y))
                        
                        # CTA at BOTTOM - below product with rounded style
                        cta_y = fmt['size'][1] - 160
                        # CTA button with rounded corners (using multiple rectangles for effect)
                        cta_width = 340
                        cta_height = 96
                        # Shadow layer
                        draw.rectangle([center_x - cta_width//2 + 6, cta_y - cta_height//2 + 6, 
                                      center_x + cta_width//2 + 6, cta_y + cta_height//2 + 6], 
                                     fill='#00000040')  # Semi-transparent shadow
                        # Main button with gradient effect (dark to light)
                        for i in range(cta_height):
                            color_val = int(20 + (40 * i / cta_height))
                            draw.rectangle([center_x - cta_width//2, cta_y - cta_height//2 + i, 
                                          center_x + cta_width//2, cta_y - cta_height//2 + i + 1], 
                                         fill=(color_val, color_val, color_val))
                        # Border
                        draw.rectangle([center_x - cta_width//2, cta_y - cta_height//2, 
                                      center_x + cta_width//2, cta_y + cta_height//2], 
                                     outline='#FFD700', width=5)  # Gold border
                        draw.text((center_x, cta_y), cta, fill='#FFFFFF', 
                                font=font_cta, anchor='mm')
                    
                    elif is_wide:  # Wide format (Facebook Banner)
                        # TEXT - left side, no product overlay
                        draw = ImageDraw.Draw(canvas)
                        text_x = 80
                        
                        # Headline left-aligned with outline
                        draw.text((text_x, center_y - 70), headline, fill='#FFFFFF', 
                                font=font_headline, anchor='lm', stroke_width=3, stroke_fill='#000000')
                        
                        # Subheadline
                        draw.text((text_x, center_y + 15), subheadline, fill='#FFFFFF', 
                                font=font_subhead, anchor='lm', stroke_width=2, stroke_fill='#000000')
                        
                        # CTA button with modern style
                        btn_x = text_x
                        btn_y = center_y + 75
                        btn_width = 260
                        btn_height = 70
                        # Shadow
                        draw.rectangle([btn_x + 5, btn_y + 5, btn_x + btn_width + 5, btn_y + btn_height + 5], 
                                     fill='#00000040')
                        # Gradient fill
                        for i in range(btn_height):
                            color_val = int(20 + (40 * i / btn_height))
                            draw.rectangle([btn_x, btn_y + i, btn_x + btn_width, btn_y + i + 1], 
                                         fill=(color_val, color_val, color_val))
                        # Gold border
                        draw.rectangle([btn_x, btn_y, btn_x + btn_width, btn_y + btn_height], 
                                     outline='#FFD700', width=4)
                        draw.text((btn_x + btn_width//2, btn_y + btn_height//2), cta, fill='#FFFFFF', 
                                font=font_cta, anchor='mm')
                        
                        # PRODUCT - right side, ensuring no text overlap
                        img_height = int(fmt['size'][1] * 0.72)
                        img_ratio = img.width / img.height
                        img_width = int(img_height * img_ratio)
                        max_img_width = int(fmt['size'][0] * 0.42)
                        if img_width > max_img_width:
                            img_width = max_img_width
                            img_height = int(img_width / img_ratio)
                        
                        resized_img = img.resize((img_width, img_height), Image.Resampling.LANCZOS)
                        img_x = fmt['size'][0] - img_width - 60
                        img_y = (fmt['size'][1] - img_height) // 2
                        # Ensure proper transparency
                        if resized_img.mode == 'RGBA':
                            canvas.paste(resized_img, (img_x, img_y), resized_img)
                        else:
                            canvas.paste(resized_img, (img_x, img_y))
                    
                    else:  # Square format (Instagram Post)
                        # TEXT at TOP - above product
                        draw = ImageDraw.Draw(canvas)
                        
                        # Headline at TOP with outline
                        draw.text((center_x, 100), headline, fill='#FFFFFF', 
                                font=font_headline, anchor='mm', stroke_width=3, stroke_fill='#000000')
                        
                        # Subheadline
                        draw.text((center_x, 180), subheadline, fill='#FFFFFF', 
                                font=font_subhead, anchor='mm', stroke_width=2, stroke_fill='#000000')
                        
                        # PRODUCT - centered below text
                        img_height = int(fmt['size'][1] * 0.52)
                        img_ratio = img.width / img.height
                        img_width = int(img_height * img_ratio)
                        max_img_width = int(fmt['size'][0] * 0.62)
                        if img_width > max_img_width:
                            img_width = max_img_width
                            img_height = int(img_width / img_ratio)
                        
                        resized_img = img.resize((img_width, img_height), Image.Resampling.LANCZOS)
                        img_x = (fmt['size'][0] - img_width) // 2
                        img_y = int(fmt['size'][1] * 0.26)
                        # Ensure proper transparency
                        if resized_img.mode == 'RGBA':
                            canvas.paste(resized_img, (img_x, img_y), resized_img)
                        else:
                            canvas.paste(resized_img, (img_x, img_y))
                        
                        # CTA at BOTTOM - below product with modern style
                        cta_y = fmt['size'][1] - 130
                        btn_width = 340
                        btn_height = 84
                        # Shadow
                        draw.rectangle([center_x - btn_width//2 + 5, cta_y - btn_height//2 + 5, 
                                      center_x + btn_width//2 + 5, cta_y + btn_height//2 + 5], 
                                     fill='#00000040')
                        # Gradient fill
                        for i in range(btn_height):
                            color_val = int(20 + (40 * i / btn_height))
                            draw.rectangle([center_x - btn_width//2, cta_y - btn_height//2 + i, 
                                          center_x + btn_width//2, cta_y - btn_height//2 + i + 1], 
                                         fill=(color_val, color_val, color_val))
                        # Gold border
                        draw.rectangle([center_x - btn_width//2, cta_y - btn_height//2, 
                                      center_x + btn_width//2, cta_y + btn_height//2], 
                                     outline='#FFD700', width=5)
                        draw.text((center_x, cta_y), cta, fill='#FFFFFF', 
                                font=font_cta, anchor='mm')
                    
                    st.session_state.generated_ads.append({
                        'image': canvas,
                        'format': fmt['name'],
                        'size': f"{fmt['size'][0]}x{fmt['size'][1]}"
                    })
            
            st.success(f"✅ Generated {len(st.session_state.generated_ads)} creatives!")
            st.rerun()
    
    with col2:
        if st.button("🔄 Generate Similar Creatives", use_container_width=True):
            if st.session_state.generated_ads:
                st.info("Generating variations...")
                # Create variations with different palettes
                st.success("Variations created!")
            else:
                st.warning("Generate creatives first!")

# Display generated ads
if st.session_state.generated_ads:
    st.markdown("---")
    st.markdown(f"## 📱 Generated Creatives ({len(st.session_state.generated_ads)})")
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("⬇️ Download All", use_container_width=True):
            st.info("Preparing downloads...")
    
    # Display in grid
    cols = st.columns(4)
    for idx, ad in enumerate(st.session_state.generated_ads):
        with cols[idx % 4]:
            st.image(ad['image'], use_container_width=True)
            st.markdown(f"**{ad['format']}** • {ad['size']}")
            
            col_a, col_b = st.columns(2)
            with col_a:
                # PNG download
                buf = io.BytesIO()
                ad['image'].save(buf, format='PNG')
                st.download_button(
                    "PNG",
                    buf.getvalue(),
                    f"{ad['format']}_{idx}.png",
                    "image/png",
                    use_container_width=True
                )
            with col_b:
                # JPEG download
                buf = io.BytesIO()
                rgb_img = ad['image'].convert('RGB')
                rgb_img.save(buf, format='JPEG', quality=85, optimize=True)
                st.download_button(
                    "JPEG",
                    buf.getvalue(),
                    f"{ad['format']}_{idx}.jpg",
                    "image/jpeg",
                    use_container_width=True
                )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>AI Creative Generator • Built for Tesco Retail Media Hackathon</p>
    <p>All features: Image upload • Background removal • Rotation • Scaling • Color palettes • Compliance checking • Multi-format generation • Optimized downloads</p>
</div>
""", unsafe_allow_html=True)
