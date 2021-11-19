# PoM: Penoso ou Mamãozinho 2.0

Penoso ou Mamãozinho, voltoou! Agora mais robusto, com mais funcionalidades e melhor estruturado. PoM é um fórum criado na disciplina de Engenharia de Software I, para os alunos se informarem e compartilharem informações sobre as disciplinas ofertadas pela UFMG. Cada disciplina possui uma página dedicada em que os alunos podem fazer comentários sobre a matéria, e compartilhar links de materiais úteis. Além disso, os comentários serão ordenados por um sistema de 'likes' e 'dislikes', dessa forma, os alunos podem achar os comentários mais relevantes de forma mais eficiente.

Agora, além de pesquisar as disciplinas e classificá-las como Penosas ou Melzinho na Chupeta, os estudantes poderão avaliar os professores que ministram as disciplinas, compartilhar arquivos em um espaço reservado para download e upload, mais segurança e personalização do seu perfil, sistema de denúncia de usuários nos comentários visando manter a integridade e respeito do fórum pela sua comunidade, diversas melhorias na interface e disponibilização ao público através do Heroku.

### Instalação

* Pode ser necessário conceder permissão de execução do script `pom`.
    ```bash
    chmod +x pom
    ```

1. Clone o repositório e vá à raiz do projeto
    ```bash
    git clone https://github.com/vfrezende/Penoso-ou-Mamaozinho-2.0.git
    cd Penoso-ou-Mamaozinho-2.0
    ```
2. Build as imagens dos containers
    ```bash
    ./pom build-container-frontend
    ./pom build-container-backend
    ```
3. Instale as dependências do frontend.
    ```bash
    ./pom install-frontend
    ```

### Execução

#### Frontend
* Para executar o frontend em modo desenvolvimento (irá executar `npm run serve`), rode:
    ```bash
    ./pom run-frontend
    ```
* Caso deseje buildar o frontend (irá executar `npm run build`), rode:
    ```bash
    ./pom build-frontend
    ```

#### Backend
* Para executar o backend, rode:
    ```bash
    ./pom run-backend
    ```

### Variáveis de Ambiente
1. Na raiz do projeto, rode o comando e altere as variáveis de ambiente necessárias no arquivo ```.env```.
    ```bash
    cp .env.example .env
    ```
2. Vá até a pasta do frontend, rode o comando e altere as variáveis de ambiente necessárias no arquivo ```.env```.
    ```bash
    cd frontend
    cp .env.example .env.development
    cp .env.example .env.production
    ```

### Backlog do Produto

#### Como um usuário do PoM, eu gostaria de poder fazer o download/upload de arquivos relacionados às disciplinas
* Inserir nova aba "Arquivos relacionados" no componente `CoursePage`
* Definir maneira de armazenamento dos arquivos
* Implementar maneira de armazenamento dos arquivos


#### Como um usuário do PoM, eu gostaria de ter a opção de reportar quaisquer publicações que considero inapropriadas
* Inserir opção Denunciar no componente `CommentBox`
* Inserir nova tabela `denuncias` ao banco de dados
* Criar model no ORM para a tabela `denuncias`
* Criar chamada na API para adicionar denúncias

#### Como um desenvolvedor do PoM, eu gostaria de incentivar os usuários a fazerem o primeiro comentário ou avaliação em novas disciplinas
* No componente `CoursePage`, adicionar mensagem “seja o primeiro a avaliar” quando não houver avaliações em uma disciplina
* No componente `CoursePage`, adicionar mensagem “seja o primeiro a comentar” quando não houver comentários na disciplina

#### Como um desenvolvedor, gostaria de que o PoM fosse facilmente transportado para diferentes ambientes
* Criar DockerFile para o PoM

#### Como um usuário, gostaria de ser informado sempre que eu não tiver acesso a um dado do PoM
* Criar componente `UnauthorizedPage`
* Para páginas com acesso restrito, renderizar o componente `UnauthorizedPage` para usuários não autorizados

#### Como um desenvolvedor, gostaria que o PoM estivesse livre de cadastros de robôs ou emails falsos
* Adicionar envio de confirmação de cadastro para novos usuários cadastrados
* Adicionar o campo `conta_confirmada` à tabela `users`.


### Backlog do Sprint #1

#### Como um desenvolvedor, eu gostaria de ter um ORM do banco de dados do PoM
* Definir biblioteca de ORM a ser adotada
* Criar models das tabelas: `comentario`, `users`, `disciplinas`, `gostei`, `nao_gostei`, `penoso`, `mamao`, `links`
* Criar models das views: `disciplinas_informacoes`, `comentarios_informacoes`, `links_informacoes`, `avaliacoes_disciplinas`, `avaliacoes_comentario`
* Modificar consultas da API para fazerem uso do ORM

#### Como um usuário do PoM, eu gostaria de poder editar meus dados cadastrados
* Criar componente `ProfilePage`
* Criar formulário permitindo editar imagem do perfil, senha e nome.
* Criar botões salvar/cancelar

#### Como um usuário, eu gostaria de poder apagar qualquer publicação que eu tenha feita no PoM
* Inserir botão Excluir no componente `CommentBox`
* Inserir novos endpoints na API, permitindo excluir comentários, arquivos e links.

#### Como um desenvolvedor do PoM, eu gostaria de informar aos usuários informações relevantes sobre o PoM
* Criar componente `footer`
* Adicionar icones redirecionáveis para as páginas do facebook e instagram do PoM
* Adicionar emails de contato do PoM


### Tecnologia:
* __Frontend__: vue.js
* __Banco de Dados__: PostgreSQL
* __Backend__: Python (Flask)

### Integrantes:
* Nathan Nogueira
* Wesley Paulino Fernandes Maciel
* Felipe Seppe de Faria
* Vitor Franco Rezende
