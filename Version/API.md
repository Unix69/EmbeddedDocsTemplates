<h1> 🧩 API </h1>

<!-- Badges -->
<div align="bottom">
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
  <a href="https://github.com/Unix69/EmbeddedDocsTemplates/blob/master/LICENSE.md">
    <img src="https://img.shields.io/github/license/Unix69/EmbeddedDocsTemplates.svg" alt="license" />
  </a>
</div>

<!-- Link compatibili sia con GitHub che con Doxygen -->
🏗️ [Project](/PROJECT.md)
<span> · </span>
⭐ [Features](/Version/FEATURE.md)
<span> · </span>
🎮 [Use Cases](/Usage/USECASES.md)
<span> · </span>
🏷️ [Versions](/Version/VERSION.md)
<span> · </span>
📜 [Release Policy](/Version/RELEASE_POLICY.md)
<span> · </span>
📦 [Namespaces](/Version/NAMESPACE.md)
<span> · </span>
🧩 [APIs](/Version/API.md)
<span> · </span>
🐞 [Bugs](/Version/BUG.md)
<span> · </span>
🔧 [Fixes](/Version/FIX.md)
<span> · </span>
📋 [Change Log](/Version/CHANGELOG.md)
<span> · </span>
☎️ [Contact Us](/CONTACT_US.md)
<br>

<p>
<b>[PROJECT_NAME]</b> provides <em>Application Programmable Interfaces (APIs)</em> to make able <em>Actors</em> to iteract with it programmatically.
</p>

<br>
<br>

<!-- Table of Contents -->

<a name="table-of-contents"></a>

### 📓 Table of Contents

Navigation index to fast explore the content:

