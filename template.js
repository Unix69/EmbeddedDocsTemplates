document.addEventListener("DOMContentLoaded", () => {

  // Costruisce l'href corretto per una span .md-link
  function buildHref(span) {
    const doxygenTarget = span.dataset.doxygen; // es: md_PROJECT.html
    const githubTarget = span.dataset.github;   // es: PROJECT.md

    const pathname = window.location.pathname;  // percorso della pagina corrente
    const isGitHubPages = window.location.hostname.endsWith("github.io");

    if (isGitHubPages) {
      // Calcola la profondità della pagina corrente rispetto a docs/html/
      const parts = pathname.split("/").filter(p => p); // rimuove vuoti
      const htmlIndex = parts.indexOf("html");
      let depth = 0;
      if (htmlIndex >= 0) {
        // numero di cartelle sotto docs/html/ prima del file corrente
        depth = parts.length - (htmlIndex + 1) - 1;
      }
      const prefix = "../".repeat(depth); // risale la cartella corretta
      return prefix + doxygenTarget;
    }

    // Se siamo su github.com, mantieni il link al file sorgente
    if (window.location.hostname === "github.com") {
      return githubTarget;
    }

    // fallback generico
    return doxygenTarget;
  }

  // Aggiorna tutti i link .md-link presenti e futuri
  function updateMdLinks() {
    document.querySelectorAll(".md-link").forEach(span => {
      if (span.dataset.processed === "true") return;
      const a = span.querySelector("a");
      if (!a) return;
      a.href = buildHref(span);
      span.dataset.processed = "true";
    });
  }

  // Esegui subito la sostituzione
  updateMdLinks();

  // MutationObserver per catturare eventuali nodi aggiunti dinamicamente (Doxygen)
  const observer = new MutationObserver(() => {
    updateMdLinks();
  });
  observer.observe(document.body, { childList: true, subtree: true });

});