# TJPE PJE - Scripts de Automação

Conjunto de scripts Python para automação de processos no sistema PJE (Processo Judicial Eletrônico) do Tribunal de Justiça de Pernambuco (TJPE).

---

## 📋 Requisitos de Configuração

### 1. **Python**
- **Versão mínima:** Python 3.8 ou superior
- **Download:** https://www.python.org/downloads/
- **Verificar instalação:**
  ```bash
  python --version
  ```

### 2. **Google Chrome**
- **Versão:** Última versão estável
- **Download:** https://www.google.com/chrome/
- **Motivo:** Os scripts usam Selenium com WebDriver do Chrome

### 3. **ChromeDriver**
O ChromeDriver é essencial para que o Selenium controle o Chrome automaticamente.

#### **Opção 1: Instalação Automática (Recomendado)**
O package `webdriver-manager` faz isso automaticamente:
```bash
pip install webdriver-manager
```

#### **Opção 2: Instalação Manual**
1. Acesse: https://chromedriver.chromium.org/
2. Baixe a versão compatível com seu Chrome
3. Extraia o arquivo `chromedriver.exe`
4. Coloque em um dos caminhos:
   - Pasta do projeto
   - `C:\chromedriver\` (Windows)
   - Adicione à variável `PATH` do sistema

---

## 🛠️ Instalação de Dependências

### Passo 1: Abra o Prompt de Comando ou PowerShell

### Passo 2: Navegue até a pasta do projeto
```bash
cd C:\Users\[seu-usuario]\Desktop\TJPE_PJE
```

### Passo 3: Instale as dependências Python
```bash
pip install selenium webdriver-manager
```

Ou crie um arquivo `requirements.txt` com o conteúdo abaixo e execute:
```bash
pip install -r requirements.txt
```

**Conteúdo do requirements.txt:**
```
selenium>=4.0.0
webdriver-manager>=3.8.0
```

### Passo 4: Verifique a instalação
```bash
python -c "from selenium import webdriver; print('Selenium instalado com sucesso!')"
```

---

## 📁 Estrutura do Projeto

O projeto está organizado em dois grupos (1G e 2G), representando as classes processuais:

```
TJPE_PJE/
├── 1G/                              # Primeira Instância
│   ├── 1_consultaProcessualPublica.py
│   ├── 2_loginUsuarioSenha.py
│   ├── 3_pesquisaProcesso.py
│   ├── 4_downloaDeAutos.py
│   ├── 5_painelDoUsuario.py
│   └── 6_cadastroDeNovoProcesso.py
├── 2G/                              # Segunda Instância
│   ├── 1_consultaProcessualPublica.py
│   ├── 2_loginUsuarioSenha.py
│   ├── 3_pesquisaProcesso.py
│   ├── 4_downloaDeAutos.py
│   ├── 5_painelDoUsuario.py
│   └── 6_cadastroDeNovoProcesso.py
└── README.md
```

---

## 📝 Descrição dos Scripts

### **1_consultaProcessualPublica.py**
- **Objetivo:** Realiza consulta processual pública
- **Funcionalidade:** Acessa a consulta pública e busca por processos de uma parte
- **Requer login:** ❌ Não
- **Acesso:** https://homologacao-pje.app.tjpe.jus.br/

### **2_loginUsuarioSenha.py**
- **Objetivo:** Realiza login no sistema com usuário e senha
- **Funcionalidade:** Autentica um usuário no PJE
- **Requer credenciais:** ✅ Sim (CPF e Senha)
- **Acesso:** Após autenticação bem-sucedida

### **3_pesquisaProcesso.py**
- **Objetivo:** Pesquisa processos no sistema
- **Funcionalidade:** Localiza processos específicos após login
- **Requer login:** ✅ Sim
- **Acesso:** Painel de pesquisa de processos

### **4_downloaDeAutos.py**
- **Objetivo:** Baixa autos de processos
- **Funcionalidade:** Download de documentos processuais
- **Requer login:** ✅ Sim
- **Acesso:** Necessário acesso ao processo específico

### **5_painelDoUsuario.py**
- **Objetivo:** Acessa o painel do usuário
- **Funcionalidade:** Exibe o painel com informações pessoais
- **Requer login:** ✅ Sim
- **Acesso:** Menu > Painel > Painel do usuário

### **6_cadastroDeNovoProcesso.py**
- **Objetivo:** Cria novo processo no sistema
- **Funcionalidade:** Abre formulário para cadastro de novo processo
- **Requer login:** ✅ Sim
- **Acesso:** Menu > Processo > Novo processo

---

## 🚀 Como Executar os Scripts

### Método 1: Prompt de Comando / PowerShell

1. Abra o Prompt de Comando ou PowerShell
2. Navegue até a pasta desejada:
   ```bash
   cd C:\Users\[seu-usuario]\Desktop\TJPE_PJE\2G
   ```
3. Execute o script:
   ```bash
   python 1_consultaProcessualPublica.py
   ```

### Método 2: IDE (Visual Studio Code, PyCharm, etc.)

1. Abra a pasta do projeto em sua IDE
2. Selecione o script desejado
3. Clique em "Run" ou pressione `F5` (dependendo da IDE)

### Método 3: Duplo clique (se Python estiver no PATH)

1. Navegue até a pasta do script
2. Dê duplo clique no arquivo `.py` desejado

---

## ⚙️ Configurações Importantes

### **Tempo de Espera**
Os scripts usam `time.sleep()` para aguardar o carregamento de elementos. Se as páginas carregarem lentamente em sua conexão, ajuste os valores:

```python
time.sleep(2)      # Aumentar para time.sleep(3) ou mais
```

### **Credenciais**
⚠️ **SEGURANÇA:** As credenciais estão hardcoded nos scripts. Para uso em produção:

1. Crie um arquivo `config.py` com as credenciais
2. Leia as credenciais de variáveis de ambiente
3. Use um arquivo `.env` com a biblioteca `python-dotenv`

**Exemplo com .env:**
```
# .env
TJPE_USER=02112357417
TJPE_PASSWORD=sua_senha
```

```python
# Script
import os
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('TJPE_USER')
password = os.getenv('TJPE_PASSWORD')
```

### **Resolução de Tela**
Os scripts usam `--start-maximized` para maximizar a janela. Ajuste conforme necessário:

```python
chrome_options.add_argument("--width=1920")
chrome_options.add_argument("--height=1080")
```

---

## 🔧 Solução de Problemas

### **Erro: "ChromeDriver not found"**
- Instale `webdriver-manager`: `pip install webdriver-manager`
- Ou baixe manualmente do site oficial

### **Erro: "Module 'selenium' not found"**
- Instale Selenium: `pip install selenium`
- Verifique se o pip está no PATH

### **Erro: "Port 9222 already in use"**
- Feche outras instâncias do Chrome ou do script
- Reinicie seu computador

### **Página não carrega**
- Verifique sua conexão com a internet
- Aumente os valores de `time.sleep()`
- Verifique se a URL está acessível

### **Elementos não encontrados**
- A estrutura da página pode ter mudado
- Verifique os seletores (ID, XPATH, CLASS_NAME)
- Aumente o tempo de espera antes de buscar elementos

---

## 📚 Documentação Útil

- **Selenium Documentation:** https://www.selenium.dev/documentation/
- **WebDriver Manager:** https://github.com/SergeyPirogov/webdriver-manager-python
- **Python Official:** https://www.python.org/doc/
- **TJPE:** https://www.tjpe.jus.br/

---

## ⚠️ Avisos Importantes

1. **Confidencialidade:** Proteja suas credenciais. Nunca compartilhe senhas em repositórios públicos.
2. **Termos de Serviço:** Verifique se a automação é permitida pelos termos de uso do TJPE.
3. **Velocidade:** Os scripts esperam tempos fixos. Conexões lentas podem causar erros.
4. **Atualizações:** O TJPE pode atualizar a interface, invalidando os seletores.
5. **Logs:** Considere adicionar logging para rastrear execuções.

---

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique a seção de Solução de Problemas
2. Consulte a documentação do Selenium
3. Abra uma issue no repositório

---

**Versão:** 1.0  
**Última atualização:** 2026-06-16  
**Autores:** Equipe TJPE
