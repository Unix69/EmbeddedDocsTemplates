<h1>
  🛠️ Fixes
</h1>


<!-- Badges -->
<p>
  <a href=""><img src="https://img.shields.io/github/last-commit/Unix69/EmbeddedDocsTemplates" alt="last update" /></a>
  <a href="https://github.com/Unix69/EmbeddedDocsTemplates/issues/"><img src="https://img.shields.io/github/issues/Unix69/EmbeddedDocsTemplates" alt="open issues" /></a>
</p>

<br>

A ***Fix*** in **[PROJECT_NAME]** is a **solution or patch** applied to a **bugged release** in order to **resolve a Bug**, patch the related **vulnerability**, and **update the affected version** according to the ***[Release Policy](./RELEASE_POLICY.md)***.
**After a Fix**, the release version of the bugged [PROJECT_NAME] changes, and the system is secured against the **threats** previously exploiting the **vulnerabilities**.
Discovered Fixes are **registered** in the **Fix Tracker** and **documented** in detail.

<br>
<br>

<!-- Table of Contents -->

<a name="table-of-contents"></a>

### 📓 Table of Contents

Navigation index to fast explore the content:

- [Fix Nature](#fix-nature)
- [Fix Level](#fix-level)
- [Priorities](#priorities)
- [Fix Tracer](#fix-tracer)
- [FAQ](#faq)
- [Contact us](#contact-us)
- [See Also](#see-also)
- [Official Links](#official-links)

<br>
<br>

<a id="fix-nature"></a>

## ⚙️ Fix Nature

| Type               | Values                                                                                 | Description |
| ------------------ | -------------------------------------------------------------------------------------- | ------------ |
| 🛠️ **Fix Nature** | *Software patch* - **SW**, *Hardware patch* - **HW**, *Configuration update* - **CFG** | Defines the **type of fix** applied to resolve an issue. |
| 🧩 **SW (Software patch)** | — | Fixes involving **code changes**, refactoring, or logic correction within the software. |
| 🔩 **HW (Hardware patch)** | — | Fixes that require **hardware-level changes**, such as board redesign, component replacement, or firmware updates. |
| ⚙️ **CFG (Configuration update)** | — | Fixes applied through **system or environment configuration**, such as editing `.conf` files, tuning parameters, or changing build flags. |

<br>
<br>

<a id="fix-level"></a>
## 🔥 Fix Level

| Type               | Values                                                  | Description |
| ------------------ | ------------------------------------------------------- | ------------ |
| 🔥 **Fix Level**   | *System-wide* - **SYS**, *User-impact* - **USR**        | Defines **which layer or scope** of the system the fix impacts. |
| 🧠 **SYS (System-wide)** | — | The fix affects **core system components** or modules with **global impact** (e.g., kernel, drivers, APIs). |
| 👤 **USR (User-impact)** | — | The fix only influences **user-level features**, interfaces, or configurations. |

<br>
<br>

<a id="priorities"></a>
## 🚦 Priorities

| Priority Level | Code | Description |
| --------------- | ---- | ------------ |
| 🟢 **Low** | **LO** | Minor issue with **no immediate impact** on performance or security; can be scheduled for later updates. |
| 🔵 **Medium** | **M** | Issue that **affects usability or stability**, but has **available workarounds**. |
| 🟠 **High** | **HI** | Major issue that **impairs system functions** or user operations; should be addressed **promptly**. |
| 🔴 **Urgent** | **URG** | Critical issue causing **service interruption**, **data loss**, or **security risk**; requires **immediate action**. |


<br>
<br>

<!-- Fix Tracer-->

<a name="fix-tracer"></a>

# Fix Tracer

[Table of Contents](#table-of-contents)


| 🛠️ Fix | 🐛 Bug | 📝 Description | 🗓️ Applied on | 💻 Nature | 🔧 Method | 🔥 Level | 🧩 Versions | ⚙️ Features | 📦 Namespaces | 🔗 APIs | ⏫ Priority |
|--------|--------|----------------|---------------|-----------|-----------|-----------|--------------|--------------|---------------|---------|-------------|
| `F-001` | `1` | Patched **username validation** to correctly verify input and allow **login** to authorized users | 15/05/2025 | **SW** | Input validation patch + unit tests | **SYS** | <ul><li>[`v1.1.1`](md_Version_VERSION.html#v1.1.1)</li><li>[`v1.2.1`](md_Version_VERSION.html#v1.2.1)</li></ul> | <ul><li>[`data core features`](md_Version_FEATURE.html#data-core-features)</li></ul> | <ul><li>[`core`](md_Version_NAMESPACE.html#core)</li></ul> | <ul><li>[`core.data`](md_Version_API.html#core-data)</li></ul> | **URG** |
| `F-002` | `2` | Added **timeout validation** in token refresh logic | 19/05/2025 | **SW** | Added token expiry check before renewal | **APP** | <ul><li>[`v1.3.1`](md_Version_VERSION.html#v1.3.1)</li></ul> | <ul><li>[`auth features`](md_Version_FEATURE.html#auth-features)</li></ul> | <ul><li>[`auth`](md_Version_NAMESPACE.html#auth)</li></ul> | <ul><li>[`auth.token`](md_Version_API.html#auth-token)</li></ul> | **HIGH** |


<br>
<br>
<a name="see-also"></a>

# See Also

[Table of Contents](#table-of-contents)

<br>

The following documents are related to this:


<ul>
  <li>
    <span class="md-link" data-github="Version/RELEASE_POLICY.md" data-doxygen="md_Version_RELEASE_POLICY.html">
        <a href="RELEASE_POLICY.md"><b>Release Policy</b></a>
      </span> file, named <code>RELEASE_POLICY.md</code>, contains the ***Release Policy*** standard adopted in **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/FEATURE.md" data-doxygen="md_Version_FEATURE.html">
        <a href="FEATURE.md"><b>Features</b></a>
      </span> file, named <code>FEATURE.md</code>, contains the ***Features*** of **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/API.md" data-doxygen="md_Version_API.html">
        <a href="API.md"><b>APIs</b></a>
      </span> file, named <code>API.md</code>, contains the ***APIs*** of **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/CHANGELOG.md" data-doxygen="md_Version_CHANGELOG.html">
        <a href="CHANGELOG.md"><b>Change Log</b></a>
      </span> file, named <code>CHANGELOG.md</code>, contains the ***Changes*** made in **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/NAMESPACE.md" data-doxygen="md_Version_NAMESPACE.html">
        <a href="NAMESPACE.md"><b>Namespaces</b></a>
      </span> file, named <code>NAMESPACE.md</code>, contains the ***Namespace*** architecture of **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/BUG.md" data-doxygen="md_Version_BUG.html">
        <a href="BUG.md"><b>Bugs</b></a>
      </span> file, named <code>BUG.md</code>, contains the ***Bugs*** identified in **README Template**.
  </li>
  <li>
    <span class="md-link" data-github="Version/FIX.md" data-doxygen="md_Version_FIX.html">
        <a href="FIX.md"><b>Fixes</b></a>
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

For **more information** on [PROJECT_NAME] <a class="md-link" data-github="CONTACT_US.md" data-doxygen="md_CONTACT_US.html"><b>contact us</b></a>.

<a name="official-links"></a>

<!-- Official Links -->

# Official Links

[Table of Contents](#table-of-contents)

* [SemVer](https://www.semver.org) – A complete guide to **Semanting Verioning**. 
* [Doxygen](https://www.doxygen.nl/index.html) – **Documentation generator** for source code.
* [GitHub](https://github.com) – **Hosting** and **collaboration platform** for **Git** repositories.
* [Git](https://git-scm.com) – **Version control** system to manage source code.
* [GNU Make](https://www.gnu.org/software/make/) – **Build automation tool** to compile projects.

<br>
<br>

