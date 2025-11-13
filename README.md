# Retail Media Creative Tool - Generative AI Solution

## Overview
A comprehensive creative builder tool that empowers advertisers to autonomously create professional, guideline-compliant retail media creatives using Generative AI.

## Features

### Core Features
- ✅ Visual drag-and-drop creative builder
- ✅ Packshot and background import/management
- ✅ AI-powered background removal
- ✅ Image manipulation (resize, rotate, crop)
- ✅ Custom color palette management
- ✅ Multi-asset composition
- ✅ AI-driven creative suggestions
- ✅ Guideline compliance validation
- ✅ Multi-format support (Facebook & Instagram)
- ✅ Optimized export (JPEG/PNG < 500KB)

### Stretch Goals Implemented
- ✅ AI-driven adaptive resizing across formats
- ✅ Intelligent guideline validation
- ✅ Collaborative review workflow
- ✅ Auto-generate campaign-ready creative sets

## Technology Stack

### Frontend
- **React 18** with TypeScript
- **Fabric.js** - Canvas manipulation and visual builder
- **TailwindCSS** - Styling
- **Zustand** - State management
- **React Query** - Server state management

### Backend
- **Node.js** with Express
- **Python Flask** - AI/ML services
- **Sharp** - Image processing
- **TensorFlow.js** - Background removal
- **OpenAI API** - Creative suggestions

### AI/ML Components
- **Remove.bg API** - Background removal
- **Stable Diffusion** - Image generation
- **GPT-4 Vision** - Guideline compliance checking
- **CLIP** - Visual similarity search

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend (React)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Visual Editor│  │ Asset Manager│  │ Export Module│      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                     API Gateway (Node.js)                    │
└─────────────────────────────────────────────────────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│Image Service │  │  AI Service  │  │  Compliance  │
│   (Sharp)    │  │   (Python)   │  │   Service    │
└──────────────┘  └──────────────┘  └──────────────┘
```

## Quick Start

### Prerequisites
- Node.js 18+
- Python 3.9+
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Install Python dependencies
cd ai-service
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys (OpenAI, Remove.bg, etc.)
```

### Running the Application

```bash
# Start all services
npm run dev

# Or start individually:
npm run dev:frontend  # Frontend on http://localhost:3000
npm run dev:backend   # Backend on http://localhost:5000
npm run dev:ai        # AI Service on http://localhost:5001
```

## Project Structure

```
retail-media-creative-tool/
├── frontend/                 # React frontend
│   ├── src/
│   │   ├── components/      # React components
│   │   │   ├── editor/      # Visual editor components
│   │   │   ├── assets/      # Asset management
│   │   │   └── export/      # Export functionality
│   │   ├── hooks/           # Custom React hooks
│   │   ├── services/        # API services
│   │   ├── store/           # State management
│   │   └── utils/           # Utilities
│   └── public/
├── backend/                  # Node.js backend
│   ├── src/
│   │   ├── routes/          # API routes
│   │   ├── controllers/     # Business logic
│   │   ├── services/        # Image processing
│   │   └── middleware/      # Express middleware
│   └── uploads/             # Temporary file storage
├── ai-service/              # Python AI service
│   ├── app.py               # Flask application
│   ├── models/              # AI models
│   ├── services/            # AI services
│   └── utils/               # Helper functions
├── docs/                    # Documentation
│   ├── GUIDELINES.md        # Compliance guidelines
│   └── API.md               # API documentation
└── examples/                # Sample creatives
```

## Key Features Explained

### 1. Visual Creative Builder
- Drag-and-drop interface powered by Fabric.js
- Real-time canvas manipulation
- Layer management
- Undo/redo functionality
- Grid and snap-to-guide features

### 2. AI-Powered Features

#### Background Removal
```typescript
// Automatic background removal using AI
const removeBackground = async (image: File) => {
  const result = await api.post('/ai/remove-background', image);
  return result.processedImage;
};
```

#### Creative Suggestions
```typescript
// Get AI-driven similar creative suggestions
const getSuggestions = async (creative: Creative) => {
  const suggestions = await api.post('/ai/suggest-similar', {
    creative,
    style: 'professional',
    industry: 'retail'
  });
  return suggestions;
};
```

