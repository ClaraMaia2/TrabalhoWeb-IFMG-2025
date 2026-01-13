# 🧘‍♀️ Sistema Web de Agendamentos – Massoterapia

## 📚 Trabalho Final – Programação Web  
Projeto desenvolvido como trabalho final da disciplina de **Programação Web**, com o objetivo de construir um sistema web completo utilizando conceitos de **CRUD**, **autenticação**, **controle de acesso por perfil** e **boas práticas com Django**.

---

## 🎯 Objetivo do Projeto

Desenvolver um sistema web funcional que permita o gerenciamento de usuários, serviços e agendamentos, aplicando na prática os conceitos estudados em sala de aula, como:

- Programação web com Django
- Autenticação e autorização
- Organização em apps
- Templates dinâmicos
- Persistência de dados com banco de dados relacional

---

## 👥 Equipe

- **Clara Araújo Maia**
- **Vinícius Perboar dos Santos Madruga**

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Django 5**
- **HTML5**
- **CSS3**
- **JavaScript**
- **SQLite** (banco de dados padrão do Django)
- **Google Fonts**

---

## 🔐 Funcionalidades Implementadas

### 1️⃣ Sistema de Autenticação
- Login de usuários
- Logout seguro
- Cadastro de novos usuários
- Recuperação de senha

### 2️⃣ Perfis de Usuário
O sistema possui **perfis diferenciados**, com controle de acesso baseado no tipo de usuário:

- **Usuário comum**
- **Terapeuta (admin/staff)**

As permissões e opções de navegação variam conforme o perfil.

### 3️⃣ Cadastros (CRUD)

O sistema conta com **mais de três cadastros**, atendendo aos requisitos do projeto:

- **Usuários**
- **Perfil do usuário** (dados pessoais)
- **Serviços**
- **Agendamentos**

Todas as operações básicas de CRUD são aplicadas conforme a necessidade do sistema.

### 4️⃣ Menu Dinâmico
O menu principal do sistema se adapta automaticamente de acordo com o usuário logado:

- Opções diferentes para usuários autenticados e não autenticados
- Funcionalidades exclusivas para terapeutas
- Links de login, cadastro, logout e agendamentos exibidos dinamicamente

### 5️⃣ Sistema de Agendamentos
- Criação de agendamentos por usuários
- Seleção de serviço, data e horário
- Bloqueio de horários já ocupados
- Visualização de:
  - **Meus agendamentos** (usuário)
  - **Todos os agendamentos** (terapeuta)

Os agendamentos são organizados por data e horário.

### 6️⃣ Interface e Usabilidade
- Layout consistente em todas as páginas
- Formulários estilizados
- Feedback visual para ações do usuário (login, logout, cadastro, etc.)
- Design responsivo e organizado

---

## 📂 Estrutura do Projeto (Resumo)

```
project/
│
├── accounts/ # Autenticação, cadastro e recuperação de senha
├── appointments/ # Agendamentos e serviços
├── core/ # Páginas principais
├── templates/ # Templates HTML
├── static/
│ ├── css/
│ ├── js/
│ └── img/
├── manage.py
└── db.sqlite3
```

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

```
gh repo clone ClaraMaia2/TrabalhoWeb-IFMG-2025
```

2. Crie e ative o ambiente virtual:

```
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```
pip install django
```

4. Execute as migrações:

```
python manage.py migrate
```

5. Inicie o servidor:

```
python manage.py runserver
```

6. Acesse no navegador:

```
http://localhost:8000/
```
