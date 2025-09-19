// JavaScript para a página de criação de personagem
document.addEventListener('DOMContentLoaded', function() {
    console.log('Página de criação de personagem carregada');
    
    // Validação básica do formulário (cliente-side apenas para melhor UX)
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const nome = document.getElementById('nome').value;
            const raca = document.getElementById('raca').value;
            const classe = document.getElementById('classe').value;
            const estilo = document.getElementById('estilo').value;
            
            if (!nome || !raca || !classe || !estilo) {
                e.preventDefault();
                alert('Por favor, preencha todos os campos antes de continuar.');
            }
        });
    }
});
