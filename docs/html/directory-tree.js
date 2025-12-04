document.addEventListener("DOMContentLoaded", () => {
    // Inizializza il tree
    initDirectoryTree("directory-tree-container");

    // Espandere/collassare cartelle
    document.querySelectorAll(".directory-tree .folder").forEach(folder => {
        folder.addEventListener("click", e => {
            e.stopPropagation();
            folder.classList.toggle("expanded");
        }); 
    });
});

// Funzione per mostrare preview in un modal
function showPreview(filename, url) {
    fetch(url)
      .then(res => res.text())
      .then(content => {
          const modal = document.createElement("div");
          modal.style.position = "fixed";
          modal.style.top = "0";
          modal.style.left = "0";
          modal.style.width = "100%";
          modal.style.height = "100%";
          modal.style.backgroundColor = "rgba(0,0,0,0.7)";
          modal.style.display = "flex";
          modal.style.alignItems = "center";
          modal.style.justifyContent = "center";
          modal.style.zIndex = "10000";

          const box = document.createElement("pre");
          box.style.background = "#fff";
          box.style.color = "#000";
          box.style.padding = "20px";
          box.style.maxWidth = "90%";
          box.style.maxHeight = "90%";
          box.style.overflow = "auto";
          box.textContent = content;

          // Chiudi cliccando fuori
          modal.addEventListener("click", () => modal.remove());
          box.addEventListener("click", e => e.stopPropagation());

          modal.appendChild(box);
          document.body.appendChild(modal);
      })
      .catch(err => alert("Impossibile caricare il file: " + filename));
}

function initDirectoryTree(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Base URL dinamico per GitHub Pages
    const baseUrl = window.location.origin + "/EmbeddedDocsTemplates/";

    const treeData = [
        { type: "file", name: "README.md", icon: "📝", link: baseUrl + "docs/html/md_README.html" },
        { type: "file", name: "ISSUE_TEMPLATE.md", icon: "📝", link: baseUrl + "docs/html/md_ISSUE_TEMPLATE.html" },
        { type: "folder", name: "Version", icon: "📁", children: [
            { type: "file", name: "BUG.md", icon: "🐞", link: baseUrl + "docs/html/md_Version_BUG.html" },
            { type: "file", name: "CHANGELOG.md", icon: "📋", link: baseUrl + "docs/html/md_Version_CHANGELOG.html" },
            { type: "file", name: "VERSION.md", icon: "🏷️", link: baseUrl + "docs/html/md_Version_VERSION.html" },
            { type: "file", name: "API.md", icon: "🧩", link: baseUrl + "docs/html/md_Version_API.html" },
            { type: "file", name: "NAMESPACE.md", icon: "📦", link: baseUrl + "docs/html/md_Version_NAMESPACE.html" },
            { type: "file", name: "RELEASE_POLICY.md", icon: "📜", link: baseUrl + "docs/html/md_Version_RELEASE_POLICY.html" },
            { type: "file", name: "FEATURE.md", icon: "⭐", link: baseUrl + "docs/html/md_Version_FEATURE.html" },
            { type: "file", name: "FIX.md", icon: "🔧", link: baseUrl + "docs/html/md_Version_FIX.html" }
        ]},
        { type: "folder", name: "Usage", icon: "📁", children: [
            { type: "file", name: "ADMINISTRATOR_GUIDE.md", icon: "🧑‍💼", link: baseUrl + "docs/html/md_Usage_ADMINISTRATOR_GUIDE.html" },
            { type: "file", name: "ROLES.md", icon: "👥", link: baseUrl + "docs/html/md_Usage_ROLES.html" },
            { type: "file", name: "DEVELOPMENT_GUIDE.md", icon: "🧑‍💻", link: baseUrl + "docs/html/md_Usage_DEVELOPMENT_GUIDE.html" },
            { type: "file", name: "ACTORS.md", icon: "👤", link: baseUrl + "docs/html/md_Usage_ACTORS.html" },
            { type: "file", name: "USECASES.md", icon: "🎮", link: baseUrl + "docs/html/md_Usage_USECASES.html" },
            { type: "file", name: "USER_GUIDE.md", icon: "📘", link: baseUrl + "docs/html/md_Usage_USER_GUIDE.html" }
        ]},
        { type: "file", name: "PROJECT.md", icon: "📄", link: baseUrl + "docs/html/md_PROJECT.html" },
        { type: "file", name: "CONTACT_US.md", icon: "☎️", link: baseUrl + "docs/html/md_CONTACT_US.html" },
        { type: "file", name: "template.css", icon: "🎨", link: baseUrl + "docs/html/template.css" },
        { type: "file", name: "LICENSE.md", icon: "📜", link: baseUrl + "docs/html/md_LICENSE.html" },
        { type: "file", name: "CODE_OF_CONDUCT.md", icon: "📝", link: baseUrl + "docs/html/md_CODE_OF_CONDUCT.html" },
        // File da visualizzare in preview
        { type: "file", name: "Makefile", icon: "📄", link: baseUrl + "Makefile", preview: true },
        { type: "file", name: "Doxyfile", icon: "⚙️", link: baseUrl + "Doxyfile", preview: true },
        { type: "file", name: "doxygen.sh", icon: "🐚", link: baseUrl + "doxygen.sh", preview: true },
        // Altri file normali
        { type: "file", name: "DoxygenLayout.xml", icon: "⚙️", link: baseUrl + "DoxygenLayout.xml" },
        { type: "file", name: "doxygen.ini", icon: "🐚", link: baseUrl + "doxygen.ini" },
        { type: "file", name: "link.js", icon: "🐚", link: baseUrl + "link.js" },
        { type: "file", name: "directory-tree.js", icon: "🐚", link: baseUrl + "directory-tree.js" },
        { type: "file", name: "header.html", icon: "🐚", link: baseUrl + "header.html" },
        { type: "file", name: "footer.html", icon: "🐚", link: baseUrl + "footer.html" },
        { type: "file", name: "index.html", icon: "🐚", link: baseUrl + "index.html" },
        { type: "folder", name: "src", icon: "📁", children: [] }
    ];

    function createTree(data) {
        const ul = document.createElement("ul");
        data.forEach(item => {
            const li = document.createElement("li");
            li.className = item.type;
            const textNode = document.createTextNode(item.icon + " ");
            li.appendChild(textNode);

            if(item.type === "file") {
                const a = document.createElement("a");
                a.textContent = item.name;
                a.href = "#";
                a.style.cursor = "pointer";

                if(item.preview) {
                    a.addEventListener("click", e => {
                        e.preventDefault();
                        showPreview(item.name, item.link);
                    });
                } else if(item.link) {
                    a.href = item.link;
                }

                li.appendChild(a);
            } else if(item.type === "folder") {
                li.appendChild(document.createTextNode(item.name));
                if(item.children) li.appendChild(createTree(item.children));
            }

            ul.appendChild(li);
        });
        return ul;
    }

    container.appendChild(createTree(treeData));
}