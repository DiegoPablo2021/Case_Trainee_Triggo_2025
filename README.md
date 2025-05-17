# Análise de Dados do E-commerce Olist

Este projeto tem como objetivo realizar uma análise completa dos dados de vendas do e-commerce brasileiro Olist, visando extrair insights relevantes sobre desempenho comercial, comportamento do cliente, logística de entregas e satisfação.

## Estrutura de Pastas

📁 Case_Trainee_Triggo_2025/
![alt text](image.png)


## Visão Geral do Projeto

A análise foi conduzida como parte de um teste técnico para o Programa de Trainee da triggo.ai - Excelência em Engenharia de Dados e DataOps 2025. Os principais objetivos foram:

- Preparar e tratar os dados do Olist.
- Realizar análises exploratórias com foco em negócios.
- Desenvolver visualizações interativas e dashboards.
- Aplicar modelos simples de machine learning.
- Gerar insights e recomendações acionáveis.

## Estrutura dos Dados

Os dados estão organizados em múltiplos arquivos `.csv`, incluindo:

- `orders.csv`: Informações gerais dos pedidos
- `order_items.csv`: Detalhes dos produtos comprados
- `order_reviews.csv`: Avaliações feitas pelos clientes
- `customers.csv`: Dados dos consumidores
- `products.csv`: Categorias e informações dos produtos
- `sellers.csv`: Dados dos vendedores
- `geolocation.csv`: Localizações geográficas (por CEP)
- `category_translation.csv`: Tradução das categorias de produto

## Principais KPIs e Resultados

| Indicador | Resultado |
|----------|-----------|
| **Quantidade total de pedidos** | 99.441 |
| **Ticket médio por pedido** | R$ 118,00 |
| **Categorias com maior receita** | Eletrônicos, Móveis, Moda |
| **Estados com maior valor médio de pedido** | SP, RJ, MG |
|  **Tempo médio de entrega** | 12 dias |
| **Avaliação média dos clientes** | 4.09 |
| **Taxa de atraso nas entregas** | 21,8% |
| **Taxa de clientes recorrentes** | 16,4% |
| **Segmentação de clientes (Clustering)** | 4 perfis distintos |
| **Predição de atraso (modelo Random Forest)** | Acurácia: 81% |

## Tecnologias Utilizadas

- Python 3.10+
- Bibliotecas:
  - `pandas`, `numpy`, `seaborn`, `matplotlib`
  - `scikit-learn` para machine learning
  - `plotly`, `folium` (para visualizações avançadas)
- Jupyter Notebook
- SQL para consultas intermediárias
- PowerPoint (entrega executiva dos resultados)

## Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/DiegoPablo2021/Case_Trainee_Triggo_2025.git
   cd Case_Trainee_Triggo_2025
   ```

2. Crie um ambiente virtual
   ```bash
   python -m venv venv
   venv/Scripts/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o notebook:
   ```bash
   jupyter notebook notebooks/etl-data.ipynb
   jupyter notebook notebooks/dashboard.ipynb
   jupyter notebook customer-segmentation/notebooks/customer_segmentation.ipynb
   ```

## Autor

Desenvolvido por **Diego Pablo de Menezes**, apaixonado por insights estratégicos e soluções de dados que impulsionam decisões inteligentes.

- [LinkedIn](https://www.linkedin.com/in/diego-pablo/)
- [E-mail](diegopmenezes@hotmail.com)

---

> Projeto desenvolvido para fins educacionais e de avaliação técnica.  
> Fonte dos dados: [Kaggle – Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).