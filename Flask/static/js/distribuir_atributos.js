// Gerenciamento da distribuição de atributos
const distribuirAtributos = {
    valoresOriginais: [],
    ocorrenciasDisponiveis: [], // Array com todas as ocorrências individuais
    ocorrenciasSelecionadas: new Set(), // Índices das ocorrências selecionadas

    inicializar: function() {
        // Obter valores do Flask e criar array de ocorrências com índices únicos
        this.valoresOriginais = [...window.valoresFlask];
        this.ocorrenciasDisponiveis = this.valoresOriginais.map((valor, index) => {
            return { valor: valor, index: index };
        });
        
        // Configurar event listeners
        this.configurarEventListeners();
        
        // Inicializar a atualização de opções
        this.atualizarTodosSelects();
    },

    configurarEventListeners: function() {
        const selects = document.querySelectorAll('.atributo-select');
        
        // Adicionar event listener para cada select
        selects.forEach(select => {
            select.addEventListener('change', (e) => {
                this.gerenciarSelecao(select);
                this.validarSelect(select);
            });
        });

        // Validação do formulário
        const form = document.getElementById('atributos-form');
        if (form) {
            form.addEventListener('submit', (e) => {
                if (!this.validarFormulario()) {
                    e.preventDefault();
                    alert('Por favor, selecione um valor para todos os atributos antes de continuar.');
                }
            });
        }
    },

    gerenciarSelecao: function(select) {
        const novoValorCompleto = select.value;
        const valorAnteriorCompleto = select.dataset.valorAnterior || '';
        
        // Extrair valor e índice da seleção anterior
        if (valorAnteriorCompleto) {
            const [valorAnterior, indexAnterior] = valorAnteriorCompleto.split('-').map(Number);
            this.ocorrenciasSelecionadas.delete(indexAnterior);
            select.dataset.valorAnterior = '';
        }
        
        // Extrair valor e índice da nova seleção
        if (novoValorCompleto) {
            const [valorNovo, indexNovo] = novoValorCompleto.split('-').map(Number);
            this.ocorrenciasSelecionadas.add(indexNovo);
            select.dataset.valorAnterior = novoValorCompleto;
        }
        
        // Atualizar todos os selects
        this.atualizarTodosSelects();
    },

    atualizarTodosSelects: function() {
        const selects = document.querySelectorAll('.atributo-select');
        
        selects.forEach(select => {
            const valorAtualCompleto = select.value;
            const valorAnteriorCompleto = select.dataset.valorAnterior || '';
            
            // Limpar todas as opções exceto a primeira
            while (select.options.length > 1) {
                select.remove(1);
            }
            
            // Adicionar opções disponíveis (apenas ocorrências não selecionadas)
            this.ocorrenciasDisponiveis.forEach(ocorrencia => {
                if (!this.ocorrenciasSelecionadas.has(ocorrencia.index) || 
                    `${ocorrencia.valor}-${ocorrencia.index}` === valorAtualCompleto) {
                    const option = document.createElement('option');
                    option.value = `${ocorrencia.valor}-${ocorrencia.index}`;
                    option.textContent = ocorrencia.valor;
                    option.dataset.index = ocorrencia.index;
                    select.appendChild(option);
                }
            });
            
            // Restaurar a seleção anterior se ainda estiver disponível
            if (valorAtualCompleto && select.querySelector(`option[value="${valorAtualCompleto}"]`)) {
                select.value = valorAtualCompleto;
            } else if (valorAnteriorCompleto && select.querySelector(`option[value="${valorAnteriorCompleto}"]`)) {
                select.value = valorAnteriorCompleto;
                select.dataset.valorAnterior = valorAnteriorCompleto;
                const indexAnterior = parseInt(valorAnteriorCompleto.split('-')[1]);
                this.ocorrenciasSelecionadas.add(indexAnterior);
            } else {
                select.value = "";
                select.dataset.valorAnterior = '';
            }
        });
    },

    validarSelect: function(select) {
        if (select.value) {
            select.style.borderColor = '';
        } else {
            select.style.borderColor = 'red';
        }
    },

    validarFormulario: function() {
        const selects = document.querySelectorAll('.atributo-select');
        let todosPreenchidos = true;
        
        selects.forEach(select => {
            if (!select.value) {
                todosPreenchidos = false;
                select.style.borderColor = 'red';
            } else {
                select.style.borderColor = '';
            }
        });
        
        return todosPreenchidos;
    }
};

// Inicializar quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    distribuirAtributos.inicializar();
});

// Exportar para uso global
window.distribuirAtributos = distribuirAtributos;
