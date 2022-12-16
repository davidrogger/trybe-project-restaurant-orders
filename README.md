# Sobre o Projeto 

- Sexto e ultimo projeto tanto do modulo quanto do curso da trybe.
- Essa seção deu continuidade com TAD, focando agora em hashmaps e set.
- Desenvolver um sistema para uma lancheonete, onde é possível coletar informações de venda com nome, o prato pedido e o dia da semana que foi realizado o pedido, de um arquivo CSV, coletando essas informações é possível realizar filtros, como buscar qual o dia mais movimentado, quantidade que determinado cliente, consumiu de um item em especifico ou qual item ele consumiu mais, qual dia ele nunca compareceu ao local.

<details>
  <summary>
    <strong>
      :telescope: Detalhes do projeto:
    </strong>
  </summary>


</details>

# Inicio do projeto

Lendo o README fornecido pela trybe, vi que para ter um ganho de tempo e eficiencia, não devia começar do primeiro requisito, pois ele pedia funcionalidades, que a classe criada no requisito 2, iria executar com muito mais eficiencia que criando método por método.

# Classe TrackOrders

Define o atributo principal, `customers` sendo um dict, pois durante todo o projeto os usuários, tinham nomes únicos, e seria a forma mais eficiente de encontrar o cliente, e capturar as informações, sem ter que percorrer todos clientes, até encontrar a informação desejada.

## add_new_order

Inicialmente quando adicionando um novo pedido, verifico se o nome do cliente ja existe, caso não, criou o campo, e adiciono os dados de orders, onde adiciono cada item, com uma contagem de quantas vezes ele pediu aquele determinado prato, e um campo de days como conjunto, onde é adicionado os dias que ele pediu aquele prato, constando a presença dele naquele dia.
Ao decorrer do projeto o add new order foi criando novos sub métodos, onde era necessário determinar qual o pedido era mais pedido, quais os dias eram mais frequentes, achei essa forma mais eficiente, do que quando formos consultar esses dados, ele verificar na hora, gerando complexidades de tempo de O(n), dessa forma ele somava a quantidade na hora da inserção do item, e ja comparava se aquele item se tornava o mais consumido, ou se aquele dia se tornava o mais movimentado durante a adição do pedido().
Métodos como:

- get_most_ordered_dish_per_customer
- get_busiest_day
- get_least_busy_day

## get_days_never_visited_per_customer

Nesse método aproveitei das propriedades do `set`, onde eu posso verificar a diferença entre os dias abertos e os dias que o cliente compareceu, resultando nos dias que ele não fez pedido nenhum.




# Tecnologias e ferramentas usadas 🛠

![Python](https://img.shields.io/badge/-Python-%23F7DF1C?style=flat-square&logo=python)


# Desafios

- Maior desafio atual, tem sido melhor forma de buscar alguma informação de forma que não gera uma grande complexidade de tempo, mesmo sendo arquivos pequenos, sempre me pergunto, 
como melhorar aquela linha de código com base em complexidade.
# Conclusão

- Depois de mais de 12 meses de curso, projeto final, foi mais simples que eu esperava, mas se fosse necessário desenvolver esse mesmo projeto 12 meses atrás, quando eu iniciei na área, provavelmente eu teria bastante problemas, como sempre é gratificante demais ver que meu eu de tempos atrás agora domina bem e encontra as soluções, e que venham mais desafios!

<details>
  <summary>
    <strong>
      ⚠️ Configurações mínimas para execução do projeto
    </strong>
  </summary>

   - Sistema Operacional Distribuição Unix
 - Python versão >= 3.8.10 

</details>

</details>

<details>
  <summary>
    <strong>
      :newspaper_roll: Requisitos solicitados durante o desenvolvimento do projeto
    </strong>
  </summary>

 
### Resultado por requisito
*Nome* | *Avaliação*
--- | :---:
1.1 - Será validado se, ao executar o método `analyze_log`, os dados são preenchidos de forma correta no arquivo `data/mkt_campaign.txt` | :heavy_check_mark:
1.2 - Será validado se, ao executar o método `analyze_log` com um arquivo inexistente, o método retorna um erro | :heavy_check_mark:
1.3 - Será validado se, ao executar o método `analyze_log` com uma extensão inválida, o método retorna um erro | :heavy_check_mark:
2.1 - Será validado se, ao instanciar a classe `TrackOrders` pela primeira vez, o método retorna a quantidade de pedidos é igual a zero | :heavy_check_mark:
2.2 - Será validado se, ao executar o método `add_new_order`, o método deve adicionar um pedido | :heavy_check_mark:
2.3 - Será validado se, ao executar `get_most_ordered_dish_per_costumer`, o método retorna o prato mais pedido | :heavy_check_mark:
2.4 - Será validado se, ao executar `get_never_ordered_per_costumer`, o método retorna o pedido que o cliente nunca fez | :heavy_check_mark:
2.5 - Será validado se, ao executar `get_days_never_visited_per_costumer`, o método retorna o dias que o cliente nunca visitou | :heavy_check_mark:
2.6 - Será validado se, ao executar o método `get_busiest_day`, o método retorna o dia mais movimentado | :heavy_check_mark:
2.7 - Será validado se, ao executar o método `get_least_busy_day`, o método retorna o dia menos movimentado | :heavy_check_mark:
3.1 - Será validado se, ao executar o método `get_quantities_to_buy`, o método retorna a lista atualizada de ingredientes | :heavy_check_mark:
3.2 - Será validado se, ao executar o método `get_quantities_to_buy` o método retorna toda a quantidade de ingredientes há se comprar de hamburguer | :heavy_check_mark:
3.3 - Será validado se, ao executar o método `get_quantities_to_buy`, o método retorna a lista atualizada dos ingredientes que usam receitas diferentes | :heavy_check_mark:
4.1 - Será validado se, ao adicionar uma quantidade maior de ingredientes, o método retorna false | :heavy_check_mark:
4.2 - Será validado se, ao executar o método `get_available_dishes`, o método retorna todos os pratos onde os pratos tem ingredientes | :heavy_check_mark:
4.3 - Será validado se, ao executar o método `get_available_dishes`, não o método retorna os pratos o qual os ingredientes não sejam suficientes para prepará-los | :heavy_check_mark:


</details>