### 3. Guideline Compliance

The tool validates creatives against:
- **Brand Guidelines**: Logo placement, colors, fonts
- **Retailer Guidelines**: Size, format, content restrictions
- **Platform Guidelines**: Facebook/Instagram specifications

```typescript
const validateCompliance = async (creative: Creative) => {
  const validation = await api.post('/compliance/validate', creative);
  return {
    isCompliant: validation.passed,
    issues: validation.issues,
    suggestions: validation.suggestions
  };
};
```

### 4. Multi-Format Support

Supported formats based on the attached images:
- Facebook: 1080x1080px (1:1)
- Instagram: 1080x1080px (1:1), 1200x628px (1.91:1)
- Instagram Stories: 1080x1920px (9:16)

### 5. Optimized Export

Automatic optimization to ensure file size < 500KB:
```typescript
const exportCreative = async (creative: Creative, format: 'jpeg' | 'png') => {
  return api.post('/export', {
    creative,
    format,
    maxSize: 500 * 1024, // 500KB
    quality: 'auto' // Auto-adjust for size
  });
};
```

## Compliance Guidelines

### Brand Guidelines (Auto-validated)
- ✓ Logo must be visible and unobstructed
- ✓ Brand colors must match palette (±5% tolerance)
- ✓ Minimum logo size: 10% of creative width
- ✓ Safe zones: 5% margin from edges

### Retailer Guidelines
- ✓ No competitor branding
- ✓ Professional imagery only
- ✓ Clear product visibility
- ✓ Readable text (minimum 12pt equivalent)
- ✓ Appropriate contrast ratios (WCAG AA)

### Platform Guidelines
- ✓ Facebook/Instagram text overlay < 20%
- ✓ High resolution (minimum 72 DPI)
- ✓ Aspect ratio compliance
- ✓ File size < 500KB

## Usage Examples

### Creating a Creative

```typescript
import { CreativeBuilder } from './components/editor';

function App() {
  return (
    <CreativeBuilder
      format="facebook-post"
      onComplete={(creative) => {
        console.log('Creative ready:', creative);
      }}
    />
  );
}
```

### Color Palette Management

```typescript
// Save frequently used colors
const savePalette = async (colors: string[]) => {
  await api.post('/user/palette', { colors });
};

// Retrieve saved palette
const palette = await api.get('/user/palette');
```

## API Endpoints

### Image Processing
- `POST /api/images/upload` - Upload images
- `POST /api/images/remove-bg` - Remove background
- `POST /api/images/resize` - Resize image
- `POST /api/images/rotate` - Rotate image

### AI Services
- `POST /api/ai/suggest-similar` - Get similar creatives
- `POST /api/ai/generate-background` - Generate backgrounds
- `POST /api/ai/enhance` - Enhance image quality

### Compliance
- `POST /api/compliance/validate` - Validate creative
- `GET /api/compliance/guidelines` - Get guidelines

### Export
- `POST /api/export/jpeg` - Export as JPEG
- `POST /api/export/png` - Export as PNG
- `POST /api/export/batch` - Export multiple formats

## Testing

```bash
# Run all tests
npm test

# Run specific test suites
npm test:frontend
npm test:backend
npm test:ai

# Run with coverage
npm test:coverage
```

## Deployment

```bash
# Build for production
npm run build

# Deploy to cloud (example: Vercel + Railway)
npm run deploy
```

## Performance Considerations

- **Lazy Loading**: Components loaded on demand
- **Image Optimization**: Automatic compression and format selection
- **Caching**: Redis for frequently accessed data
- **CDN**: Static assets served via CDN
- **Background Processing**: Heavy AI tasks queued

## Security

- API key encryption
- Rate limiting on AI endpoints
- Image sanitization
- CORS configuration
- Input validation

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for GPT-4 Vision
- Remove.bg for background removal
- Stability AI for Stable Diffusion
- Fabric.js community

## Support

For issues and questions:
- GitHub Issues: [Create an issue](https://github.com/yourrepo/issues)
- Documentation: [Full docs](https://docs.yourapp.com)
- Email: support@yourapp.com

---

Built with ❤️ for the Retail Media Creative Tool Hackathon
