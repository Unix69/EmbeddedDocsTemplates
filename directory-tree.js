document.addEventListener("DOMContentLoaded", () => {
    initDirectoryTree("directory-tree-container");
});

// ============================
//   PREVIEW MODAL
// ============================
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
          modal.style.background = "rgba(0,0,0,0.75)";
          modal.style.display = "flex";
          modal.style.alignItems = "center";
          modal.style.justifyContent = "center";
          modal.style.zIndex = "99999";

          const box = document.createElement("pre");
          box.style.background = "#fff";
          box.style.color = "#000";
          box.style.padding = "20px";
          box.style.maxWidth = "90%";
          box.style.maxHeight = "85%";
          box.style.overflow = "auto";
          box.style.borderRadius = "8px";
          box.textContent = content;

          modal.appendChild(box);

          modal.addEventListener("click", () => modal.remove());
          box.addEventListener("click", (e) => e.stopPropagation());

          document.body.appendChild(modal);
      })
      .catch(() => alert("Errore durante il caricamento di: " + filename));
}

// ============================
//   DIRECTORY TREE
// ============================
function initDirectoryTree(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    // 🔥 Cancella tutto il contenuto statico
    container.innerHTML = "";

    // Determina basePath
    let basePath = "";
    if (window.location.pathname.includes("/docs/html/")) {
        basePath = "../../";
    }

    const treeData = [
      { type: "file", name: "README.md", icon: "📝", link: basePath + "docs/html/md_README.html" },
      { type: "file", name: "ISSUE_TEMPLATE.md", icon: "📝", link: basePath + "docs/html/md_ISSUE_TEMPLATE.html" },

      {
        type: "folder", name: "Version", icon: "📁", children: [
          { type: "file", name: "BUG.md", icon: "🐞", link: basePath + "docs/html/md_Version_BUG.html" },
          { type: "file", name: "CHANGELOG.md", icon: "📋", link: basePath + "docs/html/md_Version_CHANGELOG.html" },
          { type: "file", name: "VERSION.md", icon: "🏷️", link: basePath + "docs/html/md_Version_VERSION.html" },
          { type: "file", name: "API.md", icon: "🧩", link: basePath + "docs/html/md_Version_API.html" },
          { type: "file", name: "NAMESPACE.md", icon: "📦", link: basePath + "docs/html/md_Version_NAMESPACE.html" },
          { type: "file", name: "RELEASE_POLICY.md", icon: "📜", link: basePath + "docs/html/md_Version_RELEASE_POLICY.html" },
          { type: "file", name: "FEATURE.md", icon: "⭐", link: basePath + "docs/html/md_Version_FEATURE.html" },
          { type: "file", name: "FIX.md", icon: "🔧", link: basePath + "docs/html/md_Version_FIX.html" }
        ]
      },

      {
        type: "folder", name: "Usage", icon: "📁", children: [
          { type: "file", name: "ADMINISTRATOR_GUIDE.md", icon: "🧑‍💼", link: basePath + "docs/html/md_Usage_ADMINISTRATOR_GUIDE.html" },
          { type: "file", name: "ROLES.md", icon: "👥", link: basePath + "docs/html/md_Usage_ROLES.html" },
          { type: "file", name: "DEVELOPMENT_GUIDE.md", icon: "🧑‍💻", link: basePath + "docs/html/md_Usage_DEVELOPMENT_GUIDE.html" },
          { type: "file", name: "ACTORS.md", icon: "👤", link: basePath + "docs/html/md_Usage_ACTORS.html" },
          { type: "file", name: "USECASES.md", icon: "🎮", link: basePath + "docs/html/md_Usage_USECASES.html" },
          { type: "file", name: "USER_GUIDE.md", icon: "📘", link: basePath + "docs/html/md_Usage_USER_GUIDE.html" }
        ]
      },

      { type: "file", name: "PROJECT.md", icon: "📄", link: basePath + "docs/html/md_PROJECT.html" },
      { type: "file", name: "CONTACT_US.md", icon: "☎️", link: basePath + "docs/html/md_CONTACT_US.html" },
      { type: "file", name: "template.css", icon: "🎨", link: basePath + "docs/html/template.css" },
      { type: "file", name: "LICENSE.md", icon: "📜", link: basePath + "docs/html/md_LICENSE.html" },
      { type: "file", name: "CODE_OF_CONDUCT.md", icon: "📝", link: basePath + "docs/html/md_CODE_OF_CONDUCT.html" },

      // Preview files
      { type: "file", name: "Makefile", icon: "📄", link: basePath + "Makefile", preview: true },
      { type: "file", name: "Doxyfile", icon: "⚙️", link: basePath + "Doxyfile", preview: true },
      { type: "file", name: "doxygen.sh", icon: "🐚", link: basePath + "doxygen.sh", preview: true },
      { type: "file", name: "header.html", icon: "📄", link: basePath + "header.html", preview: true },
      { type: "file", name: "footer.html", icon: "📄", link: basePath + "footer.html", preview: true },
      { type: "file", name: "index.html", icon: "📄", link: basePath + "index.html", preview: true },

      { type: "file", name: "DoxygenLayout.xml", icon: "⚙️", link: basePath + "DoxygenLayout.xml" },
      { type: "file", name: "doxygen.ini", icon: "🐚", link: basePath + "doxygen.ini" },
      { type: "file", name: "link.js", icon: "📄", link: basePath + "link.js" },
      { type: "file", name: "directory-tree.js", icon: "📄", link: basePath + "directory-tree.js" },

      { type: "folder", name: "src", icon: "📁", children: [] }
    ];

    // ----------------------------
    //  BUILDER
    // ----------------------------
    function createTree(data) {
        const ul = document.createElement("ul");

        data.forEach(item => {
            const li = document.createElement("li");
            li.classList.add(item.type);

            // Icon + Label
            const label = document.createElement("span");
            label.textContent = `${item.icon} ${item.name}`;
            label.style.cursor = "pointer";

            if (item.type === "file") {
                const a = document.createElement("a");
                a.textContent = item.name;
                a.style.marginLeft = "4px";

                if (item.preview) {
                    a.href = "#";
                    a.addEventListener("click", e => {
                        e.preventDefault();
                        showPreview(item.name, item.link);
                    });
                } else {
                    a.href = item.link;
                }

                li.appendChild(document.createTextNode(item.icon + " "));
                li.appendChild(a);
            }

            if (item.type === "folder") {
                const details = document.createElement("details");
                const summary = document.createElement("summary");
                summary.textContent = `${item.icon} ${item.name}`;
                details.appendChild(summary);

                if (item.children?.length) {
                    details.appendChild(createTree(item.children));
                }
                li.appendChild(details);
            }

            ul.appendChild(li);
        });

        return ul;
    }

    // Inietta l'albero
    container.appendChild(createTree(treeData));
}