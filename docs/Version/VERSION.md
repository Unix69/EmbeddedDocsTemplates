<div align="center">

  <img src="/logo/logo.svg" alt="logo" width="48" height="48" />
  <h1>
    Version
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
      <a href="/Version/RELEASE_POLICY.md">Release Policy</a>
      <span> · </span>
      <a href="/Version/FEATURE.md">Features</a>
      <span> · </span>
      <a href="/Version/CHANGELOG.md">Change Log</a>
      <span> · </span>
      <a href="/Version/NAMESPACE.md">Namespace</a>
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

- [Version](#version)
- [Version Compatibility](#version-compatibility)
- [Version Lifecycle](#version-lifecycle)
  - [Pre-release](#version-pre-release)
    - [Beta Version](#beta-version)
    - [Alpha Version](#alpha-version)
  - [Release](#release)
- [Versions](#versions)
- [Deprecation](#deprecation)
- [Obsolescence](#obsolescence)
- [Bugs](#bugs)
- [Fixes](#fixes)
- [Release Policy](#release-policy)
- [Features](#features)
- [Change Log](#change-log)
- [Namespace](#namespace)
- [API](#api)
- [FAQ](#faq)
- [Contact us](#contact-us)
- [See Also](#see-also)
- [Official Links](#official-links)
  
<!-- Version -->

## Version

[ToC](#notebook_with_decorative_cover-table-of-contents)

A **[PROJECT_NAME]** version identifies a release of [PROJECT_NAME] that provides a set of *Features*. It implements some *APIs* and *Namespaces* and it is subjected to some *Changes*. Furthermore every [PROJECT_NAME] version can contain
*Bugs* that will be resolved by *Fixes*.
Each release of [PROJECT_NAME] follows a given life-cycle that is defined in the **Version Lifecycle** section below. 
A version is built with a given set of metadata (such as encryption keys, encodings) and can be a pre-release version (alpha or beta version).

<br>

[PROJECT_NAME] versions are collected into the **Versions** section of this document and each of them is characterized by some attributes, that globally define the version itself. This attributes are listed into the table below.


| Version Atrribute | Version Atrribute Description | Version Atrribute Value | 
| ----------------- | ----------------------------- | ----------------------- |
| **Version ID - VID** | a unique id **identifing a version** | an alphanumeric string |
| **Version Description** | a fully detailed **description of the version** | an alphanumeric text |
| **Version Release Date** | the date **when version was released** | a datetime string in the form DD/MM/YYYY:T:HH:MM:SS-GMT+Z |
| **Features IDs** | list of unique ids **identifing the Features** implementing this version | a set of alphanumeric strings | 
| **Change IDs** | list of unique ids **identifing the Changes** related to this version | a set of alphanumeric strings |
| **Namespace IDs** | list of unique ids **identifing the Namespaces** related to this version | a set of alphanumeric strings |
| **API IDs** | list of unique ids **identifing the APIs** implementing this version | a set of alphanumeric strings |
| **Bug IDs** | list of unique ids **identifing the Bugs** found on this version | a set of alphanumeric strings |
| **Fix IDs** | list of unique ids **identifing the Fixes** performed on this version | a set of alphanumeric strings |
| **Deprecated From** | the date **when version is considered deprecated** | a datetime string in the form DD/MM/YYYY:T:HH:MM:SS-GMT+Z |
| **Obsolete From** | the date **when version is considered obsolete** | a datetime string in the form DD/MM/YYYY:T:HH:MM:SS-GMT+Z |


Every version of **[PROJECT_NAME]** will be registered, as shown in the above table, into the <a href="#version-history">Version History</a>

<hr>
<br>

<!-- Version Lifecycle -->

## Version Lifecycle

[ToC](#notebook_with_decorative_cover-table-of-contents)

Every release of **[PROJECT_NAME]** follows a standard lifecyle that is identified by the following phases:

- **Pre-Release**: release is unstable and it is not completely ready to be used, some changes should be done or maybe some bugs occur so fixes should be performed. 
  - **Beta**: release is completely unstable and features are not complete and correctly implemented, some important changes should be done or maybe some bugs occur so fixes should be performed.
  - **Alpha**: release is stable and all features are complete and correctly implemented, maybe some bugs occur and fixes should be performed.
- **Release**: release is stable and and all features are complete and correctly implemented, no official bugs occur.
- **Obsolete** release is still supported but will be abbandoned at the next version.
- **Deprecated** release is not anymore supported and became unstable.


<!-- Pre-Release -->

### Pre-Release

[ToC](#notebook_with_decorative_cover-table-of-contents)

In this version the release **can be completely unstable** (Beta version) or **partially stable** with bugs (Alpha version).
Some changes and fixes should be performed on this version.

<!-- Beta-Version -->

#### Beta-Version

[ToC](#notebook_with_decorative_cover-table-of-contents)

In this version the **release is completely unstable**, **features are not completely and not correctly implemented**, some important changes should be done or maybe some bugs occur so fixes should be performed.

<!-- Alpha-Version -->

#### Alpha-Version

[ToC](#notebook_with_decorative_cover-table-of-contents)

In this version the **release is stable** and **features are completely and correctly implemented**, maybe some bugs occur so fixes should be performed.

<!-- Release -->

### Release

[ToC](#notebook_with_decorative_cover-table-of-contents)

In this version the **release is stable** and **features are completely and correctly implemented**, **no official bugs** occur.


<!-- Deprecated -->

### Deprecated

[ToC](#notebook_with_decorative_cover-table-of-contents)

In this version the **release is still supported** by [PROJECT_NAME] but will be abbandoned at the next version.


<!-- Obsolete -->

### Obsolete

[ToC](#notebook_with_decorative_cover-table-of-contents)

In this version the **release is not anymore supported** by [PROJECT_NAME] and became unsable.


<hr>
<br>

<!-- Versions -->

## Versions

[ToC](#notebook_with_decorative_cover-table-of-contents)

| Version ID - VID | Version Description | Version Release Date | Features IDs | Change IDs | Namespace IDs | API IDs | Bug IDs | Fix IDs | Deprecated From | Obsolete From |
| ---------------- | ------------------- | -------------------- | ------------ | ---------- | ------------- | ------- | --------| ------- | --------------- | ------------- |
| 1.0.0 | This version contains the basic application | 14/05/2024 | F1,F2,F3 |  | N1, N2, N3 | API1, API2 | | | 14/06/2024 | 14/05/2025 |
| 2.0.0 | This version contains the enhanced application | 14/06/2024 | F1, F2, F3, F5 |  | N1, N2, N3, N4 | API1, API2, API3, API4 | B1 | FX1 | | |


<hr>
<br>

<!-- Deprecation -->

## Deprecation

[ToC](#notebook_with_decorative_cover-table-of-contents)

A version is deprecated when it is still supported by  **[PROJECT_NAME]** but will be abbandoned at the next version.
To know if a [PROJECT_NAME] version is deprecated, see the <a href="#versions">Versions</a> section and verify if `Deprecated From` date is defined. If `Deprecated From` date of a version is defined, it is considered deprecated
from date `Deprecated From`.

<!-- Obsolescence -->

## Obsolescence

[ToC](#notebook_with_decorative_cover-table-of-contents)

A version is obsolete when it is not anymore supported by [PROJECT_NAME] and became unsable.
To know if a [PROJECT_NAME] version is obsolete, see the <a href="#versions">Versions</a> section and verify if `Obsolete From` date is defined. If `Obsolete From` of a version is defined, it is considered obsolete from date 
`Obsolete From`.

<!-- Bugs -->

## Bugs

[ToC](#notebook_with_decorative_cover-table-of-contents)

When a **Bug** occur the release, and **all lower releases** using the bugged feature, **are unstable** and a fix is needed.
Bugs are registered into <a href="/Version/BUGS.md">Bug Tracer</a>. Have a look to be updated on last discovered <a href="/Version/BUGS.md">Bugs</a>.
 
<!-- Fixes -->

## Fixes

[ToC](#notebook_with_decorative_cover-table-of-contents)

When a **Fix** is performed the **release is stable** and the bug is fixed. Version changes because it includes a **Patch** that fixes the occurred bug.
Fixes are registered into <a href="/Version/BUGS.md">Fix Tracer</a>. Have a look to be updated on last released <a href="/Version/FIX.md">Fixes</a>


<!-- Release Policy -->

## Release Policy 

[ToC](#notebook_with_decorative_cover-table-of-contents)

Be conscious about <a href="/Version/RELEASE_POLICY.md">Release Policy</a> of [PROJECT_NAME] to know which rules each [PROJECT_NAME] **Release** respects and how it is encoded in the *Version IDentifier*.

<!-- Features -->

## Features

[ToC](#notebook_with_decorative_cover-table-of-contents)

See the complete <a href="/Version/FEATURE.md">Feature List</a> of [PROJECT_NAME] to be aware of [PROJECT_NAME]'s capabilities and potential.

<!-- Change Log -->

## Change Log

[ToC](#notebook_with_decorative_cover-table-of-contents)

Follow the <a href="/Version/CHANGELOG.md">Change Log</a> of [PROJECT_NAME] to be updated on any [PROJECT_NAME] **Changes**.

<!-- Namespace -->

## Namespace

[ToC](#notebook_with_decorative_cover-table-of-contents)

See the <a href="/Version/API.md">Namespace</a> of [PROJECT_NAME] to know details about how APIs are organized into [PROJECT_NAME] **Namespaces** and to how interact with them.

<!-- API -->

## API

[ToC](#notebook_with_decorative_cover-table-of-contents)

See the complete <a href="/Version/API.md">API Reference</a> of [PROJECT_NAME] to know details about each [PROJECT_NAME] **API** and how to use it.

<!-- FAQ -->

## FAQ

[ToC](#notebook_with_decorative_cover-table-of-contents)


* Empty


<!-- Contact us  -->

## Contact us

[ToC](#notebook_with_decorative_cover-table-of-contents)

For any question or help request on [PROJECT_NAME] *Versions*, *Release Policy*, *Features*, *Changes*, *Namespaces*, *APIs*, *Bugs* or *Fixes* please contact us using our [Contacts](/CONTACT_US.md). 

<!-- See Also -->

## See Also

[ToC](#notebook_with_decorative_cover-table-of-contents)

The following documents are related to this:

* The [Release Policy](/RELEASE_POLICY.md) file, named `RELEASE_POLICY.md`, contains the release policy standard adopted in **[PROJECT_NAME]**.
* The [Features](/FEATURE.md) file, named `FEATURE.md`, contains the features of **[PROJECT_NAME]**, labeled 
* The [Change Log](/CHANGELOG.md) file, named `CHANGELOG.md`, contains the changes made on **[PROJECT_NAME]**
* The [Namespace](/NAMESPACE.md) file, named `NAMESPACE.md`, contains the namespace architecture of **[PROJECT_NAME]**
* The [APIs](/API.md) file, named `API.md`, contains list of APIs **[PROJECT_NAME]**
* The [Bugs](/BUG.md) file, named `BUG.md`, contains the bug made on **[PROJECT_NAME]**
* The [Fixes](/FIX.md) file, named `FIX.md`, contains the fixes made on **[PROJECT_NAME]** 


<!-- Official Links -->

## Official Links

[ToC](#notebook_with_decorative_cover-table-of-contents)

Consult the official <a href="https://www.semver.org" target="_blank">SemVer guide</a> for a complete guide on SemVer.


