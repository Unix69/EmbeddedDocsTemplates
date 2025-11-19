document.addEventListener('DOMContentLoaded', () => {
    const isDoxygen = document.location.pathname.includes('/docs/html/');

    document.querySelectorAll('.md-link').forEach(link => {
        const target = isDoxygen ? link.dataset.doxygen : link.dataset.github;

        // Se siamo in Doxygen, usa solo il nome del file senza aggiungere la cartella
        link.href = target;

        console.log(`[md-link] ${link.textContent} -> ${link.href}`);
    });

    // Treeview espandibile
    function initDirectoryTree() {
        document.querySelectorAll('.directory-tree li.folder').forEach(folderLi => {
            folderLi.addEventListener('click', function(e) {
                e.stopPropagation();
                folderLi.classList.toggle('expanded');
            });
        });
    }

    initDirectoryTree();
});