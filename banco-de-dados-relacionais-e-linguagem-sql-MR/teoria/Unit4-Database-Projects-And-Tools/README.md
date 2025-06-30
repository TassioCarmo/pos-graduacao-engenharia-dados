# Projeto de Banco de Dados: Metodologia e Implementação

Este documento apresenta os principais elementos a serem considerados no desenvolvimento de um projeto de banco de dados SQL, demonstrando recursos disponíveis e detalhando as etapas metodológicas para sua execução eficiente.

## Sumário

1. [O Projeto de Banco de Dados e sua Integração com os Sistemas](#o-projeto-de-banco-de-dados-e-sua-integração-com-os-sistemas)
2. [Modelagem de Dados Orientada a Objetos](#modelagem-de-dados-orientada-a-objetos)
3. [Ferramentas de Projeto Automatizado de Banco de Dados](#ferramentas-de-projeto-automatizado-de-banco-de-dados)
4. [Construção de Projeto de Banco de Dados Relacional](#construção-de-projeto-de-banco-de-dados-relacional)

## O Projeto de Banco de Dados e sua Integração com os Sistemas

### Visão Geral (Overview)

O projeto de banco de dados é uma etapa fundamental no desenvolvimento de sistemas de informação, estabelecendo como os dados serão organizados, armazenados e acessados para atender às necessidades do negócio.

### Ciclo de Vida do Projeto de Banco de Dados (Database Project Lifecycle)

1. **Planejamento (Planning)**
   - Definição de escopo
   - Análise de requisitos
   - Alocação de recursos
   - Cronograma de implementação

2. **Análise de Requisitos (Requirements Analysis)**
   - Identificação de requisitos de dados
   - Determinação de volumes e frequência de acesso
   - Definição de requisitos de desempenho e segurança

3. **Projeto Conceitual (Conceptual Design)**
   - Criação de modelo entidade-relacionamento (ER)
   - Definição de entidades, atributos e relacionamentos

4. **Projeto Lógico (Logical Design)**
   - Transformação do modelo conceitual para modelo relacional
   - Normalização de tabelas
   - Definição de chaves primárias e estrangeiras

5. **Projeto Físico (Physical Design)**
   - Mapeamento para estruturas físicas de armazenamento
   - Definição de índices e estratégias de otimização
   - Planejamento de particionamento e clustering

6. **Implementação (Implementation)**
   - Criação de esquemas e tabelas
   - Implementação de restrições e regras
   - Povoamento inicial de dados

7. **Testes (Testing)**
   - Validação da integridade dos dados
   - Testes de desempenho
   - Simulação de carga

8. **Implantação e Manutenção (Deployment and Maintenance)**
   - Migração para ambiente de produção
   - Monitoramento de desempenho
   - Manutenção e atualização contínuas

### Integração com Sistemas (System Integration)

A integração eficiente do banco de dados com os sistemas que o utilizam é crucial para o sucesso do projeto:

#### Camadas de Integração (Integration Layers)

```
+---------------------------+
|    Interface do Usuário   |
|      (User Interface)     |
+---------------------------+
              |
+---------------------------+
|    Lógica de Negócio      |
|   (Business Logic)        |
+---------------------------+
              |
+---------------------------+
|    Camada de Acesso       |
|    (Data Access Layer)    |
+---------------------------+
              |
+---------------------------+
|    Banco de Dados         |
|    (Database)             |
+---------------------------+
```

#### Padrões de Acesso a Dados (Data Access Patterns)

1. **ORM (Object-Relational Mapping)**
   - Mapeia objetos de programação para tabelas relacionais
   - Exemplo: Hibernate, Entity Framework, JPA

   ```java
   // Exemplo de mapeamento usando JPA
   @Entity
   @Table(name = "clientes")
   public class Cliente {
       @Id
       @GeneratedValue(strategy = GenerationType.IDENTITY)
       private Long id;
       
       @Column(name = "nome", nullable = false)
       private String nome;
       
       @OneToMany(mappedBy = "cliente", cascade = CascadeType.ALL)
       private List<Pedido> pedidos;
       
       // Getters e setters
   }
   ```

2. **DAO (Data Access Object)**
   - Encapsula a lógica de acesso ao banco de dados
   - Oferece métodos específicos para operações CRUD

   ```java
   public class ClienteDAO {
       private Connection conn;
       
       public ClienteDAO(Connection conn) {
           this.conn = conn;
       }
       
       public Cliente findById(Long id) throws SQLException {
           String sql = "SELECT * FROM clientes WHERE id = ?";
           PreparedStatement stmt = conn.prepareStatement(sql);
           stmt.setLong(1, id);
           ResultSet rs = stmt.executeQuery();
           
           if (rs.next()) {
               Cliente cliente = new Cliente();
               cliente.setId(rs.getLong("id"));
               cliente.setNome(rs.getString("nome"));
               return cliente;
           }
           return null;
       }
       
       // Outros métodos CRUD
   }
   ```

3. **API REST**
   - Interfaces RESTful para acesso a dados
   - Comunicação via JSON/XML entre sistemas

   ```java
   @RestController
   @RequestMapping("/api/clientes")
   public class ClienteController {
       @Autowired
       private ClienteService clienteService;
       
       @GetMapping("/{id}")
       public ResponseEntity<Cliente> getClienteById(@PathVariable Long id) {
           Cliente cliente = clienteService.findById(id);
           if (cliente != null) {
               return ResponseEntity.ok(cliente);
           }
           return ResponseEntity.notFound().build();
       }
       
       // Outros endpoints
   }
   ```

#### Considerações para Integração (Integration Considerations)

- **Performance**: Otimização de consultas, uso adequado de índices
- **Escalabilidade**: Capacidade de lidar com crescimento de dados e usuários
- **Segurança**: Proteção contra injeção SQL e uso de credenciais seguras
- **Transações**: Garantia de consistência em operações complexas
- **Cache**: Estratégias de cache para reduzir carga no banco de dados

## Modelagem de Dados Orientada a Objetos

### Conceitos Fundamentais (Fundamental Concepts)

A modelagem de dados orientada a objetos (OODB - Object-Oriented Database) adapta os conceitos da programação orientada a objetos para o contexto de bancos de dados, permitindo representar entidades complexas com comportamentos e relacionamentos hierárquicos.

### Principais Características (Key Features)

1. **Encapsulamento (Encapsulation)**
   - Agrupa dados e comportamentos em unidades coesas (objetos)
   - Oculta detalhes de implementação interna

2. **Herança (Inheritance)**
   - Permite que classes derivadas herdem atributos e métodos de classes base
   - Facilita a reutilização de código e a modelagem hierárquica

3. **Polimorfismo (Polymorphism)**
   - Permite que objetos de diferentes classes sejam tratados de maneira uniforme
   - Flexibiliza o design e facilita extensões futuras

4. **Identidade de Objeto (Object Identity)**
   - Cada objeto possui um identificador único independente de seus valores
   - Permite referências e relacionamentos complexos

### UML na Modelagem de Dados (UML in Data Modeling)

O UML (Unified Modeling Language) é amplamente utilizado para modelar bancos de dados orientados a objetos:

#### Diagrama de Classes (Class Diagram)

```
+------------------+        +-------------------+
|     Cliente      |        |      Pedido       |
+------------------+        +-------------------+
| -id: Long        |<>------| -id: Long         |
| -nome: String    |1     n | -data: Date       |
| -email: String   |        | -valorTotal: Float|
+------------------+        +-------------------+
| +fazerPedido()   |        | +adicionarItem()  |
| +atualizarDados()|        | +calcularTotal()  |
+------------------+        +-------------------+
                              ^
                              |
                    +-----------------+
                    |  PedidoEspecial |
                    +-----------------+
                    | -desconto: Float|
                    +-----------------+
                    | +aplicarDesconto|
                    +-----------------+
```

### Mapeamento Objeto-Relacional (Object-Relational Mapping)

O mapeamento objeto-relacional (ORM) resolve o problema da incompatibilidade de paradigmas entre a orientação a objetos e o modelo relacional:

#### Estratégias de Mapeamento (Mapping Strategies)

1. **Mapeamento de Classes para Tabelas**

```sql
-- Classe Cliente mapeada para tabela
CREATE TABLE clientes (
    id BIGINT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);
```

2. **Mapeamento de Herança**

```sql
-- Estratégia de tabela única (Single Table Inheritance)
CREATE TABLE pedidos (
    id BIGINT PRIMARY KEY,
    data DATE NOT NULL,
    valor_total DECIMAL(10,2),
    tipo VARCHAR(20), -- 'NORMAL' ou 'ESPECIAL'
    desconto DECIMAL(5,2) NULL -- apenas para pedidos especiais
);

-- Alternativa: Estratégia de tabela por classe (Table Per Class)
CREATE TABLE pedidos (
    id BIGINT PRIMARY KEY,
    data DATE NOT NULL,
    valor_total DECIMAL(10,2)
);

CREATE TABLE pedidos_especiais (
    id BIGINT PRIMARY KEY REFERENCES pedidos(id),
    desconto DECIMAL(5,2) NOT NULL
);
```

3. **Mapeamento de Relacionamentos**

```sql
-- Relacionamento um-para-muitos entre Cliente e Pedido
CREATE TABLE pedidos (
    id BIGINT PRIMARY KEY,
    data DATE NOT NULL,
    valor_total DECIMAL(10,2),
    cliente_id BIGINT REFERENCES clientes(id)
);

-- Relacionamento muitos-para-muitos
CREATE TABLE produtos (
    id BIGINT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2)
);

CREATE TABLE itens_pedido (
    pedido_id BIGINT REFERENCES pedidos(id),
    produto_id BIGINT REFERENCES produtos(id),
    quantidade INTEGER NOT NULL,
    preco_unitario DECIMAL(10,2),
    PRIMARY KEY (pedido_id, produto_id)
);
```

### Bancos de Dados Objeto-Relacionais (Object-Relational Databases)

Sistemas como Oracle, PostgreSQL e SQL Server implementam extensões objeto-relacionais:

```sql
-- Exemplo PostgreSQL: Criação de tipo composto
CREATE TYPE endereco AS (
    rua VARCHAR(100),
    numero INTEGER,
    cidade VARCHAR(50),
    cep VARCHAR(10)
);

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    contato endereco
);

-- Utilizando o tipo
INSERT INTO clientes VALUES (1, 'João Silva', ROW('Rua A', 123, 'São Paulo', '01234-567'));
```

## Ferramentas de Projeto Automatizado de Banco de Dados

### CASE Tools (Computer-Aided Software Engineering)

Ferramentas CASE auxiliam no processo de design, implementação e manutenção de bancos de dados:

#### Principais Categorias (Main Categories)

1. **Modelagem Conceitual e Lógica (Conceptual and Logical Modeling)**
   - **Exemplos**: ERwin Data Modeler, MySQL Workbench, Lucidchart
   - **Funcionalidades**: Criação de diagramas ER, definição de entidades e relacionamentos

2. **Engenharia Reversa (Reverse Engineering)**
   - **Exemplos**: Navicat, DBeaver, SchemaSpy
   - **Funcionalidades**: Análise de bancos existentes, geração de documentação e diagramas

3. **Geração de Código (Code Generation)**
   - **Exemplos**: JHipster, Entity Framework
   - **Funcionalidades**: Transformação de modelos em scripts SQL ou código de acesso

4. **Administração e Monitoramento (Administration and Monitoring)**
   - **Exemplos**: pgAdmin, SQL Server Management Studio, Oracle Enterprise Manager
   - **Funcionalidades**: Administração, monitoramento de performance, otimização

### Comparativo de Ferramentas Populares (Popular Tools Comparison)

| **Ferramenta (Tool)** | **Tipo (Type)** | **Plataformas (Platforms)** | **Recursos Principais (Key Features)** |
|------------------------|-----------------|----------------------------|----------------------------------------|
| MySQL Workbench        | Modelagem/Administração | Windows, macOS, Linux | Modelagem visual, engenharia reversa, administração de servidor |
| ERwin Data Modeler     | Modelagem Empresarial | Windows | Modelagem lógica/física, gerenciamento de metadados, colaboração |
| Lucidchart             | Diagramação online | Web | Colaboração em tempo real, diversos tipos de diagramas, integrações |
| Navicat               | Gerenciamento de BD | Windows, macOS, Linux | Multi-SGBD, transferência de dados, sincronização |
| Visual Paradigm       | Modelagem UML/BD | Windows, macOS, Linux | UML completo, geração de código, documentação |
| DBeaver               | Gerenciamento de BD | Windows, macOS, Linux | Multiplataforma, open-source, suporte a diversos SGBDs |
| DbSchema              | Modelagem visual | Windows, macOS, Linux | Diagramas interativos, documentação visual, controle de versão |
| Oracle SQL Developer Data Modeler | Modelagem | Windows, macOS, Linux | Engenharia avançada, modelagem multidimensional, relatórios |

### Funcionalidades Essenciais (Essential Features)

1. **Forward Engineering**
   - Transformação de modelos conceituais/lógicos em scripts SQL
   
   ```sql
   -- Script gerado automaticamente a partir de um modelo
   CREATE TABLE clientes (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nome VARCHAR(100) NOT NULL,
       email VARCHAR(100) UNIQUE,
       data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   
   CREATE TABLE pedidos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       cliente_id INT NOT NULL,
       data_pedido DATETIME NOT NULL,
       valor_total DECIMAL(10,2),
       CONSTRAINT fk_cliente FOREIGN KEY (cliente_id) 
       REFERENCES clientes(id) ON DELETE RESTRICT
   );
   ```

2. **Reverse Engineering**
   - Geração de modelos a partir de bancos existentes
   - Exemplo: Código para extrair estrutura do banco em ferramentas programáticas

   ```java
   // Exemplo simplificado de engenharia reversa programática
   public class DatabaseReverseEngineer {
       public static void extractSchema(Connection conn) throws SQLException {
           DatabaseMetaData metaData = conn.getMetaData();
           
           // Obter tabelas
           ResultSet tables = metaData.getTables(null, null, "%", new String[]{"TABLE"});
           while (tables.next()) {
               String tableName = tables.getString("TABLE_NAME");
               System.out.println("Tabela: " + tableName);
               
               // Obter colunas
               ResultSet columns = metaData.getColumns(null, null, tableName, "%");
               while (columns.next()) {
                   String columnName = columns.getString("COLUMN_NAME");
                   String dataType = columns.getString("TYPE_NAME");
                   System.out.println("  Coluna: " + columnName + " (" + dataType + ")");
               }
               
               // Obter chaves primárias
               ResultSet primaryKeys = metaData.getPrimaryKeys(null, null, tableName);
               while (primaryKeys.next()) {
                   String pkName = primaryKeys.getString("COLUMN_NAME");
                   System.out.println("  PK: " + pkName);
               }
           }
       }
   }
   ```

3. **Sincronização de Modelo e Banco (Model-Database Synchronization)**
   - Comparação e atualização de diferenças entre modelo e banco
   - Geração de scripts de alteração

   ```sql
   -- Script de alteração gerado automaticamente
   -- para sincronizar o banco com o modelo atualizado
   ALTER TABLE clientes
   ADD COLUMN telefone VARCHAR(20) AFTER email;
   
   ALTER TABLE pedidos
   MODIFY COLUMN valor_total DECIMAL(12,2) NOT NULL;
   ```

4. **Versionamento e Controle de Mudanças (Versioning and Change Control)**
   - Comparação entre versões de modelos
   - Registro de alterações e histórico

## Construção de Projeto de Banco de Dados Relacional

### Metodologia de Projeto (Project Methodology)

Uma abordagem estruturada para o desenvolvimento de bancos de dados relacionais envolve as seguintes etapas:

#### 1. Levantamento de Requisitos (Requirements Gathering)

- **Entrevistas com stakeholders**
- **Análise de documentação existente**
- **Identificação de casos de uso**

Exemplo de documento de requisitos:

```
REQUISITOS DE DADOS - SISTEMA DE GESTÃO DE BIBLIOTECA

1. ENTIDADES PRINCIPAIS:
   - Livros: ISBN, título, autor(es), editora, ano publicação, categoria
   - Usuários: ID, nome, email, telefone, endereço, tipo (estudante/professor)
   - Empréstimos: ID, data empréstimo, data devolução prevista, data devolução efetiva
   
2. REGRAS DE NEGÓCIO:
   - Estudantes podem emprestar até 3 livros por 15 dias
   - Professores podem emprestar até 5 livros por 30 dias
   - Multa por atraso: R$1,00 por dia de atraso por livro
   
3. CONSULTAS FREQUENTES:
   - Livros disponíveis por categoria
   - Histórico de empréstimos por usuário
   - Relatório de livros atrasados
```

#### 2. Modelo Conceitual (Conceptual Model)

Diagramas ER representando entidades e relacionamentos:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
    <!-- Entidade Livro -->
    <rect x="50" y="150" width="200" height="120" fill="#e1f5fe" stroke="#0277bd" stroke-width="2" />
    <text x="150" y="180" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold">LIVRO</text>
    <line x1="50" y1="190" x2="250" y2="190" stroke="#0277bd" stroke-width="1" />
    <text x="60" y="210" font-family="Arial" font-size="12">ISBN (PK)</text>
    <text x="60" y="230" font-family="Arial" font-size="12">Título</text>
    <text x="60" y="250" font-family="Arial" font-size="12">Ano_Publicacao</text>

    <!-- Entidade Usuário -->
    <rect x="550" y="150" width="200" height="120" fill="#e8f5e9" stroke="#2e7d32" stroke-width="2" />
    <text x="650" y="180" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold">USUÁRIO</text>
    <line x1="550" y1="190" x2="750" y2="190" stroke="#2e7d32" stroke-width="1" />
    <text x="560" y="210" font-family="Arial" font-size="12">ID_Usuario (PK)</text>
    <text x="560" y="230" font-family="Arial" font-size="12">Nome</text>
    <text x="560" y="250" font-family="Arial" font-size="12">Email</text>

    <!-- Entidade Empréstimo -->
    <rect x="300" y="350" width="200" height="120" fill="#fff3e0" stroke="#ef6c00" stroke-width="2" />
    <text x="400" y="380" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold">EMPRÉSTIMO</text>
    <line x1="300" y1="390" x2="500" y2="390" stroke="#ef6c00" stroke-width="1" />
    <text x="310" y="410" font-family="Arial" font-size="12">ID_Emprestimo (PK)</text>
    <text x="310" y="430" font-family="Arial" font-size="12">Data_Emprestimo</text>
    <text x="310" y="450" font-family="Arial" font-size="12">Data_Devolucao_Prevista</text>

    <!-- Relacionamentos -->
    <line x1="250" y1="210" x2="300" y2="350" stroke="#666" stroke-width="2" />
    <line x1="550" y1="210" x2="500" y2="350" stroke="#666" stroke-width="2" />
    
    <!-- Losangos de relacionamento -->
    <polygon points="275,280 290,265 305,280 290,295" fill="#e0e0e0" stroke="#666" stroke-width="2" />
    <text x="290" y="282" text-anchor="middle" font-family="Arial" font-size="12">Tem</text>
    
    <polygon points="525,280 510,265 495,280 510,295" fill="#e0e0e0" stroke="#666" stroke-width="2" />
    <text x="510" y="282" text-anchor="middle" font-family="Arial" font-size="12">Realiza</text>
    
    <!-- Cardinalidades -->
    <text x="260" y="245" font-family="Arial" font-size="12">1</text>
    <text x="290" y="330" font-family="Arial" font-size="12">N</text>
    <text x="540" y="245" font-family="Arial" font-size="12">1</text>
    <text x="510" y="330" font-family="Arial" font-size="12">N</text>
    
    <!-- Entidade Autor -->
    <rect x="50" y="350" width="180" height="100" fill="#e8eaf6" stroke="#3f51b5" stroke-width="2" />
    <text x="140" y="380" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold">AUTOR</text>
    <line x1="50" y1="390" x2="230" y2="390" stroke="#3f51b5" stroke-width="1" />
    <text x="60" y="410" font-family="Arial" font-size="12">ID_Autor (PK)</text>
    <text x="60" y="430" font-family="Arial" font-size="12">Nome</text>
    
    <!-- Relacionamento Livro-Autor -->
    <line x1="140" y1="270" x2="140" y2="350" stroke="#666" stroke-width="2" />
    <polygon points="140,310 125,295 155,295" fill="#e0e0e0" stroke="#666" stroke-width="2" />
    <text x="140" y="310" text-anchor="middle" font-family="Arial" font-size="12">Escrito por</text>
    <text x="130" y="280" font-family="Arial" font-size="12">N</text>
    <text x="130" y="340" font-family="Arial" font-size="12">M</text>
</svg>

```

#### 3. Modelo Lógico (Logical Model)

Transformação para o modelo relacional:

```text
LIVROS (
    ISBN VARCHAR(13) PK,
    titulo VARCHAR(200) NOT NULL,
    ano_publicacao INTEGER,
    editora_id INTEGER FK REFERENCES EDITORAS(id),
    categoria_id INTEGER FK REFERENCES CATEGORIAS(id)
)

AUTORES (
    id INTEGER PK,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50)
)

LIVRO_AUTOR (
    isbn VARCHAR(13) FK REFERENCES LIVROS(ISBN),
    autor_id INTEGER FK REFERENCES AUTORES(id),
    PRIMARY KEY (isbn, autor_id)
)

USUARIOS (
    id INTEGER PK,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    tipo CHAR(1) CHECK (tipo IN ('E', 'P')), -- E=Estudante, P=Professor
    data_cadastro DATE DEFAULT CURRENT_DATE
)

EMPRESTIMOS (
    id INTEGER PK,
    usuario_id INTEGER FK REFERENCES USUARIOS(id),
    livro_isbn VARCHAR(13) FK REFERENCES LIVROS(ISBN),
    data_emprestimo DATE NOT NULL,
    data_devolucao_prevista DATE NOT NULL,
    data_devolucao_efetiva DATE,
    multa DECIMAL(10,2) DEFAULT 0.00
)

CATEGORIAS (
    id INTEGER PK,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descricao VARCHAR(200)
)

EDITORAS (
    id INTEGER PK,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200),
    telefone VARCHAR(20)
)

```

#### 4. Normalização (Normalization)

Processo de organização de dados para reduzir redundância e melhorar a integridade:

**1ª Forma Normal (1NF)**
- Eliminar grupos repetitivos
- Identificar chave primária
- Cada coluna contém apenas valores atômicos

**2ª Forma Normal (2NF)**
- Deve estar na 1NF
- Todos os atributos não-chave dependem totalmente da chave primária

**3ª Forma Normal (3NF)**
- Deve estar na 2NF
- Nenhum atributo não-chave depende transitivamente de outro atributo não-chave

Exemplo de normalização:

```
# Dados não normalizados
EMPRESTIMO (id, usuario_nome, usuario_email, livro_titulo, livro_isbn, data_emprestimo, data_devolucao)

# Após normalização
USUARIOS (id, nome, email)
LIVROS (isbn, titulo)
EMPRESTIMOS (id, usuario_id, livro_isbn, data_emprestimo, data_devolucao)
```

#### 5. Modelo Físico (Physical Model)

Implementação em SQL específico para o SGBD escolhido:

```sql
-- Criação do banco de dados
CREATE DATABASE biblioteca CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE biblioteca;

-- Tabela de Categorias
CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descricao VARCHAR(200)
) ENGINE=InnoDB;

-- Tabela de Editoras
CREATE TABLE editoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200),
    telefone VARCHAR(20)
) ENGINE=InnoDB;

