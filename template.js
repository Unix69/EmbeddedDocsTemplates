document.addEventListener('DOMContentLoaded', () => {

    // Siamo su GitHub Pages? (https://<user>.github.io/<repo>/...)
    const isGitHubPages = location.hostname.endsWith('.github.io');

    // Siamo dentro l'output HTML di Doxygen (docs/html/ o pagina md_*.html)?
    const isDoxygenHtml = (
        location.pathname.includes('/docs/html/') ||
        location.pathname.match(/\/md_.*\.html$/)
    );

    function updateMdLinks() {
        document.querySelectorAll('.md-link').forEach(span => {
            // Evita di trasformare di nuovo se già fatto
            if (span.dataset.processed === 'true') return;

            const gh  = span.dataset.github;
            const dox = span.dataset.doxygen;

            let target = '#';

            if (isDoxygenHtml) {
                // Dentro Doxygen HTML: usa SEMPRE il target HTML (md_*.html)
                if (dox) {
                    target = dox;
                } else if (gh) {
                    target = gh;
                }
            } else if (isGitHubPages) {
                // Su GitHub Pages MA fuori da docs/html: punta a docs/html/md_*.html
                if (dox) {
                    // se già contiene docs/html, non lo raddoppiamo
                    if (dox.startsWith('docs/html/')) {
                        target = dox;
                    } else {
                        target = 'docs/html/' + dox;
                    }
                } else if (gh) {
                    // fallback: usa markdown (meno ideale, ma almeno qualcosa)
                    target = gh;
                }
            } else {
                // Su GitHub "normale" (vista repository): punta ai .md
                if (gh) {
                    target = gh;
                } else if (dox) {
                    target = dox;
                }
            }

            // Crea il vero <a> e sostituisci lo span
            const a = document.createElement('a');
            a.href = target;
            a.className = (span.className ? span.className + ' ' : '') + 'md-link-dynamic';
            a.innerHTML = span.innerHTML;

            // marca come processato per sicurezza
            a.dataset.processed = 'true';

            span.replaceWith(a);
        });
    }

    // Prima trasformazione
    updateMdLinks();

    // Osserva il DOM per header/footer caricati da Doxygen
    const observer = new MutationObserver(() => {
        updateMdLinks();
    });
    observer.observe(document.body, { childList: true, subtree: true });

    // Treeview espandibile (come avevi)
    function initDirectoryTree() {
        document.querySelectorAll('.directory-tree li.folder').forEach(folderLi => {
            folderLi.addEventListener('click', function (e) {
                e.stopPropagation();
                folderLi.classList.toggle('expanded');
            });
        });
    }

    initDirectoryTree();
});