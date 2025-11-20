// template.js - Gestione automatica dei link .md-link
(function () {
  'use strict';

  const hostname = location.hostname;
  const pathname = location.pathname || '/';
  const isGithubPages = hostname.endsWith('.github.io');
  const isFileProtocol = location.protocol === 'file:';

  // Siamo già dentro docs/html? (es: /EmbeddedDocsTemplates/docs/html/md_README.html)
  const isInDocsHtml =
    pathname.includes('/docs/html/') ||
    pathname.endsWith('/docs/html') ||
    pathname.endsWith('/docs/html/');

  // Ricava il nome repo da /repo/... (per GitHub Pages)
  function getRepoName() {
    const parts = pathname.split('/').filter(Boolean); // rimuove stringhe vuote
    // es: '/EmbeddedDocsTemplates/' => ['EmbeddedDocsTemplates']
    return parts.length > 0 ? parts[0] : '';
  }

  const repo = getRepoName();

  // Base per docs/html su GitHub Pages: https://user.github.io/repo/docs/html/
  function buildDocsHtmlBase() {
    if (!isGithubPages || !repo) return null;
    return location.origin + '/' + repo + '/docs/html/';
  }

  const docsHtmlBase = buildDocsHtmlBase();

  // Unisci segmenti garantendo / singoli e niente // o ///
  function joinPaths(...parts) {
    return parts
      .map((p, i) => {
        if (!p) return '';
        p = String(p).trim();
        if (i > 0) p = p.replace(/^\/+/, ''); // togli / iniziali dai segmenti successivi
        p = p.replace(/\/+$/, '');            // togli / finali
        return p;
      })
      .filter(Boolean)
      .join('/');
  }

  // Calcola href per uno span.md-link
  function computeHref(span) {
    const githubTarget = span.dataset.github || '';
    const doxygenTarget = span.dataset.doxygen || '';

    // 1) Caso: siamo già dentro docs/html (anche in locale con file://)
    if (isInDocsHtml || isFileProtocol) {
      // Se data-doxygen è assoluto (http, https, /...), lo uso così com'è
      if (
        doxygenTarget.startsWith('http://') ||
        doxygenTarget.startsWith('https://') ||
        doxygenTarget.startsWith('/')
      ) {
        return doxygenTarget;
      }
      // Altrimenti lo uso come relativo (md_README.html, md_Project_XXX.html, ecc.)
      if (doxygenTarget) return doxygenTarget;

      // Fallback se manca data-doxygen
      return githubTarget || '#';
    }

    // 2) Caso: siamo sulla root GitHub Pages: https://user.github.io/repo/...
    if (isGithubPages && docsHtmlBase) {
      // Se data-doxygen esiste, vogliamo andare SEMPRE al file HTML di Doxygen
      if (doxygenTarget) {
        // Se per qualche motivo contiene già docs/html, lo ritorno così com'è
        if (doxygenTarget.includes('docs/html')) return doxygenTarget;
        // Costruisco URL assoluto: https://user.github.io/repo/docs/html/md_xxx.html
        return joinPaths(docsHtmlBase, doxygenTarget);
      }

      // Fallback se manca data-doxygen: linko al file della repo (es. PROJECT.md)
      if (githubTarget) {
        // Già assoluto?
        if (
          githubTarget.startsWith('http://') ||
          githubTarget.startsWith('https://') ||
          githubTarget.startsWith('/')
        ) {
          return githubTarget;
        }
        // Relativo alla root del repo
        return joinPaths(location.origin, repo, githubTarget);
      }

      return '#';
    }

    // 3) Altri casi (es: server diverso, sviluppo, ecc.)
    // Se c'è data-doxygen lo uso direttamente (relativo alla pagina corrente)
    if (doxygenTarget) return doxygenTarget;
    // Altrimenti uso data-github
    if (githubTarget) return githubTarget;
    return '#';
  }

  // Trasforma tutti gli span.md-link in <a> cliccabili
  function transformMdLinks() {
    document.querySelectorAll('span.md-link').forEach(span => {
      if (span.dataset.processed === '1') return; // già trasformato

      const href = computeHref(span);

      const a = document.createElement('a');
      a.className = (span.className || '') + ' md-link-dynamic';
      a.href = href;

      // Mantieni dentro eventuali <b>, <i>, ecc.
      while (span.firstChild) {
        a.appendChild(span.firstChild);
      }

      // Copia i data-* per debug se servono
      if (span.dataset.github) a.dataset.github = span.dataset.github;
      if (span.dataset.doxygen) a.dataset.doxygen = span.dataset.doxygen;

      // Mark processed
      a.dataset.processed = '1';

      span.parentNode.replaceChild(a, span);
    });
  }

  // Treeview per la directory
  function initDirectoryTree() {
    document.querySelectorAll('.directory-tree li.folder').forEach(folderLi => {
      if (folderLi.__md_inited) return;
      folderLi.addEventListener('click', function (e) {
        e.stopPropagation();
        folderLi.classList.toggle('expanded');
      });
      folderLi.__md_inited = true;
    });
  }

  // Esegui subito dopo caricamento DOM
  document.addEventListener('DOMContentLoaded', () => {
    transformMdLinks();
    initDirectoryTree();

    // Osserva cambiamenti (es: Doxygen inietta header/footer dopo)
    const observer = new MutationObserver(() => {
      transformMdLinks();
      initDirectoryTree();
    });
    observer.observe(document.body, { childList: true, subtree: true });
  });
})();