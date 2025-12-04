document.addEventListener("DOMContentLoaded", () => {
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

    const treeData = [
      { type: "file", name: "README.md", icon: "📝", link: "/EmbeddedDocsTemplates/docs/html/md_README.html" },
      { type: "file", name: "ISSUE_TEMPLATE.md", icon: "📝", link: "/EmbeddedDocsTemplates/docs/html/md_ISSUE_TEMPLATE.html" },
      { type: "folder", name: "Version", icon: "📁", children: [
          { type: "file", name: "BUG.md", icon: "🐞", link: "/EmbeddedDocsTemplates/docs/html/md_Version_BUG.html" },
          { type: "file", name: "CHANGELOG.md", icon: "📋", link: "/EmbeddedDocsTemplates/docs/html/md_Version_CHANGELOG.html" },
          { type: "file", name: "VERSION.md", icon: "🏷️", link: "/EmbeddedDocsTemplates/docs/html/md_Version_VERSION.html" },
          { type: "file", name: "API.md", icon: "🧩", link: "/EmbeddedDocsTemplates/docs/html/md_Version_API.html" },
          { type: "file", name: "NAMESPACE.md", icon: "📦", link: "/EmbeddedDocsTemplates/docs/html/md_Version_NAMESPACE.html" },
          { type: "file", name: "RELEASE_POLICY.md", icon: "📜", link: "/EmbeddedDocsTemplates/docs/html/md_Version_RELEASE_POLICY.html" },
          { type: "file", name: "FEATURE.md", icon: "⭐", link: "/EmbeddedDocsTemplates/docs/html/md_Version_FEATURE.html" },
          { type: "file", name: "FIX.md", icon: "🔧", link: "/EmbeddedDocsTemplates/docs/html/md_Version_FIX.html" }
      ]},
      { type: "folder", name: "Usage", icon: "📁", children: [
          { type: "file", name: "ADMINISTRATOR_GUIDE.md", icon: "🧑‍💼", link: "/EmbeddedDocsTemplates/docs/html/md_Usage_ADMINISTRATOR_GUIDE.html" },
          { type: "file", name: "ROLES.md", icon: "👥", link: "/EmbeddedDocsTemplates/docs/html/md_Usage_ROLES.html" },
          { type: "file", name: "DEVELOPMENT_GUIDE.md", icon: "🧑‍💻", link: "/EmbeddedDocsTemplates/docs/html/md_Usage_DEVELOPMENT_GUIDE.html" },
          { type: "file", name: "ACTORS.md", icon: "👤", link: "/EmbeddedDocsTemplates/docs/html/md_Usage_ACTORS.html" },
          { type: "file", name: "USECASES.md", icon: "🎮", link: "/EmbeddedDocsTemplates/docs/html/md_Usage_USECASES.html" },
          { type: "file", name: "USER_GUIDE.md", icon: "📘", link: "/EmbeddedDocsTemplates/docs/html/md_Usage_USER_GUIDE.html" }
      ]},
      { type: "file", name: "PROJECT.md", icon: "📄", link: "/EmbeddedDocsTemplates/docs/html/md_PROJECT.html" },
      { type: "file", name: "CONTACT_US.md", icon: "☎️", link: "/EmbeddedDocsTemplates/docs/html/md_CONTACT_US.html" },
      { type: "file", name: "template.css", icon: "🎨", link: "/EmbeddedDocsTemplates/docs/html/template.css" },
      { type: "file", name: "LICENSE.md", icon: "📜", link: "/EmbeddedDocsTemplates/docs/html/md_LICENSE.html" },
      { type: "file", name: "CODE_OF_CONDUCT.md", icon: "📝", link: "/EmbeddedDocsTemplates/docs/html/md_CODE_OF_CONDUCT.html" },
      { type: "file", name: "Makefile", icon: "📄", link: "/EmbeddedDocsTemplates/Makefile" },
      { type: "file", name: "Doxyfile", icon: "⚙️", link: "/EmbeddedDocsTemplates/Doxyfile" },
      { type: "file", name: "DoxygenLayout.xml", icon: "⚙️", link: "/EmbeddedDocsTemplates/DoxygenLayout.xml" },
      { type: "file", name: "doxygen.sh", icon: "🐚", link: "/EmbeddedDocsTemplates/doxygen.sh" },
      { type: "file", name: "doxygen.ini", icon: "🐚", link: "/EmbeddedDocsTemplates/doxygen.ini" },
      { type: "file", name: "link.js", icon: "🐚", link: "/EmbeddedDocsTemplates/link.js" },
      { type: "file", name: "directory-tree.js", icon: "🐚", link: "/EmbeddedDocsTemplates/directory-tree.js" },
      { type: "file", name: "header.html", icon: "🐚", link: "/EmbeddedDocsTemplates/header.html" },
      { type: "file", name: "footer.html", icon: "🐚", link: "/EmbeddedDocsTemplates/footer.html" },
      { type: "file", name: "index.html", icon: "🐚", link: "/EmbeddedDocsTemplates/index.html" },
      { type: "folder", name: "src", icon: "📁", children: [] }
    ];

    function createTree(data) {
        const ul = document.createElement("ul");
        data.forEach(item => {
            const li = document.createElement("li");
            li.className = item.type;
            li.textContent = `${item.icon} ${item.name}`;

            if(item.link) {
                const a = document.createElement("a");
                a.href = item.link;
                a.textContent = item.name;
                li.textContent = item.icon + " ";

                // Se preview=true, mostra modal invece di scaricare
                if(item.preview) {
                    a.addEventListener("click", e => {
                        e.preventDefault();
                        showPreview(item.name, item.link);
                    });
                } else {
                    li.appendChild(a);
                }

                li.appendChild(a);
            }

            if(item.type === "folder" && item.children) {
                li.appendChild(createTree(item.children));
            }
            ul.appendChild(li);
        });
        return ul;
    }

    container.appendChild(createTree(treeData));
}
