class CLI:
    def __init__(self, recommender, model_manager):
        self.recommender = recommender
        self.model_manager = model_manager

    def display_menu(self):
        print("\n=== Menu Principal ===")
        print("1. Recomendar padrão de design")
        print("2. Trocar modelo")
        print("3. Sair")
        return input("\nEscolha uma opção: ")

    def run(self):
        while True:
            choice = self.display_menu()
            
            if choice == "1":
                self.handle_recommendation()
            elif choice == "2":
                self.model_manager.list_available_models()
            elif choice == "3":
                print("\nEncerrando o programa...")
                break
            else:
                print("\nOpção inválida. Por favor, tente novamente.")

    def handle_recommendation(self):
        print("\n=== Recomendação de Padrão de Design ===")
        print("Descreva seu problema ou requisito:")
        problem = input("> ")
        
        if not problem.strip():
            print("\nPor favor, forneça uma descrição do problema.")
            return
            
        try:
            recommendation = self.recommender.analyze_use_case(problem)
            if 'error' in recommendation:
                print(f"\nErro: {recommendation['error']}")
                return
                
            print("\nRecomendação:")
            print("-" * 50)
            for pattern in recommendation['patterns']:
                print(f"\nPadrão: {pattern['name']}")
                print(f"Confiança: {pattern['confidence']*100:.1f}%")
                print(f"Explicação: {pattern['explanation']}")
                print()
                print(f"Implementação: {pattern['implementation']}")
                print("-" * 50)
        except Exception as e:
            print(f"\nErro ao obter recomendação: {str(e)}") 