<div align="left">

  <h1>🧑‍💼 Administrator Guide</h1>
  <h3>v1.0</h3>
  
  <br>
  
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

  <br><br>

  <p>
    A <b>full guide</b> to support <b>Administrators</b> during the project administration process and show how to perform administration tasks.
  </p>

</div>

<br><br>

<div align="left" style="margin-left: 24px;">

<a name="table-of-contents"></a>

## 📓 Table of Contents
- [Administration Overview](#administration-overview)
- [Administration LifeCycle](#administration-lifecycle)
- [Administration Tasks](#administration-tasks)
- [Prerequisites and Dependencies](#prerequisites-and-dependencies)
- [Installation](#installation)
- [Build](#build)
- [Configuration](#configuration)
- [Testing](#testing)
- [Documentation Generation](#documentation-generation)
- [References](#references)
- [How To](#how-to)
  - [How to access as administrator](#how-to-access-as-administrator)
- [Other Guides](#other-guides)
- [FAQ](#faq)
- [Authors](#authors)
- [Contact Us](#contact-us)

---

## Administration Overview

Administrators are responsible for the deployment, configuration, and maintenance of **README Template**. They ensure the system is properly installed, dependencies are satisfied, and documentation is consistently updated.

---

## Administration LifeCycle

The Administration LifeCycle covers:

1. Verifying system prerequisites  
2. Installing dependencies and the project  
3. Building and configuring the project  
4. Generating and maintaining documentation via Doxygen  
5. Running tests to validate the build  
6. Managing updates, fixes, and feature integrations  
7. Monitoring system and project health  

---

## Administration Tasks

Administrators perform the following tasks:

- Install and update project dependencies: Git, Doxygen, GNU Make  
- Setup project environment and folders  
- Manage system users and permissions  
- Run build scripts and manage Makefile targets  
- Generate, configure, and update Doxygen documentation  
- Apply patches and fixes as per `FIX.md`  
- Track versioning using `VERSION.md` and `CHANGELOG.md`  
- Ensure system security, backups, and stable operation  

---

## Prerequisites and Dependencies

Before building or running **README Template**, ensure the following:

- **Operating System**: GNU/Linux or Windows  
- **Software Dependencies**:  
  - GitHub / Git  
  - Doxygen (mandatory)  
  - GNU Make (mandatory)  

### Dependency Verification

<code>
git --version
doxygen --version
make --version
</code>

If all return version numbers, the system is ready.

---

## Installation

### Option A — Download ZIP

<code>
mkdir project-root
cd project-root
wget https://github.com/Unix69/README-Template/archive/refs/heads/main.zip
unzip main.zip
cp -R README-Template-main/ ./
rm -rf README-Template-main main.zip
</code>

### Option B — Clone Repository

<code>
mkdir project-root
cd project-root
git clone https://github.com/Unix69/EmbeddedDocsTemplates.git
cp -R EmbeddedDocsTemplates/ ./
rm -rf EmbeddedDocsTemplates
</code>

---

## Build

You can build **README Template** using:

### Using `doxygen.sh` script:

<code>
./doxygen.sh
</code>

### Using Makefile:

<code>
make build
</code>

### Using Standard Doxyfile:

<code>
doxygen -g Doxyfile
</code>

---

## Configuration

Administrators can configure the project by:

1. Adding source code to `./src`  
2. Modifying `doxygen.ini` parameters  
3. Editing `Doxyfile` (generated via `doxygen.sh`)  
4. Customizing `Makefile` targets  
5. Adjusting Markdown files for project documentation  

---

## Testing

Run project tests using:

<code>
sudo ./test.sh
</code>

Ensure all tests pass before deploying or updating documentation.

---

## Documentation Generation

To generate project documentation:

### Using Doxygen:

<code>
doxygen Doxyfile
</code>

### Using Makefile:

<code>
make doc
</code>

Documentation will be available in `./docs/` or the `OUTPUT_DIRECTORY` set in `Doxyfile`.
 

<br><br>

<a name="how-to"></a>

# How To 🛠️

[Table of Contents](#table-of-contents)

Below are all the "**Administrator How To**".

* [**How to access as administrator**](#how-to-access-as-admin)
* [**How to restart the system**](#how-to-restart)
* [**How to update configuration**](#how-to-update-config)

<br><br>

<a name="how-to-access-as-admin"></a>

## How to access as administrator

<code>
sudo -i
</code>

<br><br>

<a name="how-to-restart"></a>

## How to restart the system

<code>
systemctl restart [PROJECT_SERVICE]
</code>

<br><br>

<a name="how-to-update-config"></a>

## How to update configuration

1. Edit the configuration file  
   <code>nano /etc/[PROJECT_NAME]/config.conf</code>

2. Apply changes  
   <code>systemctl reload [PROJECT_SERVICE]</code>

<br><br>

<a name="other-guides"></a>

# Other Guides 📚

[Table of Contents](#table-of-contents)

<br>

| Role                  | Reference                                               | Description                    |
| --------------------- | ------------------------------------------------------- | ------------------------------ |
| 📘 <b>User Guide</b>         | <span class="md-link" data-github="Usage/USER_GUIDE.md" data-doxygen="md_Usage_USER_GUIDE.html"><a href="USER_GUIDE.md"><b>USER_GUIDE.md</b></a></span> | End-user operations            |
| 🧑‍💻 <b>Developer Guide</b> | <span class="md-link" data-github="Usage/DEVELOPMENT_GUIDE.md" data-doxygen="md_Usage_DEVELOPMENT_GUIDE.html"><a href="DEVELOPMENT_GUIDE.md"><b>DEVELOPMENT_GUIDE.md</b></a></span> | API and namespace usage        |

<br><br>

<a name="faq"></a>

# FAQ ❓

Here you can find the answers to frequently asked questions.

<br><br>

<a name="contact-us"></a>

# Contact us ☎️

For <b>more information</b> on [PROJECT_NAME]  
<span class="md-link" data-github="CONTACT_US.md" data-doxygen="md_CONTACT_US.html"><a href="CONTACT_US.md"><b>contact us</b></a></span>.

<br><br>

<a name="authors"></a>

# Authors 🧑‍💻

Here you can find <b>all authors</b> of [PROJECT_NAME] and their <b>Contribution & Info</b> 📝 :

| 👤 Author | 🤝 Contributions | 👥 Roles | Email | ☎️ Telephone | 
|--------|------|---------------|-------|-------|
| <span class="md-link" data-github="https://github.com/Unix69" data-doxygen="https://github.com/Unix69"><a href="https://github.com/Unix69"><img src="https://avatars.githubusercontent.com/u/111588387?v=4" width="100px;"/><br/><sub><b>Unix69</b></sub></a></span> | `FI`, `OP`, `DE` | `FO`, `CEO` | <a href="giuseppe.pedone.developer@gmail.com">giuseppe.pedone.developer@gmail.com</a> | +3711963527 |

<br><br>

💬 Feel free to contact them for any questions.

<br><br>

</div>