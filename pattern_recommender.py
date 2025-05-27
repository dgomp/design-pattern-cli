import os
from dotenv import load_dotenv
import json
from google.api_core import exceptions as google_exceptions
from model_manager import ModelManager

class PatternRecommender:
    def __init__(self, model_manager):
        self.model_manager = model_manager
        
        self.base_prompt = """
        Você é um especialista em Design Patterns. Analise o seguinte caso de uso e recomende os 3 Design Patterns mais apropriados.

        REGRAS IMPORTANTES:
        1. Você DEVE retornar EXATAMENTE 3 padrões
        2. A resposta DEVE ser APENAS um objeto JSON válido, sem nenhum texto adicional
        3. Os padrões devem ser ordenados do mais apropriado para o menos apropriado
        4. O valor de confiança deve ser um número entre 0 e 1 (ex: 0.85 para 85% de confiança)

        Caso de uso:
        {use_case}

        Retorne APENAS o JSON abaixo, substituindo os valores de exemplo pelos seus valores reais:
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

    def list_available_models(self):
        """Lista os modelos disponíveis usando o ModelManager."""
        return self.model_manager.list_available_models()

    def analyze_use_case(self, use_case: str) -> dict:
        try:
            prompt = self.base_prompt.format(use_case=use_case)
            
            response = self.model_manager.get_current_model().generate_content(prompt)
            
            if not response.text:
                return {'error': 'Resposta vazia da API'}
                
            try:
                # Tenta limpar a resposta para garantir que seja apenas JSON
                text = response.text.strip()
                # Remove qualquer texto antes do primeiro {
                start = text.find('{')
                if start == -1:
                    raise ValueError("Resposta não contém JSON válido")
                text = text[start:]
                # Remove qualquer texto depois do último }
                end = text.rfind('}')
                if end == -1:
                    raise ValueError("Resposta não contém JSON válido")
                text = text[:end+1]
                
                result = json.loads(text)
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
                        
                result['patterns'].sort(key=lambda x: x['confidence'], reverse=True)
                return result
                
            except json.JSONDecodeError as e:
                return {'error': f'Erro ao processar a resposta do modelo: {str(e)}'}
                
        except google_exceptions.ResourceExhausted:
            return {'error': 'Limite de requisições da API excedido. Por favor, tente novamente mais tarde.'}
        except google_exceptions.Unauthenticated:
            return {'error': 'Erro de autenticação. Verifique se sua chave API está correta.'}
        except google_exceptions.ServiceUnavailable:
            return {'error': 'Serviço temporariamente indisponível. Por favor, tente novamente mais tarde.'}
        except google_exceptions.GoogleAPIError as e:
            return {'error': f'Erro da API do Google: {str(e)}'}
        except Exception as e:
            return {'error': f'Erro ao processar a recomendação: {str(e)}'}