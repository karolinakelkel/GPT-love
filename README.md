# GPTLove

GPTLove is a backend API for AI-assisted conflict de-escalation between two users in a chat environment.

Instead of sending raw messages, users interact through an OpenAI-powered system that softens their tone, rewrites emotionally intense content into caring and respectful communication, and encourages better dialogue.

---

## Why

This project aims to:
- Promote empathy in digital conversations
- Help people avoid miscommunication and emotional harm
- Teach emotional literacy through interaction

---

## Key Features

- FastAPI-based backend with JWT user authentication
- PostgreSQL database for user and message storage
- OpenAI GPT-based message softening
- Asynchronous architecture using aiohttp or httpx
- Full test coverage with pytest
- Dockerized setup and GitHub Actions CI
- Public deployment (Render or Fly.io)

---

## Stack

- Python 3.12
- FastAPI
- PostgreSQL + SQLAlchemy
- OpenAI API
- Docker / docker-compose
- GitHub Actions
- pytest, coverage

---

## Roadmap (MVP)

- [x] Project structure
- [ ] User registration and login
- [ ] Message softening logic via OpenAI
- [ ] Chat session and message storage
- [ ] Authenticated chat API
- [ ] Testing suite
- [ ] Docker setup
- [ ] CI/CD and deployment

---

## License

MIT © Karolina Kelkel
