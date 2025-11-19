<h1>
  🐞 Bugs
</h1>

<!-- Badges -->
<p>
  <a href=""><img src="https://img.shields.io/github/last-commit/Unix69/EmbeddedDocsTemplates" alt="last update" /></a>
  <a href="https://github.com/Unix69/EmbeddedDocsTemplates/issues/"><img src="https://img.shields.io/github/issues/Unix69/EmbeddedDocsTemplates" alt="open issues" /></a>
</p>

 🏗️ [**Project**](md_PROJECT.html)
  <span> · </span>
  ⭐ [**Features**](md_Version_FEATURE.html)
  <span> · </span>
  🎮 [**Use Cases**](md_Usage_USECASES.html)
  <span> · </span>
  🏷️ [**Versions**](md_Version_VERSION.html)
  <span> · </span>
  📜 [**Release Policy**](md_Version_RELEASE_POLICY.html)
  <span> · </span>
  📦 [**Namespaces**](md_Version_NAMESPACE.html) 
  <span> · </span>
  🧩  [**APIs**](md_Version_API.html) 
  <span> · </span>
  🔧 [**Fixes**](md_Version_FIX.html)
  <span> · </span>
  📋 [**Change Log**](md_Version_CHANGELOG.html)
  <span> · </span>
  ☎️ [**Contact Us**](md_CONTACT_US.html)

<br>
<br>

A ***Bug*** in **[PROJECT_NAME]** is a design or implementation defect that occurs or is discovered in one or more of its  
***[Versions](md_Version_VERSION.html)***, ***[Features](md_Version_FEATURE.html)***,  
***[Namespaces](md_Version_NAMESPACE.html)***, or ***[APIs](md_Version_API.html)***.  

Such a defect exposes the system to specific ***vulnerabilities***, which may be exploited by ***threats*** through targeted ***attacks***, potentially causing a significant ***impact*** on the overall system behavior or integrity.  

Each ***Bug*** must be addressed by an appropriate ***[Fix](md_Version_FIX.html)***, which patches the vulnerability and updates the corresponding software **version**, following the defined  
***[Release Policy](md_Version_RELEASE_POLICY.html)***.  

After a **Fix** is applied, the affected version of the [PROJECT_NAME] release is incremented accordingly.  

All discovered bugs are **registered** in the **Bug Tracer** and are **fully documented** below.

<br>
<br>

<!-- Table of Contents -->

<a name="table-of-contents"></a>

### 📓 Table of Contents

Navigation index to fast explore the content:

