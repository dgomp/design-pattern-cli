# Design Pattern Recommender - BackEnd

Sistema inteligente para recomendar Design Patterns baseado em casos de uso, utilizando IA generativa (Google Gemini API) através de uma interface de linha de comando.

## Estrutura do Projeto

```
design-pattern-backend/
├── app.py                  # Servidor Flask e lógica do backend
├── pattern_recommender.py  # Lógica de recomendação usando Gemini API
├── ask.py                  # Interface de linha de comando
├── requirements.txt        # Dependências Python
└── README.md              # Documentação do projeto
```

## Requisitos

- Python 3.8 ou superior
- Conta Google com acesso à Gemini API (obtenha sua chave em https://makersuite.google.com/app/apikey)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/dgomp/design-pattern-backend.git
cd design-pattern-backend
```

2. Crie um arquivo `.env` na raiz do projeto com sua chave Gemini:
```
GOOGLE_API_KEY=sua_chave_aqui
```

3. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

## Executando o Sistema

1. Em um terminal, inicie o servidor:
```bash
python app.py
```

2. Em outro terminal, execute a interface de linha de comando:
```bash
python ask.py
```

## Funcionalidades

- Interface via linha de comando
- Análise de casos de uso usando IA generativa (Google Gemini)
- Recomendação dos 3 Design Patterns mais apropriados
- Porcentagem de confiança para cada recomendação
- Explicação detalhada e implementação separadas para cada padrão
- Totalmente gratuito (requer conexão com a internet e chave Gemini)

## Tecnologias Utilizadas

### Backend
- Flask (servidor web)
- requests (requisições HTTP)
- python-dotenv (variáveis de ambiente)
- Google Gemini API (IA generativa)

## API

### POST /recommend
Recebe um caso de uso e retorna recomendações de Design Patterns.

**Request Body:**
```json
{
    "useCase": "Descrição do caso de uso"
}
```

**Response:**
```json
{
    "patterns": [
        {
            "name": "Nome do Padrão",
            "confidence": 0.85,
            "explanation": "Explicação detalhada",
            "implementation": "Sugestão de implementação"
        },
        // ... até 3 padrões
    ]
}
```

## Desenvolvimento

### Backend
- `app.py`: Servidor Flask que gerencia as requisições
- `pattern_recommender.py`: Implementa a lógica de recomendação usando Gemini API
- `ask.py`: Interface de linha de comando para interação com o usuário

## Dicas
- O sistema depende de conexão com a internet para acessar a Gemini API
- Você pode testar diferentes casos de uso para ver recomendações variadas
- Para sair do programa, digite 'sair' quando solicitado

## Contribuindo
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request 