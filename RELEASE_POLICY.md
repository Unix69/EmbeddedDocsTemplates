<div align="center">

  <img src="assets/logo.png" alt="logo" width="200" height="auto" />
  <h1>Awesome Readme Template</h1>
  
  <p>
    An awesome README template for your projects! 
  </p>
  
  
<!-- Badges -->
<p>
  <a href="https://github.com/Louis3797/awesome-readme-template/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Louis3797/awesome-readme-template" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/Louis3797/awesome-readme-template" alt="last update" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/network/members">
    <img src="https://img.shields.io/github/forks/Louis3797/awesome-readme-template" alt="forks" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/stargazers">
    <img src="https://img.shields.io/github/stars/Louis3797/awesome-readme-template" alt="stars" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/issues/">
    <img src="https://img.shields.io/github/issues/Louis3797/awesome-readme-template" alt="open issues" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/Louis3797/awesome-readme-template.svg" alt="license" />
  </a>
</p>
   
<h4>
    <a href="https://github.com/Louis3797/awesome-readme-template/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/Louis3797/awesome-readme-template">Documentation</a>
  <span> · </span>
    <a href="https://github.com/Louis3797/awesome-readme-template/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/Louis3797/awesome-readme-template/issues/">Request Feature</a>
  </h4>
</div>



# :scroll: Release Policy

<!-- Content -->

This document specifies and explains the Release Policy followed for **[PROJECT-NAME]** versioning. Knowing the **Release Policy**, helps to characterize a given software release and its temporarly evolution. So **reading the Release Policy is a best practice** when you are approaching to a new product.


<!-- Table of Contents -->

# :notebook_with_decorative_cover: Table of Contents

Navigation index to fast explore the content:

