// JAVASCRIPT PARA A PÁGINA DE CRIAÇÃO DE PERSONAGENS

// Garante que todos os elementos HTML estejam carregados antes do JS tentar acessá-los
document.addEventListener('DOMContentLoaded', function() {
    console.log('Página de criação de personagem carregada'); // Log informativo no console do navegador 
  
    
//  Validação do preenchimento correto de cada campo para o envio no Flask
    const form = document.querySelector('form'); // Seleciona o primeiro formulário da página
    if (form) {
        form.addEventListener('submit', function(e) {
            // Obtém os valores atuais de cada input e armazena na constante para verificação 
            const nome = document.getElementById('nome').value;
            const raca = document.getElementById('raca').value;
            const classe = document.getElementById('classe').value;
            const estilo = document.getElementById('estilo').value;
            
            // Verifica se algum campo está vazio
            if (!nome || !raca || !classe || !estilo) {
                e.preventDefault();
                alert('Por favor, preencha todos os campos antes de continuar.');
            }
        });
    }
});
