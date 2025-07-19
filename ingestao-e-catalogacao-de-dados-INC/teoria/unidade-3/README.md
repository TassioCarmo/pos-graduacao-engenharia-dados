## Fluxo de tarefas

- Um **fluxo de tarefas** (ou *task flow*) é a sequência de atividades ou comandos que precisam ser executados em uma ordem específica. Cada tarefa representa uma ação individual e normalmente depende do sucesso da anterior para ser iniciada.

**Características principais:**

- Foco na execução de processos  
- Pode envolver scripts, comandos, chamadas de API etc.  
- Geralmente faz parte de uma automação  

---

## Fluxo de dados

- Um **fluxo de dados** (ou *data flow*) é o caminho percorrido pelos dados desde sua origem até o destino final, podendo passar por transformações, enriquecimentos ou validações ao longo do percurso.

**Características principais:**

- Foco na movimentação e transformação dos dados  
- Pode ser *batch*, *streaming* ou em tempo real  
- Normalmente envolve múltiplas fontes e destinos  

---

## ETL / ELT

**ETL** (Extract, Transform and Load) e **ELT** (Extract, Load and Transform) são processos de integração/preparação de dados muito utilizados em ambientes de Business Intelligence e análise de dados. A diferença principal está na ordem da etapa de transformação.

Cada etapa possui um fluxo de tarefas/dados associado:

1. **E: Extração (Extract)**  
   - Coleta e extração de dados de várias fontes (bancos de dados, arquivos, APIs etc.).  
   - Armazenamento temporário em *staging*.  
   - Dados brutos (sem modificações).

2. **T: Transformação (Transform)**  
   - Limpeza, formatação, reestruturação e enriquecimento dos dados.  
   - Aplicação de regras de negócio, filtragem, agregação, padronização etc.

3. **L: Carga (Load)**  
   - Carregamento dos dados no destino final (Data Warehouse, Data Lake, sistemas de arquivos etc.).  
   - Organização em esquemas otimizados para consultas.

- No **ETL**, a transformação ocorre antes do carregamento, otimizando consultas posteriores em casos de grande volume de dados.  
- No **ELT**, a transformação é feita após o carregamento, aproveitando o poder de processamento e armazenamento do destino final.

---

### Ferramentas de ETL & ELT

Há várias ferramentas ETL/ELT disponíveis (open source ou proprietárias). A escolha deve considerar:

- Recursos e funcionalidades  
- Facilidade de uso  
- Escalabilidade e desempenho  
- Integração com sistemas existentes  
- Suporte e comunidade  
- Segurança  
- Custo  
- Documentação  
```
