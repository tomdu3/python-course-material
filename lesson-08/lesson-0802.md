## 8.2. Project Documentation

- [Readme Guide](https://youtu.be/l1DE7L-4eKQ)
- [How to write a kickass README](https://dev.to/scottydocs/how-to-write-a-kickass-readme-5af9)
- [How to Write a Good README File for Your GitHub Project](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)
- [Writing good README files](https://coderefinery.github.io/documentation/writing-readme-files/)
- [How to create a stunning README.md](https://medium.com/@sagarganiga468/how-to-create-a-stunning-readme-md-edf1c74b6a46)
  - [Sample README.md](https://github.com/SagarGaniga/How-to-Create-A-Stunning-README.md)

![Documentation AI](./documentationai.jpg)

### 8.2.1. Why Documentation Is Important

The `README.md` file is the first file that is visible to others when you push your project to a GitHub repository. It is a great way to introduce your project to others and show them how to use your code. It also helps others understand your project. You can easily say that a `README.md` is a calling card for your project. It should be a summary of your project and its features.

For many smaller and mid-size project, this is a good enough documentation. For larger projects, it should be accompanied by a detailed documentation. Nevertheless, if we browse through many of the open source projects, we can find that most of them have a good and complete `README.md` file.

The `README.md` file is also a great way to document our project from it's conception to the final product for ourselves. It will happen in the future, that we would return to one of our projects, only to find ourselves reading the code and trying to understand what it does.

### 8.2.2. MarkDown Syntax
- [Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github)
- [MarkDown Guide: *Basic Syntax*](https://www.markdownguide.org/basic-syntax/)
- [MarkDown Guide: *Cheet Sheet*](https://www.markdownguide.org/cheat-sheet/)
- [John Gruber: *MarkDown: Basics*](https://daringfireball.net/projects/markdown/basics)

`README.md` file is written in `MarkDown`. Markdown is a simple, easy-to-use syntax for formatting text. It is a great way to document our project. We will not got too much into details here. Here is a demonstration of the basic syntax of `MarkDown`:

Here is the Markdown syntax demonstration in two parts:

**Headings**
```
# Heading 1
## Heading 2
### Heading 3
```
**Text Formatting**
```
**Bold text**
*Italic text*
~~This is strikethrough text.~~

<u>This is underlined text.</u>
```

**Links**
```
[Link to Google](https://www.google.com)
[Link to Google](https://www.google.com "Title of link")

```

**Lists**
- ordered lists
```
1. Item 1
2. Item 2
3. Item 3
```

1. Item 1
2. Item 2
3. Item 3

- unordered lists

```
- Item 1
- Item 2
- Item 3
```

- Item 1
- Item 2
- Item 3

**Code**
For code quotes we use triple backticks. If we want to have syntax highlighting we can write the name of the coding language immediately after the backticks.

\`\`\`python
print("Hello, world!")
\`\`\`

```python
print("Hello, world!")
```

```
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
|----------|----------|----------|
| Cell 4   | Cell 5   | Cell 6   |
```

```
> This is a quote
> That's all folks!
```

```
Term: Definition
:   Description
```

```
<h1>Heading</h1>
<p>This is a paragraph</p>
```
***Example Outputs***

**Bold text** and *Italic text* are used to emphasize certain words.

~~This is strikethrough text.~~

<u>This is underlined text.</u>

[Link to Google](https://www.google.com) and [Link to Google](https://www.google.com "Title of link") are used to create links.


```python
print("Hello, world!")
```


The following table shows the structure of a Markdown document:

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
---

**Quotes**
```
> This is a quote
```

> This is a quote

**Definition lists** are used to define technical terms:

```
Term: Definition
:   Description
```

Term: Definition
:   Description

**Image**
```
![Image Text](link-to-the-image)
```

![Image](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)

Finally, **HTML code** is used to format the text:

```html
<h1>Heading</h1>
<p>This is a paragraph</p>
```
<h1>Heading</h1>
<p>This is a paragraph</p>


### 8.2.3. How to Write a Good README File for Your GitHub Project

For the documentation, we can have more different `md`, but the one that is the primary is `README.md`. When we put that file in the root directory of our project, it is rendered on our GitHub project repo. GitHub automatically converts our headings into working links and it makes it easier to navigate through our project. It also can automatically generate the table of contents.

Here is the list of sections and brief descriptions of each:

**1. Introduction**
A brief description of the project, including its purpose and main features.

**2. Overview**
A high-level overview of the project, including its features, functionalities, and technologies used.

**3. Flowchart**
A visual representation of the project's workflow, showing the steps involved in using the project.

**4. Technologies**
A list of the technologies and dependencies used in the project, including libraries, frameworks, and tools.

**5. Getting Started**
Step-by-step instructions for getting started with the project, including cloning the repository, installing dependencies, and creating a `.env` file.


**6. Usage**
Instructions for using the project, including step-by-step guides and configuration options.

**7. Changelog**
A list of significant changes made to the project, including bug fixes, new features, and improvements.


**8. Contributing**
Instructions for contributing to the project, including how to fork the repository, create a new branch, and submit a pull request.

**9. License**
Information about the license under which the project is released, including terms and conditions.

**10. Credits**
Acknowledgments to contributors and sponsors who have helped make the project possible.

**11. Links**
Additional resources and links for more information about the project, including its website, documentation, and social media channels.

Here is the provided sample you can use: [Sample README.md](./README-sample.md)

### 8.2.4. Some Auxiliary Resources

- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/) - a good MarkDown Tutorial from GitHub
- [Readme.so](https://readme.so/) - as the website says - the easiest way to create a README. It is an interactive `README.md` editor.
- [Example of a good GitHub README](https://github.com/SagarGaniga/How-to-Create-A-Stunning-README.md) - a good README example with different elements.
- VS Code extension for Automatically Generated Markdown Table of Contents - [Auto Markdown TOC](https://marketplace.visualstudio.com/items?itemName=joffreykern.markdown-toc)

## 8.3. Project Directory Structure

- [The Hitchhiker's Guide to Python: *Structuring Your Project*](https://docs.python-guide.org/writing/structure/)
- [Tech with Tim: *How To Structure A Programming Project*](https://youtu.be/CAeWjoP525M)
- [Programming 101: File Structures](https://medium.com/@deshayk/programming-101-file-structures-2e4699ac0fc2)
- [Guide to Python Project Structure and Packaging](https://medium.com/@joshuale/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95)

### 8.3.1. Recommended Project Structure

There are different ways how to organise your project and you can check the links above to learn more. For your final project, I would propose the structure below. If the project is small, you can use the same you don't have to have `aux` directory.


>.
├── app.py
├── aux
│   ├── end.txt
│   ├── highscores.json
│   ├── highscores.py
│   ├── intro.txt
│   ├── questions.json
│   ├── quiz.py
│   └── retrieve_api.py
├── docs
│   ├── img
│   │   └── image.png
│   └── pdf
│       └── doc.pdf
├── README.md
└── requirements.txt

- in the project's root directory (`/`):
  - `app.py` - is the main file of your project
  - `README.md` - is our main project documentation file
  - `requirements.txt` - contains all the dependencies of your project
- `aux/` - directory, contains auxiliary scripts and data files
- `docs/` - directory, contains documentation files (images, PDFs, etc.)

### 8.3.2. Importing Modules from different directories

- [Python Import Module From Different Directory](https://www.geeksforgeeks.org/python-import-module-from-different-directory/)

- general syntax:
  - `from directory_name import module_name` - import module from a directory. We call then functions by using `module_name.function_name()`
  - `from directory_name.subdirectory_name import module_name` - import module from a subdirectory. We call then functions by using `module_name.function_name()`
  - `from directory_name.module_name import function_name` - import specific function from a module in a directory
  - `from directory_name.module_name import *` - import all functions from a module in a directory

If we take into consideration the structure we presented in [Recommended Project Structure](#831-recommended-project-structure), we can import modules from a subdirectory this way.

```python
import aux.highscores as highscores
```
- in this case we need to call functions by using `highscores.function_name()`
or

```python
from aux import highscores
```
- also, in this case we need to call functions by using `highscores.function_name()`
- 
or

```python
from aux.highscores import *
```

- in this case we need to call functions by using only `function_name()`


## 8.4. Using Screenshots and Screencasts in your documentation

- [Asciinema](https://asciinema.org/) - a CLI tool to record and share terminal sessions.
- [pyPeek](https://github.com/firatkiral/pypeek) - a terminal-based screen cast tool.

To illustrate functionalities, we can use screenshots and screencasts in the documentation. This is a very easy and effective way to present the project and it's features.

Let us see what are they:
- `screenshots` are image files and stored in `docs/img` folder
- `screencasts` are usually `gif` files and stored in `docs/img` folder
- if they are in a video format, best way is to use `YouTube ` platform and add link to the video. Presenting your project in a video gives you an opportunity to explain your project verbally and, if you wish, in a more visually appealing way (video editing is an important part of this process).

Examples:
**Asciinema**
[![asciicast](https://asciinema.org/a/iUTVa1Dg0BcPwqIESMCPv5BHF.svg)](https://asciinema.org/a/iUTVa1Dg0BcPwqIESMCPv5BHF)

**pyPeek gif image**
![pyPeek gif image](https://github.com/tomdu3/smiling-depression/blob/main/assets/readme_images/testing/navbar-links.gif?raw=true)


**Image**
![Static Image](https://github.com/tomdu3/smiling-depression/blob/main/assets/readme_images/amiresponsive.png?raw=true)

**Screencast Video**
- [The Ultimate Guide: What Is A Screencast & How To Create One? (2024)](https://www.vmaker.com/blog/ultimate-guide-what-is-screencast-how-to-create-one/)