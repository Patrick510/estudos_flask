function deleteAula(textId) {
  fetch(`/delete/${textId}`, {
    method: "DELETE",
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById(`item-${textId}`).remove();
      alert(data.message);
    })
    .catch((error) => {
      alert("Erro ao excluir o texto.");
    });
}
