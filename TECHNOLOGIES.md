# Technologies & Frameworks Used

## 🎨 AI Creative Generator - Fashion Retail Media

### **Core Technologies**

#### **Python 3.12**
- Primary programming language
- Used for backend logic and image processing

#### **Streamlit**
- Web framework for creating interactive data apps
- Powers the entire UI/UX interface
- Enables rapid prototyping and deployment
- Provides built-in widgets for file uploads, buttons, and displays

### **Image Processing & Computer Vision**

#### **Pillow (PIL Fork)**
- Python Imaging Library for image manipulation
- Used for:
  - Background removal and transparency handling
  - Image resizing and canvas creation
  - Drawing text overlays on banners
  - Color palette extraction and application
  - Format conversion (PNG, JPEG, WebP)
  - Gradient generation for backgrounds

#### **ImageDraw (Pillow Module)**
- Drawing graphics and text on images
- Creating custom shapes (rectangles, circles for badges)
- Rendering CTA buttons with gradients
- Text stroke effects for visibility

#### **ImageFont (Pillow Module)**
- Typography and font rendering
- Multiple font fallback system (Arial → DejaVu)
- Dynamic font sizing for different banner formats
- Cross-platform font compatibility

#### **ImageFilter (Pillow Module)**
- Image filtering and effects
- Edge detection for background removal

### **Frontend Technologies**

#### **HTML5 & CSS3**
- Custom styling through Streamlit markdown
- Responsive design with media queries
- Gradient backgrounds and animations
- CSS Grid and Flexbox for layouts

#### **Responsive Design**
- Mobile-first approach
- Viewport-based sizing (vw, rem)
- Overflow control for cross-device compatibility
- Word-wrapping and flexible containers

### **Data Structures & Libraries**

#### **Python Standard Library**
- `io` - In-memory file operations
- `random` - Randomization for text variety and gradient selection
- `datetime` - Timestamp generation for file naming

### **Design & UI Frameworks**

#### **Color Theory**
- 7 vibrant gradient color schemes
- HSL color space manipulation
- Brand color palette system
- Contrast optimization for readability

#### **Typography System**
- Hierarchical font sizing (62px - 27px range)
- Text stroke outlines for visibility
- Responsive font scaling
- Platform-specific font rendering

### **Banner Generation System**

#### **Multi-Format Support**
- Instagram Post (1080x1080)
- Instagram Story (1080x1920)
- Instagram Reel Cover (1080x1920)
- Facebook Post (1200x628)
- Facebook Story (1080x1920)

#### **Layout Algorithms**
- Format-specific positioning logic
- Vertical vs. horizontal layout detection
- Product image centering and scaling
- Text placement to avoid product overlay
- Safe margin calculations for social media UI

### **Text Content System**

#### **Dynamic Text Generation**
- 15 unique headlines
- 15 unique subheadlines
- 10 unique CTAs
- Randomized text distribution
- No text repetition across banners

### **Deployment & DevOps**

#### **Streamlit Cloud**
- Cloud hosting platform
- Auto-deployment from GitHub
- Environment variable management
- SSL/HTTPS encryption

#### **Git & GitHub**
- Version control system
- Repository: `Ai-Creative-Generator-Ads-Generator-`
- Continuous integration workflow

### **Package Management**

#### **pip**
- Python package installer
- Requirements.txt for dependency management

#### **System Packages (Linux)**
- fonts-dejavu-core (DejaVu fonts for cloud deployment)

### **File Format Support**

#### **Input Formats**
- PNG (with transparency)
- JPEG/JPG
- WebP

#### **Output Formats**
- PNG (high quality with transparency)
- JPEG (optimized for social media)

### **Session Management**

#### **Streamlit Session State**
- Persistent state management
- Multi-image upload tracking
- Generated ads storage
- Color palette persistence
- File deduplication

### **Development Tools**

#### **VS Code**
- Primary IDE
- Python extensions
- Git integration

#### **Windows PowerShell**
- Terminal environment
- Script execution
- Git commands

---

## 📊 Technical Specifications

### Performance Optimizations
- Lazy loading for images
- Session state caching
- Efficient image resampling (LANCZOS algorithm)
- Minimal memory footprint

### Responsive Design Features
- Ultra-compact layout (0.3rem - 0.5rem padding)
- Viewport-constrained containers (100vw max-width)
- Horizontal scroll prevention
- Word-wrap on all elements
- Flexible column ratios

### Accessibility
- High contrast text with stroke outlines
- Readable font sizes (minimum 0.65rem)
- Clear visual hierarchy
- Mobile-friendly touch targets

### Browser Compatibility
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- Tested on Streamlit Cloud environment

---

## 🏷️ Tags & Keywords

`Streamlit` `Python` `PIL` `Pillow` `Computer Vision` `Image Processing` 
`AI` `Generative AI` `Creative Generator` `Banner Generator` `Social Media` 
`Instagram` `Facebook` `Typography` `Gradient Design` `Responsive Design` 
`Cloud Deployment` `GitHub` `Git` `Fashion` `Retail Media` `Marketing` 
`Advertising` `CTA Buttons` `Background Removal` `Canvas Drawing` 
`Multi-Format` `Cross-Platform` `Web App` `Frontend` `Backend` 
`CSS3` `HTML5` `Automated Design` `Template Generation`
