document.addEventListener("DOMContentLoaded", function () {
    const comentarioBtn = document.getElementById("comentario-btn");
    const comentarioContainer = document.getElementById("comentarios-modal");
    const comentarioForm = document.getElementById("comentario-form");

    comentarioBtn.addEventListener("click", function () {
        comentarioContainer.style.display = "block";
        loadComentarios();
    });

    comentarioForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const texto = document.getElementById("comentario-texto").value;
        adicionarComentario(texto);
    });

    function loadComentarios() {
        comentarioContainer.innerHTML = `<div class="loading-animation">Loading...</div>`;
        fetch(`/nota/${nota_id}/comentarios/`)
            .then(response => response.json())
            .then(data => {
                comentarioContainer.innerHTML = data.comentarios.map(comentario => `
                    <div class="comentario">
                        <strong>${comentario.usuario__username}</strong>: ${comentario.texto}
                    </div>
                `).join('');
            });
    }

    function adicionarComentario(texto) {
        fetch(`/nota/${nota_id}/adicionar_comentario/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: `texto=${texto}`
        })
        .then(response => response.json())
        .then(comentario => {
            comentarioContainer.innerHTML += `
                <div class="comentario">
                    <strong>${comentario.usuario}</strong>: ${comentario.texto}
                </div>
            `;
        });
    }
});
