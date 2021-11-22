# PoM: Penoso ou Mamãozinho 2.0

Penoso ou Mamãozinho, voltoou! Agora mais robusto, com mais funcionalidades e melhor estruturado. PoM é um fórum criado na disciplina de Engenharia de Software I, para os alunos se informarem e compartilharem informações sobre as disciplinas ofertadas pela UFMG. Cada disciplina possui uma página dedicada em que os alunos podem fazer comentários sobre a matéria, e compartilhar links de materiais úteis. Além disso, os comentários serão ordenados por um sistema de 'likes' e 'dislikes', dessa forma, os alunos podem achar os comentários mais relevantes de forma mais eficiente.

Agora, além de pesquisar as disciplinas e classificá-las como Penosas ou Melzinho na Chupeta, os estudantes poderão avaliar os professores que ministram as disciplinas, compartilhar arquivos em um espaço reservado para download e upload, mais segurança e personalização do seu perfil, sistema de denúncia de usuários nos comentários visando manter a integridade e respeito do fórum pela sua comunidade, diversas melhorias na interface e disponibilização ao público através do Heroku.

## Backlog movido para o [GitHub Projects](https://github.com/vfrezende/Penoso-ou-Mamaozinho-2.0/projects/1)

### Tecnologia:
* __Frontend__: vue.js
* __Banco de Dados__: PostgreSQL
* __Backend__: Python (Flask)

### Integrantes:
* Nathan Nogueira
* Wesley Paulino Fernandes Maciel
* Felipe Seppe de Faria
* Vitor Franco Rezende
* 
### Instalação

    * Certifique-se que o Docker esteje instalado em sua maquina. Caso não esteja, siga o tutorial abaixo:
    ```bash
        https://docs.docker.com/get-docker/
    ```
1. Clone o repositório e vá à raiz do projeto
    * Pode ser necessário conceder permissão de execução do script `pom`.
    ```bash
    chmod +x pom
    ```
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
