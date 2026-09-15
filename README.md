# Som Dashboard (Controle de Áudio Remoto)

> **Módulo:** Automação Local e Interatividade.
> **Objetivo:** Aplicação web que funciona como um "Controle Remoto na Nuvem". Permite que usuários acionem efeitos sonoros e músicas através de um dashboard na internet. Os comandos são enviados para a nuvem e lidos quase instantaneamente por um script local que executa o áudio nas caixas de som físicas.

---

## Arquitetura e Fluxo de Dados

A solução é dividida entre o servidor web na nuvem e o executor de mídia local, conectados por um banco de dados que atua como "mensageria".

```mermaid
flowchart TD
    subgraph Nuvem_Railway [Servidor Web]
        App[app.py\nDashboard Flask]
        DB[(PostgreSQL\nTabela 'comando')]
    end

    subgraph Desktop_Local [Computador c/ Caixas de Som]
        Cliente[cliente_local.py\nLoop de Escuta]
        Player((Player Nativo\nWindows))
        MP3[Arquivos MP3\nArmazenamento Local]
    end

    Celular((Usuário)) -->|Clica no Botão| App
    App -->|1. Insere (nome do arquivo)| DB
    Cliente -.->|2. Polling (1 seg)| DB
    DB -->|3. Retorna novo ID| Cliente
    Cliente -->|4. Lê o caminho físico| MP3
    Cliente -->|5. Dispara Execução| Player
```

### Tecnologias Utilizadas
* **Dashboard (Backend Web):** Python (Flask) e HTML/CSS.
* **Mensageria/Fila:** PostgreSQL (Railway) servindo como ponte de comunicação assíncrona em tempo real.
* **Cliente Local (Desktop):** Script Python rodando em *loop* infinito, utilizando o comando `start` nativo do Windows para abrir o arquivo de áudio no player padrão sem bloquear a execução.

---

## Instalação e Execução

### 1. Servidor Web (Dashboard)
Responsável por exibir a interface e receber os comandos de toque.
```bash
cd SOM_DASHBOARD
pip install -r requirements.txt
python app.py
```
> O sistema está preparado para deploy no Railway (possui `Procfile` e o script `criar_tabela_comando.py` para setup inicial do banco de dados).

### 2. Cliente Local (Desktop)
Este script **deve rodar apenas no computador físico que está conectado aos alto-falantes**. 
Abra o arquivo `cliente_local.py` e certifique-se de que a variável `CAMINHO` aponta para a pasta real do seu computador onde os arquivos `.mp3` foram baixados.

```bash
python cliente_local.py
```
O console ficará aberto fazendo *polling* (verificando o banco) a cada 1 segundo e disparará o som assim que você apertar no celular/painel web.
