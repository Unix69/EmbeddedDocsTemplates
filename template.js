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
        const doxygenTarget = span.dataset.doxygen; // es: "md_Version_FEATURE.html"
        const githubTarget  = span.dataset.github;  // es: "Version/FEATURE.md" o "../PROJECT.md"
        const path          = window.location.pathname;

        // 1) Sei già su una pagina md_*.html di Doxygen
        //    → usa SEMPRE il valore di data-doxygen, SENZA modifiche.
        if (isDoxygenMarkdownPage()) {
            return doxygenTarget;
        }

        // 2) Sei sulla root GitHub Pages del progetto
        //    → punta alla pagina HTML di Doxygen corrispondente, sotto docs/html/
        if (isOnProjectRoot()) {
            return 'docs/html/' + doxygenTarget;
        }

        // 3) Sei nel repo su GitHub, visualizzando i .md
        //    (es: https://github.com/unix69/EmbeddedDocsTemplates/blob/main/README.md)
        if (path.includes('/EmbeddedDocsTemplates') && !path.includes('/docs/html/')) {
            // In questo contesto vogliamo tenere il link ai file .md
            return githubTarget;
        }

        // 4) Fallback generico: preferisci data-doxygen, altrimenti data-github
        return doxygenTarget || githubTarget || '#';
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