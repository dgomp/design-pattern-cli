from pattern_recommender import PatternRecommender

def main():
    print("=== Sistema de Recomendação de Padrões de Design ===")
    print("Digite seu caso de uso (ou 'sair' para encerrar):")
    
    try:
        recommender = PatternRecommender()
    except ValueError as e:
        print(f"\nErro: {str(e)}")
        return
    
    while True:
        use_case = input("\n> ")
        
        if use_case.lower() == 'sair':
            print("\nEncerrando o programa...")
            break
            
        if not use_case.strip():
            print("Por favor, digite um caso de uso válido.")
            continue
            
        try:
            result = recommender.analyze_use_case(use_case)
            
            if 'error' in result:
                print(f"\nErro: {result['error']}")
                continue
                
            print("\nRecomendações:")
            print("-" * 50)
            for pattern in result.get("patterns", []):
                confidence = pattern.get('confidence', 0)
                confidence_percent = f"{confidence * 100:.1f}%"
                print(f"\nPadrão: {pattern.get('name', 'N/A')}")
                print(f"Confiança: {confidence_percent}")
                print(f"Explicação: {pattern.get('explanation', 'N/A')}")
                print()
                if 'implementation' in pattern:
                    print(f"Implementação: {pattern['implementation']}")
                print("-" * 50)
                
        except Exception as e:
            print(f"\nErro inesperado: {str(e)}")

if __name__ == "__main__":
    main() 