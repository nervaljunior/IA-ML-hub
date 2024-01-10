# ReverseGame-IA

#### a implementação do jogo utilizando a linguagem python

**Criadores**: [Felipe Teles](https://github.com/felipersteles), [Nerval Junior](https://github.com/nervaljunior) ,[Rodrigo pontes](https://github.com/rodrigopontis) e [João leonardo](https://github.com/joaoleopo)

![](https://img.shields.io/badge/Language-Python-blue) ![](https://img.shields.io/badge/IDE-Microsoft%20Visual%20Studio%202022-blue) ![](https://img.shields.io/badge/Environment-Windows-red) ![](https://img.shields.io/badge/User%20Interface-GUI%20%2B%20CLI-yellowgreen)

---


## Objetivo

### o objetivo é criar uma IA com uma boa heuristica

Para vencer, você precisa ter mais peças no tabuleiro do que seu oponente até o final do jogo. Como damas ou xadrez, as peças do jogo são pretas ou brancas. Quando o jogo termina, cada jogador conta suas peças restantes no tabuleiro para determinar o vencedor.

### o tabuleiro é 8x8

![image](https://github.com/nervaljunior/ReverseGame-IA/assets/108685222/0595d500-3604-4c48-a6c9-848eb06eba05)

### no jogo as peças tem um lado preto e um lado é branco

### caso a peça de cor diferente encurrale a peça de cor diferente as peças dos meio mudam de cor.

### elas podem ser encurraladas na diagonal, vertical e horizontal

## Implementando a Heuristica

![image](https://github.com/nervaljunior/ReverseGame-IA/assets/108685222/2e885141-9983-4b27-b46a-0b9695196bd3)

Para realizar a implementacao da heuristica, basta aplicar as condições criadas e estudadas na função em que realiza a verificação dos movimentos do compudor estando ela presente na **linha 185** do arquivo [reversi.py](./reversi.py)

## dicas:

seja o ultimo a entregar a lateral e os cantos e seus adjacentes
fazer com que o adiversario se afaste primeiro do meio
preste atenção nas bordas

![image](https://github.com/nervaljunior/ReverseGame-IA/assets/108685222/ee80b913-5e92-4796-ac78-c9933f3781c5)


## "os jogos estao para a IA assim como as corridas estao para os projetos de automoveis"( S.Russel )


# Inteligencia Artificial 28/03/2023

Linguagem orientada a agentes

## Conceitos

### Percepção
Informação que o agente consegue pegar do ambiente
- Exemplo: vizinhança

### Ações
O que o agente faz 
- Exemplo: andar, coletar, soltar

### Desempenho
Baseado em tempo de execução

## Tipos básicos de agente
- agentes reativos simples
- agentes reativos baseados em modelos
- agentes baseados em objetivos
- agentes baseados na utilidade

### Agente reativo simples
- Só toma decisão baseadas apenas nas percepções atuais do ambiente
- Não leva em consideração o histórico de ações ou o estado futuro do ambiente. 
- Eles respondem automaticamente a estímulos do ambiente, sem ter uma representação interna do mundo.

### Agente reativo com modelos
- Mantem históricos
- Esses agentes também tomam decisões com base nas percepções atuais do ambiente
- Têm uma representação interna do ambiente que lhes permite construir modelos internos do mundo. 
- Eles usam esses modelos para prever o efeito de suas ações antes de agir, permitindo-lhes fazer escolhas mais informadas.

### Agente baseado em objetivos
- Inicia execução com uma lista de objetivos
- Eles usam informações sobre o ambiente.
- Seu estado interno e seus objetivos para planejar e executar ações que os levem mais perto de seus objetivos.

### Agente baseado em utilizade
- Tem felicidade 
- Esses agentes atribuem valores de utilidade a diferentes ações e escolhem a ação que maximiza a utilidade esperada. Eles podem levar em consideração não apenas os objetivos imediatos, mas também as consequências de longo prazo de suas ações.
- exemplo items que valem mais pontos, etc...



