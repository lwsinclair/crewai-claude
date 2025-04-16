# Integrando o MCP Server com Claude

Este documento explica como integrar o servidor MCP do CrewAI com o Claude Desktop.

## Pré-requisitos

1. Servidor MCP em execução (usando `python mcp/run_server.py` ou `source venv/bin/activate && python mcp/run_server.py`)
2. Claude Desktop instalado no seu computador

## Configuração do Claude Desktop

### Passo 1: Iniciar o MCP Server

Primeiro, certifique-se de que o servidor MCP está em execução:

```bash
cd /Users/pedro/Documents/projects/crewai
source venv/bin/activate
python mcp/run_server.py
```

O servidor deve estar rodando em http://0.0.0.0:8000 (ou http://localhost:8000)

### Passo 2: Configurar o MCP no Claude Desktop

1. Abra o Claude Desktop
2. Clique no menu de configurações (geralmente um ícone de engrenagem)
3. Vá para "Configurações" ou "Preferências"
4. Procure a seção "MCP" ou "Model Control Protocol"
5. Adicione um novo servidor MCP com:
   - Nome: CrewAI Tools
   - URL: http://localhost:8000
   - Permissões: Ative todas as permissões necessárias

### Passo 3: Verificar a Configuração

1. Inicie uma nova conversa no Claude Desktop
2. Digite `/mcp list` para visualizar os servidores MCP disponíveis
3. Você deve ver "CrewAI Tools" na lista
4. Digite `/mcp use CrewAI Tools` para usar este servidor MCP
5. Agora você pode usar os comandos `/tool` para acessar as ferramentas expostas pelo servidor MCP

## Ferramentas Disponíveis

O servidor MCP expõe as seguintes ferramentas:

1. **custom_tool**: A ferramenta personalizada do CrewAI (o nome real depende da configuração)
2. **web_search**: Pesquisa na web por informações
3. **data_analysis**: Analisa dados e fornece insights

## Exemplos de Uso

### Usando a Ferramenta de Pesquisa Web

```
/tool web_search
query: "CrewAI multi-agent systems"
num_results: 5
```

### Usando a Ferramenta de Análise de Dados

```
/tool data_analysis
data: "vendas mensais: jan=100, fev=120, mar=150, abr=130, mai=170"
analysis_type: "trends"
```

## Solução de Problemas

Se você encontrar problemas ao conectar o Claude Desktop ao servidor MCP:

1. Verifique se o servidor MCP está em execução
2. Certifique-se de que não há firewalls ou restrições de rede bloqueando a conexão
3. Verifique o URL do servidor MCP (tente usar `localhost` em vez de `0.0.0.0`)
4. Verifique os logs do servidor MCP para erros
5. Reinicie o Claude Desktop após configurar o servidor MCP