-- Tabela de Livros
CREATE TABLE livros (
    isbn VARCHAR(13) PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    ano_publicacao INT,
    editora_id INT,
    categoria_id INT,
    exemplares_totais INT DEFAULT 1,
    exemplares_disponiveis INT DEFAULT 1,
    FOREIGN KEY (editora_id) REFERENCES editoras(id) ON DELETE SET NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE SET NULL,
    CHECK (exemplares_disponiveis <= exemplares_totais)
) ENGINE=InnoDB;

-- Tabela de Autores
CREATE TABLE autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50)
) ENGINE=InnoDB;

-- Tabela de relacionamento entre Livros e Autores (N:M)
CREATE TABLE livro_autor (
    isbn VARCHAR(13),
    autor_id INT,
    PRIMARY KEY (isbn, autor_id),
    FOREIGN KEY (isbn) REFERENCES livros(isbn) ON DELETE CASCADE,
    FOREIGN KEY (autor_id) REFERENCES autores(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Tabela de Usuários
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    tipo ENUM('E', 'P') NOT NULL COMMENT 'E=Estudante, P=Professor',
    data_cadastro DATE DEFAULT CURRENT_DATE,
    ativo BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Tabela de Empréstimos
CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    livro_isbn VARCHAR(13) NOT NULL,
    data_emprestimo DATE NOT NULL DEFAULT CURRENT_DATE,
    data_devolucao_prevista DATE NOT NULL,
    data_devolucao_efetiva DATE,
    multa DECIMAL(10,2) DEFAULT 0.00,
    status ENUM('ativo', 'devolvido', 'atrasado') NOT NULL DEFAULT 'ativo',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE RESTRICT,
    FOREIGN KEY (livro_isbn) REFERENCES livros(isbn) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Índices para melhoria de performance
CREATE INDEX idx_livros_categoria ON livros(categoria_id);
CREATE INDEX idx_emprestimos_usuario ON emprestimos(usuario_id);
CREATE INDEX idx_emprestimos_livro ON emprestimos(livro_isbn);
CREATE INDEX idx_emprestimos_status ON emprestimos(status);

-- Views
CREATE VIEW vw_livros_disponiveis AS
SELECT l.isbn, l.titulo, l.ano_publicacao, e.nome AS editora, c.nome AS categoria,
       l.exemplares_disponiveis
FROM livros l
LEFT JOIN editoras e ON l.editora_id = e.id
LEFT JOIN categorias c ON l.categoria_id = c.id
WHERE l.exemplares_disponiveis > 0;

CREATE VIEW vw_emprestimos_ativos AS
SELECT e.id, u.nome AS usuario, u.email, l.titulo AS livro, 
       e.data_emprestimo, e.data_devolucao_prevista,
       DATEDIFF(
```
