<div align="center">

  <img src="/logo/logo.svg" alt="logo" width="48" height="48" />
  <h1>[PROJECT_NAME]</h1>
  
  <br>
  <br>
  
  <p>
    An awesome README to navigate and use the project in an easy way.  
  </p>
  
<!-- Badges -->

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

<br>
<br>

:building_construction: **<a href="/PROJECT.md">Project</a>**
<span> · </span>
⭐ **<a href="/Version/FEATURE.md">Feature</a>**
<span> · </span>
:video_game: **<a href="/Usage/USECASES.md">Usage</a>**
<span> · </span>
🏷️ **<a href="/Version/Version.md">Versions</a>**
<span> · </span>
📦 **<a href="/Version/NAMESPACE.md">Namespaces</a>**
<span> · </span>
🧩  **<a href="/Version/API.md">APIs</a>**
<span> · </span>
🐞 **<a href="/Version/BUG.md">Bugs</a>**
<span> · </span>
🔧 **<a href="/Version/FIX.md">Fixes</a>**

</div>



<br/>

# 📓 Table of Contents

- [Project](#project)
- [Usage & Actors](#usage--actors)
- [Version & Features](#versions--features)
- [Getting Started](#getting-started)
- [APIs & Namespaces](#apis--namespaces)
- [Bug & Fix Tracking](#bug--fix-tracking)
- [Official Guides](#official-guides)
- [How To](#how-to)
- [License](#license)
- [Contributing](#contributing)
  - [Code Of Conduct](#code-of-conduct)
  - [Fork Project](#fork-project)
  - [Pull Request](#pull-request)
  - [Issue](#issue)
- [FAQ](#faq)
- [Authors](#authors)
- [Contact](#contact-us)
- [Acknowledgements](#acknowledgements)


<br>
<br>

<br>
<br>



<div align="center">
  <a href="screenshots/project.png" target="_blank">
    <img src="screenshots/project.png" alt="Project" height="360px" width="360px" />
  </a>
</div>

<br>
<br>

**[PROJECT_NAME]** is a modular, scalable, and AI-ready software architecture designed to demonstrate... *(short summary here)*

<br>
<br>


---

# Project 🎯 

<br>
<br>

- 📜 **[PROJECT.md](PROJECT.md)** – Project file

  - :checkered_flag: [Goal](./PROJECT.md#goal) 
  - 🚀 [Architecture](./PROJECT.md#architecture)
  - 💻 [Tech Stack](./PROJECT.md#tech-stack)
  - :file_folder: [Directory Tree](./PROJECT.md#directory-tree)

<br>
<br>

# Usage & Actors 🎮 

The **usage model** defines *who* interacts with the system (**Actors**), *how* they act (**Roles**), and *what* they can access (**Features**, **APIs**, **Namespaces**).

- [Actors](./Usage/ACTORS.md) - **define** and **shows** the possibile **actors** and their *available* **features**, **API's** and **namespaces**.
- [Roles](./Usage/ROLES.md) - **define** and **shows** the **available rolse** for each **actor** and their *accessable* **feature**, **API** and **namespace**.
- [Use Cases](./Usage/USECASES.md) - **list** and **shows** all possible **use cases**, considering partecipating all **actors**, their assumed **role** and their used **features**, **APIs** and **namespaces**.

| 👤 Actor | 👥 Role(s) | 📦 APIs / Namespaces | ⭐ Features |
|--------|----------|----------------------------|----------------|
| :desktop_computer: **System** | Administrator  | All internal APIs | Core, Monitoring |
| :technologist: **Developer** | Developer | `/dev/*`, `/core/*` | Integration, Build |
| 👤 **User** | User | `/public/*`, `/data/*` | Consumption, Query |

🔒 Access is **role-based**: unauthorized 👥 roles are automatically denied API or Feature access ❌.

<br>

---

<br>


# Versions & Features 🏷️

Each **Version** defines supported **Features**, **APIs**, and **Namespaces**.
Tracking these ensures safe updates and backward compatibility.

* 👉 Both ***Features*** and ***Versions*** follow the 📜 ***[Release Policy](/Version/RELEASE_POLICY.md)***.
* 🔐 Access to ***Features*** is **role-based**: unauthorized roles are automatically **denied** feature access ❌.

<br>

## 🏷️ Available versions

| 🏷️ Version | Status      | ⭐ Features  | 🧩 APIs      | 📦 Namespaces  | 🔄 Major Changes |
| -------- | ----------- | --------- | --------- |------------ | ------------- |
| `v1.0.0` | Stable      | <ul> <li>`F-1`</li> <li>`F-2`</li> </ul> | <ul> <li>`API-1`</li> <li>`API-2`</li> </ul> | `N-1` | Initial release |
| `v1.1.0` | Released    | <ul> <li>`F-1`</li> <li>`F-2`</li> </ul> | <ul> <li>`API-1`</li> <li>`API-2`</li> </ul> | `N-1` | Added core namespaces   |
| `v1.2.0` | Pre-release | <ul> <li>`F-1`</li> <li>`F-2`</li> </ul> | <ul> <li>`API-1`</li> <li>`API-2`</li> </ul> | `N-1` | Introduced AI API layer |

<br>

## ⭐ Available features 

| ⭐ Feature  | Description | 🏷️ Versions | 🧩 APIs | 📦 Namespaces  | 👤 Actors | 👥 Roles | 🔄 Changes |
| -------- | ----------- | ----------- | --------- | ----------- |----------- | ----------- |----------- |
| `F-1` | - | <ul><li>`v1.0.0`</li><li>`v1.1.0`</li></ul> | <ul><li>`API-1`</li> <li>`API-2`</li></ul>  | `N-1` | Actors | Roles  | Initial release |
| `F-2` | - | <ul> <li>`v1.0.0`</li> <li>`v1.1.0`</li> </ul>    |  <ul> <li>`API-1`</li> <li>`API-2`</li></ul> | `N-1` | Actors | Roles  | Added core namespaces   |

<br>
<br>

🔗 References:

* [VERSION.md](/Version/VERSION.md) - **list** and **shows** the **available verions** and their features, API's and namespaces.
* [FEATURE.md](/Version/FEATURE.md) **list** and **shows** all **available features**. 
* [RELEASE_POLICY.md](/Version/RELEASE_POLICY.md) **shows** the followed **relase policy** of each version, feature, API and namespace, and **shows and explains** the applied **policy rules**.
* [CHANGE_LOG.md](/Version/CHANGE_LOG.md.md) **list** all **changes related to** available versions, features, API's and namespaces

<br>

---

<br>


# Getting Started 🚀

Let's start to keep in touch with **[PROJECT_NAME]**.

- **Step 1 - Verify Prerequisites and Dependencies**
	
[PROJECT_NAME] needs to run on **hosts** equipped with specific **hardware** and **software**.
So read carefully the **prerequisites** to respect and the **dependencies** satisify.

- **Step 2 - Get and Install**
- **Step 3 - Build**
- **Step 4 - Setup and Configure**
- **Step 5 - Test and Verify** 
- **Step 6 - Run**
- **Step 7 - Deploy**
- **Step 8 - Uninstall**


<br>
<br>

## 💻 Prerequisites

List of software or packages required

<br>

## 📦 Dependencies

Dependencies required for running the project

<br>

## ⭐ Installation

To ***install*** the project follow this setps:

1) Run the `install.sh` script contained into the current directory
	<pre> sudo ./install.sh </pre>

<br>

## ⚙️ Configuration

To ***configure*** the project follow this setps:

<br>

1) Run the `config.sh` script contained into the current directory
	<pre> sudo ./config.sh </pre>
2) ...

<br>

## ✅ Tests

To ***test*** the project follow this setps:

<br>

1) Run the `test.sh` script contained into the current directory
	<pre> sudo ./test.sh </pre>
2) ...

<br>

## 🚀 Run

To ***run*** the project follow this setps:

<br>

1) Run the `start.sh` script contained into the current directory
	<pre> sudo ./start.sh </pre>


<br>

<br>

## 🛠️ Build

To ***build*** the project follow this setps:

<br>

1) Run the `build.sh` script contained into the current directory
	<pre> sudo ./build.sh </pre>
2) ...

<br>

## 🌍 Deployment

To ***deploy*** the project follow this setps:

<br>

1) ...
2) ...

<br>

## ❌ Uninstall

To ***uninstall*** the project follow this setps:

1) Run the `uninstall.sh` script contained into the current directory
	<pre> sudo ./uninstall.sh </pre>

<br>


<br>

---

<br>


# APIs & Namespaces 🔖


* **APIs** define the interaction surface and helps features to achieve their scope.
* **Namespaces** group APIs logically and control access.
* 👉 Both ***APIs*** and ***Namespaces*** follow the 📜 ***[Release Policy](/Version/RELEASE_POLICY.md)***.


| 📦 Namespace   | 🧩 API | 📜 Description |
| ----------- | ------------------ | --------------------------- |
| `core.auth` | `auth.login()`     | Authentication endpoints    |
| `core.data` | `data.fetch()`     | Data retrieval and storage  |
| `dev.utils` | `build.redeploy()` | Developer tools and helpers |

<br>

## 🧩 APIs

| 🧩 API | ⭐ Features  | 🏷️ Versions  | 📦 Namespaces  | 👤 Actors | 👥 Roles | 🔄 Changes |
| -------- | ----------- | --------- | ----------- |----------- | ----------- |----------- |
| `auth.login()` | `F-1` | <ul><li>`v1.0.0`</li><li>`v1.1.0`</li><li>`v1.2.0`</li></ul>  | `core.auth` | Actors | Roles  | Initial release |
|  `data.fetch()`  | `F-2` | <ul> <li>`v1.0.0`</li> <li>`v1.1.0`</li> <li>`v1.2.0`</li></ul>    |  <ul> <li>`API-1`</li> <li>`API-2`</li></ul> | `core.data` | Actors | Roles  | Added core namespaces |

<br>

## 📦 Namespaces

| 📦 Namespaces | 🏷️ Versions    | 🔖 APIs     | ⭐ Features  | 👤 Actors | 👥 Roles | 🔄 Changes |
| ------ | ----------- | --------- | ----------- |----------- | ----------- |----------- |
| `core.auth` | <ul><li>`v1.0.0`</li><li>`v1.1.0`</li><li>`v1.2.0`</li></ul> | <ul><li>`auth.login()`</li> <li>`data.fetch()`</li></ul>  | `F-1` | Actors | Roles  | Initial release |
| `core.data` | <ul> <li>`v1.0.0`</li> <li>`v1.1.0`</li> <li>`v1.2.0`</li></ul>    |  <ul><li>`auth.login()`</li> <li>`data.fetch()`</li></ul> | `F-1` | Actors | Roles  | Added core namespaces |

<br>

🔗 References:

* [API Reference](./Version/API.md) 🔖
* [Namespace Reference](./Version/NAMESPACE.md) 📦

<br>
<br>

# Bug & Fix Tracking 🔥

All discovered **bugs** and applied **fixes** are documented under `/Version/BUG.md` and `/Version/FIX.md` and its traced on the `/Version/CHANGELOG.md`.

| Type   | ID     | Affects               | Description              |  Discovered/Applied on |  Changes |
| ------ | ------ | --------------------- | ------------------------ | ------ | ------ |
| 🐞 Bug | b=`#122` | v=`v1.2.0`, fs=`data core features` apis=`core.data` ns=`core`| Timeout on large queries | 14/05/2024 at 03:00 am | c=`#1` |
| 🔧 Fix | f=`#123` | v=`v1.2.1`, fs=`data view feature` apis=`view.show.data` ns=`view` | Added pagination | 14/05/2025 at 03:00 am | c=`#2` |

See:

* [BUG.md](./Version/BUG.md)
* [FIX.md](./Version/FIX.md)
* [CHANGELOG.md](./Version/CHANGELOG.md)

<br>
<br>

# Change Log ⚙️  

<br>
<br>

Each ***Change*** apported to **[PROJECT_NAME]** is registered into a log called ***[Change Log](/Version/CHANGE_LOG.md)***. So Read the latest ***[Change Log](/Version/CHANGE_LOG.md)*** to be updated with last changes on [PROJECT_NAME], **before upgrading** or **deploying** it.

<br>

### 🧩 Types of Changes

<br>

There are different ***changes*** that can be applied on [PROJECT_NAME]:

| 🔧 Type | 📝 Description |
|----------|----------------|
| :heavy_plus_sign: `add` | A new component, API, or feature has been introduced. |
| 🛠️ `modify` | An existing element has been improved, refactored, or redesigned. |
| ❌ `delete` | A deprecated element has been safely removed. |
| :wrench: `fix` | A bug or regression has been resolved. |

<br>

### 🧩 Components  

<br>

**Changes** can be applied **to any components**. These are the main changable [PROJECT_NAME] components, that **must be declared** into the **Change Log** in case of any changes:

| 🔧 Component | 📝 Description |
|----------|----------------|
| **API** | the changed API's, if any API is changed |
| **Feature** | the changed Features, if any feature is changed |
| **Namespace** | the changed Namespaces, if any namespace is changed |


<br>

### 📋 Example of Changes

| Change | Fix | Features | Versions | APIs | Namespaces | Description |
|--------|-----|-----------|-----------|------|-------------|--------------|
| `fix` | `#14` | `#101`, `#115` | `v1.2.3` | `auth.validate`, `session.refresh` | `core.auth` | Improved token validation under high concurrency |  


<br>
<br>



# How To 🛠️

<br>

Here you can find all provided **"How To"**:

* <a href="#how-to-fork">How to fork Project</a>
* <a href="#how-to-make-a-pull-request">How to make pull request for Project </a>
* <a href="/Version/NAMESPACE.md#how-to-import-namespaces">How import Namespaces</a>
* <a href="/Version/NAMESPACE.md#how-to-address-apis-through-namespaces">How to address APIs through namespaces</a>
* <a href="/Version/API.md#how-to-develop-apis">How to develop API</a>
* <a href="/Version/API.md#how-to-integrate-apis">How to integrate API</a>
* <a href="/Version/FEATURE.md#how-to-use-features">How to use Features</a>
* <a href="/Version/FEATURE.md#how-to-develop-features">How to develop Features</a>

<br>

---

<br>


# Official Guides 📚

| Type                  | Reference                                               | Description                    |
| --------------------- | ------------------------------------------------------- | ------------------------------ |
| 📘 User Guide         | [USER_GUIDE.md](/Usage/USER_GUIDE.md)                   | End-user operations            |
| 🧑‍💼 Admin Guide     | [ADMINISTRATOR_GUIDE.md](/Usage/ADMINISTRATOR_GUIDE.md) | Configuration & maintenance    |
| 🧑‍💻 Developer Guide | [DEVELOPMENT_GUIDE.md](/Usage/DEVELOPMENT_GUIDE.md)     | API and namespace usage        |


<br>
<br>

# Release Policy 📜

Here you can find the ***Relase Policy*** followed by ***Versions***, ***Features***, ***APIs***, ***Namespaces***:

* [Release Policy](./Version/RELASE_POLICY.md)

<br>
<br>

# Licenses 📜

<br>

[PROJECT_NAME] is distributed under this <a href="/LICENSE.md">License</a>.

<br>

---

<br>


# Contributing 👋

1. <a href="#fork-project">Fork the project</a>  
2. Create your Feature Branch (`git checkout -b feature/Feature`)  
3. Commit your Changes (`git commit -m 'Add some Feature'`)  
4. Push to the Branch (`git push origin feature/Feature`)  
5. Open a <a href="#pull-request">pull request</a>

See [CODE_OF_CONDUCT.md](/CODE_OF_CONDUCT.md).

<br>
<br>

## Fork Project

<br>

### How to fork

1.  
2.  
3.  

<br>
<br>

## Pull Request

<br>

### How to make a pull request

1.  
2.  
3.  

<br>
<br>

## Issue ⚠️

If some ***Issues*** on **[PROJECT_NAME]** occur, the *Actor* can open an issue on GitHub by using the provided <a href="/ISSUE_TEMPLATE.md">issue template</a>, or  <a href="/CONTACT_US.md">contact us</a> directly to signal the issue manually. 

<br>

### Open Issue

To open an issue see <a href="/ISSUE_TEMPLATE.md">Open Issue Template</a> and follow the instructions.

<br>

### Issue Tracer

To see all traced issues see <a href="/ISSUES.md">Issues</a>.


<br>

---

<br>

# See Also

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

The following documents are related to this:

* The [Project](/Project/PROJECT.md) file, named `PROJECT.md`, contains the ***Project Description*** of **[PROJECT_NAME]**
* The [Use Cases](/Usage/USECASES.md) file, named `USECASES.md`, shows the ***Use Cases*** of **[PROJECT_NAME]** 
* The [Actors](/Usage/ACTORS.md) file, named `ACTORS.md`, explains type of ***Actors*** on **[PROJECT_NAME]**
* The [Roles](/Usage/ROLES.md) file, named `ROLES.md`, explains the ***Roles*** of ***Actors*** in **[PROJECT_NAME]**
* The [Administrator Guide](/Usage/ADMINISTRATOR_GUIDE.md) file, named `ADMINISTRATOR_GUIDE.md`, explains ***Administrators*** how to manage **[PROJECT_NAME]**
* The [User Guide](/Usage/USER_GUIDE.md) file, named `USER_GUIDE.md`, explains ***Users*** user how to use **[PROJECT_NAME]**
* The [Developer Guide](/Usage/DEVELOPMENT_GUIDE.md) file, named `DEVELOPMENT_GUIDE.md`, explains ***Developers*** how to develop **[PROJECT_NAME]**
* The [Version](/Version/VERSION.md) file, named `VERSION.md`, shows and explain each **[PROJECT_NAME]** ***Version*** 
* The [Release Policy](/Version/RELEASE_POLICY.md) file, named `RELEASE_POLICY.md`, contains the ***Release Policy*** standard adopted in **[PROJECT_NAME]**.
* The [Features](/Version/FEATURE.md) file, named `FEATURE.md`, contains the ***Features*** of **[PROJECT_NAME]**
* The [APIs](/Version/API.md) file, named `API.md`, contains the ***APIs*** of **[PROJECT_NAME]** 
* The [Change Log](/Version/CHANGELOG.md) file, named `CHANGELOG.md`, contains the ***Changes*** made on **[PROJECT_NAME]**
* The [Namespace](/Version/NAMESPACE.md) file, named `NAMESPACE.md`, contains the ***Namespace*** architecture of **[PROJECT_NAME]**
* The [Bugs](/Version/BUG.md) file, named `BUG.md`, contains the ***Bug*** exposed on **[PROJECT_NAME]**
* The [Fixes](/Version/FIX.md) file, named `FIX.md`, contains the ***Fixes*** made on **[PROJECT_NAME]**

<br>

---

<br>

# FAQ ❓

Here you can find the Frequently Asked Questions and Answers.

<br>
<br>

# Contact us ☎️

For **more information** on [PROJECT_NAME] <a href="/CONTACT_US.md">contact us</a>.

<br>
<br>

# Authors 🧑‍💻

Here you can find **all authors** of [PROJECT_NAME] and **their info**:

* | Author | Name | Contributions | Roles | Email | Telephone | 
  |--------|------|---------------|-------|-------|------------|
  | [<img src="https://avatars.githubusercontent.com/u/111588387?v=4" width="100px;"/><br/><sub><b>Unix69</b></sub>](https://github.com/Unix69) | Giuseppe Pedone | `FI`, `OP`, `DE` | `FO` and `CEO` | <a href="giuseppe.pedone.developer@gmail.com">giuseppe.pedone.developer@gmail.com</a> | +3711963527 |
  | [<img src="https://avatars.githubusercontent.com/u/111588387?v=4" width="100px;"/><br/><sub><b>Unix69</b></sub>](https://github.com/Unix69) | Giuseppe Pedone | `OP`, `DE` | `CTO` and `TEC` | <a href="giuseppe.pedone.developer@gmail.com">giuseppe.pedone.developer@gmail.com</a> | +3711963527 |

<br>
<br>

💬 Contact them if you have any Questions. 

<br>
<br>

# Acknowledgements

Special thanks to:

* *Open source community*
* *Contributors* of similar templates
* *Libraries and frameworks* that made this project possible

<br>

---

<br>
