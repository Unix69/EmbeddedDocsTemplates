<div align="center" style="margin-left: 24px;">
  
<table style="width:320px">
	<tr>
		<td style="text-align:left">
			<img src="Images/Logo/GnuLinuxLogo.svg" alt="GNU/Linux" width="160" height="160">
		</td>
		<td style="text-align:right">
			<img src="Images/Logo/doxygen.svg" alt="Doxygen" width="160" height="160"> 
		</td> 
	</tr> 
</table>

  <h1>README Template</h1>
  
  <br>  

<!-- Badges -->
<p>
  <a href="https://github.com/Unix69/EmbeddedDocsTemplates/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Unix69/EmbeddedDocsTemplates" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/Unix69/EmbeddedDocsTemplates" alt="last update" />
  </a>
  <a href="https://github.com/Unix69/EmbeddedDocsTemplates/network/members">
    <img src="https://img.shields.io/github/forks/Unix69/EmbeddedDocsTemplates" alt="forks" />
  </a>
  <a href="https://github.com/Unix69/EmbeddedDocsTemplates/stargazers">
    <img src="https://img.shields.io/github/stars/Unix69/EmbeddedDocsTemplates" alt="stars"/>
  </a>
  <a href="https://github.com/Unix69/EmbeddedDocsTemplates/issues/">
    <img src="https://img.shields.io/github/issues/Unix69/EmbeddedDocsTemplates" alt="open issues" />
  </a>
  <a href="https://github.com/Unix69/EmbeddedDocsTemplates/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/Unix69/EmbeddedDocsTemplates.svg" alt="license" />
  </a>
</p>

<br>

  
🏗️ <span class="md-link"
         data-github="PROJECT.md"
         data-doxygen="md_PROJECT.html">
  <a href="PROJECT.md">Project</a>
</span>
 ·
⭐ <span class="md-link"
         data-github="Version/FEATURE.md"
         data-doxygen="md_Version_FEATURE.html">
  <a href="Version/FEATURE.md">Features</a>
</span>
 ·
🎮 <span class="md-link"
         data-github="Usage/USECASES.md"
         data-doxygen="md_Usage_USECASES.html">
  <a href="Usage/USECASES.md">Use Cases</a>
</span>
 ·
🏷️ <span class="md-link"
         data-github="Version/VERSION.md"
         data-doxygen="md_Version_VERSION.html">
  <a href="Version/VERSION.md">Versions</a>
</span>
 ·
📜 <span class="md-link"
         data-github="Version/RELEASE_POLICY.md"
         data-doxygen="md_Version_RELEASE_POLICY.html">
  <a href="Version/RELEASE_POLICY.md">Release Policy</a>
</span>
 ·
📦 <span class="md-link"
         data-github="Version/NAMESPACE.md"
         data-doxygen="md_Version_NAMESPACE.html">
  <a href="Version/NAMESPACE.md">Namespaces</a>
</span>
 ·
🧩 <span class="md-link"
         data-github="Version/API.md"
         data-doxygen="md_Version_API.html">
  <a href="Version/API.md">APIs</a>
</span>
 ·
🐞 <span class="md-link"
         data-github="Version/BUG.md"
         data-doxygen="md_Version_BUG.html">
  <a href="Version/BUG.md">Bugs</a>
</span>
 ·
🔧 <span class="md-link"
         data-github="Version/FIX.md"
         data-doxygen="md_Version_FIX.html">
  <a href="Version/FIX.md">Fixes</a>
</span>
 ·
📋 <span class="md-link"
         data-github="Version/CHANGELOG.md"
         data-doxygen="md_Version_CHANGELOG.html">
  <a href="Version/CHANGELOG.md">Change Log</a>
</span>
 ·
☎️ <span class="md-link"
         data-github="CONTACT_US.md"
         data-doxygen="md_CONTACT_US.html">
  <a href="CONTACT_US.md">Contact Us</a>
</span>

<br>
<br>


<div align="left" style="margin-left: 24px;">

<br>
<br>

<!-- Table of Contents -->

<a name="table-of-contents"></a>

### 📓 Table of Contents

Navigation index to fast explore the content:

