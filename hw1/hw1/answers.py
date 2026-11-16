r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**

1. **False.** A useful split must make both subsets representative of the same
distribution the model will face in deployment. A split that, for example, puts
all samples of one class (or all images of one type) in the test set, or that is
not shuffled when the data is ordered, gives a test set that does not reflect
the training distribution. The resulting test error is then a poor estimate of
the generalization error. The size of each subset also matters: a tiny test set
gives a noisy estimate, and a tiny train set gives a weak model.

2. **False.** Cross-validation is used to select hyperparameters / models, so it
must use only the training data (split into train and validation folds). If the
test set is used during CV, information from it leaks into our choices, and the
final test error is no longer an unbiased estimate of performance on unseen
data. The test set should be used only once, at the very end.

3. **True.** In each fold the model is evaluated on a validation fold it was not
trained on, so the validation error is an estimate of the error on unseen data.
Averaging the validation performance over the $k$ folds gives a lower-variance
proxy for the generalization error, which is what we use to compare
hyperparameter settings. (It is a proxy, not the true value: the final unbiased
estimate still comes from the held-out test set.)

4. **True.** Injecting noise into the labels (for example of a fraction of the
training samples) lets us check how sensitive the model is to label errors,
which exist in real data. A robust model's performance should degrade
gracefully, while a model that fits the noisy labels perfectly is memorizing
rather than learning the underlying pattern. This is a way to probe robustness
and over-fitting, not a way to improve accuracy on clean data.
"""

part1_q2 = r"""
**Your answer:**

**No, the approach is not justified.** By choosing $\lambda$ according to
performance on the test set, the friend is using the test set to train
(tune) the model: $\lambda$ is a hyperparameter, and selecting it is part of the
learning process. The chosen $\lambda$ is therefore fitted to that particular
test set, and the reported test performance becomes an optimistically biased
estimate of the generalization error. The test set is no longer "unseen" data.

The correct approach is to select $\lambda$ using a **validation set** taken from
the training data, or with **k-fold cross-validation** on the training set:
train with each candidate $\lambda$ on the training folds, evaluate on the
validation fold, pick the $\lambda$ with the best average validation score,
retrain on the full training set with that $\lambda$, and only then evaluate
once on the test set.
"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**

The hinge term for sample $i$ and wrong class $j$ is
$\max(0, \Delta + \vectr{w_j}\vec{x_i} - \vectr{w_{y_i}}\vec{x_i})$. It is
zero whenever the correct-class score exceeds the wrong-class score by at least
$\Delta$: $s_{y_i} - s_j \geq \Delta$.

If $\Delta < 0$, this condition holds even when $s_j > s_{y_i}$, as long as the
wrong class wins by less than $|\Delta|$. So **misclassified samples can incur
zero loss**: the margin no longer asks the correct class to win, only to "not
lose by too much".

Combined with the regularization term this becomes degenerate. Take
$\mat{W} = 0$: all scores are $0$, so every margin term is
$\max(0, \Delta + 0) = 0$ (since $\Delta < 0$), and the regularization term
$\frac{\lambda}{2}\|\mat{W}\|^2$ is also $0$. The total loss is $0$, which is
the global minimum because the loss is non-negative. So minimizing the loss
drives the weights to the trivial solution $\mat{W}=0$ (or anything with
small enough weights), and the classifier learns nothing useful. In general,
the hinge loss stops pushing towards correct classification, and the
regularization simply shrinks the weights towards zero.
"""

part2_q2 = r"""
**Your answer:**

Each row $\vec{w_j}$ of the weight matrix, reshaped to the input image size,
acts as a **template** for class $j$. The score of class $j$ is the dot product
$\vectr{w_j}\vec{x}$. Bright (positive) weights are where strokes of digit $j$
usually appear, so ink there raises the score; dark (negative) weights are
where strokes of other digits usually appear, so ink there lowers the score.
In the images we can see a blurry "average" shape of each digit (for example,
the template for 0 is a ring), because the model learns roughly the average
picture of each class.

The linear model is therefore doing **template matching**: it learns, per
class, which pixel locations should be on and which should be off. It cannot
represent the different ways a digit can be written (it has one template per
class), and it is sensitive to the position, thickness and slant of the
strokes, since it compares pixel by pixel.

