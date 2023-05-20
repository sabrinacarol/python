# Write in English my code
# git forever to move
# write to variavel drescritiveis
# USAR MAIS O TECLADO PC

# Git
- git status
- git -v (verifica se o git está instalado)
- git add (adiciona o arquivo para subir para o git.com )
- 

Subindo seu repositório no GitHub através da linha de comando
https://dev.to/alanfabricio/subindo-seu-repositorio-no-github-atraves-da-linha-de-comando-3kcm

projeto
Um passo a passo rápido para quem pretende subir o seu repositório no GitHub!
Tenha certeza que o seu git está instalado. 

- No terminal ou prompt de comando cheque através do comando git -v

- No GitHub, crie um novo repositório. 
- Na tela onde pede para fazer upload ou criar aquivos, guarde o link HTTPS que será geradoGitHub

- Abra o Git Bash ou terminal na pasta onde está o seu projeto

- Inicie a pasta como um repositório do Git através do comando:
git init

- Em seguida, adicione os arquivos de configuração para preparar o commit:
git add .

- Opcional: Adicione um arquivo readme caso não tenha iniciado o repositório com ele:
git add README.md

- Crie um novo commit para os arquivos que irá subir para o repositório:
git commit -m "first commit"

- Suba seus arquivos utilizando a URL gerada no passo 2 no seguinte comando:
git remote add origin URL-GERADA-PELO-PASSO-2-AQUI

- Autorize o upload com seu login e senha:
git push -u origin master