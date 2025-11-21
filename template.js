document.addEventListener('DOMContentLoaded', () => {

    function isGithubPages() {
        return window.location.hostname.includes("github.io");
    }

    function isDoxygen() {
        return window.location.pathname.includes('/docs/html/');
    }

    function buildHref(span) {
        const doxygenTarget = span.dataset.doxygen;
        const githubTarget  = span.dataset.github;

        console.log(doxygenTarget);
        console.log(githubTarget);

        if (isDoxygen()) {
            console.log(doxygenTarget);
            // Tutti i file HTML di Doxygen sono nella stessa cartella
            return doxygenTarget;
        }

        if (isGithubPages()) {
            // Link puntano ai .md su GitHub
            console.log(githubTarget);
        }

        // Fallback generico: usa Doxygen se apri da filesystem
        return doxygenTarget;
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