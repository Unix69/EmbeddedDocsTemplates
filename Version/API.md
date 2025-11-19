
<h1>
  🧩 API
</h1>

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
🐞 [**Bugs**](md_Version_BUG.html) 
<span> · </span>
🔧 [**Fixes**](md_Version_FIX.html)
<span> · </span>
📋 [**Change Log**](md_Version_CHANGELOG.html)
<span> · </span>
☎️ [**Contact Us**](md_CONTACT_US.html)

<br>

<p>
**[PROJECT_NAME]** provides ***Application Programmable Interfaces (APIs)*** to make able ***Actors*** to iteract with it programmatically.
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
  - a set of ***Parameters*** to specify during the **API Request**.
  - a ***Response Type*** returned on **API Response**. Both depend on the given API **implementation specifications** so read the single **API documentation** to know how each API act and how to use it.

<br>

## 🎮 Used by
APIs are used by:
    - ***Features*** to implement themself. Each API declare into which features they are used.
    - ***Actors*** into ***Use Cases*** to perform tasks. Each API declare for which actors they are suited for.
## ⭐ Versions
Each API is available on a specific ***Version*** and can contain ***Bugs*** solved by as soon as possible by ***Fixes***. Each API release follow the ***[Release Policy](/RELEASE_POLICY.md)*** and declare the implemented versions, the discovered bugs and provided fixes.
## 🧩 Collection
APIs are colleted into ***Namespaces*** that expose the API and other related resources to use the API properly. Each API declare the ***Namespace*** that contain themself.
## 🔐 Accessibility
API's accessibility is ***Role*** based, if the role used by the actor to access the API does not correspond to the admitted, the API will fail and return a permission fail respose. Each API declare the admitted roles.
## ↩️ Changes
An ***API*** can be modified by some ***Changes***, during the [PROJECT_NAME] lifecycle so read the ***[Change Log](/CHANGELOG.md)*** to be updated with last API changes.
## 🛠️ Extendabilty
It's possibile to extend the set of APIs of each namespace by adding new API. To know how, follow the ***[Development Guide](/Usage/DEVELOPMENT_GUIDE.md)*** .
  

<br>

<!-- API Reference -->

<a id="api-reference"></a>

# API Reference

<br>

The whole set of API is divided into **Namespaces**. Each namespace is composed by some **Sub-Namespaces** that specialize it. The following navigation index contains all APIs grouped by namespaces:

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


The `Control` namespace provides control capabilities and resources with its sub-namespace system:

- [Command](#command)
    - int <a href="#start">Start</a>(bool fast_start, bool exit_on_fail, int *level> - Initialize and start the control subsystem.<br>
    - int <a href="#exit">Exit</a>(bool fast_exit, bool exit_on_fail, int *level) - Safely terminate the control subsystem.<br> 
- [Process](#process)
    - int <a href="#terminate">Terminate</a>() - Terminate the currently running process or subsystem.<br>
    - <a href="#wait">Wait</a>() - Wait for the completion of the process or child task.<br>

<br>


<a name="command"></a>

## Command

The `Command` sub-namespace provides process and subsystem control operations.

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

<a href="/Version/NAMESPACE.md/#command">Control::Command</a>
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

<a href="/Version/NAMESPACE.md/#command">Control::Command</a>
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

<a href="/Version/NAMESPACE.md/#process">Control::Process</a>
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

<a href="/Version/NAMESPACE.md/#process">Control::Process</a>
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

