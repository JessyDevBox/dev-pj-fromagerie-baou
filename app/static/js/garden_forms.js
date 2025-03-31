document.addEventListener("DOMContentLoaded", function() {
    // Void multiple doc loaded event;
    if (window.DocLoaded) return;
    window.DocLoaded = true;

    // Modal - Add Garden
    const formGardenAdd = document.getElementById("addGardenForm");
    if (formGardenAdd) {
        formGardenAdd.addEventListener("submit", async (event) => {
            event.preventDefault();
            // console.log("** formGardenAdd (event submit)");
            const data = {
                name: formGardenAdd.querySelector("#gardenName").value,
                description: formGardenAdd.querySelector("#gardenDescription").value,
                user_id: formGardenAdd.querySelector("#gardenUserId").value,
            };
            // console.log("** Data:", data);

            try {
                const response = await fetch("/api/gardens", {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json',
                        // 'Authorization': 'Bearer ' + localStorage.getItem('token'),
                    },
                    body: JSON.stringify(data),
                });
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Error on post /api/gardens. TODO Message.');
                }
            } catch (error) {
                console.error('Error on post /api/gardens:', error);
            }
        });
    }
});


// Remove Garden
async function deleteGarden(id) {
    if (confirm('Êtes-vous sûr de vouloir supprimer ce jardin ?')) {
        try {
            const response = await fetch(`/api/gardens/${id}`, {
                method: 'DELETE',
                headers: {
                    'Authorization': 'Basic ' + btoa('admin:mypassword')
                }
            });

            if (response.ok) {
                location.reload();
            } else {
                alert('Erreur lors de la suppression du jardin');
            }
        } catch (error) {
            console.error('Erreur:', error);
        }
    }
}

// Fonction pour éditer un jardin (à implémenter)
function editGarden(id) {
    // TODO: Implémenter la fonction d'édition
    alert('Fonctionnalité en cours de développement');
}
