document.addEventListener('DOMContentLoaded', () => {

    function getRelativePrefix() {
        const depth = location.pathname.split('/').length - 3; 
        // -3 perché: ["", "EmbeddedDocsTemplates", "docs", "html", "md_PROJECT.html"]
        // depth = 1 se sei in docs/html/md_PROJECT.html
        return '../'.repeat(depth > 0 ? depth : 0);
    }

    const relativePrefix = getRelativePrefix();

    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            if (span.dataset.processed === 'true') return;

            let target;

            if (location.hostname.endsWith('.github.io')) {
                // Su GitHub Pages punta sempre all'HTML generato
                target = relativePrefix + span.dataset.doxygen;
            } else {
                // Su GitHub repo punta al .md
                target = span.dataset.github;
            }

            const a = document.createElement('a');
            a.href = target;
            a.className = 'md-link-dynamic';
            a.innerHTML = span.innerHTML;
            a.dataset.processed = 'true';

            span.replaceWith(a);
        });
    }

    updateMdLinks();

    const observer = new MutationObserver(() => updateMdLinks());
    observer.observe(document.body, { childList: true, subtree: true });

    document.querySelectorAll('.directory-tree li.folder').forEach(folderLi => {
        folderLi.addEventListener('click', e => {
            e.stopPropagation();
            folderLi.classList.toggle('expanded');
        });
    });
});