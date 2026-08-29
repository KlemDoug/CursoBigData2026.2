### 1\. Filtro de Números Pares e Ímpares
Crie uma função chamada `separar_pares_impares(lista_numeros)`.

  * Ela deve receber uma lista de números inteiros.
  * Dentro da função, crie duas novas listas: uma para os pares e outra para os ímpares.
  * Use um loop `for` para percorrer a `lista_numeros`.
  * A função deve retornar um dicionário com duas chaves, `'pares'` e `'impares'`, contendo as respectivas listas.

### 2\. Contador de Frequência de Palavras
Crie uma função chamada `contar_frequencia_palavras(texto)`.

  * Ela deve receber uma string (um parágrafo ou frase).
  * A função deve tratar todas as palavras como minúsculas (use `.lower()`) e pode usar `.split()` para separar o texto em uma lista de palavras.
  * Ela deve retornar um dicionário onde cada chave é uma palavra única e cada valor é o número de vezes que essa palavra apareceu no texto.

### 3\. Elementos em Comum (Interseção)
Crie uma função chamada `encontrar_elementos_comuns(lista1, lista2)`.

  * Ela deve receber duas listas.
  * A função deve retornar um set (conjunto) contendo apenas os elementos que existem em *ambas* as listas. (A conversão para `set` facilita muito isso).

### 4\. Agenda Telefônica
Crie um programa que funcione como uma agenda telefônica. O programa deve ter:

1.  Um dicionário principal (ex: `agenda = {}`).
2.  Uma função `adicionar_contato(agenda, nome, telefone)` que adiciona um par nome/telefone ao dicionário.
3.  Uma função `buscar_contato(agenda, nome)` que retorna o telefone do nome buscado (ou uma mensagem de "Não encontrado").
4.  Um loop `while True` principal que pergunta ao usuário o que ele quer fazer (adicionar, buscar, sair). O loop só deve parar quando o usuário digitar "sair".

### 5\. Agrupando Alunos por Nota
Crie uma função `agrupar_alunos_por_nota(dicionario_alunos)`.

  * Ela deve receber um dicionário onde a chave é o nome do aluno (string) e o valor é a sua nota (inteiro). Ex: `{'Ana': 9, 'Beto': 7, 'Carla': 9, 'Daniel': 7}`.
  * A função deve retornar um novo dicionário onde as chaves são as notas e os valores são listas dos alunos que tiraram aquela nota.
  * Resultado esperado para o exemplo: `{9: ['Ana', 'Carla'], 7: ['Beto', 'Daniel']}`.


### 6\. Carrinho de Compras com Estoque
Crie um programa que simule um carrinho de compras.

1.  Comece com um dicionário de `estoque` (aninhado):
    ```python
    estoque = {
        'maca': {'preco': 5.0, 'qtd': 100},
        'banana': {'preco': 2.0, 'qtd': 50}
    }
    ```
2.  Crie um `carrinho = {}` (dicionário vazio).
3.  Crie uma função `adicionar_ao_carrinho(produto, quantidade)` que:
      * Verifica se o `produto` existe no `estoque`.
      * Verifica se a `quantidade` pedida está disponível no `estoque`.
      * Se sim, adiciona ao `carrinho` (ex: `carrinho['maca'] = 2`) e subtrai do `estoque`.
      * Se não, imprime uma mensagem de erro.
4.  Use um loop `while` para pedir ao usuário o produto e a quantidade até que ele digite "finalizar".
5.  No final, crie uma função `calcular_total(carrinho, estoque)` que imprime o valor total da compra.

### 7\. Validador de Senha
Crie uma função `validar_senha(senha)`.

  * Ela deve receber uma string `senha`.
  * A função deve retornar `True` se a senha atender a todas as regras, e `False` caso contrário:
    1.  Ter pelo menos 8 caracteres.
    2.  Conter pelo menos um número (use `isdigit()`).
    3.  Conter pelo menos uma letra maiúscula (use `isupper()`).
    4.  Conter pelo menos uma letra minúscula (use `islower()`).
    5.  Conter pelo menos um caractere especial. (Dica: crie um `set` de especiais, ex: `especiais = {'!', '@', '#', '$', ...}` e verifique se algum caractere da senha está nesse set).