- [Release Policy Brief Description](#release-policy-brief-description)
- [Version Identifier Composition and Format](#version-identifier-composition-and-format)
- [Version Label Encoding](#version-label-encoding)
- [Versioning Rules](#versioning-rules)	
	* [Versioning Precedence Rules](#versioning-precedence-rules)
	* [Versioning Grammar Rules](#versioning-grammar-rules)
- [Official Links](#official-links)



<!-- Release Policy Brief Description -->

## Release Policy Brief Description

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

**[PROJECT-NAME]** follows **Semantic Versioning (SemVer)** whereby the **Version Identifier (VID)** expresses a meaning about the characteristics of the identified software release, by encoding some ordered **labels** where each of them specify a software release state feature. 
SemVer is applicable from **[PROJECT-NAME] v1.0.0** onwards.


<!-- Version Identifier Composition and Format -->

## Version Identifier Composition and Format

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

SemVer's VIDs are essentially composed by a mandatory part, called **MAIN-VID**, and an optional part named **EXT-VID** in this format [NORM-VID][EXT-VID].

| SUB VID   | Description                                                                                                                                                                                   | Format |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| MAIN-VID  | **Static** structured and **Mandatory** identifier expressed by dot separated **MAJOR-VID**, **MINOR-VID** and **PATCH-VID** labels  | <ul><li> [MAJOR-VID].[MINOR-VID].[PATCH-VID] </li></ul> |
| EXT-VID   | **Dynamic** structured and **Optional** identifier expressed by **-/+** separated **PRE-RELEASE-VID**, **BUILD-METADATA-VID** labels | <ul><li> [MAIN-VID]-[PRE-RELEASE-VID]+[BUILD-METADATA-VID]</li><li>[MAIN-VID]-[PRE-RELEASE-VID]</li><li>[MAIN-VID]+[BUILD-METADATA-VID]</li></ul> |

So the **fully detailed VID** is encoded by the following expression:

<ul><li>[MAJOR-VID].[MINOR-VID].[PATCH-VID][-PRE-RELEASE-VID][+BUILD-METADATA-VID]</ul></li>

<br>

> :memo: **Notes**: each of **EXT-VID's** labels can be used optionally


<!-- Version Label Encoding -->

## Version Label Encoding

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

| MAIN-VID Labels | Description                                                                                         | Encoding                                                                | Hints |
| --------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MAJOR-VID       | It defines the major version identifier and it identifies **incompatible API changes**              | **Non negative integer** increased numerically. It **cannot be empty**. | <ul><li> 0 identify the initial development version. Anything can change at any time. The public API are not considered stable</li><li>It is incremented if any backward incompatible changes are introduced to the public API. </li><li> It can also include minor and patch level changes </li><li> **PATCH-VID** and **MINOR-VID** are resetted to 0 when major version is incremented</li></ul> |
| MINOR-VID       | It defines the minor version identifier and it identifies **backward compatible feature additions** | **Non negative integer** increased numerically. It **cannot be empty**. | <ul><li> It is incremented if new, backward compatible functionality is introduced to the public API </li><li> It is incremented if any public API functionality is marked as deprecated </li><li> It is incremented if substantial new functionality or improvements are introduced within the private code. It can include patch level changes </li></ul> |
| PATCH-VID       | It defines the patch version identifier and it identifies **backward compatible bug fixes**         | **Non negative integer** increased numerically. It **cannot be empty**. | <ul><li> It is incremented if only backward compatible bug fixes are introduced. </li><li> A bug fix is defined as an internal change that fixes incorrect behavior </li></ul> |

<br>

| EXT-VID Labels     | Description                                                                                                                                                                                                   | Encoding                                                                                                                                                                                                        | Hints                                                                                             	                                                                                                                                                                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | 
| PRE-RELEASE-VID    | It defines the pre-release version identifier and it identify an **unstable software version** that **might not satisfy the intended compatibility requirements** as denoted by its associated **[MAIN-VID]** | It is precedeed by an Hyphen (**-**) and a series of dot separated identifiers, immediately following the **PATCH-VID**. Each identifier comprise **only ASCII alphanumerics and hyphens** and **cannot be empty**.                        | <ul><li> Numeric identifiers do not include leading zeroes </li><li> Pre-release versions have a lower precedence than the associated normal version </li><li> A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version </li></ul> |
| BUILD-METADATA-VID | It defines the **metadata used into building process**                                                                                                                                                        | It is precedeed by a Plus (**+**) sign and a series of dot separated identifiers, immediately following the **PRE-RELEASE-VID** or **PATCH-VID**. Each identifier comprise **only ASCII alphanumerics and hyphens** and **cannot be empty**. | <ul><li> Build metadata has to be ignored when determining version precedence </li><li> Thus two versions that differ only in the build metadata, have the same precedence </li></ul>                                                                                                                                                            |

<br>

> :memo: **Notes** <ul><li> Once a Software version has been released, the contents of that version will be not modified anymore. Any modifications are released as a new version </li><li> **1.0.0** defines the public API. The way in which the version number is incremented after this release is dependent on this public API and how it changes </li></ul>


<!-- Versioning Rules -->

## Versioning Rules

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

This section contains version grammar and version precedence rules in order to validate a **VID** or compare two **VIDs** each other. Following this basic rules is helpful to understand <a href="https://www.semver.org" target="_blank">SemVer</a> and to move between different software releases.


<!-- Versioning Precedence Rules -->

### Versioning Precedence Rules

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

Precedence refers to how **VIDs** are compared to each other when ordered. The following precedence rules can be used to determine the precedence of a given **[MAIN-VID]** or **[EXT-VID]** respect to another:

- Precedence are calculated by **separating the version into major, minor, patch and pre-release identifiers** in that order (build metadata does not figure into precedence).
- **Precedence is determined by the first difference when comparing each of these identifiers from left to right** as follows: major, minor, and patch versions are always compared numerically.
	+ Example: **1.0.0** < **2.0.0** < **2.1.0** < **2.1.1**.
- When **major, minor, and patch are equal**, a **pre-release version has lower precedence than a normal version**:
	+ Example: **1.0.0-alpha** < **1.0.0**.
- Precedence for two pre-release versions with the same major, minor, and patch version are determined by comparing each dot separated identifier from left to right until a difference is found as follows:
	+ **Identifiers consisting of only digits are compared numerically**.
	+ **Identifiers with letters or hyphens are compared lexically in ASCII sort order**.
	+ **Numeric identifiers always have lower precedence than non-numeric identifiers**.
	+ A **larger set of pre-release fields has a higher precedence than a smaller set**, if all of the preceding identifiers are equal.
		+ Example: **1.0.0-alpha** < **1.0.0-alpha.1** < **1.0.0-alpha.beta** < **1.0.0-beta** < **1.0.0-beta.2** < **1.0.0-beta.11** < **1.0.0-rc.1** < **1.0.0**.


<!-- Versioning Grammar Rules -->

### Versioning Grammar Rules

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

```
		<VID> ::= <NORM-VID>
				 | <NORM-VID> "-" <PRE-RELEASE-VID>
				 | <NORM-VID> "+" <BUILD-METADATA-VID>
				 | <NORM-VID> "-" <PRE-RELEASE-VID> "+" <BUILD-METADATA-VID>

		<NORM-VID> ::= <MAJOR-VID> "." <MINOR-VID> "." <PATCH-VID>

		<MAJOR-VID> ::= <numeric identifier>

		<MINOR-VID> ::= <numeric identifier>

		<PATCH-VID> ::= <numeric identifier>

		<PRE-RELEASE-VID> ::= <dot-separated pre-release identifiers>

		<BUILD-METADATA-VID> ::= <dot-separated build identifiers>

		<dot-separated pre-release identifiers> ::= <pre-release identifier>
						          | <pre-release identifier> "." <dot-separated pre-release identifiers>

		<pre-release identifier> ::= <alphanumeric identifier>
					   | <numeric identifier>

		<dot-separated build identifiers> ::= <build identifier>
						    | <build identifier> "." <dot-separated build identifiers>

		<build identifier> ::= <alphanumeric identifier>
				     | <digits>

		<alphanumeric identifier> ::= <non-digit>
					    | <non-digit> <identifier characters>
					    | <identifier characters> <non-digit>
					    | <identifier characters> <non-digit> <identifier characters>

		<numeric identifier> ::= "0"
				       | <positive digit>
				       | <positive digit> <digits>

		<identifier characters> ::= <identifier character>
					  | <identifier character> <identifier characters>

		<identifier character> ::= <digit>
					 | <non-digit>

		<non-digit> ::= <letter>
			      | "-"

		<digits> ::= <digit>
			   | <digit> <digits>

		<digit> ::= "0"
			  | <positive digit>

		<positive digit> ::= "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

		 
		<letter> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J"
			   | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T"
			   | "U" | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" | "c" | "d"
			   | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n"
			   | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x"
			   | "y" | "z"
```

<!-- Related Docs -->

## Related Docs

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

The following documents are related to this documents:

* The `VERSION.md` file [Version](file://home/giuseppe/Documents/Programming/Templates/Code Additional Documentation Templates/Readme/VERSION.md) that contains the version history of **[PROJECT_NAME]**
* The `CHANGELOG.md` file [Version](file://home/giuseppe/Documents/Programming/Templates/Code Additional Documentation Templates/Readme/VERSION.md) that contains the changes made on **[PROJECT_NAME]**


<!-- Official Links -->

## Official Links

[Table of Contents](#notebook_with_decorative_cover-table-of-contents)

Consult the official <a href="https://www.semver.org" target="_blank">SemVer guide</a> for a complete guide on SemVer 




