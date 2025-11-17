// JAVASCRIPT PARA A PÁGINA DA FICHA

// Garante que todos os elementos HTML estejam carregados antes do JS tentar acessá-los
document.addEventListener('DOMContentLoaded', function() {
    console.log('Ficha do personagem carregada'); // Log informativo no console do navegador
    
    // Efeitos visuais para a ficha: adiciona transição suave de cor para células de tabela
    const tabelas = document.querySelectorAll('table');
    tabelas.forEach(tabela => {
        tabela.addEventListener('mouseover', function(e) {
            if (e.target.tagName === 'TD') {
                e.target.style.transition = 'background-color 0.3s ease';
            }
        });
    }); 
    
    // Adiciona tooltips automáticos para texto muito longo
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
