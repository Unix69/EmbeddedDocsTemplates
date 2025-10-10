<div align="center">

  <img src="/logo/logo.svg" alt="logo" width="48" height="48" />
  <h1>
    Bugs
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
      <a href="/Version/API.md">API</a>
      <span> · </span>
      <a href="/Version/FIX.md">Fixes</a>
  </h4>

</div>

<br/>

<!-- Table of Contents -->

# :notebook_with_decorative_cover: Table of Contents

Navigation index to fast explore the content:

- [Bug Tracer](#bug-tracer)
- [FAQ](#faq)
- [Contact us](#contact-us)
- [See Also](#see-also)
- [Official Links](#official-links)


### Definition

A **Bug** in **[PROJECT_NAME]** is a design or implementation defect occurred on some **Versions**, **Features**, **Namespaces** and **APIs** of [PROJECT_NAME] that **needs to be solved by some Fixes**.

### Modification

A Bug **will be fixed by** some **Fixes**, performed during the [PROJECT_NAME] lifecycle.

### Indexing

To **keep trace** of occurred Bugs a **Bug Tracer is used**. Each **Bug** present in the Bug Tracer **is identified by some Attributes**, that globally define the Bug itself. 
This Attributes are listed into the table below.  

| Bug Atrribute | Bug Atrribute Description | Bug Atrribute Value | 
| ------------- | ------------------------- | ------------------- |
| **Bug ID - BID** | a unique id **identifing a bug** | an alphanumeric string |
| **Bug Description** | a fully detailed **description of the bug** | an alphanumeric text |
| **Bug Level** | the **level of the occurred bug** | the possible bug levels are: <ul><li>`HW` Hardware Level</li><li>`SYS` System Level</li><li>`APP` Application Level</li></ul> |
| **Bug Type** | the **type of the occured bug** | the possible bug types are: <ul><li>`NET` Network Bug</li><li>`STORE` Storage Bug</li><li>`PROC` Processing Bug</li></ul> |
| **Discovery Date** | the **date when bug has been discovered** | a datetime string in the form DD/MM/YYYY:T:HH:MM:SS-GMT+Z |
| **Fixing Date** | the **date when bug has been fixed** | a datetime string in the form DD/MM/YYYY:T:HH:MM:SS-GMT+Z |
| **Affected Version** | list of unique ids **identifing the Versions** affected by this bug | a set of alphanumeric strings | 
| **Affected Features** | list of unique ids **identifing the Features** affected by this bug | a set of alphanumeric strings | 
| **Applied Change** | list of unique ids **identifing the Changes** made to solve this bug | a set of alphanumeric strings |
| **Affected Namespaces** | list of unique ids **identifing the Namespaces** affected by this bug | a set of alphanumeric strings |
| **Affected APIs** | list of unique ids **identifing the APIs** affected by this bug | a set of alphanumeric strings |
| **Performed Fixes** | list of unique ids **identifing the Fixes** made to resolve this bug | a set of alphanumeric strings |

Every bug discovered on **[PROJECT_NAME]** will be registered, as shown in the above table, into the <a href="#bug-tracer>Bug Tracer</a>

<!-- Bug Tracer-->

## Bug Tracer

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

| Bug ID | Bug Description | Bug Level | Bug Type | Discovery Date | Fixing Date | Affected Versions | Affected Features | Applied Changes | Affected Namespaces | Affected APIs | Performed Fixes |
| ------ | --------------- | --------- | -------- | -------------- | ----------- | ----------------- | ----------------- | --------------- | ------------------- | ------------- | --------------- |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |


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
* The [APIs](/API.md) file, named `API.md`, contains list of APIs **[PROJECT_NAME]**
* The [Fixes](/FIX.md) file, named `FIX.md`, contains the fixes made on **[PROJECT_NAME]**


<!-- Official Links -->

## Official Links

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

Consult the official <a href="https://www.semver.org" target="_blank">SemVer guide</a> for a complete guide on SemVer
