// ficha.js - JavaScript para a ficha do personagem (apenas melhorias de UX)
document.addEventListener('DOMContentLoaded', function() {
    console.log('Ficha do personagem carregada');
    
    // Efeitos visuais para a ficha
    const tabelas = document.querySelectorAll('table');
    tabelas.forEach(tabela => {
        tabela.addEventListener('mouseover', function(e) {
            if (e.target.tagName === 'TD') {
                e.target.style.transition = 'background-color 0.3s ease';
            }
        });
    });
    
    // Adicionar tooltip para células com texto muito longo
    const celulasTabela = document.querySelectorAll('td');
    celulasTabela.forEach(celula => {
        if (celula.textContent.length > 50) {
            celula.title = celula.textContent;
        }
    });
    
    // Adicionar efeito de destaque ao passar o mouse nas linhas da tabela
    const linhasTabela = document.querySelectorAll('tr');
    linhasTabela.forEach(linha => {
        linha.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#f5f5f5';
            this.style.transition = 'background-color 0.3s ease';
        });
        
        linha.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '';
        });
    });
});
