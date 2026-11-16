# 🧁 Avelino's Cupcake Store

> **Projeto Integrador Transdisciplinar em Engenharia de Software II (PIT II)**  
> **Instituição:** Cruzeiro do Sul Virtual  
> **Autor:** Raul Avelino  
> **Tecnologia Principal:** Python (Flask) + Bootstrap 5  

---

## 📋 Sobre o Projeto

O **Avelino's Cupcake Store** é uma plataforma e-commerce web desenvolvida para comercialização de cupcakes e kits artesanais. O sistema foi projetado seguindo o padrão arquitetonial **MVC (Model-View-Controller)**, garantindo a separação de responsabilidades entre a regra de negócio, a interface do usuário e o controle de dados.

O projeto atende aos requisitos práticos e teóricos das 3 Situações-Problema da disciplina de PIT II, englobando modelagem de banco de dados, desenvolvimento do front-end responsivo, lógica de back-end em Python e suíte de testes unitários.

---

## 🚀 Tecnologias Utilizadas

* **Back-end:** Python 3 (Framework Flask)
* **Front-end:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5, FontAwesome
* **Arquitetura:** MVC (Model-View-Controller)
* **Banco de Dados (Previsto):** SQLite / PostgreSQL
* **Hospedagem (Planejada):** Render
* **Testes Unitários:** Pytest
* **Controle de Versão:** Git / GitHub

---

## 📂 Estrutura do Projeto (Padrão MVC)

```text
avelinos-cupcake-store/
├── app/
│   ├── views/                  # (V) Camada de Apresentação
│   │   ├── static/
│   │   │   └── css/
│   │   │       └── style.css   # Estilização e identidade visual da loja
│   │   └── templates/
│   │       ├── base.html       # Layout base com Navbar e Gaveta do Carrinho (Offcanvas)
│   │       └── index.html      # Catálogo de produtos dinâmico
├── tests/                      # Suíte de Testes com Pytest
│   └── test_produtos.py
├── app.py                      # (C/M) Arquivo principal do servidor Flask e Rotas API
├── requirements.txt            # Dependências da aplicação
└── README.md                   # Documentação principal do repositório