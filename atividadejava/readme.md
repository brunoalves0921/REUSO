# Framework Simples em Java

Este é um framework simples para gerenciar entidades genéricas, permitindo operações CRUD (Create, Read, Update, Delete).  
A implementação usa **Java + Gradle**, aplicando conceitos de **POO, Generics** e boas práticas de desenvolvimento.

---

##  Dados do Aluno

- **Nome:** Jorge Bruno Costa Alves  
- **Matrícula:** 509718  
- **Curso:** Ciência da Computação  

---

##  Funcionalidades
✅ Cadastro de produtos  
✅ Listagem de produtos com ID  
✅ Busca de produtos pelo ID  
✅ Atualização de produtos  
✅ Remoção de produtos  
✅ Implementação com armazenamento em memória e arquivo  

---

##  Estrutura do Projeto
```
/atividadejava
├── src
│ ├── main
│ │ ├── java
│ │ │ ├── me
│ │ │ │ ├── bruno
│ │ │ │ │ ├── framework
│ │ │ │ │ │ ├── Main.java
│ │ │ │ │ │ ├── model
│ │ │ │ │ │ │ ├── Produto.java
│ │ │ │ │ │ ├── repository
│ │ │ │ │ │ │ ├── CrudRepository.java
│ │ │ │ │ │ │ ├── InMemoryRepository.java
│ │ │ │ │ │ │ ├── InFileRepository.java
├── build.gradle
├── settings.gradle
├── README.md
├── build/
```
---

##  Como Executar

### 1️⃣ **Instalar o Gradle** (se ainda não tiver)  
Baixe e instale o Gradle:  
🔗 [https://gradle.org/install/](https://gradle.org/install/)  

Ou use o **Gradle Wrapper**:  
```sh
gradle wrapper
```

### 2️⃣ Gerar o .jar executável
```sh
gradlew build
```

### 3️⃣ Executar a Aplicação
```sh
java -jar build/libs/FrameworkAtividade-1.0.0.jar
```
