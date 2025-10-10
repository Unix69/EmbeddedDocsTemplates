<div align="center">

  <img src="/logo/logo.svg" alt="logo" width="48" height="48" />
  <h1>
    Namespace
  </h1>

  <!-- Badges -->
  <p>
    <a href="https://github.com/Unix69/EmbeddedDocsTemplates/graphs/contributors"><img src="https://img.shields.io/github/contributors/Unix69/EmbeddedDocsTemplates" alt="contributors" /></a>
    <a href=""><img src="https://img.shields.io/github/last-commit/Unix69/EmbeddedDocsTemplates" alt="last update" /></a>
    <a href="https://github.com/Unix69/EmbeddedDocsTemplates/network/members"><img src="https://img.shields.io/github/forks/Unix69/EmbeddedDocsTemplates" alt="forks" /></a>
    <a href="https://github.com/Unix69/EmbeddedDocsTemplates/stargazers"><img src="https://img.shields.io/github/stars/Unix69/EmbeddedDocsTemplates" alt="stars"/></a>
    <a href="https://github.com/Unix69/EmbeddedDocsTemplates/issues/"><img src="https://img.shields.io/github/issues/Unix69/EmbeddedDocsTemplates" alt="open issues" /></a>
    <a href="https://github.com/Unix69/EmbeddedDocsTemplates/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Unix69/EmbeddedDocsTemplates.svg" alt="license" /></a>
  </p>


  <h4>
      <a href="/Version/VERSION.md">Version</a>
      <span> · </span>
      <a href="/Version/RELEASE_POLICY.md">Release Policy</a>
      <span> · </span>
      <a href="/Version/FEATURE.md">Features</a>
      <span> · </span>
      <a href="/Version/CHANGELOG.md">Change Log</a>
      <span> · </span>
      <a href="/Version/API.md">API</a>
      <span> · </span>
      <a href="/Version/BUG.md">Bugs</a>
      <span> · </span>
      <a href="/Version/FIX.md">Fixes</a>
  </h4>

</div>

<br/>

<!-- Table of Contents -->

# :notebook_with_decorative_cover: Table of Contents

Navigation index to fast explore the content:

