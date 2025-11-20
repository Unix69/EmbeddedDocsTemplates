document.addEventListener('DOMContentLoaded', () => {

    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            if (span.dataset.processed) return;

            let target;
            if (document.location.pathname.endsWith('.html')) {
                // Se siamo in HTML Doxygen
                target = span.dataset.doxygen;

                // Solo se non contiene già 'docs/html/' aggiungila
                if (!target.startsWith('docs/html/')) {
                    target = 'docs/html/' + target;
                }
            } else {
                // GitHub repo
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

    // Treeview espandibile
    document.querySelectorAll('.directory-tree li.folder').forEach(folderLi => {
        folderLi.addEventListener('click', e => {
            e.stopPropagation();
            folderLi.classList.toggle('expanded');
        });
    });

});