- [API Characteristics](#characteristics)
- [API Reference](#api-reference)
- [How To](#how-to)
  - [How To Integrate APIs](#how-to-integrate-apis)
  - [How To Develop APIs](#how-to-develop-apis)
- [FAQ](#faq)
- [Contact us](#contact-us)
- [See Also](#see-also)
- [Official Links](#official-links)

<br>
<br>

<a id="characteristics"></a>

# Characteristics

Each API defines:
  - a set of <em>Parameters</em> to specify during the <b>API Request</b>.
  - a <em>Response Type</em> returned on <b>API Response</b>. Both depend on the given API <b>implementation specifications</b> so read the single <b>API documentation</b> to know how each API act and how to use it.

<br>

## 🎮 Used by
APIs are used by:
    - <em>Features</em> to implement themself. Each API declare into which features they are used.
    - <em>Actors</em> into <em>Use Cases</em> to perform tasks. Each API declare for which actors they are suited for.
## ⭐ Versions
Each API is available on a specific <em>Version</em> and can contain <em>Bugs</em> solved by as soon as possible by <em>Fixes</em>. Each API release follow the 
<a class="md-link" data-github="RELEASE_POLICY.md" data-doxygen="md_Version_RELEASE_POLICY.html"><b>Release Policy</b></a>
and declare the implemented versions, the discovered bugs and provided fixes.
## 🧩 Collection
APIs are colleted into <em>Namespaces</em> that expose the API and other related resources to use the API properly. Each API declare the <em>Namespace</em> that contain themself.
## 🔐 Accessibility
API's accessibility is <em>Role</em> based, if the role used by the actor to access the API does not correspond to the admitted, the API will fail and return a permission fail respose. Each API declare the admitted roles.
## ↩️ Changes
An <em>API</em> can be modified by some <em>Changes</em>, during the [PROJECT_NAME] lifecycle so read the 
<a class="md-link" data-github="CHANGELOG.md" data-doxygen="md_Version_CHANGELOG.html"><b>Change Log</b></a>
to be updated with last API changes.
## 🛠️ Extendabilty
It's possibile to extend the set of APIs of each namespace by adding new API. To know how, follow the 
<a class="md-link" data-github="DEVELOPMENT_GUIDE.md" data-doxygen="md_Usage_DEVELOPMENT_GUIDE.html"><b>Development Guide</b></a>.
  

<br>

<!-- API Reference -->

<a id="api-reference"></a>

# API Reference

<br>

The whole set of API is divided into <b>Namespaces</b>. Each namespace is composed by some <b>Sub-Namespaces</b> that specialize it. The following navigation index contains all APIs grouped by namespaces:

- [Control](#control)
  - [Command](#command)
    - int <a href="#start">Start</a> (bool fast_start, bool exit_on_fail, int *level) - Initialize and start the control subsystem.<br>
    - int <a href="#exit">Exit</a> (bool fast_exit, bool exit_on_fail, int *level) - Safely terminate the control subsystem.<br> 
  - [Process](#process)
    - int <a href="#terminate">Terminate</a>() - Terminate the currently running process or subsystem.<br>
    - <a href="#wait">Wait</a>() - Wait for the completion of the process or child task.<br>

<br>
<br>

<a name="control"></a>

# Control


The <code>Control</code> namespace provides control capabilities and resources with its sub-namespace system:

- [Command](#command)
    - int <a href="#start">Start</a>(bool fast_start, bool exit_on_fail, int *level> - Initialize and start the control subsystem.<br>
    - int <a href="#exit">Exit</a>(bool fast_exit, bool exit_on_fail, int *level) - Safely terminate the control subsystem.<br> 
- [Process](#process)
    - int <a href="#terminate">Terminate</a>() - Terminate the currently running process or subsystem.<br>
    - <a href="#wait">Wait</a>() - Wait for the completion of the process or child task.<br>

<br>


<a name="command"></a>

## Command

The <code>Command</code> sub-namespace provides process and subsystem control operations.

  <summary><b>Command</b> Namespace</summary>
  <p>The <b>Command</b> namespace includes initialization and termination APIs.</p>

 - [Command](#command)
    - int <a href="#start">Start</a>(bool fast_start, bool exit_on_fail, int *level> - Initialize and start the control subsystem.<br>
    - int <a href="#exit">Exit</a>(bool fast_exit, bool exit_on_fail, int *level) - Safely terminate the control subsystem.<br> 

<br>
<br>

<br>
<br>

<!-- Start -->

<a name="start"></a>

### Start 📎

<br>


```html
int Start(bool fast_start, bool exit_on_fail, int level*);

```

<br>


##### 🧩 NAMESPACE


<a class="md-link" data-github="Version/NAMESPACE.md#command" data-doxygen="md_Version_NAMESPACE.html#command">Control::Command</a>

<br>


##### FULL-DESCRIPTOR

Control::Command::Start
<br>

##### 📋 DESCRIPTION

Start is a control command that starts 
<br>

##### ⚠️ REQUIREMENTS

Start requires v1.0.0 or above
<br>

##### AVAILABLE FROM

version > v1.0.0
<br>

##### 🛠️ PARAMETERS
 
- **bool fast_start**: enable fast start on start operation 
- **bool exit_on_fail**: exit when a fail during start occurs
- **int level***: optional level integer used to start 
<br>

##### ↩️ RETURNS

- **int result**:
<br>

##### ⛔ EXCEPTIONS

- **ResourceNotFoundException**: This exception occurs when the resources to start are not available.
- **PermissionDeinedException**: This exception occurs when permissions to start are not granted.
<br>

##### ❌ ERRORS
<br>

##### ⭐ EXAMPLES
<br>

##### 📋 NOTES

> When using start, be sure to import Control::Command namespace
<br>

---

<a name="exit"></a>


<!-- Exit -->
### Exit 📎
<br>


```html

int Exit(bool fast_exit, bool exit_on_fail, int level*);

```

<br>

##### 🧩 NAMESPACE

<a class="md-link" data-github="Version/NAMESPACE.md#command" data-doxygen="md_Version_NAMESPACE.html#command">Control::Command</a>

<br>

##### FULL-DESCRIPTOR

Control::Command::Exit
<br>

##### 📋 DESCRIPTION

Exit is a control command that exites 
<br>

##### ⚠️ REQUIREMENTS

Exit requires v1.0.0 or above
<br>

##### AVAILABLE FROM

version > v1.0.0
<br>

##### PARAMETERS
 
- **bool fast_exit**: enable fast exit on exit operation 
- **bool exit_on_fail**: exit when a fail during exit occurs
- **int level***: optional level integer used to exit 
<br>

##### ↩️ RETURNS

- **int result** 
<br>

##### ⛔  EXCEPTIONS

- **ResourceNotFoundException**: This exception occurs when the resources to start are not available.
- **PermissionDeinedException**: This exception occurs when permissions to start are not granted.
<br>

##### ❌ ERRORS 
<br>

##### ⭐ EXAMPLES
<br>

##### 📋 NOTES

> When using exit, be sure to import Control::Command namespace

<br>
<br>

<a name="process"></a>

## Process

  <summary><b>Process</b> Namespace</summary>
  <p>The <b>Process</b> subnamespace provides process handling APIs.</p>

  - [Process](#process)
    - int <a href="#terminate">Terminate</a>() - Terminate the currently running process or subsystem.<br>
    - <a href="#wait">Wait</a>() - Wait for the completion of the process or child task.<br>


<br>
<br>

<!-- Terminate -->

<a name="terminate"></a>


### Terminate 📎
<br>

```html

int Terminate();

```

<br>

##### 🧩 NAMESPACE

<a class="md-link" data-github="Version/NAMESPACE.md#process" data-doxygen="md_Version_NAMESPACE.html#process">Control::Process</a>


<br>

##### FULL-DESCRIPTOR

Control::Process::Exit
<br>

##### 📋 DESCRIPTION

Terminate is a control command that exites 
<br>

##### ⚠️ REQUIREMENTS

Terminate requires v1.0.0 or above
<br>

##### AVAILABLE FROM

version > v1.0.0
<br>

##### ↩️ RETURNS 

- **int result** 
<br>

##### ⛔  EXCEPTIONS
 
- **PermissionDeinedException**
<br>

##### ❌ ERRORS 

<br>

##### EXAMPLES

##### 📋 NOTES

> When using terminate, be sure to import Control::Process namespace
<br>

---


<a name="wait"></a>

<!-- Wait -->

### Wait 📎
<br>

```html
  int Wait();
```
<br>

##### 🧩 NAMESPACE

<a class="md-link" data-github="Version/NAMESPACE.md#process" data-doxygen="md_Version_NAMESPACE.html#process">Control::Process</a>

<br>

##### FULL-DESCRIPTOR


Control::Process::Wait
<br>

##### 📋 DESCRIPTION

Wait is a control command that waites 
<br>

##### ⚠️ REQUIREMENTS

Wait requires v1.0.0 or above
<br>

##### AVAILABLE FROM

version > v1.0.0
<br>

##### ↩️ RETURNS
 
- **int result** 
<br>

##### ⛔  EXCEPTIONS

- **PermissionDeinedException**:
<br>

##### ❌ ERRORS
<br>

##### ⭐ EXAMPLES
<br>

##### 📋 NOTES

> When using wait, be sure to import Control::Process namespace

<br>
<br>

<!-- How To-->

<a name="how-to"></a>

# How To 🛠️

[Table of Contents](#table-of-contents)

In this section we explain **How To** perform certain **tasks that involve APIs**. In particular there is explained:

- <a href="#how-to-integrate-apis">How To Integrate APIs</a> helps a Developer on how to integrate [PROJECT_NAME] APIs into new products.
- <a href="#how-to-develop-apis">How To Develop APIs</a> helps a Developer on how to develop new [PROJECT_NAME] APIs.

<br>

<!-- How To Integrate APIs-->

<a name="how-to-integrate-api"></a>

### How To Integrate APIs

[Table of Contents](#table-of-contents)


<br>

<!-- How To Develop APIs-->

<a name="how-to-develop-api"></a>

### How To Develop APIs

[Table of Contents](#table-of-contents)

<br>
<br>

<a name="see-also"></a>

# See Also

[Table of Contents](#table-of-contents)

<br>

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
