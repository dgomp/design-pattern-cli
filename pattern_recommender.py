import os
from dotenv import load_dotenv
import json
import re
import requests

class PatternRecommender:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("Chave da API do Google Gemini não encontrada. Por favor, crie um arquivo .env com GOOGLE_API_KEY=sua_chave_aqui")
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        self.base_prompt = """
        Analise o seguinte caso de uso e recomende os 3 Design Patterns mais apropriados.
        Para cada padrão, forneça:
        1. Nome do padrão
        2. Porcentagem de confiança (valor entre 0 e 1, onde 0.85 representa 85% de confiança)
        3. Explicação detalhada
        4. Sugestão de implementação

        IMPORTANTE: Você DEVE retornar EXATAMENTE 3 padrões, ordenados do mais apropriado para o menos apropriado.

        Caso de uso:
        {use_case}

        Responda APENAS com um objeto JSON válido no seguinte formato, sem nenhum texto adicional:
        {{
            "patterns": [
                {{
                    "name": "Nome do Padrão",
                    "confidence": 0.85,
                    "explanation": "Explicação detalhada",
                    "implementation": "Sugestão de implementação"
                }},
                {{
                    "name": "Nome do Segundo Padrão",
                    "confidence": 0.75,
                    "explanation": "Explicação detalhada",
                    "implementation": "Sugestão de implementação"
                }},
                {{
                    "name": "Nome do Terceiro Padrão",
                    "confidence": 0.65,
                    "explanation": "Explicação detalhada",
                    "implementation": "Sugestão de implementação"
                }}
            ]
        }}
        """

    def analyze_use_case(self, use_case: str) -> dict:
        try:
            prompt = self.base_prompt.format(use_case=use_case)
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [
                    {"parts": [{"text": prompt}]}
                ]
            }
            response = requests.post(
                f"{self.api_url}?key={self.api_key}",
                headers=headers,
                json=data
            )
            if response.status_code != 200:
                return {'error': f'Erro na API: {response.status_code}'}
            response_data = response.json()
            if 'candidates' not in response_data or not response_data['candidates']:
                return {'error': 'Resposta inválida da API'}
            text_response = response_data['candidates'][0]['content']['parts'][0]['text']
            try:
                json_str = text_response.strip()
                match = re.search(r'\{[\s\S]*\}', json_str)
                if match:
                    json_str = match.group(0)
                else:
                    raise ValueError("Nenhum objeto JSON encontrado na resposta do modelo.")
                result = json.loads(json_str)
                if not isinstance(result, dict) or 'patterns' not in result:
                    raise ValueError("Resposta não contém a chave 'patterns'")
                if not isinstance(result['patterns'], list):
                    raise ValueError("'patterns' não é uma lista")
                if len(result['patterns']) != 3:
                    raise ValueError("A resposta deve conter exatamente 3 padrões")
                for pattern in result['patterns']:
                    if not isinstance(pattern, dict):
                        raise ValueError("Padrão inválido na lista")
                    required_fields = ['name', 'confidence', 'explanation', 'implementation']
                    for field in required_fields:
                        if field not in pattern:
                            raise ValueError(f"Campo '{field}' ausente no padrão")
                    confidence = pattern['confidence']
                    if isinstance(confidence, (int, float)):
                        if confidence > 1:
                            pattern['confidence'] = confidence / 100
                        elif confidence < 0:
                            pattern['confidence'] = 0
                        elif confidence > 1:
                            pattern['confidence'] = 1
                    else:
                        raise ValueError("Valor de confiança deve ser um número")
                # Ordena os padrões por confiança (do maior para o menor)
                result['patterns'].sort(key=lambda x: x['confidence'], reverse=True)
                return result
            except json.JSONDecodeError as e:
                return {'error': f'Erro ao processar a resposta do modelo: {str(e)}'}
        except Exception as e:
            return {'error': f'Erro ao processar a recomendação: {str(e)}'}

def main():
    print("=== Sistema de Recomendação de Design Patterns ===")
    recommender = PatternRecommender()
    
    print("\nDigite seu caso de uso (ou 'sair' para encerrar):")
    
    while True:
        use_case = input("\nCaso de Uso: ")
        
        if use_case.lower() == 'sair':
            break
            
        if use_case.strip():
            print("\nAnalisando seu caso de uso...\n")
            recommendation = recommender.analyze_use_case(use_case)
            print("Recomendação:")
            print(recommendation)
        else:
            print("Por favor, insira um caso de uso válido.")

if __name__ == "__main__":
    main() 