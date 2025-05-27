# Design Pattern Recommender - CLI

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Sistema inteligente para recomendar Design Patterns baseado em casos de uso, utilizando IA generativa (Google Gemini API) através de uma interface de linha de comando.

## 📋 Sobre o Projeto

Este sistema utiliza Inteligência Artificial para analisar casos de uso e recomendar os Design Patterns mais apropriados para cada situação. Ele é especialmente útil para desenvolvedores que precisam tomar decisões arquiteturais baseadas em boas práticas de design.

## 🏗️ Estrutura do Projeto

```
design-pattern-cli/
├── main.py                # Ponto de entrada do sistema
├── cli.py                 # Interface de linha de comando
├── pattern_recommender.py # Lógica de recomendação usando Gemini API
├── model_manager.py       # Gerenciamento dos modelos do Gemini
├── requirements.txt       # Dependências Python
├── .env                   # Arquivo de configuração (não versionado)
└── README.md              # Documentação do projeto
```

## ⚙️ Requisitos

- Python 3.8 ou superior
- Conta Google com acesso à Gemini API (obtenha sua chave em https://makersuite.google.com/app/apikey)
- Conexão com a internet

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/dgomp/design-pattern-cli.git
cd design-pattern-cli
```

2. Crie um arquivo `.env` na raiz do projeto com sua chave Gemini:
```
GOOGLE_API_KEY=sua_chave_aqui
```

3. Gere sua API Key [aqui](https://makersuite.google.com/app/apikey) (clique em **Criar chave de API**).

4. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

## 💻 Executando o Sistema

Execute o sistema:
```bash
python main.py
```

## ✨ Funcionalidades

- Interface via linha de comando intuitiva
- Seleção automática do modelo mais recente do Gemini
- Possibilidade de trocar o modelo durante a execução
- Análise de casos de uso usando IA generativa (Google Gemini)
- Recomendação dos 3 Design Patterns mais apropriados
- Porcentagem de confiança para cada recomendação
- Explicação detalhada e implementação separadas para cada padrão
- Totalmente gratuito (requer conexão com a internet e chave Gemini)

## 🛠️ Tecnologias Utilizadas

- google-generativeai (API do Google Gemini)
- python-dotenv (variáveis de ambiente)
- Python 3.8+

## 📦 Desenvolvimento

### Componentes
- `main.py`: Ponto de entrada do sistema
- `cli.py`: Interface de linha de comando
- `pattern_recommender.py`: Implementa a lógica de recomendação usando Gemini API
- `model_manager.py`: Gerencia os modelos do Gemini e suas configurações

## 📝 Exemplo de Uso

1. Execute o programa:
```bash
python main.py
```

2. No menu principal, escolha a opção 1 para recomendar um padrão de design

3. Digite um caso de uso, por exemplo:
```
Preciso criar um sistema que permita diferentes formas de pagamento (cartão de crédito, boleto, pix) e que seja fácil adicionar novos métodos no futuro.
```

4. O sistema retornará:
- Os 3 Design Patterns mais apropriados
- Porcentagem de confiança para cada padrão
- Explicação detalhada
- Sugestão de implementação

5. Use a opção 2 do menu para trocar o modelo do Gemini, se desejar

## 💡 Dicas
- O sistema configura automaticamente o modelo mais recente do Gemini
- Você pode trocar o modelo a qualquer momento através do menu
- Quanto mais detalhado for seu caso de uso, melhores serão as recomendações
- O sistema depende de conexão com a internet para acessar a Gemini API

## 🤝 Contribuindo
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 