This explains the errors we got: a sample is misclassified when its strokes
overlap another class's template more than its own. In our results, a 9 with a
slanted, open top was classified as 4, a 7 as 9 (both have a stroke across the
top and a long diagonal down), a 5 as 6 (its lower loop is closed, like a 6),
and a 6, a 4 and a 2 written in unusual or slanted shapes were classified as
2, 6 and 7. In each case the digit is written in a way that does not match the
"average" shape of its class, and the model has only one template per class.
"""

part2_q3 = r"""
**Your answer:**

1. **Good.** The training loss drops very quickly in the first epoch (from about
$2.4$ to about $0.8$) and then keeps decreasing more and more slowly, flattening
out smoothly (to about $0.35$ on train and $0.46$ on validation) without
oscillations or spikes. So training has converged within the given number of
epochs.
   - With a **learning rate that is too low**, the loss would decrease very
   slowly and almost linearly, and would still be clearly decreasing (far from
   converged) at the end of the same number of epochs.
   - With a **learning rate that is too high**, the loss would be noisy and
   oscillate or jump around, possibly increase or diverge, and would not
   settle into a smooth minimum, because each step overshoots the minimum.

2. **Slightly overfitted to the training set.** At the end of training the
accuracy is about $92.5\%$ on the training set, about $91\%$ on the validation
set and $89.0\%$ on the test set. The model does a little better on the data it
was trained on than on unseen data, but the gap is small (a few percentage
points), and the gap between the train and validation curves stays small and
stable over the epochs. If the model were highly overfitted
we would see a large gap, with test accuracy stagnating or dropping while
train accuracy keeps rising. If it were underfitted, both accuracies would be
low and still improving, with test accuracy close to or equal to train
accuracy.
"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**

The ideal residual plot shows the residuals $e^{(i)} = y^{(i)} - \hat{y}^{(i)}$
**randomly scattered around the horizontal line $e=0$**, in a narrow band of
roughly constant width across all predicted values $\hat{y}$, with no visible
pattern (no curve, no funnel shape, no clusters). This means the errors are
small, unbiased, and do not depend on the prediction, so the model has captured
the structure in the data and what remains is noise.

In the plot for the **top-5 features** model ($MSE=27.20$, $R^2=0.68$), the
residuals are spread fairly widely (the $\pm\sigma$ band is about $\pm 5$) and
they are not random: the errors depend on $\hat{y}$. At high predicted prices
($\hat{y}\approx 35$-$42$) the points form a straight diagonal line of large
errors, and there are a few very large errors (about $30$) around
$\hat{y}\approx 20$. These are mostly the houses whose price is capped at the
maximum value ($50$) in the dataset, which the model strongly under-predicts.
This structure shows that a linear function of those 5 features cannot capture
the non-linear relationships in the data, so the model underfits.

In the **final plot after adding non-linear features and selecting
hyperparameters with CV** (best: degree $2$, $\lambda\approx 0.43$), the fit is
much better: train $MSE=7.82$, $R^2=0.91$ and test $MSE=14.01$, $R^2=0.80$.
The residuals are much closer to zero (the band is about $\pm 3$), more evenly
scattered around $e=0$ over the whole range of $\hat{y}$, and the train and test
points are mixed in the same band, so the model generalizes reasonably well.
The test MSE is higher than the train MSE, but most of that gap comes from a
single test outlier with a residual of about $24$ (it alone adds about $5.6$ to
the test MSE over $102$ test samples). Without it the test error is close to
the train error, so the model is not strongly over-fitting. A few large
residuals remain, again mainly for the capped high-price houses.
"""

part3_q2 = r"""
**Your answer:**

1. **Yes, it is still a linear regression model.** "Linear" refers to linearity
in the **parameters** $\vec{w}$, not in the original features. After the
transformation $\vec{x} \mapsto \phi(\vec{x})$ the model is
$\hat{y} = \vectr{w}\phi(\vec{x}) + b$, which is linear in $\vec{w}$ and in the
new features $\phi(\vec{x})$. The loss is still a quadratic function of
$\vec{w}$ and we solve it with the same closed-form solution. Only the
relationship between $\hat{y}$ and the *original* features is non-linear.

