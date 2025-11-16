class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_nota(self, nota):
        """Adiciona uma nota à lista de notas do aluno"""
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print(f"Nota {nota} inválida! Deve estar entre 0 e 10.")
    
    def calcular_media(self):
        """Calcula a média das notas do aluno"""
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def verificar_situacao(self):
        """Verifica se o aluno foi aprovado ou reprovado"""
        media = self.calcular_media()
        
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
    
    def exibir_resultado(self):
        """Exibe o resultado completo do aluno"""
        media = self.calcular_media()
        situacao = self.verificar_situacao()
        
        print(f"\n{'='*40}")
        print(f"RESULTADO DO ALUNO: {self.nome}")
        print(f"{'='*40}")
        print(f"Notas: {self.notas}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        print(f"{'='*40}")


class SistemaEscolar:
    def __init__(self):
        self.alunos = []
    
    def cadastrar_aluno(self):
        """Cadastra um novo aluno e suas notas"""
        nome = input("\nDigite o nome do aluno: ")
        aluno = Aluno(nome)
        
        print(f"\nCadastrando notas para {nome}:")
        for i in range(3):
            while True:
                try:
                    nota = float(input(f"Digite a {i+1}ª nota: "))
                    aluno.adicionar_nota(nota)
                    break
                except ValueError:
                    print("Por favor, digite um número válido!")
        
        self.alunos.append(aluno)
        return aluno
    
    def exibir_todos_resultados(self):
        """Exibe os resultados de todos os alunos cadastrados"""
        if not self.alunos:
            print("\nNenhum aluno cadastrado!")
            return
        
        print(f"\n{'='*50}")
        print("RESULTADOS FINAIS - TODOS OS ALUNOS")
        print(f"{'='*50}")
        
        for aluno in self.alunos:
            media = aluno.calcular_media()
            situacao = aluno.verificar_situacao()
            print(f"{aluno.nome:<15} | Notas: {aluno.notas} | Média: {media:.2f} | {situacao}")


def main():
    """Função principal do sistema"""
    sistema = SistemaEscolar()
    
    while True:
        print("\n" + "="*50)
        print("SISTEMA ESCOLAR - CONTROLE DE NOTAS")
        print("="*50)
        print("1 - Cadastrar aluno")
        print("2 - Ver resultado de um aluno")
        print("3 - Ver todos os resultados")
        print("4 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            aluno = sistema.cadastrar_aluno()
            aluno.exibir_resultado()
            
        elif opcao == "2":
            if sistema.alunos:
                print("\nAlunos cadastrados:")
                for i, aluno in enumerate(sistema.alunos, 1):
                    print(f"{i} - {aluno.nome}")
                
                try:
                    indice = int(input("\nDigite o número do aluno: ")) - 1
                    if 0 <= indice < len(sistema.alunos):
                        sistema.alunos[indice].exibir_resultado()
                    else:
                        print("Número inválido!")
                except ValueError:
                    print("Por favor, digite um número válido!")
            else:
                print("\nNenhum aluno cadastrado!")
                
        elif opcao == "3":
            sistema.exibir_todos_resultados()
            
        elif opcao == "4":
            print("\nSaindo do sistema...")
            break
            
        else:
            print("\nOpção inválida! Tente novamente.")


# Executar o programa
if __name__ == "__main__":
    main()