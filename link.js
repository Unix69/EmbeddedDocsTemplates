// template.js — usa SOLO data-doxygen + href-md esistente
document.addEventListener("DOMContentLoaded", () => {

  // Controlla se siamo su GitHub Pages (github.io)
  const isGitHubPages = window.location.hostname.endsWith("github.io");

  // Restituisce il nuovo href da usare (solo per github.io)
  function getDoxygenHref(doxygenTarget) {
    if (!doxygenTarget) return null;

    const path = window.location.pathname || "";
    // se siamo già dentro docs/html/ (es: /EmbeddedDocsTemplates/docs/html/md_README.html)
    if (path.includes("/docs/html/")) {
      // i file md_*.html sono nella stessa cartella
      return "./" + doxygenTarget;
    }
    // se siamo in root o altrove (es: index.html)
    return "docs/html/" + doxygenTarget;
  }

  // Applica la logica ai .md-link presenti nel DOM
  function applyMdLinks() {
    document.querySelectorAll("span.md-link").forEach(span => {
      const a = span.querySelector("a");
      if (!a) return; // se non c'è <a> salta

      // Prendi il valore data-doxygen
      const doxygenTarget = span.dataset.doxygen?.trim();

      // Se siamo su github.io e c'è data-doxygen → sostituisci href
      if (isGitHubPages && doxygenTarget) {
        const newHref = getDoxygenHref(doxygenTarget);
        if (newHref) a.setAttribute("href", newHref);
      }

      // altrimenti NON toccare l'href (rimane quello .md già presente)
    });
  }

  // Esegui ora
  applyMdLinks();

  // Osserva il DOM per future modifiche/iniezioni (Doxygen)
  const observer = new MutationObserver(() => applyMdLinks());
  observer.observe(document.body, { childList: true, subtree: true });

});