- [Types](#types)
- [Priorities](#priorities)
- [Bug Tracer](#bug-tracer)
- [FAQ](#faq)
- [Contact Us](#contact-us)
- [See Also](#see-also)
- [Official Links](#official-links)

<br>
<br>

<a name="types"></a>

## 🐛 Types

| Type | Values | Description |
| ------ | --------------- | ------------ |
| ⚙️ **Bug Nature** | *Hardware* - **HW**, *Software* - **SW** | Defines the **origin** of the bug — whether it stems from hardware malfunction or software defect. |
| 🔥 **Bug Level** | *System* - **SYS**, *User* - **USR** | Indicates the **impact scope** — system-wide (core modules) or user-level (application features). |
| 🧩 **HW (Hardware)** | — | The bug originates from **physical components**, circuits, or embedded firmware interactions. |
| 💻 **SW (Software)** | — | The bug comes from **code logic**, **API misuse**, or incorrect software behavior. |
| 🧠 **SYS (System)** | — | Affects **core services**, kernel modules, or global resources shared by multiple subsystems. |
| 👤 **USR (User)** | — | Affects **user interface**, session management, or per-user configurations only. |

<br>
<br>

<a name="priorities"></a>

## 🚦 Priorities

| Priority | Code | Description |
| ------ | ---- | ------------ |
| 🟢 **Low** | **LO** | Minor glitch, negligible effect on functionality or security; can be postponed. |
| 🔵 **Medium** | **M** | Noticeable issue that affects stability or usability, but has workarounds. |
| 🟠 **High** | **HI** | Major issue reducing functionality or system reliability; requires prompt fix. |
| 🔴 **Urgent** | **URG** | Critical problem causing crashes, security breaches, or service interruptions; fix immediately. |

<br>
<br>

<a name="bug-tracer"></a>

## 🧾 Bug Tracer

All discovered **Bugs** in **[PROJECT_NAME]** are tracked here, with full details on their origin, severity, affected modules, and related fixes.

Each bug is linked to:
- 🧩 Affected **Versions**
- ⚙️ Related **Features**
- 📦 **Namespaces**
- 🔗 **APIs**
- 🛠️ The **Fix** that resolves it


| 🐛 Bug | 📝 Description | 🗓️ Discovered on | 🛡️ Vulnerabilities | ⚠️ Threats | 💥 Attacks | 💣 Impact | ⚙️ Nature | 🔥 Level | 🧩 Versions | ⚙️ Features | 📦 Namespaces | 🔗 APIs | ⏫ Priority |
| ------ | --------------- | ---------------- | ------------------ | ----------- | ----------- | ----------------- | ----------------- | --------------- | -------------- | -------------- | -------------- | -------------- | --------------- |
| `1` | The **username string** is not correctly verified, so **login** is **denied** to all users | 14/05/2025 | Bad username verification | - | DoS, DDoS | Availability and Usability | **SW** | **SYS** | <ul><li>`v1.1.0`</li><li>`v1.2.0`</li></ul> | <ul><li>`data core features`</li></ul> | <ul><li>`core`</li></ul> | <ul><li>`core.data`</li></ul> | **URG** |


<br>

<a name="see-also"></a>

# See Also

<br>

The following documents are related to this:

* The [**Project**](md_PROJECT.html) file, named `PROJECT.md`, contains the ***Project Description*** of **[PROJECT_NAME]**.  
* The [**Use Cases**](md_Usage_USECASES.html) file, named `USECASES.md`, shows the ***Use Cases*** of **[PROJECT_NAME]**.  
* The [**Actors**](md_Usage_ACTORS.html) file, named `ACTORS.md`, explains the types of ***Actors*** in **[PROJECT_NAME]**.  
* The [**Roles**](md_Usage_ROLES.html) file, named `ROLES.md`, describes the ***Roles*** of the ***Actors*** in **[PROJECT_NAME]**.  
* The [**Administrator Guide**](md_Usage_ADMINISTRATOR_GUIDE.html) file, named `ADMINISTRATOR_GUIDE.md`, explains to ***Administrators*** how to manage **[PROJECT_NAME]**.  
* The [**User Guide**](md_Usage_USER_GUIDE.html) file, named `USER_GUIDE.md`, explains to ***Users*** how to use **[PROJECT_NAME]**.  
* The [**Developer Guide**](md_Usage_DEVELOPMENT_GUIDE.html) file, named `DEVELOPMENT_GUIDE.md`, explains to ***Developers*** how to develop **[PROJECT_NAME]**.  
* The [**Versions**](md_Version_VERSION.html) file, named `VERSION.md`, shows and explains each ***Version*** of **[PROJECT_NAME]**.  
* The [**Release Policy**](md_Version_RELEASE_POLICY.html) file, named `RELEASE_POLICY.md`, contains the ***Release Policy*** standard adopted in **[PROJECT_NAME]**.  
* The [**Features**](md_Version_FEATURE.html) file, named `FEATURE.md`, contains the ***Features*** of **[PROJECT_NAME]**.  
* The [**APIs**](md_Version_API.html) file, named `API.md`, contains the ***APIs*** of **[PROJECT_NAME]**.  
* The [**Change Log**](md_Version_CHANGELOG.html) file, named `CHANGELOG.md`, contains the ***Changes*** made in **[PROJECT_NAME]**.  
* The [**Namespaces**](md_Version_NAMESPACE.html) file, named `NAMESPACE.md`, contains the ***Namespace*** architecture of **[PROJECT_NAME]**.  
* The [**Bugs**](md_Version_BUG.html) file, named `BUG.md`, contains the ***Bugs*** identified in **[PROJECT_NAME]**.  
* The [**Fixes**](md_Version_FIX.html) file, named `FIX.md`, contains the ***Fixes*** applied to **[PROJECT_NAME]**.  

<br>


<a name="faq"></a>


# FAQ ❓

Here you can find the Frequently Asked Questions and Answers.

<br>
<br>

<a name="contact-us"></a>


# Contact us ☎️

For **more information** on [PROJECT_NAME] [**contact us**](md_CONTACT_US.html).

<br>
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