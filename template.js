document.addEventListener('DOMContentLoaded', () => {

    // heuristica rapida: siamo chiaramente nell'output html di doxygen?
    const looksLikeDoxygen = () => {
        const p = location.pathname;
        if (p.endsWith('.html')) return true;
        if (p.includes('/docs/html/')) return true;
        // altri casi personalizzabili...
        return false;
    };

    // prova ad effettuare un HEAD sul path per vedere se esiste (fallback silenzioso)
    async function existsHead(path) {
        try {
            const resp = await fetch(path, { method: 'HEAD' });
            return resp.ok;
        } catch (e) {
            return false;
        }
    }

    // risolvi il target effettivo per uno span (prova d'abord d o y x, poi fallback a github)
    async function resolveTarget(span) {
        const dox = span.dataset.doxygen;
        const gh  = span.dataset.github;

        // se stiamo già in un file .html / doxygen, preferiamo doxygen
        if (looksLikeDoxygen()) {
            if (dox) return dox;
            if (gh) return gh;
            return '#';
        }

        // altrimenti, tentiamo di verificare se il file d o y x è raggiungibile:
        if (dox) {
            // prova diretta
            if (await existsHead(dox)) return dox;

            // prova con una possibile cartella docs/html/ (se tu pubblichi con docs/html)
            const prefixed = 'docs/html/' + dox;
            if (await existsHead(prefixed)) return prefixed;

            // prova con root basename (es. /EmbeddedDocsTemplates/md_README.html)
            const base = location.pathname.replace(/\/$/, '');
            const alt = base ? (base + '/' + dox) : dox;
            if (await existsHead(alt)) return alt;
        }

        // fallback: link markdown per GitHub repo (o data-github)
        if (gh) return gh;
        return dox || '#';
    }

    // converte ogni .md-link in <a href=...> con risoluzione asincrona
    async function updateMdLinks() {
        const spans = Array.from(document.querySelectorAll('.md-link'));
        for (const span of spans) {
            // evita doppia trasformazione
            if (span.dataset.processed) continue;

            const target = await resolveTarget(span);

            const a = document.createElement('a');
            a.href = target || '#';
            // mantieni la stessa classe (ma evita di rompere altre cose)
            a.className = (span.className ? span.className + ' ' : '') + 'md-link-dynamic';
            // usa innerHTML per preservare <b>, <code>, ecc.
            a.innerHTML = span.innerHTML;

            // sostituisci e marca l'ancora esistente
            span.replaceWith(a);
            a.dataset.processed = 'true';
        }
    }

    // esegui la prima conversione
    updateMdLinks();

    // osservatore per elementi aggiunti dinamicamente (es. header/footer inserti da doxygen)
    const observer = new MutationObserver(() => {
        updateMdLinks();
    });
    observer.observe(document.body, { childList: true, subtree: true });

    // Treeview espandibile
    function initDirectoryTree() {
        document.querySelectorAll('.directory-tree li.folder').forEach(folderLi => {
            // usa 'pointerdown' o 'click' in base al comportamento voluto
            folderLi.addEventListener('click', function(e) {
                e.stopPropagation();
                folderLi.classList.toggle('expanded');
            });
        });
    }

    initDirectoryTree();
});