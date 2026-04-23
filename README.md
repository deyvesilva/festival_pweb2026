# 🎸 Projeto Festival 

### 🔗 Sincronização de Rotas (`urls.py`)
* **O problema:** Havia uma falha na correspondência entre os nomes das rotas e os links definidos no menu (`layout.html`), causando erros de navegação.
* **A solução:** Ajustei os caminhos e os atributos `name` (ex: `'dias'`, `'palcos'`, `'dia'`) para que o sistema de roteamento do Django consiga resolver corretamente os pedidos.

### ⚙️ Ligação Views-Modelos (`views.py`)
* **O problema:** As funções de visualização estavam incompletas ou não filtravam os dados corretamente, o que impedia a exibição de informação específica por dia ou concerto.
* **A solução:** Corrigi as consultas (queries) à base de dados. As views agora utilizam os IDs passados pela URL para ir buscar exatamente o que o utilizador selecionou, garantindo que a página de detalhe mostre a banda correta.

### 📄 Criação de Templates
* **O problema:** O projeto estava incompleto, apresentando erros de *TemplateDoesNotExist*.
* **A solução:** Implementei o ficheiro **`dias.html`**. Este ficheiro é o núcleo da aplicação, pois faz a ponte entre as datas do festival e a programação de bandas.

### 📊 Exibição Dinâmica de Conteúdo
* **O problema:** A página de listagem era estática e não mostrava a relação entre os dias e os concertos.
* **A solução:** Utilizei um **ciclo aninhado (nested loop)** no template `dias.html`. Agora, para cada dia registado, o sistema lista automaticamente os concertos e os palcos associados, tornando a interface informativa e funcional.

### 🚀 Navegação Dinâmica
* **O problema:** Os links estavam "partidos" ou levavam a páginas genéricas.
* **A solução:** Implementei a tag `{% url %}` com a passagem dinâmica de parâmetros. Isto permite que a navegação seja fluida: ao clicar num dia ou num concerto, o Django encaminha o utilizador para a página correta com os dados filtrados.
