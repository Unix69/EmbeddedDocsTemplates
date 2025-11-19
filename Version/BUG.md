<h1>
  🐞 Bugs
</h1>


<!-- Badges -->
<p>
  <a href=""><img src="https://img.shields.io/github/last-commit/Unix69/EmbeddedDocsTemplates" alt="last update" /></a>
  <a href="https://github.com/Unix69/EmbeddedDocsTemplates/issues/"><img src="https://img.shields.io/github/issues/Unix69/EmbeddedDocsTemplates" alt="open issues" /></a>
</p>

<br>

A ***Bug*** in **[PROJECT_NAME]** is a design or implementation defect occurring in one or more of its  
***[Versions](md_Version_VERSION.html)***, ***[Features](md_Version_FEATURE.html)***,  
***[Namespaces](md_Version_NAMESPACE.html)***, or ***[APIs](md_Version_API.html)***.  

Such a defect exposes the system to specific ***vulnerabilities***, which may be exploited by ***threats*** through targeted ***attacks***, potentially causing significant ***impact*** on system behavior or integrity.  

Each ***Bug*** must be addressed by an appropriate ***[Fix](md_Version_FIX.html)***, which patches the vulnerability and updates the corresponding software version following the defined  
***[Release Policy](md_Version_RELEASE_POLICY.html)***.  

After a **Fix** is applied, the affected version of the [PROJECT_NAME] release is incremented accordingly.  

All discovered bugs are **registered** in the **Bug Tracer** and **fully documented** below.

<br><br>

<a name="table-of-contents"></a>

### 📓 Table of Contents

Navigation index:

