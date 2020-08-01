---
title: Generative Models
description: ML fundamentals 7
categories:
  - machine-learning
tags:
toc: true
toc_sticky: true
comments: true
excerpt: |
  Regularization / Comparison between Ridge and Lasso Regression / bias-variance tradeoff
# header:
#   image: /assets/images/logos/logo-text-8c3ba8a6.svg
---

# Generative Models

```{r setup, include = FALSE}
knitr::opts_chunk$set(echo = TRUE, fig.align = "center", cache = TRUE, autodep = TRUE)
```

***

In this chapter, we continue our discussion of classification methods. We introduce three new methods, each a **generative** method. This in comparison to logistic regression, which is a **discriminative** method.

Generative methods model the joint probability, $p(\boldsymbol{x}, y)$, often by assuming some distribution for the conditional distribution of $\boldsymbol{X}$ given $Y$, $f(\boldsymbol{x} \mid y)$. Bayes theorem is then applied to classify according to $p(y \mid \boldsymbol{x})$. Discriminative methods such as logistic regression directly model this conditional, $p(y \mid \boldsymbol{x})$. A detailed discussion and analysis can be found in [Ng and Jordan, 2002](https://papers.nips.cc/paper/2020-on-discriminative-vs-generative-classifiers-a-comparison-of-logistic-regression-and-naive-bayes.pdf).

***

## Reading

- **Required:** [ISL Chapter 4, Sections 4](https://faculty.marshall.usc.edu/gareth-james/ISL/ISLR%20Seventh%20Printing.pdf)

***

```{r packages, message = FALSE, warning = FALSE}
library("MASS")
library("tidyverse")
library("knitr")
library("kableExtra")
library("klaR")
```

***

Each of the methods in this chapter will use Bayes theorem to build a classifier.

$$
p_k(\boldsymbol{x}) = P(Y = k \mid \boldsymbol{X} = \boldsymbol{x}) = \frac{\pi_k \cdot f_k(\boldsymbol{x})}{\sum_{g = 1}^{G} \pi_g \cdot f_g(\boldsymbol{x})}
$$

We call $p_k(\boldsymbol{x})$ the **posterior** probability, which we will estimate then use to create classifications. The $\pi_g$ are called the **prior** probabilities for each possible class $g$. That is, $\pi_g = P(Y = g)$, unconditioned on $\boldsymbol X$. (Here, there are $G$ possible classes, denoted $1, 2, \ldots G$. We use $k$ to refer to a particular class.) The $f_g(x)$ are called the **likelihoods**, which are indexed by $g$ to denote that they are conditional on the classes. The denominator is often referred to as a **normalizing constant**.

The methods will differ by placing different modeling assumptions on the likelihoods, $f_g(\boldsymbol x)$. For each method, the priors could be learned from data or pre-specified.

For each method, classifications are made to the class with the highest estimated posterior probability, which is equivalent to the class with the largest

$$
\log(\hat{\pi}_k \cdot \hat{f}_k(\boldsymbol{x})).
$$

By substituting the corresponding likelihoods, simplifying, and eliminating unnecessary terms, we could derive the discriminant function for each.

To illustrate these new methods, we return to the iris data, which you may remember has three classes. After a test-train split, we create a number of plots to refresh our memory.

```{r}
set.seed(9)
iris_idx = sample(nrow(iris), size = trunc(0.50 * nrow(iris)))
# iris_idx = sample(nrow(iris), size = trunc(0.10 * nrow(iris)))
iris_trn = iris[iris_idx, ]
iris_tst = iris[-iris_idx, ]
```

Note that we have only performed a test-train split, so we are not validating any of these models. Also note that using 50% of the data for training is an arbitrary choice here.

```{r, fig.height = 8, fig.width = 8}
caret::featurePlot(x = iris_trn[, c("Sepal.Length", "Sepal.Width",
                                    "Petal.Length", "Petal.Width")],
                   y = iris_trn$Species,
                   plot = "density",
                   scales = list(x = list(relation = "free"),
                                 y = list(relation = "free")),
                   adjust = 1.5,
                   pch = "|",
                   layout = c(2, 2),
                   auto.key = list(columns = 3))
```

```{r, fig.height=8, fig.width=8}
caret::featurePlot(x = iris_trn[, c("Sepal.Length", "Sepal.Width",
                                    "Petal.Length", "Petal.Width")],
                   y = iris_trn$Species,
                   plot = "ellipse",
                   auto.key = list(columns = 3))
```

```{r, fig.height=4, fig.width=7}
caret::featurePlot(x = iris_trn[, c("Sepal.Length", "Sepal.Width",
                                    "Petal.Length", "Petal.Width")],
                   y = iris_trn$Species,
                   plot = "box",
                   scales = list(y = list(relation = "free"),
                                 x = list(rot = 90)),
                   layout = c(4, 1))
```

Especially based on the pairs plot, we see that it should not be too difficult to find a good classifier.

Notice that we use `caret::featurePlot` to access the `featurePlot()` function without loading the entire `caret` package.

***

## Linear Discriminant Analysis

Linear Discriminant Analysis, **LDA**, assumes that the features are multivariate normal conditioned on the classes.

$$
\boldsymbol{X} \mid Y = k \sim N(\boldsymbol{\mu}_k, \boldsymbol\Sigma)
$$

$$
f_k(\boldsymbol{x}) = \frac{1}{(2\pi)^{p/2}|\boldsymbol\Sigma|^{1/2}}\exp\left[-\frac{1}{2}(\boldsymbol x - \boldsymbol\mu_k)^{\prime}\boldsymbol\Sigma^{-1}(\boldsymbol x - \boldsymbol\mu_k)\right]
$$

Notice that $\boldsymbol\Sigma$ does **not** depend on $k$, that is, we are assuming the same $\Sigma$ for each class. We then use information from all the classes to estimate $\boldsymbol\Sigma$.

To fit an LDA model, we use the `lda()` function from the `MASS` package.

```{r}
iris_lda = lda(Species ~ ., data = iris_trn)
iris_lda
```

Here we see the estimated $\hat{\pi}_k$ and $\hat{\boldsymbol\mu}_k$ for each class.

```{r}
is.list(predict(iris_lda, iris_trn))
names(predict(iris_lda, iris_trn))
head(predict(iris_lda, iris_trn)$class, n = 10)
head(predict(iris_lda, iris_trn)$posterior, n = 10)
```

As we should come to expect, the `predict()` function operates in a new way when called on an `lda` object. By default, it returns an entire list. Within that list `class` stores the classifications and `posterior` contains the estimated probability for each class.

```{r}
iris_lda_trn_pred = predict(iris_lda, iris_trn)$class
iris_lda_tst_pred = predict(iris_lda, iris_tst)$class
```

We store the predictions made on the train and test sets.

```{r}
calc_misclass = function(actual, predicted) {
  mean(actual != predicted)
}
```

```{r}
calc_misclass(predicted = iris_lda_trn_pred, actual = iris_trn$Species)
calc_misclass(predicted = iris_lda_tst_pred, actual = iris_tst$Species)
```

As expected, LDA performs well on both the train and test data. (Note that the "training error" here is calculated on the training data since there is no validation data. This is not how we have usually defined training error.)

```{r}
table(predicted = iris_lda_tst_pred, actual = iris_tst$Species)
```

Looking at the test set, we see that we are perfectly predicting both setosa and virginica. The only error is labeling a couple versicolors as a virginica.

```{r}
iris_lda_flat = lda(Species ~ ., data = iris_trn, prior = c(1, 1, 1) / 3)
iris_lda_flat
```

Instead of learning (estimating) the proportion of the three species from the data, we could instead specify them ourselves. Here we choose a uniform distributions over the possible species. We would call this a "flat" prior.

```{r}
iris_lda_flat_trn_pred = predict(iris_lda_flat, iris_trn)$class
iris_lda_flat_tst_pred = predict(iris_lda_flat, iris_tst)$class
```

```{r}
calc_misclass(predicted = iris_lda_flat_trn_pred, actual = iris_trn$Species)
calc_misclass(predicted = iris_lda_flat_tst_pred, actual = iris_tst$Species)
```

This actually gives a better test accuracy! In practice, this could be useful if you have prior knowledge about the future proportions of the response variable.

***

## Quadratic Discriminant Analysis

Quadratic Discriminant Analysis, **QDA**, also assumes that the features are multivariate normal conditioned on the classes.

$$
\boldsymbol X \mid Y = k \sim N(\boldsymbol\mu_k, \boldsymbol\Sigma_k)
$$

$$
f_k(\boldsymbol x) = \frac{1}{(2\pi)^{p/2}|\boldsymbol\Sigma_k|^{1/2}}\exp\left[-\frac{1}{2}(\boldsymbol x - \boldsymbol\mu_k)^{\prime}\boldsymbol\Sigma_{k}^{-1}(\boldsymbol x - \boldsymbol\mu_k)\right]
$$

Notice that now $\boldsymbol\Sigma_k$ **does** depend on $k$, that is, we are allowing a different $\boldsymbol\Sigma_k$ for each class. We only use information from class $k$ to estimate $\Sigma_k$.

```{r}
iris_qda = qda(Species ~ ., data = iris_trn)
iris_qda
```

Here the output is similar to LDA, again giving the estimated $\hat{\pi}_k$ and $\hat{\boldsymbol\mu}_k$ for each class. Like `lda()`, the `qda()` function is found in the `MASS` package.

Consider trying to fit QDA again, but this time with a smaller training set. (Use the commented line above to obtain a smaller test set.) This will cause an error because there are not enough observations within each class to estimate the large number of parameters in the $\boldsymbol\Sigma_k$ matrices. This is less of a problem with LDA, since all observations, no matter the class, are being use to estimate the shared $\boldsymbol\Sigma$ matrix.

```{r}
iris_qda_trn_pred = predict(iris_qda, iris_trn)$class
iris_qda_tst_pred = predict(iris_qda, iris_tst)$class
```

The `predict()` function operates the same as the `predict()` function for LDA.

```{r}
calc_misclass(predicted = iris_qda_trn_pred, actual = iris_trn$Species)
calc_misclass(predicted = iris_qda_tst_pred, actual = iris_tst$Species)
```

```{r}
table(predicted = iris_qda_tst_pred, actual = iris_tst$Species)
```

Here we see that QDA has similar performance to LDA. This is somewhat surprising, as we can see from the plots above that the covariance matrix for each class is likely not the same. In this case, we would sort of assume that LDA is too restrictive a model as it assumes the same covariance within each class. (It is likely due to the high seperation of the data that this doesn't make much of a difference. Also, random chance as we're not dealing with a lot of data.)

Since QDA is a more complex model than LDA (it has many more parameters), QDA is more likely to overfit than LDA. (Although, that does not seem to have happened here.)

Also note that, QDA creates quadratic decision boundaries, while LDA creates linear decision boundaries. We could also add quadratic terms to LDA to allow it to create quadratic decision boundaries.

***

## Naive Bayes

Naive Bayes comes in many forms. With only numeric features, it often assumes a multivariate normal conditioned on the classes, but a very specific multivariate normal.

$$
{\boldsymbol X} \mid Y = k \sim N(\boldsymbol\mu_k, \boldsymbol\Sigma_k)
$$

Naive Bayes assumes that the features $X_1, X_2, \ldots, X_p$ are independent. This is the "naive" part of naive Bayes. The Bayes part is nothing new. Since $X_1, X_2, \ldots, X_p$ are assumed independent, each $\boldsymbol\Sigma_k$ is diagonal, that is, we assume no correlation between features. Independence implies zero correlation.

This will allow us to write the (joint) likelihood as a product of univariate distributions. In this case, the product of univariate normal distributions instead of a (joint) multivariate distribution.

$$
f_k(\boldsymbol x) = \prod_{j = 1}^{p} f_{kj}(\boldsymbol x_j)
$$

Here, $f_{kj}(\boldsymbol x_j)$ is the density for the $j$-th feature conditioned on the $k$-th class. Notice that there is a $\sigma_{kj}$ for each feature for each class.

$$
f_{kj}(\boldsymbol x_j) = \frac{1}{\sigma_{kj}\sqrt{2\pi}}\exp\left[-\frac{1}{2}\left(\frac{x_j - \mu_{kj}}{\sigma_{kj}}\right)^2\right]
$$

When $p = 1$, this version of naive Bayes is equivalent to QDA.

```{r}
iris_nb = NaiveBayes(Species ~ ., data = iris_trn)
```

```{r}
iris_nb$apriori
```

```{r}
iris_nb$tables
```

Many packages implement naive Bayes. Here we choose to use `NaiveBayes()` from the package `klaR`.

The output from `iris_nb$tables` gives the mean and standard deviation of the normal distribution for each feature in each class. Notice how these mean estimates match those for LDA and QDA above.

```{r}
head(predict(iris_nb, iris_trn)$class)
head(predict(iris_nb, iris_trn)$posterior)
```

```{r}
iris_nb_trn_pred = predict(iris_nb, iris_trn)$class
iris_nb_tst_pred = predict(iris_nb, iris_tst)$class
```

```{r}
calc_misclass(predicted = iris_nb_trn_pred, actual = iris_trn$Species)
calc_misclass(predicted = iris_nb_tst_pred, actual = iris_tst$Species)
```

```{r}
table(predicted = iris_nb_tst_pred, actual = iris_tst$Species)
```

Like LDA, naive Bayes is having trouble with virginica.

```{r, echo = FALSE}
classifiers = c("LDA", "LDA, Flat Prior", "QDA", "Naive Bayes")
train_err = c(
  calc_misclass(predicted = iris_lda_trn_pred,      actual = iris_trn$Species),
  calc_misclass(predicted = iris_lda_flat_trn_pred, actual = iris_trn$Species),
  calc_misclass(predicted = iris_qda_trn_pred,      actual = iris_trn$Species),
  calc_misclass(predicted = iris_nb_trn_pred,       actual = iris_trn$Species)
)
test_err = c(
  calc_misclass(predicted = iris_lda_tst_pred,      actual = iris_tst$Species),
  calc_misclass(predicted = iris_lda_flat_tst_pred, actual = iris_tst$Species),
  calc_misclass(predicted = iris_qda_tst_pred,      actual = iris_tst$Species),
  calc_misclass(predicted = iris_nb_tst_pred,       actual = iris_tst$Species)
)
results = data.frame(
  classifiers,
  train_err,
  test_err
)
colnames(results) = c("Method", "Train Error", "Test Error")
```

```{r, echo = FALSE}
knitr::kable(results)
```

Summarizing the results, we see that Naive Bayes is the worst of LDA, QDA, and NB for this data. So why should we care about naive Bayes?

The strength of Naive Bayes comes from its ability to handle a large number of features, $p$, even with a limited sample size $n$. Even with the naive independence assumption, Naive Bayes works rather well in practice. Also because of this assumption, we can often train naive Bayes where LDA and QDA may be impossible to train because of the large number of parameters relative to the number of observations.

Here naive Bayes doesn't get a chance to show its strength since LDA and QDA already perform well, and the number of features is low. The choice between LDA and QDA is mostly down to a consideration about the amount of complexity needed. (Also note that complexity within these models can also be altered by changing the features used. More features generally means a more flexible model.)

***

## Discrete Inputs

So far, we have assumed that all features are numeric. What happens with categorical features?

```{r}
# create "new" dataset
iris_trn_mod = iris_trn
# made Sepal.Width categorical
iris_trn_mod$Sepal.Width = factor(ifelse(iris_trn$Sepal.Width > 3,
                                  ifelse(iris_trn$Sepal.Width > 4,
                                         "Large", "Medium"),
                                  "Small"))
# check levels of factor
levels(iris_trn_mod$Sepal.Width)
```

Here we make a new dataset where `Sepal.Width` is categorical, with levels `Small`, `Medium`, and `Large`. We then try to train classifiers using only the sepal variables.

```{r}
NaiveBayes(Species ~ Sepal.Length + Sepal.Width, data = iris_trn_mod)$tables
```

Naive Bayes makes a somewhat obvious and intelligent choice to model the categorical variable as a multinomial. It then estimates the probability parameters of a multinomial distribution.

```{r}
lda(Species ~ Sepal.Length + Sepal.Width, data = iris_trn_mod)
```

LDA (and QDA) however creates dummy variables, here with `Large` as the reference level, then continues to model them as normally distributed. Not great, but better then not using a categorical variable.
