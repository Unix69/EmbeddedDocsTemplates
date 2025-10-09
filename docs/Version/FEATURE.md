<div align="center">

  <img src="/logo/logo.svg" alt="logo" width="48" height="48" />
  <h1>
    Features
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

- [Feature Index](#feature-index)
- [Feature Reference](#feature-reference)
- [How To](#how-to)
  - [How To Use Features](#how-to-use-features)
  - [How To Develop Features](#how-to-develop-features)
- [About New Features](#about-new-features)
- [About Next Features](#about-next-features)
- [FAQ](#faq)
- [Contact us](#contact-us)
- [See Also](#see-also)
- [Official Links](#official-links)

## Features

In [PROJECT_NAME] a **Feature is a functionality**, related to a given [PROJECT_NAME] version, that **permits to perform some tasks**.
Every Feature can be **used by a specific Actor** and only **when it assumes a given Role**.
A [PROJECT_NAME] **Feature is related to some Namespaces which define a set of API**, designed to control the feature and to perform tasks with it.

### Modification

A feature **will be modified by** some **Changes**, during [PROJECT_NAME] lifecycle.
Furthermore every [PROJECT_NAME] **feature can contain Bugs** that will be **resolved by Fixes**.

### Indexing

To **keep trace** of Features a **Feature Index is used**. Each **Feature** present in the Index **is identified by some Attributes**, that globally define the Feature itself. 
This Attributes are listed into the table below. 

| Feature Atrribute | Feature Atrribute Description | Feature Atrribute Value | 
| --------- | --------------------- | --------------- |
| **Feature ID - FID** | a unique id **identifing a feature** | an alphanumeric string |
| **Version IDs** | list of unique ids **identifing the Versions** implementing this feature | a set of alphanumeric strings | 
| **Change IDs** | list of unique ids **identifing the Changes** related to this feature | a set of alphanumeric strings |
| **Namespace IDs** | list of unique ids **identifing the Namespaces** related to this feature | a set of alphanumeric strings |
| **API IDs** | list of unique ids **identifing the APIs** implementing this feature | a set of alphanumeric strings |
| **Bug IDs** | list of unique ids **identifing the Bugs** found on this feature | a set of alphanumeric strings |
| **Fix IDs** | list of unique ids **identifing the Fixes** performed on this feature | a set of alphanumeric strings |
| **Actor IDs** | list of unique ids **identifing the Actors** that can use this feature | a set of alphanumeric strings |
| **Role IDs** | list of unique ids **identifing the Roles** needed by the actor to use this feature | a set of alphanumeric strings |

<!-- Feature List-->

## Feature Index

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

| Feature ID | Feature Description | Version IDs | Change IDs | Namespace IDs | API IDs | Bug IDs | Fix IDs | Actor IDs | Role IDs |
| ---------- | ------------------- | ----------- | ---------- | ------------- | ------- | ------- | ------- | --------- | -------- |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |

For a complete description of each Features and its usage, follow the <a href="#feature-reference">Feature Reference</a>.

<br>

<!-- Feature Reference-->

## Feature Reference

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

Here you have the complete description of each Feature including requirements, permissions and usage examples. Lets start to see each feature in detail.

<!-- Feature 0-->

## :star: Feature 0

This feature permit to...

#### :pill: Usage Examples

Here there are some examples that shows you how to perform certain tasks with this feature

<br>

#### State

- **Obsolete** from version *v1.0.0*
- **Deprecated** from version *v2.0.0* :x:


#### :warning: Requirements

To use this feature it is required to:

* Requirement 0
* Requirement 1
* Requirement 2


#### Actors and Roles

By beeing this actors it is possible to use this feature:

| :boy:Actor |
| ---------- | 
| **<a href="/Implementation/ACTOR.md/#client">Client</a>** |
| **<a href="/Implementation/ACTOR.md/#service">Service</a>** | 
| **<a href="/Implementation/ACTOR.md/#system">System</a>** |


By assuming this roles an actor can use this feature:

| :shirt:Role |
| ----------- | 
| **<a href="/Implementation/ROLE.md/#administrator">Administrator</a>** |
| **<a href="/Implementation/ROLE.md/#user">User</a>** | 
| **<a href="/Implementation/ROLE.md/#developer">Developer</a>** |

#### Namespaces and APIs

This namespaces and APIs are used to implement this feature:

| :paperclip:Namespaces | Full Name | Brief Description |
| ---------- | --------- | ----------------- | 
| ***<a href="/Version/NAMESPACE.md/#control">Control</a>*** | *Control*  | contains all control API implementing feature control |
| ***<a href="/Version/NAMESPACE.md/#command">Command</a>*** | *Control::Command* | contains al command API implementing feature commands |
| ***<a href="/Version/NAMESPACE.md/#process">Process</a>*** | *Control::Process* | contains al process API implementing feature processes |


| :paperclip:API | Full Name | Brief Description |
| --- | --------- | ----------------- | 
| ***<a href="/Version/API.md/#configure">configure</a>*** | *Control::configure*  | **configure** permits to configure the control layer of [PROJECT_NAME] feature |
| ***<a href="/Version/API.md/#setup">setup</a>*** | *Control::setup* | **setup** permits to setup the control layer of [PROJECT_NAME] feature |
| ***<a href="/Version/API.md/#exit">exit</a>*** | *Control::exit* | **exit** permits to terminate the control process of [PROJECT_NAME] feature |



<!-- Feature 1  -->

## :star: Feature 1

This feature permit to...

#### :pill: Usage Examples

Here there are some examples that shows you how to perform certain tasks with this feature

<br>

#### State

- **Obsolete** from version *v1.0.0*
- **Deprecated** from version *v2.0.0* :x:


#### :warning: Requirements

To use this feature it is required to:

* Requirement 0
* Requirement 1
* Requirement 2


#### Actors and Roles

By beeing this actors it is possible to use this feature:

| :boy:Actor |
| ---------- | 
| **<a href="/Implementation/ACTOR.md/#client">Client</a>** |
| **<a href="/Implementation/ACTOR.md/#service">Service</a>** | 
| **<a href="/Implementation/ACTOR.md/#system">System</a>** |


By assuming this roles an actor can use this feature:

| :shirt:Role |
| ----------- | 
| **<a href="/Implementation/ROLE.md/#administrator">Administrator</a>** |
| **<a href="/Implementation/ROLE.md/#user">User</a>** | 
| **<a href="/Implementation/ROLE.md/#developer">Developer</a>** |

#### Namespaces and APIs

This namespaces and APIs are used to implement this feature:

| :paperclip:Namespaces | Full Name | Brief Description |
| ---------- | --------- | ----------------- | 
| ***<a href="/Version/NAMESPACE.md/#control">Control</a>*** | *Control*  | contains all control API implementing feature control |
| ***<a href="/Version/NAMESPACE.md/#command">Command</a>*** | *Control::Command* | contains al command API implementing feature commands |
| ***<a href="/Version/NAMESPACE.md/#process">Process</a>*** | *Control::Process* | contains al process API implementing feature processes |


| :paperclip:API | Full Name | Brief Description |
| --- | --------- | ----------------- | 
| ***<a href="/Version/API.md/#configure">configure</a>*** | *Control::configure*  | **configure** permits to configure the control layer of [PROJECT_NAME] feature |
| ***<a href="/Version/API.md/#setup">setup</a>*** | *Control::setup* | **setup** permits to setup the control layer of [PROJECT_NAME] feature |
| ***<a href="/Version/API.md/#exit">exit</a>*** | *Control::exit* | **exit** permits to terminate the control process of [PROJECT_NAME] feature |




<!-- Feature 2 -->

## :star: Feature 2

This feature permit to...

#### :pill: Usage Examples

Here there are some examples that shows you how to perform certain tasks with this feature

<br>

#### State

- **Obsolete** from version *v1.0.0*
- **Deprecated** from version *v2.0.0* :x:


#### :warning: Requirements

To use this feature it is required to:

* Requirement 0
* Requirement 1
* Requirement 2


#### Actors and Roles

By beeing this actors it is possible to use this feature:

| :boy:Actor |
| ---------- | 
| **<a href="/Implementation/ACTOR.md/#client">Client</a>** |
| **<a href="/Implementation/ACTOR.md/#service">Service</a>** | 
| **<a href="/Implementation/ACTOR.md/#system">System</a>** |


By assuming this roles an actor can use this feature:

| :shirt:Role |
| ----------- | 
| **<a href="/Implementation/ROLE.md/#administrator">Administrator</a>** |
| **<a href="/Implementation/ROLE.md/#user">User</a>** | 
| **<a href="/Implementation/ROLE.md/#developer">Developer</a>** |

#### Namespaces and APIs

This namespaces and APIs are used to implement this feature:

| :paperclip:Namespaces | Full Name | Brief Description |
| ---------- | --------- | ----------------- | 
| ***<a href="/Version/NAMESPACE.md/#control">Control</a>*** | *Control*  | contains all control API implementing feature control |
| ***<a href="/Version/NAMESPACE.md/#command">Command</a>*** | *Control::Command* | contains al command API implementing feature commands |
| ***<a href="/Version/NAMESPACE.md/#process">Process</a>*** | *Control::Process* | contains al process API implementing feature processes |


| :paperclip:API | Full Name | Brief Description |
| --- | --------- | ----------------- | 
| ***<a href="/Version/API.md/#configure">configure</a>*** | *Control::configure*  | **configure** permits to configure the control layer of [PROJECT_NAME] feature |
| ***<a href="/Version/API.md/#setup">setup</a>*** | *Control::setup* | **setup** permits to setup the control layer of [PROJECT_NAME] feature |
| ***<a href="/Version/API.md/#exit">exit</a>*** | *Control::exit* | **exit** permits to terminate the control process of [PROJECT_NAME] feature |


<br>

<!-- How To-->

## How To

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)


<!-- How To Use Features-->

### How To Use Features

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)


<!-- How To Develop Features-->

### How To Develop Features

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)



<!-- About New Features -->

## About New Features

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

This features are introduced in the new version:

* Feature 3
* Feature 4
* Feature 5


<!-- About Next Features-->

## About Next Features

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

The next features that will be introduced in the next version are:

* Feature 6
* Feature 7
* Feature 8


<!-- FAQ -->

## FAQ

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)


* Empty


<!-- Contact us  -->

## Contact us

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

For any question or help request on **[PROJECT_NAME]'s** versioning system or release policy please contact us using our [Contacts](/CONTACT_US.md




<!-- See Also -->

## See Also

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

The following documents are related to this:

* The [Version](/VERSION.md) file, named `VERSION.md`, contains the version history of **[PROJECT_NAME]**
* The [Release Policy](/RELEASE_POLICY.md) file, named `RELEASE_POLICY.md`, contains the release policy standard adopted in **[PROJECT_NAME]**.
* The [Change Log](/CHANGELOG.md) file, named `CHANGELOG.md`, contains the changes made on **[PROJECT_NAME]**
* The [Namespace](/NAMESPACE.md) file, named `NAMESPACE.md`, contains the namespace architecture of **[PROJECT_NAME]**
* The [APIs](/API.md) file, named `API.md`, contains list of APIs **[PROJECT_NAME]**
* The [Fixes](/FIX.md) file, named `FIX.md`, contains the fixes made on **[PROJECT_NAME]**


<!-- Official Links -->

## Official Links

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

Consult the official <a href="https://www.semver.org" target="_blank">SemVer guide</a> for a complete guide on SemVer

