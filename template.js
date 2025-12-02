ocument.addEventListener('DOMContentLoaded', () => {

    //
    // RILEVAMENTO CONTESTO
    //

    // Siamo in una pagina markdown di Doxygen?
    // Esempi:
    //  - /EmbeddedDocsTemplates/docs/html/md_README.html
    //  - /EmbeddedDocsTemplates/docs/html/md_Version_FEATURE.html
    function isDoxygenMarkdownPage() {
        const path = window.location.pathname;
        return path.includes('/docs/html/md_');
    }

    // Siamo nella root di GitHub Pages del progetto?
    // Es: /EmbeddedDocsTemplates/  oppure /EmbeddedDocsTemplates/index.html
    function isOnProjectRoot() {
        const path = window.location.pathname;
        return /\/EmbeddedDocsTemplates(\/index\.html)?\/?$/.test(path);
    }

    //
    // COSTRUZIONE HREF
    //

    function buildHref(span) {
        const doxygenTarget = span.dataset.doxygen;
        const githubTarget = span.dataset.github;

        const pathname = window.location.pathname; // es: /docs/html/md_Version_NAMESPACE.html
        const pathParts = pathname.split('/').filter(p => p);
        // calcola profondità sotto docs/html/
        let depth = 0;
        const docsIndex = pathParts.indexOf('html'); // docs/html/...
        if (docsIndex >= 0) {
            depth = pathParts.length - (docsIndex + 1) - 1; // -1 per il file corrente
        }

        const prefix = '../'.repeat(depth);

        if (window.location.hostname.endsWith('github.io')) {
            return prefix + doxygenTarget; // link relativo corretto
        }
        if (window.location.hostname === 'github.com') {
            return githubTarget;
        }
        return doxygenTarget;
    }

    //
    // GESTIONE SPAN .md-link
    //
    // N.B.: NON sostituiamo lo span con una nuova <a>,
    //       ma prendiamo la <a> esistente e ne modifichiamo solo l'href.
    //

    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            if (span.dataset.processed === 'true') return;

            const a = span.querySelector('a');
            if (!a) return;

            const href = buildHref(span);
            if (href) {
                a.href = href;
            }

            span.dataset.processed = 'true';
        });
    }

    // Esegui subito
    updateMdLinks();

    // Osserva il DOM per eventuali elementi aggiunti dopo (Doxygen a volte inietta cose)
    const observer = new MutationObserver(() => {
        updateMdLinks();
    });
    observer.observe(document.body, { childList: true, subtree: true });

    //
    // TREEVIEW CARTELLE (se usi quella parte)
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