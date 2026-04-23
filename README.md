# festival

# Resumo das Alterações
 # # Sincronização de Rotas:
 Ajustei o ficheiro urls.py para que os nomes dos links (como 'dias' e 'palcos') correspondessem exatamente ao que estava escrito nos botões do menu.

# # Ligação Views-Modelos: 
Corrigi as funções no views.py para que elas fossem procurar a informação correta à base de dados. Antes, algumas views tentavam mostrar tudo de uma vez ou não encontravam o ID do concerto selecionado.

 # # Criação de Templates:
Como o projeto estava incompleto, criei o ficheiro HTML que faltava (dias.html) para que o site deixasse de dar erro de "página não encontrada".

# # Exibição de Conteúdo:
No ecrã dos dias, adicionei um ciclo para que, por baixo de cada data, apareça a lista real de concertos e bandas, em vez de apenas a data isolada.

# # Navegação Dinâmica: 
Garanti que, ao clicar num dia ou num palco, o Django saiba exatamente que concertos mostrar, passando o ID correto entre as páginas.
