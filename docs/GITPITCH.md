# Try GitPitch Documentation

This document provides a quick overview of the documentation available on [gitpitch.com](https://gitpitch.com).

## Foundation Features

### Slideshow Menu

Every slideshow presentation makes a burger-menu available in the bottom-left corner of each slide. The menu provides access to the following slideshow presentation features:

* Offline Slideshow
* PDF Slideshow
* Theme Switcher - depricated?
* Table of Contents

### Online Slideshow


### Offline Slideshow

### PDF Slideshow

### Keyboard Controls

## Layout Features

The default layout policy centers content on your slides. However, if you ever want to change that default layout policy for your slide deck you can activate a custom layout policy.

### Automatic Layout
### Snap Layouts

## Markdown Features

https://guides.github.com/features/mastering-markdown/

### Fragments

Markdown fragment support is a simple yet powerful feature that can be used to reveal individual elements on a slide one-by-one.

* [Text Fragments](https://gitpitch.com/docs/markdown-features/fragments/#1-text-fragments)
* [List Fragments](https://gitpitch.com/docs/markdown-features/list-fragments/)
* [Boxed-Text Fragments](https://gitpitch.com/docs/markdown-features/fragments/#2-boxed-text-fragments)
* [Image Fragments](https://gitpitch.com/docs/markdown-features/fragments/#3-image-fragments)
* [Font Awesome Icon Fragments](https://gitpitch.com/docs/markdown-features/fragments/#4-font-awesome-icon-fragments)
* [Snap Layouts Fragments](https://gitpitch.com/docs/markdown-features/fragments/#5-snap-layouts-fragments)
* [Table Row Fragments](https://gitpitch.com/docs/markdown-features/fragments/#6-table-row-fragments)
* [HTML Snippet Fragments](https://gitpitch.com/docs/markdown-features/fragments/#7-html-snippet-fragments)

### Shortcuts

GitPitch provides a number of syntax shortcuts supported by `PITCHME.md` markdown that can be used to alter the appearance or behaviour of content or generate rich visual components on any slide.

* @size - Set Custom Font Size
* @color - Set Custom Font Color
* @css - Set Custom CSS Class
* @title - Set Custom TOC Label for Slide
* @transition - Set Slide-Specific Transition
* @box - Boxed Text Widget
* @box - Boxed Text With Title Widget
* @quote - Quote Widget
* @quote - Quote With Attribution Widget
* @fa - Font Awesome 5 Icon Widget
* @img - Image Widget
* @gitlink - Git Repo Link Widget
* @diff - Git Diff Widget
* @snap - Snap Layouts Widget

> Note: This feature is not supported by the GitPitch [open source project](https://github.com/gitpitch/gitpitch).

## Code Features

### Fenced Code Blocks

### Repository Source Files

### GitHub GIST Snippets

### Git Diff

## Image Features

### Inline Images

Any JPEG, PNG, or GIF image can be displayed inline within any slide using standard Markdown image syntax.

```md
![Logo](assets/img/logo.jpg)
![SAMBA Deployment](https://onetapbeyond.github.io/resource/img/samba/new-samba-deploy.jpg)
```

> Note: Remember to [size-optimize](https://gitpitch.com/docs/image-features/size-limits) your presentation images for the Web. A recommended tool is [tinypng.com](https://tinypng.com/).

### Background Images

```md
---?image=assets/img/bg.jpg
---?image=http://spark.apache.org/docs/latest/img/cluster-overview.png
```

#### scaling

Image delimiter syntax supports a size parameter that gives you complete control over background image sizing and scaling. The size parameter can take values including auto, contain, cover, w% h%, auto h%, etc. The default scaling value for background images is 100% 100%.

#### Positioning

Image delimiter syntax supports a position parameter that gives you complete control over background image positioning within slides. The position parameter can take values including center, left, right, 25% 75%, bottom 50px right 100px, etc. The default position value for background images is centre.

## Rich Media Features

## Speaker Features

GitPitch slideshow presentations support a number of great features tailored specifically for conference speakers and training instructors.

* [Speaker Notes](https://gitpitch.com/docs/speaker-features/notes/#speaker-notes) - Add private annotations to slides
* [Speaker Notes Fragments](https://gitpitch.com/docs/markdown-features/list-fragments) - Add fragment-specific speaker notes to lists
* [Speaker Notes Preview](https://gitpitch.com/docs/speaker-features/notes/#speaker-notes-preview) - Preview speaker notes by appending an n=true query parameter to the GitPitch URL
* [Speaker Window](https://gitpitch.com/docs/speaker-features/window/) - Provide a tailored view of any slide show presentation by pressing the **S** key
* [Speaker Remote Control](https://gitpitch.com/docs/settings/remote-control) - Add navigation between slides using remote control devices

## Theme Template

The GitPitch default theme template is provided [here](https://github.com/gitpitch/theme-template/blob/master/css/template.css)

```yaml
theme-background : [ "#FFF" ]
theme-headline   : [ "Raleway", "#5289F7", "none" ]
theme-byline     : [ "Raleway", "#111111", "none" ]
theme-text       : [ "Ubuntu", "#1C1C1C", "none" ]
theme-links      : [ "#5289F7", "#5254F7" ]
theme-code       : [ "Source Code Pro" ]
theme-controls   : [ "#484848" ]
theme-margins    : [ "0", "15px" ]
```

## Settings

GitPitch offers a wide range of slide show settings that can be used to customize the overall look-and-feel and behaviour of any presentation.

These settings are configured by the `PITCHME.yaml` properties file alongside the `PITCHME.md` file in this repository.

### Theme

The theme setting lets you select a fixed theme for your presentation. The default `GitPitch` theme is the [template theme](https://github.com/gitpitch/theme-template/blob/master/css/template.css):

```yaml
theme : template
```

See full detail [here](https://gitpitch.com/docs/settings/theme/).

### Custom Theme

The theme-override setting lets you override the CSS styles associated with the fixed theme for your presentation.

The following custom CSS stylesheet to override the default style in order to remove image borders and box-shadow for your slideshow:

```css
.reveal section img {
  border: 0;
  box-shadow: none;
}
```

Assuming that CSS stylesheet lived in the assets/css/PITCHME.css directory within your repository, you could active this custom theme override for your presentation as follows:

```yaml
theme-override : assets/css/PITCHME.css
```

See full detail [here](https://gitpitch.com/docs/settings/custom-theme/).

### Code Highlighting

The highlight setting lets you customize the syntax highlighting style for code rendered on slides within your presentation.

Support for code syntax highlighting is provided by the `highlight.js` library. This is an example configuration:

```yaml
highlight : mono-blue
```

See an interactive demo of available styles [here](https://highlightjs.org/static/demo/). Full details on this setting can be found [here](https://gitpitch.com/docs/settings/highlight/).

### Code Line Numbers

The code-line-numbers setting lets you activate the display of line-numbers alongside code rendered on slides within your presentation.

This feature is disabled by default but use the following setting to enable it:

```yaml
code-line-numbers : true
```

See full detail [here](https://gitpitch.com/docs/settings/line-numbers/).

### Layout

The layout setting lets you set an automatic layout policy for your slide show content. See [snap layouts](https://gitpitch.com/docs/layout-features/snap-layouts) to learn how to override the automatic layout policy for individual content on individual slides.

The following slide show layouts are supported:

* center (default)
* center-left
* center-right
* top
* top-left
* top-right

This is an example layout configuration:

```yaml
layout : top-left
```

See full detail [here](https://gitpitch.com/docs/settings/layout/).

### Logo

The logo setting lets you use a custom logo to brand every slide in your presentation. The default position of the logo is the top-left corner, however this can be changed by specifying a logo-position setting alongside the logo setting.

Supported positions are:

* top-left (default)
* top-right
* bottom-left
* bottom-right

This is an example logo configuration:

```yaml
logo : assets/img/logo.png
logo-position : top-right
```

See full detail [here](https://gitpitch.com/docs/settings/logo/).

### Background

`GitPitch` supports a number of background-* settings that can be combined to deliver precise control over default background images used by any presentation.

* Background - Specify a default background image for all slides within your presentation
* Background size - Specify a sizing and scaling policy for your default background image
* Background position - Specify a custom position for your default background image
* Background colour - Fill any exposed slide area not covered by your default background image with a colour
* Background repeat - Repeat a background image on a slide background

This is an example background configuration:

```yaml
background : assets/img/bg.png
background-size : auto 90%
background-position : left
background-color : black
background-repeat : repeat-x
```

See the full detail on the background setting [here](https://gitpitch.com/docs/settings/background/).

### Transition

The transition setting lets you select the default slide transition style for your presentation. To override the default behaviour, see [slide specific transition override](https://gitpitch.com/docs/markdown-features/shortcuts#set-slide-specific-transition).

The currently supported slide transition styles are:

* none (default)
* slide
* fade
* convex
* concave
* zoom

> Note: transitions must be disabled on slides using snap-layouts

This is an example transition configuration:

```yaml
transition : fade
```

See the full detail on the slide transition setting [here](https://gitpitch.com/docs/settings/transition/).

### Title

The title setting lets you set a custom HTML title for your slide show presentation.

This is an example title configuration:

```yaml
title : "Try GitPitch Today"
```

See the full detail on the title setting [here](https://gitpitch.com/docs/settings/title/).

### Footnote

The footnote setting lets you display a custom footnote on every slide within your presentation. It also supports arbitrary HTML fragments alongside plain text - see [Interactive Footnotes](https://gitpitch.com/docs/settings/footnote/#interactive-footnotes) and [Custom Footnote Styling](https://gitpitch.com/docs/settings/footnote/#custom-footnote-styling).

This is an example footnote configuration:

```yaml
footnote : "© 2019 auticon Ltd."
```

See the full detail on the title setting [here](https://gitpitch.com/docs/settings/footnote/).

### Published

For public repositories the published setting lets you flag a presentation as post-development and ready for sharing.

The following configuration marks the presentation as published:

```yaml
published : true
```

When the published setting is activated the `GitPitch` menus for the presentation are automatically simplified as below. The Git Service and Theme Chooser panels are hidden leaving only the Home panel and the Table of Contents navigation panel available.

![settings-published-menu](https://gitpitch.com/docs/images/settings-published-menu.jpg)

See the full detail on the published setting [here](https://gitpitch.com/docs/settings/published/).

### Controls Layout

The controls-layout setting lets you control the position of the navigation controls for your presentation. By default, the navigation controls for a presentation are found in the bottom-right corner of each slide. Alternatively the **edges** value can be chosen to cause the navigation controls to display in a centered position on each edge of the slide:

The following configuration marks the presentation as published:

```yaml
controls-layout : edges
```

See the full detail on the controls layout setting [here](https://gitpitch.com/docs/settings/published/).

### Print Fragments

The print-fragments setting lets you force each slide fragment to be printed on an independent page during PDF generation for your presentation. The default when PDF printing online at [gitpitch.com](https://gitpitch.com) is to ignore markdown fragments and code presenting fragments during the PDF printing process.

To set fragments to be printed use the following setting:

```yaml
print-fragments : true
```

See the full detail on the controls layout setting [here](https://gitpitch.com/docs/settings/print-fragments/).

### Remote Control

The remote-control setting lets you activate navigation using a remote control device: Logitech, Kensington, etc.

This feature is disabled by default but use the following setting to enable it:

```yaml
remote-control : true
```

See the full detail on the remote control settings [here](https://gitpitch.com/docs/settings/remote-control/).

### Eager Loading

When the eager-loading setting is activated slide show assets, including images and videos, are loaded over the network when a presentation is first opened in the browser.

This feature is disabled by default ensuring a lazy-loading policy is used. Use the setting below to enable it:

```yaml
eager-loading : true
```

By default, this setting is disabled, ensuring a lazy-loading policy is used for slide show presentation assets.

See the full detail on the eager loading setting [here](https://gitpitch.com/docs/settings/eager-loading/).

### Charts Plug-in

The charts setting lets you activate `Chart.js` rendering for your slide show presentation. Use the setting below to enable it:

```yaml
charts : true
```

See details on creating charts using this plug-in [here](https://gitpitch.com/docs/rich-media-features/charts).

### Maths Plug-in

The mathjax setting lets you activate `MathJax.js` rendering for your slide show presentation. This setting enables the plug-in and customises the [*MathJax* Configuration](https://docs.mathjax.org/en/latest/configuration.html#configuring-mathjax). For example, the below setting activates the `TeX-MML-AM_HTMLorMML-full` configuration:

```yaml
mathjax : TeX-MML-AM_HTMLorMML-full
```

See details on creating formulas using this plug-in [here](https://gitpitch.com/docs/rich-media-features/math-formulas).
