import os
from dotenv import load_dotenv
from model_manager import ModelManager
from pattern_recommender import PatternRecommender
from cli import CLI

def main():
    load_dotenv()
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("Erro: GOOGLE_API_KEY não encontrada nas variáveis de ambiente.")
        return

    try:
        model_manager = ModelManager(api_key)
        
        recommender = PatternRecommender(model_manager)
        
        cli = CLI(recommender, model_manager)
        cli.run()
        
    except Exception as e:
        print(f"Erro ao inicializar o sistema: {str(e)}")

if __name__ == "__main__":
    main() 