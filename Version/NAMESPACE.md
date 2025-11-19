<h1>
  📦 Namespace
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
<br>

<!-- Table of Contents -->

<a name="table-of-contents"></a>

### 📓 Table of Contents

Navigation index to fast explore the content:

<br>

- [Namespace Reference](#namespace-reference)
- [How To](#how-to)
  - [How To Import Namespaces](#how-to-import-namespaces)
  - [How To Address APIs through Namespaces](#how-to-address-apis-through-namespaces)
- [See Also](#see-also)
- [FAQ](#faq)
- [Official Links](#official-links)

<br>
<br>

<!-- Namespace Reference -->

<a name="namespace-ference"></a>


## Namespace Reference

The following navigation index represents the [PROJECT_NAME] namespace division into namespaces and sub-namespaces:

- [Control](#control)
  - [Command](#command)
  - [Process](#process)

<br>
<br>
<br>

<!-- Control -->

<a name="control"></a>

## 📎 Control 

<br>

*Control* is a **Namespace** of [PROJECT_NAME] **containing all control namespaces and APIs used to manage [PROJECT_NAME]**

<br>

**Requirements**:
  - ⚠️  The **minimum required version** is *v1.0.0*

<br>

**State**:
  - **Obsolete** from version *v1.0.0*
  - **Deprecated** from version *v2.0.0* :x:
 
<br>

| 📦 Sub Namespace | Full Name | Brief Description |
| --------------------- | --------- | ----------------- |
| <a href="#star-command">Command</a> | *Control::Command* | Brief Description |
| <a href="#star-process">Process</a> | *Control::Process* | Brief Description |


<br>

| 🔧 Attribute | Full Name | Type | Description |
| ----------------- | --------- | ---- | ----------- |
| ***fast_start*** | *Control::fast_start* | **bool** | enable fast start on start operation |
| ***exit_on_fail*** | *Control::exit_on_fail* | **bool** | exit when a fail during start occurs |
| ***level*** | *Control::level* | **int** | optional level integer used to start |

<br>

| ⭐ Property | Full Name | Type | Permissions | Description |
| -------------- | --------- | ---- | ----------- | ----------- |
| ***fast_start*** | *Control::fast_start* | **bool** | RW | enable fast start on start operation |
| ***exit_on_fail*** | *Control::exit_on_fail* | **bool** | RW | exit when a fail during start occurs |
| ***level*** | *Control::level* | **int** | R | optional level integer used to start |

<br>

*Control* namespace contains the following API:

<br>

| 🧩 API | Full Name | Brief Description |
| --- | --------- | ----------------- | 
| ***<a href="md_Version_API.html#start">start</a>*** | *control::command::start*  | **start** permits initialize and start the control process |
| ***<a href="md_Version_API.html#exit">exit</a>*** | **control::command::exit* | **exit** permits to terminate the control process subsystem|
| ***<a href="md_Version_API.html#terminate">terminate</a>*** | *control::process::terminate* | **terminate** permits to safely terminate the control process subsystem |
| ***<a href="md_Version_API.html#wait">wait</a>*** | *control::process:wait* | **wait** permits to wait for the completion of the control process or child task |

<br>


---

<br>

<!-- Command -->

<a name="command"></a>

## 📎 Command

<br>

*Command* is a **Sub-Namespace** of <a href="#control">Control</a> **containing all command APIs used to execute commands on [PROJECT_NAME]**. To explore this namespace (its attributes and properties) visit <a href="/Version/NAMESPACE.md/#command">Command Sub-Namespace</a>.  

<br>

**Dependencies**:
  - <a href="#star-control">Control</a>

<br>

**Requirements**:
  - ⚠️  The **minimum required version** is *v1.0.0*

<br>

**State**:
  - **Obsolete** from version *v1.0.0*
  - **Deprecated** from version *v2.0.0* :x:

<br>

| 🔧 Attribute | Full Name | Type | Description |
| ----------------- | --------- | ---- | ----------- |
| ***fast_start*** | *Control::Command::fast_start* | **bool** | enable fast start on start operation |
| ***exit_on_fail*** | *Control::Command::exit_on_fail* | **bool** | exit when a fail during start occurs |
| ***level*** | *Control::Command::level* | **int** | optional level integer used to start |

<br>

| ⭐ Property | Full Name | Type | Permissions | Description |
| -------------- | --------- | ---- | ----------- | ----------- |
| ***fast_start*** | *Control::Command::fast_start* | **bool** | RW | enable fast start on start operation |
| ***exit_on_fail*** | *Control::Command::exit_on_fail* | **bool** | RW | exit when a fail during start occurs |
| ***level*** | *Control::Command::level* | **int** | R | optional level integer used to start |

<br>

*Command* sub-namespace contains the following API:

<br>

| 🧩 API | Full Name | Brief Description |
| --- | --------- | ----------------- | 
| ***<a href="md_Version_API.html#start">start</a>*** | *control::command::start*  | **start** permits initialize and start the control process |
| ***<a href="md_Version_API.html#exit">exit</a>*** | **control::command::exit* | **exit** permits to terminate the control process subsystem|


<br>

---

<!-- Process -->


<a name="process"></a>

##  📎 Process
<br>

*Process* is a **Sub-Namespace** of <a href="#control">Control</a> **containing all processes APIs used to manage processes in [PROJECT_NAME]**. To explore this namespace (its attributes and properties) visit <a href="/Version/NAMESPACE.md/#process">Process Sub-Namespace</a>.   

<br>

**Dependencies**:
  - <a href="#star-control">Control</a>

<br>

**Requirements**:
  - ⚠️  The **minimum required version** is *v1.0.0*


<br>

**State**:
  - **Obsolete** from version *v1.0.0*
  - **Deprecated** from version *v2.0.0* :x:

<br>

| 🔧 Attribute | Full Name | Type | Description |
| ----------------- | --------- | ---- | ----------- |
| ***fast_start*** | *Control::Process::fast_start* | **bool** | enable fast start on start operation |
| ***exit_on_fail*** | *Control::Process::exit_on_fail* | **bool** | exit when a fail during start occurs |
| ***level*** | *Control::Process::level* | **int** | optional level integer used to start |

<br>

| ⭐ Property | Full Name | Type | Permissions | Description |
| --------------- | --------- | ---- | ----------- | ----------- |
| ***fast_start*** | *Control::Process::fast_start* | **bool** | RW | enable fast start on start operation |
| ***exit_on_fail*** | *Control::Process::exit_on_fail* | **bool** | RW | exit when a fail during start occurs |
| ***level*** | *Control::Process::level* | **int** | R | optional level integer used to start |

<br>

*Process* sub-namespace contains the following API:

<br>

| 🧩 API | Full Name | Brief Description |
| --- | --------- | ----------------- | 
| ***<a href="md_Version_API.html#terminate">terminate</a>*** | *control::process::terminate* | **terminate** permits to safely terminate the control process subsystem |
| ***<a href="md_Version_API.html#wait">wait</a>*** | *control::process:wait* | **wait** permits to wait for the completion of the control process or child task |

<br>


<!-- How To-->

# How To

[Table of Contents](#table-of-contents)

In this section we explain **How To** perform certain **tasks that involve Namespaces and APIs**. In particular there is explained:

- [**How To Import ⬇️ Namespaces**](#how-to-import-namespaces) helps a **Developer** on how to import [PROJECT_NAME] Namespaces into new projects.
- [**How To Address APIs 🧩 through Namespaces**](##how-to-address-apis-through-namespaces) helps a **Developer** on how to address APIs through their Namespaces.

<br>

<!-- How To Import Namespaces-->

<a name="how-to-import-namespaces"></a>

### ⬇️ How To Import Namespaces

[Table of Contents](#table-of-contents)


<br>

<!-- How To Address APIs through Namespaces-->

<a name="how-to-address-apis-through-namespaces"></a>

### 🧩 How To Address APIs through Namespaces

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
[PROJECT_NAME]**.  
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