---
title: Linear Regression
description: ML fundamentals 2
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

## Explanation versus Prediction

Before we even begin to discuss regression, we make a bold announcement: **STAT 432 is not a course about inference.** It is very possible that there will be **zero** causal claims in this book. While it would certainly be nice (but extremely difficult) to uncover causal relationships, our focus will be on predictive relationships.

Suppose (although it is likely untrue) that there is a strong correlation between wearing a wrist watch, and car accidents. Depending on your frame of reference, you should view this information in very different ways.

- Suppose you are a car insurance company. This is great news! You can now more accurately predict the number of accidents of your policy holders if you know whether or not they wear a wrist watch. For the sake of understanding how much your company will need to pay out in a year, you don't care what *causes* accidents, you just want to be able to **predict** (estimate) the number of accidents.
- Suppose you are a car driver. As a driver, you want to stay safe. That is, you want to do things that decrease accidents. In this framing, you care about things that **cause** accidents, not things that *predict* accidents. In other words, this correlation information should **not** lead to you throwing away your wrist watch.

*Disclaimer:* Extremely high correlation should not simply be ignored. For example, there is a very high correlation between smoking and lung cancer. (Fun fact: [RA Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher), the most famous statistician, did not believe that smoking caused cancer. It's actually a part of a larger [fasinating story](https://rss.onlinelibrary.wiley.com/doi/full/10.1111/j.1740-9713.2014.00765.x).) However, this strong correlation is not proof that smoking causes lung cancer. Instead, additional study is needed to rule out confounders, establish mechanistic relationships, and more.

## Setup

We now introduce the **regression** task. Regression is a subset of a broader machine learning tasks called *supervised learning*, which also include *classification*. (We will return later to discuss supervised learning in general after getting through some specifics of regression and classification.)

Stated simply, the regression tasks seeks to estimate (predict) a **numeric** quantity. For example:

- Estimating the **salary** of a baseball player.
- Estimating the **price** of a home for sale.
- Estimating the **credit score** of a bank customer,
- Estimating the number of **downloads** of a podcast.

Each of these quantities is some numeric value. The goal of regression is to estimate (predict) these quantities when they are unknown through the use of additional, possibly correlated quantities, for example the offensive and defensive statistics of a baseball player, or the location and attributes of a home.

## Mathematical Setup

To get a better grasp of what regression is, we move to defining the task mathematically. Consider a random variable $Y$ which represents a **response** (or outcome or target) variable, and $p$ **feature** variables $\boldsymbol{X} = (X_1, X_2, \ldots, X_p)$. Features are also called covariates or predictors. (We find the "predictors" nomenclature to be problematic when discussing prediction tasks.)

In the most common regression setup, we assume that the response variable $Y$ is some function of the features, plus some random noise.

$$
Y = f(\boldsymbol{X}) + \epsilon
$$

- We call $f(\boldsymbol{X})$ the **signal**. This $f$ is the function that we would like to *learn*.
- We call $\epsilon$ the **noise**. We do not want to learn this which we risk if we overfit. (More on this later.)

So our goal will be to find some $f$ such that $f(\boldsymbol{X})$ is close to $Y$. But how do we define close? There are many ways but we will start with, and most often consider, squared error loss. Specifically, we define a loss function,

$$
L(Y, f(\boldsymbol{X})) \triangleq \left(Y - f(\boldsymbol{X})\right) ^ 2
$$

Now we can clarify the goal of regression, which is to minimize the above loss, *on average*. We call this the **risk** of estimating $Y$ using $f(\boldsymbol{X})$.

$$
R(Y, f(\boldsymbol{X})) \triangleq \mathbb{E}[L(Y, f(\boldsymbol{X}))] = \mathbb{E}_{\boldsymbol{X}, Y}[(Y - f(\boldsymbol{X})) ^ 2]
$$

Before attempting to minimize the risk, we first re-write the risk after conditioning on $\boldsymbol{X}$.

$$
\mathbb{E}_{\boldsymbol{X}, Y} \left[ (Y - f(\boldsymbol{X})) ^ 2 \right] = \mathbb{E}_{\boldsymbol{X}} \mathbb{E}_{Y \mid \boldsymbol{X}} \left[ ( Y - f(\boldsymbol{X}) ) ^ 2 \mid \boldsymbol{X} = \boldsymbol{x} \right]
$$

Minimizing the right-hand side is much easier, as it simply amounts to minimizing the inner expectation with respect to $Y \mid \boldsymbol{X}$, essentially minimizing the risk pointwise, for each $\boldsymbol{x}$.

It turns out, that the risk is minimized by the **conditional mean** of $Y$ given $\boldsymbol{X}$,

$$
\mu(\boldsymbol{x}) \triangleq \mathbb{E}[Y \mid \boldsymbol{X} = \boldsymbol{x}]
$$

which we call the **regression function**. (This is not a learned function, this is the function we would like to learn in order to minimize the squared error loss on average. $f$ is any function, $\mu$ is the function that would minimize squared error loss on average if we knew if, but will instead need to learn it form the data.

Note that $\boldsymbol{x}$ represents (potential) realized values of the random variables $\boldsymbol{X}$.

$$
\boldsymbol{x} = (x_1, x_2, \ldots, x_p)
$$

We can now state the goal of the regression task: we want to **estimate** the **regression function**. How do we do that?

## Linear Regression Models

What do linear regression models **do**? They estimate the conditional mean of $Y$ given $\boldsymbol{X}$! (How convenient.)

Consider the following probability model

$$
Y = 1 - 2x - 3x ^ 2 + 5x ^ 3 + \epsilon
$$

where $\epsilon \sim \text{N}(0, \sigma^2)$.

Alternatively we could write

$$
Y \mid X \sim \text{N}(1 - 2x - 3x ^ 2 + 5x ^ 3, \sigma^2)
$$

This perhaps makes it clearer that

$$
\mu(x) = \mathbb{E}[Y \mid \boldsymbol{X} = \boldsymbol{x}] = 1 - 2x - 3x ^ 2 + 5x ^ 3
$$

What do linear models do? More specifically than before, linear regression models estimate the conditional mean of $Y$ given $$\boldsymbol{X}$$ by assuming this conditional mean is a **linear combination of the feature variables**.

Suppose for a moment that we did not know the above **true** probability model, or even the more specifically the regression function. Instead, all we had was some data, $$(x_i, y_i)$$ for $$i = 1, 2, \ldots, n$$.

How do we fit (or "train" in ML language) a linear model with this data? In order words, how to be learn the regression function from this data with a linear regression model?

First, we need to make assumptions about the *form* of the regression function, up to, but **not** including some unknown parameters. Consider three possible linear models, in particular, three possible regression functions.

**Degree 1 Polynomial**

$$
\mu(x) = \beta_0 + \beta_1 x
$$

**Degree 3 Polynomial**

$$
\mu(x) = \beta_0 + \beta_1 x + \beta_2 x^2 + \beta_3 x^3
$$

**Degree 9 Polynomial**

$$
\mu(x) = \beta_0 + \beta_1 x + \beta_2 x^2 + \beta_3 x^3 + \ldots + \beta_9 x^9
$$

These are chosen mostly arbitrarily for illustrative purposes which we'll see in a moment.

So how do we actually **fit** these models, that is train them, with the given data. We have a couple of options: Maximum Likelihood or **Least Squares**! In this case, they actually produce the same result, so we use least squares for simplicity of explanation.

To fit the degree 3 polynomial using least squares, we *minimize*

$$
\sum_{i = 1}^{n}\left(y_i - (\beta_0 + \beta_1 x_i + \beta_2 x_i^2 + \beta_3 x_i^3)\right) ^ 2
$$

Skipping the details of the minimization, we would acquire $$\hat{\beta}_0$$, $$\hat{\beta}_1$$, $$\hat{\beta}_2$$, and $$\hat{\beta}_3$$ which are estimates of $${\beta}_0$$, $${\beta}_1$$, $${\beta}_2$$, and $${\beta}_3$$.

Taken together, we would have

$$
\hat{\mu}(x) = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \hat{\beta}_2 x_2^2 + \hat{\beta}_3 x_3^3
$$

which is then an estimate of $$\mu(x)$$.

While in this case, it will almost certainly not be the case that $$\hat{\beta}_0 = 1$$ or $$\hat{\beta}_1 = -2$$ or $$\hat{\beta}_2 = -3$$ or $$\hat{\beta}_3 = 5$$, which are the true values of the $$\beta$$ coefficients, they are at least reasonable estimates.

As a bit of an aside, note that in this case, it is sort of ambiguous as to whether there is one feature, $x$, which is seen in the data, or three features $$x$$, $$x^2$$, and $$x^3$$, which are seen in the model. The truth is sort of in the middle. The data has a single feature, but through feature engineering, we have created two additional features for fitting the model. Note that when using R, **you do not need to modify the data to do this**, instead you should use R's formula syntax to specify this feature engineering when fitting the model. More on this when we discuss the `lm()` function in R. (We introduce this somewhat confusing notion early so we can emphasize that linear models are about linear combinations of features, not necessarily linear relationships. Although, linear models are very good at learning linear relationships.)

Suppose instead we had assumed that

$$
\mu(x) = \beta_0 + \beta_1 x
$$

This model is obviously flawed as it doesn't contain enough terms to capture the true regression function. (Later we will say this model is not "flexible" enough.)

Or, suppose we had assumed

$$
\mu(x) = \beta_0 + \beta_1 x + \beta_2 x^2 + \beta_3 x^3 + \ldots + \beta_9 x^9
$$

This model is also flawed, but for a different reason. (Later we will say this model is too "flexible.") After using least squares, we will obtain some $\hat{\beta}_9$ even though there is not a 9th degree term in the true regression function!

Here we see the three models fit to the data above. The dashed black curve is the true mean function, that is the true mean of $$Y$$ given $$x$$, and the solid colored curves are the estimated mean functions.

Now we ask the question: which of these models is best? Given these pictures, there are two criteria that we could consider.

- How close is the estimated regression (mean) function to the data? (Degree 9 is best! There is no error!)
- How close is the estimated regression (mean) function to the true regression (mean) function? (Degree 3 is best.)

From the presentation here, it's probably clear that the latter is actually what matters. We can demonstrate this by generating some "new" data.

These plots match the plots above, except newly simulated data is shown. (The regression functions were still estimated with the previous data.) Note that the degree 3 polynomial matches the data about the same as before. The degree 9 polynomial now correctly predicts none of the new data and makes some **huge** errors.

We will define these concepts more generally later, but for now we note that:

- The Degree 9 Polynomial is **overfitting**. It performs well on the data used to fit the model, but poorly on new data.
- The Degree 1 Polynomial is **underfitting**. It performs poorly on the data used to fit the model and poorly on new data.

There's a bit of a problem though! In practice, we don't know the true mean function, and we don't have the magical ability to simulate new data! Yikes! After we discuss a bit about how to fit these models in R, we'll return to this issue. (Spoiler: Don't fit the model to all the available data. Pretend the data you didn't use is "new" when you evaluate models.)


A warning: **Do not _name_ the second argument to the predict function.** This will cause issues because sometimes the name of that argument is `newdata`, as it is here, but sometimes it is `data`. If you use the wrong name, bad things will happen. It is safer to simply never name this argument. (However, in general, arguments after the first should be named. The `predict()` function is the exception.)

## Data Splitting

(Note: Many readers will have possibly seen some machine learning previously. **For now, please pretend that you have never heard of or seen cross-validation**. Cross-validation will clutter the initial introduction of many concepts. We will return to and formalize it later.)

OK. So now we can fit models, and make predictions (create estimates of the conditional mean of $Y$ given values of the features), how do we evaluate how well our models perform, **without** knowing the true model!

First, let's state a somewhat specific goal. We would like to train models that **generalize** well, that is, perform well on "new" or "unseen" data that was **not** used to train the model.

To accomplish this goal, we'll just "create" a dataset that isn't used to train the model! To create it, we will just split it off. (We'll actually do so twice.)

First, denote the *entire* available data as $\mathcal{D}$.

$$
\mathcal{D} = \{ (x_i, y_i) \in \mathbb{R}^p \times \mathbb{R}, \ i = 1, 2, \ldots n \}
$$

We first split this data into a **train** and **test** set. We will discuss these two dataset ad nauseam, but let's set two rules right now.

- You can do **whatever** you would like with the training data.
  - However, it is best used to train, evaluate, and select models.
- **Do not, ever, for any reason, fit a model using test data!**
  - Additionally, you should not **select** models using test data.
  - In STAT 432, we will only use test data to provide a final estimate of the generalization error of a chosen model. (Much more on this along the way.)

Again, **do not, ever, for any reason, fit a model using test data!** I repeat: **Do not, ever, for any reason, fit a model using test data!** (You've been warned.)

To perform this split, we will *randomly* select some observations for the train (`trn`) set, the remainder will be used for the test (`tst`) set.

$$
\mathcal{D} = \mathcal{D}_{\texttt{trn}} \cup \mathcal{D}_{\texttt{tst}}
$$

As a general guiding heuristic, use 80% of the data for training, 20% for testing.

In addition to the train-test split, we will further split the train data into **estimation** and **validation** sets. These are somewhat confusing terms, developed for STAT 432, but hear us out.

To perform this split, we will *randomly* select some observations (from the train set) for the estimation (`est`) set, the remainder will be used for the validation (`val`) set.

$$
\mathcal{D}_{\texttt{trn}} = \mathcal{D}_{\texttt{est}} \cup \mathcal{D}_{\texttt{val}}
$$

Again, use 80% of the data for estimation, 20% for validation.

The need for this second split might not become super clear until later on, but the general idea is this:

- Fit a bunch of candidate models to the **estimation** data. (Think of this as the data to *estimate* the model parameters. That's how we chose the name.)
- Using these candidate models, evaluate how well they perform using the **validation** data.
- After evaluating and picking a single model, re-fit this model to the entire **training** dataset.
- Provide an estimate of how well this model performs using the **test** data.

Now that we have data for estimation, and validation, we need some **metrics** for evaluating these models.

## Regression Metrics

If our goal is to "predict" then we want small errors. In general there are two types of errors we consider:

- Squared Errors: $$(y_i - \hat{\mu}(\boldsymbol{x}_i)) ^2$$

- Absolute Errors: $$|y_i - \hat{\mu}(\boldsymbol{x}_i)|$$

In both cases, we will want to consider the average errors made. We define two metrics.

**Root Mean Square Error** (RMSE)

$$
\text{rmse}\left(\hat{f}_{\texttt{set_f}}, \mathcal{D}_{\texttt{set_D}} \right) = \sqrt{\frac{1}{n_{\texttt{set_D}}}\displaystyle\sum_{i \in {\texttt{set_D}}}^{}\left(y_i - \hat{f}_{\texttt{set_f}}({x}_i)\right)^2}
$$

**Mean Absolute Error** (MAE)

$$
\text{mae}\left(\hat{f}_{\texttt{set_f}}, \mathcal{D}_{\texttt{set_D}} \right) = \frac{1}{n_{\texttt{set_D}}}\displaystyle\sum_{i \in {\texttt{set_D}}}^{}\left|y_i - \hat{f}_{\texttt{set_f}}({x}_i)\right|
$$

- $\hat{f}_{\texttt{set_f}}$ is a function $f$ estimated using a model fit to some dataset $\texttt{set_f}$.
- The $(x_i, y_i)$ are data from dataset $\mathcal{D}_{\texttt{set_D}}$.

For both, smaller is better. (Less error on average.) In both, we note both the data that the model was fit to, as well as the data the model is evaluated on.

Depending on the data used for these different sets, we "define" different metrics. For example, for RMSE, we have:

**Train RMSE**: Evaluate a model fit to estimation data, using estimation data.

$$
\text{RMSE}_{\texttt{trn}} = \text{rmse}\left(\hat{f}_{\texttt{est}}, \mathcal{D}_{\texttt{est}}\right) = \sqrt{\frac{1}{n_{\texttt{est}}}\displaystyle\sum_{i \in {\texttt{est}}}^{}\left(y_i - \hat{f}_{\texttt{est}}({x}_i)\right)^2}
$$

**Validation RMSE**: Evaluate a model fit to estimation data, using validation data.

$$
\text{RMSE}_{\texttt{val}} = \text{rmse}\left(\hat{f}_{\texttt{est}}, \mathcal{D}_{\texttt{val}}\right) = \sqrt{\frac{1}{n_{\texttt{val}}}\displaystyle\sum_{i \in {\texttt{val}}}^{}\left(y_i - \hat{f}_{\texttt{est}}({x}_i)\right)^2}
$$

**Test RMSE**: Evaluate a model fit to training data, using test data.

$$
\text{RMSE}_{\texttt{tst}} = \text{rmse}\left(\hat{f}_{\texttt{trn}}, \mathcal{D}_{\texttt{tst}}\right) = \sqrt{\frac{1}{n_{\texttt{tst}}}\displaystyle\sum_{i \in {\texttt{tst}}}^{}\left(y_i - \hat{f}_{\texttt{trn}}({x}_i)\right)^2}
$$

For the rest of this chapter, we will largely ignore train error. It's a bit confusing, since it doesn't use the full training data! However, think of training error this way: training error evaluates how well a model performs on the data used to fit the model. (This is the general concept behind "training error." Others might simply call the "estimation" set the training set. We use "estimation" so that we can reserve "train" for the full training dataset, not just the subset use to initially fit the model.)

Let's return to the `sim_mlr_data` data and apply these splits and metrics to this data.

```{r}
# test-train split
mlr_trn_idx = sample(nrow(sim_mlr_data), size = 0.8 * nrow(sim_mlr_data))
mlr_trn = sim_mlr_data[mlr_trn_idx, ]
mlr_tst = sim_mlr_data[-mlr_trn_idx, ]
```

Here we randomly select 80% of the rows of the full data, and store these indices as `mlr_trn_idx`. We then create the `mlr_trn` and `mlr_tst` datasets by either selecting or anti-selecting these rows from the original dataset.

```{r}
# estimation-validation split
mlr_est_idx = sample(nrow(mlr_trn), size = 0.8 * nrow(mlr_trn))
mlr_est = mlr_trn[mlr_est_idx, ]
mlr_val = mlr_trn[-mlr_est_idx, ]
```

We then repeat the process from above within the train data.

Now, let's compare `mod_3` and `mod_4`. To do so, we first fit both models to the estimation data.

```{r}
mod_3_est = lm(y ~ ., data = mlr_est)
mod_4_est = lm(y ~ x1 + I(sin(x2)) + I(x3 ^ 3) + x4, data = mlr_est)
```

We then calculate the validation error for both. Because we will do it so often, we go ahead and write a function to calculate RMSE, given vectors of the actual values (from the data used to evaluate) and the predictions from the model.

```{r}
calc_rmse = function(actual, predicted) {
  sqrt(mean((actual - predicted) ^ 2))
}
```

```{r}
# calculate validation RMSE, model 3
calc_rmse(actual = mlr_val$y,
          predicted = predict(mod_3_est, mlr_val))
```

```{r}
# calculate validation RMSE, model 4
calc_rmse(actual = mlr_val$y,
          predicted = predict(mod_4_est, mlr_val))
```

Here we see that `mod_4_est` achieves a lower validation error, so we move forward with this model. We then refit to the full train data, then evaluate on test.

```{r}
mod_4_trn = lm(y ~ x1 + I(sin(x2)) + I(x3 ^ 3) + x4, data = mlr_trn)
```

```{r}
# calculate test RMSE, model 4
calc_rmse(actual = mlr_tst$y,
          predicted = predict(mod_4_trn, mlr_tst))
```

We ignore the validation metrics. (We already used them for selecting a model.) This test RMSE is our estimate of how well our selected model will perform on unseen data, on average (in a squared error sense).

Note that for selecting a model there is no difference between MSE and RMSE, but for the sake of understanding, RMSE has preferential units, the same units as the response variables. (Whereas MSE has units squared.) We will always report RMSE.
