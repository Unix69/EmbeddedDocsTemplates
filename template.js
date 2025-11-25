document.addEventListener('DOMContentLoaded', () => {

    //
    // RILEVAMENTO CONTESTO
    //

    // Siamo in una pagina di documentazione Doxygen per markdown?
    // Es: /EmbeddedDocsTemplates/docs/html/md_README.html
    function isDoxygenMarkdownPage() {
        const path = window.location.pathname;
        return path.includes('/docs/html/md_');
    }

    // Siamo nella root di GitHub Pages del progetto?
    // Es: /EmbeddedDocsTemplates/  oppure /EmbeddedDocsTemplates/index.html
    function isOnProjectRoot() {
        const path = window.location.pathname;
        // Adatta "EmbeddedDocsTemplates" al nome del repo
        return /\/EmbeddedDocsTemplates(\/index\.html)?\/?$/.test(path);
    }

    //
    // COSTRUZIONE HREF
    //

    function buildHref(span) {
        const doxygenTarget = span.dataset.doxygen; // es: "md_Version_FEATURE.html"
        const githubTarget  = span.dataset.github;  // es: "Version/FEATURE.md" o "../PROJECT.md"
        const path          = window.location.pathname;

        // 1) Se siamo in una pagina md_*.html di Doxygen:
        //    usa SEMPRE il valore di data-doxygen così com'è.
        if (isDoxygenMarkdownPage()) {
            return doxygenTarget;
        }

        // 2) Se siamo nella root del progetto GitHub Pages:
        //    prefix "docs/html/" a data-doxygen.
        if (isOnProjectRoot()) {
            return 'docs/html/' + doxygenTarget;
        }

        // 3) Se siamo dentro il repo su GitHub (visualizzazione dei .md):
        //    usa il link al file markdown.
        if (path.includes('/EmbeddedDocsTemplates') && !path.includes('/docs/html/')) {
            return githubTarget;
        }

        // 4) Fallback: prova con data-doxygen se esiste, altrimenti data-github
        return doxygenTarget || githubTarget || '#';
    }

    //
    // GESTIONE SPAN .md-link
    //

    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            if (span.dataset.processed === 'true') return;

            const a = span.querySelector('a');
            if (!a) return;

            a.href = buildHref(span);
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