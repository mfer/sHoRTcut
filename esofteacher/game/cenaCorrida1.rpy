Momento1: Indo para o cliente

dp: Olá (NOMEJOGADOR). Vi você conversando com o (NOMEDOSCRUMMASTER) quando chegou. Meu nome é (NOMEDONODOPRODUTO).
dp: (NOMESUPERVISOR) pediu para te acompanhar nesse projeto, já que você foi contratado há pouco tempo. Atuarei, junto com você, como dono do produto, para que você possa ir treinando, aprendendo e se acostumando com a empresa. 
dp: Não se assuste, então, se eu fizer alguns questionamentos para ver se está aprendendo mesmo. (NOMESUPERVISOR) que pediu para fazer isso, a culpa não é minha!
dp: Como está trabalhando em outro projeto também, talvez terei que te substituir se em algum momento não puder trabalhar no projeto com a PadaOne.
dp: Estamos indo para a confeitaria Mestre do Bolo agora para levantar o que precisam do primeiro módulo.
dp: Você será responsável por escrever as histórias que conseguirmos levantar lá. Você sabe o que é uma história?
[história.1] Frases que capturam o que o usuário faz ou precisa fazer no sistema, escritas de modo informal.
[história.2] Frases que contam como o usuário deve interagir com o sistema, o que ele precisa que o sistema faça, escritas de modo formal, como um diagrama.
[história.3] Não sei.

[história.1]:
dp: Exatamente!
- pula para [história.fim].

[história.2]:
- aumenta stress em X
dp: Quase isso…
dp: As frases idealmente devem ser escritas de modo mais informal, para serem mais fáceis de serem entendidas pelo cliente.
- pula para [história.fim]

[história.3]:
- aumenta stress em X
dp: Queria ser assim tranquilo, que nem você…
dp: Histórias são frases que capturam o que o usuário faz ou precisa fazer no sistema, escritas de modo informal.
- pula para [história.fim]

[história.fim]
dp: A partir das histórias que você escrever é que vamos depois definir as tarefas para os programadores.
dp: Vamos descer que nosso taxi já deve estar chegando.


Momento 2: Levantando requisitos no cliente - montando histórias

define cliente cl
define jogador jg
define donoproduto dp
Background: confeitaria mestreDoBolo

dp: Boa tarde, somos da empresa PadaSoft, conforme conversamos por telefone, viemos levantar os requisitos do primeiro módulo.
dp: Eu sou o (NOMEDONOPRODUTO), esse aqui é o (NOMEJOGADOR).
cl: Olá, sou o dono da confeitaria Mestre do Bolo, meu nome é (NOMECLIENTEAGIL).
cl: Estamos querendo um software que possibilite um contato mais próximo com os nossos clientes.
- pula para [options]

[options]:
dp: Então, meu caro (NOMEJOGADOR). Você quer perguntar algo?
[option.1, aparece se flagOption1 = 0 ] (NOMECLIENTEAGIL), quais são as informações mais relevantes?
[option.5, aparece se flagOption1 = 1 e flagOption5 = 0] Quais informações você quer que sejam armazenadas para cada cliente?
[option.6, aparece se flagOption5 = 1 e flagOption6 = 0] Quais campos serão de preenchimento obrigatório?
[option.7, aparece se flagOption5 = 1 e flagOption7 = 0] Como você gostaria de poder pesquisar por clientes?
[option.2, aparece se flagOption2 = 0] (NOMECLIENTEAGIL), como vocês gostariam de inserir essas informações?  
[option.3, aparece se flagOption3 = 0] (NOMECLIENTEAGIL), como esse software vai ajudar a melhorar a qualidade dos seus serviços?
[option.4] Não, tudo bem por mim agora.

