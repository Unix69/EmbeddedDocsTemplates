document.addEventListener('DOMContentLoaded', () => {

    function isDoxygen() {
        // Quando siamo nella documentazione generata (anche su GitHub Pages)
        return window.location.pathname.includes('/docs/html/');
    }

    function isGitHubWeb() {
        // Quando apri i .md direttamente su github.com
        return window.location.hostname === 'github.com';
    }

    function buildHref(span) {
        const githubTarget  = span.dataset.github;   // .md
        const doxygenTarget = span.dataset.doxygen;  // HTML generato da Doxygen

        if (isDoxygen()) {
            // Qui trasformiamo PROJECT_8md.html → md_PROJECT.html
            return doxygenTarget.replace(/^([A-Z0-9_]+)_8md\.html$/, (_, name) => `md_${name}.html`);
        }

        if (isGitHubWeb()) {
            // Puntiamo ai .md su GitHub
            return githubTarget;
        }

        // Fallback generico (apertura locale dei .html di Doxygen)
        return doxygenTarget.replace(/^([A-Z0-9_]+)_8md\.html$/, (_, name) => `md_${name}.html`);
    }

    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            if (span.dataset.processed) return;

            const a = document.createElement('a');
            a.textContent = span.textContent;
            a.className = 'md-link-dynamic';
            a.href = buildHref(span);

            span.replaceWith(a);
        });
    }

    // Esegui subito
    updateMdLinks();

    // Osserva il DOM per eventuali elementi aggiunti dopo
    const observer = new MutationObserver(updateMdLinks);
    observer.observe(document.body, { childList: true, subtree: true });

    // Treeview folders
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