- [Types](#types)
- [Priorities](#priorities)
- [Bug Tracer](#bug-tracer)
- [FAQ](#faq)
- [Contact Us](#contact-us)
- [See Also](#see-also)
- [Official Links](#official-links)

<br><br>

<a name="types"></a>

## 🐛 Types

| Type | Values | Description |
|------|--------|------------|
| ⚙️ **Bug Nature** | *Hardware* - **HW**, *Software* - **SW** | Defines the **origin** of the bug — hardware or software. |
| 🔥 **Bug Level** | *System* - **SYS**, *User* - **USR** | Indicates the **impact scope** — system-wide or user-level. |
| 🧩 **HW (Hardware)** | — | Bug originates from **physical components**, circuits, or firmware interactions. |
| 💻 **SW (Software)** | — | Bug originates from **code logic**, **API misuse**, or incorrect software behavior. |
| 🧠 **SYS (System)** | — | Affects **core services**, kernel modules, or global resources. |
| 👤 **USR (User)** | — | Affects **user interface**, session management, or per-user configurations. |

<br><br>

<a name="priorities"></a>

## 🚦 Priorities

| Priority | Code | Description |
|----------|------|------------|
| 🟢 **Low** | **LO** | Minor glitch, negligible effect; can be postponed. |
| 🔵 **Medium** | **M** | Noticeable issue affecting stability or usability; has workarounds. |
| 🟠 **High** | **HI** | Major issue reducing functionality or reliability; requires prompt fix. |
| 🔴 **Urgent** | **URG** | Critical problem causing crashes, security breaches, or service interruptions; fix immediately. |

<br><br>

<a name="bug-tracer"></a>

## 🧾 Bug Tracer

All **Bugs** in **[PROJECT_NAME]** are tracked here with full details:

| 🐛 Bug | 📝 Description | 🗓️ Discovered on | 🛡️ Vulnerabilities | ⚠️ Threats | 💥 Attacks | 💣 Impact | ⚙️ Nature | 🔥 Level | 🧩 Versions | ⚙️ Features | 📦 Namespaces | 🔗 APIs | ⏫ Priority |
|--------|----------------|-----------------|-------------------|------------|------------|-----------|-----------|-----------|-------------|-------------|---------------|--------|------------|
| `1` | The **username string** is not verified, so **login** is **denied** to all users | 14/05/2025 | Bad username verification | - | DoS, DDoS | Availability and Usability | **SW** | **SYS** | <ul><li>`v1.1.0`</li><li>`v1.2.0`</li></ul> | <ul><li>`data core features`</li></ul> | <ul><li>`core`</li></ul> | <ul><li>`core.data`</li></ul> | **URG** |

<br>

<a name="see-also"></a>

# See Also

The following documents are related to this:

<ul>
  <li> 
    * <span class="md-link" data-github="PROJECT.md" data-doxygen="md_PROJECT.html"><b>Project</b></span> file, named <code>PROJECT.md</code>, contains the ***Project Description*** of **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Usage/USECASES.md" data-doxygen="md_Usage_USECASES.html"><b>Use Cases</b></span> file, named <code>USECASES.md</code>, shows the ***Use Cases*** of **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Usage/ACTORS.md" data-doxygen="md_Usage_ACTORS.html"><b>Actors</b></span> file, named <code>ACTORS.md</code>, explains the types of ***Actors*** in **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Usage/ROLES.md" data-doxygen="md_Usage_ROLES.html"><b>Roles</b></span> file, named <code>ROLES.md</code>, describes the ***Roles*** of the ***Actors*** in **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Usage/ADMINISTRATOR_GUIDE.md" data-doxygen="md_Usage_ADMINISTRATOR_GUIDE.html"><b>Administrator Guide</b></span> file, named <code>ADMINISTRATOR_GUIDE.md</code>, explains to ***Administrators*** how to manage **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Usage/USER_GUIDE.md" data-doxygen="md_Usage_USER_GUIDE.html"><b>User Guide</b></span> file, named <code>USER_GUIDE.md</code>, explains to ***Users*** how to use **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Usage/DEVELOPMENT_GUIDE.md" data-doxygen="md_Usage_DEVELOPMENT_GUIDE.html"><b>Developer Guide</b></span> file, named <code>DEVELOPMENT_GUIDE.md</code>, explains to ***Developers*** how to develop **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Version/VERSION.md" data-doxygen="md_Version_VERSION.html"><b>Versions</b></span> file, named <code>VERSION.md</code>, shows and explains each ***Version*** of **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Version/RELEASE_POLICY.md" data-doxygen="md_Version_RELEASE_POLICY.html"><b>Release Policy</b></span> file, named <code>RELEASE_POLICY.md</code>, contains the ***Release Policy*** standard adopted in **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Version/FEATURE.md" data-doxygen="md_Version_FEATURE.html"><b>Features</b></span> file, named <code>FEATURE.md</code>, contains the ***Features*** of **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Version/API.md" data-doxygen="md_Version_API.html"><b>APIs</b></span> file, named <code>API.md</code>, contains the ***APIs*** of **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Version/CHANGELOG.md" data-doxygen="md_Version_CHANGELOG.html"><b>Change Log</b></span> file, named <code>CHANGELOG.md</code>, contains the ***Changes*** made in **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Version/NAMESPACE.md" data-doxygen="md_Version_NAMESPACE.html"><b>Namespaces</b></span> file, named <code>NAMESPACE.md</code>, contains the ***Namespace*** architecture of **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Version/BUG.md" data-doxygen="md_Version_BUG.html"><b>Bugs</b></span> file, named <code>BUG.md</code>, contains the ***Bugs*** identified in **README Template**.
  </li>
  <li>
    * <span class="md-link" data-github="Version/FIX.md" data-doxygen="md_Version_FIX.html"><b>Fixes</b></span> file, named <code>FIX.md</code>, contains the ***Fixes*** applied to **README Template**.
  </li>
</ul>
<br>

<br>

<a name="faq"></a>

# FAQ ❓

Frequently Asked Questions and Answers.

<br><br>

<a name="contact-us"></a>

# Contact us ☎️

For more information on [PROJECT_NAME]  
[**contact us**](md_CONTACT_US.html).

<br><br>

<a name="official-links"></a>

# Official Links

* [SemVer](https://www.semver.org) – Guide to **Semantic Versioning**  
* [Doxygen](https://www.doxygen.nl/index.html) – **Documentation generator**  
* [GitHub](https://github.com) – **Code hosting & collaboration**  
* [Git](https://git-scm.com) – **Version control** system  
* [GNU Make](https://www.gnu.org/software/make/) – **Build automation** tool
<br><br>
