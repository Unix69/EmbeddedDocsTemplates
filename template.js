document.addEventListener('DOMContentLoaded', () => {

    // Siamo già nella documentazione Doxygen?
    // Es: /EmbeddedDocsTemplates/docs/html/md_README.html
    function isInDoxygenDocs() {
        return window.location.pathname.includes('/docs/html/');
    }

    // Siamo nella root di GitHub Pages del progetto?
    // Es: /EmbeddedDocsTemplates/  oppure /EmbeddedDocsTemplates/index.html
    function isOnProjectRoot() {
        const path = window.location.pathname;
        // Adatta "EmbeddedDocsTemplates" al tuo repo se cambi nome
        return /\/EmbeddedDocsTemplates(\/index\.html)?\/?$/.test(path);
    }

    // Costruisce l'href corretto a partire dai data-*
    function buildHref(span) {
        const doxygenTarget = span.dataset.doxygen; // es: "md_PROJECT.html"
        const githubTarget  = span.dataset.github;  // es: "PROJECT.md"

        // 1) Se siamo già dentro docs/html, i link Doxygen sono "piatti"
        //    es: md_PROJECT.html è nella stessa cartella della pagina corrente
        if (isInDoxygenDocs()) {
            return doxygenTarget;
        }

        // 2) Se siamo sulla root del progetto GitHub Pages,
        //    vogliamo andare nella documentazione Doxygen:
        //    /EmbeddedDocsTemplates/docs/html/md_PROJECT.html
        if (isOnProjectRoot()) {
            return 'docs/html/' + doxygenTarget;
        }

        // 3) Fallback: se per qualche motivo sei in un'altra pagina HTML,
        //    preferisci comunque la doc Doxygen (caso generico)
        if (window.location.pathname.endsWith('.html')) {
            return doxygenTarget;
        }

        // 4) Se proprio non siamo in un contesto HTML (es: preview MD in GitHub),
        //    usiamo il link alla versione Markdown del repo
        return githubTarget;
    }

    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            if (span.dataset.processed) return;
            
            const a = document.createElement('a');
            a.textContent = span.textContent;
            a.className   = 'md-link-dynamic';
            a.href        = buildHref(span);

            // Se vuoi, puoi copiare anche eventuali classi extra dello span
            // a.classList.add(...span.classList);

            span.replaceWith(a);
        });
    }

    // Esegui subito
    updateMdLinks();

    // Osserva il DOM per eventuali elementi aggiunti dopo (es. Doxygen che carica parti dinamiche)
    const observer = new MutationObserver(() => {
        updateMdLinks();
    });
    observer.observe(document.body, { childList: true, subtree: true });

    // Treeview cartelle (come avevi già)
    function initDirectoryTree() {
        document.querySelectorAll('.directory-tree li.folder').forEach(folderLi => {
            folderLi.addEventListener('click', e => {
                e.stopPropagation();
                folderLi.classList.toggle('expanded');
            });
        });
    }

    initDirectoryTree();
});