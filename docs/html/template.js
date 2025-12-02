function buildHref(span) {
    const doxygenTarget = span.dataset.doxygen; // md_*.html
    const githubTarget = span.dataset.github;   // *.md

    const isGitHubPages = window.location.hostname.endsWith("github.io");
    if (isGitHubPages) {
        // Sempre relativi alla root di docs/html
        return "./" + doxygenTarget; // se sei già in docs/html, "./md_README.html"
    }

    // GitHub.com → punta ai file .md nella repo
    return githubTarget;
}

function updateMdLinks() {
    document.querySelectorAll(".md-link").forEach(span => {
        if (span.dataset.processed === "true") return;
        const a = span.querySelector("a");
        if (!a) return;
        a.href = buildHref(span);
        span.dataset.processed = "true";
    });
}