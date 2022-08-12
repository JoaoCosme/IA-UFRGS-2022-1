# Testes de pesos e profundidade

## Pesos escolhidos para os testes 1, 2 e 3:

**quantidade_de_pecas**: 20

**menos_espacos_vazios**: 10

**diferenca_pecas**: 10

**e_vitoria**: 100

**mobilidade**: 10

**cantos_capturados**: 20

**estabilidade**: 40

## **TESTE 1**: Profundidade =  5

|#|Pontuação randomplayer|Pontuação alfa_beta|Vitória alfa_beta|
|--|--------|--------|--------|
|1|22|42|x|
|2|34|30|
|3|12|52|x|
|4|27|37|x|
|5|48|16|
|6|29|35|x|
|7|43|21
|8|20|44|x
|9|18|46|x
|10|23|41|x

Win% = 70%

## **TESTE 2**: Profundidade =  7

**Player 2 (advsearch.alfa_beta_player) DISQUALIFIED! Too many illegal move attempts.
End of game reached!**

## **TESTE 3** Profundidade = 6

|#|Pontuação randomplayer|Pontuação alfa_beta|Vitória alfa_beta|
|--|--------|--------|--------|
|1|29|35|x|
|2|25|39|x|
|3|25|39|x|
|4|28|36|x|
|5|21|43|x|
|6|30|34|x|
|7|25|39|x|
|8|45|19|
|9|18|46|x|
|10|32|32|Draw|

Win% = 80%

**P.S: apesar da boa quantidade de vitórias, profundidade = 6 apresenta muitos timeouts durante as partidas. Não é recomendado o uso dessa profundidade.**

## **Testes com 2 alfa_beta juntos:**

**Profundidade máxima = 5** (ambos)

## **TESTE 1**

|avalia|alfa_beta_player1|alfa_beta_player2|
|--|----|----|
|**quantidade_de_pecas**|20|20|
|**menos_espacos_vazios**|10|10|
|**diferenca_pecas**|10|10|
|**e_vitoria**|100|100|
|**mobilidade**|10|20|
|**cantos_capturados**|20|30|
|**estabilidade**|40|40|

|Pontuação alfa_beta1|Pontuação alfa_beta2|Vitória|
|--------|--------|--------|
|39|25|alfa_beta1|

## **TESTE 2**

|avalia|alfa_beta_player1|alfa_beta_player2|
|--|----|----|
|**quantidade_de_pecas**|20|10|
|**menos_espacos_vazios**|10|10|
|**diferenca_pecas**|10|10|
|**e_vitoria**|100|50|
|**mobilidade**|10|20|
|**cantos_capturados**|20|100|
|**estabilidade**|40|30|

|Pontuação alfa_beta1|Pontuação alfa_beta2|Vitória|
|--------|--------|--------|
|42|22|alfa_beta1|

## **TESTE 3**

|avalia|alfa_beta_player1|alfa_beta_player2|
|--|----|----|
|**quantidade_de_pecas**|20|20|
|**menos_espacos_vazios**|10|10|
|**diferenca_pecas**|10|10|
|**e_vitoria**|100|100|
|**mobilidade**|10|10|
|**cantos_capturados**|20|20|
|**estabilidade**|40|40|

|Pontuação alfa_beta1|Pontuação alfa_beta2|Vitória|
|--------|--------|--------|
|38|26|alfa_beta1|

**OBS: neste caso, ganhou quem foi o primeiro a jogar.**

## **TESTE 4**

|avalia|alfa_beta_player1|alfa_beta_player2|
|--|----|----|
|**quantidade_de_pecas**|20|80|
|**menos_espacos_vazios**|10|20|
|**diferenca_pecas**|10|10|
|**e_vitoria**|100|400|
|**mobilidade**|10|20|
|**cantos_capturados**|20|100|
|**estabilidade**|40|70|

|Pontuação alfa_beta1|Pontuação alfa_beta2|Vitória|
|--------|--------|--------|
|42|22|alfa_beta1|

## **TESTE 5**

|avalia|alfa_beta_player1|alfa_beta_player2|
|--|----|----|
|**quantidade_de_pecas**|10|20|
|**menos_espacos_vazios**|10|10|
|**diferenca_pecas**|10|10|
|**e_vitoria**|100|100|
|**mobilidade**|20|10|
|**cantos_capturados**|30|20|
|**estabilidade**|20|40|

|Pontuação alfa_beta1|Pontuação alfa_beta2|Vitória|
|--------|--------|--------|
|39|25|alfa_beta2|

## **TESTE 6**

|avalia|alfa_beta_player1|alfa_beta_player2|
|--|----|----|
|**quantidade_de_pecas**|40|20|
|**menos_espacos_vazios**|10|10|
|**diferenca_pecas**|10|10|
|**e_vitoria**|100|100|
|**mobilidade**|20|10|
|**cantos_capturados**|20|20|
|**estabilidade**|40|40|

|Pontuação alfa_beta1|Pontuação alfa_beta2|Vitória|
|--------|--------|--------|
|39|25|alfa_beta2|

a sequência [20,10,10,100,10,20,40] apresenta os melhores resultados nos testes