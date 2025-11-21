document.addEventListener('DOMContentLoaded', () => {

    function isGitHub() {
        return window.location.hostname === "github.com";
    }

    function isGitHubPages() {
        return window.location.hostname.includes("github.io");
    }

    function isDoxygen() {
        return window.location.pathname.includes('/docs/html/');
    }

    function normalizeDoxygenLink(link) {
        if (link.startsWith('md_') && link.endsWith('.html')) return link;
        return link.replace(/^(.*)_8md\.html$/, 'md_$1.html');
    }

    function buildHref(span) {
        const doxygenTarget = span.dataset.doxygen;
        const githubTarget  = span.dataset.github;

        if (isGitHub()) {
            // su GitHub punta al .md originale
            return githubTarget;
        }

        if (isGitHubPages() && isDoxygen()) {
            // su GitHub Pages con Doxygen, punta a md_XXX.html
            return normalizeDoxygenLink(doxygenTarget);
        }

        // fallback locale
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

    updateMdLinks();

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