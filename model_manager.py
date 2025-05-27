import google.generativeai as genai
import re

class ModelManager:
    def __init__(self, api_key: str):
        """Inicializa o gerenciador de modelos."""
        genai.configure(api_key=api_key)
        self.current_model = None
        self.set_latest_model()

    def _extract_date(self, model_name: str) -> str:
        """Extrai a data do nome do modelo."""
        date_match = re.search(r'(\d{2}-\d{2}|\d{4}-\d{2}-\d{2})', model_name)
        if date_match:
            return date_match.group(1)
        return "0000-00-00"

    def get_latest_model(self):
        """Retorna o nome do modelo mais recente disponível."""
        try:
            models = list(genai.list_models())
            models.sort(key=lambda x: self._extract_date(x.name), reverse=True)
            return models[0].name if models else None
            
        except Exception as e:
            print(f"Erro ao obter o modelo mais recente: {str(e)}")
            return None

    def set_latest_model(self):
        """Configura automaticamente o modelo mais recente."""
        latest_model = self.get_latest_model()
        if latest_model:
            print(f"\nConfigurando automaticamente o modelo mais recente: {latest_model}")
            return self.set_model(latest_model)
        return False

    def set_model(self, model_name: str):
        """Define o modelo a ser utilizado."""
        try:
            self.current_model = genai.GenerativeModel(
                model_name,
                generation_config=genai.GenerationConfig(
                    temperature=0.7,
                    top_p=0.95,
                    top_k=40
                )
            )
            return True
        except Exception as e:
            print(f"Erro ao configurar o modelo: {str(e)}")
            return False

    def get_current_model(self):
        """Retorna o modelo atual."""
        return self.current_model

    def list_available_models(self):
        """Lista todos os modelos disponíveis do Gemini e permite seleção."""
        try:
            models = list(genai.list_models())
            models.sort(key=lambda x: self._extract_date(x.name), reverse=True)
            
            print("\nModelos disponíveis (ordenados por data, mais recentes primeiro):")
            print("-" * 50)
            
            for i, model in enumerate(models, 1):
                print(f"\n{i}. Nome: {model.name}")
                print(f"   Descrição: {model.description}")
                print(f"   Display Name: {model.display_name}")
                print("-" * 50)
            
            while True:
                try:
                    choice = input("\nDigite o número do modelo desejado (ou 'cancelar' para manter o atual): ")
                    
                    if choice.lower() == 'cancelar':
                        print("\nOperação cancelada. Mantendo o modelo atual.")
                        return False
                    
                    index = int(choice) - 1
                    if 0 <= index < len(models):
                        selected_model = models[index]
                        print(f"\nModelo selecionado: {selected_model.display_name}")
                        
                        if self.set_model(selected_model.name):
                            print("Modelo configurado com sucesso!")
                            return True
                        else:
                            print("Falha ao configurar o modelo. Mantendo o modelo atual.")
                            return False
                    else:
                        print("\nNúmero inválido. Por favor, escolha um número da lista.")
                except ValueError:
                    print("\nEntrada inválida. Por favor, digite um número ou 'cancelar'.")
                    
        except Exception as e:
            print(f"Erro ao listar modelos: {str(e)}")
            return False 