<br>
- [Namespace](#namespace)
- [Namespace Index](#namespace-index)
- [Namespace Reference](#namespace-reference)
- [How To](#how-to)
  - [How To Import Namespaces](#how-to-import-namespaces)
  - [How To Address APIs through Namespaces](#how-to-address-apis-through-namespaces)
- [See Also](#see-also)
- [Official Links](#official-links)

<br>

---

<!-- Namespace -->

## Namespace

The whole set of **[PROJECT_NAME] APIs** is divided into *Namespaces*. Each *Namespace* is composed by some *Sub-Namespaces* that specializing it.
Every Namespace provides *APIs* that implements *Features*. A *Namespace* is characterized by some **attributes** and **properties**. A *Namespace* can be modified by some *Namespace Changes*, during [PROJECT_NAME] lifecycle.

An *Attribute* is a Read Only (RO) field, representing the *Namespace* characteristic that cannot be changed by the namespace user.
While a *Property* is a RO or Readable and Writeable (RW) field, representing the *Namespace* characteristic that can be changed by the namespace user.



Furthermore every *Namespace* can contain *Namespace Bugs* that will be resolved by *Namespace Fixes*.

[PROJECT_NAME] Namespaces are collected into the **Namespace Index** section of this document and each of them is characterized by some attributes, that globally define the *Namespace* itself. This attributes are listed into the table
below

<br>

| Namespace Atrribute | Namespace Atrribute Description | Namespace Atrribute Value | 
| ------------------- | ------------------------------- | ------------------------- |
| **Namespace ID - NID** | a unique id **identifing a namespace** | an alphanumeric string |
| **Version IDs** | list of unique ids **identifing the Versions** on which the namespace is present | a set of alphanumeric strings |
| **Feature IDs** | list of unique ids **identifing the Features** related to this namespace | a set of alphanumeric strings |
| **Change IDs** | list of unique ids **identifing the Changes** related to this namespace | a set of alphanumeric strings |
| **API IDs** | list of unique ids **identifing the APIs** contained into this namespace | a set of alphanumeric strings |
| **Bug IDs** | list of unique ids **identifing the Bugs** found on this namespace | a set of alphanumeric strings |
| **Fix IDs** | list of unique ids **identifing the Fixes** performed on this namespace | a set of alphanumeric strings |

<br>

---

<br>

<!-- Namespaces Index -->

## Namespaces Index

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

| Namespace ID | Version IDs | Feature IDs | Change IDs | API IDs | Bug IDs | Fix IDs |
| ------------ | ----------- | ----------- | ---------- | ------- | ------- | ------- |
| | | | | | | | 
| | | | | | | | 
| | | | | | | | 
| | | | | | | | 
| | | | | | | | 
| | | | | | | |
| | | | | | | |

<br>

For a complete description of each Namespace (its attributes and properties), follow the <a href="#namespace-reference">Namespace Reference</a>.

<br>

---

<!-- Namespace Reference -->

## Namespace Reference

The following index represents the [PROJECT_NAME] namespace division:

<dl>
<dt><details>
<summary><a href="#star-control">Control</a></summary>
<dd>
  <dl>
  <dt><a href="#star-command">Command</a></dt>
  <dt><a href="#star-process">Process</a></dt>
  </dl>
</dd>
</details>
</dt>

</dl>

<br>

Navigate this reference to **explore [PROJECT_NAME] Namespaces**.

<br>


<!-- Control -->

## :star: Control

<br>

*Control* is a **Namespace** of [PROJECT_NAME] **containing all control namespaces and APIs used to manage [PROJECT_NAME]**

<br>

**Requirements**:
  - :warning: The **minimum required version** is *v1.0.0*

<br>

**State**:
  - **Obsolete** from version *v1.0.0*
  - **Deprecated** from version *v2.0.0* :x:
 
<br>

| :scroll:Sub Namespace | Full Name | Brief Description |
| --------------------- | --------- | ----------------- |
| <a href="#star-command">Command</a> | *Control::Command* | Brief Description |
| <a href="#star-process">Process</a> | *Control::Process* | Brief Description |


<br>

| :wrench:Attribute | Full Name | Type | Description |
| ----------------- | --------- | ---- | ----------- |
| ***fast_start*** | *Control::fast_start* | **bool** | enable fast start on start operation |
| ***exit_on_fail*** | *Control::exit_on_fail* | **bool** | exit when a fail during start occurs |
| ***level*** | *Control::level* | **int** | optional level integer used to start |

<br>

| :star:Property | Full Name | Type | Permissions | Description |
| -------------- | --------- | ---- | ----------- | ----------- |
| ***fast_start*** | *Control::fast_start* | **bool** | RW | enable fast start on start operation |
| ***exit_on_fail*** | *Control::exit_on_fail* | **bool** | RW | exit when a fail during start occurs |
| ***level*** | *Control::level* | **int** | R | optional level integer used to start |

<br>

*Control* namespace contains the following API:

<br>

| API | Full Name | Brief Description |
| --- | --------- | ----------------- | 
| ***<a href="/Version/API.md/#configure">configure</a>*** | *Control::configure*  | **configure** permits to configure the control layer of [PROJECT_NAME] |
| ***<a href="/Version/API.md/#setup">setup</a>*** | *Control::setup* | **setup** permits to setup the control layer of [PROJECT_NAME] |
| ***<a href="/Version/API.md/#exit">exit</a>*** | *Control::exit* | **exit** permits to terminate the control process of [PROJECT_NAME] |

<br>

<!-- Command -->

## :star: Command

<br>

*Command* is a **Sub-Namespace** of <a href="#control">Control</a> **containing all command APIs used to execute commands on [PROJECT_NAME]**. To explore this namespace (its attributes and properties) visit <a href="/Version/NAMESPACE.md/#command">Command Sub-Namespace</a>.  

<br>

**Dependencies**:
  - <a href="#star-control">Control</a>

<br>

**Requirements**:
  - :warning: The **minimum required version** is *v1.0.0*

<br>

**State**:
  - **Obsolete** from version *v1.0.0*
  - **Deprecated** from version *v2.0.0* :x:

<br>

| :wrench:Attribute | Full Name | Type | Description |
| ----------------- | --------- | ---- | ----------- |
| ***fast_start*** | *Control::Command::fast_start* | **bool** | enable fast start on start operation |
| ***exit_on_fail*** | *Control::Command::exit_on_fail* | **bool** | exit when a fail during start occurs |
| ***level*** | *Control::Command::level* | **int** | optional level integer used to start |

<br>

| :star:Property | Full Name | Type | Permissions | Description |
| -------------- | --------- | ---- | ----------- | ----------- |
| ***fast_start*** | *Control::Command::fast_start* | **bool** | RW | enable fast start on start operation |
| ***exit_on_fail*** | *Control::Command::exit_on_fail* | **bool** | RW | exit when a fail during start occurs |
| ***level*** | *Control::Command::level* | **int** | R | optional level integer used to start |

<br>

*Command* sub-namespace contains the following API:

<br>

| API | Full Name | Brief Description |
| --- | --------- | ----------------- | 
| ***<a href="/Version/API.md/#configure">configure</a>*** | *Control::Command::configure*  | **configure** permits to configure the control layer of [PROJECT_NAME] |
| ***<a href="/Version/API.md/#setup">setup</a>*** | *Control::Command::setup* | **setup** permits to setup the control layer of [PROJECT_NAME] |
| ***<a href="/Version/API.md/#exit">exit</a>*** | *Control::Command::exit* | **exit** permits to terminate the control process of [PROJECT_NAME] |

<br>

---

<!-- Process -->

## :star: Process
<br>

*Process* is a **Sub-Namespace** of <a href="#control">Control</a> **containing all processes APIs used to manage processes in [PROJECT_NAME]**. To explore this namespace (its attributes and properties) visit <a href="/Version/NAMESPACE.md/#process">Process Sub-Namespace</a>.   

<br>

**Dependencies**:
  - <a href="#star-control">Control</a>

<br>

**Requirements**:
  - :warning: The **minimum required version** is *v1.0.0*


<br>

**State**:
  - **Obsolete** from version *v1.0.0*
  - **Deprecated** from version *v2.0.0* :x:

<br>

| :wrench:Attribute | Full Name | Type | Description |
| ----------------- | --------- | ---- | ----------- |
| ***fast_start*** | *Control::Process::fast_start* | **bool** | enable fast start on start operation |
| ***exit_on_fail*** | *Control::Process::exit_on_fail* | **bool** | exit when a fail during start occurs |
| ***level*** | *Control::Process::level* | **int** | optional level integer used to start |

<br>

| :star:Property | Full Name | Type | Permissions | Description |
| --------------- | --------- | ---- | ----------- | ----------- |
| ***fast_start*** | *Control::Process::fast_start* | **bool** | RW | enable fast start on start operation |
| ***exit_on_fail*** | *Control::Process::exit_on_fail* | **bool** | RW | exit when a fail during start occurs |
| ***level*** | *Control::Process::level* | **int** | R | optional level integer used to start |

<br>

*Process* sub-namespace contains the following API:

<br>

| API | Full Name | Brief Description |
| --- | --------- | ----------------- | 
| ***<a href="/Version/API.md/#configure">configure</a>*** | *Control::Process::configure*  | **configure** permits to configure the control layer of [PROJECT_NAME] |
| ***<a href="/Version/API.md/#setup">setup</a>*** | *Control::Process::setup* | **setup** permits to setup the control layer of [PROJECT_NAME] |
| ***<a href="/Version/API.md/#exit">exit</a>*** | *Control::Process::exit* | **exit** permits to terminate the control process of [PROJECT_NAME] |

<br>

---

<!-- How To-->

## How To

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

In this section we explain **How To** perform certain **tasks that involve Namespaces and APIs**. In particular there is explained:

- <a href="#how-to-import-namespaces">How To Import Namespaces</a> helps a Developer on how to import [PROJECT_NAME] Namespaces into new projects.
- <a href="#how-to-address-apis-through-namespaces">How To Address APIs through Namespaces</a> helps a Developer on how to address APIs through their Namespaces.

<br>

<!-- How To Import Namespaces-->

### How To Import Namespaces

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)


<br>

<!-- How To Address APIs through Namespaces-->

### How To Address APIs through Namespaces

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

<br>

---



<!-- FAQ -->

## FAQ

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)


* Empty


<!-- Contact us  -->

## Contact us

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

For any question or help request on [PROJECT_NAME] **Versions**, **Release Policy**, **Features**, **Changes**, **Namespaces**, **APIs**, **Bugs** or **Fixes** please contact us using our [Contacts](/CONTACT_US.md).



<!-- See Also -->

## See Also

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

The following documents are related to this:

* The [Version](/VERSION.md) file, named `VERSION.md`, contains the version history of **[PROJECT_NAME]**
* The [Release Policy](/RELEASE_POLICY.md) file, named `RELEASE_POLICY.md`, contains the release policy standard adopted in **[PROJECT_NAME]**.
* The [Features](/FEATURE.md) file, named `FEATURE.md`, contains the features of **[PROJECT_NAME]**, labeled 
* The [Change Log](/CHANGELOG.md) file, named `CHANGELOG.md`, contains the changes made on **[PROJECT_NAME]**
* The [Namespace](/NAMESPACE.md) file, named `NAMESPACE.md`, contains the namespace architecture of **[PROJECT_NAME]**
* The [Bugs](/BUG.md) file, named `BUG.md`, contains the bug made on **[PROJECT_NAME]**
* The [Fixes](/FIX.md) file, named `FIX.md`, contains the fixes made on **[PROJECT_NAME]**


<!-- Official Links -->

## Official Links

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

Consult the official <a href="https://www.semver.org" target="_blank">SemVer guide</a> for a complete guide on SemVer
