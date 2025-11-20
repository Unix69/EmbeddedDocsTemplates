document.addEventListener('DOMContentLoaded', () => {

    function isOnGitHubPagesRoot() {
        // Esempio: /EmbeddedDocsTemplates/   (index.html "root" del progetto)
        const path = window.location.pathname;
        return /\/EmbeddedDocsTemplates\/?$/.test(path);
    }

    function isInDocsHtml() {
        // Esempio: /EmbeddedDocsTemplates/docs/html/md_README.html
        return window.location.pathname.includes('/docs/html/');
    }

    function buildHrefFromDataset(span) {
        const doxygenTarget = span.dataset.doxygen;
        const githubTarget  = span.dataset.github;

        if (isInDocsHtml()) {
            // Siamo già in docs/html → link relativi alla stessa cartella
            return doxygenTarget; // es: "md_Version_FEATURE.html"
        }

        if (isOnGitHubPagesRoot()) {
            // Siamo su https://unix69.github.io/EmbeddedDocsTemplates/
            // → dobbiamo andare in docs/html/<pagina_doxygen>
            return 'docs/html/' + doxygenTarget; // es: "docs/html/md_README.html"
        }

        // Caso generico (ad esempio se apri il file HTML dal filesystem o da altre path)
        // Fallback: se siamo in un .html, usa doxygen; altrimenti github
        if (window.location.pathname.endsWith('.html')) {
            return doxygenTarget;
        } else {
            return githubTarget;
        }
    }

    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            if (span.dataset.processed) return;

            const a = document.createElement('a');
            a.textContent = span.textContent;
            a.className   = 'md-link-dynamic';
            a.href        = buildHrefFromDataset(span);

            // sostituisco lo span con <a>
            span.replaceWith(a);

            // (NB: non puoi più settare dataset.processed sullo span perché è stato rimosso;
            // se vuoi, puoi usare un attributo su <a>, ma non è strettamente necessario)
        });
    }

    // Esegui subito
    updateMdLinks();

    // Osserva il DOM per eventuali elementi aggiunti dopo
    const observer = new MutationObserver(() => {
        updateMdLinks();
    });
    observer.observe(document.body, { childList: true, subtree: true });

    // Treeview
    function initDirectoryTree() {
        document.querySelectorAll('.directory-tree li.folder').forEach(folderLi => {
            folderLi.addEventListener('click', function(e) {
                e.stopPropagation();
                folderLi.classList.toggle('expanded');
            });
        });
    }

    initDirectoryTree();
});