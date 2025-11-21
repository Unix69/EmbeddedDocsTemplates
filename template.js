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
        if (pathname.includes('/docs/html/')) {
            return doxygenTarget;
        }

        // Caso 2: siamo nella root di GitHub Pages
        // Adatta "EmbeddedDocsTemplates" al tuo repo
        if (/\/EmbeddedDocsTemplates(\/index\.html)?\/?$/.test(pathname)) {
            return 'docs/html/' + doxygenTarget;
        }

        // Caso 3: preview markdown su GitHub
        if (pathname.includes('/EmbeddedDocsTemplates') && !pathname.includes('/docs/html/')) {
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
            if (span.dataset.processed) return;

            const a = document.createElement('a');
            a.textContent = span.textContent.trim();
            a.className = 'md-link-dynamic';
            a.href = buildHref(span);

            span.replaceWith(a); // sostituisce lo span con <a>
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