[option.1]:
cl: Apesar de sermos uma confeitaria renomada, ainda armazenamos as informações dos nossos clientes em arquivos de papel: nomes, telefones, endereços, esse tipo de coisa... 
img (http://www.arquivopublico.pr.gov.br/arquivos/Image/ArquivoSEOP3.jpg)
cl: Queremos mudar essa cultura e utilizar um programa de computador. 
cl: Ficará muito mais fácil fazer backup, encontrar e atualizar uma informação.
- aumentar a barra de escopo em X1
- setar flagOption1
- pula para options

[option.2]:
cl: Nós teremos um funcionário dentro da empresa que vai ficar responsável por isso. 
- aumentar a barra de escopo em X2
- setar flagOption2
- pula para options

[option.3]
cl: Ah! De diversas maneiras. Queremos, por exemplo, saber quais produtos mais vendidos. Quais clientes compram mais. 
- aumentar a barra de escopo em X3
- setar flagOption3
- pula para options

[option.4]:
- aumentar barra de stress de acordo com as flagOption’s que não foram setadas.
-pula para option.fim

[option.5]:
cl: Bom, é importante que tenha cadastrado o Nome, o CPF, o telefone e o endereço.
cl: Ah! Coloquem também data de nascimento! Não temos essa informação hoje no nosso arquivo, mas é legal saber quando o cliente está fazendo aniversário.
- aumentar a barra de escopo em X5
- setar flagOption5
- pula para options

[option.6]:
cl: Hmm… Coloca só o Nome e o CPF. Nem sempre tenho as outras informações.
- aumentar a barra de escopo em X6
- setar flagOption6
- pula para options

[option.7]:
cl: Quero poder buscar por todas as informações, mas deixe que a pesquisa por Nome e CPF sejam a opção padrão, a escolha mais fácil. É o que mais vamos usar.
cl: Quero poder digitar tanto o nome quanto o CPF para encontrar o cliente.
cl: Ah, coloque também uma caixinha que me avise quem são os aniversariantes do dia!
- aumentar barra de escopo em X7
- setar flagOption7
- pula para options.

[option.fim]
jg: Ok, acho que esta informação o suficiente para definirmos a primeira entrega.    
dp: Obrigado pelas informações, (NOMECLIENTEAGIL).
cl: Por nada. Espero ver isso funcionando em breve!

Momento 3: De volta para a empresa

define scrumMaster mb
define jogador jg
Background: (o mesmo da cena aa)

mb: Bom que já voltaram!
mb: (NOMEDONOPRODUTO) me falou que vocês levantaram como deve ser o módulo (PRIMEIROMODULO).
mb: Estamos indo planejar agora a primeira corrida. Você sabe o que é uma corrida?
[sprint.1]Chegar rápido de um lugar até outro?
[sprint.2]Uma tradução de sprint?
[sprint.3]Não sei.

[sprint.1]:
- aumentar a barra de stress em X
mb: É… em outro contexto.
- Pula para sprint.explicacao

[sprint.2]:
mb: Isso! Mas o que é uma sprint?
[sprint2.1]Não sei.
[sprint2.2]Reunião de uma metodologia ágil.
[sprint2.3]Unidade de tempo de desenvolvimento do projeto.

[sprint.3]
- aumentar a barra de stress em X
mb: Não fique triste, irei te explicar agora…
- pula para sprint.explicacao

[sprint2.1]:
- aumentar a barra de stress em X
- pula para sprint.explicacao

[sprint2.2]:
- aumentar a barra de stress em X
mb: Não, não é isso…
- pula para sprint.explicacao

[sprint2.3]:
mb: Isso!
- pula para sprint.explicacao

[sprint.explicacao]
mb: A corrida é a unidade básica de desenvolvimento em Scrum. Corridas tendem a durar entre uma semana e um mês, e são um esforço dentro de uma faixa de tempo (ou seja, restrito a uma duração específica) de comprimento constante.
mb: O conjunto de funcionalidades que entram em uma corrida é um conjunto de prioridades de requisitos de alto nível definidos pelo Dono do Produto.
mb: Vamos então para a reunião.

Momento 4: Reunião da definição da corrida.

dp: (NOMEJOGADOR), fale para a gente quais são as histórias levantadas com o cliente.
- se flagOption6 e flagOption7 iguais a 1, pula para [historiasCliente.full]
- se flagOption6 igual a 1, pula para [historiasCliente.obrigatórios]
- se flagOption7 igual a 1, pula para [historiasCliente GT.pesquisa]
- se flagOption5 igual a 1, pula para [historiasCliente.campos]
- pula para [historiasCliente.simples]

[historiasCliente.full]:
jg: Temos três histórias:
jg: “Eu, como dono da empresa, quero cadastrar clientes com Nome, CPF, telefone, endereço e data de nascimento, sendo que apenas Nome e CPF são obrigatórios.”
“Eu, como dono da empresa, quero encontrar meus clientes com base em qualquer campo, mas principalmente por Nome e CPF.”
“Eu, como dono da empresa, quero ser avisado de quais clientes fazem aniversário no dia.”
- pula para [historiasCliente.fim]

[historiasCliente.obrigatórios]:
jg: Temos duas histórias:
jg: “Eu, como dono da empresa, quero cadastrar clientes com Nome, CPF, telefone, endereço e data de nascimento, sendo que apenas Nome e CPF são obrigatórios.”
“Eu, como dono da empresa, quero pesquisar meus clientes cadastrados.”
- pula para [historiasCliente.fim]

[historiasCliente.pesquisa]:
jg: Temos três histórias:
jg: “Eu, como dono da empresa, quero cadastrar clientes com Nome, CPF, telefone, endereço e data de nascimento.”
“Eu, como dono da empresa, quero encontrar meus clientes com base em qualquer campo, mas principalmente por Nome e CPF.”
“Eu, como dono da empresa, quero ser avisado de quais clientes fazem aniversário no dia.”
- pula para [historiasCliente.fim]

[historiasCliente.campos]:
jg: Temos duas histórias:
jg: “Eu, como dono da empresa, quero cadastrar clientes com Nome, CPF, telefone, endereço e data de nascimento.”
“Eu, como dono da empresa, quero pesquisar meus clientes cadastrados.”
- pula para [historiasCliente.fim]

[historiasCliente.simples]:
jg: Temos duas histórias:
jg: “Eu, como dono da empresa, quero cadastrar clientes.”
“Eu, como dono da empresa, quero pesquisar meus clientes cadastrados.”
- pula para [historiasCliente.fim]

[historiasCliente.fim]:
dp: Ok. Quais serão implementadas nessa primeira sprint? 
dp: Lembre-se que o importante é termos software funcionando no prazo de até duas semanas.


Momento 5: Desenvolvimento

Momento 6: Apresentação para o cliente

