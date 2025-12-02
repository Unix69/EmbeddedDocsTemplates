document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".md-link").forEach(span => {
    const htmlTarget = span.dataset.doxygen;
    if (!htmlTarget) return;

    // Se siamo su GitHub Pages, sostituiamo href con il link .html
    if (window.location.hostname.endsWith("github.io")) {
      let a = span.querySelector("a");
      if (a) {
        // Aggiustamento relativo rispetto alla posizione corrente
        const pathParts = window.location.pathname.split("/").filter(Boolean);
        const depth = pathParts.includes("html") ? pathParts.length - pathParts.indexOf("html") - 1 : 0;
        const prefix = "../".repeat(depth);
        a.href = prefix + htmlTarget;
      }
    }
  });
});