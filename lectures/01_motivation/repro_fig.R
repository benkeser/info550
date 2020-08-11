# load packages
library(scifigure)

# function to get rid of 
my_sci_figure <- function (experiments, custom_icons = NULL, stage_names = c("Population", 
    "Question", "Hypothesis", "Exp. Design", "Experimenter", 
    "Data", "Analysis Plan", "Analyst", "Code", "Estimate", "Claim"), 
    hide_stages = NULL, diff = FALSE, showlegend = TRUE, cols = c("#D20000", 
        "#007888", "#CDCDCD", "black"), leg_text = c("Incorrect", 
        "Different", "Unobserved", "Original")) {
    if (!all(unlist(lapply(experiments, function(x) {
        x %in% c("observed", "different", "unobserved", "incorrect")
    })))) {
        stop("Invalid cell value in experiments data frame.")
    }
    if (ncol(experiments) > 20) {
        experiments <- experiments[, 1:20]
        warning("Only showing the first 20 experiments for ease of plotting.")
    }
    idx <- !(rownames(experiments) %in% hide_stages)
    stage_names <- stage_names[idx]
    experiments <- experiments[idx, , drop = FALSE]
    grid::grid.newpage()
    gptext <- grid::gpar(fontsize = 16 - min(nrow(experiments), 
        7))
    yht <- seq(0.95, 0.05, length = nrow(experiments))
    if (!is.null(stage_names)) {
        vp1 <- grid::viewport(x = 0.1, y = 0.5, width = 0.2, 
            height = 0.9)
        grid::pushViewport(vp1)
        grid::grid.text(stage_names, x = 0.9, y = yht, gp = gptext)
        grid::upViewport()
    }
    if (is.null(custom_icons)) {
        if (diff == FALSE) {
            icons <- scifigure::icons
        }
        else {
            icons <- scifigure::icons_diff
        }
    }
    else {
        if (length(stage_names) * 4 != length(custom_icons)) {
            stop("There must be four icons for each stage name.")
        }
        icons <- custom_icons
    }
    vp2 <- grid::viewport(x = 0.5, y = 0.5, width = 0.6, height = 0.9)
    grid::pushViewport(vp2)
    for (j in 1:ncol(experiments)) {
        for (i in 1:nrow(experiments)) {
            grid::grid.raster(icons[[paste(rownames(experiments)[i], 
                experiments[i, j], sep = "_")]], x = j/(ncol(experiments) + 
                1), y = yht[i], height = 0.08 - 0.03 * (ncol(experiments) > 
                4), width = grid::unit(max(0.05, min(0.1, 1/((ncol(experiments) * 
                3)))), "snpc"))
        }
    }
    grid::upViewport()
    vp3 <- grid::viewport(x = 0.5, y = 0.95, width = 0.6, height = 0.1)
    grid::pushViewport(vp3)
    grid::grid.text(colnames(experiments), x = (1:ncol(experiments))/(ncol(experiments) + 
        1), y = 0.7, gp = gptext, rot = ifelse(ncol(experiments) > 
        12, 90, 0))
    if (showlegend) {
        grid::upViewport()
        vp4 <- grid::viewport(x = 0.9, y = 0.5, width = 0.2, 
            height = 0.6)
        grid::pushViewport(vp4)
        if (diff == FALSE) {
            grid::grid.rect(width = 0.25, height = 0.1, x = 0.3, 
                y = c(0.4, 0.6), gp = grid::gpar(fill = cols[c(2,4)]))
        }
        else {
            # grid::grid.raster(icons[[3]], x = 0.3, y = 0.8, height = grid::unit(0.18, 
            #     "snpc"), width = grid::unit(0.18, "snpc"))
            grid::grid.raster(icons[[4]], x = 0.3, y = 0.6, height = grid::unit(0.18, 
                "snpc"), width = grid::unit(0.18, "snpc"))
            grid::grid.raster(icons[[1]], x = 0.3, y = 0.4, height = grid::unit(0.18, 
                "snpc"), width = grid::unit(0.18, "snpc"))
            # grid::grid.raster(icons[[2]], x = 0.3, y = 0.2, height = grid::unit(0.18, 
            #     "snpc"), width = grid::unit(0.18, "snpc"))
        }
        leg_text = c("Different", "Original")
        grid::grid.text(leg_text, x = 0.3, y = c(0.3, 0.5), gp = grid::gpar(fontsize = 9))
        grid::grid.rect(width = 0.25, height = 0.1, x = 0.3, 
            y = c(0.4, 0.6), gp = grid::gpar(fill = cols[c(2,4)]))
        grid::grid.text(leg_text, x = 0.3, y = c(0.3, 0.5), gp = grid::gpar(fontsize = 9))
    }
}

exp_names <- c("Original", "Reproducible", "Replicable", "Generalizable")
exps <- init_experiments(4, exp_names)
diffs <- list(
    NULL,
    "analyst",
    c("experimenter", "data", "analyst", "code", "estimate", "claim"),
    c("population")
)
exps_diffs <- data.frame(mapply(x = exp_names, y = diffs, function(x, y){
    exps[y, x] <- "different"
    exps[,x]
}))
row.names(exps_diffs) <- row.names(exps)