- [About the Project](#about-the-project)
- [Goal](#goal)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Directory Tree](#directory-tree)
- [See Also](#see-also)
- [Contact Us](#contact-us)


<br>
<br>

<!-- Project -->
# About the Project

This awesome **README Template**, offer a **standard way to documenting and mantaining Software** in a **reliable** way and **ready** to deploy, through **GitHub MarkDown Language** and **GitHub Actions**. The template automatically trace and analyse the Software **source code** at each change by binding **embedded code descriptions** and **hints** within the code, and dedicated sections into the **README** architecture such as **Version**, **API**, **Bug**, **Fix**, **Namespace**, **Feature**, **Change**.


<br>
<br>

<a name="goal"></a>

<!-- Goal -->
## 🏁 Goal

Provide a **ready to use** template to optimize the documentation development process.

<br>
<br>

<a name="architecture"></a>

<!-- Architecture -->
# 🚀 Architecture

The architecture of the README Template is organized into **two main layers**: a **Markdown-based documentation** set and a customized **HTML site** generated via Doxygen. Both layers are fully editable, allowing complete customization for each project’s needs.  

To streamline and automate the documentation workflow, the template includes a **Makefile** integrated with the Make build tool. This Makefile provides predefined commands to **build, generate, and clean** the documentation, ensuring a consistent and repeatable process.  

By design, the Makefile can be **seamlessly integrated into the project’s existing build toolchain**, enabling the simultaneous production of software and its corresponding documentation. This approach ensures that documentation remains up-to-date, synchronized with code changes, and ready for deployment alongside the product.

<br>
<br>

## Markdown-based documentation

The Markdown-based documentation consists of a set of `.md` files, **rooted at `./README.md`**, which serve as the canonical source for project information. These files provide a comprehensive description of the project, including its structure, capabilities, versioning, usage, contribution workflow, and license.

The template organizes documentation according to the software lifecycle, divided into thematic sections:

- **Capabilities & Features**  
  Each project can list its main capabilities and features, making it clear what the software can do and which modules or components are available.

- **API & Namespaces**  
  API and namespace documentation provides a complete view of the software's public interface and internal module structure, facilitating integration with other systems.

- **Versioning**  
  Includes information on versions, known bugs, fixes, changelogs, and release policies, allowing clear tracking of the software's evolution.

- **Usage**  
  Contains use cases, actors, roles, and user or administrator guides, documenting how the software is used in different operational scenarios.

- **GitHub CI/CD**  
  Specifies contribution procedures, forks, pull requests, and issue management, making documentation an integral part of the collaborative development workflow.

- **License**  
  Manages legal information regarding software usage and distribution.

<br>

#### Organization of Markdown Files

- **Project Overview**
  - `README.md` – entry point and high-level overview of the project.
  - `PROJECT.md` – detailed project description, goals, and scope.
  - `CONTACT_US.md` – project contact information.
  - `LICENSE.md` – licensing information.
  - `CODE_OF_CONDUCT.md` – project rules and contribution guidelines.

- **Capabilities & Features**
  - `API.md` – API specification and reference.
  - `FEATURE.md` – list and description of project features.
  - `NAMESPACE.md` – project namespace organization and mapping.

- **Versioning**
  - `VERSION.md` – current version of the project.
  - `BUG.md` – known issues and defects.
  - `FIX.md` – applied fixes and patches.
  - `CHANGELOG.md` – detailed change history.
  - `RELEASE_POLICY.md` – rules and strategies for software releases.

- **Usage**
  - `USECASES.md` – typical use cases of the software.
  - `ACTORS.md` – actors interacting with the system.
  - `ROLES.md` – user roles and permissions.
  - `ADMINISTRATOR_GUIDE.md` – administrator-focused documentation.
  - `USER_GUIDE.md` – end-user documentation.
  - `DEVELOPMENT_GUIDE.md` – guidelines for developers integrating with the system.

- **CI/CD and Contribution Workflow**
  - Documents describing how to contribute, fork, create pull requests, and report issues using GitHub workflows.

<br>

**Purpose and Advantages:**

- The Markdown documentation reflects **all phases of software production**, from initial design to release management.
- Each file focuses on a specific aspect of the project, making documentation **modular and easy to maintain**.
- Tracks project **capabilities, features, API endpoints, namespaces, bugs, fixes, changes, version history, release policies, and user/actor roles**.
- Ensures **traceability between development phases and documentation**, keeping project knowledge organized and up-to-date.
- Markdown serves as the **source of truth**, which is then integrated into the HTML documentation for interactive navigation.

<br>

### Folder Structure

- **Version/**  
  Contains Markdown files for managing bugs, fixes, changelogs, versions, release policies, API, namespaces, and features.  
  This allows each production phase to be documented modularly.

- **Usage/**  
  Contains guides and descriptions related to users, roles, actors, and use cases.  
  Helps define processes and software usage flows.

<br>

### How It Works for Each Project

Each project can use Markdown files to:

1. Document **features**, **API**, **namespaces**, **versions**, **bugs**, **fixes**, **changes**, and **release policies**.
2. Easily update documentation without modifying the HTML site or source code: Markdown files are independent and directly editable.
3. Automatically generate HTML pages via Doxygen, integrating Markdown content with source code documentation (classes, packages, files).

<br>

### Advantages

- **Complete Traceability:** Every change in the code or functionality can be documented and linked to the corresponding version.
- **Automation:** Thanks to the Make + Doxygen toolchain, the HTML documentation is automatically updated with Markdown content and inline code comments.
- **Integration:** Doxygen tags (`@fix`, `@bug`, `@change`, `@todo`, `@api`, `@namespace`, `@feature`) allow linking development notes directly to source code.
- **Modular Clarity:** Folder structure (Version, Usage) separates concepts and production phases, making documentation readable and navigable.
- **Collaboration-Friendly:** Multiple team members can edit Markdown files, while Doxygen generates a unified, always up-to-date HTML site.


<br>
<br>

## HTML-based site

The HTML-based site consists of `.html`, `.js`, and `.css` files, **rooted at the base directory `./`**, that customize and extend the default Doxygen output. This layer transforms the Markdown documentation and source code comments into a fully navigable and interactive website.

The Doxygen part generates a **fully navigable HTML site** with integrated Markdown documentation:

- Markdown files are converted into HTML pages within the site.
- Source code documentation is included, showing classes, packages, file hierarchies, and diagrams.
- Custom headers, footers, CSS, and JS allow a tailored visual style and interactive navigation.
- The template supports **custom Doxygen tags** (`@fix`, `@bug`, `@change`, `@todo`, `@api`, `@namespace`, `@feature`) for embedding comments directly in the code, keeping documentation always linked to the implementation.

<br>

#### Key Components

- `index.html` – the root page of the site.
- `header.html` / `footer.html` – custom header and footer sections applied site-wide.
- `stylesheet.css` / `template.css` – style sheets controlling fonts, colors, logos, layout, and overall site design.
- `link.js` – dynamically rewrites links to GitHub, GitHub Pages, and Markdown-based pages.
- `directory-tree.js` – generates expandable/collapsible directory trees for easy navigation through files and folders.

<br>

#### Functionality and Structure

- The HTML site **mirrors the Markdown organization**, converting each `.md` file into an `.html` page.
- Integrates **source code documentation**, showing classes, methods, packages, files, and relationships.
- Provides interactive features such as **search, expandable trees, and clickable references**.
- Copies all required resources (images, JS, CSS) into `docs/html` to ensure URLs in both Markdown and HTML pages resolve correctly.
- Allows full **customization of layout, style, and navigation** without modifying the Markdown source files.
- Ensures **dynamic linking between code, Markdown documentation, and GitHub**, maintaining an always up-to-date connection between code and documentation.

<br>

### How Doxygen Works in This Template

1. **Configuration File (`doxygen.ini`)**  
   Contains project-specific parameters that are read by the script `doxygen.sh`. These parameters are used to configure Doxygen dynamically.

2. **Script (`doxygen.sh`)**  
   Reads `doxygen.ini` and generates a `Doxyfile` by adding or modifying the necessary parameters.  
   This ensures that the HTML documentation will reflect the current project setup, Markdown files, and source code structure.

3. **Generating Documentation**  
   - `make build`: prepares any required intermediate files or configuration.
   - `make doc`: runs Doxygen with the generated `Doxyfile` (`doxygen Doxyfile`) and produces the full HTML documentation.
   - During this process, the Make command also **copies resources** such as images into `docs/html` so that all links in Markdown and HTML pages remain valid and functional.

<br>

### Advantages of the Doxygen Site

- **Unified View:** Combines Markdown documentation with code-level information.
- **Interactive Navigation:** Tree views, search, and hyperlinks make exploring the documentation easy.
- **Automatic Updates:** Changes in Markdown or source code automatically update the HTML site.
- **Resource Management:** Images and other assets are copied automatically to the output folder, ensuring all URLs remain valid.
- **Integration with Production:** The Make toolchain allows seamless integration with the software build process, making documentation generation part of the continuous development workflow.

<br>
<br>

### 3️⃣ Source Code Integration

- All project source code is placed under `./src`.
- Doxygen parses the source files and extracts comments and structure.
- Custom aliases such as `@fix`, `@bug`, `@change`, `@todo`, `@api`, `@namespace`, and `@feature` are used in comments to automatically integrate code-related notes into the HTML documentation.
- This mechanism ensures a **live link between code and documentation**, keeping documentation synchronized with code changes.


---

Overall, this template provides a **fully automated documentation system** that maintains a clear connection between project planning, Markdown documentation, and source code, simplifying both development and maintenance while keeping documentation always up-to-date.




<br>
<br>

<a name="tech-stack"></a>

## 💻 Tech Stack

* **Languages**: *HTML*, *JavaScript*
* **Frameworks**: *DoxyGen*
* **Infrastructure**: *GitHub*, *GitHub Actions*

<br>
<br>

<a name="directory-tree"></a>

## 📁 Directory Tree

<br>

<div class="directory-tree">
    <ul>
      <li class="file" data-icon="📝"><span class="md-link" data-github="README.md" data-doxygen="md_README.html">README.md</span></li>
      <li class="file" data-icon="📝"><span class="md-link" data-github="ISSUE_TEMPLATE.md" data-doxygen="md_ISSUE_TEMPLATE.html">ISSUE_TEMPLATE.md</span></li>
      <li class="folder">📁 Version
        <ul>
          <li class="file" data-icon="🐞"><span class="md-link" data-github="BUG.md" data-doxygen="md_Version_BUG.html">BUG.md</span></li>
          <li class="file" data-icon="📋"><span class="md-link" data-github="CHANGELOG.md" data-doxygen="md_Version_CHANGELOG.html">CHANGELOG.md</span></li>
          <li class="file" data-icon="🏷️"><span class="md-link" data-github="VERSION.md" data-doxygen="md_Version_VERSION.html">VERSION.md</span></li>
          <li class="file" data-icon="🧩"><span class="md-link" data-github="API.md" data-doxygen="md_Version_API.html">API.md</span></li>
          <li class="file" data-icon="📦"><span class="md-link" data-github="NAMESPACE.md" data-doxygen="md_Version_NAMESPACE.html">NAMESPACE.md</span></li>
          <li class="file" data-icon="📜"><span class="md-link" data-github="RELEASE_POLICY.md" data-doxygen="md_Version_RELEASE_POLICY.html">RELEASE_POLICY.md</span></li>
          <li class="file" data-icon="⭐"><span class="md-link" data-github="FEATURE.md" data-doxygen="md_Version_FEATURE.html">FEATURE.md</span></li>
          <li class="file" data-icon="🔧"><span class="md-link" data-github="FIX.md" data-doxygen="md_Version_FIX.html">FIX.md</span></li>
        </ul>
      </li>
      <li class="folder">📁 Usage
        <ul>
          <li class="file" data-icon="🧑‍💼"><span class="md-link" data-github="ADMINISTRATOR_GUIDE.md" data-doxygen="md_Usage_ADMINISTRATOR_GUIDE.html">ADMINISTRATOR_GUIDE.md</span></li>
          <li class="file" data-icon="👥"><span class="md-link" data-github="ROLES.md" data-doxygen="md_Usage_ROLES.html">ROLES.md</span></li>
          <li class="file" data-icon="🧑‍💻"><span class="md-link" data-github="DEVELOPMENT_GUIDE.md" data-doxygen="md_Usage_DEVELOPMENT_GUIDE.html">DEVELOPMENT_GUIDE.md</span></li>
          <li class="file" data-icon="👤"><span class="md-link" data-github="ACTORS.md" data-doxygen="md_Usage_ACTORS.html">ACTORS.md</span></li>
          <li class="file" data-icon="🎮"><span class="md-link" data-github="USECASES.md" data-doxygen="md_Usage_USECASES.html">USECASES.md</span></li>
          <li class="file" data-icon="📘"><span class="md-link" data-github="USER_GUIDE.md" data-doxygen="md_Usage_USER_GUIDE.html">USER_GUIDE.md</span></li>
        </ul>
      </li>
      <li class="file" data-icon="📄"><span class="md-link" data-github="PROJECT.md" data-doxygen="md_PROJECT.html">PROJECT.md</span></li>
      <li class="file" data-icon="☎️"><span class="md-link" data-github="CONTACT_US.md" data-doxygen="md_CONTACT_US.html">CONTACT_US.md</span></li>
      <li class="file" data-icon="📄"><span class="md-link" data-github="LICENSE.md" data-doxygen="md_LICENSE.html">LICENSE.md</span></li>
      <li class="file" data-icon="📝"><span class="md-link" data-github="CODE_OF_CONDUCT.md" data-doxygen="md_CODE_OF_CONDUCT.html">CODE_OF_CONDUCT.md</span></li>
      <li class="file" data-icon="📄"><span class="md-link" data-github="../../Makefile" data-doxygen="../../Makefile">Makefile</span></li>
      <li class="file" data-icon="⚙️"><span class="md-link" data-github="../../Doxyfile" data-doxygen="../../Doxyfile">Doxyfile</span></li>
      <li class="file" data-icon="⚙️"><span class="md-link" data-github="../../DoxygenLayout.xml" data-doxygen="../../DoxygenLayout.xml">DoxygenLayout.xml</span></li>
      <li class="file" data-icon="🐚"><span class="md-link" data-github="../../doxygen.sh" data-doxygen="../../doxygen.sh">doxygen.sh</span></li>
      <li class="file" data-icon="📄"><span class="md-link" data-github="../../doxygen.ini" data-doxygen="../../doxygen.ini">doxygen.ini</span></li>
      <li class="file" data-icon="📄"><span class="md-link" data-github="../../index.html" data-doxygen="../../index.html">index.html</span></li>
      <li class="file" data-icon="📄"><span class="md-link" data-github="../../header.html" data-doxygen="../../header.html">header.html</span></li>
      <li class="file" data-icon="📄"><span class="md-link" data-github="../../footer.html" data-doxygen="../../footer.html">footer.html</span></li>
      <li class="file" data-icon="📄"><span class="md-link" data-github="../../stylesheet.css" data-doxygen="../../stylesheet.css">stylesheet.css</span></li>
      <li class="file" data-icon="📄"><span class="md-link" data-github="../../link.js" data-doxygen="../../link.js">link.js</span></li>
      <li class="file" data-icon="📄"><span class="md-link" data-github="../../directory-tree.js" data-doxygen="../../directory-tree.js">directory-tree.js</span></li>
      <li class="folder">📁 src</li>
    </ul>
</div>

<br>
<br>

<a name="see-also"></a>

# See Also

[Table of Contents](#table-of-contents)

<br>

<ul>
  <li>
    <span class="md-link" data-github="PROJECT.md" data-doxygen="md_PROJECT.html">
        <a href="PROJECT.md"><b>Project</b></a>
      </span> file, named <code>PROJECT.md</code>, contains the ***Project Description*** of **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Usage/USECASES.md" data-doxygen="md_Usage_USECASES.html">
        <a href="Usage/USECASES.md"><b>Use Cases</b></a>
      </span> file, named <code>USECASES.md</code>, shows the ***Use Cases*** of **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Usage/ACTORS.md" data-doxygen="md_Usage_ACTORS.html">
        <a href="Usage/ACTORS.md"><b>Actors</b></a>
      </span> file, named <code>ACTORS.md</code>, explains the types of ***Actors*** in **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Usage/ROLES.md" data-doxygen="md_Usage_ROLES.html">
        <a href="Usage/ROLES.md"><b>Roles</b></a>
      </span> file, named <code>ROLES.md</code>, describes the ***Roles*** of the ***Actors*** in **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Usage/ADMINISTRATOR_GUIDE.md" data-doxygen="md_Usage_ADMINISTRATOR_GUIDE.html">
        <a href="Usage/ADMINISTRATOR_GUIDE.md"><b>Administrator Guide</b></a>
      </span> file, named <code>ADMINISTRATOR_GUIDE.md</code>, explains to ***Administrators*** how to manage **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Usage/USER_GUIDE.md" data-doxygen="md_Usage_USER_GUIDE.html">
        <a href="Usage/USER_GUIDE.md"><b>User Guide</b></a>
      </span> file, named <code>USER_GUIDE.md</code>, explains to ***Users*** how to use **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Usage/DEVELOPMENT_GUIDE.md" data-doxygen="md_Usage_DEVELOPMENT_GUIDE.html">
        <a href="Usage/DEVELOPMENT_GUIDE.md"><b>Developer Guide</b></a>
      </span> file, named <code>DEVELOPMENT_GUIDE.md</code>, explains to ***Developers*** how to develop **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/VERSION.md" data-doxygen="md_Version_VERSION.html">
        <a href="Version/VERSION.md"><b>Versions</b></a>
      </span> file, named <code>VERSION.md</code>, shows and explains each ***Version*** of **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/RELEASE_POLICY.md" data-doxygen="md_Version_RELEASE_POLICY.html">
        <a href="Version/RELEASE_POLICY.md"><b>Release Policy</b></a>
      </span> file, named <code>RELEASE_POLICY.md</code>, contains the ***Release Policy*** standard adopted in **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/FEATURE.md" data-doxygen="md_Version_FEATURE.html">
        <a href="Version/FEATURE.md"><b>Features</b></a>
      </span> file, named <code>FEATURE.md</code>, contains the ***Features*** of **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/API.md" data-doxygen="md_Version_API.html">
        <a href="Version/API.md"><b>APIs</b></a>
      </span> file, named <code>API.md</code>, contains the ***APIs*** of **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/CHANGELOG.md" data-doxygen="md_Version_CHANGELOG.html">
        <a href="Version/CHANGELOG.md"><b>Change Log</b></a>
      </span> file, named <code>CHANGELOG.md</code>, contains the ***Changes*** made in **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/NAMESPACE.md" data-doxygen="md_Version_NAMESPACE.html">
        <a href="Version/NAMESPACE.md"><b>Namespaces</b></a>
      </span> file, named <code>NAMESPACE.md</code>, contains the ***Namespace*** architecture of **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/BUG.md" data-doxygen="md_Version_BUG.html">
        <a href="Version/BUG.md"><b>Bugs</b></a>
      </span> file, named <code>BUG.md</code>, contains the ***Bugs*** identified in **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/FIX.md" data-doxygen="md_Version_FIX.html">
        <a href="Version/FIX.md"><b>Fixes</b></a>
      </span> file, named <code>FIX.md</code>, contains the ***Fixes*** applied to **README Template**.
  </li>
</ul>


<br>  


<br>

<a name="faq"></a>


# FAQ ❓

Here you can find the Frequently Asked Questions and Answers.

<br>
<br>

<a name="contact-us"></a>


# Contact us ☎️



For **more information** on [PROJECT_NAME] [**contact us**](md_readme_CONTACT_US.html).

<br>

<a name="official-links"></a>

# Official Links

[Table of Contents](#table-of-contents)

* [SemVer](https://www.semver.org) – A complete guide to **Semanting Verioning**. 
* [Doxygen](https://www.doxygen.nl/index.html) – **Documentation generator** for source code.
* [GitHub](https://github.com) – **Hosting** and **collaboration platform** for **Git** repositories.
* [Git](https://git-scm.com) – **Version control** system to manage source code.
* [GNU Make](https://www.gnu.org/software/make/) – **Build automation tool** to compile projects.

<br>
<br>

</div>


