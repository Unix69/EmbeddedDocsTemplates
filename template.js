document.addEventListener('DOMContentLoaded', () => {

    //
    // RILEVAMENTO CONTESTO
    //

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

    //
    // COSTRUZIONE HREF
    //

    function buildHref(span) {
        const doxygenTarget = span.dataset.doxygen; // md_PROJECT.html
        const githubTarget  = span.dataset.github;  // PROJECT.md
        const pathname      = window.location.pathname;

        // Caso 1: già in docs/html (Doxygen)
        // ➜ Usa SEMPRE data-doxygen così com'è
        if (pathname.includes('/docs/html/')) {
            return doxygenTarget;
        }

        // Caso 2: siamo nella root di GitHub Pages
        // Es: https://unix69.github.io/EmbeddedDocsTemplates/
        if (/\/EmbeddedDocsTemplates(\/index\.html)?\/?$/.test(pathname)) {
            return 'docs/html/' + doxygenTarget;
        }

        // Caso 3: preview markdown su GitHub (o altre viste non Doxygen)
        if (pathname.includes('/EmbeddedDocsTemplates') && !pathname.includes('/docs/html/')) {
            // Qui ha senso mandare direttamente al .md su GitHub
            return githubTarget;
        }

        // Fallback generico
        return doxygenTarget;
    }

    //
    // GESTIONE SPAN .md-link
    //

    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            if (span.dataset.processed === 'true') return;

            const a = span.querySelector('a');
            if (!a) return; // niente <a> dentro, niente da fare

            // Usa sempre buildHref per determinare il link finale
            a.href = buildHref(span);

            // segna lo span come già processato
            span.dataset.processed = 'true';
        });
    }

    // Esegui subito
    updateMdLinks();

    // Osserva il DOM per eventuali elementi aggiunti dopo (es. Doxygen che carica parti dinamiche)
    const observer = new MutationObserver(() => {
        updateMdLinks();
    });
    observer.observe(document.body, { childList: true, subtree: true });

    //
    // TREEVIEW CARTELLE
    //
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