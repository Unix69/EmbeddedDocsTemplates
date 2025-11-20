document.addEventListener('DOMContentLoaded', () => {

    // Funzione per convertire tutti gli span.md-link in link <a>
    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            // Evita di ricreare più volte il link se già trasformato
            if (span.dataset.processed) return;

            const isHtmlPage = document.location.pathname.endsWith('.html');

            // Determina il target corretto
            let target = isHtmlPage ? span.dataset.doxygen : span.dataset.github;

            // Se siamo in una pagina HTML e NON dentro docs/html/, aggiungi il prefisso docs/html/
            if (isHtmlPage && !document.location.pathname.includes('/docs/html/')) {
                target = 'docs/html/' + target;
            }

            const a = document.createElement('a');
            a.href = target;
            a.textContent = span.textContent;
            a.className = 'md-link-dynamic';

            span.replaceWith(a);
            span.dataset.processed = true;
        });
    }

    // Aggiorna i link già presenti all'avvio
    updateMdLinks();

    // Osserva il DOM per eventuali aggiunte future (es. footer/header inclusi)
    const observer = new MutationObserver(() => {
        updateMdLinks();
    });
    observer.observe(document.body, { childList: true, subtree: true });

    // Treeview espandibile
    function initDirectoryTree() {
        document.querySelectorAll('.directory-tree li.folder').forEach(folderLi => {
            folderLi.addEventListener('click', function(e) {
                e.stopPropagation();
                folderLi.classList.toggle('expanded');
            });
        });
    }

    // Inizializza treeview
    initDirectoryTree();
});