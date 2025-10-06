# Credit Card Fraud

## Sobre o arquivo

- Contém transações feitas com cartão de crédito em setembro de 2023
- O dataset representa transações realizadas em dois dias
- O dataset está altamente desbalanceado, 284,807 transações validas e 492 transações fraudulentas (0.172%)
- O objetivo principal do modelo a ser construido com estes dados será prever corretamente o valor da coluna Class para novas transações.

### Esturtura

- Time: Representa o tempo em segundos da transação em relação a primeira transação do dataset
- V1, V2, V3, ..., V28: São colunas que continham dados como localização, idade, estabelecimento e outras informações que tiveram que ser transformadas para garantir confidencialidade. A transformação ocorreu utilizando PCA, dessa forma os dados permanecem confidencializados e ainda podem ser usados nos algoritmos de machine learning
- Amount: Valor da transação
- Class: Classificação da transação, sendo 0 uma transação normal e 1 uma transação fraudulenta.