# 🌍 OpenWorld API

Uma API RESTful e WebSocket feita com FastAPI que simula um mundo aberto com jogadores, itens, batalhas, coleta de recursos e interações com NPCs.

---

## 🚀 Tecnologias

- Python 3.11+
- FastAPI
- WebSocket
- JWT (Auth)
- SQLAlchemy
- PostgreSQL ou SQLite
- Uvicorn
- Alembic
- dotenv

---

## 📁 Estrutura de Pastas

```bash
.
├── api/           # Rotas (players, itens, auth, etc)
├── core/          # Configs globais, JWT, segurança
├── models/        # SQLAlchemy (Player, Item, etc)
├── schemas/       # Pydantic (validação e entrada/saída)
├── services/      # Regras de negócio
├── db/            # Conexão e scripts do banco
├── soquets/       # Comunicação WebSocket
├── .env.example   # Variáveis de ambiente (modelo)
├── main.py        # Ponto de entrada

DATABASE_URL=sqlite:///./world.db
JWT_SECRET_KEY=sua-chave-secreta
JWT_ALGORITHM=HS256

🛠️ Como rodar o projeto
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute a API:

bash
Copiar
Editar
uvicorn main:app --reload
Acesse em: http://localhost:8000/docs

✅ Funcionalidades
Cadastro e login com JWT

Criação de jogadores

Criação e coleta de itens

Comunicação em tempo real com WebSocket

Sistema de batalhas e exploração (em construção)

📦 Deploy
Em breve será feito o deploy na Render/Railway.
As variáveis .env são obrigatórias no ambiente de produção.

🧠 Contribuição
Esse projeto é um desafio pessoal de aprendizado com foco em FastAPI, JWT, sockets e organização de código profissional.

🧔 Autor
Desenvolvido por Marcos Vinícius
🔗 LinkedIn

