[![GitPitch](https://gitpitch.com/assets/badge.svg)](https://gitpitch.com/acdaniells/try-gitpitch)

# Try GitPitch

This project is for trying out the various free features of the `GitPitch` markdown presentation service used by developers for creating modern slide shows. This service extends the capabilities of the hugely popular and powerful `Reveal.js` HTML presentation framework and combines it with the distributed and collaborative file management capabilities of `Git`.

The following sections show how to get started with the project and provide a quick overview of the documentation available on [gitpitch.com](https://gitpitch.com).

## Getting Started

To get started with this project an account on `GitHub` is required.

For a simpler introduction to `GitPitch` follow [GitPitch try-gitpitch for GitHub Users](https://github.com/gitpitch/try-gitpitch) tutorial.

### Fork this Repository

Create a fork of this repository.

Forking this repository will create a new try-gitpitch repository under your own GitHub account. Within your new repository you will find the basic file structure for a GitPitch slide show presentation:

```
.
├── PITCHME.md
├── PITCHME.yaml
├── assets
│   ├── css
│   │   └── PITCHME.css
│   └── img
│       └── *.{jpg, gif, png}
└── talks
    ├── advanced
    │   ├── PITCHME.md
    │   └── PITCHME.yaml
    └── simple
        ├── PITCHME.md
        └── PITCHME.yaml
```

Only a PITCHME.md markdown file is required to create a GitPitch slide show presentation. This is the file where you add the markdown content for your slides. Optional files, such as PITCHME.yaml and PITCHME.css can be added to activate custom settings and styles for your slide deck.

Having forked this repository you are now ready to move on to step 2. in this try GitPitch tutorial.

### View the Presentation

Following a fork of the repository a `PITCHME.md` markdown file will be found in your new repository. This means that your first GitPitch slide deck is immediately available at the following URL:

```
https://gitpitch.com/$USER/try-gitpitch
```

> You must substitute your GitHub account name for $USER in the above slide show URL.

Using your slide show URL, go ahead and open your new slide deck in the browser now. When you open your slide deck you should see the first sample slide that should look a lot like this screenshot:



> For comparison purposes, the slide show URL for the GitPitch In-60-Seconds sample presentation associated with the gitpitch GitHub account can be launched here.

A slide show URL for a presentation published on `GitHub` is defined as follows:

```
https://gitpitch.com/$USER/try-gitpitch/?p=talks/sample-1/$BRANCH?p=$DIRECTORY
```

That's it for the first part of the try GitPitch tutorial.

If you are eager to jump straight back into the GitPitch Docs, click here. But if you want to learn a little more about how the sample presentation for this tutorial was created - and that's strongly recommended - then read on for additional details and tips.

### Markdown Basics

The [Mastering Markdown Guide](https://guides.github.com/features/mastering-markdown/) is a good resource to learn or refresh the basic usage of Markdown and the `GitHub` Flavored Markdown extensions.


### The PITCHME.md Convention

`GitPitch` introduces the `PITCHME.md` convention that automatically turns any `PITCHME.md` file found within a Git repository into a beautiful slide show presentation.

This convention gives developers a simple and convenient way to promote, pitch or present absolutely anything.

### Slide Delimiters

To split markdown content into a series of slides, presentation authors must use a special slide delimiter syntax. Each delimiter denotes the start of a new slide.

To create a new slide use the following delimiter syntax within your PITCHME.md file:

```
---
```

As both horizontal (default) and vertical slides are supported by `GitPitch` each has it's own unique delimiter syntax. To create a new vertical-slide use the following delimiter syntax within your PITCHME.md file:

```
+++
```

By using a combination of horizontal and vertical slide delimiters you can customize how your audience experiences and navigates content within your slide show presentation.

> Note: Typically horizontal slides present top-level information. Vertical slides are then used to drill-down.

### GitPitch Documentation

* [Free Features Overview](docs/GITPITCH.md)
* [GitPitch Documenation](https://gitpitch.com/docs)

## Sample Presentations

This repository currently contains two sets of sample slides located in the talks folder. These samples:

| Name                  | Slides        | Documentation |
|:--------------------- |:-------------:|:-----:|
| Simple Presentation   | [![GitPitch](https://gitpitch.com/assets/badge.svg)](https://gitpitch.com/acdaniells/try-gitpitch/master?p=talks/simple) | [docs](talks/simple/README.md) |
| Advanced Presentation | [![GitPitch](https://gitpitch.com/assets/badge.svg)](https://gitpitch.com/acdaniells/try-gitpitch/master?p=talks/advanced) | [docs](talks/advanced/README.md) |

# License

This project by Andrew Daniells is licensed under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode).

![cc-by-4.0 license](https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by.svg)
