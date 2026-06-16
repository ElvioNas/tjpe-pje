# 🚀 Guia Rápido de Início

## 5 Passos para Começar

### 1️⃣ Instale Python
- Baixe de: https://www.python.org/downloads/
- Marque **"Add Python to PATH"** durante a instalação
- Reinicie o computador

### 2️⃣ Instale Google Chrome
- Baixe de: https://www.google.com/chrome/
- Instale normalmente

### 3️⃣ Abra o Prompt de Comando
- Windows: `Win + R` → digite `cmd` → `Enter`
- PowerShell: `Win + X` → `Windows PowerShell` ou `Terminal`

### 4️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

Ou manualmente:
```bash
pip install selenium webdriver-manager
```

### 5️⃣ Execute um script
```bash
cd TJPE_PJE\2G
python 1_consultaProcessualPublica.py
```

---

## ✅ Verificar Instalação

```bash
# Verifica Python
python --version

# Verifica Selenium
python -c "from selenium import webdriver; print('OK')"

# Verifica pip
pip --version
```

---

## ❌ Erros Comuns e Soluções

| Erro | Solução |
|------|---------|
| "python: command not found" | Python não está no PATH. Reinstale marcando "Add to PATH" |
| "No module named selenium" | Execute: `pip install selenium` |
| "ChromeDriver not found" | Execute: `pip install webdriver-manager` |
| "Connection refused" | Verifique sua internet e a URL do TJPE |

---

## 📖 Próximas Etapas

1. Leia o **README.md** completo para todas as opções
2. Examine os scripts para entender o fluxo
3. Adapte conforme suas necessidades
4. Configure credenciais usando `.env` para segurança

---

**Precisa de ajuda?** Consulte o README.md completo!