2. **Not any function, in practice.** We can only fit functions that are linear
combinations of the features we chose to add (e.g. polynomials up to the chosen
degree, logs, products). A function outside that span (e.g. $\sin$ of a feature
when we only added polynomials) can at best be approximated. In theory, with
enough well-chosen basis functions (for example high-degree polynomials) we can
approximate any continuous function on a bounded domain, but the number of
features grows very quickly with the degree and the number of original
features, which increases computation and the risk of over-fitting. We also
have to know or guess the right features in advance; this is exactly the
limitation that deep learning addresses by learning the features.

3. In the **new feature space** $\phi(\vec{x})$ the decision boundary
$\vectr{w}\phi(\vec{x}) + b = 0$ is **still a hyperplane**, because the
classifier is linear in the transformed features. But in the **original
feature space** the boundary is generally **not a hyperplane**: it is the set of
points satisfying a non-linear equation in $\vec{x}$ (e.g. with quadratic
features it is a quadric surface, such as a circle, ellipse or parabola in 2D).
So adding non-linear features allows the linear classifier to separate data
that is not linearly separable in the original space.
"""

part3_q3 = r"""
**Your answer:**

**1.** Let $x, y \sim \text{Uniform}(0,1)$ be independent, so their joint density
is $1$ on the unit square. By symmetry, the regions $y < x$ and $y > x$
contribute equally:

$$
\mathbb{E}_{x,y}[|y-x|]
= \int_0^1\int_0^1 |y-x| \, dy\, dx
= 2\int_0^1 \int_0^x (x-y)\, dy\, dx
= 2\int_0^1 \frac{x^2}{2}\, dx
= \int_0^1 x^2 \, dx
= \frac{1}{3}.
$$

**2.** Fix the generated value $\hat{x}$ and assume $\hat{x}\in[0,1]$ (the support
of the target). Split the integral at $\hat{x}$:

$$
\mathbb{E}_{x}[|\hat{x}-x|]
= \int_0^{\hat{x}} (\hat{x}-x)\, dx + \int_{\hat{x}}^1 (x-\hat{x})\, dx
= \frac{\hat{x}^2}{2} + \frac{(1-\hat{x})^2}{2}
= \hat{x}^2 - \hat{x} + \frac{1}{2}.
$$

(Sanity check: averaging over $\hat{x}\sim U(0,1)$ gives
$\frac{1}{3} - \frac{1}{2} + \frac{1}{2} = \frac{1}{3}$, matching part 1.)

So the loss is
$L_{\text{ED}} = 2\left(\hat{x}^2 - \hat{x} + \frac{1}{2}\right) = 2\hat{x}^2 - 2\hat{x} + 1$.

**3.** The constant term of the polynomial ($\frac{1}{2}$, or $1$ after
multiplying by $2$) does not depend on $\hat{x}$, and therefore not on the
generator's parameters. Training only uses the **gradient** of the loss with
respect to the parameters, and the derivative of a constant is $0$:
$\frac{d}{d\hat{x}}(2\hat{x}^2 - 2\hat{x} + 1) = 4\hat{x} - 2$, the same as for
$2\hat{x}^2 - 2\hat{x}$. Adding or removing a constant shifts the loss value but
does not change its minimizer or the optimization steps, so we can drop it.
(For the same reason the full energy distance term $\mathbb{E}[|x-x'|] = \frac{1}{3}$,
which depends only on the data, can be dropped. Likewise, a positive overall
scale factor like the $2$ only rescales the gradient, which is equivalent to
changing the learning rate, and does not change the minimizer.)

Note: minimizing $\hat{x}^2 - \hat{x}$ gives $\hat{x} = \frac{1}{2}$: a
deterministic generator trained only on this term would always output the
mean (median) of the data, not samples spread over $[0,1]$. The full energy
distance also includes the term $-\mathbb{E}[|\hat{x}-\hat{x}'|]$, which rewards
diversity among generated samples and prevents this collapse.
"""

# ==============

# ==============
