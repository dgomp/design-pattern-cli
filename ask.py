import requests
import json

def main():
    print("=== Sistema de Recomendação de Padrões de Design ===")
    print("Digite seu caso de uso (ou 'sair' para encerrar):")
    
    while True:
        use_case = input("\n> ")
        
        if use_case.lower() == 'sair':
            print("\nEncerrando o programa...")
            break
            
        if not use_case.strip():
            print("Por favor, digite um caso de uso válido.")
            continue
            
        try:
            response = requests.post(
                "http://localhost:5000/recommend",
                json={"useCase": use_case},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
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
            else:
                print(f"\nErro: {response.json().get('error', 'Erro desconhecido')}")
                
        except requests.exceptions.ConnectionError:
            print("\nErro: Não foi possível conectar ao servidor. Certifique-se de que o servidor está rodando.")
            break
        except Exception as e:
            print(f"\nErro inesperado: {str(e)}")

if __name__ == "__main__":
    main() 