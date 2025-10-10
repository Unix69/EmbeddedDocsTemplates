<div align="center">

  <img src="/logo/logo.svg" alt="logo" width="48" height="48" />
  <h1>
    API
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
      <a href="/Version/NAMESPACE.md">Namespace</a>
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

- [API](#api)
- [API Index](#api-index)
- [API Reference](#api-reference)
- [How To](#how-to)
  - [How To Integrate APIs](#how-to-integrate-apis)
  - [How To Develop APIs](#how-to-develop-apis)
- [FAQ](#faq)
- [Contact us](#contact-us)
- [See Also](#see-also)
- [Official Links](#official-links)

<br>

---

<!-- API -->

## API

In **[PROJECT_NAME]** an *Application Programmable Interface - API* is used to iteract with [PROJECT_NAME] by following a *Request-Response* schema.
The Client performs a *Request* by invoking the *API*, and the Server satisfies the *Request* and emits a *Response*.
It defines a set of *Parameters* settable during the *Request*, and a *Response Type* returned during the *Answer*. Both depend on the given *API* implementation specifications.

APIs are organized into *Namespaces* and implement *Features*.
An *API* can be modified by some *API Changes*, during the [PROJECT_NAME] lifecycle. An *API* is available from a given [PROJECT_NAME] *Version*.
Furthermore every [PROJECT_NAME] *API* can contain *API Bugs* that will be resolved by *API Fixes*.

[PROJECT_NAME] APIs are collected into the **API Index** section of this document and each of them is characterized by some attributes, that globally define the *API* itself. This attributes are listed into the table below

<br>

| API Atrribute | API Atrribute Description | API Atrribute Value | 
| ------------- | ------------------------- | ------------------- |
| **API ID - APIID** | a unique id **identifing a API** | an alphanumeric string |
| **API Name** | a name **used to call the API** | an alphanumeric text |
| **Namespace ID** | a unique id **identifing the Namespace** which belong this API | a set of alphanumeric strings |
| **Version IDs** | list of unique ids **identifing the Versions** on which the API is present | a set of alphanumeric strings |
| **Feature IDs** | list of unique ids **identifing the Features** related to this API | a set of alphanumeric strings |
| **Change IDs** | list of unique ids **identifing the Changes** related to this API | a set of alphanumeric strings |
| **Bug IDs** | list of unique ids **identifing the Bugs** found on this API | a set of alphanumeric strings |
| **Fix IDs** | list of unique ids **identifing the Fixes** performed on this API | a set of alphanumeric strings |
| **Deprecated From** | the date **when the API is considered deprecated** | a datetime string in the form DD/MM/YYYY:T:HH:MM:SS-GMT+Z |
| **Obsolete From** | the date **when the API is considered obsolete** | a datetime string in the form DD/MM/YYYY:T:HH:MM:SS-GMT+Z |

<br>

---

<!-- API Index -->

## API Index

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

The following table contains the index of APIs present in [PROJECT_NAME]

<br>

| API ID - APIID | API Name | Namespace ID | Version IDs | Feature IDs | Change IDs | Bug IDs | Fix IDs | Deprecated From | Obsolete From |
| -------------- | -------- | ------------ | ----------- | ----------- | ---------- | ------- | ------- | --------------- | ------------- |
| | | | | | | | |

<br>

For a complete description of each API and its usage, follow the <a href="#api-reference">API Reference</a>.

<br>

---

<!-- API Reference -->

## API Reference

The whole set of API is divided into **Namespaces**. Each namespace is composed by some **Sub-Namespaces** that specialize it. The following index contains all APIs divided into [PROJECT_NAME] namespaces:

<dl>
<dt>Control</dt>
<dd>
<dl>
<dt><details>
<summary>Command</summary>
  <ul>
      <li>int <a href="#paperclip-start">Start</a>(bool fast_start, bool exit_on_fail, int level*)</li>
      <li>int <a href="#paperclip-exit">Exit</a>(bool fast_exit, bool exit_on_fail, int level*)</li>
  </ul>
</details></dt>
<dt><details>
<summary>Process</summary>
  <ul>
      <li>int <a href="#paperclip-terminate">Terminate</a>()</li>
      <li>int <a href="#paperclip-wait">Wait</a>()</li>
  </ul>
</details></dt>
</dl>
</dd>
</dl>

<br>

Navigate this reference to **explore [PROJECT_NAME] APIs**.

<br>

---

<!-- Start -->

### :paperclip: Start

<br>


```c++

int Start(bool fast_start, bool exit_on_fail, int level*);

```

<br>


##### NAMESPACE

<a href="/Version/NAMESPACE.md/#paperclip-command">Control::Command</a>
<br>


##### FULL-DESCRIPTOR

Control::Command::Start
<br>

##### :scroll: DESCRIPTION

Start is a control command that starts 
<br>

##### :warning: REQUIREMENTS

Start requires v1.0.0 or above
<br>

##### AVAILABLE FROM

version > v1.0.0
<br>

##### :wrench: PARAMETERS
 
- **bool fast_start**: enable fast start on start operation 
- **bool exit_on_fail**: exit when a fail during start occurs
- **int level***: optional level integer used to start 
<br>

##### :leftwards_arrow_with_hook: RETURNS

- **int result**:
<br>

##### :no_entry: EXCEPTIONS

- **ResourceNotFoundException**: This exception occurs when the resources to start are not available.
- **PermissionDeinedException**: This exception occurs when permissions to start are not granted.
<br>

##### :x: ERRORS
<br>

##### :star: EXAMPLES
<br>

##### :memo: NOTES

> When using start, be sure to import Control::Command namespace
<br>

---

<!-- Exit -->
### :paperclip: Exit
<br>


```c++

int Exit(bool fast_exit, bool exit_on_fail, int level*);

```

<br>

##### NAMESPACE

<a href="/Version/NAMESPACE.md/#paperclip-command">Control::Command</a>
<br>

##### FULL-DESCRIPTOR

Control::Command::Exit
<br>

##### :scroll: DESCRIPTION

Exit is a control command that exites 
<br>

##### :warning: REQUIREMENTS

Exit requires v1.0.0 or above
<br>

##### AVAILABLE FROM

version > v1.0.0
<br>

##### :wrench: PARAMETERS
 
- **bool fast_exit**: enable fast exit on exit operation 
- **bool exit_on_fail**: exit when a fail during exit occurs
- **int level***: optional level integer used to exit 
<br>

##### :leftwards_arrow_with_hook: RETURNS

- **int result** 
<br>

##### :no_entry: EXCEPTIONS

- **ResourceNotFoundException**: This exception occurs when the resources to start are not available.
- **PermissionDeinedException**: This exception occurs when permissions to start are not granted.
<br>

##### :x: ERRORS 
<br>

##### :star: EXAMPLES
<br>

##### :memo: NOTES

> When using exit, be sure to import Control::Command namespace
<br>

---

<!-- Terminate -->

### :paperclip: Terminate
<br>

```c++

int Terminate();

```

<br>

##### NAMESPACE

<a href="/Version/NAMESPACE.md/#paperclip-process">Control::Process</a>
<br>

##### FULL-DESCRIPTOR

Control::Process::Exit
<br>

##### :scroll: DESCRIPTION

Terminate is a control command that exites 
<br>

##### :warning: REQUIREMENTS

Terminate requires v1.0.0 or above
<br>

##### AVAILABLE FROM

version > v1.0.0
<br>

##### :leftwards_arrow_with_hook: RETURNS 

- **int result** 
<br>

##### :no_entry: EXCEPTIONS
 
- **PermissionDeinedException**
<br>

##### :x: ERRORS 

<br>

##### EXAMPLES

##### :memo: NOTES

> When using terminate, be sure to import Control::Process namespace
<br>

---

<!-- Wait -->

### :paperclip: Wait
<br>

```c++

int Wait();

```
<br>

##### NAMESPACE

<a href="/Version/NAMESPACE.md/#paperclip-process">Control::Process</a>
<br>

##### FULL-DESCRIPTOR


Control::Process::Wait
<br>

##### :scroll: DESCRIPTION

Wait is a control command that waites 
<br>

##### :warning: REQUIREMENTS

Wait requires v1.0.0 or above
<br>

##### AVAILABLE FROM

version > v1.0.0
<br>

##### :leftwards_arrow_with_hook: RETURNS
 
- **int result** 
<br>

##### :no_entry: EXCEPTIONS

- **PermissionDeinedException**:
<br>

##### :x: ERRORS
<br>

##### :star: EXAMPLES
<br>

##### :memo: NOTES

> When using wait, be sure to import Control::Process namespace
<br>

---


<!-- How To-->

## How To

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

In this section we explain **How To** perform certain **tasks that involve APIs**. In particular there is explained:

- <a href="#how-to-integrate-apis">How To Integrate APIs</a> helps a Developer on how to integrate [PROJECT_NAME] APIs into new products.
- <a href="#how-to-develop-apis">How To Develop APIs</a> helps a Developer on how to develop new [PROJECT_NAME] APIs.

<br>

<!-- How To Integrate APIs-->

### How To Integrate APIs

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)


<br>

<!-- How To Develop APIs-->

### How To Develop APIs

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

<br>

---

<!-- FAQ -->

## FAQ

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)


* Empty


<!-- Contact us  -->

## Contact us

[ToC](#notebook_with_decorative_cover-table-of-contents)

For any question or help request on [PROJECT_NAME] *Versions*, *Release Policy*, *Features*, *Changes*, *Namespaces*, *APIs*, *Bugs* or *Fixes* please contact us using our [Contacts](/CONTACT_US.md). 


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

[ToC](#notebook_with_decorative_cover-table-of-contents)

Consult the official <a href="https://www.semver.org" target="_blank">SemVer guide</a> for a complete guide on SemVer.



