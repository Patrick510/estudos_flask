# EXERCICIOS PARA PROVA - ESTUDO

## 3. Página de upload de fotos:

Objetivo da atividade: Criar uma aplicação simples para fazer upload de imagens.

### Funcionalidades:

- Formulário para escolher o arquivo a partir do computador do usuário.
- Armazenar os arquivos enviados pelos usuários em uma pasta.
- Utilização de templates para formatar a página.- Retornar mensagens de sucesso ou falha na autenticação. Em caso de sucesso, deve-se retornar também o path de onde o arquivo foi armazenado no servidor.

### Dicas:

- Utilizar lista para armazenar os arquivos enviados.
- Usar o módulo datetime para registrar a data e hora do upload do arquivo.
- Criar um template básico com HTML e CSS para estilizar a página.
  Tempo: 30 minutos. Tempo não é longo, portanto, o foco deve ser em funcionalidades básicas.
  Aprendizado: O objetivo principal é praticar os conceitos aprendidos e explorar novas possibilidades com o Flask.
  Ferramentas: Recomenda-se utilizar um editor de código com suporte a Python e Flask, como o Visual Studio Code.
  Proibido usar Internet.

# Prova 6: Registro de Aulas

## Duração: 30 minutos

## Regras

Prova sem consulta à internet. O uso de anotações realizadas no caderno
durante as aulas é permitido. O caderno deve ser apresentado para o professor 24
horas antes do início da prova para análise.
Avaliação: O código será avaliado quanto à funcionalidade, organização, boas práticas
e uso correto dos conceitos estudados.

## Enunciado

### Você foi contratado para criar um protótipo funcional de uma aplicação web para o

registro de aulas ministradas. A aplicação deve permitir que o usuário visualize,
adicione e exclua registros de aulas. Utilize o framework Flask para implementar a
solução.

## Cenário

### O sistema deve conter uma interface inicial que exiba uma lista de aulas. Cada aula

contém os seguintes campos: ID, Matéria, Professor e Data. As aulas devem ser
exibidas em ordem cronológica. O sistema também deve permitir adicionar novos
registros de aulas e excluir registros existentes. As alterações devem ser refletidas na
interface principal.

## Tarefas

### 1. Crie uma estrutura de projeto Flask que inclua:

- Um arquivo principal (app.py) para a lógica da aplicação Flask.
- Uma pasta com o nome “templates” contendo os arquivos HTML.
- Uma pasta com o nome “static” (opcional) para incluir estilos CSS. CSS é opcional
  devido ao limite de tempo para realizar a prova.

## 2. Implemente as seguintes rotas:

- / (rota principal): Renderiza uma página HTML contendo a lista de registros. Cada
  registro deve conter um botão de “Excluir” associado a ele.
- /adicionar (método POST): Permite adicionar um novo registro à lista, recebendo os
  dados via formulário HTML.
- /excluir/<int:id>: Exclui um registro da lista com base no ID informado na URL.
  Dados da aplicação

### Exemplo inicial:

```
{"id": 1, "descricao": "Matemática", "quantidade": "Carlos", "localizacao": "2025-01-01"}
{"id": 2, "descricao": "História", "quantidade": "Ana", "localizacao": "2025-01-02"}
```

### Templates HTML

- index.html: Página principal que exibe a lista de registros em formato de tabela, com
  botões para excluir cada registro.
- adicionar.html: Página com um formulário HTML para adicionar um novo registro.

### Regras de implementação

- O ID dos registros deve ser gerado automaticamente (não repetido).
- Use o render_template para carregar os arquivos HTML.
- As alterações (adição ou exclusão) devem ser refletidas na página principal sem a
  necessidade de reiniciar a aplicação.

### Extras opcionais (se houver tempo)

- Adicione um botão para editar os dados de um registro.
- Utilize CSS para estilizar a tabela e o formulário.
- Adicione mensagens de feedback ao usuário após cada ação (ex.: 'Registro
  adicionado com sucesso!').

### Entrega

O projeto deve ser funcional e executável no servidor local Flask. O professor avaliará:

- Funcionamento correto das rotas e interação com os dados.
- Organização do código e uso adequado dos conceitos.
- Implementação das funcionalidades obrigatórias e, se possível, das opcionais.

Boa sorte!
