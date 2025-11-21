document.addEventListener('DOMContentLoaded', () => {

    function isGithubPages() {
        return window.location.hostname.includes("github.io");
    }

    function isDoxygen() {
        return window.location.pathname.includes('/docs/html/');
    }

    /**
     * Trasforma i link _8md.html generati da Doxygen in md_XXX.html
     * Esempio: PROJECT_8md.html → md_PROJECT.html
     */
    function normalizeDoxygenLink(href) {
        // Matcha qualsiasi file tipo "NAME_8md.html"
        return href.replace(/([^\/]+)_8md\.html$/, (_, name) => {
            // Se era un file in Usage/... mantieni il prefisso
            if (name.includes('Usage_')) {
                return 'md_' + name.replace('Usage_', 'Usage_') + '.html';
            }
            return 'md_' + name + '.html';
        });
    }

    function buildHref(span) {
        const doxygenTarget = span.dataset.doxygen;
        const githubTarget  = span.dataset.github;

        if (isDoxygen()) {
            // Se Doxygen ha generato il _8md.html, convertiamo in md_XXX.html
            return normalizeDoxygenLink(doxygenTarget);
        }

        if (isGithubPages()) {
            // Se siamo su github.io → link verso GitHub
            return githubTarget;
        }

        // Fallback generico: usa Doxygen
        return normalizeDoxygenLink(doxygenTarget);
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