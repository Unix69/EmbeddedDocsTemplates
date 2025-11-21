document.addEventListener('DOMContentLoaded', () => {

    function isDoxygen() {
        // Siamo in Doxygen / GitHub Pages con HTML generato
        return window.location.pathname.includes('/docs/html/');
    }

    function buildHref(span) {
        const doxygenTarget = span.dataset.doxygen;
        const githubTarget  = span.dataset.github;

        if (isDoxygen()) {
            // Tutti i file HTML di Doxygen stanno in docs/html/
            return doxygenTarget;  // es: "md_PROJECT.html"
        }

        // Fuori da Doxygen (es. preview HTML locale): se vuoi puoi usare ancora i .md
        return githubTarget || '#';
    }

    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            // Se non siamo in Doxygen, lascia stare: GitHub userà il link interno <a href="...md">
            if (!isDoxygen()) {
                return;
            }

            if (span.dataset.processed) return;

            const href = buildHref(span);
            const text = span.textContent.trim();

            const a = document.createElement('a');
            a.textContent = text;
            a.className   = 'md-link-dynamic';
            a.href        = href;

            // Sostituisco l'intero contenuto dello span con il nuovo <a>
            span.innerHTML = '';
            span.appendChild(a);

            span.dataset.processed = 'true';
        });
    }

    // Esegui subito
    updateMdLinks();

    // Osserva il DOM per eventuali cambi dinamici (es. Doxygen che inietta roba)
    const observer = new MutationObserver(() => {
        updateMdLinks();
    });
    observer.observe(document.body, { childList: true, subtree: true });

    // Treeview (come avevi già)
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