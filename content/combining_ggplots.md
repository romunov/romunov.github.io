Title: How to combine plots and table made with ggplot (or grid graphics) in R
Date: 2018-10-02
Category: HowTo
Tags: R, ggplot2, combine, plots, gridExtra, cowplot, patchwork

In the last few years, a number of options of how to combine grid graphics (incl. `ggplot2`) have emerged.
If you can't remember all functions to do this, this post may serve as a reference guide, but it's mostly
for me because I keep forgetting the functionalities provided by [`cowplot`](https://github.com/wilkelab/cowplot) and [`patchwork`](https://github.com/thomasp85/patchwork) packages ([thank you Jaap](https://chat.stackoverflow.com/transcript/75819?m=44067437#44067437)). Here appearing in order I encountered them.

```
library(ggplot2)

# prepare some figures
fig1 <- ggplot(mtcars, aes(x = mpg, y = disp, color = as.factor(gear))) +
  theme_bw() +
  theme(legend.position = "top") +
  scale_color_discrete(name = "gear") +
  geom_point()

fig2 <- ggplot(mtcars, aes(x = gear, y = disp, fill = as.factor(gear))) +
  theme_bw() +
  theme(legend.position = "top") +
  scale_fill_discrete(name = "gear") +
  geom_violin()
```

## gridExtra
Here is oldie but goldie from Baptiste's [`gridExtra`](https://cran.r-project.org/web/packages/gridExtra/index.html) package.
You can, for example, specify the layout matrix or specify number of columns. The below code chunk is using `ggplot2::ggsave` which saves the last subplot only, which is why I saved the result of `grid.arrange` into a new variable (but see `cowplot` below).

```
library(gridExtra)

fig.combined1 <- grid.arrange(fig1, fig2, ncol = 2)
ggsave(plot = fig.combined1, filename = "grid.arrange.png",
       width = 8, height = 4, units = "in", dpi = 96)
```
![oldie but goldie grid arrange]({static}images/grid.arrange.png)


## cowplot
Next is `cowplot`, which comes with nice [vignettes](https://cran.r-project.org/web/packages/cowplot/index.html). What I like about this package is the elegant adding of letters to subplots, e.g.

```
library(cowplot)

plot_grid(fig1, fig2, labels = "AUTO")
cowplot::ggsave(filename = "plotgrid.png", width = 8,
                height = 4, units = "in", dpi = 96)
```

See the vignettes for more information. Package also packs its own `ggplot` which masks the function `ggplot2::ggsave` (read: `ggsave` from package `ggplot2`). The beauty of it is that it saves the gridded plot, not the last (sub)plot.

![cowplot's grid_plot]({static}images/plotgrid.png)

## patchwork

Thomas did a great job of making combining of plots trivially easy. The [GitHub repository](https://github.com/thomasp85/patchwork) of the package is a rich source of information and I could never do it justice. Here's my botched attempt of just an example of what the package functionality provides.

```
library(patchwork)

fig1 + fig2
cowplot
```

![patchwork plus]({static}/images/patchplus.png)
