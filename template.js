document.addEventListener("DOMContentLoaded", () => {

  function buildHref(span) {
    const doxygenTarget = span.dataset.doxygen; // md_*.html
    const githubTarget = span.dataset.github;   // *.md

    const pathname = window.location.pathname; // percorso della pagina corrente
    const isGitHubPages = window.location.hostname.endsWith("github.io");

    if (isGitHubPages) {
      // Percorso relativo robusto
      // Se il file corrente è in docs/html/, risali alla root se necessario
      let prefix = "";
      if (pathname.includes("/docs/html/")) {
        const depth = pathname.split("/").length - pathname.split("/").indexOf("html") - 2;
        prefix = "../".repeat(depth);
      }

      // Aggiungi cartella docs/html se il target è in docs/html/
      if (doxygenTarget.startsWith("md_") && !doxygenTarget.includes("_root_")) {
        if (!pathname.endsWith(doxygenTarget)) {
          if (!doxygenTarget.startsWith("docs/html/") && doxygenTarget !== "md_PROJECT.html") {
            prefix += "docs/html/";
          }
        }
      }
      return prefix + doxygenTarget;
    }

    // Su github.com usa il file md
    if (window.location.hostname === "github.com") {
      return githubTarget;
    }

    return doxygenTarget;
  }

  function updateMdLinks() {
    document.querySelectorAll(".md-link").forEach(span => {
      if (span.dataset.processed === "true") return;
      const a = span.querySelector("a");
      if (!a) return;
      a.href = buildHref(span);
      span.dataset.processed = "true";
    });
  }

  updateMdLinks();

  // Observer per nodi aggiunti dinamicamente da Doxygen
  const observer = new MutationObserver(() => updateMdLinks());
  observer.observe(document.body, { childList: true, subtree: true });

});