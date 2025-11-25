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
        const doxygenTarget = span.dataset.doxygen; // md_Version_FEATURE.html
        const githubTarget  = span.dataset.github;  // Version/FEATURE.md
        const pathname      = window.location.pathname;

        // Siamo su GitHub Pages?
        const isGitHubPages = window.location.hostname.endsWith('github.io');

        if (isGitHubPages) {
            // Siamo già dentro docs/html
            if (pathname.includes('/docs/html/')) {
                return './' + doxygenTarget; // link relativo dalla pagina corrente
            }
            // Siamo nella root del progetto
            return 'docs/html/' + doxygenTarget;
        }

        // Se siamo su github.com
        if (window.location.hostname === 'github.com') {
            return githubTarget;
        }

        // Fallback generico
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