# Sistema de cadastro e remoção de lixo

Este projeto realiza o cadastro e a remoção dos lixos encontrados nos oceanos fornecidos pelos usuários, como plástico, vidro, metal e madeira, os tipos mais encontrados no ecossistema marítimo. O sistema garante que apenas itens não numéricos sejam adicionados ou removidos das respectivas listas.

## Membros
Rafael Porto Annunciato - 554939 \
Pedro Gustavo Schmitz Sécio - 555758

## Estrutura

### Funções Principais 
1. **adicao(opcao)**
    - Realiza o cadastro de um tipo de lixo especificado pelo usuário.
    - Chama a função **adicionar_lixo** passando o tipo de lixo e a lista correspondente.
2. **remocao(opcao)**
    - Realiza a remoção de um tipo de lixo especificado pelo usuário.
    - Chama a função **remover_lixo** passando o tipo de lixo e a lista correspondente.
3. **tipos_lixo(lista, buscar)**
    - Verifica se um item está presente na lista de tipos de lixo.

### Variáveis Globais
- **Opções:** Lista com os tipos de lixo permitidos ('plástico','vidro','metal','madeira')
- **Plástico, vidro, metal, madeira:** Listas que armazenam os lixos de cada tipo. 

### Loop Principal
- O programa fica em um loop contínuo, solicitando ao usuário o tipo de lixo e a ação desejada (adicionar ou remover).
- Força o usuário a digitar apenas os tipos de lixo presentes na lista **opcoes**.
- Após cada operação, pergunta se o usuário deseja ou não continuar.

## Uso
1. Executar
    - Ao executar o script, o usuário verá uma mensagem de boas-vindas.
    - O programa pedirá ao usuário para digitar o tipo de lixo e a ação desejada (Adicionar ou Remover).
2. Adicionar Lixo
    - Digite **Adicionar** quando solicitado para adicionar um lixo.
    - O programa solicitará o tipo de lixo a ser adicionado e garantirá que a entrada não seja numérica.
3. Remover Lixo
    - Digite **Remover** quando solicitado para remover um lixo.
    - O programa solicitará o tipo de lixo a ser removido e garantirá que a entrada não seja numérica.
4. Encerrar
    - Para encerrar o programa digite **não** no input perguntando se deseja continuar

### Exemplo 
```console
Bem Vindo!
Digite o tipo de lixo encontrado
-> plástico

O que deseja fazer hoje
Adicionar dados        
Remover dados
-> adicionar

Digite o lixo de plástico para ser adicionado: copo
['copo']

Deseja continuar: sim

Digite o tipo de lixo encontrado
-> plástico

O que deseja fazer hoje
Adicionar dados        
Remover dados
-> remover

Digite o lixo de plástico para ser removido: copo
[]

Deseja continuar: não
Obrigado pela visita
```
