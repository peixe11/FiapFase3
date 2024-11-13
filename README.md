# Documentação do Projeto de Sistema de Irrigação Inteligente

## Visão Geral do Projeto
Este projeto consiste no desenvolvimento de um sistema de irrigação automatizado e inteligente utilizando o microcontrolador ESP32. Ele visa monitorar e ajustar as condições do solo com base em sensores simulados no ambiente Wokwi. A lógica de irrigação depende de três parâmetros críticos para as culturas agrícolas: níveis de nutrientes (Fósforo e Potássio), acidez (pH) e umidade do solo. Esses parâmetros são monitorados continuamente, e a irrigação é ativada ou desativada automaticamente conforme condições predefinidas.

Além do sistema de monitoramento em tempo real, o projeto também possui um banco de dados para armazenar as leituras dos sensores e o histórico de operações de irrigação, utilizando um banco de dados SQL.

## Sensores e Componentes Utilizados

### Substituição de Sensores
- **Botões para Fósforo (P) e Potássio (K)**: Para representar a presença de nutrientes, foram implementados dois botões, um para cada nutriente. Quando pressionados, indicam a presença do nutriente; quando não pressionados, indicam sua ausência. Esse estado binário é interpretado como "tudo ou nada" (True para pressionado e False para solto).
- **Sensor LDR para pH**: Um sensor de intensidade de luz (LDR) substitui o sensor de pH. O valor lido pelo LDR, variando de 0 a 4095, é comparado ao intervalo de pH (0 a 14) para simular as condições do solo, com valores próximos a 7 sendo neutros.
- **Sensor DHT22 para Umidade e Temperatura**: Mantém a leitura real de umidade do solo. Um valor de umidade abaixo de 30% é um dos critérios para ativar a irrigação.
- **Relé para Controle da Bomba d’Água**: Um relé é usado para simular a ativação da bomba d'água, controlando o fluxo de irrigação conforme a lógica de decisão do sistema.

### Regras de Irrigação
A irrigação será ativada conforme a seguinte regra de decisão:

- **Umidade < 30%**: Se o nível de umidade for inferior a 30%, a irrigação é ativada para corrigir o déficit hídrico do solo.
- **estadoP == LOW (Botão de Fósforo)**: Se o botão P (Fósforo) estiver pressionado, o sistema interpreta que o nutriente está ausente, ativando a irrigação.
- **estadoK == LOW (Botão de Potássio)**: De forma semelhante, se o botão K estiver pressionado, a irrigação será acionada.
- **LDR > 2300**: Um valor acima de 2300 no sensor LDR indica um valor "ácido" de pH, acionando a irrigação para equilibrar as condições do solo.

Essas condições visam manter o solo equilibrado e adequado para a plantação, com irrigação ajustada dinamicamente conforme as leituras dos sensores.

---

### Banco de Dados e Estrutura SQL

#### Estrutura do Banco de Dados
O banco de dados é composto por três tabelas: **Sensores**, **Irrigacao** e **Historico_Irrigacao**. Ele armazena informações sobre as leituras dos sensores e as operações de irrigação, permitindo consulta e controle das condições históricas da lavoura.

- **Tabela Sensores**
  - `id_sensor`: Identificador único para cada leitura.
  - `tipo_sensor`: Especifica o tipo de sensor (P, K, pH, Umidade).
  - `valor`: Valor lido pelo sensor.
  - `data_leitura`: Data e hora da leitura.

- **Tabela Irrigacao**
  - `id_irrigacao`: Identificador único para cada operação de irrigação.
  - `status`: Indica o estado da irrigação ('Ligado' ou 'Desligado').
  - `data_operacao`: Data e hora da operação.

- **Tabela Historico_Irrigacao**
  - `id_historico`: Identificador único para cada entrada de histórico.
  - `id_sensor`: Chave estrangeira referenciando o sensor.
  - `id_irrigacao`: Chave estrangeira referenciando a operação de irrigação.
  - `data_registro`: Data e hora do registro no histórico.

#### Código de Manipulação do Banco de Dados em Python
A manipulação do banco de dados é realizada com operações CRUD (Create, Read, Update, Delete) usando o módulo `cx_Oracle` para conexão com um banco Oracle.

- `inserir_leitura_sensor`: Insere uma nova leitura de sensor no banco de dados.
- `registrar_irrigacao`: Registra uma nova operação de irrigação (Ligado ou Desligado).
- `registrar_historico`: Insere um registro no histórico para associar uma leitura de sensor a uma operação de irrigação.
- `consultar_historico`: Exibe todo o histórico de leituras e operações de irrigação.
- `atualizar_leitura_sensor`: Atualiza o valor de uma leitura de sensor específica.
- `deletar_historico`: Deleta uma entrada específica do histórico de operações.

#### Exemplo de Código em Python

```python
# Inserir uma leitura de umidade
inserir_leitura_sensor("Umidade", 55)

# Registrar uma irrigação ligada
registrar_irrigacao("Ligado")

# Registrar o histórico da leitura com irrigação
registrar_historico(id_sensor=1, id_irrigacao=1)

# Atualizar leitura do sensor
atualizar_leitura_sensor(1, 60)

# Deletar um registro específico do histórico
deletar_historico(1)

# Consultar histórico completo de operações
consultar_historico()

# Fechar a conexão com o banco de dados
connection.close()

Este código cria um fluxo de coleta e armazenamento de dados de sensores e operações de irrigação. Cada leitura de sensor e cada operação é registrada no banco de dados, permitindo rastreabilidade completa das condições da lavoura e das ações tomadas pelo sistema.

---

### Conclusão

Este projeto representa um sistema de irrigação inteligente que simula um ambiente agrícola, utilizando sensores e lógica de controle para manter condições ideais do solo. A substituição dos sensores por componentes simulados permite desenvolver e testar a lógica do sistema de forma prática, e o uso de um banco de dados relacional facilita o controle e monitoramento histórico das operações de irrigação e leituras dos sensores.
