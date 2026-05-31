# CineChat AI 🎬

A real-time AI chatbot companion for cinephiles. Discuss movies, get recommendations, and explore cinema with an AI that understands film deeply.

## Features

✨ **Real-time Messaging** - WebSocket-based instant communication
🤖 **AI-Powered Conversations** - GPT-4 integrated with cinema knowledge
🎥 **Movie Recommendations** - Personalized suggestions based on preferences
🎞️ **Film Database** - Access to extensive movie information
💾 **Chat History** - Persistent conversation storage
👥 **User Profiles** - Personalized experience for cinephiles

## Tech Stack

### Frontend
- Next.js 14 (React 18+)
- TypeScript
- Socket.IO Client
- Tailwind CSS
- Zustand (State Management)

### Backend
- FastAPI (Python)
- WebSockets
- PostgreSQL
- Redis (Caching & Message Brokering)
- OpenAI API (GPT-4)
- SQLAlchemy ORM

### Infrastructure
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- Environment-based configuration

## Project Structure

```
cinechat-ai/
├── frontend/                 # Next.js application
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── hooks/
│   ├── store/
│   └── package.json
├── backend/                  # FastAPI application
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── database/
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .github/workflows/        # CI/CD
└── README.md
```

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+
- Python 3.10+
- PostgreSQL (or use Docker)
- Redis (or use Docker)

### Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/Abdulla-fr/cinechat-ai.git
cd cinechat-ai

# Create environment files
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local

# Start all services
docker-compose up -d

# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

### Manual Setup

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://user:password@localhost/cinechat
REDIS_URL=redis://localhost:6379/0
OPENAI_API_KEY=your_openai_api_key
JWT_SECRET=your_jwt_secret
ALLOWED_ORIGINS=http://localhost:3000
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_WS_URL=ws://localhost:8000
```

## API Documentation

Interactive API docs available at: `http://localhost:8000/docs`

## Development

### Run Tests
```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm test
```

### Code Quality
```bash
# Backend
pylint app/
black app/

# Frontend
npm run lint
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions, please open an issue on GitHub.

---

**CineChat AI** - Where cinema lovers meet AI intelligence 🎬✨
