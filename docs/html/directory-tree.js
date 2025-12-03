document.addEventListener("DOMContentLoaded", () => {
    // Menu directory-tree espandibile/collassabile
  document.querySelectorAll(".directory-tree .folder").forEach(folder => {
    folder.addEventListener("click", e => {
      e.stopPropagation(); // Previene click sui parent
      folder.classList.toggle("expanded"); // <-- cambia open -> expanded
    });
  });
});