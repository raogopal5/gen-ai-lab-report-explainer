for oolama run

ollama pull llama3:mistral
ollama serve

for run backend

cd backend
pip install -r requirements.txt
uvicorn app:app --reload


for run frontend

npm create vite@latest frontend -- --template react
cd frontend
npm install
npm run dev



cd frontend
npm install
npm run dev