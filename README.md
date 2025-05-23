# Design Pattern Recommender - CLI

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Sistema inteligente para recomendar Design Patterns baseado em casos de uso, utilizando IA generativa (Google Gemini API) através de uma interface de linha de comando.

## 📋 Sobre o Projeto

Este sistema utiliza Inteligência Artificial para analisar casos de uso e recomendar os Design Patterns mais apropriados para cada situação. Ele é especialmente útil para desenvolvedores que precisam tomar decisões arquiteturais baseadas em boas práticas de design.

## 🏗️ Estrutura do Projeto

```
design-pattern-backend/
├── pattern_recommender.py  # Lógica de recomendação usando Gemini API
├── ask.py                  # Interface de linha de comando
├── requirements.txt        # Dependências Python
├── .env                    # Arquivo de configuração (não versionado)
└── README.md               # Documentação do projeto
```

## ⚙️ Requisitos

- Python 3.8 ou superior
- Conta Google com acesso à Gemini API (obtenha sua chave em https://makersuite.google.com/app/apikey)
- Conexão com a internet

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/design-pattern-cli.git
cd design-pattern-cli
```

2. Crie um arquivo `.env` na raiz do projeto com sua chave Gemini:
```
GOOGLE_API_KEY=sua_chave_aqui
```

3. Gere sua API Key [aqui](https://makersuite.google.com/app/apikey) (clique em *Criar chave de API*).

4. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

## 💻 Executando o Sistema

Execute a interface de linha de comando:
```bash
python ask.py
```

## ✨ Funcionalidades

- Interface via linha de comando
- Análise de casos de uso usando IA generativa (Google Gemini)
- Recomendação dos 3 Design Patterns mais apropriados
- Porcentagem de confiança para cada recomendação
- Explicação detalhada e implementação separadas para cada padrão
- Totalmente gratuito (requer conexão com a internet e chave Gemini)

## 🛠️ Tecnologias Utilizadas

- requests (requisições HTTP)
- python-dotenv (variáveis de ambiente)
- Google Gemini API (IA generativa)

## 📦 Desenvolvimento

### Componentes
- `pattern_recommender.py`: Implementa a lógica de recomendação usando Gemini API
- `ask.py`: Interface de linha de comando para interação com o usuário

## 📝 Exemplo de Uso

1. Execute o programa:
```bash
python ask.py
```

2. Digite um caso de uso, por exemplo:
```
Preciso criar um sistema que permita diferentes formas de pagamento (cartão de crédito, boleto, pix) e que seja fácil adicionar novos métodos no futuro.
```

3. O sistema retornará:
- Os 3 Design Patterns mais apropriados
- Porcentagem de confiança para cada padrão
- Explicação detalhada
- Sugestão de implementação

## 💡 Dicas
- O sistema depende de conexão com a internet para acessar a Gemini API
- Você pode testar diferentes casos de uso para ver recomendações variadas
- Para sair do programa, digite 'sair' quando solicitado
- Quanto mais detalhado for seu caso de uso, melhores serão as recomendações

## 🤝 Contribuindo
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 