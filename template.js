function initDirectoryTree() {
    document.querySelectorAll('.directory-tree li.folder').forEach(function(li) {
        li.addEventListener('click', function(e) {
            e.stopPropagation();
            li.classList.toggle('expanded');
        });
    });
}

// Se il documento è ancora in caricamento, aspetta DOMContentLoaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDirectoryTree);
} else {
    // DOM già pronto (es. script in fondo al body)
    initDirectoryTree();
}