document.addEventListener('DOMContentLoaded', () => {
    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            if (span.dataset.processed) return;

            let target;
            const isHtmlPage = document.location.pathname.endsWith('.html');

            if (isHtmlPage) {
                // Cartella corrente della pagina
                const currentDir = document.location.pathname.replace(/\/[^\/]*$/, '/');
                target = span.dataset.doxygen;

                // Se il link non ha già "docs/html" lo aggiungiamo
                if (!target.includes('docs/html')) {
                    target = 'docs/html/' + target;
                }

                // Rendiamo il percorso relativo alla pagina corrente
                const pageDepth = currentDir.split('/').length - 2; // -2 perché pathname inizia con /
                let prefix = '';
                for (let i = 0; i < pageDepth; i++) prefix += '../';
                target = prefix + target.replace(/^docs\/html\//, '');
            } else {
                target = span.dataset.github;
            }

            const a = document.createElement('a');
            a.href = target;
            a.textContent = span.textContent;
            a.className = 'md-link-dynamic';

            span.replaceWith(a);
            span.dataset.processed = true;
        });
    }

    updateMdLinks();

    const observer = new MutationObserver(updateMdLinks);
    observer.observe(document.body, { childList: true, subtree: true });

    document.querySelectorAll('.directory-tree li.folder').forEach(folderLi => {
        folderLi.addEventListener('click', e => {
            e.stopPropagation();
            folderLi.classList.toggle('expanded');
        });
    });
});